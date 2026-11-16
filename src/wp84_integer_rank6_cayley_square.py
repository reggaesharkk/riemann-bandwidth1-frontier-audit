#!/usr/bin/env python3
"""Exact certificate for the small-integer one-Cayley rank-six square."""
import sympy as sp

def main():
    x=sp.symbols("x", real=True)
    I=sp.I

    u=(x+I)/(x-I)

    q=(
        72*u**3
        -(6+106*I)*u**2
        -(44+8*I)*u
        -(12-3*I)
    )/105

    pq=sp.simplify(q*sp.conjugate(q))

    A=sp.Rational(82,25)
    b=sp.Rational(9,4)

    g=(
        (x**2-A*x+b)**2
        /
        ((x**2+1)*(x**2+b**2))
    )

    diff=sp.factor(sp.together(pq-g))
    num,den=sp.fraction(diff)
    Pnum=sp.Poly(num,x,domain=sp.QQ)

    expected_num=sp.Poly(
        558400*x**8
        +4033600*x**7
        -3655019*x**6
        -46464400*x**5
        +102823262*x**4
        -73448000*x**3
        +17415581*x**2
        -486000*x
        +234900,
        x,
        domain=sp.QQ
    )

    expected_den=(
        275625
        *(x**2+1)**3
        *(16*x**2+81)
    )

    assert Pnum==expected_num
    assert sp.expand(den-expected_den)==0
    assert Pnum.count_roots(-sp.oo,sp.oo)==0
    assert Pnum.eval(0)>0
    assert Pnum.LC()>0

    # Pinned Christoffel model.
    P=sp.Poly(
        1
        -sp.Rational(43428,13891)*x
        +sp.Rational(37704,13891)*x**2
        -sp.Rational(9660,13891)*x**3,
        x,
        domain=sp.QQ
    )

    pn,pd=sp.fraction(sp.cancel(pq))
    inv=sp.invert(sp.Poly(pd,x,domain=sp.QQ),P)
    rem=sp.rem(
        sp.Poly(pn,x,domain=sp.QQ)*inv,
        P
    ).as_expr()
    R=sp.Poly(rem,x)

    w0=sp.Rational(1415,13891)
    p0=sp.simplify(pq.subs(x,0))

    E=sp.factor(
        R.nth(0)
        +R.nth(1)
        +sp.Rational(4,3)*R.nth(2)
        +w0*(p0-R.nth(0))
    )

    expected_E=sp.Rational(
        7587045874174614507624172997869,
        54870156196139009489148448558425
    )

    assert E==expected_E

    qpos=sp.factor(1-E)
    simple=sp.factor(1-2*E)

    print("Sturm real-root count =",Pnum.count_roots(-sp.oo,sp.oo))
    print("E_model[Q*Q] =",E,"~",float(E))
    print("positive-index model lower =",qpos,"~",float(qpos))
    print("simple-zero model ledger =",simple,"~",float(simple))
    print("RESULT: WP84_INTEGER_RANK6_CAYLEY_SQUARE_PASS")

if __name__=="__main__":
    main()
