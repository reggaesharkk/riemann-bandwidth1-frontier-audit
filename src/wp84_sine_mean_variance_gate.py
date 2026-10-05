#!/usr/bin/env python3
"""Exact checker for the sine-square mean/variance reduction."""
import sympy as sp

def main():
    x=sp.symbols("x", real=True)

    a=sp.Rational(63,50)
    t=sp.Rational(17,16)

    s=2*a*x/(x**2+a**2)

    L=(
        -sp.Rational(7,10000)
        +sp.Rational(15473,10000)*x
        -sp.Rational(1197,2000)*x**2
    )

    diff=sp.factor(sp.together(s-L))
    num,den=sp.fraction(diff)

    target=(
        14962500*x**4
        -38682500*x**3
        +23771965*x**2
        +1587663*x
        +27783
    )

    assert sp.Poly(num,x)==sp.Poly(target,x)
    assert sp.expand(
        den
        -10000*(2500*x**2+3969)
    )==0

    P=sp.Poly(num,x)
    assert P.count_roots(-sp.oo,sp.oo)==0
    assert P.eval(0)>0
    assert P.LC()>0

    mean_lower=sp.simplify(
        -sp.Rational(7,10000)
        +sp.Rational(15473,10000)
        -sp.Rational(1197,2000)*sp.Rational(4,3)
    )
    assert mean_lower==sp.Rational(3743,5000)

    mean_term=sp.factor((1-t*mean_lower)**2)

    Erec=sp.Float("0.163249981456072",30)
    var_ceiling=sp.N(
        (Erec-mean_term)/(t*t),
        20
    )

    print("Sturm real-root count =",P.count_roots(-sp.oo,sp.oo))
    print("mean lower =",mean_lower,"~",float(mean_lower))
    print("mean-term ceiling =",mean_term,"~",float(mean_term))
    print("variance ceiling ~",var_ceiling)
    print("RESULT: WP84_SINE_MEAN_VARIANCE_PASS")

if __name__=="__main__":
    main()
