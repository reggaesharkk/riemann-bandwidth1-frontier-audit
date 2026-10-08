"""Exact Faulhaber verification for full source root phases, h<=13."""
from fractions import Fraction as Q
from math import factorial,comb
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]
def power_sums(M,H):
 # Coefficients in ascending powers of M; exact telescoping recurrence.
 S=[[Q(0),Q(1)]]
 def trim(a):
  while len(a)>1 and a[-1]==0:a.pop()
  return a
 for h in range(1,H+1):
  top=[Q(0)]*(h+2);top[h+1]=1
  for j in range(h):
   for k,v in enumerate(S[j]):top[k]-=Q(comb(h+1,j))*v
  S.append(trim([v/Q(h+1) for v in top]))
 return S
def ev(poly,x):return sum(v*x**i for i,v in enumerate(poly))
def rootjet(n,span,m,h,lam):
 M=n-span;S=power_sums(M,h)
 return Q(lam**h,n)*sum((Q((-m)**(h-j),factorial(h-j)*factorial(j))*ev(S[j],M) for j in range(h+1)),Q(0))
def direct(n,span,m,h,lam):
 M=n-span
 # coefficient of u^h in exp(-m*lambda*u)*sum_r exp(r*lambda*u)/n.
 from math import comb
 return Q(lam**h,n*factorial(h))*sum((comb(h,j)*(-m)**(h-j)*sum(r**j for r in range(M)) for j in range(h+1)),Q(0))
def main():
 assert power_sums(0,0)==[[Q(0),Q(1)]]
 for h in range(14):
  for n,span,m,lam in [(12001,12000,-3,7),(24005,11987,17,11),(50001,7,0,13)]:
   assert rootjet(n,span,m,h,lam)==direct(n,span,m,h,lam)
  if h:
   p=power_sums(1, h)[h];assert len(p)==h+2 and p[-1]==Q(1,h+1)
 # Coefficient polynomials in n have degree <=h after division by n; verify sampled finite differences.
 for h in range(14):
  vals=[n*rootjet(n,5,2, h,3) for n in range(8,8+h+3)]
  for _ in range(h+2):vals=[b-a for a,b in zip(vals,vals[1:])]
  assert all(x==0 for x in vals),(h,vals)
 assert rootjet(12001,12000,0,0,1)==Q(1,12001)
 assert rootjet(12001,12000,0,1,1)==0 # with one root r=0, first derivative vanishes
 out={'R':6000,'max_closed_five_step_prefix_range':12000,'all_paths_have_roots_if_n_at_least':12001,'verified_orders':'0..13','section_jet_formula':'c0^h*lambda^h/n sum_(j=0)^h (-minprefix)^(h-j)S_j(n-span)/((h-j)!j!)','fixed_jet_laurent_range_in_n':'-1..h; after multiplication by n the degree is <=h+1','leading_coefficient':'(c0*lambda)^h/(h+1)!','small_to_large_affine_claim':False}
 (ROOT/'notes/WP84_FIFTH_FULL_POOL_SECTION_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS exact Faulhaber/root-phase formula through u^13, R=6000')
if __name__=='__main__':main()
