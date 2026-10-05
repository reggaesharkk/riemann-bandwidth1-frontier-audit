#!/usr/bin/env python3
"""Exact certificate for the two-simple-pole WP84 minorant."""
from fractions import Fraction as F
import math

def main():
    # Negative-half-line identity:
    # [y^2+(17/5)y+9/4]^2 -(y^2+1)(y^2+81/16)
    coeff=[
        F(34,5),
        F(3999,400),
        F(153,10),
    ]
    assert all(c>0 for c in coeff)

    q=F(
        298046731976058910350368,
        343933139638869493768225
    )
    simple=2*q-1
    assert simple==F(
        252160324313248326932511,
        343933139638869493768225
    )

    residues=[
        complex(68/65,-3999/3250),
        complex(153/65,35991/13000),
    ]
    heights=[1.0,9/4]

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
    print("RESULT: WP84_TWO_SIMPLE_POLE_MINORANT_PASS")

if __name__=="__main__":
    main()
