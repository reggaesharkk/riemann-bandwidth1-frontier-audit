#!/usr/bin/env python3
"""Exact checker for the retuned a=4/3 direct degree-two Cayley square."""
import sympy as sp

def main():
    x=sp.symbols("x", real=True)
    I=sp.I
    a=sp.Rational(4,3)

    u=(x+I*a)/(x-I*a)

    q=(
        773*u**2
        +(376-1361*I)*u
        -(664+397*I)
    )/1000

    p=sp.factor(sp.simplify(q*sp.conjugate(q)))

    num,den=sp.fraction(sp.together(p-1))

    expected_num=(
        188388909*x**4
        -1174517712*x**3
        +1517576544*x**2
        -1145293056*x
        +149760
    )

    assert sp.Poly(num,x)==sp.Poly(expected_num,x)
    assert sp.expand(
        den
        -1000000*(9*x**2+16)**2
    )==0

    Pneg=sp.Poly(num,x)
    assert Pneg.count_roots(-sp.oo,0)==0
    assert Pneg.eval(0)>0

    model_poly=sp.Poly(
        1
        -sp.Rational(43428,13891)*x
        +sp.Rational(37704,13891)*x**2
        -sp.Rational(9660,13891)*x**3,
        x,
        extension=I
    )

    pn,pd=sp.fraction(sp.cancel(p))
    inv=sp.invert(
        sp.Poly(pd,x,extension=I),
        model_poly
    )
    rem=sp.rem(
        sp.Poly(pn,x,extension=I)*inv,
        model_poly
    ).as_expr()
    R=sp.Poly(rem,x,extension=I)

    w0=sp.Rational(1415,13891)
    p0=sp.simplify(p.subs(x,0))

    E=sp.factor(
        R.nth(0)
        +R.nth(1)
        +sp.Rational(4,3)*R.nth(2)
        +w0*(p0-R.nth(0))
    )

    expected_E=sp.Rational(
        2425080141045661660562746421,
        21513987578630813262384200000
    )
    assert E==expected_E

    print("negative-half-line Sturm root count =",
          Pneg.count_roots(-sp.oo,0))
    print("E_model =",E,"~",float(E))
    print("positive-index model lower ~",float(1-E))
    print("simple-zero model ledger ~",float(1-2*E))
    print("RESULT: WP84_DIRECT_DEGREE2_A4_3_RETUNED_PASS")

if __name__=="__main__":
    main()
