from pathlib import Path
import os,hashlib,zipfile,json
D=Path(__file__).resolve().parent
files=[]
for base,dirs,names in os.walk(D,followlinks=False):
    dirs[:]=[n for n in dirs if n!='__pycache__' and not (Path(base)==D/'baseline' and n=='lib')]
    for n in names:
        p=Path(base)/n
        if n!='SHA256SUMS.txt' and p.is_file() and not p.is_symlink():files.append(p)
for n in ['CompositionalLeaf','CompositionalRight','A1294CompactParent']:
    p=D/'baseline/lib/Zeta23/ThmD/Sextuple'/f'{n}.olean'
    if not p.is_file() or p.is_symlink():raise RuntimeError('unsafe/missing output '+n)
    files.append(p)
files=sorted(set(files))
manifest=''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(D).as_posix()+'\n' for p in files)
(D/'SHA256SUMS.txt').write_text(manifest)
zpath=D.parent.parent/'SHARKBRIDGE01_A1294_EXPERIMENT_20261104.zip'
with zipfile.ZipFile(zpath,'x',zipfile.ZIP_DEFLATED) as z:
    for p in files+[D/'SHA256SUMS.txt']:z.write(p,p.relative_to(D).as_posix())
verify=D.parent.parent/'sharkbridge01_independent_extract_20261104'
with zipfile.ZipFile(zpath) as z:
    if z.testzip() is not None:raise RuntimeError('CRC')
    z.extractall(verify)
for line in (verify/'SHA256SUMS.txt').read_text().splitlines():
    digest,n=line.split('  ',1)
    if hashlib.sha256((verify/n).read_bytes()).hexdigest()!=digest:raise RuntimeError('manifest '+n)
result={'zip':str(zpath),'bytes':zpath.stat().st_size,'sha256':hashlib.sha256(zpath.read_bytes()).hexdigest(),'manifest_entries':len(files),'CRC':'PASS','independent_extraction_manifest':'PASS','dependency_links_excluded':True}
(zpath.with_suffix('.receipt.json')).write_text(json.dumps(result,indent=2));print(json.dumps(result,indent=2))
