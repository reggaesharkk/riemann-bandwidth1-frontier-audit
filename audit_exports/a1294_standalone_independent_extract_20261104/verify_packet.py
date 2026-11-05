from pathlib import Path
import json,hashlib,subprocess,sys
D=Path(__file__).resolve().parent
for name in ['core_build.log','leaf_build.log','total_build.log','baseline_build.log','import_audit.log','baseline_import_audit.log']:
    s=(D/name).read_text(encoding='utf-8')
    if 'Exit status: 0' not in s or 'error:' in s or 'sorryAx' in s:raise RuntimeError('unsuccessful proof/audit '+name)
s=(D/'leaf_build.log').read_text(encoding='utf-8')
for name in ['wire_success','model_success','all_rows','tangent_checked','accepted','leaf_sound']:
    if f"'IndependentTerminal22.{name}' depends on axioms: [propext, Classical.choice, Quot.sound]" not in s:raise RuntimeError('axioms '+name)
if 'explicitLeafCheck_sound model_success accepted' not in s:raise RuntimeError('final generic soundness dependency')
for n,v in json.loads((D/'source_hashes.json').read_text()).items():
    p=D/n
    if p.stat().st_size!=v['bytes'] or hashlib.sha256(p.read_bytes()).hexdigest()!=v['sha256']:raise RuntimeError('hash '+n)
new=json.loads((D/'standalone_closure_complete.json').read_text());old=json.loads((D/'baseline_closure_complete.json').read_text())
ns={r['module'] for r in new['records']};os={r['module'] for r in old['records']}
if ns-os!={'StandaloneCore','StandaloneTerminal22'} or os-ns!={'Zeta23.ThmD.Sextuple.CompositionalLeaf'}:raise RuntimeError('import closure')
if new['source_files_unresolved'] or old['source_files_unresolved']:raise RuntimeError('incomplete source census')
subprocess.run([sys.executable,str(D/'verify_source.py')],check=True)
print('PASS: exact sources/objects, successful independent compiler logs and axioms, no historical acceptance import in complete loaded-module closure. Failed optional path modules are excluded from success. Python is not the Lean kernel or a cryptographic authenticity anchor.')
