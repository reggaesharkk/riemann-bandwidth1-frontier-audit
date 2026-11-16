#!/usr/bin/env python3
"""Regression/inequality gate for the exact E2 shift-range safe lobe."""

import math
import random

def Dd(d,s):
    return sum(
        complex(
            math.cos(2*math.pi*k*s),
            math.sin(2*math.pi*k*s)
        )
        for k in range(d)
    )/d

def main():
    # Exact elementary constant chain used in the note.
    # Alternating log(1+x) upper bound at x=1/11.
    upper_12 = 12 * (
        1/11
        -1/(2*11**2)
        +1/(3*11**3)
    )
    assert upper_12 < 157/150
    assert 157/150 < math.pi/3

    rng=random.Random(8467)
    worst=1.0

    for _ in range(300):
        T=rng.uniform(12,300)
        L=rng.uniform(2,80)
        d=max(1,int(T*L/(2*math.pi)))

        M=rng.uniform(1000,100000)
        H=M/T

        m=rng.uniform(M,2*M)
        h=rng.uniform(-H,H)
        n=m+h
        if n<=0:
            continue

        Y=math.log(m/n)

        # E2 shift range maps inside the improved lobe.
        assert abs(Y) < math.pi/(3*T) + 1e-14

        K=complex(
            math.cos(T*Y),
            math.sin(T*Y)
        )*Dd(d,Y/L)

        worst=min(worst,K.real)
        assert K.real >= -2e-12,(T,L,d,M,m,h,Y,K.real)

    print("minimum sampled Re K =",worst)
    print("RESULT: WP84_E2_SHIFT_SAFE_LOBE_PASS")

if __name__=="__main__":
    main()
