import json,re,zipfile,hashlib
from pathlib import Path
D=Path(__file__).resolve().parent
R=D.parent
rows=json.loads((D/'downloads_inventory.json').read_text(encoding='utf-8-sig'))
rows += json.loads((D/'downloads_research_folders_inventory.json').read_text(encoding='utf-8'))
rows = [r for r in rows if 'SHA256' in r]
known={}
for p in R.rglob('*.json'):
 if not any(x in p.name.lower() for x in ('inventory','manifest','hash')): continue
 if D in p.parents or p.stat().st_size>8_000_000: continue
 try: text=p.read_text(encoding='utf-8-sig')
 except (OSError,UnicodeError): continue
 for h in set(re.findall(r'(?i)\b[0-9a-f]{64}\b',text)):
  known.setdefault(h.lower(),[]).append(str(p))
for r in rows:
 r['prior_inventory_matches']=known.get(r['SHA256'],[])
 r['status']='EXACT_HASH_ALREADY_RECORDED' if r['prior_inventory_matches'] else 'NO_MATCH_IN_SCANNED_INVENTORIES'
 if r['Name'].lower().endswith('.zip'):
  try:
   with zipfile.ZipFile(r['OriginalPath']) as z:
    r['candidate_source_log_memory_members']=[i.filename for i in z.infolist() if re.search(r'(?i)(\.py$|\.lean$|generator|memory|benchmark|\.log$|log\.txt$)',i.filename)]
  except (OSError,zipfile.BadZipFile) as e:r['archive_inventory_error']=str(e)
(D/'provenance_comparison.json').write_text(json.dumps(rows,indent=2),encoding='utf-8')
print('files',len(rows),'previously recorded',sum(bool(r['prior_inventory_matches']) for r in rows),'no hash match',sum(not r['prior_inventory_matches'] for r in rows))
print('NO_MATCH does not establish that a file was previously unexamined; archive members were inventoried by name only.')

