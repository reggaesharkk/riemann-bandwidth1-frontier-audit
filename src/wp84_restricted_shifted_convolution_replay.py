"""Exact continuation regressions; finite identities, not an arithmetic theorem."""
from itertools import combinations,product
from math import factorial,gcd,prod
from pathlib import Path
import json
import sympy as s
from wp84_c5_pointwise_supercritical_sign import arrangement,c5,outer_overlap,dot

def main():
    m=s.symbols('m',positive=True,integer=True)
    # d=m^4, a single eigenvalue m: small normalized HS, divergent sixth mass.
    assert s.simplify(m**2/m**4-m**-2)==0
    assert s.simplify(m**6/m**4-m**2)==0
    # q equal Fourier coefficients 1/q: coefficient L2=1/q, coherent sample=1.
    q=s.symbols('q',positive=True,integer=True)
    assert s.simplify(q*(1/q)**2-1/q)==0
    assert q*(1/q)==1
    # Exact grouping, including distinctness within arrays and across the shift.
    primes=[2,3,5,7,11];g=[{p:s.Rational(p+j,17)+s.I*s.Rational(j+1,p) for p in primes} for j in range(5)]
    kernel=lambda n,b:s.Rational(n, n+b)+s.I*s.Rational(n-b,n*b)
    direct=0;a2={};a3={}
    for ps in product(primes,repeat=2):
        if len(set(ps))<2:continue
        n=prod(ps);a2[n]=a2.get(n,0)+g[0][ps[0]]*g[2][ps[1]]
    for ps in product(primes,repeat=3):
        if len(set(ps))<3:continue
        n=prod(ps);a3[n]=a3.get(n,0)+g[1][ps[0]]*g[3][ps[1]]*g[4][ps[2]]
    for ps in product(primes,repeat=5):
        if len(set(ps))<5:continue
        n=ps[0]*ps[2];b=ps[1]*ps[3]*ps[4]
        direct+=g[0][ps[0]]*g[2][ps[2]]*s.conjugate(g[1][ps[1]]*g[3][ps[3]]*g[4][ps[4]])*kernel(n,b)
    grouped=sum(a*s.conjugate(b)*kernel(n,k) for n,a in a2.items() for k,b in a3.items() if gcd(n,n-k)==1)
    assert s.expand(direct-grouped)==0
    assert s.Rational(10,9)!=s.Rational(20,19) # same shift, different carrier/kernel argument
    # Exact all-five-neighborhood integral in a single affine chamber.
    center=[s.Rational(3,5),-s.Rational(2,5),s.Rational(3,5),-s.Rational(2,5)]
    delta=s.Rational(1,100)
    from fractions import Fraction as F
    cf=[F(str(x)) for x in center]
    assert all(abs(dot(a,cf)-b)>F(1,100)*sum(abs(x) for x in a) for a,b in arrangement())
    assert c5(cf)==F(1,5) and outer_overlap(cf)==F(1,5)
    t=s.symbols('t0:4');d=s.symbols('d');y=[d*(2*v-1) for v in t]
    P=(s.Rational(1,5)+y[0]+y[2])*(s.Rational(1,5)-y[0]-y[1]-y[2])
    def below(a):
        result=0
        for mask in product([0,1],repeat=4):
            z=a-sum(mask)
            if z<=0:continue
            poly=s.Poly(s.expand(P.subs({t[i]:t[i]+mask[i] for i in range(4)},simultaneous=True)),*t)
            for powers,coef in poly.terms():
                result+=(-1)**sum(mask)*coef*prod(factorial(k) for k in powers)*z**(4+sum(powers))/factorial(4+sum(powers))
        return result
    masspoly=s.factor((2*d)**4*(below(s.Rational(5,2))-below(s.Rational(3,2))))
    mass=s.factor(masspoly.subs(d,delta));assert 0<mass<s.Rational(1,36)
    out={'regressions':'PASS','proper_power_status':'CLOSED bounded signed-gate equivalence',
         'HS_counterexample':'dimension m^4, eigenvalue m: HS^2=m^-2, sixth mass=m^2',
         'coefficient_L2_counterexample':'q coefficients 1/q: L2^2=1/q, coherent sample=1',
         'restricted_shift_grouping':'PASS including gcd(n,h)=1',
         'kernel_h_only_factorization':False,'balanced_neighborhood_delta':'1/100',
         'balanced_neighborhood_mass_polynomial':str(masspoly),'balanced_neighborhood_mass':str(mass),
         'balanced_neighborhood_fraction_total':str(36*mass),
         'point_mass':'0','fixed_dyadic_cell_limiting_model_mass':'0',
         'BBMZ_first_average_threshold':'Q >= N^(1/6+epsilon)',
         'BBMZ_second_average_threshold':'Q >= N^(1/3+epsilon)',
         'arithmetic_theorem_proved':False}
    (Path(__file__).resolve().parents[1]/'notes/WP84_RESTRICTED_SHIFTED_CONVOLUTION_REPLAY.json').write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
