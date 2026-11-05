"""SHARKBRIDGE-01 v1 experimental table dialect, NOT a SharkLang VM opcode.
Strict canonical JSON wire format; no signing, provider calls or original-file execution.
"""
from pathlib import Path
from fractions import Fraction as F
from math import gcd
import json, ast, hashlib, zlib, sys, time, copy, importlib.util
from typing import Any, Sequence
D=Path(__file__).resolve().parent

def helpers():
    # Execute only the two audited pure parser helpers and canonical hash helpers.
    # Never import the original modules, run their CLI, or instantiate a signer.
    env={'json':json,'hashlib':hashlib,'Any':Any,'Sequence':Sequence,'PackageAuthError':ValueError}
    for filename,names in [('reference/sharklang/sharklang.py',{'_no_duplicate_json_keys','strict_json_loads'}),('reference/protocol/kernel.py',{'canonical_json_bytes','sha256_canonical'})]:
        tree=ast.parse((D/filename).read_text(encoding='utf-8-sig'))
        nodes=[n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name in names]
        if len(nodes)!=len(names):raise ValueError('helper source mismatch')
        exec(compile(ast.Module(body=nodes,type_ignores=[]),filename,'exec'),env)
    return env
H=helpers(); canonical=H['canonical_json_bytes']; strict=H['strict_json_loads']

def source_data(j):
    leaves=[]
    for side in ['left','right']:
        c=j['children'][side]; rows=[]
        for t in c['fifteen_models']:
            rows.append(['d','macroPiece'+str(t['direct_catalog_index'])] if t['kind']=='direct_piece' else ['f',t['base'],[[x['segment'][0],x['segment'][1],x['declaration']] for x in t['segments']]])
        leaves.append({'node':c['topology_node_zero_based'],'terminal':c['terminal_index_zero_based'],'box':c['box_exact'],'anchor':c['anchor_coordinates_exact'],'rows':rows})
    return {'A':j['children']['left']['A'],'B':j['children']['left']['B'],'parent':j['parent']['box_exact'],'axis':j['parent']['split_axis_zero_based'],'node':65,'children':[66,67],'leaves':leaves}

def encode(s):
    rats=set(); cats=set(); segments=set()
    def qr(x):
        f=F(x); rats.add((f.numerator,f.denominator));return (f.numerator,f.denominator)
    qr(s['A']);qr(s['B'])
    for b in [s['parent']]+[l['box'] for l in s['leaves']]:
        for lo,hi in b:qr(lo);qr(hi)
    for l in s['leaves']:
        for x in l['anchor']:qr(x)
        for r in l['rows']:
            if r[0]=='d':cats.add(r[1])
            else:
                qr(r[1])
                for lo,hi,c in r[2]:segments.add((qr(lo),qr(hi),c));cats.add(c)
    rats=sorted(rats);cats=sorted(cats);qi={x:i for i,x in enumerate(rats)};ci={x:i for i,x in enumerate(cats)}
    seg=sorted((qi[a],qi[b],ci[c]) for a,b,c in segments);si={x:i for i,x in enumerate(seg)}
    ref=lambda x:qi[(F(x).numerator,F(x).denominator)]
    box=lambda b:[[ref(a),ref(b)] for a,b in b]
    leaves=[]
    for l in s['leaves']:
        rows=[]
        for r in l['rows']:
            rows.append([0,ci[r[1]]] if r[0]=='d' else [1,ref(r[1]),[si[(ref(a),ref(b),ci[c])] for a,b,c in r[2]]])
        leaves.append([l['node'],l['terminal'],box(l['box']),[ref(x) for x in l['anchor']],rows])
    return {'version':'SHARKBRIDGE01/1','q':rats,'catalog':cats,'segments':seg,'A':ref(s['A']),'B':ref(s['B']),'parent':[s['node'],s['axis'],box(s['parent']),s['children']],'leaves':leaves}

def decode(raw):
    if not isinstance(raw,bytes) or len(raw)>1000000:raise ValueError('payload bound')
    w=strict(raw.decode('utf-8'))
    if type(w)!=dict or set(w)!={'version','q','catalog','segments','A','B','parent','leaves'} or w['version']!='SHARKBRIDGE01/1':raise ValueError('schema/version')
    if canonical(w)!=raw:raise ValueError('noncanonical wire')
    def nat(x):
        if type(x)!=int or x<0 or x>1000000:raise ValueError('natural index')
        return x
    def at(xs,i):
        i=nat(i)
        if i>=len(xs):raise ValueError('reference out of range')
        return xs[i]
    if type(w['q'])!=list or not 1<=len(w['q'])<=2000:raise ValueError('rational table size')
    q=[]
    for r in w['q']:
        if type(r)!=list or len(r)!=2:raise ValueError('rational record')
        n,d=r
        if type(n)!=int or type(d)!=int or d<=0 or abs(n).bit_length()>512 or d.bit_length()>512 or gcd(abs(n),d)!=1:raise ValueError('noncanonical rational')
        q.append(str(F(n,d)))
    if w['q']!=sorted(w['q']) or len(set(q))!=len(q):raise ValueError('rational order/duplicate')
    cats=w['catalog']
    import re
    if type(cats)!=list or len(cats)>666 or any(type(c)!=str or not re.fullmatch(r'(macroPiece|refinementPiece|refinementV2Piece)\d+',c) for c in cats) or sorted(set(cats))!=cats:raise ValueError('catalog')
    seg=[]
    if type(w['segments'])!=list or len(w['segments'])>1000:raise ValueError('segment bound')
    for r in w['segments']:
        if type(r)!=list or len(r)!=3:raise ValueError('segment shape')
        a,b,c=r;a=at(q,a);b=at(q,b);c=at(cats,c)
        if F(a)>F(b):raise ValueError('reversed interval')
        seg.append([a,b,c])
    if sorted(w['segments'])!=w['segments'] or len(set(map(tuple,w['segments'])))!=len(seg):raise ValueError('segment order/duplicate')
    def box(b):
        if type(b)!=list or len(b)!=5 or any(type(r)!=list or len(r)!=2 for r in b):raise ValueError('five-box')
        out=[[at(q,a),at(q,h)] for a,h in b]
        if any(F(a)>F(h) for a,h in out):raise ValueError('box ordering')
        return out
    p=w['parent']
    if type(p)!=list or len(p)!=4 or p[0]!=65 or type(p[0])!=int or p[1] not in range(5) or type(p[1])!=int or p[3]!=[66,67] or type(p[3])!=list or any(type(x)!=int for x in p[3]):raise ValueError('parent instruction')
    pb=box(p[2]);leaves=[]
    if type(w['leaves'])!=list or len(w['leaves'])!=2:raise ValueError('leaf count')
    for i,l in enumerate(w['leaves']):
        if type(l)!=list or len(l)!=5 or l[:2]!=[66+i,22+i] or any(type(x)!=int for x in l[:2]):raise ValueError('leaf identity')
        b=box(l[2]);anchor=[at(q,x) for x in l[3]]
        if len(anchor)!=5 or any(not F(lo)<=F(a)<=F(hi) for a,(lo,hi) in zip(anchor,b)):raise ValueError('anchor')
        if type(l[4])!=list or len(l[4])!=15:raise ValueError('fifteen rows')
        rows=[]
        for r in l[4]:
            if type(r)!=list or not r or type(r[0])!=int:raise ValueError('row')
            if r[0]==0 and len(r)==2:rows.append(['d',at(cats,r[1])])
            elif r[0]==1 and len(r)==3 and type(r[2])==list and 0<len(r[2])<=256:rows.append(['f',at(q,r[1]),[at(seg,x) for x in r[2]]])
            else:raise ValueError('row tag/shape')
        for k,(lo,hi) in enumerate(pb):
            mid=(F(lo)+F(hi))/2
            expected=[F(lo),mid] if i==0 else [mid,F(hi)]
            if k!=p[1]:expected=[F(lo),F(hi)]
            if list(map(F,b[k]))!=expected:raise ValueError('source split coverage')
        leaves.append({'node':l[0],'terminal':l[1],'box':b,'anchor':anchor,'rows':rows})
    return {'A':at(q,w['A']),'B':at(q,w['B']),'parent':pb,'axis':p[1],'node':p[0],'children':p[3],'leaves':leaves}

def main():
    j=json.loads((D/'frozen/authentic_input.json').read_text());s=source_data(j);w=encode(s);raw=canonical(w)
    if canonical(decode(raw))!=canonical(s):raise RuntimeError('lossless semantic roundtrip')
    (D/'semantic.json').write_bytes(canonical(s));(D/'payload.sb01').write_bytes(raw);(D/'payload.zlib').write_bytes(zlib.compress(raw,9))
    tests=0
    mutations=[lambda x:x.update(version='bad'),lambda x:x['q'][0].__setitem__(1,0),lambda x:x['q'][0].__setitem__(1,2*x['q'][0][1]),lambda x:x['segments'][0].__setitem__(2,9999),lambda x:x['leaves'][0][4].pop(),lambda x:x['leaves'][0][2].pop(),lambda x:x['leaves'][0][4].__setitem__(0,[99]),lambda x:x['parent'].__setitem__(1,3)]
    for mutate in mutations:
        x=strict(raw.decode());mutate(x)
        try:decode(canonical(x))
        except (ValueError,TypeError,IndexError):tests+=1
        else:raise RuntimeError('malformed accepted')
    for bad in [raw+b' ',b'{"version":1,"version":2}',b'{"version":NaN}']:
        try:decode(bad)
        except ValueError:tests+=1
        else:raise RuntimeError('invalid JSON accepted')
    result={'LOSSLESS_ROUNDTRIP':'PASS','negative_tests':tests,'rats':len(w['q']),'segments':len(w['segments']),'catalog':len(w['catalog']),'rows':30,'semantic_bytes':len(canonical(s)),'wire_bytes':len(raw),'wire_zlib_bytes':len(zlib.compress(raw,9))}
    for label,data in [('semantic',canonical(s)),('wire',raw),('frozen_ledger',(D/'frozen/authentic_input.json').read_bytes())]:
        comp=zlib.compress(data,9)
        if zlib.decompress(comp)!=data:raise RuntimeError('zlib roundtrip')
        result[label+'_zlib_bytes']=len(comp)
    try:import zstandard as zstd
    except ImportError:result['zstd']='NOT_INSTALLED_NOT_DOWNLOADED'
    else:
        for label,data in [('semantic',canonical(s)),('wire',raw)]:
            c=zstd.ZstdCompressor(level=19).compress(data)
            if zstd.ZstdDecompressor().decompress(c)!=data:raise RuntimeError('zstd roundtrip')
            result[label+'_zstd_bytes']=len(c)
    (D/'codec_results.json').write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
if __name__=='__main__':main()
