from pathlib import Path
import hashlib,json,zipfile,sys
D=Path(__file__).resolve().parent
expected='151048a061e5aef71befb0150c6d44e034855171c9b5c7949ac875e7eabf53ba'
archive=D/'reference/predecessor.zip'
if hashlib.sha256(archive.read_bytes()).hexdigest()!=expected:raise RuntimeError('predecessor archive')
with zipfile.ZipFile(archive) as z:
    if z.testzip() is not None:raise RuntimeError('predecessor CRC')
    for n in ['CheckpointSmoke.lean','SourceNode65.lean','CombinedTree.lean','source_prefix.json','authentic_input.json']:
        if (D/n).read_bytes()!=z.read(n):raise RuntimeError('copied source changed: '+n)
    original=D.parent/'A1294_GLOBAL_BRIDGE_20261104'
    records=[]
    for n in ['GenericGlobalization.lean','GenericGlobalization.olean','generic_global_build.log','GlobalInterface.lean','GlobalInterface.olean','global_build.log']:
        data=z.read(n)
        if original.is_dir() and (original/n).read_bytes()!=data:raise RuntimeError('historical successful artifact changed: '+n)
        records.append({'path':n,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest(),'live_original_checked':original.is_dir()})
    for n in ['generic_global_build.log','global_build.log']:
        s=z.read(n).decode('utf-8')
        if 'Exit status: 0' not in s or 'sorryAx' in s or 'error:' in s:raise RuntimeError('predecessor positive proof log')
decisions=json.loads((D/'DECISIONS.json').read_text())
if decisions['NEW_LEAN_BUILD_STARTED'] or decisions['NEW_LEAN_OBJECTS']!=0:raise RuntimeError('status changed')
if any(D.glob('*.olean')):raise RuntimeError('unexpected new object; status needs reassessment')
version=(D/'native_lean_version.txt').read_text(encoding='utf-8-sig')
if '4.33.0-rc2' not in version or 'd8b18978322de05a8f3dba51ef03cf5461676c17' not in version:raise RuntimeError('native compiler')
print('PASS: preserved predecessor and copied sources; successful global artifacts unchanged; native pinned version recorded; no new Lean build/object claimed. Integrity verification only: checkpoint and source-connected replay remain unverified.')
if __name__=='__main__' and '--write-receipt' in sys.argv:
    (D/'preservation_receipt.json').write_text(json.dumps({'predecessor_sha256':expected,'artifacts':records,'scope':'preservation only, no new mathematical proof'},indent=2))
