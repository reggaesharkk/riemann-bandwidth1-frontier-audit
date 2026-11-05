import os,re,json,hashlib,datetime
from pathlib import Path
D=Path(__file__).resolve().parent
root=Path(r'C:\Users\Asus\Downloads')
pat=re.compile(r'A129[4-9]|A1300|WP84|LRSC|SharkLang|Shark.?Protocol',re.I)
rows=[]
for top in root.iterdir():
 if not top.is_dir() or not pat.search(top.name):continue
 for parent,dirs,files in os.walk(top):
  dirs[:]=[x for x in dirs if x.lower() not in {'.git','.aws','.ssh','.venv','venv','node_modules','__pycache__'}]
  for name in files:
   p=Path(parent)/name
   if re.search(r'credential|secret|private.?key|token|password|^\.env',name,re.I):continue
   if p.suffix.lower() not in {'.py','.lean','.txt','.json','.md','.zip','.csv','.log','.bat','.toml'}:continue
   try:
    st=p.stat();h=hashlib.sha256()
    with p.open('rb') as f:
     for b in iter(lambda:f.read(1048576),b''):h.update(b)
    rows.append({'Name':name,'OriginalPath':str(p),'Bytes':st.st_size,'CreationTimeUtc':datetime.datetime.fromtimestamp(st.st_ctime,datetime.timezone.utc).isoformat(),'LastWriteTimeUtc':datetime.datetime.fromtimestamp(st.st_mtime,datetime.timezone.utc).isoformat(),'SHA256':h.hexdigest()})
   except OSError as e:rows.append({'OriginalPath':str(p),'error':str(e)})
(D/'downloads_research_folders_inventory.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print('matching research-folder files',len(rows))
