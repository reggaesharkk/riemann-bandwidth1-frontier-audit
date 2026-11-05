from pathlib import Path
import json,re,zlib,struct,hashlib,time
from codec import decode,canonical
D=Path(__file__).resolve().parent
def stats(path):
    s=path.read_text(encoding='utf-8')
    def value(label):return re.search(label+r': (.*)',s).group(1).strip()
    wall=value(r'Elapsed \(wall clock\) time \(h:mm:ss or m:ss\)')
    sec=0
    for x in wall.split(':'):sec=sec*60+float(x)
    return {'wall_seconds':sec,'peak_rss_kib':int(value(r'Maximum resident set size \(kbytes\)')),'major_faults':int(value(r'Major \(requiring I/O\) page faults')),'exit':int(value('Exit status'))}
sources=sorted((D/'baseline/Zeta23/ThmD/Sextuple').glob('*.lean'))
objects=[D/'baseline/lib/Zeta23/ThmD/Sextuple'/p.with_suffix('.olean').name for p in sources]
def stream(paths):return b''.join(struct.pack('>Q',p.stat().st_size)+p.read_bytes() for p in paths)
results={}
for name,paths in [('baseline_sources',sources),('experimental_closure_sources',sources+[D/'WireParent.lean']),('baseline_objects',objects),('experimental_closure_objects',objects+[D/'WireParent.olean'])]:
    data=stream(paths);start=time.perf_counter();c=zlib.compress(data,9);elapsed=time.perf_counter()-start
    if zlib.decompress(c)!=data:raise RuntimeError('byte roundtrip')
    results[name]={'file_bytes':sum(p.stat().st_size for p in paths),'framed_stream_bytes':len(data),'zlib9_bytes':len(c),'compression_seconds':elapsed,'roundtrip':'PASS'}
results['baseline_total']=stats(D/'baseline_total.log');results['wire_increment']=stats(D/'wire_build.log')
results['import_only']=stats(D/'import_only.log')
results['experimental_complete_closure']={'wall_seconds':results['baseline_total']['wall_seconds']+results['wire_increment']['wall_seconds'],'peak_rss_kib':max(results['baseline_total']['peak_rss_kib'],results['wire_increment']['peak_rss_kib']),'major_faults':results['baseline_total']['major_faults']+results['wire_increment']['major_faults'],'method':'serial measured baseline plus additional measured bridge; no independent cold-cache trial'}
results['kernel_only_time']='NOT_ISOLATED: measured Lean compilation includes elaboration and kernel checking; no full dependency recheck or independent -t0 replay'
raw=(D/'payload.sb01').read_bytes();start=time.perf_counter()
for _ in range(20):decode(raw)
results['python_decode_mean_seconds']=(time.perf_counter()-start)/20
results['common_dependency_cache_upper_bounds_bytes']={'mathlib_lib_lean':6006957427,'zeta23_lib_lean':659473397,'note':'installed cache totals, not a minimal transitive import closure; excluded from any savings claim'}
results['converter_required_source_bytes']=sum((D/n).stat().st_size for n in ['codec.py','generate_wire_lean.py','reference/sharklang/sharklang.py','reference/protocol/kernel.py'])
(D/'measurements.json').write_text(json.dumps(results,indent=2));print(json.dumps(results,indent=2))
