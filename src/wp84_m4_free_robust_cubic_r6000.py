#!/usr/bin/env python3
"""Exact regression gate for the m4-free robust cubic >79 fallback."""

from fractions import Fraction as F
import sympy as sp

x,y=sp.symbols("x y")

# Centered cubic.
a0=F(-19101,185500)
a1=F(961,3710)
a2=F(31,50)
a3=F(-371,500)

def S(q):
    return sp.Rational(q.numerator,q.denominator)

q=S(a0)+S(a1)*y+S(a2)*y**2+S(a3)*y**3
P=sp.expand(q.subs(y,x-1))

P_expected=(
    1
    -sp.Rational(594893,185500)*x
    +sp.Rational(1423,500)*x**2
    -sp.Rational(371,500)*x**3
)
assert sp.expand(P-P_expected)==0

q2=sp.expand(q**2)
c=[sp.factor(q2.coeff(y,k)) for k in range(7)]
expected=[
    sp.Rational(364848201,34410250000),
    -sp.Rational(18356061,344102500),
    -sp.Rational(26060119,430128125),
    sp.Rational(21981971,46375000),
    sp.Rational(0),
    -sp.Rational(11501,12500),
    sp.Rational(137641,250000),
]
assert c==expected
assert c[4]==0

# Robust centered moment ledger.
mu=[
    sp.Rational(1),
    sp.Rational(0),
    sp.Rational(1,3),
    sp.Rational(0),
    sp.Symbol("mu4"),
    sp.Rational(1,36),
    sp.Rational(34,135),
]
E=sp.expand(sum(c[k]*mu[k] for k in range(7)))
assert not E.has(mu[4])
Erob=sp.factor(E)
assert Erob==sp.Rational(240421959557,2322691875000)

# One-pole bounded consumer.
a=sp.Rational(221,200)
p=sp.factor(a**6*P**2/(x**2+a**2)**3)

# Half-line support: exact positive coefficient test after x=-y.
N=sp.expand(a**6*P.subs(x,-y)**2-(y**2+a**2)**3)
Np=sp.Poly(N,y,domain=sp.QQ)
assert Np.coeff_monomial(1)==0
assert all(Np.coeff_monomial(y**k)>0 for k in range(1,7))

# Exact curvature Sturm gate.
fpp=sp.factor(sp.diff(p,x,2))
num,den=map(sp.expand,sp.fraction(fpp))
M=sp.Rational(137721,5000)

def integer_poly(expr):
    poly=sp.Poly(expr,x,domain=sp.QQ)
    L=sp.ilcm(*[z.q for z in poly.all_coeffs()])
    return sp.Poly(sp.expand(expr*L),x,domain=sp.ZZ)

qp=integer_poly(M*den+num)
qm=integer_poly(M*den-num)
assert sp.count_roots(qp,-sp.oo,sp.oo)==0
assert sp.count_roots(qm,-sp.oo,sp.oo)==0
assert qp.eval(0)>0
assert qm.eval(0)>0

# Exact band budget.
pi_lo=F(333,106)
Mq=F(137721,5000)
Cband=3*Mq/(pi_lo*pi_lo)
assert Cband==F(128952763,15401250)

R=6000
band=Cband/R
c2abs=F(26060119,430128125)
variance=c2abs*F(2)/(pi_lo*pi_lo*R)
assert variance==F(26060119,12734908593750)

ceiling=F(21,200)
Erob_q=F(240421959557,2322691875000)
margin=ceiling-Erob_q-band-variance
assert margin==F(52897896569489,572357731837500000)
assert margin>0

R0=1
while ceiling-Erob_q-Cband/R0-c2abs*F(2)/(pi_lo*pi_lo*R0)<=0:
    R0+=1
assert R0==5628

print("P_dag =",sp.factor(P))
print("centered coefficients =",c)
print("ROBUST_MOMENT_BOUND =",Erob)
print("GLOBAL_CURVATURE_BOUND: |p_dag''| <",M)
print("C_band <=",Cband,"~",float(Cband))
print("R =",R)
print("band charge =",band,"~",float(band))
print("variance deficit charge =",variance,"~",float(variance))
print("final residual below 0.105 =",margin,"~",float(margin))
print("first positive-budget integer R =",R0)
print("TARGET: mu5_c >= 1/36-o(1), mu6_c <= 34/135+o(1), no mu4 target")
print("RESULT: WP84_M4_FREE_ROBUST_CUBIC_R6000_PASS")
