#!/usr/bin/env python3
"""Exact coefficient checker for the sine-square heat-curvature map."""
import sympy as sp

def main():
    I=sp.I

    a=sp.Rational(63,50)
    t=sp.Rational(17,16)

    A1=sp.simplify(a*(-2*t-I*t**2))
    A2=sp.simplify(a**2*t**2)

    assert A1==(
        -sp.Rational(1071,400)
        -sp.Rational(18207,12800)*I
    )
    assert A2==sp.Rational(1147041,640000)

    print("A1 =",A1)
    print("A2 =",A2)
    print("|T12 coefficient| ~",
          float(sp.Abs(A1))/sp.pi.evalf()**2)
    print("|T22 coefficient| ~",
          float(A2)/sp.pi.evalf()**2)
    print("|T13 coefficient| ~",
          2*float(A2)/sp.pi.evalf()**2)
    print("RESULT: WP84_SINE_HEAT_COEFFICIENT_MAP_PASS")

if __name__=="__main__":
    main()
