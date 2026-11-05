import hashlib, json, re, zipfile
from pathlib import Path

D = Path(__file__).resolve().parent
sha = lambda p: hashlib.sha256(p.read_bytes()).hexdigest()
source = D / 'CompositionalLeaf.lean'
if sha(source) != '4a34b508b8ce2dbf72f0bcacce70d01acea7848d381882f72fbeebcf1124bf61':
    raise RuntimeError('changed corrected source')
s = source.read_text(encoding='utf-8-sig')
prefix = (D / 'AuthenticDeclarationPrefix.lean').read_text(encoding='utf-8-sig')
if not s.startswith(prefix):
    raise RuntimeError('authentic declaration prefix changed')
if sha(D / 'authentic_input.json') != '9d261c03f582e7b1f61bc08f38025d3871f01f70806c3ab87783a2a5768da072':
    raise RuntimeError('ledger changed')
d = json.loads((D/'authentic_input.json').read_text())['children']['left']
if sum(len(t['segments']) for t in d['fifteen_models']) != 208 or len(re.findall(r'^theorem segment_\d+_\d+ :', s, re.M)) != 208:
    raise RuntimeError('segment count')
log = (D/'build_project.log').read_text()
if 'Exit status: 0' not in log or 'sorryAx' in log or 'error:' in log:
    raise RuntimeError('unsuccessful kernel build')
for name in ['all_rows','tangent_checked','decode_6','decode_10','accepted','leaf_sound']:
    if f"'AuthenticCompactLeaf.{name}' depends on axioms: [propext, Classical.choice, Quot.sound]" not in log:
        raise RuntimeError('missing clean axiom report: '+name)
print('PASS: preserved literal data, 208 segments, successful compiler log and six clean axiom reports. This script does not replace Lean kernel checking.')
