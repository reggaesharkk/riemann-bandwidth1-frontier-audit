#!/usr/bin/env python3
import sympy as sp

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
    rem=sp.rem(sp.Poly(pn,x,extension=I)*inv,P).as_expr()
    R=sp.Poly(rem,x,extension=I)
    return sp.factor(
        R.nth(0)+R.nth(1)+sp.Rational(4,3)*R.nth(2)
        +w0*(sp.simplify(expr.subs(x,0))-R.nth(0))
    )

def main():
    x=sp.symbols("x", real=True)
    a=sp.Rational(63,50)
    t=sp.Rational(37,35)
    s=2*a*x/(x**2+a**2)
    p=sp.factor((1-t*s)**2)
    E=model_expect(p,x)
    expected=sp.Rational(
        2123356554130375347858538674965521,
        17287082796917862060833277294351001
    )
    assert E==expected
    print("a =",a)
    print("t =",t)
    print("E_model =",E,"~",float(E))
    print("positive-index model lower ~",float(1-E))
    print("simple-zero model ledger ~",float(1-2*E))
    print("RESULT: WP84_SINE_SQUARE_RANK4_PASS")

if __name__=="__main__":
    main()
