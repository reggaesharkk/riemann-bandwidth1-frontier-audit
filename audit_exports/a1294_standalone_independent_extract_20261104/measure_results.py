from pathlib import Path
import re,json,hashlib
D=Path(__file__).resolve().parent
def stat(n):
 s=(D/n).read_text(encoding='utf-8')
 def v(label):return re.search(label+r': (.*)',s).group(1).strip()
 sec=0
 for x in v(r'Elapsed \(wall clock\) time \(h:mm:ss or m:ss\)').split(':'):sec=sec*60+float(x)
 return {'wall_seconds':sec,'peak_rss_kib':int(v(r'Maximum resident set size \(kbytes\)')),'major_faults':int(v(r'Major \(requiring I/O\) page faults')),'exit':int(v('Exit status'))}
new=json.loads((D/'standalone_closure_complete.json').read_text());old=json.loads((D/'baseline_closure_complete.json').read_text())
a={r['module'] for r in new['records']};b={r['module'] for r in old['records']}
if a-b!={'StandaloneCore','StandaloneTerminal22'} or b-a!={'Zeta23.ThmD.Sextuple.CompositionalLeaf'}:raise RuntimeError('unexpected import difference')
if any(x in n for n in a for x in ['CompositionalLeaf','CompositionalRight','AuthenticCompactLeaf','AuthenticCompactRight','A1294CompactParent','WireParent']):raise RuntimeError('historical acceptance dependency')
core=stat('core_build.log');leaf=stat('leaf_build.log');baseline=stat('baseline_build.log');outer=stat('total_build.log')
fresh=(D/'Baseline.olean').stat().st_size
cached=next(r['olean_bytes'] for r in old['records'] if r['module']=='Zeta23.ThmD.Sextuple.CompositionalLeaf')
r={'standalone_core':core,'standalone_leaf':leaf,'baseline_leaf':baseline,'standalone_outer_wrapper':outer,'standalone_compile_process_sum_seconds':core['wall_seconds']+leaf['wall_seconds'],'new_source_bytes':sum((D/n).stat().st_size for n in ['StandaloneCore.lean','StandaloneTerminal22.lean']),'baseline_source_bytes':(D/'baseline/Zeta23/ThmD/Sextuple/CompositionalLeaf.lean').stat().st_size,'new_local_olean_bytes':sum((D/n).stat().st_size for n in ['StandaloneCore.olean','StandaloneTerminal22.olean']),'baseline_fresh_olean_bytes':fresh,'baseline_cached_olean_bytes_in_raw_census':cached,'new_closure_olean_bytes':new['olean_bytes'],'baseline_closure_olean_bytes_adjusted_for_fresh_root':old['olean_bytes']+fresh-cached,'common_module_count':len(a&b),'common_source_bytes':new['source_bytes_found']-140348,'new_only':sorted(a-b),'old_only':sorted(b-a),'notes':['Compile-process sums are comparable units; outer wrapper includes additional Lake/shell startup and is reported separately.','Cache/paging conditions not randomized or controlled. No isolated kernel-only timing or full imported-module -t0 replay.','Raw baseline import audit loads the previously built module with identical source hash; its object is 8 bytes smaller than this fresh baseline artifact. The adjusted closure explicitly pays the observed difference.','Complete import-module census includes companion object files, not OS runtime libraries or a minimal reachable-proof-constant graph.']}
(D/'measurements.json').write_text(json.dumps(r,indent=2));print(json.dumps(r,indent=2))
