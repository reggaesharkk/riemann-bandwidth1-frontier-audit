from pathlib import Path
from fractions import Fraction as F
import io, json, re, hashlib, zipfile
D=Path(__file__).resolve().parent
def require(p,msg):
    if not p: raise RuntimeError(msg)
def sha(b): return hashlib.sha256(b).hexdigest()
if (D/'SHA256SUMS.txt').exists():
    for line in (D/'SHA256SUMS.txt').read_text().splitlines():
        h,n=line.split('  ',1);require(sha((D/n).read_bytes())==h,'manifest '+n)
raw=(D/'reference/node65.zip').read_bytes()
require(sha(raw)=='7205153baa297ab573ab65b212db41469144f494eaa2eea064b9650182b35a54','predecessor')
with zipfile.ZipFile(io.BytesIO(raw)) as old:
    require(old.testzip() is None,'predecessor CRC')
    for line in old.read('SHA256SUMS.txt').decode().splitlines():
        h,n=line.split('  ',1);require(sha(old.read(n))==h,'old artifact '+n)
    with zipfile.ZipFile(io.BytesIO(old.read('reference/global_bridge.zip'))) as g:
        v2=g.read('frozen/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip')
require(sha(v2)=='3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5','frozen V2')
with zipfile.ZipFile(io.BytesIO(v2)) as z:
    prefix='A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/'
    manifest=json.loads(z.read(prefix+'certificate/manifest.json'))
    streams={k:z.read(prefix+'certificate/'+n) for k,n in [('topology','topology-u8.bin'),('kinds','terminal-kinds-u8.bin'),('anchors','anchors-u16le.bin')]}
    for k,b in streams.items():require(sha(b)==manifest['stream_sha256'][k],k+' full source hash')
    cats=[]
    for key,name in [('stable','macro-data-exact.json'),('v1','refinement-catalog-v1-exact.json'),('v3','refinement-catalog-v3.json')]:
        b=z.read(prefix+'data/'+name);require(sha(b)==manifest['input_sha256'][key],key+' hash');cats+=json.loads(b)['pieces']
require(len(cats)==666,'catalog length')
top=streams['topology'][:68];kinds=streams['kinds'][:24];anchors=streams['anchors'][:240]
require(list(top[63:68])==[4,0,1,0,0] and list(kinds[21:24])==[1,1,1],'source target')
pending=[([(F(0),F(60))]*5,[])];t=0;nodes={}
for n,code in enumerate(top):
    box,path=pending.pop();q=sum(k==1 for k in kinds[:t])
    nodes[n]=(box,path,t,q)
    if code==0:t+=1
    else:
        axis=code-1;l,h=box[axis];m=(l+h)/2;a=box.copy();b=box.copy();a[axis]=(l,m);b[axis]=(m,h)
        pending += [(b,path+[[axis,'R']]),(a,path+[[axis,'L']])]
geo=json.loads((D/'source_geometry.json').read_text())
for entry in geo['nodes']:
    n=entry['node'];box,path,tc,qc=nodes[n]
    require(entry['box']==[[str(a),str(b)] for a,b in box] and entry['path']==path,'node box/path '+str(n))
    require(entry['terminal_cursor_before']==tc and entry['quadratic_cursor_before']==qc,'cursor '+str(n))
require(nodes[64][1]==nodes[63][1]+[[3,'L']] and nodes[65][1]==nodes[63][1]+[[3,'R']],'children')
require(t==24 and [nodes[n][2] for n in range(63,68)]==[21,21,22,22,23],'source cursors')
leaf=json.loads((D/'authentic_input.json').read_text())['children']['left']
recheck=json.loads((D/'authentic_input_recheck.json').read_text())
require(leaf==recheck['children']['left'],'independent extraction repeat')
require(leaf['box_exact']==[[str(a),str(b)] for a,b in nodes[64][0]],'leaf geometry')
q=nodes[64][3];codes=[anchors[q*10+2*i]+256*anchors[q*10+2*i+1] for i in range(5)]
require(codes==[0]*5==leaf['anchor_codes_u16le'],'source lower corner')
require(F(leaf['rank_tangent_lower'])-F(leaf['A'])==F(leaf['exact_margin'])>0,'external exact margin')
require(len(leaf['fifteen_models'])==15,'fifteen models')
anchor=list(map(F,leaf['anchor_coordinates_exact']));B=F(leaf['B'])
value=B*sum(anchor);gradient=[B]*5
for row in leaf['fifteen_models']:
    a,b=row['gap_index_range_inclusive'];weight=F(row['weight'])
    dot=sum(anchor[a:b+1])+F(row['offset'])
    value+=F(row['base'])+weight*dot*dot
    for k in range(a,b+1):gradient[k]+=2*weight*dot
tangent=value+sum(g*(F(leaf['box_exact'][i][0 if g>=0 else 1])-anchor[i]) for i,g in enumerate(gradient))
require(tangent==F(leaf['rank_tangent_lower']),'independently expanded quadratic tangent')
for i,row in enumerate(leaf['fifteen_models']):
    require(row['pair_index_zero_based']==i,'row order')
    a,b=row['gap_index_range_inclusive'];box=nodes[64][0]
    require([str(sum((box[k][0] for k in range(a,b+1)),F(0))),str(sum((box[k][1] for k in range(a,b+1)),F(0)))]==row['distance_interval'],'distance row')
    if row['kind']=='segmented_constant':
        end=F(row['distance_interval'][0])
        for s in row['segments']:
            require(F(s['segment'][0])==end,'segment seam');end=F(s['segment'][1])
            require(s['source_item']==cats[s['catalog_index_zero_based']],'original selected catalog item')
        require(end==F(row['distance_interval'][1]),'complete endpoint coverage')
require(sum(len(r['segments']) for r in leaf['fifteen_models'])==254,'segments')
for mod,log in [('Terminal21','terminal21'),('Source63','source63'),('ReplayTransport','transport'),('Node63Helpers','helpers63'),('Node63Replay','replay63'),('Node63Controls','controls63')]:
    s=(D/(log+'.log')).read_text(encoding='utf-8')
    require('Exit status: 0' in s and 'sorryAx' not in s and 'error:' not in s,mod+' clean log')
    require((D/(mod+'.olean')).stat().st_size>0,mod+' object')
    source=(D/(mod+'.lean')).read_text(encoding='utf-8')
    # Comments are removed before checking forbidden proof constructs.
    source=re.sub(r'--[^\n]*','',source)
    require(re.search(r'\b(sorry|admit|native_decide|axiom)\b',source) is None,mod+' proof shortcuts')
source=(D/'Terminal21.lean').read_text(encoding='utf-8')
require('AuthenticCompactLeaf.accepted' not in source and 'AuthenticCompactRight.accepted' not in source,'independent acceptance')
require('A1294Combined.replay65' in (D/'Node63Replay.lean').read_text(),'imported node65 replay')
env=(D/'environment.txt').read_text()
for h in ['fba91d214655aaa1fd0504bb893c8859c20c79f9','51e6992efd06126df61a496bebf8f49482a4e129','d8b18978322de05a8f3dba51ef03cf5461676c17','f65ae374b127388dc40e203a57337dd7e2d594417453bca4d0ff00df5c557a57','2d17b9c061e22c4d9a14a59ead52c4f0f33068692a2e2a08e37657570fed62dd']:
    require(h in env,'pinned environment '+h)
print('PASS: manifests, preserved objects, original source prefix/catalog data, exact geometry, bounded controls and recorded clean Lean builds. Python verification is not a substitute for Lean replay.')
