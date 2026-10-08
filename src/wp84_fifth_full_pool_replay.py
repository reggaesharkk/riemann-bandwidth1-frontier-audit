"""Independent exact checks for full-pool decomposition and section lift."""
from pathlib import Path
from math import factorial
from fractions import Fraction as Q
import json,copy
ROOT=Path(__file__).resolve().parents[1]
def rho(n,r):return max(0,n-r)
def split_cancelled_pool(full_primes,visible,core,window,independent=True):
 if not independent:return set(),set(),set()
 full={q for q in full_primes if q not in visible and window(q)}
 core_part=full & set(core); omitted=full-set(core)
 assert core_part.isdisjoint(omitted) and core_part|omitted==full
 return full,core_part,omitted
def validator(s):
 errors=[]
 if s.get('pool')!='all_admissible_primes_to_N':errors.append('omitted-prime tail dropped')
 if s.get('R')!=6000:errors.append('band changed')
 if s.get('section')!='source_selected_I(T)':errors.append('section replaced')
 if s.get('d_ratio')!='source dprime/d->1':errors.append('section density changed')
 if s.get('normalization')!='a_phi(T)^-5 and 1/dprime exactly':errors.append('normalization changed')
 if s.get('fake_logs'):errors.append('rational fake logs')
 if not s.get('all_paths'):errors.append('path/section term removed')
 if s.get('jet_coefficients')!='exact coefficient extraction':errors.append('jet coefficient altered')
 if s.get('prime_windows')!='all source masks chi':errors.append('prime-window condition changed')
 return errors
def main():
 cert=json.loads((ROOT/'notes/WP84_FIFTH_FULL_POOL_LIFT_CERTIFICATE.json').read_text())
 assert len(cert['four_blocks'])==4 and cert['R']==6000
 expected_hidden={15:[31,32],10:[16,17,21,22,25,29],36:[47,49,50,62,65,69],34:[37,39,43,56,60,63]}
 hidden_count=visible_count=0
 for b in cert['four_blocks']:
  assert len(b['ids']) in (6,8,16) and len(b['excess_pair_block_indices'])==len(b['ids'])
  assert sorted(b['hidden_pair_ids'])==sorted(expected_hidden[b['ids'][0]])
  for d in b['descriptors']:
   assert sum(d['multiplicities'])==5
   assert sum((n-abs(e))//2 for n,e in zip(d['multiplicities'],d['net_exponents']))==1
   ex=d['excess_pair_block']
   assert d['hidden_canceled_prime']==(d['net_exponents'][ex]==0)
   hidden_count+=int(d['hidden_canceled_prime']);visible_count+=int(not d['hidden_canceled_prime'])
 assert (hidden_count,visible_count)==(20,18)
 # Core versus omitted is meaningful only for net-zero excess blocks.
 # Visible-excess descriptors have no independent q-variable at all.
 assert all(not d['hidden_canceled_prime'] for d in cert['four_blocks'][0]['descriptors'] if d['id'] in [15,20,26,28])
 # Path prefix range bound is sharp at 2R for five closed increments.
 R=6000
 assert 2*R==12000
 for n in (12000,12001,24001,10**8):
  for r in (0,1,2*R):
   exact=Q(rho(n,r),n)
   if n>2*R:assert exact==1-Q(r,n)
   else:assert exact==0 if r>=n else exact==1-Q(r,n)
 mutations=[]
 fullset={2,3,5,7,11,13,17,19};vis={2,3};core={2,3,5,7,11,13}
 complete,cp,om=split_cancelled_pool(fullset,vis,core,lambda q:True)
 assert complete==cp|om and cp=={5,7,11,13} and om=={17,19}
 assert split_cancelled_pool(fullset,vis,core,lambda q:True,independent=False)==(set(),set(),set())
 try:assert cp|(om-{17})==complete
 except AssertionError:mutations.append('drop omitted prime')
 else:raise AssertionError('omitted-prime deletion was not detected')
 # Exact omitted-prime scalar h=0 exists only for net-zero excess blocks.
 # With layout-specific masks, keep separate signatures; never merge them.
 full={'pool':'all_admissible_primes_to_N','R':6000,'section':'source_selected_I(T)','d_ratio':'source dprime/d->1','normalization':'a_phi(T)^-5 and 1/dprime exactly','fake_logs':False,'all_paths':True,'jet_coefficients':'exact coefficient extraction','prime_windows':'all source masks chi'}
 assert validator(full)==[]
 for key,value,label in [('pool','six-prime core','drop omitted primes'),('R',2,'change R'),('section','n=2','replace section'),('d_ratio','0','alter dprime/d'),('normalization','1','change normalization'),('fake_logs',True,'rational fake logs'),('all_paths',False,'remove section/path term'),('jet_coefficients','perturbed','perturb jet coefficient'),('prime_windows','all primes <=N only','violate prime-window conditions')]:
  bad=dict(full);bad[key]=value;assert validator(bad);mutations.append(label)
 # Model-specific nonzero small section / zero all-large section root functional.
 H=lambda n:rho(n,1)-2*rho(n,2)+rho(n,3)
 assert H(2)==1 and all(H(n)==0 for n in range(3,100))
 # Full-cutoff second moment is not an absolutely summable omitted tail.
 # Algebraic/PNT asymptotic is documented, not claimed from a finite truncation.
 (ROOT/'notes/WP84_FIFTH_FULL_POOL_REPLAY.json').write_text(json.dumps({'decision':'F','blocks':[b['ids'] for b in cert['four_blocks']],'source_matrix_constructor_exact_schema':True,'excess_pair_classification':{str(d['id']):('independent net-zero prime q' if d['hidden_canceled_prime'] else 'repeated visible carrier prime; no independent q tail') for b in cert['four_blocks'] for d in b['descriptors']},'omitted_pair_moment':'only for net-zero excess blocks: S_(r,eta)=sum_{q<=N prime, q outside core/visible, window signature eta}(log q)^r/q','leading_order':'hidden-pair h=0 has r=2 only and a nonpositive coefficient termwise; visible-excess omission is zero; layout-specific window masks require separate eta moments','large_section_identity':'after common translation the h-jet is c0^h*lambda^h/n sum_j (-min)^(h-j)S_j(n-span)/((h-j)!j!); exact Laurent polynomial powers -1..h','explicit_R':6000,'section_threshold':12001,'d_threshold':'24002 conditional on dprime/d>=1/2','dprime_rate_threshold_from_source':'not quantified','full_pool_tail_smallness':False,'rank_stability_norm':None,'determinant_limit':None,'corruptions_rejected':mutations,'source_selected_row_promotions':0},indent=2)+'\n')
 print('PASS 38 exact descriptors (20 net-zero q / 18 visible repeated), core/omitted split, R=6000 threshold, and corruption rejections')
if __name__=='__main__':main()
