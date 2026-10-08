"""Universal cyclic-transpose trace polynomial jets in D,J and prime logs."""
from collections import defaultdict
from fractions import Fraction as Q
from math import factorial
from itertools import product,permutations
import json
from pathlib import Path
from wp84_fifth_large_block_exact_rank import assignments,FS
ROOT=Path(__file__).resolve().parents[1]
def comp(k,b):
 if b==1:yield (k,);return
 for i in range(k+1):
  for t in comp(k-i,b-1):yield(i,)+t
def orbit(w):
 if not w:return ''
 return min(w[i:]+w[:i] for w in (w,w[::-1]) for i in range(len(w)))
def coeff(fid,carrier,K):
 ans=defaultdict(Q);pool=tuple(sorted(set(p for ps in carrier.values() for p in ps)))
 for pi,eps,ps,e in assignments(fid,carrier,pool):
  for ks in comp(K,5):
   logs=tuple(sum(ks[i] for i in range(5) if ps[pi[i]]==p) for p in pool)
   terms=[]
   for k,sgn in zip(ks,eps):
    if not k:terms.append([('',Q(1))]);continue
    terms.append([('D'*k,Q(sgn**k,factorial(k)))]+[('D'*i+'J'+'D'*(k-1-i),Q(-sgn**(k-1),factorial(k))) for i in range(k)])
   for ts in product(*terms):
    w=''.join(t[0] for t in ts);c=Q(1)
    for t in ts:c*=t[1]
    ans[(logs,orbit(w),K-w.count('J'))]+=c
 return {k:v for k,v in ans.items() if v}
def main():
 for ids,carrier in [([18,23,27,30],{2:[0],1:[1,2],-1:[3]}),([41,45,58,67],{2:[0],1:[1],-1:[2,3]}),([40,44,57,66],{2:[0],1:[1],-2:[2]})]:
  for K in [4,5,6]:
   maps=[coeff(i,carrier,K) for i in ids];base=maps[0]
   for i,m in zip(ids[1:],maps[1:]):
    d={k:m.get(k,Q(0))-base.get(k,Q(0)) for k in set(m)|set(base)};d={k:v for k,v in d.items() if v}
    print(ids[0],i,'order',K,'terms',len(d))
    if K==5 and len(d)<40:print(d)
if __name__=='__main__':main()
