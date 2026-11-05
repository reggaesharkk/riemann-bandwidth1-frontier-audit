from pathlib import Path
import os,re,sys,json,subprocess,hashlib
log=Path(sys.argv[1]);out=Path(sys.argv[2])
prefix=Path(subprocess.check_output(['lean','--print-prefix'],text=True).strip())
roots=[Path(p).resolve() for p in os.environ.get('LEAN_PATH','').split(':') if p]+[prefix/'lib/lean']
names=list(dict.fromkeys(re.findall(r'CLOSURE ([A-Za-z0-9_.]+)',log.read_text())))
if not names:raise RuntimeError('no module inventory')
records=[]
for n in names:
    rel=Path(*n.split('.'));found=None
    for root in roots:
        p=(root/rel).with_suffix('.olean')
        if p.is_file():found=p;break
    if found is None:raise RuntimeError('unresolved import '+n)
    source_root=Path(str(root).replace('/.lake/build/lib/lean','')) if '/.lake/build/lib/lean' in str(root) else prefix/'src/lean' if root==prefix/'lib/lean' else root
    src=(source_root/rel).with_suffix('.lean')
    files=[p for p in [found,Path(str(found)+'.private'),Path(str(found)+'.server'),found.with_suffix('.ir')] if p.is_file()]
    rec={'module':n,'object':str(found),'olean_bytes':found.stat().st_size,'artifact_files':[{'path':str(p),'bytes':p.stat().st_size} for p in files],'source':str(src) if src.is_file() else None,'source_bytes':src.stat().st_size if src.is_file() else None}
    if src.is_file():rec['source_sha256']=hashlib.sha256(src.read_bytes()).hexdigest()
    records.append(rec)
summary={'modules':len(records),'olean_bytes':sum(r['olean_bytes'] for r in records),'all_listed_artifact_bytes':sum(p['bytes'] for r in records for p in r['artifact_files']),'source_bytes_found':sum(r['source_bytes'] or 0 for r in records),'source_files_unresolved':[r['module'] for r in records if r['source'] is None],'records':records,'scope':'actual transitive imported module names from Lean environment header; object and companion-file sizes, source hashes where resolved; runtime/shared libraries and compiler executable outside this module census'}
out.write_text(json.dumps(summary,indent=2));print({k:v for k,v in summary.items() if k!='records'})
