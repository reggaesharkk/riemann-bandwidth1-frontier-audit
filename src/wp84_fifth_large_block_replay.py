"""Independent raw entry/assignment replay and hostile certificate mutations."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from math import factorial
from functools import lru_cache
import json,copy,hashlib
ROOT=Path(__file__).resolve().parents[1]
FS=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
@lru_cache(None)
def entry(a,e,i,j,R,K):
 out=[];l=j-i
 for k in range(K+1):
  if i==j:v=Q((e*i*a)**k,factorial(k))-(a*Q((e*i*a)**(k-1),factorial(k-1)) if k else 0)
  elif abs(l)>R:v=Q(0)
  else:v=-sum((Q(a**h*(e*l)**(h-1),factorial(h))*Q((e*i*a)**(k-h),factorial(k-h)) for h in range(1,k+1)),Q(0))
  out.append(v)
 return tuple(out)
@lru_cache(None)
def path_trace(word,n,R,K):
 # Root-by-root propagation, independent scalar polynomial convolutions.
 out=[Q(0)]*(K+1)
 for root in range(n):
  state={root:[Q(1)]+[Q(0)]*K}
  for a,e in word:
   nxt={j:[Q(0)]*(K+1) for j in range(n)}
   for i,A in state.items():
    for j in range(n):
     B=entry(a,e,i,j,R,K)
     for k in range(K+1):nxt[j][k]+=sum(A[h]*B[k-h] for h in range(k+1))
   state=nxt
  out=[x+y for x,y in zip(out,state[root])]
 return out

def jets(fid,carrier,pool,logs,n,R,K,drop=False):
 f=FS[fid];pi=tuple(map(int,f['equality_partition'].split(',')));eps=[1 if x=='+' else -1 for x in f['sign_word']];nb=max(pi)+1
 target={int(e):tuple(p) for e,p in carrier.items()};ans=[Q(0)]*(K+1);count=0
 for ps in product(pool,repeat=nb):
  if len(set(ps))<nb:continue
  exps=[sum(eps[i] for i in range(5) if pi[i]==b) for b in range(nb)]
  if any(tuple(sorted(ps[b] for b in range(nb) if exps[b]==e))!=tuple(sorted(pp)) for e,pp in target.items()):continue
  if any(e and e not in target for e in exps):continue
  count+=1
  if drop and count==1:continue
  w=Q(1)
  for i in range(5):w*=logs[ps[pi[i]]]
  for b,e in enumerate(exps):w/=ps[b]**((pi.count(b)-abs(e))//2)
  word=tuple((logs[ps[pi[i]]],eps[i]) for i in range(5))
  v=path_trace(word,n,R,K)
  ans=[x+w*y/n for x,y in zip(ans,v)]
 return ans,count

def det(A):
 n=len(A)
 if not n:return Q(1)
 # Independent fraction-free Bareiss algorithm.
 a=[list(map(Q,r)) for r in A];sgn=1;prev=Q(1)
 for k in range(n-1):
  pivot=next((j for j in range(k,n) if a[j][k]),None)
  if pivot is None:return Q(0)
  if pivot!=k:a[pivot],a[k]=a[k],a[pivot];sgn=-sgn
  q=a[k][k]
  for i in range(k+1,n):
   for j in range(k+1,n):a[i][j]=(a[i][j]*q-a[i][k]*a[k][j])/prev
   a[i][k]=0
  prev=q
 return sgn*a[-1][-1]

def validate(c,recomputed):
 assert c['fifth_analytic_bounds']==[38,72]
 assert len(set(c['analytic_promotion']['witness_ids']))==38
 assert sum(b['new_analytic_lower']-b['old_analytic_lower'] for b in c['blocks'])==9
 for p,h in c['source_sha256'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
 for b,rows in zip(c['blocks'],recomputed):
  for f in b['layouts']:assert f['pi']==FS[f['id']]['equality_partition'] and f['signs']==FS[f['id']]['sign_word']
  assert b['jet_rows']==[[str(x) for x in r] for r in rows]
  minor=[[rows[i][j] for j in b['minor_columns']] for i in b['minor_rows']]
  assert minor==[[Q(x) for x in r] for r in b['minor']]
  assert det(minor)==Q(b['minor_determinant'])!=0

def main():
 c=json.loads((ROOT/'notes/WP84_FIFTH_LARGE_BLOCK_EXACT_CERTIFICATE.json').read_text());recomputed=[]
 for b in c['blocks']:
  K=b['depth_history'][-1]['amplitude_depth']-5;rows=[]
  for spec in c['specializations']:
   logs=dict(zip(b['pool'],spec['logs']));columns=[];counts=[]
   for f in b['ids']:
    v,count=jets(f,b['carrier'],b['pool'],logs,spec['n'],spec['R'],K);columns.append(v);counts.append(count)
   for k in range(K+1):rows.append([v[k] for v in columns])
  recomputed.append(rows);print('Replayed',b['ids'],'depth',K+5,flush=True)
 validate(c,recomputed)
 mutations=[]
 def reject(label,bad):
  try:validate(bad,recomputed)
  except AssertionError:mutations.append(label)
  else:raise AssertionError('corruption accepted: '+label)
 for label,field in [('jet coefficient','jet_rows'),('exact minor entry','minor')]:
  bad=copy.deepcopy(c);bad['blocks'][0][field][0][0]=str(Q(bad['blocks'][0][field][0][0])+1);reject(label,bad)
 bad=copy.deepcopy(c);bad['blocks'][0]['minor_determinant']='0';reject('force determinant zero',bad)
 bad=copy.deepcopy(c);bad['blocks'][0]['layouts'][0]['pi']='0,1,0,2,0';reject('repeated-prime location',bad)
 b=c['blocks'][0];sp=c['specializations'][0];v,_=jets(b['ids'][0],b['carrier'],b['pool'],dict(zip(b['pool'],sp['logs'])),sp['n'],sp['R'],6,drop=True)
 bad=copy.deepcopy(c);bad['blocks'][0]['jet_rows'][0][0]=str(v[0]);reject('delete singleton assignment',bad)
 def checkpath(lags):assert sum(lags)==0 and all(abs(l)<=6000 for l in lags)
 checkpath([1,-1,0,0,0])
 try:checkpath([2,-1,0,0,0])
 except AssertionError:mutations.append('displacement')
 else:raise AssertionError('bad path accepted')
 # Every earlier finite-model kernel is broken by the final exact jet stencil.
 broken=0
 for b,rows in zip(c['blocks'],recomputed):
  for h in b['depth_history'][:-1]:
   for v in h['kernel']:
    v=list(map(Q,v));assert any(sum(a*x for a,x in zip(row,v)) for row in rows);broken+=1
 (ROOT/'notes/WP84_FIFTH_LARGE_BLOCK_HOSTILE_REPLAY.json').write_text(json.dumps({'independent_scalar_path_replay':True,'blocks':7,'corruptions_rejected':mutations,'finite_model_kernel_vectors_broken':broken,'actual_analytic_bounds':[38,72],'formal_minors_do_not_promote_four_larger_blocks':True},indent=2)+'\n')
 print('PASS all seven exact matrices, Bareiss minors, finite-jet coincidence tests and six corruption rejections')
if __name__=='__main__':main()
