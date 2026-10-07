"""Independent cosine-Gram replay of sector and budget certificates."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial,prod
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
j=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_LONG_TAIL_CERTIFICATE.json').read_text())
plo=F(333,106);phi=F(355,113)
def cos_upper(r):
    r=F(r)%2
    if r>1:r=2-r
    if r==0:return F(1)
    if r==1:return F(-1)
    if r==F(1,2):return F(0)
    x=r*plo
    return min(F(1),sum(((-1)**k*x**(2*k)/F(factorial(2*k)) for k in range(20)),F(0))+x**40/F(factorial(40)))
# Verify the elementary exponential constant in the lattice count.
k=12
exp2_upper=sum((F(2)**i/F(factorial(i)) for i in range(k+1)),F(0))+F(2)**(k+1)/F(factorial(k+1))/(1-F(2,k+2))
assert exp2_upper<8
checks=0
for d,M in ((17,11),(23,23),(31,29)):
    for znum in range(1,4*d+1):
        z=F(znum,8*d)
        # Expand squared sampled sum directly, instead of producer's sine quotient.
        upper=(M+2*sum((F(M-k)*cos_upper(2*k*z) for k in range(1,M)),F(0)))/d**2
        envelope=min(F(M,d),1/(2*d*z))**2
        assert upper<=envelope;checks+=1
assert checks==j['rational_interval_kernel_checks']==284
cases=j['exact_examples']
for c in cases:
    q=F(prod(p for p,e in zip(c['primes'],c['signs']) if e==1),prod(p for p,e in zip(c['primes'],c['signs']) if e==-1))
    assert q==F(c['product_ratio'])
    assert c['root_count']==c['dprime']
# Separate elementary log inequalities verify the nonexact classifications.
# log(64/63) in [1/64,1/63]; L=log63>=5log2>=10/3.
assert F(1,63)<F(100)/(2*phi*63)
assert F(1,64)>F(1)/(2*plo*63)
assert cases[0]['m']==cases[1]['m']==1
# central 35/30=7/6: log(7/6)<=1/6; nearest bin zero.
assert F(1,6)<F(100)/(2*phi*63)
assert F(cases[2]['product_ratio'])==F(7,6) and cases[2]['m']==0
# 7^6/63^3 in (2/5,1/2): log distance >log2>=2/3, <log(5/2)<=3/2<L/2.
ratio=F(7**6,63**3)
assert F(2,5)<ratio<F(1,2)
assert F(2,3)>F(100)/(2*plo*63)
assert F(3,2)<F(5,3) and cases[3]['m']==3
assert F(cases[4]['product_ratio'])==64 and cases[4]['m']==1
assert [c['sector'] for c in cases]==['NearAlias','LongTail','Central','LongTail','EXACT_ALIAS']
path=j['displaced_root_example'];walk=[0]
for l in path['lags']:walk.append(walk[-1]+l)
assert path['root_count']==path['dprime']-(max(walk)-min(walk))
A=F(j['A']);B=F(j['B']);J=F(j['Jstar'])
ideal=J+A/36-B*F(157,630);rel=J+A/36-B*F(34,135)
assert ideal==F(27704610381502,17886179119921875)==F(j['ideal_allowance'])
assert rel==F(52897896569489,572357731837500000)==F(j['relaxed_allowance'])
near=j['near_alias_primitive_example'];factor=1+F(near['H'],2)
assert factor==201==F(near['multiplier_upper'])
assert F(near['ideal_allocation_primitive_max'])*factor==ideal
assert F(near['relaxed_allocation_primitive_max'])*factor==rel
soft=j['soft_alias_norm_counterexample'];v=soft['v'];K=soft['positive_cluster_count']
assert K==v//10000 and 4*phi*F(K,v)<F(1,50)
assert F(soft['rotated_real_correlation_lower_squared'])==F(4999,5000)**2*K
for f,h in j['frozen_sha256'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
assert all(j[k] is None for k in ('certified_near_alias_charge','certified_long_tail_charge','certified_total_side_charge','remaining_paid_allowance'))
print('PASS independent cosine-Gram interval bounds, elementary-log sector replay, joint budgets and frozen source hashes')
