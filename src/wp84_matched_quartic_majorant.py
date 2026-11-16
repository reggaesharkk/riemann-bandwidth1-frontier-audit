#!/usr/bin/env python3
"""Exact certificate for the quartic majorant of the matched two-pole defect."""
import sympy as sp

def main():
    x=sp.symbols("x", real=True)

    b=sp.Rational(9,4)
    g=(
        (x-1)**2/(x**2+1)
        *
        (x-b)**2/(x**2+b**2)
    )

    P4=(
        sp.Rational(593,2000)*x**4
        -sp.Rational(212,125)*x**3
        +sp.Rational(1761,500)*x**2
        -sp.Rational(3133,1000)*x
        +sp.Rational(1011,1000)
    )

    diff=sp.factor(sp.together(P4-g))
    num,den=sp.fraction(diff)

    target=(
        9488*x**8
        -54272*x**7
        +170225*x**6
        -429280*x**5
        +731653*x**4
        -674554*x**3
        +284698*x**2
        -39546*x
        +1782
    )

    assert sp.Poly(num,x)==sp.Poly(target,x)
    assert sp.expand(den-2000*(x**2+1)*(16*x**2+81))==0

    poly=sp.Poly(num,x)
    assert poly.count_roots(-sp.oo,sp.oo)==0
    assert poly.eval(0)>0
    assert poly.LC()>0

    E=sp.simplify(
        sp.Rational(593,2000)*sp.Rational(13,4)
        -sp.Rational(212,125)*2
        +sp.Rational(1761,500)*sp.Rational(4,3)
        -sp.Rational(3133,1000)
        +sp.Rational(1011,1000)
    )
    assert E==sp.Rational(233,1600)

    print("Sturm real-root count =",poly.count_roots(-sp.oo,sp.oo))
    print("E_model[P4] =",E,"~",float(E))
    print("positive-index model lower =",1-E,"~",float(1-E))
    print("simple-zero model ledger =",1-2*E,"~",float(1-2*E))
    print("RESULT: WP84_MATCHED_QUARTIC_MAJORANT_PASS")

if __name__=="__main__":
    main()
