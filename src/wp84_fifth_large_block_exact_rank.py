"""Exact full-assignment carrier jet reconnaissance, not analytic rank promotion."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations,product
from functools import lru_cache
import json,hashlib
from wp84_fifth_shared_block_replay import series
from wp84_fifth_5_7_difference_replay import smul,tr
ROOT=Path(__file__).resolve().parents[1]
FS=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
BLOCKS=[b for b in json.loads((ROOT/'notes/WP84_FIFTH_SHARED_BLOCK_TABLE.json').read_text()) if not b['complete']]
PRIMES=(2,3,5,7,11,13)
@lru_cache(None)
def traceword(word,n,R,K):
 E=[series(a,e,n,R,K) for a,e in word];P=E[0]
 for A in E[1:]:P=smul(P,A,K)
 return tuple(tr(A) for A in P)
def assignments(fid,carrier,pool):
 f=FS[fid];pi=tuple(map(int,f['equality_partition'].split(',')));eps=tuple(1 if s=='+' else -1 for s in f['sign_word']);bs=sorted(set(pi))
 e={b:sum(eps[i] for i in range(5) if pi[i]==b) for b in bs};groups={v:[b for b in bs if e[b]==v] for v in set(e.values())}
 choices=[]
 for v,bb in sorted(groups.items()):
  pp=carrier.get(v,()) if v else tuple(p for p in pool if p not in set(sum((list(x) for x in carrier.values()),[])))
  if v and len(pp)!=len(bb):raise ValueError((fid,v,pp,bb))
  choices.append([dict(zip(bb,x)) for x in permutations(pp,len(bb))])
 for parts in product(*choices):
  p={b:q for d in parts for b,q in d.items()}
  if len(set(p.values()))!=len(p):continue
  yield pi,eps,p,e

def jets(fid,carrier,pool,logs,n,R,K):
 out=[Q(0)]*(K+1);count=0
 for pi,eps,p,e in assignments(fid,carrier,pool):
  count+=1;word=tuple((logs[p[pi[i]]],eps[i]) for i in range(5));weight=Q(1)
  for i in range(5):weight*=logs[p[pi[i]]]
  for b,q in p.items():weight/=q**((pi.count(b)-abs(e[b]))//2)
  for k,x in enumerate(traceword(word,n,R,K)):out[k]+=weight*x/Q(n)
 # omit only common -u^5/(2 sqrt(product p^abs e)), not column-varying factors
 return out,count

def elimination(rows,columns):
 piv=[];selected=[];basis=[]
 for ri,row in enumerate(rows):
  v=list(map(Q,row))
  for p,b in zip(piv,basis):
   x=v[p];v=[a-x*c for a,c in zip(v,b)]
  nz=next((j for j,x in enumerate(v) if x),None)
  if nz is not None:
   v=[x/v[nz] for x in v];piv.append(nz);basis.append(v);selected.append(ri)
 return piv,selected,basis

def determinant(A):
 a=[list(map(Q,row)) for row in A];d=Q(1)
 for j in range(len(a)):
  k=next((k for k in range(j,len(a)) if a[k][j]),None)
  if k is None:return Q(0)
  if k!=j:a[j],a[k]=a[k],a[j];d=-d
  q=a[j][j];d*=q
  for k in range(j+1,len(a)):
   t=a[k][j]/q
   for l in range(j,len(a)):a[k][l]-=t*a[j][l]
 return d

def kernel(rows,k):
 piv,_,bb=elimination(rows,k)
 for i in range(len(piv)-1,-1,-1):
  for j in range(i):
   t=bb[j][piv[i]];bb[j]=[a-t*b for a,b in zip(bb[j],bb[i])]
 out=[]
 for f in range(k):
  if f in piv:continue
  v=[Q(0)]*k;v[f]=1
  for p,b in zip(piv,bb):v[p]=-b[f]
  out.append(list(map(str,v)))
 return out
def main():
 results=[]
 for b in BLOCKS:
  ids=b['ids'];patterns=[]
  for i in ids:
   f=FS[i];patterns.append({'id':i,'signs':f['sign_word'],'pi':f['equality_partition']})
  # Choose the source orientation from the first member, never fake free carriers.
  pi,eps,p,e=next(assignments_seed(ids[0]))
  carrier={}
  for bb,v in e.items():
   if v:carrier.setdefault(v,[]).append(p[bb])
  rows=[];labels=[];depths=[];ranks=[];allcounts=[]
  for K in [4,6,8,10,12]:
   rows=[];labels=[];allcounts=[]
   for si,(n,R,logs) in enumerate([(2,1,dict(zip(PRIMES,[1,2,3,4,5,6]))),(3,1,dict(zip(PRIMES,[2,5,7,11,13,17]))),(3,2,dict(zip(PRIMES,[3,4,8,9,12,16]))) ]):
    coeff=[];counts=[]
    for i in ids:
     a,c=jets(i,carrier,PRIMES,logs,n,R,K);coeff.append(a);counts.append(c)
    allcounts.append(counts)
    for order in range(K+1):rows.append([a[order] for a in coeff]);labels.append({'specialization':si,'amplitude_order':5+order})
   piv,sel,_=elimination(rows,len(ids));ranks.append({'amplitude_depth':5+K,'specialization_rank':len(piv),'kernel':kernel(rows,len(ids))})
   print(ids,'depth',5+K,'exact specialization rank',len(piv),flush=True)
   if len(piv)==len(ids):break
  minor=[[rows[i][j] for j in piv] for i in sel];d=determinant(minor);assert d
  results.append({'ids':ids,'support':b['support'],'layouts':patterns,'old_analytic_lower':1,'new_analytic_lower':4 if ids in ([18,23,27,30],[41,45,58,67],[40,44,57,66]) else 1,'analytic_upper':len(ids),'unresolved_dimensions':len(ids)-(4 if ids in ([18,23,27,30],[41,45,58,67],[40,44,57,66]) else 1),'carrier':carrier,'pool':PRIMES,'assignment_counts':allcounts,'depth_history':ranks,'jet_rows':[[str(x) for x in row] for row in rows],'row_labels':labels,'minor_rows':sel,'minor_columns':piv,'minor':[[str(x) for x in row] for row in minor],'minor_determinant':str(d),'finite_model_kernel':kernel(rows,len(ids)),'promotion':'NOT PROMOTED: rational log and small section specializations are algebraic diagnostics only'})
 out={'parent':'df5cf745c8fc6acb5bbf2ba85211f86f6b93ac9d','decision':'B','fifth_analytic_bounds':[38,72],'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json','notes/WP84_FIFTH_SHARED_BLOCK_TABLE.json']},'specializations':[{'n':2,'R':1,'logs':[1,2,3,4,5,6]},{'n':3,'R':1,'logs':[2,5,7,11,13,17]},{'n':3,'R':2,'logs':[3,4,8,9,12,16]}],'blocks':results,'analytic_promotion':{'resolved_blocks':[[18,23,27,30],[41,45,58,67],[40,44,57,66]],'new_dimensions':9,'minor_certificates':['notes/WP84_FIFTH_LARGE_BLOCK_18_CERTIFICATE.json','notes/WP84_FIFTH_LARGE_BLOCK_40_41_CERTIFICATE.json','notes/WP84_FIFTH_LARGE_BLOCK_LEGAL_MINOR_INTERVALS.json'],'total_453_family_bounds':[38,453],'witness_ids':sorted(set(json.loads((ROOT/'notes/WP84_FIFTH_SHARED_RANK_WITNESS.json').read_text())['witness_ids']+[23,27,30,45,58,67,44,57,66]))}}
 assert len(out['analytic_promotion']['witness_ids'])==38
 assert sum(b['new_analytic_lower']-b['old_analytic_lower'] for b in results)==9
 (ROOT/'notes/WP84_FIFTH_LARGE_BLOCK_EXACT_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')

def assignments_seed(fid):
 f=FS[fid];pi=tuple(map(int,f['equality_partition'].split(',')));eps=tuple(1 if s=='+' else -1 for s in f['sign_word']);bs=sorted(set(pi));p=dict(zip(bs,PRIMES));e={b:sum(eps[i] for i in range(5) if pi[i]==b) for b in bs}
 yield pi,eps,p,e
if __name__=='__main__':main()
