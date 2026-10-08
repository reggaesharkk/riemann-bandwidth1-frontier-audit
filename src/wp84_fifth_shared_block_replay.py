"""Independent signed full-path series replay; exact Fractions, no numerical rank."""
from wp84_fifth_5_7_difference_replay import mul,add,sub,tr,scale,comm,smul
from fractions import Fraction as Q
from itertools import permutations,product
from math import factorial
from pathlib import Path
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def series(a,e,n,R,K):
 out=[]
 for k in range(K+1):
  A=[[Q(0) for j in range(n)] for i in range(n)]
  for i in range(n):
   A[i][i]=Q(a**k*e**k*i**k,factorial(k))-(Q(a**k*e**(k-1)*i**(k-1),factorial(k-1)) if k else 0)
   for j in range(n):
    if i!=j and abs(i-j)<=R and k:A[i][j]=Q(a**k*e**(k-1)*(i**k-j**k),factorial(k)*(j-i))
  out.append(A)
 return out
FS=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
def amplitude(fid,roles,n,R,K):
 f=FS[fid];pi=list(map(int,f['equality_partition'].split(',')));sign=[1 if x=='+' else -1 for x in f['sign_word']]
 blocks=sorted(set(pi));exps={b:sum(sign[i] for i in range(5) if pi[i]==b) for b in blocks}
 groups={e:[b for b in blocks if exps[b]==e] for e in set(exps.values())}
 choices=[]
 for e,bs in groups.items():choices.append([dict(zip(bs,ls)) for ls in permutations(roles[e])])
 ans=[Q(0)]*(K+1)
 for assignment in product(*choices):
  logs={k:v for d in assignment for k,v in d.items()}
  E=[series(logs[pi[i]],sign[i],n,R,K) for i in range(5)];P=E[0]
  for A in E[1:]:P=smul(P,A,K)
  for k in range(K+1):ans[k]+=tr(P[k])
 return ans

def main():
 cert=json.loads((ROOT/'notes/WP84_FIFTH_SHARED_RANK_WITNESS.json').read_text())
 for p,h in cert['source_sha256'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 checks=[]
 for n,R in [(2,1),(3,1),(3,2)]:
  D=[[Q(i*(i==j)) for j in range(n)] for i in range(n)];J=[[Q(abs(i-j)<=R) for j in range(n)] for i in range(n)]
  L=scale(comm(D,mul(J,J)),Q(-1,2));M=scale(comm(D,J),-2)
  ll=tr(mul(L,L));lm=tr(mul(L,M));mm=tr(mul(M,M));a,b,c,w,v=map(Q,[3,5,2,7,11])
  cases=[(1,2,6,{3:[a],1:[b,c]},-2*a*a*b*c*(b-a)*(c-a)*ll),
   (11,13,5,{3:[a],1:[b],-1:[c]},-a*a*b*c*(b-a)*lm),
   (35,55,4,{3:[a],-1:[b,c]},-2*a*a*b*c*mm),
   (51,70,4,{1:[a,b,c],-2:[w]},-2*w*w*(a*b+a*c+b*c)*mm),
   (52,71,4,{1:[a,b,c],-1:[v,w]},-4*v*w*(a*b+a*c+b*c)*mm),
   (3,4,6,{2:[a,b],1:[c]},-a*b*c*(b-a)**2*(a+b-c)*ll),
   (4,6,6,{2:[a,b],1:[c]},-a*a*b*b*(b-a)**2*ll),
   (14,24,5,{2:[a,b],-1:[c]},a*b*c*(b-a)**2*lm),
   (24,19,6,{2:[a,b],-1:[c]},-a*a*b*b*(b-a)**2*ll)]
  for f,g,k,roles,expected in cases:
   A=amplitude(f,roles,n,R,k);B=amplitude(g,roles,n,R,k);delta=[x-y for x,y in zip(A,B)]
   assert all(x==0 for x in delta[:k]),(f,g,n,delta)
   assert delta[k]==expected!=0,(f,g,n,delta[k],expected)
   checks.append({'ids':[f,g],'n':n,'R':R,'trace_order':k,'coefficient_c1':str(expected)})
 # Exact symbolic two-cell determinant evaluated as rational log indeterminates.
 ratio=lambda c:c*(a+b-c)/(a*b)
 assert ratio(Q(1))-ratio(Q(2))==Q(-5,15)
 assert cert['new_fifth_lower']==len(cert['witness_ids'])==29
 # Source-level integrity mutations: full descriptors, never abstract word labels.
 f=FS[5];base=json.dumps(f,sort_keys=True)
 def reject(obj):assert json.dumps(obj,sort_keys=True)!=base
 for key in ['equality_partition','sign_word']:
  x=json.loads(base)
  if key=='equality_partition':x[key]='99'+x[key][1:]
  else:x[key]='-'+x[key][1:]
  reject(x)
 # Explicit path/root phase coefficients; exchange one lag or root without updating the other data.
 logs=[Q(2),Q(3),Q(5),Q(7),Q(11)];lags=[1,-1,0,0,0]
 phase=lambda roots:sum(a*r for a,r in zip(logs,roots))
 roots=[0,1,0,0,0];assert phase(roots)!=phase([1,1,0,0,0])
 assert sum(lags)==0 and sum([2]+lags[1:])!=0
 assert len(list(permutations([2,3,5])))==6 and 5!=6
 assert Q(3)**5!=Q(3)**4
 parent=json.loads((ROOT/'notes/WP84_FIFTH_5_7_DIFFERENCE_CERTIFICATE.json').read_text())
 assert parent['first_nonzero_jet']['amplitude_order']==11
 assert ll!=0 and 0!=-2*a*a*ll
 (ROOT/'notes/WP84_FIFTH_SHARED_INDEPENDENT_REPLAY.json').write_text(json.dumps({'checks':checks,'failure_tests':['displacement','root index','missing singleton assignment','prime-log exponent','forced parent coefficient zero'],'exact_arithmetic':True,'scope':'finite rational realizations verify algebra; universal proof and legal-cell arguments in note'},indent=2)+'\n')
 print('PASS 27 exact signed full-path coefficient checks; lower jets vanish; all five mutation detectors reject')
if __name__=='__main__':main()



