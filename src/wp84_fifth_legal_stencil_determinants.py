"""Sparse exact determinant polynomials: formal, never legal-cell promotion."""
from pathlib import Path
from collections import defaultdict
from fractions import Fraction as Q
from math import factorial,lcm
from functools import lru_cache
import json,hashlib
from wp84_fifth_large_block_exact_rank import assignments,FS,determinant
ROOT=Path(__file__).resolve().parents[1];POOL=(2,3,5,7,11,13)
@lru_cache(None)
def tracepoly(word,n,R,K):
 total=[defaultdict(Q) for _ in range(K+1)]
 for root in range(n):
  z=(0,)*7;states=[ [defaultdict(Q) for _ in range(K+1)] for _ in range(n)];states[root][0][z]=Q(1)
  for p,e in word:
   nxt=[ [defaultdict(Q) for _ in range(K+1)] for _ in range(n)]
   for i in range(n):
    for j in range(n):
     if abs(i-j)>R:continue
     for k in range(K+1):
      terms=[]
      if k==0:
       if i==j:terms=[(0,Q(1))]
      else:
       if i==j:terms.append((k,Q(e**k*i**k,factorial(k))))
       q=-Q(e**(k-1)*sum(i**t*j**(k-1-t) for t in range(k)),factorial(k))
       if q:terms.append((k-1,q))
      for h in range(K-k+1):
       for key,v in states[i][h].items():
        for cpower,q in terms:
         key2=list(key);key2[p]+=k;key2[6]+=cpower;nxt[j][h+k][tuple(key2)]+=v*q
   states=nxt
  for k in range(K+1):
   for key,v in states[root][k].items():total[k][key]+=v
 return [{key:v for key,v in a.items() if v} for a in total]
def column(fid,carrier,n,R,K):
 ans=[defaultdict(Q) for _ in range(K+1)]
 for pi,eps,p,e in assignments(fid,carrier,POOL):
  nu=[0]*6;extra=[0]*6
  for b,q in p.items():
   z=POOL.index(q);nu[z]=pi.count(b);extra[z]=(pi.count(b)-abs(e[b]))//2
  assert sum(extra)==1
  word=tuple((POOL.index(p[pi[i]]),eps[i]) for i in range(5))
  for k,poly in enumerate(tracepoly(word,n,R,K)):
   for key,v in poly.items():ans[k][tuple(a+b for a,b in zip(key[:6],nu))+(key[6],)+tuple(extra)]+=v/n
 return [{key:v for key,v in a.items() if v} for a in ans]
def evaluate(poly,logs,c=1):
 out=Q(0)
 for key,v in poly.items():
  for a,k in zip(logs,key[:6]):v*=a**k
  v*=c**key[6]
  for p,k in zip(POOL,key[7:]):v/=p**k
  out+=v
 return out

def main():
 old=json.loads((ROOT/'notes/WP84_FIFTH_LARGE_BLOCK_EXACT_CERTIFICATE.json').read_text());out=[]
 for b in old['blocks'][:4]:
  K=b['depth_history'][-1]['amplitude_depth']-5;mat=[];rows=[];scale=[];checked=[]
  cols={s:[column(f,{int(e):v for e,v in b['carrier'].items()},sp['n'],sp['R'],K) for f in b['ids']] for s,sp in enumerate(old['specializations'])}
  for ri in b['minor_rows']:
   label=b['row_labels'][ri];s=label['specialization'];k=label['amplitude_order']-5
   polys=[cols[s][j][k] for j in b['minor_columns']];den=1
   for poly in polys:
    for v in poly.values():den=lcm(den,v.denominator)
   scale.append(den);logs=old['specializations'][s]['logs'];evaluated=[evaluate(poly,logs) for poly in polys]
   assert evaluated==[Q(b['jet_rows'][ri][j]) for j in b['minor_columns']];checked.append(evaluated)
   mat.append([[[int(v*den),*key[:6],key[6],*key[7:]] for key,v in sorted(poly.items())] for poly in polys]);rows.append(label)
  det=determinant(checked);assert det==Q(b['minor_determinant'])!=0
  out.append({'ids':b['ids'],'layouts':b['layouts'],'support':b['support'],'depth':K+5,'row_labels':rows,'row_positive_denominators':scale,'matrix_integer_polynomials':mat,'formula':'D_formal = det(M_integer)/(product(row_positive_denominators)); cell variables z[s,j]=log p_j, x[s,j]=1/p_j; c0 formal; sqrt(P_v) and -1/2 column-common row factors stripped','cleared_determinant':'sum_sigma sign(sigma) product_i M_integer[i,sigma(i)]','exact_rational_diagnostic_determinant':str(det),'nonzero_polynomial':True,'factorization_status':'common positive row denominators and multihomogeneous log degrees extracted; residual determinant left as exact sparse determinant expression, not factorized','physical_status':'FORMAL_ONLY','rows_different_cells':True})
  print('Built exact sparse polynomial determinant',b['ids'],flush=True)
 result={'parent':'e139eeab18f94a9888997ee6f132e6ef2dbf1145','decision':'E','fifth_bounds':[38,72],'term_encoding':'[integer_coefficient, six log powers, c0 power, six reciprocal-prime powers]','four_blocks':out,'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['notes/WP84_FIFTH_LARGE_BLOCK_EXACT_CERTIFICATE.json','notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json']}}
 (ROOT/'notes/WP84_FIFTH_LEGAL_STENCIL_DETERMINANT_POLYNOMIALS.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
if __name__=='__main__':main()
