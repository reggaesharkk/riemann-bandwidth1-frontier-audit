#!/usr/bin/env python3
"""Exact-rational regression gate for the equal-scale Brownian connected kernel.

The analytic proof is in notes/WP84_PHI4_EQUAL_SCALE_BROWNIAN_KERNEL.md.
This checker recomputes the full 26-term connected overlap expression using
Fraction arithmetic on a dense exact rational grid and checks the closed
formula for all eight alternating sign orderings after symmetrization.
"""

from fractions import Fraction as F
from itertools import permutations

ZERO=F(0)
ONE=F(1)

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

ALTS=[
    o for o in permutations(range(4))
    if all((o[j]<2)!=(o[j+1]<2) for j in range(3))
]
assert len(ALTS)==8

def overlap(vals):
    return max(ZERO,ONE-(max(vals)-min(vals)))

def amp(v):
    # Common first walk, retaining the final endpoint.
    walk=[ZERO]
    cur=ZERO
    for q in v:
        cur+=q
        walk.append(cur)
    oa=overlap(walk)

    b=ZERO
    Y=sum(v,ZERO)
    for sign,masks in TERMS:
        vals=[ZERO]
        for mk in masks:
            vals.append(sum((v[j] for j in mk),ZERO))
        vals.append(Y)
        b += sign*overlap(vals)
    return oa*b

def sym_amp(s,x,y):
    base=[x,s-x,-y,-(s-y)]
    return sum(
        (amp([base[j] for j in o]) for o in ALTS),
        ZERO
    )/8

def depth(s,u):
    return min(u-s+1,1-u)

def target(s,x,y):
    return -(s-1)*min(depth(s,x),depth(s,y))

def main():
    checked=0

    # Exact rational grid covering the full domain.
    for den in (8,10,12,16,20):
        for si in range(den,2*den+1):
            s=F(si,den)
            lo=s-1
            xs=[
                F(j,den)
                for j in range(0,den+1)
                if lo<=F(j,den)<=1
            ]
            for x in xs:
                for y in xs:
                    got=sym_amp(s,x,y)
                    want=target(s,x,y)
                    assert got==want,(s,x,y,got,want)
                    checked+=1

    # Negative-semidefinite Gram identity on exact finite samples:
    # -C=(s-1) integral 1_{r<d_j}1_{r<d_k} dr.
    for s in (F(11,10),F(6,5),F(7,5),F(8,5)):
        xs=[
            s-1 + (2-s)*F(j,8)
            for j in range(9)
        ]
        ds=[depth(s,x) for x in xs]

        # Direct matrix from the closed formula.
        K=[
            [(s-1)*min(ds[i],ds[j]) for j in range(len(xs))]
            for i in range(len(xs))
        ]

        # Check quadratic forms for a deterministic set of integer vectors.
        vectors=[]
        n=len(xs)
        for shift in range(7):
            vectors.append([
                F(((3*j+5*shift)%11)-5,1)
                for j in range(n)
            ])

        for z in vectors:
            q=sum(
                z[i]*K[i][j]*z[j]
                for i in range(n)
                for j in range(n)
            )
            assert q>=0,q

    print("exact grid identities checked =",checked)
    print("RESULT: WP84_PHI4_EQUAL_SCALE_BROWNIAN_KERNEL_PASS")

if __name__=="__main__":
    main()
