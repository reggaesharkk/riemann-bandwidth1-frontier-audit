#!/usr/bin/env python3
"""Exact Fourier-coefficient gate for the corrected S4 heat kernel."""
import sympy as sp

def main():
    t=sp.symbols("t", real=True)
    pi=sp.pi

    S4=(
        pi**4/sp.Integer(45)
        -pi**2*t**2/sp.Integer(6)
        +pi*t**3/sp.Integer(6)
        -t**4/sp.Integer(24)
    )

    for r in range(1,9):
        coeff=sp.simplify(
            sp.integrate(
                S4*sp.exp(-sp.I*r*t),
                (t,0,2*pi)
            )/(2*pi)
        )
        assert sp.simplify(coeff-sp.Rational(1,r**4))==0,(r,coeff)

    print("verified Fourier coefficients 1/r^4 for r=1,...,8")
    print("RESULT: WP84_HEAT_S4_KERNEL_PASS")

if __name__=="__main__":
    main()
