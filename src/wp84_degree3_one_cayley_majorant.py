#!/usr/bin/env python3
"""Exact certificate for the degree-3 one-Cayley majorant."""
import sympy as sp

x=sp.symbols("x", real=True)
I=sp.I

def main():
    u=(x+I)/(x-I)

    coeff=[
        sp.Rational(1679,1000),
        sp.Rational(206,1000),
        sp.Rational(-2251,1000),
        sp.Rational(-621,1000),
        sp.Rational(-329,1000),
        sp.Rational(-150,1000),
        sp.Rational(43,1000),
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
    g=(
        (x-1)**2/(x**2+1)
        *
        (x-b)**2/(x**2+b**2)
    )

    diff=sp.factor(sp.together(p3-g))
    num,den=sp.fraction(diff)

    target_num=(
        912*x**8
        +7520*x**7
        -6599*x**6
        -83092*x**5
        +185207*x**4
        -136916*x**3
        +36799*x**2
        -1584*x
        +81
    )
    target_den=500*(x**2+1)**3*(16*x**2+81)

    assert sp.expand(num-target_num)==0
    assert sp.expand(den-target_den)==0

    Pnum=sp.Poly(num,x)
    assert Pnum.count_roots(-sp.oo,sp.oo)==0
    assert Pnum.eval(0)>0
    assert Pnum.LC()>0

    # Pinned Christoffel cubic.
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
        69125495024210721523306745833,
        497688491574957002169146925700
    )
    assert E==expected

    q=1-E
    simple=1-2*E

    print("Sturm real-root count =",Pnum.count_roots(-sp.oo,sp.oo))
    print("E_model[p3] =",E,"~",float(E))
    print("positive-index lower =",q,"~",float(q))
    print("simple-zero model ledger =",simple,"~",float(simple))
    print("RESULT: WP84_DEGREE3_CAYLEY_MAJORANT_PASS")

if __name__=="__main__":
    main()
