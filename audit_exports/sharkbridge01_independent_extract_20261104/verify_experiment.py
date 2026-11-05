from pathlib import Path
import json,hashlib,zlib
from fractions import Fraction as F
from codec import decode,canonical
D=Path(__file__).resolve().parent
raw=(D/'evidence.json').read_bytes();ev=json.loads(raw)
if hashlib.sha256(raw).hexdigest()!=(D/'evidence.sha256').read_text().split()[0]:raise RuntimeError('evidence digest')
for n,v in ev['files'].items():
    data=(D/n).read_bytes()
    if len(data)!=v['bytes'] or hashlib.sha256(data).hexdigest()!=v['sha256']:raise RuntimeError('evidence binding: '+n)
s=decode((D/'payload.sb01').read_bytes())
if canonical(s)!=(D/'semantic.json').read_bytes():raise RuntimeError('semantic bytes')
if zlib.decompress((D/'payload.zlib').read_bytes())!=(D/'payload.sb01').read_bytes():raise RuntimeError('compressed bytes')
j=json.loads((D/'frozen/authentic_input.json').read_text());count=0
for side,l in zip(['left','right'],s['leaves']):
    original=j['children'][side]
    if l['box']!=original['box_exact'] or l['anchor']!=original['anchor_coordinates_exact']:raise RuntimeError('box/anchor')
    for t,r in zip(original['fifteen_models'],l['rows']):
        if t['kind']=='direct_piece':
            if r!=['d','macroPiece'+str(t['direct_catalog_index'])]:raise RuntimeError('direct model')
        else:
            exact=[[x['segment'][0],x['segment'][1],x['declaration']] for x in t['segments']]
            if r!=['f',t['base'],exact]:raise RuntimeError('floor/segment stream')
            count+=len(exact)
if count!=400:raise RuntimeError('source segment occurrences')
log=(D/'wire_build.log').read_text(encoding='utf-8')
if 'sorryAx' in log or 'error:' in log or 'Exit status: 0' not in log:raise RuntimeError('failed proof log')
if "'SharkBridge01.parent' depends on axioms: [propext, Classical.choice, Quot.sound]" not in log:raise RuntimeError('parent axioms')
print('PASS: bound source/payload/decoded/proof artifacts; exact 400-segment stream, boxes, anchors and 30 rows; lossless byte roundtrips; recorded clean Lean acceptance. This Python check is not itself a mathematical proof or an external authentication anchor.')
