#!/usr/bin/env python3
"""Exact checker for the direct degree-two Cayley square."""

import sympy as sp

def main():
    x=sp.symbols("x", real=True)
    I=sp.I
    u=(x+I)/(x-I)

    q=(
        623*u**2
        +(55-1058*I)*u
        -(557+58*I)
    )/1000

    p=sp.factor(sp.simplify(q*sp.conjugate(q)))

    num,den=sp.fraction(sp.together(p-1))
    expected=(
        260097*x**4
        -5295592*x**3
        +5812394*x**2
        -4717448*x
        +121
    )

    assert sp.Poly(num,x)==sp.Poly(expected,x)
    assert sp.expand(den-1000000*(x**2+1)**2)==0

    Pneg=sp.Poly(num,x)
    assert Pneg.count_roots(-sp.oo,0)==0
    assert Pneg.eval(0)>0
    assert Pneg.LC()>0

    model_poly=sp.Poly(
        1
        -sp.Rational(43428,13891)*x
        +sp.Rational(37704,13891)*x**2
        -sp.Rational(9660,13891)*x**3,
        x,
        domain=sp.QQ
    )

    pn,pd=sp.fraction(sp.cancel(p))
    inv=sp.invert(sp.Poly(pd,x,domain=sp.QQ),model_poly)
    rem=sp.rem(
        sp.Poly(pn,x,domain=sp.QQ)*inv,
        model_poly
    ).as_expr()
    R=sp.Poly(rem,x)

    w0=sp.Rational(1415,13891)
    p0=sp.simplify(p.subs(x,0))

    E=sp.factor(
        R.nth(0)
        +R.nth(1)
        +sp.Rational(4,3)*R.nth(2)
        +w0*(p0-R.nth(0))
    )

    expected_E=sp.Rational(
        314919677809788131206697,
        2914998924731524849000000
    )
    assert E==expected_E

    print("negative-half-line Sturm root count =",
          Pneg.count_roots(-sp.oo,0))
    print("p(0) =",p0)
    print("E_model =",E,"~",float(E))
    print("model positive-index value =",1-E,"~",float(1-E))
    print("model simple-zero ledger =",1-2*E,"~",float(1-2*E))
    print("RESULT: WP84_DIRECT_DEGREE2_CAYLEY_SQUARE_PASS")

if __name__=="__main__":
    main()
