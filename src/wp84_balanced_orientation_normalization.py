#!/usr/bin/env python3
"""Exact orientation-normalization gate for the balanced fixed-scale ledger."""

from fractions import Fraction as F
from itertools import combinations, permutations
import wp84_phi4_equal_scale_brownian_kernel as eq

Z=F(0)

def six_fixed_order_words():
    out=[]
    for pos in combinations(range(4),2):
        P=set(pos)
        ip=iter([0,1])
        im=iter([2,3])
        q=[]
        for k in range(4):
            q.append(next(ip) if k in P else next(im))
        out.append(tuple(q))
    assert len(out)==6
    return out

SIX=six_fixed_order_words()
ALL=list(permutations(range(4)))
ALT=[
    o for o in ALL
    if all((o[j]<2)!=(o[j+1]<2) for j in range(3))
]
assert len(ALL)==24
assert len(ALT)==8

def amp_order(base,o):
    return eq.amp([base[j] for j in o])

def main():
    checked=0
    for den in (8,10,12,16):
        for si in range(den,2*den+1):
            s=F(si,den)
            lo=s-1
            xs=[
                F(j,den)
                for j in range(den+1)
                if lo<=F(j,den)<=1
            ]
            for x in xs:
                for y in xs:
                    base=[x,s-x,-y,-(s-y)]

                    s6=sum((amp_order(base,o) for o in SIX),Z)
                    s24=sum((amp_order(base,o) for o in ALL),Z)
                    s8=sum((amp_order(base,o) for o in ALT),Z)

                    target=eq.target(s,x,y)

                    # Four same-sign label permutations per sign pattern.
                    assert s24==4*s6,(s,x,y,s24,s6)

                    # Only the eight alternating labelled words survive.
                    assert s24==s8,(s,x,y,s24,s8)

                    # The old eight-order average is exactly half the
                    # six-sign-pattern fixed-internal-order sum.
                    assert s8/F(8)==s6/F(2),(s,x,y,s8,s6)

                    assert s8/F(8)==target,(s,x,y,s8,target)
                    checked+=1

    print("exact orientation points =",checked)
    print("RESULT: WP84_BALANCED_ORIENTATION_NORMALIZATION_PASS")

if __name__=="__main__":
    main()
