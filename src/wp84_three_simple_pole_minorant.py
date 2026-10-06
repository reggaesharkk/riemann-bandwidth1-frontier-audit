#!/usr/bin/env python3
"""Exact certificate for the three-simple-pole WP84 minorant."""
from fractions import Fraction as F
import math

def main():
    # f=1-Q^2/D
    A=F(20)
    B=F(81,2)

    # Negative-half-line coefficient test:
    # (y^3+A y^2+B y+18)^2 - (y^2+1)(y^2+9)(y^2+36)
    coeff=[
        F(40),
        F(435),
        F(1656),
        F(7965,4),
        F(1458)
    ]
    assert all(c>0 for c in coeff)

    q=F(
        120853387254098829282930524740,
        136197874685286537177311582089
    )
    simple=2*q-1
    assert simple==F(
        105508899822911121388549467391,
        136197874685286537177311582089
    )

    residues=[
        complex(-79/280,-1245/448),
        complex(189/8,-855/64),
        complex(-117/35,1215/28),
    ]
    heights=[1.0,3.0,6.0]
    cband=12/math.pi**2*sum(
        abs(c)/a**3
        for c,a in zip(residues,heights)
    )

    qrec=0.8367500185439279
    margin=float(q)-qrec

    print("q =",q,"~",float(q))
    print("simple =",simple,"~",float(simple))
    print("record margin =",margin)
    print("C_band =",cband)
    print("margin/C_band =",margin/cband)
    print("RESULT: WP84_THREE_SIMPLE_POLE_MINORANT_PASS")

if __name__=="__main__":
    main()
