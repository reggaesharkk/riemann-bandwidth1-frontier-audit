import json,collections
from pathlib import Path
D=Path(__file__).resolve().parent
r=json.loads((D/'provenance_comparison.json').read_text())
g=collections.defaultdict(list)
for x in r:g[x['SHA256']].append(x['OriginalPath'])
s={'files':len(r),'hash_recorded':sum(bool(x['prior_inventory_matches']) for x in r),'no_inventory_match':sum(not x['prior_inventory_matches'] for x in r),'exact_duplicate_groups':{h:p for h,p in g.items() if len(p)>1},'unmatched_source_candidates':[x for x in r if not x['prior_inventory_matches'] and x['Name'].endswith(('.py','.lean'))]}
(D/'provenance_summary.json').write_text(json.dumps(s,indent=2),encoding='utf-8')
print('duplicate groups',len(s['exact_duplicate_groups']),'unmatched source candidates',len(s['unmatched_source_candidates']))
