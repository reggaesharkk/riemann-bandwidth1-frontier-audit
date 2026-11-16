#!/usr/bin/env python3
"""Exact certificate for the updated band-conditioned sine-square point."""
import sympy as sp
import math

def model_expect(expr,x):
    I=sp.I
    P=sp.Poly(
        1-sp.Rational(43428,13891)*x
        +sp.Rational(37704,13891)*x**2
        -sp.Rational(9660,13891)*x**3,
        x,
        extension=I
    )
    w0=sp.Rational(1415,13891)

    pn,pd=sp.fraction(sp.cancel(expr))
    inv=sp.invert(sp.Poly(pd,x,extension=I),P)
    rem=sp.rem(
        sp.Poly(pn,x,extension=I)*inv,
        P
    ).as_expr()
    R=sp.Poly(rem,x,extension=I)

    return sp.factor(
        R.nth(0)
        +R.nth(1)
        +sp.Rational(4,3)*R.nth(2)
        +w0*(sp.simplify(expr.subs(x,0))-R.nth(0))
    )

def main():
    x=sp.symbols("x", real=True)

    a=sp.Rational(63,50)
    t=sp.Rational(17,16)

    s=2*a*x/(x**2+a**2)
    p=sp.factor((1-t*s)**2)

    E=model_expect(p,x)

    expected=sp.Rational(
        16936977322225889866362306131535233,
        138296662375342896486666218354808008
    )
    assert E==expected

    C=(
        12*float(t)*math.sqrt(4+float(t)**2)
        +36*float(t)**2
    )/(math.pi**2*float(a)**2)

    Erec=0.163249981456072
    margin=Erec-float(E)

    print("a =",a)
    print("t =",t)
    print("E_model =",E,"~",float(E))
    print("positive-index model lower ~",float(1-E))
    print("simple-zero model ledger ~",float(1-2*E))
    print("C_sine ~",C)
    print("margin ~",margin)
    print("margin/C ~",margin/C)
    print("RESULT: WP84_SINE_SQUARE_UPDATED_CONDITIONING_PASS")

if __name__=="__main__":
    main()
