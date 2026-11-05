import json,re
from pathlib import Path
D=Path(__file__).resolve().parent
out=[]
for name,status in [('import_baseline.log','PASS'),('segment_profile_v2.log','PASS'),('compact_bridge_build.log','PASS'),('authentic_leaf_build.log','FAILED_DECIDE'),('authentic_leaf_rfl_actual.log','FAILED_RFL'),('bridge_artifact_build.log','PASS_ARTIFACT')]:
 t=(D/name).read_text(encoding='utf-8-sig');get=lambda p:re.search(p,t).group(1)
 out.append({'log':name,'status':status,'wall':get(r'Elapsed \(wall clock\) time.*?: (\S+)'),'peak_rss_KiB':int(get(r'Maximum resident set size \(kbytes\): (\d+)')),'major_page_faults':int(get(r'Major \(requiring I/O\) page faults: (\d+)'))})
(D/'benchmarks.json').write_text(json.dumps(out,indent=2),encoding='utf-8')
print(json.dumps(out,indent=2))
