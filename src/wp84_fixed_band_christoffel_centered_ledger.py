#!/usr/bin/env python3
"""Exact centered-ledger gate for the fixed-band Christoffel square."""

from fractions import Fraction as F
from math import comb

DEN=13891
P=[F(1),-F(43428,DEN),F(37704,DEN),-F(9660,DEN)]

RAW=[
    F(1),
    F(1),
    F(4,3),
    F(2),
    F(13,4),
    F(101,18),
    F(12809,1260),
]

def poly_shift_one(p):
    # coefficients of p(1+y)
    out=[F(0)]*len(p)
    for k,pk in enumerate(p):
        for j in range(k+1):
            out[j]+=pk*F(comb(k,j))
    return out

def conv(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            out[i+j]+=x*y
    return out

def centered(k):
    return sum(F(comb(k,j))*(-1)**(k-j)*RAW[j] for j in range(k+1))

def main():
    q=poly_shift_one(P)
    assert q==[
        -F(1493,13891),
        F(3000,13891),
        F(8724,13891),
        -F(9660,13891),
    ]

    g=conv(q,q)
    expected=[
        F(2229049,192959881),
        -F(8958000,192959881),
        -F(17049864,192959881),
        F(81188760,192959881),
        F(18148176,192959881),
        -F(168547680,192959881),
        F(93315600,192959881),
    ]
    assert g==expected

    cm=[centered(k) for k in range(7)]
    assert cm==[
        F(1),F(0),F(1,3),F(0),F(1,4),F(1,36),F(157,630)
    ]

    model=sum(g[k]*cm[k] for k in range(7))
    assert model==F(1415,13891)

    pair4_cost=g[4]*(F(4,15)-F(1,4))
    assert pair4_cost>0

    t=-g[5]/(2*g[6])
    rem=g[4]-g[5]*g[5]/(4*g[6])
    assert t==F(727,805)
    assert rem==-F(57960000,192959881)

    print("centered coefficients =",g)
    print("centered model moments =",cm)
    print("model square =",model,"~",float(model))
    print("pair-only m4 cost =",pair4_cost,"~",float(pair4_cost))
    print("square center =",t,"~",float(t))
    print("quartic remainder =",rem,"~",float(rem))
    print("RESULT: WP84_FIXED_BAND_CHRISTOFFEL_CENTERED_LEDGER_PASS")

if __name__=="__main__":
    main()
