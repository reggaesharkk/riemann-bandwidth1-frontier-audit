#!/usr/bin/env python3
"""Exact gate for the rational canonical one-pole fixed-band fallback."""

from fractions import Fraction as F
import sympy as sp

x,y=sp.symbols("x y")
A=sp.Rational(43428,13891)
B=sp.Rational(37704,13891)
C=sp.Rational(9660,13891)
P=1-A*x+B*x**2-C*x**3
a=sp.Rational(1129,1000)

def integer_poly(expr,var):
    p=sp.Poly(expr,var,domain=sp.QQ)
    L=sp.ilcm(*[c.q for c in p.all_coeffs()])
    return sp.Poly(sp.expand(expr*L),var,domain=sp.ZZ),L

def main():
    # Exact half-line support.
    N=sp.expand(a**6*P.subs(x,-y)**2-(y**2+a**2)**3)
    Np,L=integer_poly(N,y)
    coeff=[Np.coeff_monomial(y**k) for k in range(7)]
    assert coeff[0]==0
    assert all(c>0 for c in coeff[1:])

    # Exact bounded consumer and global curvature certificate.
    p=sp.factor(a**6*P**2/(x**2+a**2)**3)
    ppp=sp.factor(sp.diff(p,x,2))
    num,den=map(sp.expand,sp.fraction(ppp))

    M=sp.Rational(261637,10000)
    qp,_=integer_poly(M*den+num,x)
    qm,_=integer_poly(M*den-num,x)

    assert sp.count_roots(qp,-sp.oo,sp.oo)==0
    assert sp.count_roots(qm,-sp.oo,sp.oo)==0
    assert qp.eval(0)>0
    assert qm.eval(0)>0

    # Pointwise domination is algebraic:
    # p/P^2 = a^6/(x^2+a^2)^3 <= 1 on R.

    pi_lo=F(333,106)
    Mq=F(261637,10000)
    Cband=3*Mq/(pi_lo*pi_lo)
    assert Cband==F(734938333,92407500)

    w0=F(1415,13891)
    ceiling=F(21,200)
    margin=ceiling-w0
    assert margin==F(8711,2778200)

    # First integer R with Cband/R < model margin.
    R0=1
    while Cband/R0>=margin:
        R0+=1
    assert R0==2537

    expected={
        3000:(
            F(28373424167,277222500000),
            F(1865397603797,3850897747500000),
        ),
        5300:(
            F(956411989,9240750000),
            F(209857689199,128363258250000),
        ),
    }
    for R,(target,allow) in expected.items():
        got=ceiling-Cband/R
        assert got==target
        assert got-w0==allow
        assert allow>0

    pair_cost=F(3024696,1929598810)
    Rpair=1
    while ceiling-Cband/Rpair-w0<=pair_cost:
        Rpair+=1
    assert Rpair==5073

    print("support coefficients (scaled) =",coeff)
    print("GLOBAL_CURVATURE_BOUND: |p_a''| <",M)
    print("C_band <=",Cband,"~",float(Cband))
    print("first model-positive R =",R0)
    for R,(target,allow) in expected.items():
        print("R",R,"square target <",target,"~",float(target))
        print("R",R,"allowance above w0 =",allow,"~",float(allow))
    print("first R exceeding pair-only m4 cost =",Rpair)
    print("RESULT: WP84_RATIONAL_CANONICAL_ONE_POLE_BAND_PASS")

if __name__=="__main__":
    main()
