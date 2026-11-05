from pathlib import Path
from fractions import Fraction as F
import json,re,hashlib,zipfile
D=Path(__file__).resolve().parent
j=json.loads((D/'authentic_input.json').read_text())['children']['left']
ref=(D/'GenericReference.lean').read_text(encoding='utf-8-sig');core=(D/'StandaloneCore.lean').read_text(encoding='utf-8');leaf=(D/'StandaloneTerminal22.lean').read_text(encoding='utf-8')
if not core.startswith(ref.split('def decodedRow')[0]):raise RuntimeError('generic math rewritten')
for banned in ['AuthenticCompactLeaf','AuthenticCompactRight','CompositionalLeaf','CompositionalRight','A1294CompactParent','native_decide','sorry','admit','getD','get!']:
    if banned in core or banned in leaf:raise RuntimeError('forbidden dependency/default: '+banned)
if re.findall(r'^import (\S+)',leaf,re.M)!=['StandaloneCore']:raise RuntimeError('leaf imports')
q={int(i):F(int(n),int(d)) for i,n,d in re.findall(r'def q(\d+) : CompactRat := ⟨\((-?\d+)\),(\d+)⟩',leaf)}
ss={int(i):(q[int(a)],q[int(b)],c) for i,a,b,c in re.findall(r'def s(\d+) : SourceSegment := \{lo := interpRat q(\d+), hi := interpRat q(\d+), piece := (\w+)\}',leaf)}
count=0
for t in j['fifteen_models']:
    i=t['pair_index_zero_based']
    if t['kind']=='direct_piece':continue
    ids=re.search(rf'def segments{i} : List SourceSegment := \[([^\]]*)\]',leaf).group(1)
    got=[ss[int(n)] for n in re.findall(r's(\d+)',ids)]
    expected=[(F(x['segment'][0]),F(x['segment'][1]),x['declaration']) for x in t['segments']]
    if got!=expected:raise RuntimeError('source stream '+str(i))
    floorid=int(re.search(rf'def model{i} : ModelRow := .floor \(interpRat q(\d+)\)',leaf).group(1))
    if q[floorid]!=F(t['base']):raise RuntimeError('floor changed')
    count+=len(ids.split(','))
if count!=208 or len(ss)!=107:raise RuntimeError('record count')
payload=json.loads((D/'data_certificate.json').read_text())
if payload['q']!=[[q[i].numerator,q[i].denominator] for i in range(len(q))]:raise RuntimeError('payload rationals')
used=set()
for r in payload['segments']:
    used.update(r[:2])
for r in payload['rows']:
    if r[0]==1:used.add(r[1])
if used!=set(range(len(q))):raise RuntimeError('unchecked unused rational')
for t,r in zip(j['fifteen_models'],payload['rows']):
    if t['kind']=='direct_piece':
        if r[0]!=0 or payload['catalog'][r[1]]!='macroPiece'+str(t['direct_catalog_index']):raise RuntimeError('direct payload')
    else:
        if r[0]!=1 or q[r[1]]!=F(t['base']):raise RuntimeError('payload floor')
        got=[(q[payload['segments'][k][0]],q[payload['segments'][k][1]],payload['catalog'][payload['segments'][k][2]]) for k in r[2]]
        if got!=[(F(x['segment'][0]),F(x['segment'][1]),x['declaration']) for x in t['segments']]:raise RuntimeError('payload segments')
if hashlib.sha256((D/'authentic_input.json').read_bytes()).hexdigest()!='9d261c03f582e7b1f61bc08f38025d3871f01f70806c3ab87783a2a5768da072':raise RuntimeError('frozen input')
full=json.loads((D/'authentic_input.json').read_text())
archive=D/'frozen/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip'
if hashlib.sha256(archive.read_bytes()).hexdigest()!=full['v2_zip_sha256']:raise RuntimeError('frozen archive')
with zipfile.ZipFile(archive) as z:
    prefix='A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/'
    paths={'topology':'certificate/topology-u8.bin','kinds':'certificate/terminal-kinds-u8.bin','anchors':'certificate/anchors-u16le.bin','stable':'data/macro-data-exact.json','v1':'data/refinement-catalog-v1-exact.json','v3':'data/refinement-catalog-v3.json'}
    for key,digest in (full['source_stream_sha256']|full['source_input_sha256']).items():
        if hashlib.sha256(z.read(prefix+paths[key])).hexdigest()!=digest:raise RuntimeError('source hash '+key)
print('PASS: unchanged generic math prefix; no original acceptance imports/references/default lookups; all exact 208 source segment occurrences and floors reconstructed from 107 interned records. This is external provenance verification, not kernel authentication of V2 bytes.')
