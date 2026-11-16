#!/usr/bin/env python3
"""Exact 4D arrangement certificate for nonclosed balanced C4 amplitude.

For four signed normalized shifts v0,...,v3, do NOT impose sum vj=0.
Every overlap path includes its final endpoint Y=sum vj.

The connected second-overlap bracket is the same 26-term ordered-partition
sum used by the closed C4 certificate.  This script proves that on every
balanced 2-positive/2-negative sign orthant, whenever the common first walk
overlap is nonzero, the bracket is <=0.

All acceptance decisions use integer determinants and Fraction arithmetic.
"""

from fractions import Fraction as F
from itertools import combinations, permutations
from math import gcd

Z=F(0)
O=F(1)

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

# Affine forms are (constant,c0,c1,c2,c3).
ZERO=(Z,Z,Z,Z,Z)
V=[
    (Z,O,Z,Z,Z),
    (Z,Z,O,Z,Z),
    (Z,Z,Z,O,Z),
    (Z,Z,Z,Z,O),
]
TOTAL=(Z,O,O,O,O)

def add(a,b):
    return tuple(x+y for x,y in zip(a,b))

def sub(a,b):
    return tuple(x-y for x,y in zip(a,b))

# Common first walk now includes the nonclosed final endpoint.
WALK=[ZERO]
cur=ZERO
for v in V:
    cur=add(cur,v)
    WALK.append(cur)

def positions(masks):
    out=[ZERO]
    for mk in masks:
        q=ZERO
        for j in mk:
            q=add(q,V[j])
        out.append(q)
    # In the closed scripts this endpoint equals zero and is redundant.
    # Here it is essential.
    out.append(TOTAL)
    return out

def ev(a,x):
    return a[0]+sum(a[j+1]*x[j] for j in range(4))

def spread(pos,x):
    vals=[ev(p,x) for p in pos]
    return max(vals)-min(vals)

def overlap(pos,x):
    return max(Z,O-spread(pos,x))

def B4(x):
    out=Z
    for sign,masks in TERMS:
        out += sign*overlap(positions(masks),x)
    return out

def normalize_hp(a):
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
    families=[WALK]+[positions(m) for _,m in TERMS]

    # All max/min branch walls and cutoff walls.
    for pos in families:
        for i in range(len(pos)):
            for j in range(len(pos)):
                if i==j:
                    continue
                d=sub(pos[i],pos[j])
                if not any(d):
                    continue
                for c in (-O,Z,O):
                    fs.add(normalize_hp((d[0]-c,)+d[1:]))

    # Cube and sign walls.
    for k in range(4):
        for c in (-O,Z,O):
            q=[Z]*5
            q[0]=-c
            q[k+1]=O
            fs.add(normalize_hp(tuple(q)))

    return sorted(fs)

def det3(A):
    return (
        A[0][0]*(A[1][1]*A[2][2]-A[1][2]*A[2][1])
       -A[0][1]*(A[1][0]*A[2][2]-A[1][2]*A[2][0])
       +A[0][2]*(A[1][0]*A[2][1]-A[1][1]*A[2][0])
    )

def det4(A):
    out=0
    for j in range(4):
        M=[
            [A[r][c] for c in range(4) if c!=j]
            for r in range(1,4)
        ]
        out += ((-1)**j)*A[0][j]*det3(M)
    return out

def solve4(fs):
    A=[[int(f[j+1]) for j in range(4)] for f in fs]
    b=[-int(f[0]) for f in fs]
    D=det4(A)
    if D==0:
        return None
    out=[]
    for col in range(4):
        M=[row[:] for row in A]
        for i in range(4):
            M[i][col]=b[i]
        out.append(F(det4(M),D))
    return tuple(out)

def main():
    hs=hyperplanes()
    assert len(hs)==45,len(hs)

    vertices=set()
    for four in combinations(hs,4):
        x=solve4(four)
        if x is None:
            continue
        if all(-O<=u<=O for u in x):
            vertices.add(x)

    assert len(vertices)==327,len(vertices)

    # Six balanced sign orthants.
    summaries=[]
    for positive in combinations(range(4),2):
        P=set(positive)
        vals=[]
        for x in vertices:
            if any((x[j]<0 if j in P else x[j]>0) for j in range(4)):
                continue
            # Common first-overlap support.
            if spread(WALK,x)>O:
                continue
            vals.append(B4(x))

        assert vals
        mx=max(vals)
        mn=min(vals)
        assert mx<=0,(positive,mx)
        summaries.append((positive,len(vals),mn,mx))

    print("hyperplanes =",len(hs))
    print("ambient rational vertices =",len(vertices))
    for positive,n,mn,mx in summaries:
        print(
            "positive labels",positive,
            "support vertices",n,
            "min",mn,
            "max",mx
        )
    print("RESULT: WP84_PHI4_BALANCED_NONCLOSED_NONPOSITIVE_PASS")

if __name__=="__main__":
    main()
