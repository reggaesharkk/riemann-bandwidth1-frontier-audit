#!/usr/bin/env python3
"""Exact Sturm and rational-budget gate for the delta=79 functional-band rung."""

from fractions import Fraction as F
import sympy as sp

x=sp.symbols("x")
A=sp.Rational(43428,13891)
B=sp.Rational(37704,13891)
C=sp.Rational(9660,13891)
P=1-A*x+B*x**2-C*x**3
g=sp.expand(P**2)
f=sp.factor(80*g/(g+79))
fpp=sp.factor(sp.diff(f,x,2))
num,den=map(sp.expand,sp.fraction(fpp))

def integer_poly(expr):
    p=sp.Poly(expr,x,domain=sp.QQ)
    L=sp.ilcm(*[c.q for c in p.all_coeffs()])
    return sp.Poly(sp.expand(expr*L),x,domain=sp.ZZ)

def main():
    qp=integer_poly(71*den+num)
    qm=integer_poly(71*den-num)

    assert sp.count_roots(qp,-sp.oo,sp.oo)==0
    assert sp.count_roots(qm,-sp.oo,sp.oo)==0
    assert qp.eval(0)>0
    assert qm.eval(0)>0

    w0=F(1415,13891)
    h79=F(80)*w0/(F(79)+w0)
    assert h79==F(28300,274701)

    C79=F(213)*F(106,333)**2
    assert C79==F(797756,36963)

    R=12000
    charge=C79/R
    assert charge==F(199439,110889000)

    ceiling=F(21,200)
    residual=ceiling-h79-charge
    assert residual==F(915620351,5076886531500)
    assert residual>0

    y=ceiling-charge
    square_ceiling=F(79)*y/(F(80)-y)
    assert square_ceiling==F(452034287,4429838047)

    allowance=square_ceiling-w0
    assert allowance==F(10987444212,61534880310877)
    assert allowance>0

    print("GLOBAL_CURVATURE_BOUND: |F79''| < 71")
    print("C79 <=",C79,"~",float(C79))
    print("R =",R)
    print("band charge <=",charge,"~",float(charge))
    print("Jensen model cap =",h79,"~",float(h79))
    print("residual below 0.105 =",residual,"~",float(residual))
    print("required square <",square_ceiling,"~",float(square_ceiling))
    print("allowance above w0 =",allowance,"~",float(allowance))
    print("RESULT: WP84_FUNCTIONAL_BAND_DELTA79_PASS")

if __name__=="__main__":
    main()
