#!/usr/bin/env python3
import sympy as sp

def main():
    x=sp.symbols("x", real=True)
    I=sp.I
    a=sp.Rational(4,3)
    u=(x+I*a)/(x-I*a)
    q=(623*u**2 +(55-1058*I)*u -(557+58*I))/1000
    p=sp.cancel(q*sp.conjugate(q))

    P=sp.Poly(
        1-sp.Rational(43428,13891)*x
        +sp.Rational(37704,13891)*x**2
        -sp.Rational(9660,13891)*x**3,
        x, domain=sp.QQ
    )
    pn,pd=sp.fraction(p)
    inv=sp.invert(sp.Poly(pd,x,domain=sp.QQ),P)
    rem=sp.rem(sp.Poly(pn,x,domain=sp.QQ)*inv,P)
    R=sp.Poly(rem.as_expr(),x)
    w0=sp.Rational(1415,13891)
    p0=sp.simplify(p.subs(x,0))
    E=sp.factor(
        R.nth(0)+R.nth(1)+sp.Rational(4,3)*R.nth(2)
        +w0*(p0-R.nth(0))
    )
    expected=sp.Rational(
        2643915226535620881849576949,
        21513987578630813262384200000
    )
    assert E==expected
    print("E_model =",E,"~",float(E))
    print("positive-index model lower ~",float(1-E))
    print("simple-zero model ledger ~",float(1-2*E))
    print("RESULT: WP84_DIRECT_DEGREE2_A4_3_PASS")

if __name__=="__main__":
    main()
