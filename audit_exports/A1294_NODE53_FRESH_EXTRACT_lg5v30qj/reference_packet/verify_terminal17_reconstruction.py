from __future__ import annotations
import hashlib, importlib.util, json, struct, sys, zipfile
from fractions import Fraction as F
from pathlib import Path
ROOT = Path(__file__).resolve().parent
V2ROOT = ROOT / 'reference' / 'v2_source' / 'A1294_SOURCE_FREE_REPLAY_PACKAGE_V2'
V2ZIP = ROOT / 'reference' / 'predecessor' / 'A1294_CATALOG18_IDENTITY_20261105' / 'reference' / 'input' / 'A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip'
INPUT = ROOT / 'terminal17_authentic_input.json'
EXPECTED_ZIP = '3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5'
def require(ok, msg):
    if not ok:
        raise RuntimeError(msg)
def sha(data): return hashlib.sha256(data).hexdigest()
def qs(x): return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'
require(sha(V2ZIP.read_bytes()) == EXPECTED_ZIP, 'V2 ZIP hash')
with zipfile.ZipFile(V2ZIP) as zf:
    require(zf.testzip() is None, 'V2 ZIP CRC')
    pref='A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/'
    pm=json.loads(zf.read(pref+'PACKAGE_MANIFEST.json'))
    for rel,meta in pm['files'].items():
        b=zf.read(pref+rel)
        require(len(b)==meta['bytes'] and sha(b)==meta['sha256'], f'V2 package manifest: {rel}')
cert=V2ROOT/'certificate'; data=V2ROOT/'data'
man=json.loads((cert/'manifest.json').read_text())
streams={k:cert/f for k,f in [('topology','topology-u8.bin'),('kinds','terminal-kinds-u8.bin'),('anchors','anchors-u16le.bin')]}
catalog_paths={'stable':data/'macro-data-exact.json','v1':data/'refinement-catalog-v1-exact.json','v3':data/'refinement-catalog-v3.json'}
for k,p in streams.items(): require(sha(p.read_bytes())==man['stream_sha256'][k],f'stream hash {k}')
for k,p in catalog_paths.items(): require(sha(p.read_bytes())==man['input_sha256'][k],f'catalog hash {k}')
spec=importlib.util.spec_from_file_location('a1294_v2_replay_independent',V2ROOT/'replay_a1294_source_free.py')
mod=importlib.util.module_from_spec(spec); sys.modules[spec.name]=mod; spec.loader.exec_module(mod)
top=streams['topology'].read_bytes(); kinds=streams['kinds'].read_bytes(); anchors=streams['anchors'].read_bytes()
require(list(top[55:68])==[1,0,5,0,3,0,2,0,4,0,1,0,0], 'topology 55..67')
# Independently replay only the bounded DFS prefix, validating each prescribed weighted split.
pending=[([(F(0),F(60)) for _ in range(5)],[])]
term=0; nodes={}
for ni,tok in enumerate(top[:68]):
    require(bool(pending),f'DFS stack empty at node {ni}')
    box,path=pending.pop()
    nodes[ni]=(box,path,tok,term if tok==0 else None)
    if tok==0:
        term+=1; continue
    require(1<=tok<=5,f'bad split token {tok} at {ni}')
    widths=[(box[i][1]-box[i][0])*mod.WEIGHTS[i] for i in range(5)]
    axis=max(range(5),key=widths.__getitem__)
    require(tok==axis+1,f'weighted split selection at {ni}')
    lo,hi=box[axis]; mid=(lo+hi)/2
    lb=list(box); rb=list(box); lb[axis]=(lo,mid); rb[axis]=(mid,hi)
    pending.append((rb,path+[(axis,'R')]))
    pending.append((lb,path+[(axis,'L')]))
require(nodes[55][2]==1 and nodes[56][2]==0 and nodes[56][3]==17,'node/terminal ordinals')
require(nodes[56][1]==nodes[55][1]+[(0,'L')], 'terminal 17 left path')
require(nodes[57][1]==nodes[55][1]+[(0,'R')], 'node 57 right path')
require(kinds[17]==1 and list(kinds[17:24])==[1]*7,'terminal kinds')
anchor_offset=10*sum(k==1 for k in kinds[:17])
codes=struct.unpack_from('<5H',anchors,anchor_offset)
require(codes==(0,0,0,0,0),'terminal 17 anchor codes')
leaf=nodes[56][0]; parent=nodes[55][0]
conv=lambda box:[[qs(lo),qs(hi)] for lo,hi in box]
record=json.loads(INPUT.read_text(encoding='utf-8-sig'))
leafrec=record['children']['left']; parentrec=record['parent']
require(conv(parent)==parentrec['box_exact'],'node 55 box')
require(conv(leaf)==leafrec['box_exact'],'node 56 box')
require(leafrec['anchor_stream_byte_offset']==anchor_offset,'anchor offset')
require(leafrec['anchor_codes_u16le']==list(codes),'serialized anchor')
require(leafrec['anchor_coordinates_exact']==[qs(a) for a,_ in leaf],'anchor coordinates')
raw=[json.loads(p.read_text(encoding='utf-8'))['pieces'] for p in catalog_paths.values()]
def source_piece(ix):
    if ix<56: return raw[0][ix],f'macroPiece{ix}'
    if ix<272: return raw[1][ix-56],f'refinementPiece{ix-56}'
    return raw[2][ix-272],f'refinement2Piece{ix-272}'
catalog=mod.ExactCatalog(catalog_paths['stable'],catalog_paths['v1'],catalog_paths['v3'],mod.Q(man['A']),mod.Q(man['B']))
def expected_segments(lo,hi):
    end=min(hi,catalog.cutoff)
    if end<=lo: return []
    bounds={lo,end}
    first=catalog.stable_owner(lo); last=catalog.stable_owner(min(end,F(59)))
    for owner in range(max(0,first-1),min(55,last+1)+1):
        bounds.update(x for x in catalog.group_boundaries[owner] if lo<x<end)
    bounds.update(x for x in catalog.group_boundaries[-1] if lo<x<end)
    ordered=sorted(bounds); out=[]
    for sl,sh in zip(ordered,ordered[1:]):
        piece=catalog.strongest_full_cover(sl,sh)
        if piece is None:
            candidates=[p for group in catalog.groups.values() for p in group if p.lo<=sl and sh<=p.hi]
            require(bool(candidates),f'coverage gap [{sl},{sh}]')
            piece=max(candidates,key=lambda p:(mod.interval_infimum(p,sl,sh),-p.idx))
        item,name=source_piece(piece.idx)
        out.append({'segment':[qs(sl),qs(sh)],'catalog_index_zero_based':piece.idx,'declaration':name,
                    'owner_index':piece.owner,'source_item':item,'model_infimum':qs(mod.interval_infimum(piece,sl,sh))})
    return out
partials=mod.PARTIALS
require(len(leafrec['fifteen_models'])==15,'fifteen rows')
seg_total=0; refs=[]
for j,row in enumerate(leafrec['fifteen_models']):
    require(row['pair_index_zero_based']==j,'row index')
    a,b=partials[j]
    dlo=sum((leaf[i][0] for i in range(a,b+1)),F(0)); dhi=sum((leaf[i][1] for i in range(a,b+1)),F(0))
    require(row['distance_interval']==[qs(dlo),qs(dhi)],f'row {j} exact distance interval')
    clip=min(dhi,catalog.cutoff)
    direct=catalog.strongest_full_cover(dlo,clip) if dlo<=clip else None
    use_seg=direct is None
    if direct is not None and direct.idx<56 and catalog.groups.get(direct.owner):
        scalar=catalog.segmented_scalar_lower(dlo,dhi)
        dl=mod.interval_infimum(direct,dlo,clip)
        use_seg=scalar>dl
    require(row['kind']==('segmented_constant' if use_seg else 'direct_piece'),f'row {j} selection kind')
    if use_seg:
        scalar=catalog.segmented_scalar_lower(dlo,dhi)
        require(row['base']==qs(scalar),f'row {j} exact segmented scalar')
        exp=expected_segments(dlo,dhi)
        require(row['segments']==exp,f'row {j} selected segment list')
        prev=dlo
        for s in exp:
            lo,hi=map(lambda x:F(x),s['segment'])
            require(lo==prev and lo<hi,f'row {j} contiguous endpoints')
            prev=hi; refs.append(s['catalog_index_zero_based'])
        require(prev==min(dhi,catalog.cutoff),f'row {j} coverage endpoint')
        require(row['weight']=='0' and row['offset']=='0','segmented weights')
        require(row['direct_catalog_index'] is None,'segmented direct ref')
        seg_total+=len(exp)
    else:
        require(row['direct_catalog_index']==direct.idx,'direct source index')
        require(row['base']==qs(direct.floor) and row['weight']==qs(direct.curvature) and row['offset']==qs(-direct.center),'direct source coefficients')
        require(row['piece_interval']==[qs(direct.lo),qs(direct.hi)],'direct interval')
        require(row['segments']==[],'direct segment absence')
        refs.append(direct.idx)
tangent=catalog.tangent_lower_from_codes(leaf,codes)
A=mod.Q(man['A'])
require(qs(tangent)==leafrec['rank_tangent_lower'],'tangent exact value')
require(qs(tangent-A)==leafrec['exact_margin'] and tangent>A,'strict rational margin')
unique=sorted(set(refs)); macro=sum(i<56 for i in unique); v1=sum(56<=i<272 for i in unique); v3=sum(i>=272 for i in unique)
require(len(unique)==175 and (macro,v1,v3)==(21,154,0),'source selected reference counts')
print('PASS terminal 17 independent source/witness checks')
print('topology55_67='+str(list(top[55:68])))
print('node55_axis=0 node56_terminal=17 kind=quadratic node57=right_child')
print('node55_box='+str(parentrec['box_exact']))
print('node56_box='+str(leafrec['box_exact']))
print('anchor_codes='+str(codes)+' offset='+str(anchor_offset))
print('rows=15 segment_occurrences='+str(seg_total)+' distinct_references='+str(len(unique))+' blocks='+str((macro,v1,v3)))
print('tangent='+qs(tangent))
print('margin='+qs(tangent-A))
print('stream_sha256='+json.dumps(record['source_stream_sha256'],sort_keys=True))
print('catalog_sha256='+json.dumps(record['source_input_sha256'],sort_keys=True))

