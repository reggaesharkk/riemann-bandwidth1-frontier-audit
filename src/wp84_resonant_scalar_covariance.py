#!/usr/bin/env python3
"""Exact symbolic gate for the resonant alpha/beta covariance fingerprint."""
import sympy as sp

def main():
    s=sp.symbols("s", real=True)
    r=sp.symbols("r", integer=True, nonzero=True)
    k=2*sp.pi*r

    aa0=sp.integrate(s,(s,0,1))/2
    assert sp.simplify(aa0-sp.Rational(1,4))==0

    aa=sp.integrate(s*sp.cos(k*s),(s,0,1))/2
    assert sp.simplify(aa)==0

    ab=sp.integrate(s*(1-s)*sp.sin(k*s),(s,0,1))
    assert sp.simplify(ab)==0

    bb0=2*sp.integrate(s*(1-s)**2,(s,0,1))
    assert sp.simplify(bb0-sp.Rational(1,6))==0

    bb=2*sp.integrate(s*(1-s)**2*sp.cos(k*s),(s,0,1))
    target=-1/(2*sp.pi**2*r**2)
    assert sp.simplify(bb-target)==0

    print("C_aa(0) =",aa0)
    print("C_aa(r!=0) =",sp.simplify(aa))
    print("C_ab(r) =",sp.simplify(ab))
    print("C_bb(0) =",bb0)
    print("C_bb(r!=0) =",sp.simplify(bb))
    print("RESULT: WP84_RESONANT_SCALAR_COVARIANCE_PASS")

if __name__=="__main__":
    main()
