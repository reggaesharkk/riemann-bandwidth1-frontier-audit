import json,hashlib
from fractions import Fraction
from pathlib import Path
D=Path(__file__).resolve().parent
p=D/'authentic_input.json'
if hashlib.sha256(p.read_bytes()).hexdigest()!='9d261c03f582e7b1f61bc08f38025d3871f01f70806c3ab87783a2a5768da072':raise RuntimeError('source ledger hash')
d=json.loads(p.read_text());l=d['children']['left']
if (l['topology_node_zero_based'],l['terminal_index_zero_based'],len(l['fifteen_models']))!=(66,22,15):raise RuntimeError('source indices')
for t in l['fifteen_models']:
 lo,hi=map(Fraction,t['distance_interval'])
 if t['kind']=='direct_piece':
  a,b=map(Fraction,t['piece_interval'])
  if not a<=lo<=hi<=b:raise RuntimeError('direct interval')
 else:
  cur=lo
  for s in t['segments']:
   a,b=map(Fraction,s['segment'])
   if a!=cur or b<a or Fraction(t['base'])>Fraction(s['model_infimum']):raise RuntimeError('segment cover/floor')
   cur=b
  if cur!=hi:raise RuntimeError('incomplete coverage')
if Fraction(l['exact_margin'])<=0:raise RuntimeError('margin')
print('PASS: authenticated left-leaf indices, exact coverage, source floor margins. This is external data validation, not Lean acceptance.')
