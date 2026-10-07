"""Signed near-alias support reduction, conditional H optimizer and soft-bound test."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import prod,factorial,comb
import csv,json,hashlib
from functools import lru_cache
from wp84_near_alias_long_tail_discharge import log_interval,PI,tuple_constructor
log_interval=lru_cache(maxsize=None)(log_interval)
ROOT=Path(__file__).resolve().parents[1]
def partitions(n):
    def go(a):
        if len(a)==n:yield tuple(a);return
        for v in range(max(a)+2):yield from go(a+[v])
    yield from go([0])
def pattern(labels,eps):
    k=max(labels)+1
    nu=[labels.count(j) for j in range(k)]
    e=[sum(s for x,s in zip(labels,eps) if x==j) for j in range(k)]
    ap=sum(max(t,0) for t in e);am=sum(max(-t,0) for t in e)
    return nu,e,ap,am

def extrema(primes,e):
    assert len(primes)>=len(e)
    pos=sorted((v for v in e if v>0),reverse=True);neg=sorted((-v for v in e if v<0),reverse=True)
    low=primes;high=primes[::-1]
    return F(prod(low[j]**v for j,v in enumerate(pos)),prod(high[j]**v for j,v in enumerate(neg))),F(prod(high[j]**v for j,v in enumerate(pos)),prod(low[j]**v for j,v in enumerate(neg)))
def matching_extrema(primes,e,allowed):
    """Exact finite injective assignment with arbitrary intersected slot windows."""
    def opt(maximize):
        dp={0:F(1)}
        for p in primes:
            nxt=dp.copy()
            for mask,q in dp.items():
                for j,c in enumerate(e):
                    if not mask>>j&1 and p in allowed[j]:
                        key=mask|1<<j;value=q*F(p)**c
                        if key not in nxt or (value>nxt[key] if maximize else value<nxt[key]):nxt[key]=value
            dp=nxt
        return dp.get((1<<len(e))-1)
    return opt(False),opt(True)
def ceil(q):return -((-q.numerator)//q.denominator)
def floor(q):return q.numerator//q.denominator
def finite_m_range(lo,hi,X,H):
    if lo is None:return []
    L=log_interval(X);a=(F(H)/(2*PI[1]*X),F(H)/(2*PI[0]*X))
    qlo=log_interval(lo);qhi=log_interval(hi)
    lower=[(qlo[i]-a[j])/L[k] for i,j,k in product(range(2),repeat=3)]
    upper=[(qhi[i]+a[j])/L[k] for i,j,k in product(range(2),repeat=3)]
    assert ceil(min(lower))==ceil(max(lower)) and floor(min(upper))==floor(max(upper)), 'refine boundary intervals'
    return [m for m in range(ceil(min(lower)),floor(max(upper))+1) if m]
def alias_status(e,m,nu=None):
    active=sum(v!=0 for v in e)
    if not active:return 'support_empty'
    if active==1:return 'closed_one_active_block'
    if nu is not None and all(v>=2 for v in nu):return 'closed_no_singleton_blocks'
    if (all(v>=0 for v in e) or all(v<=0 for v in e)) and abs(m)==1:return 'closed_one_side_first_alias'
    return 'remaining_signed_dilated_product'
def energy_test(primes=(2,3,5,7),r=3):
    count={};weighted={}
    for row in product(primes,repeat=r):
        n=prod(row);count[n]=count.get(n,0)+1;weighted[n]=weighted.get(n,F(0))+F(1,n)
    assert max(count.values())<=factorial(r)
    s2=sum((F(1,p*p) for p in primes),F(0))
    assert sum((v*v for v in weighted.values()),F(0))<=factorial(r)*s2**r
    return {'prime_list':list(primes),'r':r,'ordered_tuples':len(primes)**r,'max_representation_count':max(count.values()),'weighted_energy':str(sum((v*v for v in weighted.values()),F(0))),'energy_bound':str(factorial(r)*s2**r),'scope':'exact rational regression a(p)=1/p; theorem norm inequality proved in note'}
def slab_checks():
    checks=0
    for k in range(1,4):
        for e in product((-2,0,2),repeat=k):
            active=sum(v!=0 for v in e)
            if not active:continue
            neg=sum(v<0 for v in e)
            def cdf(x):
                return sum(((-1)**j*comb(active,j)*max(x-j,F(0))**active for j in range(active+1)),F(0))/factorial(active)
            for m in range(-6,7):
                if not m:continue
                for w in (F(1,100),F(1,1000)):
                    volume=cdf(neg+(m+w)/2)-cdf(neg+(m-w)/2)
                    assert 0<=volume<=w;checks+=1
    return checks
def main():
    primes=[p for p in range(2,73) if all(p%q for q in range(2,int(p**.5)+1))]
    L=log_interval(1000);g72=(L[0]-log_interval(72)[1]);g73=(L[1]-log_interval(73)[0])
    assert g72>0 and g72*g72>L[1] and g73>0 and g73*g73<L[0]
    rows=[];counts={};closed=remaining=0
    for b in (5,6):
        counts[str(b)]={'patterns':0,'support_alias_slots':0,'closed_one_active_block':0,'closed_one_side_first_alias':0,'closed_no_singleton_blocks':0,'remaining_signed_dilated_product':0}
        for labels in partitions(b):
            for eps in product((-1,1),repeat=b):
                nu,e,ap,am=pattern(labels,eps);counts[str(b)]['patterns']+=1
                ms=[] if ap+am==0 else [m for m in range(1-am,ap) if m]
                lo,hi=extrema(primes,e);toy=finite_m_range(lo,hi,1000,10)
                statuses=[alias_status(e,m,nu) for m in ms]
                for z in statuses:counts[str(b)][z]+=1;counts[str(b)]['support_alias_slots']+=1
                rows.append([b,''.join('+' if v==1 else '-' for v in eps),','.join(map(str,labels)),','.join(map(str,nu)),','.join(map(str,e)),ap,am,','.join(map(str,ms)),','.join(statuses),str(lo),str(hi),','.join(map(str,toy))])
    assert len(rows)==14656
    with (ROOT/'notes/WP84_SIGNED_NEAR_ALIAS_SUPPORT.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['degree','sign_word','equality_labels','block_multiplicities','net_block_exponents','net_positive_degree','net_negative_degree','asymptotic_support_alias_m','alias_statuses','finite_example_min_ratio','finite_example_max_ratio','finite_example_support_m_X1000_H10']);w.writerows(rows)
    # Explicit sufficient finite thresholds behind the one-active-block proof.
    for k in range(2,7):
        for m in range(1,k):
            X_big=10**60;H_big=400;center=10**(60*m//k)
            assert 60*m%k==0 and 3*H_big*F(center,X_big)/(2*PI[0]*k)<1
    # Exact matching test includes different block prime windows and distinctness.
    e=[2,-1,0];allowed=[set((2,3,5)),set((3,5,7)),set((2,7))]
    opt=matching_extrema([2,3,5,7],e,allowed)
    brute=[F(prod(p**max(c,0) for p,c in zip(t,e)),prod(p**max(-c,0) for p,c in zip(t,e))) for t in product([2,3,5,7],repeat=3) if len(set(t))==3 and all(p in a for p,a in zip(t,allowed))]
    assert opt==(min(brute),max(brute))
    atoms=[]
    for ps,es,x,h in (([2]*6,[1]*6,63,100),([2,2,2,3,3,3],[1]*6,215,10),([2,3,11,13,17],[1,1,-1,-1,-1],405,10)):
        dp=int(F(x)*log_interval(x)[0]);atom=tuple_constructor(ps,es,[0]*len(ps),x,h,0,dp-1)
        assert atom['sector']=='NearAlias'
        labels=[ps.index(v) for v in ps];unique={v:i for i,v in enumerate(sorted(set(labels)))};labels=tuple(unique[v] for v in labels)
        nu,e,ap,am=pattern(labels,es);atom['net_block_exponents']=e;atom['new_alias_status']=alias_status(e,atom['m'],nu);atoms.append(atom)
    assert [v['new_alias_status'] for v in atoms]==['closed_one_active_block','closed_no_singleton_blocks','remaining_signed_dilated_product']
    A=F(11501,12500);B=F(137641,250000);J=F(64788151489666079,572357731837500000)
    ideal=J+A/36-B*F(157,630);rel=J+A/36-B*F(34,135)
    grid=[{'H':str(h),'primitive_multiplier':str(1+h/2),'ideal_full_allocation_requirement':str(ideal/(1+h/2)),'relaxed_full_allocation_requirement':str(rel/(1+h/2))} for h in map(F,('1/100','1','10','100','400','1000'))]
    z=10**10;X=z**5;V=z**3;U=X*V;K=V//10000
    lower_sq=F(4999,5000)**2*F(K*K,16*X)
    assert 4*PI[1]*F(K,V)<F(1,50) and 2*PI[1]*F(K,V)<F(1,100) and lower_sq>1
    frozen={}
    for f in ('notes/WP84_DIRECT_CORRELATION_EXPONENT_CELLS.csv','notes/WP84_DIRECT_SIGNED_RESTRICTED_CORRELATION_ATTACK.md','notes/WP84_NEAR_ALIAS_AND_LONG_TAIL_DISCHARGE.md'):
        frozen[f]=hashlib.sha256((ROOT/f).read_bytes()).hexdigest()
    result={'decision':'C','parent':'72b4775f2833f105b4513f97bd4350ee8a0f8ecf','A':str(A),'B':str(B),'Jstar':str(J),'ideal_allowance':str(ideal),'relaxed_allowance':str(rel),'exact_alias_atoms':atoms,'pattern_counts':counts,'total_patterns':len(rows),'finite_example':{'X':1000,'N':72,'H':10,'primes':primes,'scope':'exact extrema; interval support possibility does not assert actual near-resonant tuples'},'matching_window_example':{'net_e':e,'min_ratio':str(opt[0]),'max_ratio':str(opt[1])},'energy_regression':energy_test(),'exact_uniform_slab_volume_checks':slab_checks(),'H_requirements':grid,'H_optimization':{'near_requirement_only':'strictly decreasing in H; supremum allowance as H->0; no positive attained optimizer','if_H_ge_1':'H=1 maximizes permitted primitive error in this conditional surrogate','full_tradeoff':'UNDETERMINED: signed primitive and central/tail charge functions not proved','conditional_surrogate_optimum':'H*=sqrt(2K/E0) for E0*(1+H/2)+K/H; not a feasible arithmetic choice'},'improved_soft_norm_counterexample':{'z':z,'X':X,'U':U,'V':V,'K':K,'H':'1/100','coefficient_envelope':'|a(n)|<=n^(-1/2), |b(v)|<=v^(-1/2)','each_l2_squared_upper':'1','removed_exact_aliases':True,'rotated_nonexact_near_alias_lower_squared':str(lower_sq),'scope':'generic arrays satisfy pointwise envelope and l2 bounds; NOT prime-factor/PNT/BV-compatible'},'new_closed_families_limiting_charge':'0','remaining_near_alias_charge':None,'remaining_ideal_budget':None,'remaining_relaxed_budget':None,'obtained_primitive_bound':None,'minimal_new_lemma':'one-sided weighted sampled nonexact alias correlation over surviving equality-pattern/m pairs at fixed R and one declared admissible H','strict_gt79':'OPEN','frozen_sha256':frozen}
    (ROOT/'notes/WP84_SIGNED_NEAR_ALIAS_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS 14656 sign/equality patterns, exact support extrema, window matching and energy bounds')
    print('Counts:',counts)
    print('H400 relaxed primitive requirement',float(rel/201));print('Decision C: smaller residual lemma unproved; no charged arithmetic bound')
if __name__=='__main__':main()
