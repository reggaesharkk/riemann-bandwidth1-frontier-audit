from pathlib import Path
from fractions import Fraction as F
import hashlib,json,re
D=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
expected='9d261c03f582e7b1f61bc08f38025d3871f01f70806c3ab87783a2a5768da072'
for n in ['authentic_input.json','authentic_input_O.json','authentic_input_OO.json']:
    if sha(D/n)!=expected:raise RuntimeError('replay disagreement: '+n)
j=json.loads((D/'authentic_input.json').read_text())
s=(D/'CompositionalRight.lean').read_text(encoding='utf-8')
r=j['children']['right']; l=j['children']['left']; p=j['parent']
if len(re.findall(r'^theorem segment_\d+_\d+ :',s,re.M))!=192:raise RuntimeError('segment proof count')
for t in r['fifteen_models']:
    i=t['pair_index_zero_based']
    for k,x in enumerate(t.get('segments',[])):
        exact=f'theorem segment_{i}_{k} : sourceSegmentCheck ({t["base"]}) {{lo := ({x["segment"][0]}), hi := ({x["segment"][1]}), piece := {x["declaration"]}}} = true'
        if exact not in s:raise RuntimeError('segment literal mismatch: '+str((i,k)))
    if f'theorem row_checked_{i} :' not in s:raise RuntimeError('missing row')
if r['rank_tangent_lower'] not in s:raise RuntimeError('tangent mismatch')
axis=p['split_axis_zero_based']
for i,(lo,hi) in enumerate(p['box_exact']):
    mid=(F(lo)+F(hi))/2
    if list(map(F,l['box_exact'][i]))!=[F(lo),mid if i==axis else F(hi)]:raise RuntimeError('left split')
    if list(map(F,r['box_exact'][i]))!=[mid if i==axis else F(lo),F(hi)]:raise RuntimeError('right split')
old=(D/'historical/A1294TwoQuadraticParent.lean').read_text(encoding='utf-8-sig')
new=(D/'A1294CompactParent.lean').read_text(encoding='utf-8')
head=lambda x:x.split('theorem source_parent_box_predicate :')[1].split(':= by')[0]
if head(old)!=head(new):raise RuntimeError('parent statement mismatch')
box=lambda x:x.split('def sourceParentBox : GapBox where')[1].split('\n\n')[0]
if box(old)!=box(new):raise RuntimeError('parent box mismatch')
if 'AuthenticCompactLeaf.leaf_sound' not in new or 'AuthenticCompactRight.leaf_sound' not in new:raise RuntimeError('compact dependency missing')
print('PASS: three exact frozen replays; 192 source segment proof statements; 15 rows; exact tangent; midpoint boxes; historical parent statement and box identical; both compact theorem references.')
