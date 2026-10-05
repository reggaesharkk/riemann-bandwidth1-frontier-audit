#!/usr/bin/env python3
import sympy as sp

def main():
    r = sp.sqrt(22)
    p = sp.Rational(3,25)
    xm = 1 - r/3
    xp = 1 + r/22

    assert sp.simplify(p*xm + (1-p)*xp) == 1
    assert sp.simplify(p*xm**2 + (1-p)*xp**2) == sp.Rational(4,3)

    a = sp.Rational(23,20)
    sm = sp.simplify(2*a*xm/(xm**2 + a**2))
    spv = sp.simplify(2*a*xp/(xp**2 + a**2))
    mu = sp.simplify(p*sm + (1-p)*spv)
    var = sp.factor(p*(sm-mu)**2 + (1-p)*(spv-mu)**2)

    delta = sp.expand(var - sp.Rational(1,3))
    A = sp.simplify(delta.coeff(r,1))
    B = sp.simplify(-delta.subs(r,0))
    assert A > 0 and B > 0
    assert sp.simplify(22*A*A - B*B) > 0

    Erec = sp.Rational(163249981456072, 10**15)
    t = sp.Rational(113,100)
    mean_lower = sp.Rational(1481,2000)
    ceiling = sp.factor((Erec - (1-t*mean_lower)**2)/(t*t))
    assert ceiling < sp.Rational(1,9)

    print("variance ~", sp.N(var,20))
    print("ceiling ~", sp.N(ceiling,20))
    print("RESULT: WP84_SINE_FIRST_TWO_MOMENT_OBSTRUCTION_PASS")

if __name__ == "__main__":
    main()
