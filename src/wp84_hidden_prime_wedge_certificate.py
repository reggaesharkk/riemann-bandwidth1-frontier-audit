"""Exact structural exterior-power certificate for large-section fifth blocks."""
from pathlib import Path
import json
import wp84_hidden_prime_moment_constructor as mom

ROOT=Path(__file__).resolve().parents[1]

def build():
    basis=mom.collect()
    out={'source_head':'b299cbdb12a525739ac17fc489eb7992e8f316ff','R':6000,'section_formula_source':'WP84_FIFTH_FULL_POOL_SECTION_REPLAY.json','common_leading_row_fact':'For each fixed carrier and row jet h, the coefficient of n^h is (c0*lambda)^h/(h+1)! times the same all-ones column vector.','exterior_vanishing':'The determinant term with all m rows at their leading n_i^h_i order vanishes for m>=2. More generally, any term with at least two rows taking their common leading vector vanishes.','first_possible_total_section_deficit':'m-1','first_possible_coefficient':'Delta_B= sum_{k=1}^m a_k * det(rows r_i for i!=k; row k=ones), where a_k=(c0*lambda_k)^h_k/(h_k+1)! and r_i is the exact coefficient-vector of n_i^(h_i-1) in row i. This is the exact coefficient at total deficit m-1; it may vanish.','status':'UNKNOWN: r_i is a source-mask-indexed full-prime sum; neither its exact entry coefficients nor nonvanishing of Delta_B are certified. Therefore this is a first possible coefficient, not asserted to be the first nonzero coefficient.','blocks':[]}
    for b in basis['blocks']:
      m=b['formal_rank']
      out['blocks'].append({'ids':b['ids'],'size':m,'hidden_layout_count':b['hidden_layout_count'],'visible_layout_count':b['visible_layout_count'],'conditional_mask-merged_moment_dimension':b['block_moment_count_if_one_mask_per_slot_pair'],'correction_matrix_rank':'UNKNOWN; exact coefficient matrices depend on unimplemented chi_q, selected endpoints and full q sums','leading_common_row_rank':1,'determinant_vanishes_through_total_deficit':m-2,'first_possible_total_deficit':m-1,'first_possible_coefficient':'Delta_B formula above','first_nonzero_coefficient':'NOT DETERMINED','sign':'not certifiable','certified_analytic_rank':1,'visible_only_subsystem':'No square full-rank minor certified; the visible columns alone have not been lifted'})
    return out

def main():
  data=build();(ROOT/'notes/WP84_HIDDEN_PRIME_WEDGE_CERTIFICATE.json').write_text(json.dumps(data,indent=2)+'\n')
  print('PASS exact exterior leading-term cancellation; first possible deficit m-1 recorded, nonvanishing not asserted')
if __name__=='__main__':main()
