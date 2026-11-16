#!/usr/bin/env python3
"""Exact chamber proof that the untruncated Phi4 connected kernel vanishes.

For the public b=4 connected-cumulant construction, each ordered-partition
term contains the range ("spread") of a nested chain of subset sums of
v0,v1,v2,v3 with v3=-(v0+v1+v2).

Before the positive-part truncation, the signed 26-term connected sum is

    sum_t sign_t * (1 - spread_t(v)).

This script proves that expression is identically zero on R^3.

The max/min choices can change only on seven central hyperplanes:
    v2, v1, v1+v2, v0, v0+v2, v0+v1, v0+v1+v2 = 0.

We enumerate all 2^7 sign patterns, certify feasibility of each open chamber
with exact Fraction arithmetic, and on each feasible chamber verify that the
signed affine coefficient of every spread cancels exactly.
"""
from fractions import Fraction as F
from itertools import combinations, permutations, product
from math import gcd
from collections import Counter

ZERO=(0,0,0)
W=((1,0,0),(0,1,0),(0,0,1),(-1,-1,-1))
HYP=(
    (0,0,1),
    (0,1,0),
    (0,1,1),
    (1,0,0),
    (1,0,1),
    (1,1,0),
    (1,1,1),
)

def set_partitions(items):
    if not items:
        yield []
        return
    first,rest=items[0],items[1:]
    for part in set_partitions(rest):
        for i in range(len(part)):
            yield part[:i]+[[first]+part[i]]+part[i+1:]
        yield [[first]]+part

def compile_terms(b=4):
    out=[]
    for P in set_partitions(list(range(b))):
        m=len(P)
        sign=(-1)**(m-1)
        first=next(i for i,blk in enumerate(P) if 0 in blk)
        others=[i for i in range(m) if i!=first]
        for perm in permutations(others):
            order=[first]+list(perm)
            masks=[]
            cur=frozenset()
            for bi in order[:-1]:
                cur=cur|frozenset(P[bi])
                masks.append(tuple(sorted(cur)))
            out.append((sign,tuple(masks)))
    return out

def addv(a,b):
    return tuple(x+y for x,y in zip(a,b))

def positions(masks):
    out=[ZERO]
    for mk in masks:
        z=ZERO
        for j in mk:
            z=addv(z,W[j])
        out.append(z)
    return tuple(out)

def det3(M):
    a,b,c=M
    return (a[0]*(b[1]*c[2]-b[2]*c[1])
            -a[1]*(b[0]*c[2]-b[2]*c[0])
            +a[2]*(b[0]*c[1]-b[1]*c[0]))

def solve3(A):
    D=det3(A)
    if D==0:
        return None
    out=[]
    for j in range(3):
        M=[list(r) for r in A]
        for i in range(3):
            M[i][j]=1
        out.append(F(det3(M),D))
    return tuple(out)

def dot(a,x):
    return sum(F(ai)*xi for ai,xi in zip(a,x))

def feasible_point(signs):
    A=[tuple(s*a for a in n) for s,n in zip(signs,HYP)]
    for inds in combinations(range(len(A)),3):
        x=solve3([A[i] for i in inds])
        if x is None:
            continue
        if all(dot(row,x)>=1 for row in A):
            return x
    return None

def spread_gradient(pos,x):
    vals=[dot(p,x) for p in pos]
    imax=max(range(len(vals)),key=lambda i:vals[i])
    imin=min(range(len(vals)),key=lambda i:vals[i])
    assert vals[imax]>vals[imin] or len(set(vals))==1
    return tuple(pos[imax][j]-pos[imin][j] for j in range(3))

def main():
    raw=compile_terms(4)
    assert len(raw)==26
    terms=[(s,positions(m)) for s,m in raw]
    assert Counter(s for s,_ in terms)==Counter({1:13,-1:13})
    assert sum(s for s,_ in terms)==0

    feasible=[]
    for signs in product((-1,1),repeat=len(HYP)):
        x=feasible_point(signs)
        if x is not None:
            feasible.append((signs,x))

    # Seven planes in R^3 produce exactly 32 feasible open chambers here.
    assert len(feasible)==32,len(feasible)

    for signs,x in feasible:
        g=[0,0,0]
        for sign,pos in terms:
            sg=spread_gradient(pos,x)
            for j in range(3):
                g[j]+=sign*sg[j]
        assert g==[0,0,0],(signs,x,g)

    print("ordered-partition terms =",len(terms))
    print("central hyperplanes      =",len(HYP))
    print("feasible open chambers   =",len(feasible))
    print("constant coefficient sum = 0")
    print("spread gradient sum      = (0,0,0) on every chamber")
    print("RESULT: WP84_PHI4_UNTRUNCATED_CANCELLATION_PASS")

if __name__=="__main__":
    main()
