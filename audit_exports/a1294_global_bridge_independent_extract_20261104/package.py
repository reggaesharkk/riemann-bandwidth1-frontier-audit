from pathlib import Path
import hashlib,zipfile,json,os
D=Path(__file__).resolve().parent
files=[]
for base,dirs,names in os.walk(D,followlinks=False):
    dirs[:]=[n for n in dirs if n!='__pycache__']
    for n in names:
        p=Path(base)/n
        if n!='SHA256SUMS.txt' and p.is_file() and not p.is_symlink():files.append(p)
files=sorted(files)
(D/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(D).as_posix()+'\n' for p in files))
zpath=D.parent.parent/'A1294_GLOBAL_INTERFACE_SOURCE_BRIDGE_AUDIT_20261104.zip'
with zipfile.ZipFile(zpath,'x',zipfile.ZIP_DEFLATED) as z:
    for p in files+[D/'SHA256SUMS.txt']:z.write(p,p.relative_to(D).as_posix())
v=D.parent.parent/'a1294_global_bridge_independent_extract_20261104'
with zipfile.ZipFile(zpath) as z:
    if z.testzip() is not None:raise RuntimeError('CRC')
    z.extractall(v)
for line in (v/'SHA256SUMS.txt').read_text().splitlines():
    h,n=line.split('  ',1)
    if hashlib.sha256((v/n).read_bytes()).hexdigest()!=h:raise RuntimeError('manifest '+n)
r={'zip':str(zpath),'bytes':zpath.stat().st_size,'sha256':hashlib.sha256(zpath.read_bytes()).hexdigest(),'manifest_entries':len(files),'CRC':'PASS','independent_extraction_manifest':'PASS','proof_scope':'CONDITIONAL_GLOBAL_INTERFACE_ONLY; SOURCE_CONNECTED_SUBTREE_OPEN'}
(zpath.with_suffix('.receipt.json')).write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
