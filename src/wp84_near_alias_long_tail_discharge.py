"""Exact alias-sector construction and conditional tail/budget certificates.
No prime correlation bound is inferred from these finite algebraic checks.
"""
from fractions import Fraction as F
from pathlib import Path
from math import factorial,prod
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
PI=(F(333,106),F(355,113))
def log_interval(q,k=36):
    q=F(q);shift=0
    while q>=2:q/=2;shift+=1
    while q<1:q*=2;shift-=1
    def core(v):
        z=(v-1)/(v+1)
        lo=2*sum((z**(2*j+1)/F(2*j+1) for j in range(k)),F(0))
        return lo,lo+2*z**(2*k+1)/(F(2*k+1)*(1-z*z))
    a,b=core(q);c,d=core(F(2))
    return (a+shift*c,b+shift*d) if shift>=0 else (a+shift*d,b+shift*c)
def scale(a,t):return (a[0]*t,a[1]*t) if t>=0 else (a[1]*t,a[0]*t)
def subtract(a,b):return a[0]-b[1],a[1]-b[0]
def absolute(a):
    if a[0]>=0:return a
    if a[1]<=0:return -a[1],-a[0]
    return F(0),max(-a[0],a[1])
def classify(q,X,H):
    q,X,H=F(q),F(X),F(H);L=log_interval(X);lam=log_interval(q)
    middle=(lam[0]+lam[1])/(L[0]+L[1]);m=(middle+F(1,2)).numerator//(middle+F(1,2)).denominator
    delta=subtract(lam,scale(L,m));ad=absolute(delta)
    assert ad[1]<L[0]/2, 'nearest-bin boundary needs separate interval refinement'
    if q==X**m:return {'m':m,'sector':'EXACT_CENTRAL' if m==0 else 'EXACT_ALIAS','removed':True}
    threshold=(H/(2*PI[1]*X),H/(2*PI[0]*X))
    if ad[1]<threshold[0]:sector='Central' if m==0 else 'NearAlias'
    elif ad[0]>threshold[1]:sector='LongTail'
    else:sector='BOUNDARY_UNRESOLVED'
    return {'m':m,'sector':sector,'removed':False}
def tuple_constructor(primes,signs,lags,X,H,kminus,kplus):
    assert len(primes)==len(signs)==len(lags) and sum(lags)==0
    assert len(primes) in (5,6)
    assert all(e in (-1,1) for e in signs)
    assert all(p>=2 and all(p%q for q in range(2,int(p**0.5)+1)) for p in primes)
    L_bounds=log_interval(X)
    for p in primes:
        gap=L_bounds[0]-log_interval(p)[1]
        assert gap>0 and gap*gap>=L_bounds[1], 'leaf exceeds natural cutoff'
    assert kplus-kminus+1<=int(F(X)*L_bounds[0])
    u=[0]
    for l in lags:u.append(u[-1]+l)
    imin=kminus-min(u);imax=kplus-max(u);M=max(0,imax-imin+1);d=kplus-kminus+1
    plus=prod(p for p,e in zip(primes,signs) if e==1);minus=prod(p for p,e in zip(primes,signs) if e==-1)
    return {'degree':len(primes),'omega':str(-F(11501,12500) if len(primes)==5 else F(137641,250000)),'section':[kminus,kplus],'prefix_displacements':u,'equality_labels':[primes.index(p) for p in primes],'slot_weights':[{'prime':p,'cp':f'-log({p})/(a_phi*L*sqrt({p}))','filter_lag':l,'filter_sign':e,'path_phase':f'exp(2*pi*i*({e*u[j]})*log({p})/L)','window':'full natural ordinary-prime cutoff; no window discarded'} for j,(p,e,l) in enumerate(zip(primes,signs,lags))],'primes':primes,'signs':signs,'lags':lags,'root_count':M,'dprime':d,'i_min':imin,'product_ratio':str(F(plus,minus)),**classify(F(plus,minus),X,H),'exact_kernel':'exp(i*T*lambda)*exp(2*pi*i*i_min*lambda/L)/dprime * sum_{k=0}^{M-1}exp(2*pi*i*k*lambda/L)','normalization':'1/dprime; every original cp, filter, path phase and tuple mask retained'}
def sin_pi_interval(t,k=16):
    t=F(t)%2;sgn=1
    if t>1:t-=1;sgn=-1
    if t>F(1,2):t=1-t
    if t==F(1,2):return (F(1),F(1)) if sgn==1 else (F(-1),F(-1))
    lo,hi=t*PI[0],t*PI[1]
    # sin increasing on [0,pi/2]; endpoint pi/2 needs upper=1.
    def bounds(x):
        terms=[(-1)**j*x**(2*j+1)/F(factorial(2*j+1)) for j in range(k)]
        val=sum(terms,F(0));err=x**(2*k+1)/F(factorial(2*k+1))
        return val-err,val+err
    a=bounds(lo)[0];b=F(1) if hi>=PI[0]/2 else bounds(hi)[1]
    return (max(F(0),a),min(F(1),b)) if sgn==1 else (-min(F(1),b),-max(F(0),a))
def kernel_checks():
    checks=0
    for d,M in ((17,11),(23,23),(31,29)):
        for j in range(1,4*d+1):
            z=F(j,8*d);den=sin_pi_interval(z);num=absolute(sin_pi_interval(M*z))
            upper=num[1]/(d*den[0]);bound=min(F(M,d),1/(2*d*z))
            assert upper<=bound;checks+=1
    return checks
def main():
    A=F(11501,12500);B=F(137641,250000);J=F(64788151489666079,572357731837500000)
    ideal=J+A/36-B*F(157,630);rel=J+A/36-B*F(34,135)
    # Natural X=63, N>=7 (checked independently in note); full section d=floor(X log X).
    L=log_interval(63);d=int(63*L[0]);assert d==int(63*L[1])
    cases=[tuple_constructor([2]*6,[1]*6,[0]*6,63,100,0,d-1),tuple_constructor([2]*6,[1]*6,[0]*6,63,1,0,d-1),tuple_constructor([5,7,2,3,5],[1,1,-1,-1,-1],[0]*5,63,100,0,d-1),tuple_constructor([7]*6,[1]*6,[0]*6,63,100,0,d-1),tuple_constructor([2]*6,[1]*6,[0]*6,64,100,0,260)]
    assert [c['sector'] for c in cases]==['NearAlias','LongTail','Central','LongTail','EXACT_ALIAS']
    # Nonzero path: repeated compression has root count d-2, not d.
    path=tuple_constructor([5,7,2,3,5],[1,1,-1,-1,-1],[1,1,-1,-1,0],63,100,0,d-1)
    assert path['root_count']==d-2
    H=400;near_factor=1+F(H,2)
    m=1000;X=m**5;v=m**3;K=v//10000
    phase_upper=4*PI[1]*F(K,v);assert phase_upper<F(1,50)
    lower_square=F(4999,5000)**2*K
    pins={}
    for f in ('notes/WP84_DIRECT_CORRELATION_EXPONENT_CELLS.csv','notes/WP84_DIRECT_SIGNED_CORRELATION_CERTIFICATE.json','notes/WP84_DIRECT_SIGNED_RESTRICTED_CORRELATION_ATTACK.md'):
        pins[f]=hashlib.sha256((ROOT/f).read_bytes()).hexdigest()
    result={'decision':'F','parent':'6667160c71f198a2419d9f93000a4afdfb23b425','A':str(A),'B':str(B),'Jstar':str(J),'ideal_allowance':str(ideal),'relaxed_allowance':str(rel),'exact_examples':cases,'displaced_root_example':path,'rational_interval_kernel_checks':kernel_checks(),'near_alias_primitive_example':{'H':H,'multiplier_upper':str(near_factor),'ideal_allocation_primitive_max':str(ideal/near_factor),'relaxed_allocation_primitive_max':str(rel/near_factor),'scope':'conditional on signed primitive estimate; none proved'},'soft_alias_norm_counterexample':{'m':m,'X':X,'v':v,'positive_cluster_count':K,'positive_start':X*v+1,'each_l2_squared':1,'nonexact_only':True,'phase_upper':str(phase_upper),'rotated_real_correlation_lower_squared':str(lower_square),'scope':'generic coefficient norms only; not prime-compatible, not pointwise prime-envelope-compatible'},'certified_bound_formulas':{'near_alias_dyadic':'r!s! |a_phi|^(-b) [14 H sqrt(UV)/T + sqrt(min(U,V)/max(U,V))]','tail_envelope':'sum_LongTail |omega_b W| min(M_l/dprime,L/(2 dprime |delta|))','tail_primitive_multiplier':'1/dprime+pi log(T L/(2H))+pi L/(4dprime)*(T/H-2/L)','scope':'valid bounds, not certified small limiting charges'},'closed_removed_limiting_charge':'0','certified_near_alias_charge':None,'certified_long_tail_charge':None,'certified_total_side_charge':None,'remaining_paid_allowance':None,'uncharged_reference_allowances_preserved':True,'central_only_reduction':False,'strict_gt79':'OPEN','frozen_sha256':pins}
    (ROOT/'notes/WP84_NEAR_ALIAS_LONG_TAIL_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact alias examples, actual root intervals,',result['rational_interval_kernel_checks'],'rational interval kernel bounds')
    print('Conditional near primitive maxima:',float(ideal/near_factor),float(rel/near_factor))
    print('Decision F: both side charges remain uncertified; no central-only reduction')
if __name__=='__main__':main()
