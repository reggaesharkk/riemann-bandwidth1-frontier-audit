from pathlib import Path
import hashlib,json,subprocess,sys
D=Path(__file__).resolve().parent
for name in ['right_build.log','parent_build.log']:
    s=(D/name).read_text(encoding='utf-8')
    if 'Exit status: 0' not in s or 'sorryAx' in s or 'error:' in s:raise RuntimeError('failed build '+name)
for filename,names in [('right_build.log',['AuthenticCompactRight.all_rows','AuthenticCompactRight.tangent_checked','AuthenticCompactRight.accepted','AuthenticCompactRight.leaf_sound']),('parent_build.log',['A1294CompactParent.source_children_match_parent_split','AuthenticCompactLeaf.accepted','AuthenticCompactRight.accepted','A1294CompactParent.source_parent_box_predicate'])]:
    s=(D/filename).read_text(encoding='utf-8')
    for n in names:
        if f"'{n}' depends on axioms: [propext, Classical.choice, Quot.sound]" not in s:raise RuntimeError('axiom report '+n)
if 'AuthenticCompactLeaf.leaf_sound' not in (D/'parent_build.log').read_text(encoding='utf-8') or 'AuthenticCompactRight.leaf_sound' not in (D/'parent_build.log').read_text(encoding='utf-8'):raise RuntimeError('printed parent dependencies')
for name,entry in json.loads((D/'source_hashes.json').read_text(encoding='utf-8')).items():
    p=D/name
    if p.stat().st_size!=entry['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=entry['sha256']:raise RuntimeError('hash '+name)
subprocess.run([sys.executable,str(D/'verify_inputs.py')],check=True)
print('PASS: successful build logs, standard axiom reports, printed compact child dependencies, exact bundled hashes. Kernel verification itself is evidenced by the Lean compiler logs, not by this Python script.')
