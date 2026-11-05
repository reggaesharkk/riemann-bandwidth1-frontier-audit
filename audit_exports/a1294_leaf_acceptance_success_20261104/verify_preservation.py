import hashlib,json,re
from pathlib import Path
D=Path(__file__).resolve().parent
old=(D.parent/'a1294_fifteen_bridge_20261104/AuthenticCompactLeaf.lean').read_text(encoding='utf-8-sig').split('set_option maxRecDepth 4000 in')[0]
new=(D/'CompositionalLeaf.lean').read_text(encoding='utf-8-sig')
d=json.loads((D/'authentic_input.json').read_text())['children']['left']
if not new.startswith(old):raise RuntimeError('changed authentic declarations')
if sum(len(t['segments']) for t in d['fifteen_models'])!=208:raise RuntimeError('source segment count')
if len(re.findall(r'^theorem segment_\d+_\d+ :',new,re.M))!=208:raise RuntimeError('proof segment count')
if hashlib.sha256((D/'authentic_input.json').read_bytes()).hexdigest()!='9d261c03f582e7b1f61bc08f38025d3871f01f70806c3ab87783a2a5768da072':raise RuntimeError('input hash')
print('PASS: unchanged authentic declaration prefix, frozen ledger hash, all 208 source segments and 208 separate segment checks.')
