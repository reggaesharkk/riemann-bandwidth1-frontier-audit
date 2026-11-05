from pathlib import Path
import json,hashlib
D=Path(__file__).resolve().parent
src=Path('/home/reggaeshark/.elan/toolchains/leanprover--lean4---v4.33.0-rc2/src/lean/lake/Lake/Util/Casing.lean')
for name in ['standalone','baseline']:
    data=json.loads((D/f'{name}_closure.json').read_text())
    for r in data['records']:
        if r['module']=='Lake.Util.Casing' and r['source'] is None:
            r['source']=str(src);r['source_bytes']=src.stat().st_size;r['source_sha256']=hashlib.sha256(src.read_bytes()).hexdigest()
    data['source_bytes_found']=sum(r['source_bytes'] or 0 for r in data['records'])
    data['source_files_unresolved']=[r['module'] for r in data['records'] if r['source'] is None]
    (D/f'{name}_closure_complete.json').write_text(json.dumps(data,indent=2))
    print(name,data['modules'],data['olean_bytes'],data['all_listed_artifact_bytes'],data['source_bytes_found'],data['source_files_unresolved'])
