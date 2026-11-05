from pathlib import Path
import hashlib,json,zipfile,re,ast
D=Path(__file__).resolve().parent
for n,v in json.loads((D/'source_hashes.json').read_text()).items():
    p=D/n
    if p.stat().st_size!=v['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=v['sha256']:raise RuntimeError('hash '+n)
for filename,names in [('generic_global_build.log',['Zeta23.ThmD.Sextuple.MacroPrototype.affineTree_global_at']),('global_build.log',['A1294GlobalBridge.exact_tail_margin','A1294GlobalBridge.A1294_global_of_root_predicate'])]:
    s=(D/filename).read_text(encoding='utf-8')
    if 'Exit status: 0' not in s or 'error:' in s or 'sorryAx' in s:raise RuntimeError('failed positive module '+filename)
    for n in names:
        if f"'{n}' depends on axioms: [propext, Classical.choice, Quot.sound]" not in s:raise RuntimeError('axiom report '+n)
original=(D/'ParametricAdapter.source.lean').read_text(encoding='utf-8')
excerpt='theorem affineTree_global_at'+original.split('theorem affineTree_global_at')[1].split('#print axioms fastLeafCheckAt_sound')[0]
if excerpt not in (D/'GenericGlobalization.lean').read_text(encoding='utf-8'):raise RuntimeError('upstream proof changed')
interface=(D/'GlobalInterface.lean').read_text(encoding='utf-8')
if '(root : BoxPredicate' not in interface:raise RuntimeError('root no longer explicit')
for n in ['GenericGlobalization.lean','GlobalInterface.lean']:
    if re.search(r'\b(sorry|admit|axiom|native_decide)\b',(D/n).read_text(encoding='utf-8')):raise RuntimeError('proof shortcut '+n)
prefix=json.loads((D/'source_prefix.json').read_text())
archive=D/'frozen/A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip'
if hashlib.sha256(archive.read_bytes()).hexdigest()!=prefix['archive_sha256']:raise RuntimeError('V2 hash')
with zipfile.ZipFile(archive) as z:
    for key,member,count in [('topology','topology-u8.bin',68),('kinds','terminal-kinds-u8.bin',24),('anchors','anchors-u16le.bin',240)]:
        raw=list(z.open('A1294_SOURCE_FREE_REPLAY_PACKAGE_V2/certificate/'+member).read(count))
        if raw!=prefix[key]:raise RuntimeError('source prefix '+key)
source=(D/'SourceNode65.lean').read_text(encoding='utf-8')
for field,key in [('topologyBytes','topology'),('kindBytes','kinds'),('anchorBytes','anchors')]:
    value=ast.literal_eval(re.search(rf'def {field} : List Nat := (\[[^\]]*\])',source).group(1))
    if value!=prefix[key]:raise RuntimeError('literal conversion '+field)
failed=(D/'source_failed_v1.log').read_text(encoding='utf-8')
if 'error:' not in failed or 'sorryAx' not in failed or 'Exit status: 1' not in failed:raise RuntimeError('failure evidence lost')
if (D/'checkpoint_smoke.log').exists() or (D/'CombinedTree.olean').exists():raise RuntimeError('status ledger needs reassessment')
print('PASS: two successful conditional-globalization modules and clean axioms; verbatim upstream proof; exact frozen source-prefix literals; failed/uncompiled source bridge correctly excluded. Root and complete source-connected subtree remain OPEN.')
