from pathlib import Path
import hashlib,json,subprocess,sys,zipfile
D=Path(__file__).resolve().parent
files=sorted(p for p in D.rglob('*') if p.is_file() and p.name!='SHA256SUMS.txt' and '__pycache__' not in p.parts)
(D/'SHA256SUMS.txt').write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+p.relative_to(D).as_posix()+'\n' for p in files))
dest=D.parent.parent/'A1294_NODE61_SOURCE_CONNECTED_SEVEN_NODE_REPLAY_20261105.zip'
with zipfile.ZipFile(dest,'x',zipfile.ZIP_DEFLATED) as z:
    for p in files+[D/'SHA256SUMS.txt']:z.write(p,p.relative_to(D).as_posix())
out=D.parent.parent/'a1294_node61_independent_extract_20261105'
if out.exists():raise RuntimeError('Use a new independent extraction directory')
with zipfile.ZipFile(dest) as z:
    if z.testzip() is not None:raise RuntimeError('ZIP CRC')
    z.extractall(out)
results=[]
for mode in [[],['-O'],['-OO']]:
    for script in ['verify_packet.py','finish_decoders.py']:
        r=subprocess.run([sys.executable,*mode,str(out/script)],capture_output=True,text=True)
        results.append({'mode':mode,'script':script,'exit':r.returncode,'stdout':r.stdout,'stderr':r.stderr})
        if r.returncode:raise RuntimeError(results)
receipt={'zip':str(dest.resolve()),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'manifest_entries':len(files),'CRC':'PASS','independent_extraction_replays':results,'scope':'terminal20 and source-connected nodes61..67 kernel proved; complete root OPEN'}
dest.with_suffix('.receipt.json').write_text(json.dumps(receipt,indent=2));print(json.dumps(receipt,indent=2))
