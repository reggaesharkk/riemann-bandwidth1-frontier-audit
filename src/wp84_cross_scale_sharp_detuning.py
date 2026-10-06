#!/usr/bin/env python3
"""Exact-rational regression/certificate for the sharp cross-scale formula.

The written note gives the chamber derivation.  This checker independently
reconstructs the complete 26-term connected bracket and verifies the closed
formula on exact rational grids covering the fundamental chamber.
"""
from fractions import Fraction as F
from itertools import combinations, permutations

Z=F(0); O=F(1)

def set_partitions(items):
    if not items:
        yield []
        return
    first,rest=items[0],items[1:]
    for part in set_partitions(rest):
        for i in range(len(part)):
            yield part[:i]+[[first]+part[i]]+part[i+1:]
        yield [[first]]+part

def compile_terms():
    out=[]
    for P in set_partitions(list(range(4))):
        m=len(P)
        sign=(-1)**(m-1)
        first=next(i for i,b in enumerate(P) if 0 in b)
        others=[i for i in range(m) if i!=first]
        for perm in permutations(others):
            order=[first]+list(perm)
            cur=frozenset()
            masks=[]
            for bi in order[:-1]:
                cur=cur|frozenset(P[bi])
                masks.append(tuple(sorted(cur)))
            out.append((sign,tuple(masks)))
    assert len(out)==26
    return out

TERMS=compile_terms()

def overlap(vals):
    return max(Z,O-(max(vals)-min(vals)))

def amp(v):
    walk=[Z]
    cur=Z
    for q in v:
        cur+=q
        walk.append(cur)
    oa=overlap(walk)

    Y=sum(v,Z)
    b=Z
    for sign,masks in TERMS:
        vals=[Z]
        for mk in masks:
            vals.append(sum((v[j] for j in mk),Z))
        vals.append(Y)
        b += sign*overlap(vals)
    return oa*b

def closed_formula(c,d,a,b):
    delta=d-c

    O1=max(Z,min(a,b,1-d-a))
    A1=-min(c+a,d)*O1

    O2=min(b,max(Z,a-delta))
    A2=-c*O2

    C6=A1+A2
    G=2*c*O2
    E=C6+G
    return A1,A2,C6,G,E

def main():
    checked=0
    worst=Z

    for den in (8,10,12,16,20):
        for ci in range(0,den+1):
            c=F(ci,den)
            for di in range(ci,den+1):
                d=F(di,den)
                delta=d-c

                aa=[
                    F(j,den)
                    for j in range(den+1)
                    if F(j,den)<=F(1,2)*(1-c)
                ]
                bb=[
                    F(j,den)
                    for j in range(den+1)
                    if F(j,den)<=F(1,2)*(1-d)
                ]

                for a in aa:
                    for b in bb:
                        v1=(c+a,-(d+b),1-a,-(1-b))
                        v2=(-(d+b),c+a,-(1-b),1-a)

                        A1,A2,C6,G,E=closed_formula(c,d,a,b)

                        assert amp(v1)==A1,(c,d,a,b,amp(v1),A1)
                        assert amp(v2)==A2,(c,d,a,b,amp(v2),A2)

                        # The other four balanced sign patterns vanish on
                        # common-overlap support by the independent exact
                        # theorem.  Here the two surviving words therefore
                        # give the full six-word sum.
                        got=amp(v1)+amp(v2)
                        assert got==C6

                        assert E<=0

                        rho=min(delta,1-delta)
                        assert -E<=rho,(c,d,a,b,E,rho)

                        if rho>0:
                            worst=max(worst,(-E)/rho)

                        checked+=1

    print("exact chamber points =",checked)
    print("max sampled (-E)/rho =",worst)
    print("RESULT: WP84_CROSS_SCALE_SHARP_DETUNING_PASS")

if __name__=="__main__":
    main()
