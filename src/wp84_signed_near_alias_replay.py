"""Independent near-alias replay: exponential intersections, patterns and budgets."""
from pathlib import Path
from fractions import Fraction as F
from math import prod,factorial
from itertools import product
import csv,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
j=json.loads((ROOT/'notes/WP84_SIGNED_NEAR_ALIAS_CERTIFICATE.json').read_text())
rows=list(csv.DictReader((ROOT/'notes/WP84_SIGNED_NEAR_ALIAS_SUPPORT.csv').open()))
assert len(rows)==14656
primes=j['finite_example']['primes'];X=1000;H=10
alo=F(H)/(2*F(355,113)*X);ahi=F(H)/(2*F(333,106)*X)
def exp_low(x):return sum((x**k/F(factorial(k)) for k in range(8)),F(0))
def exp_high(x):return exp_low(x)+x**8/F(factorial(8))/(1-x/9)
elo=exp_low(alo);ehi=exp_high(ahi)
counts={};keys=set()
for row in rows:
    b=int(row['degree']);signs=[1 if c=='+' else -1 for c in row['sign_word']]
    labs=list(map(int,row['equality_labels'].split(',')));k=max(labs)+1
    nu=[sum(v==i for v in labs) for i in range(k)]
    e=[sum(signs[t] for t in range(b) if labs[t]==i) for i in range(k)]
    assert nu==list(map(int,row['block_multiplicities'].split(','))) and e==list(map(int,row['net_block_exponents'].split(',')))
    ap=sum(v for v in e if v>0);am=-sum(v for v in e if v<0)
    assert ap==int(row['net_positive_degree']) and am==int(row['net_negative_degree'])
    expected=[] if not ap+am else [m for m in range(1-am,ap) if m]
    got=list(map(int,row['asymptotic_support_alias_m'].split(','))) if row['asymptotic_support_alias_m'] else []
    assert got==expected
    pos=sorted([v for v in e if v>0],reverse=True);neg=sorted([-v for v in e if v<0],reverse=True)
    qlo=F(prod(primes[t]**v for t,v in enumerate(pos)),prod(primes[-1-t]**v for t,v in enumerate(neg)))
    qhi=F(prod(primes[-1-t]**v for t,v in enumerate(pos)),prod(primes[t]**v for t,v in enumerate(neg)))
    assert qlo==F(row['finite_example_min_ratio']) and qhi==F(row['finite_example_max_ratio'])
    finite=[]
    for m in range(-6,7):
        if not m:continue
        center=F(X)**m
        if qhi>=center/elo and qlo<=center*elo:finite.append(m)
        else:assert qhi<center/ehi or qlo>center*ehi
    actual=list(map(int,row['finite_example_support_m_X1000_H10'].split(','))) if row['finite_example_support_m_X1000_H10'] else []
    assert finite==actual
    statuses=[]
    for m in got:
        if sum(v!=0 for v in e)==1:z='closed_one_active_block'
        elif min(nu)>=2:z='closed_no_singleton_blocks'
        elif (ap==0 or am==0) and abs(m)==1:z='closed_one_side_first_alias'
        else:z='remaining_signed_dilated_product'
        statuses.append(z)
    assert statuses==(row['alias_statuses'].split(',') if row['alias_statuses'] else [])
    key=str(b);counts.setdefault(key,{'patterns':0,'support_alias_slots':0,'closed_one_active_block':0,'closed_one_side_first_alias':0,'closed_no_singleton_blocks':0,'remaining_signed_dilated_product':0})
    counts[key]['patterns']+=1
    for z in statuses:counts[key]['support_alias_slots']+=1;counts[key][z]+=1
    keys.add((b,row['sign_word'],tuple(labs)))
assert len(keys)==14656 and counts==j['pattern_counts']
assert counts['5']['patterns']==52*32 and counts['6']['patterns']==203*64
A=F(j['A']);B=F(j['B']);J=F(j['Jstar']);ideal=J+A/36-B*F(157,630);rel=J+A/36-B*F(34,135)
assert ideal==F(j['ideal_allowance']) and rel==F(j['relaxed_allowance'])
prev=None
for row in j['H_requirements']:
    h=F(row['H']);f=1+h/2;v=F(row['relaxed_full_allocation_requirement'])
    assert f==F(row['primitive_multiplier']) and v*f==rel
    assert F(row['ideal_full_allocation_requirement'])*f==ideal
    if prev is not None:assert v<prev
    prev=v
assert F(j['H_requirements'][4]['relaxed_full_allocation_requirement'])==rel/201
soft=j['improved_soft_norm_counterexample'];z=soft['z'];X=z**5;V=z**3;K=V//10000
assert soft['U']==X*V and soft['V']==V and soft['K']==K
assert 2*F(355,113)*F(K,V)<F(1,100)
assert F(soft['rotated_nonexact_near_alias_lower_squared'])==F(4999,5000)**2*F(K*K,16*X)>1
# Independent sum-of-divisor representations checks the rational energy regression.
e=j['energy_regression'];ps=e['prime_list'];r=e['r'];d={}
for tup in product(ps,repeat=r):
    n=prod(tup);d[n]=d.get(n,F(0))+F(1,n)
assert sum((v*v for v in d.values()),F(0))==F(e['weighted_energy'])
assert F(e['energy_bound'])==factorial(r)*sum((F(1,p*p) for p in ps),F(0))**r
for f,h in j['frozen_sha256'].items():assert hashlib.sha256((ROOT/f).read_bytes()).hexdigest()==h
assert j['exact_uniform_slab_volume_checks']==864
assert F(8,5)*(F(1,2)+F(7,64))==F(39,40)
assert F(39,40)-F(11,10)+F(3,5)==F(19,40)
assert j['remaining_near_alias_charge'] is None and j['obtained_primitive_bound'] is None
print('PASS 14656 independent pattern/range records; exponential core intersections; H targets; energy, soft-bound and frozen-hash checks')
