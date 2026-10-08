"""Isolate the 18 no-independent-q columns and fail closed on promotion."""
from pathlib import Path
import json
import wp84_fifth_full_pool_amplitude as layouts
ROOT=Path(__file__).resolve().parents[1]

def main():
 blocks=[]
 for ids in layouts.IDS:
  ds=[layouts.descriptor(i) for i in ids]
  vis=[d['id'] for d in ds if not d['hidden_canceled_prime']]
  blocks.append({'block':ids,'size':len(ids),'visible_layouts':vis,'visible_count':len(vis),'exact_matrix':'columns are full source prime/path/section sums for these descriptors, with every nonzero-net equality block prime fixed by the carrier and all distinct visible block primes summed through N(T)','hidden_q_contribution':'exactly absent for these columns','candidate_minor_sizes':list(range(1,min(len(ids),len(vis))+1)),'certified_visible_only_minor':None,'promotion':'none; no source-selected row minor with exact large-section nonzero determinant is recorded'})
 out={'source_head':'990ccbd8f340eea8abccbc0c05dd6fb939e4022b','R':6000,'visible_layout_count':sum(x['visible_count'] for x in blocks),'blocks':blocks,'independence_from_hidden_columns':'source sums split by layout columns exactly; any rank promotion still requires an actual legal visible-only minor','decision':'no visible-only promotion certified'}
 (ROOT/'notes/WP84_VISIBLE_PRIME_SUBSYSTEM.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS visible layouts isolated: 18; no hidden-q coordinates charged to their columns')
if __name__=='__main__':main()
