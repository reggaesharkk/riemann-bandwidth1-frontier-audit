"""Exact multilinear reducer template for the first large-section wedge term."""
from pathlib import Path
import json
import wp84_exact_determinant_coefficient_builder as builder
ROOT=Path(__file__).resolve().parents[1]

def reduce_block(b):
    m=b['size']; vars=b['moment_variables']
    return {'ids':b['ids'],'size':m,'variables':vars,'exact_expression':'sum_(k=1)^m a_k * sum_(sigma in S_m) sign(sigma) * v_B, sigma(k) * product_(i!=k) r_(i,sigma(i))(S_2,...,S_(h_i+2))','multilinearity':'each subleading row r_i is affine-linear in its permitted source moments; v_B is affine-linear in S_2; hence total degree <=m','candidate_support':vars,'certified_support':None,'cancellations_removed':[],'cancellation_status':'Cannot remove terms without exact source-selected row coefficients; the source row selector is not specified as an executable row tuple. No formal-core determinant coefficient is substituted.','first_possible_deficit':m-1,'identically_zero_status':'undetermined','exact_source_polynomial':'the displayed permutation expansion with r_i entries given by the exact finite trace/path/root sums in WP84_EXACT_DETERMINANT_COEFFICIENTS.json'}

def main():
  data=builder.build();out={'source_head':data['source_head'],'R':6000,'blocks':[reduce_block(b) for b in data['blocks']],'global_determinant_visible_moment_count':'undetermined; at most 9; source coefficient cancellation not evaluated','decision':'F'}
  (ROOT/'notes/WP84_WEDGE_SUPPORT_REDUCTION.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS first possible wedge expression reduced; support marked undetermined where source coefficients are unavailable')
if __name__=='__main__':main()
