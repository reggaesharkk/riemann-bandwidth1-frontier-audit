#!/usr/bin/env python3
"""Exact certificate for the full-sharp mean/variance sine-square retuning."""
import sympy as sp

def model_expect(expr,x):
    P=sp.Poly(
        1
        -sp.Rational(43428,13891)*x
        +sp.Rational(37704,13891)*x**2
        -sp.Rational(9660,13891)*x**3,
        x,
        domain=sp.QQ
    )
    w0=sp.Rational(1415,13891)

    pn,pd=sp.fraction(sp.cancel(expr))
    inv=sp.invert(
        sp.Poly(pd,x,domain=sp.QQ),
        P
    )
    rem=sp.rem(
        sp.Poly(pn,x,domain=sp.QQ)*inv,
        P
    ).as_expr()
    R=sp.Poly(rem,x,domain=sp.QQ)

    return sp.factor(
        R.nth(0)
        +R.nth(1)
        +sp.Rational(4,3)*R.nth(2)
        +w0*(sp.simplify(expr.subs(x,0))-R.nth(0))
    )

def main():
    x=sp.symbols("x", real=True)

    a=sp.Rational(23,20)
    t=sp.Rational(113,100)

    s=2*a*x/(x**2+a**2)

    L=(
        -sp.Rational(3,625)
        +sp.Rational(16189,10000)*x
        -sp.Rational(819,1250)*x**2
    )

    num,den=sp.fraction(
        sp.factor(
            sp.together(s-L)
        )
    )

    expected_num=(
        2620800*x**4
        -6475600*x**3
        +3485208*x**2
        +636019*x
        +25392
    )

    assert sp.Poly(num,x)==sp.Poly(expected_num,x)
    assert sp.expand(
        den-(4000000*x**2+5290000)
    )==0

    Pnum=sp.Poly(num,x)
    assert Pnum.count_roots(-sp.oo,sp.oo)==0
    assert Pnum.eval(0)>0
    assert Pnum.LC()>0

    mean_lower=sp.factor(
        -sp.Rational(3,625)
        +sp.Rational(16189,10000)
        -sp.Rational(819,1250)*sp.Rational(4,3)
    )
    assert mean_lower==sp.Rational(1481,2000)

    mean_term=sp.factor(
        (1-t*mean_lower)**2
    )
    assert mean_term==sp.Rational(
        1065826609,
        40000000000
    )

    mu=model_expect(s,x)
    s2=model_expect(s**2,x)
    var=sp.factor(s2-mu**2)
    E=model_expect((1-t*s)**2,x)

    assert mu==sp.Rational(
        325240778083160,
        405859957296217
    )
    assert s2==sp.Rational(
        119473137226275432821220460800,
        164722304936487086853082511089
    )
    assert var==sp.Rational(
        13691573498136102617344875200,
        164722304936487086853082511089
    )
    assert E==sp.Rational(
        473814077352141196977236513933,
        4118057623412177171327062777225
    )

    Erec=sp.Float("0.163249981456072",40)
    var_ceiling=sp.N(
        (Erec-mean_term)/(t*t),
        20
    )

    print("Sturm real-root count =",Pnum.count_roots(-sp.oo,sp.oo))
    print("mean lower =",mean_lower,float(mean_lower))
    print("mean term =",mean_term,float(mean_term))
    print("model mean =",mu,float(mu))
    print("model second =",s2,float(s2))
    print("model variance =",var,float(var))
    print("model energy =",E,float(E))
    print("model simple ledger ~",float(1-2*E))
    print("variance ceiling ~",var_ceiling)
    print("RESULT: WP84_SINE_FULL_SHARP_RETUNE_PASS")

if __name__=="__main__":
    main()
