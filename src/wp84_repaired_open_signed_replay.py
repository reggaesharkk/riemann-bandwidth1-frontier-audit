"""Independent exponential-integral and full R1 pairing replay."""
from pathlib import Path
from itertools import permutations,product
from fractions import Fraction as F
from copy import deepcopy
import sympy as s,json
ROOT=Path(__file__).resolve().parents[1]
h=s.symbols('h')
def J(n,k):
    if k==0:return s.Rational(1,n+1)
    if n==0:return 0
    return s.expand(h/k-n*h*J(n-1,k)/k)
def leaf(l,e):
    if l==0:return [(0,0,1),(1,0,-1)]
    return [(0,0,e*h/l),(0,e*l,-e*h/l)]
cache={}
for l,m,d in product(range(-1,2),range(-1,2),range(-8,9)):
    z=sum(a*b*J(1+n+nn,d+k+kk) for n,k,a in leaf(l,1) for nn,kk,b in leaf(m,-1))
    z=s.Poly(s.expand(z+z.subs(h,-h)),h)
    assert all(power[0]%2==0 for power,coef in z.terms())
    cache[l,m,d]={power[0]//2:F(coef) for power,coef in z.terms() if coef}
# Independent perfect matchings by permutation quotient.
matchings=set()
for p in permutations(range(8)):
    matchings.add(tuple(sorted(tuple(sorted(p[i:i+2])) for i in range(0,8,2))))
assert len(matchings)==105
out=[F(0)]*5
for lag in product((-1,0,1),repeat=8):
    if sum(lag):continue
    u=[0]
    for l in lag:u.append(u[-1]+l)
    for pi in matchings:
        if (6,7) in pi and lag[6:]==(0,0):continue
        opened=sum(lag[i]+lag[j]!=0 for i,j in pi)
        if not opened:continue
        polynomial={0:F(opened,4)}
        for i,j in pi:
            new={}
            for k,a in polynomial.items():
                for t,b in cache[lag[i],lag[j],u[i]-u[j]].items():new[k+t]=new.get(k+t,F(0))+a*b
            polynomial=new
        for k,v in polynomial.items():out[k]+=v
c=json.loads((ROOT/'notes/WP84_REPAIRED_OPEN_PATH_SIGNED_CERTIFICATE.json').read_text())
def check(c):
    assert list(map(F,c['R1_O8_diagonal_polynomial_in_x']))==out
    assert out[0]==out[1]==0 and out[2]>0 and out[3]<0 and out[4]>0
    w=c['witness'];p=list(map(F,w['p_coefficients']));m=list(map(F,w['relaxed_completion_moments']));E=sum(p[i]*m[i] for i in range(9))
    assert F(c['allowance_ceiling'])==F(21,200)-E
    assert c['fully_paid_budget']=='UNCERTIFIED' and c['mu7_mu8']=='NO-GO'
check(c)
for kind in range(2):
    bad=deepcopy(c)
    if kind==0:bad['R1_O8_diagonal_polynomial_in_x'][2]='0'
    else:bad['allowance_ceiling']='1'
    try:check(bad)
    except AssertionError:pass
    else:raise AssertionError('corruption accepted')
print('PASS independent 105-pairing full diagonal, exponential integration, ledger and two corruption tests')
