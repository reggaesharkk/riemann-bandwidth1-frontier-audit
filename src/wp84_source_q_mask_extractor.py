"""Executable q-admissibility predicate from the exact WP84 source trace."""
from math import isqrt
from pathlib import Path
import json
import wp84_fifth_full_pool_amplitude as layouts

ROOT=Path(__file__).resolve().parents[1]
JET_MAX={i:6 for i in [15,20,26,28,31,32,10,12,16,17,21,22,25,29,34,37,39,43,53,56,60,63]}
JET_MAX.update({i:8 for i in [36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69]})

def is_prime(n):
    if not isinstance(n,int) or n<2:return False
    if n%2==0:return n==2
    for d in range(3,isqrt(n)+1,2):
        if n%d==0:return False
    return True

def root_count(lags,n):
    if len(lags)!=5 or sum(lags)!=0 or any(abs(x)>6000 for x in lags):return 0
    v=[0]
    for a in lags:v.append(v[-1]+a)
    return max(0,n-(max(v)-min(v)))

def q_mask(layout_id,block,jet,path,section,q,source_state):
    """True iff q contributes to this source atom.

    Source state fields: N, visible_primes (one prime per nonzero-net block),
    alias (the chosen m), and carrier_alias_admissible (the exact source
    nearest-alias, nonzero-detuning indicator computed from visible carrier).
    Section is (k_minus,k_plus), inclusive. Jet changes the weight, not the
    Boolean prime mask. The source trace has no additional slot interval:
    every ordinary prime is in [2,N].
    """
    d=layouts.descriptor(layout_id)
    if block!=d['excess_pair_block'] or not d['hidden_canceled_prime']:return False
    if jet<0 or jet>JET_MAX.get(layout_id,-1):return False
    if not is_prime(q) or q>source_state['N']:return False
    visible=set(source_state['visible_primes'])
    if len(visible)!=len(source_state['visible_primes']):return False
    if len(visible)!=sum(e!=0 for e in d['net_exponents']):return False
    if any(not is_prime(p) or p>source_state['N'] for p in visible):return False
    if q in visible:return False
    kminus,kplus=section;n=kplus-kminus+1
    if n<=0 or root_count(path,n)==0:return False
    if source_state.get('alias') not in d['aliases'] or not source_state.get('carrier_alias_admissible',False):return False
    return True

def q_weight(q,j):
    if not is_prime(q) or j<0:raise ValueError('ordinary prime and nonnegative log power required')
    return (q,j,'(log q)^j/q')

def main():
    rows=[]
    for block in layouts.blocks():
      for d in block['descriptors']:
        if not d['hidden_canceled_prime']:continue
        rows.append({'layout':d['id'],'hidden_block':d['excess_pair_block'],'slot_pair':[i for i,b in enumerate(d['partition']) if b==d['excess_pair_block']],'mask':'prime(q) and 2<=q<=N(T) and q notin visible carrier primes and source carrier alias admitted and source root count rho_I(path)>0','independent_of':['jet','Fourier path except zero-root veto','section endpoints except zero-root veto','orientation'],'path_dependence':'only the contribution weight; Boolean root veto uses rho_I(path), independent of q','carrier_dependence':'visible-prime exclusion and carrier alias indicator; q has net exponent zero','multiplicity':'one q assignment per equality block; no factor 2; source raw-orbit coefficient remains external'})
    out={'source':'WP84_FULL_WEIGHT_EVALUATION_MAP_KERNEL.md eqs. for q_B<=N, distinct equality-block primes, alias indicator and root interval; WP84_FIFTH_BLOCK_5_7_EXACT_DIFFERENCE.md exact trace/path equivalence','source_head':'990ccbd8f340eea8abccbc0c05dd6fb939e4022b','predicate':'q_mask(layout,block,jet,path,section,q,source_state)','prime_interval':'ordinary primes 2<=q<=N(T)=floor(exp(L-sqrt(L)))','extra_slot_windows':'none in the source trace; all five slot primes have the same natural cutoff','equality_exclusion':'q is repeated exactly in its two hidden-block slots; no other equality block may use q','coprimality':'all distinct equality-block primes are distinct ordinary primes, hence pairwise coprime; no additional gcd condition','alias':'lambda=sum e_b log P_b has no q term because e_hidden=0; carrier nearest-alias mask depends only on visible primes','path':'path closure and |ell_s|<=6000 affect weights; section root veto is rho_I(ell)>0 and does not depend on q','section':'root interval [k_- - min(prefix), k_+ - max(prefix)]; q-independent','orientation':'conjugate sign/path has identical q domain','layouts':rows}
    (ROOT/'notes/WP84_EXACT_Q_MASK_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
    # A direct truth-table replay on one hidden descriptor.
    d=layouts.descriptor(31); state={'N':19,'visible_primes':[2,3,5],'alias':2,'carrier_alias_admissible':True};section=(10,20);path=(0,0,0,0,0)
    assert q_mask(31,d['excess_pair_block'],0,path,section,7,state)
    assert not q_mask(31,d['excess_pair_block'],0,path,section,5,state)
    assert not q_mask(31,d['excess_pair_block'],0,path,section,23,state)
    assert not q_mask(31,d['excess_pair_block'],0,path,section,9,state)
    assert not q_mask(15,layouts.descriptor(15)['excess_pair_block'],0,path,section,7,state)
    assert not q_mask(31,d['excess_pair_block'],0,path,section,7,{**state,'alias':3})
    assert not q_mask(31,d['excess_pair_block'],0,(1,0,0,0,0),section,7,state)
    print('PASS exact q mask: cutoff, primality, visible exclusion, alias, root and hidden-block checks')
if __name__=='__main__':main()
