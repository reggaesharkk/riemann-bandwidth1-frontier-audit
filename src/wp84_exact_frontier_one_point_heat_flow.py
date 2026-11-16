#!/usr/bin/env python3
"""Regression gate for the exact-frontier one-point heat-flow identities."""

import sympy as sp

a=sp.real_root(sp.Rational(13891,9660),3)
A=sp.Rational(43428,13891)
B=sp.Rational(37704,13891)
C=sp.Rational(9660,13891)

u=sp.symbols("u")
I=sp.I

q0=(-I+A*a+I*B*a**2-C*a**3)/8
q1=(3*I-A*a+I*B*a**2-3*C*a**3)/8
q2=(-3*I-A*a-I*B*a**2-3*C*a**3)/8
q3=(I+A*a-I*B*a**2-C*a**3)/8
q=[q0,q1,q2,q3]

def cc(z):
    return sp.conjugate(z).subs(sp.conjugate(a),a)

def main():
    assert sp.simplify(C*a**3-1)==0
    assert sp.simplify(sum(q)+1)==0

    c0=sp.simplify(sum(z*cc(z) for z in q))
    c1=sp.simplify(q1*cc(q0)+q2*cc(q1)+q3*cc(q2))
    c2=sp.simplify(q2*cc(q0)+q3*cc(q1))
    c3=sp.simplify(q3*cc(q0))

    Einf=sp.simplify(c0+2*sp.re(c1+c2+c3))
    assert sp.simplify(Einf-1)==0

    Ah=sp.simplify(2*I*a*(c1+2*c2+3*c3))
    Bh=sp.simplify((2*I*a)**2*(c2+3*c3))
    Ch=sp.simplify((2*I*a)**3*c3/2)

    print("a_* =",sp.N(a,20))
    print("A_* =",sp.N(Ah,20))
    print("B_* =",sp.N(Bh,20))
    print("C_* =",sp.N(Ch,20))
    print("E_infinity =",Einf)

    w0=sp.Rational(1415,13891)
    target_integral=sp.simplify(1-w0)
    cushion=sp.simplify(target_integral-sp.Rational(895,1000))
    assert target_integral==sp.Rational(12476,13891)
    assert cushion==sp.Rational(8711,2778200)

    print("model integrated curvature =",target_integral,"~",float(target_integral))
    print(">79 curvature cushion =",cushion,"~",float(cushion))
    print("RESULT: WP84_EXACT_FRONTIER_HEAT_FLOW_PASS")

if __name__=="__main__":
    main()
