"""Build the exact nine-moment source determinant coefficient expression."""
from pathlib import Path
import json
import wp84_fifth_full_pool_amplitude as layouts
ROOT=Path(__file__).resolve().parents[1]

BLOCK_H={15:6,10:6,36:8,34:6}

def source_entry_formula(h,j):
    if j<2 or j>h+2:return '0'
    k=j-2
    return ('Re sum_(visible injective carrier assignments tau; closed paths |ell_s|<=6000; roots i in [k_--min(v),k_+-max(v)]) '
            '1_{carrier nearest-alias and 0<|lambda-mL|<=H/T} * exp(i*T*lambda) '
            '* [u^(%d)]{(visible-slot product and exact prefix phases) * '
            'exp(c0*i_min*lambda*u)/n * sum_(r=0)^(n-range(v)-1)exp(c0*r*lambda*u) '
            '* kappa_(hidden_pair,%d)(ell) * (visible log factors) }'% (h-k,k))

def build():
  result=[]
  for ids in layouts.IDS:
    desc=[layouts.descriptor(x) for x in ids];hidden=[d for d in desc if d['hidden_canceled_prime']]
    hmax=BLOCK_H[ids[0]];m=len(ids)
    result.append({'ids':ids,'size':m,'hmax':hmax,'moment_variables':[f'S_{j}(N)' for j in range(2,hmax+3)],'matrix_identity':'M_full=M_visible+sum_(j=2)^(hmax+2) S_j E_(B,j)','E_entry_rule':{f'jet_h={h}':{f'S_{j}':source_entry_formula(h,j) for j in range(2,h+3)} for h in range(hmax+1)},'visible_correction':'replace each hidden assignment sum by S_j(N)-sum_(p in visible carrier primes, p<=N)(log p)^j/p; the subtracted finite terms are charged to M_visible','hidden_layout_slots':{str(d['id']):[s for s,b in enumerate(d['partition']) if b==d['excess_pair_block']] for d in hidden},'leading_vector':'v_B(S_2)=exact order-five carrier coefficient vector; source formula is -1/2 times complete visible assignment sum with hidden q weight (log q)^2/q','first_possible_section_coefficient':'C_(m-1)(S)=sum_(k=1)^m a_k det(r_1(S),...,r_(k-1)(S),v_B(S),r_(k+1)(S),...,r_m(S)); a_k=(c0*lambda_k)^h_k/(h_k+1)!','coefficient_polynomial_status':'exact multilinear determinant expression specified; evaluated coefficients/support require actual source-selected row cells and complete visible-prime sums','determinant_visible_support':'not certified; structural candidate powers only','correction_matrix_span_rank':f'unknown, upper bound {min(m,hmax+1)} from at most {hmax+1} moment matrices','common_row_dimension':'unknown','common_column_dimension':'unknown','determinant_null_correction_dimension':'unknown'})
  return {'source_head':'990ccbd8f340eea8abccbc0c05dd6fb939e4022b','decision':'F','R':6000,'global_hidden_moment_basis':[f'S_{j}(N)' for j in range(2,11)],'basis_count':9,'blocks':result,'section_expansion':'source section coefficients are Laurent polynomials in n_i=dprime_i; first possible total deficit m-1; top row vector is the exact common order-five carrier vector v_B, not ones','PNT_main_if_full_interval':'S_j(N)~(log N)^j/j, j=2..10; not inserted into determinant without coefficient support proof'}

def main():
  data=build();(ROOT/'notes/WP84_EXACT_DETERMINANT_COEFFICIENTS.json').write_text(json.dumps(data,indent=2)+'\n');print('PASS exact source determinant expression built over nine master moments; no support/nonzero claim')
if __name__=='__main__':main()
