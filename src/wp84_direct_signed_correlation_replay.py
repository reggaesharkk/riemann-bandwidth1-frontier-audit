"""Independent divisor-enumeration replay; no convolution helper imported."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import comb
import json,csv,sympy as s
ROOT=Path(__file__).resolve().parents[1]
def tuples(n,k):
    if k==1:
        yield (n,);return
    for d in s.divisors(n):
        for tail in tuples(n//d,k-1):yield (int(d),)+tail
def logs(n):return dict(s.factorint(n))
def add(out,scale,n):
    for p,v in logs(n).items():out[p]=out.get(p,0)+scale*v
for n in range(1,121):
    hb={};va={}
    for j in range(1,4):
        for t in tuples(n,2*j):
            if max(t[:j])<=7:
                scale=(-1)**(j-1)*comb(3,j)
                for a in t[:j]:scale*=int(s.mobius(a))
                add(hb,scale,t[-1])
    for a,b in tuples(n,2):
        if a<=5:add(va,int(s.mobius(a)),b)
    for a,b,c in tuples(n,3):
        if c>1 and len(logs(c))==1:
            if a<=5 and c<=7:add(va,-int(s.mobius(a)),next(iter(logs(c))))
            if a>5 and c>7:add(va,int(s.mobius(a)),next(iter(logs(c))))
    if 1<n<=7 and len(logs(n))==1:add(va,1,next(iter(logs(n))))
    expected={next(iter(logs(n))):1} if len(logs(n))==1 else {}
    assert {p:v for p,v in hb.items() if v}==expected
    assert {p:v for p,v in va.items() if v}==expected
j=json.loads((ROOT/'notes/WP84_DIRECT_SIGNED_CORRELATION_CERTIFICATE.json').read_text())
a=[F(-19101,185500),F(961,3710),F(31,50),F(-371,500)]
c=[sum((a[u]*a[v] for u in range(4) for v in range(4) if u+v==b),F(0)) for b in range(7)]
assert c[4]==0 and c[5]==-F(j['A']) and c[6]==F(j['B'])
jstar=F(21,200)-c[0]-c[2]/3-F(128952763,92407500000)-F(26060119,12734908593750)
assert jstar==F(j['Jstar'])
assert jstar-c[5]/36-c[6]*F(157,630)==F(j['ideal_joint_allowance'])
assert jstar-c[5]/36-c[6]*F(34,135)==F(j['relaxed_joint_allowance'])
with (ROOT/'notes/WP84_DIRECT_CORRELATION_EXPONENT_CELLS.csv').open() as f:
    rows=list(csv.DictReader(f))
assert len(rows)==9216
counts={}
for row in rows:
    assert None not in row
    b=int(row['degree']);r=int(row['plus_count'])
    intervals=[tuple(map(F,row[f'window{i}'].split(':'))) for i in range(1,b+1)]
    pos=[sum(x[k] for x in intervals[:r]) for k in (0,1)]
    neg=[sum(x[k] for x in intervals[r:]) for k in (0,1)]
    if min(pos[1],neg[1])<max(pos[0],neg[0]):label='central_resonance_support_empty'
    elif pos[1]==neg[0] or neg[1]==pos[0]:label='resonance_boundary'
    elif pos[1]+neg[1]<2:label='fixed_gap_mean_value_short'
    elif pos[0]+neg[0]>2:label='supercritical_long'
    else:label='critical_or_length_transition'
    assert row['class']==label
    key=str((b,r));counts.setdefault(key,{});counts[key][label]=counts[key].get(label,0)+1
assert counts==j['cell_counts']
assert 1-1/F(6,5)==F(1,6)
assert F(8,9)-1+F(1,6)==F(1,18)
assert F(7,8)-1+F(1,6)==F(1,24)
soft=j['soft_l2_counterexample'];m=soft['m'];K=soft['cluster_length'];T=m**5;N=m**6
assert F(2*T*(K-1),N)<F(1,50)
assert F(4999,5000)*(K-1)==F(soft['nonexact_real_correlation_lower'])
print('PASS independent divisor-tuple Vaughan/HB replay (120 integers)')
print('PASS consumer coefficient convolution, exact allowances, 9216 cells, shift/loss exponents and soft-norm counterexample')
