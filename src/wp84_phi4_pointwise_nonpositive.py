#!/usr/bin/env python3
"""Exact arrangement certificate for C4(v)<=0 on closed four-step cycles."""

from fractions import Fraction as F
from itertools import permutations, combinations
from math import gcd

ZERO,ONE=F(0),F(1)

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

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
            masks=[]
            cur=frozenset()
            for bi in order[:-1]:
                cur=cur|frozenset(P[bi])
                masks.append(tuple(sorted(cur)))
            out.append((sign,tuple(masks)))
    assert len(out)==26
    return out

TERMS=compile_terms()
Z=(ZERO,ZERO,ZERO,ZERO)
V=[
    (ZERO,ONE,ZERO,ZERO),
    (ZERO,ZERO,ONE,ZERO),
    (ZERO,ZERO,ZERO,ONE),
    (ZERO,-ONE,-ONE,-ONE),
]
WALK=[
    Z,
    V[0],
    add(V[0],V[1]),
    add(add(V[0],V[1]),V[2]),
]

def posB(masks):
    out=[Z]
    for mk in masks:
        c=Z
        for j in mk:
            c=add(c,V[j])
        out.append(c)
    return out

def ev(a,x):
    return a[0]+sum(a[i+1]*x[i] for i in range(3))

def spread(pos,x):
    vals=[ev(p,x) for p in pos]
    return max(vals)-min(vals)

def ov(pos,x):
    return max(ZERO,ONE-spread(pos,x))

def B4(x):
    s=ZERO
    for sign,masks in TERMS:
        s += sign*ov(posB(masks),x)
    return s

def normalize_hyperplane(a):
    dens=[q.denominator for q in a]
    l=1
    for d in dens:
        l=l*d//gcd(l,d)
    z=[q.numerator*(l//q.denominator) for q in a]
    g=0
    for t in z:
        g=gcd(g,abs(t))
    if g:
        z=[t//g for t in z]
    for t in z:
        if t:
            if t<0:
                z=[-u for u in z]
            break
    return tuple(z)

def hyperplanes():
    fs=set()
    positions=[WALK]+[posB(m) for _,m in TERMS]
    for pos in positions:
        for i in range(len(pos)):
            for j in range(len(pos)):
                if i==j:
                    continue
                d=sub(pos[i],pos[j])
                if not any(d):
                    continue
                for c in (-ONE,ZERO,ONE):
                    f=(d[0]-c,)+d[1:]
                    fs.add(normalize_hyperplane(f))
    # Explicit cube walls.
    for k in range(3):
        for c in (-ONE,ONE):
            z=[ZERO]*4
            z[0]=-c
            z[k+1]=ONE
            fs.add(normalize_hyperplane(tuple(z)))
    return sorted(fs)

def det3(A):
    return (
        A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
       -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
       +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
    )

def solve3(fs):
    A=[[F(f[j+1]) for j in range(3)] for f in fs]
    b=[F(-f[0]) for f in fs]
    d=det3(A)
    if d==0:
        return None
    pts=[]
    for col in range(3):
        M=[row[:] for row in A]
        for i in range(3):
            M[i][col]=b[i]
        pts.append(det3(M)/d)
    return tuple(pts)

def main():
    hs=hyperplanes()
    assert len(hs)==21,len(hs)

    vertices=set()
    for triple in combinations(hs,3):
        p=solve3(triple)
        if p is None:
            continue
        if all(-ONE<=t<=ONE for t in p):
            vertices.add(p)

    assert len(vertices)==35,len(vertices)

    support=[]
    for p in vertices:
        if spread(WALK,p)<=ONE:
            support.append((B4(p),p))

    assert len(support)==21,len(support)
    mx=max(v for v,_ in support)
    assert mx==0,mx
    assert all(v<=0 for v,_ in support)

    print("unique hyperplanes =",len(hs))
    print("ambient rational vertices =",len(vertices))
    print("support vertices =",len(support))
    print("max B4 on support vertices =",mx)
    print("RESULT: WP84_PHI4_POINTWISE_NONPOSITIVE_PASS")

if __name__=="__main__":
    main()
