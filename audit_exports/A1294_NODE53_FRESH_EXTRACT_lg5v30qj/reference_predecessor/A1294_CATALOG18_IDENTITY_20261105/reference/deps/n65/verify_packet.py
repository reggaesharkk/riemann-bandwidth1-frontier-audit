from pathlib import Path
from fractions import Fraction as F
import hashlib, io, json, re, zipfile

D = Path(__file__).resolve().parent
def require(p, message):
    if not p:
        raise RuntimeError(message)
def sha(data):
    return hashlib.sha256(data).hexdigest()

if (D/'SHA256SUMS.txt').exists():
    for line in (D/'SHA256SUMS.txt').read_text().splitlines():
        h, n = line.split('  ', 1)
        require(sha((D/n).read_bytes()) == h, 'manifest: '+n)

refs = {
    'global_bridge': '151048a061e5aef71befb0150c6d44e034855171c9b5c7949ac875e7eabf53ba',
    'compact_parent': '643dfc7b60959608c1c6550457f21a487eeaaade5d9d410090f486693a3f2bd9',
}
for n,h in refs.items():
    require(sha((D/'reference'/f'{n}.zip').read_bytes()) == h, n)
with zipfile.ZipFile(D/'reference/global_bridge.zip') as z:
    raw = z.read('frozen/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip')
require(sha(raw) == '3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5', 'V2')
prefix = json.loads((D/'source_prefix.json').read_text())
src = (D/'SourceNode65.lean').read_text(encoding='utf-8')
with zipfile.ZipFile(io.BytesIO(raw)) as z:
    for key, name, size, lean_name in [
        ('topology','topology-u8.bin',68,'topologyBytes'),
        ('kinds','terminal-kinds-u8.bin',24,'kindBytes'),
        ('anchors','anchors-u16le.bin',240,'anchorBytes')]:
        with z.open('A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/certificate/'+name) as f:
            data = list(f.read(size))
        require(data == prefix[key], key+' source prefix')
        match = re.search(r'def '+lean_name+r' : List Nat := (\[[^\n]+\])', src)
        require(match is not None and json.loads(match[1]) == data, key+' Lean literals')

pending=[[]]; cursor=0; found={}
for node, token in enumerate(prefix['topology']):
    path=pending.pop(0)
    if node in (65,66,67): found[node]=(path,cursor)
    if token == 0:
        require(prefix['kinds'][cursor] in (0,1), 'terminal kind')
        cursor += 1
    else:
        require(1 <= token <= 5,'split')
        pending[0:0]=[path+[(token-1,False)],path+[(token-1,True)]]
j=json.loads((D/'authentic_input.json').read_text())
require(len(found[65][0])==43 and found[65][1]==22, 'parent location')
require(found[66]==(found[65][0]+[(0,False)],22), 'left relationship')
require(found[67]==(found[65][0]+[(0,True)],23), 'right relationship')
lo=[F(0)]*5; hi=[F(60)]*5
for axis, upper in found[65][0]:
    mid=(lo[axis]+hi[axis])/2
    if upper: lo[axis]=mid
    else: hi[axis]=mid
require([[str(l),str(h)] for l,h in zip(lo,hi)]==j['parent']['box_exact'],'exact parent box')
require(cursor==24, 'terminal exhaustion prefix')
for t in (22,23):
    q=sum(k==1 for k in prefix['kinds'][:t])
    require(prefix['anchors'][10*q:10*q+10] == [0]*10,'quadratic-only anchor cursor')

for stem in ['checkpoint_targeted','source','helpers','replay_only','combined','negative']:
    log=(D/(stem+'.log')).read_text(encoding='utf-8')
    require('Exit status: 0' in log and 'sorryAx' not in log and 'error:' not in log, stem+' clean build')
for stem in ['CheckpointTargeted','SourceNode65','CombinedHelpers','ReplayOnly','CombinedTree','NegativeControls']:
    require((D/(stem+'.olean')).stat().st_size>0, stem+' object')
    text=(D/(stem+'.lean')).read_text(encoding='utf-8')
    require(re.search(r'\b(sorry|admit|native_decide|axiom)\b',text) is None, stem+' forbidden proof shortcut')
require('source_check_accepted' in (D/'CombinedTree.lean').read_text(), 'source-check dependency')
print('PASS: manifest, frozen references, bounded source extraction, exact path/box, recorded clean builds. This Python check is not a Lean kernel replay.')
