from pathlib import Path
import hashlib,json,zipfile
from codec import canonical,H
D=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
if sha(D/'frozen/authentic_input.json')!='9d261c03f582e7b1f61bc08f38025d3871f01f70806c3ab87783a2a5768da072':raise RuntimeError('source ledger')
if sha(D/'frozen/a1294_compact_parent_20261104.zip')!='643dfc7b60959608c1c6550457f21a487eeaaade5d9d410090f486693a3f2bd9':raise RuntimeError('frozen packet')
with zipfile.ZipFile(D/'frozen/a1294_compact_parent_20261104.zip') as z:
    raw=z.read('frozen/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip')
    if hashlib.sha256(raw).hexdigest()!='3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5':raise RuntimeError('V2 nested bytes')
for filename in ['baseline_total.log','wire_build.log','import_only.log']:
    s=(D/filename).read_text(encoding='utf-8')
    if 'Exit status: 0' not in s or 'sorryAx' in s or 'error:' in s:raise RuntimeError('compiler failure '+filename)
wire=(D/'wire_build.log').read_text(encoding='utf-8')
for name in ['decoded_left','decoded_right','accepted_left','accepted_right','leaf_left','leaf_right','parent']:
    if f"'SharkBridge01.{name}' depends on axioms: [propext, Classical.choice, Quot.sound]" not in wire:raise RuntimeError('axiom report '+name)
files=['frozen/authentic_input.json','frozen/a1294_compact_parent_20261104.zip','payload.sb01','payload.zlib','semantic.json','codec.py','generate_wire_lean.py','WireParent.lean','WireParent.olean','wire_build.log','baseline_total.log','import_only.log','measurements.json','codec_results.json','structural_results.json']
body={'schema':'SHARKBRIDGE01-EVIDENCE/1','encoding_version':'SHARKBRIDGE01/1','research_owner':'Prince','worktree_base_commit':'eb36159ee7e57053fcae3de025fe4dac539435ab','branch':'codex/sharkbridge-01','original_V2_zip_sha256':'3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5','compiler':{'version':'4.33.0-rc2','revision':'d8b18978322de05a8f3dba51ef03cf5461676c17','upstream':'fba91d214655aaa1fd0504bb893c8859c20c79f9','mathlib':'51e6992efd06126df61a496bebf8f49482a4e129'},'files':{n:{'sha256':sha(D/n),'bytes':(D/n).stat().st_size} for n in files},'results':{'typed_IR_two_leaf_kernel_equivalence':'PROVED','wire_byte_parser_kernel_verified':False,'acceptance_proofs_reused':True,'full_tree':'OPEN'},'signatures':'NONE; no keys accessed','authentication_scope':'locally recomputable canonical SHA-256; requires a separately trusted anchor to prevent replacement or rollback; not mathematical proof'}
(D/'evidence.json').write_bytes(canonical(body));(D/'evidence.sha256').write_text(H['sha256_canonical'](body)+'  evidence.json\n')
print('Evidence SHA256',sha(D/'evidence.json'))
