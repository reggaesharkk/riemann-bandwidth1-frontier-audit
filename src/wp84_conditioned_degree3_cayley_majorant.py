#!/usr/bin/env python3
"""Exact certificate for the conditioned two-pole degree-3 Cayley majorant."""
import sympy as sp

x=sp.symbols("x", real=True)
I=sp.I

def main():
    u=(x+I)/(x-I)

    coeff=[
        sp.Rational(16895,10000),
        sp.Rational(2101,10000),
        sp.Rational(-22720,10000),
        sp.Rational(-6312,10000),
        sp.Rational(-3306,10000),
        sp.Rational(-1525,10000),
        sp.Rational(439,10000),
    ]

    basis=[sp.Integer(1)]
    for k in range(1,4):
        uk=sp.expand_complex(u**k)
        basis += [
            sp.simplify(sp.re(uk)),
            sp.simplify(sp.im(uk))
        ]

    p3=sp.cancel(sum(c*b for c,b in zip(coeff,basis)))

    b=sp.Rational(9,4)
    A=sp.Rational(82,25)
    g=(
        (x**2-A*x+b)**2
        /
        ((x**2+1)*(x**2+b**2))
    )

    diff=sp.factor(sp.together(p3-g))
    num,den=sp.fraction(diff)

    target_num=(
        18544*x**8
        +153120*x**7
        -141929*x**6
        -1672190*x**5
        +3748517*x**4
        -2772972*x**3
        +737557*x**2
        -34542*x
        +567
    )

    # Sympy may cancel a common factor between numerator and denominator.
    # Compare the normalized numerator exactly.
    Pnum=sp.Poly(num,x)
    assert Pnum==sp.Poly(target_num,x)
    assert Pnum.count_roots(-sp.oo,sp.oo)==0
    assert Pnum.eval(0)>0
    assert Pnum.LC()>0

    P=sp.Poly(
        1
        -sp.Rational(43428,13891)*x
        +sp.Rational(37704,13891)*x**2
        -sp.Rational(9660,13891)*x**3,
        x,
        domain=sp.QQ
    )

    pn,pd=sp.fraction(p3)
    inv=sp.invert(sp.Poly(pd,x,domain=sp.QQ),P)
    rem=sp.rem(sp.Poly(pn,x,domain=sp.QQ)*inv,P).as_expr()
    R=sp.Poly(rem,x)

    w0=sp.Rational(1415,13891)
    p0=sp.simplify(p3.subs(x,0))

    E=sp.simplify(
        R.nth(0)
        +R.nth(1)
        +sp.Rational(4,3)*R.nth(2)
        +w0*(p0-R.nth(0))
    )

    expected=sp.Rational(
        6816992961687106121191829211903,
        49768849157495700216914692570000
    )
    assert E==expected

    print("Sturm real-root count =",Pnum.count_roots(-sp.oo,sp.oo))
    print("E_model[p3] =",E,"~",float(E))
    print("positive-index lower ~",float(1-E))
    print("simple-zero model ledger ~",float(1-2*E))
    print("RESULT: WP84_CONDITIONED_DEGREE3_CAYLEY_MAJORANT_PASS")

if __name__=="__main__":
    main()
