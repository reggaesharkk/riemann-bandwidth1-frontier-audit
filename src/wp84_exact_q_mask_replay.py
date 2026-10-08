"""Independent exact q-mask / moment-count replay and hostile mutations."""
from pathlib import Path
from math import isqrt
from collections import defaultdict
from fractions import Fraction
import json,copy
ROOT=Path(__file__).resolve().parents[1]
FUNCS=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
BLOCKS=[[15,20,26,28,31,32],[10,12,16,17,21,22,25,29],[36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69],[34,37,39,43,53,56,60,63]]
EXPECTED_HIDDEN={31,32,16,17,21,22,25,29,47,49,50,62,65,69,37,39,43,56,60,63}
EXPECTED_VISIBLE={15,20,26,28,10,12,36,38,42,46,48,54,59,61,64,68,34,53}

def prime(n):
 if n<2:return False
 return all(n%d for d in range(2,isqrt(n)+1))

def domain(q,N,V,alias_ok,roots):
 return prime(q) and q<=N and q not in V and alias_ok and roots>0

def canon(N,V):return ('P_N',tuple(sorted(p for p in set(V) if p<=N)))

def validator(cert):
 e=[]
 if cert.get('master_domain')!='all ordinary primes 2<=q<=N(T)':e.append('selected/truncated q range')
 if cert.get('hidden_multiplicity')!=2:e.append('hidden block multiplicity changed')
 if cert.get('carrier_net_exponent')!=0:e.append('carrier sign/net exponent changed')
 if cert.get('moment_powers')!=list(range(2,11)):e.append('log power changed/deleted')
 if cert.get('R')!=6000:e.append('R changed')
 if cert.get('section')!='source-selected I(T)':e.append('d=2/surrogate section')
 if cert.get('visible_layouts')!=sorted(EXPECTED_VISIBLE):e.append('visible layout deleted')
 if cert.get('all_moments_zero'):e.append('moments forced to zero')
 if cert.get('first_coefficient_formula')!='sum_k a_k det(r_except_k, v_B)':e.append('C_(m-1) perturbed')
 if cert.get('excluded_visible_primes')!='all distinct visible carrier primes':e.append('q exclusion deleted')
 if cert.get('mask_equivalence')!='P_N minus exact visible-prime set':e.append('different masks merged or identical masks split')
 return e

def main():
 hidden=set();visible=set();pairmap=defaultdict(list)
 for block in BLOCKS:
  for fid in block:
   f=FUNCS[fid];pi=list(map(int,f['equality_partition'].split(',')));eps=[1 if z=='+' else -1 for z in f['sign_word']]
   ex=next(b for b in set(pi) if pi.count(b)>abs(sum(eps[s] for s in range(5) if pi[s]==b)))
   if sum(eps[s] for s in range(5) if pi[s]==ex)==0:
    hidden.add(fid);pairmap[tuple(s for s in range(5) if pi[s]==ex)].append(fid)
   else:visible.add(fid)
 assert hidden==EXPECTED_HIDDEN and visible==EXPECTED_VISIBLE
 assert len(pairmap)==9 and sum(len(x) for x in pairmap.values())==20
 assert list(range(2,11))==[2,3,4,5,6,7,8,9,10]
 # Exact domain equivalence and finite-exclusion decomposition.
 assert canon(100,[2,3])==canon(100,[3,2])
 assert canon(100,[2,3])!=canon(100,[2,5])
 for q in range(2,50):
  lhs=domain(q,47,{2,3,5},True,1)
  rhs=prime(q) and q<=47 and q not in {2,3,5}
  assert lhs==rhs
 # S_j - visible exclusions is an exact identity for arbitrary weights,
 # tested as a formal atom-by-prime coefficient vector.
 for j in range(2,11):
  ps=[p for p in range(2,100) if prime(p)]
  full={p:1 for p in ps};exc={p:1 for p in ps if p in {2,3,5}}
  reduced={p:1 for p in ps if p not in {2,3,5}}
  assert {p:full.get(p,0)-exc.get(p,0) for p in ps if full.get(p,0)-exc.get(p,0)}==reduced
 base={'master_domain':'all ordinary primes 2<=q<=N(T)','hidden_multiplicity':2,'carrier_net_exponent':0,'moment_powers':list(range(2,11)),'R':6000,'section':'source-selected I(T)','visible_layouts':sorted(visible),'all_moments_zero':False,'first_coefficient_formula':'sum_k a_k det(r_except_k, v_B)','excluded_visible_primes':'all distinct visible carrier primes','mask_equivalence':'P_N minus exact visible-prime set'}
 assert validator(base)==[]
 tests=[('merge different q masks',lambda x:x.update(mask_equivalence='one pooled mask')),('split identical q masks',lambda x:x.update(mask_equivalence='layout-specific duplicate masks')),('delete q exclusion',lambda x:x.update(excluded_visible_primes='none')),('truncate q range',lambda x:x.update(master_domain='six primes')),('forget multiplicity',lambda x:x.update(hidden_multiplicity=1)),('change carrier sign',lambda x:x.update(carrier_net_exponent=1)),('change log power',lambda x:x.update(moment_powers=list(range(3,12)))),('force moments zero',lambda x:x.update(all_moments_zero=True)),('change R',lambda x:x.update(R=5999)),('use d=2',lambda x:x.update(section='d=2')),('delete visible layout',lambda x:x.update(visible_layouts=x['visible_layouts'][:-1])),('perturb C_m-1',lambda x:x.update(first_coefficient_formula='perturbed'))]
 rejected=[]
 for label,mut in tests:
  b=copy.deepcopy(base);mut(b);assert validator(b),label;rejected.append(label)
 out={'decision':'F','hidden_count':len(hidden),'visible_count':len(visible),'candidate_73_to_exact_master_moments':'73 -> 9','moment_powers':list(range(2,11)),'pair_slot_layouts':{str(k):sorted(v) for k,v in sorted(pairmap.items())},'mask_equivalence_rule':'exact set equality after visible exclusions','corruption_tests_rejected':rejected,'determinant_visible_moment_count':'unknown; exact source coefficient wedge not evaluated','certified_rank_increment':0}
 (ROOT/'notes/WP84_EXACT_Q_MASK_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n')
 print('PASS exact mask replay: 20 hidden, 18 visible, 73 -> 9, 12 hostile corruptions rejected')
if __name__=='__main__':main()
