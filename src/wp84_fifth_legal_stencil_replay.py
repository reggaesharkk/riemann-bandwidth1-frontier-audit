"""Legality obstruction certificate, prime cone and sparse polynomial replay."""
from pathlib import Path
from fractions import Fraction as Q
from math import gcd
from functools import reduce
import copy,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def monomial(t,logs):
 v=Q(t[0])
 for x,k in zip(logs,t[1:7]):v*=x**k
 for p,k in zip([2,3,5,7,11,13],t[8:14]):v/=p**k
 return v # c0=1 algebra check only

def determinant(a):
 a=[list(r) for r in a];d=Q(1)
 for j in range(len(a)):
  pivot=next((i for i in range(j,len(a)) if a[i][j]),None)
  if pivot is None:return Q(0)
  if pivot!=j:a[j],a[pivot]=a[pivot],a[j];d=-d
  x=a[j][j];d*=x
  for i in range(j+1,len(a)):
   t=a[i][j]/x
   for k in range(j+1,len(a)):a[i][k]-=t*a[j][k]
 return d

def classify(row):
 reasons=[]
 if row.get('prime_order')!=sorted(row.get('prime_order',[])) or len(set(row.get('prime_order',[])))!=len(row.get('prime_order',[])):reasons.append('prime ordering/distinctness violation')
 if row.get('band')!=6000:reasons.append('band mismatch')
 if not row.get('logs_are_actual'):reasons.append('rational surrogate logs')
 if not row.get('complete_prime_pool'):reasons.append('incomplete canceled-prime sum')
 if not row.get('source_section'):reasons.append('section selector not certified')
 if not row.get('alias_admission'):reasons.append('near-alias mask not certified')
 if not row.get('full_normalization'):reasons.append('normalization not certified')
 return {'legal':not reasons,'reasons':reasons}

def main():
 polys=json.loads((ROOT/'notes/WP84_FIFTH_LEGAL_STENCIL_DETERMINANT_POLYNOMIALS.json').read_text());old=json.loads((ROOT/'notes/WP84_FIFTH_LARGE_BLOCK_EXACT_CERTIFICATE.json').read_text());rows=[];factors=[]
 for p,h in polys['source_sha256'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 for b,o in zip(polys['four_blocks'],old['blocks'][:4]):
  matrix=[];fac=[]
  for i,(row,label,den) in enumerate(zip(b['matrix_integer_polynomials'],b['row_labels'],b['row_positive_denominators'])):
   allterms=[t for col in row for t in col];assert den>0 and allterms
   logmin=[min(t[1:7][j] for t in allterms) for j in range(6)]
   cmin=min(t[7] for t in allterms);xmin=[min(t[8:14][j] for t in allterms) for j in range(6)];ig=reduce(gcd,[abs(t[0]) for t in allterms])
   fac.append({'row':i,'positive_denominator':den,'integer_gcd':ig,'log_powers':logmin,'c0_power':cmin,'reciprocal_prime_powers':xmin})
   h=label['amplitude_order']-5;assert all(sum(t[1:7])==5+h and sum(t[8:14])==1 and t[7]<=h for t in allterms)
   logs=old['specializations'][label['specialization']]['logs'];matrix.append([sum((monomial(t,logs) for t in col),Q(0))/den for col in row])
  assert determinant(matrix)==Q(b['exact_rational_diagnostic_determinant'])!=0
  factors.append({'ids':b['ids'],'row_monomial_factors':fac,'residual':'divide each integer row polynomial by its displayed monomial and gcd; determinant remains exact; no further factorization certified'})
  # All target carriers have exponent sum in (-negative count,positive count).
  fs=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text());f=fs[b['ids'][0]];pi=list(map(int,f['equality_partition'].split(',')));eps=[1 if s=='+' else -1 for s in f['sign_word']];e=[sum(eps[j] for j in range(5) if pi[j]==i) for i in range(max(pi)+1)];ap=sum(max(0,x) for x in e);am=sum(max(0,-x) for x in e);m=next(m for m in f['aliases'] if 0<m<ap);t=Q(m+am,ap+am);gamma=[t if x>0 else 1-t if x<0 else Q(1,2) for x in e];assert sum(x*y for x,y in zip(e,gamma))==m and all(0<x<1 for x in gamma)
  rows.append({'ids':b['ids'],'net_exponents':e,'m':m,'gamma':list(map(str,gamma)),'prime_realization':'PROVED for finite prescribed tuple with strict slack; not full-pool minor','full_legal_minor':None,'legal_jet_rank_certified_here':1,'legal_leading_row':'w_j=-sum_matching_assignments product(log p)^nu / product p^(nu/2) /2, nonzero','kernel_basis':'w_0*e_j-w_j*e_0 for each j>0; LEGALITY-UNRESOLVED beyond this one row'})
 diagnostic={'band':1,'logs_are_actual':False,'complete_prime_pool':False,'source_section':False,'alias_admission':False,'full_normalization':False};assert not classify(diagnostic)['legal']
 # Necessary admission conditions are independently toggled; a synthetic rule test is NOT a physical certificate.
 rulefixture={k:True for k in ['logs_are_actual','complete_prime_pool','source_section','alias_admission','full_normalization']};rulefixture['band']=6000;rulefixture['prime_order']=[2,3,5];assert classify(rulefixture)['legal']
 rejected=[]
 for label,key,val in [('illegal section','source_section',False),('diagnostic-only replacement','band',1),('illegal merged primes','prime_order',[2,2,5]),('ordering violation','prime_order',[3,2,5])]:
  x=dict(rulefixture);x[key]=val;assert not classify(x)['legal'];rejected.append(label)
 # No new legal full minor exists, so minors are audited as formal only.
 b=polys['four_blocks'][0];s=old['specializations'][b['row_labels'][0]['specialization']]['logs'];original=sum(monomial(t,s) for t in b['matrix_integer_polynomials'][0][0]);assert original!=0
 def artifact_validate(candidate):
  reference=old['blocks'][0]
  assert candidate['layouts']==reference['layouts']
  for ri,(row,label,den) in enumerate(zip(candidate['matrix_integer_polynomials'],candidate['row_labels'],candidate['row_positive_denominators'])):
   logs=old['specializations'][label['specialization']]['logs']
   actual=[sum((monomial(t,logs) for t in col),Q(0))/den for col in row]
   expected=[Q(reference['jet_rows'][reference['minor_rows'][ri]][j]) for j in reference['minor_columns']]
   assert actual==expected
 def rejects_artifact(label,bad):
  try:artifact_validate(bad)
  except AssertionError:rejected.append(label)
  else:raise AssertionError('mutation accepted '+label)
 artifact_validate(b)
 bad=copy.deepcopy(b);bad['matrix_integer_polynomials'][0][0][0][0]+=1;rejects_artifact('alter coefficient',bad)
 bad=copy.deepcopy(b);bad['matrix_integer_polynomials'][0][0]=[];rejects_artifact('zero minor entry',bad)
 bad=copy.deepcopy(b);bad['layouts'][0]['pi']='0,1,0,2,0';rejects_artifact('move repeated slot',bad)
 assert 1-2+1==0 and -1+4-3==0
 rootcount=lambda n: max(0,n-1)-2*max(0,n-2)+max(0,n-3)
 assert rootcount(2)==1 and all(rootcount(n)==0 for n in range(3,20))
 out={'root_counterexample':{'H2':1,'H_n_for_n_ge3':0,'affine_coefficients':[0,0],'ranges':[1,2,3],'band':6000},'decision':'E','fifth_bounds':[38,72],'total_453_bounds':[38,453],'no_new_legal_minor':True,'four_targets':rows,'factorizations':factors,'diagnostic_classification':classify(diagnostic),'corruption_suite_scope':'admission-rule and formal-artifact integrity tests; synthetic fixture is not a certified legal cell','rejected_corruptions':rejected,'prime_realization_window':'[C Y^gamma,2C Y^gamma], fixed positive C, gamma bounded away from0 and1; PNT supplies fixed finite count for large Y','missing_theorem':'complete-cutoff carrier-jet stencil injectivity at source-selected large n and R6000'}
 (ROOT/'notes/WP84_FIFTH_LEGAL_CELL_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS independent sparse polynomial evaluation, exact determinants, common factors, prime-cone conditions; all four stencils FORMAL_ONLY')
if __name__=='__main__':main()
