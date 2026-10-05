#!/usr/bin/env python3
"""WP84 exact falsifier: the Radau b3 value is not forced by moments m0..m6.

Construct seven positive rational atoms on [0,4], solve exactly for positive
rational weights matching

    m0=1, m1=1, m2=4/3, m3=2,
    m4=13/4, m5=101/18, m6=12809/1260,

and evaluate the bounded beta consumer b3 exactly.

Result:
    E[b3] ~= 0.89036309 < 0.895.

Therefore the value 0.8964412949 obtained by evaluating b3 on the
zero-atom + three-node Radau quadrature is a surrogate value, not a
moment-implied lower bound.

Pure rational arithmetic with Fraction; no LP solver.
"""
from fractions import Fraction as F
from math import comb, factorial

NODES = [
    F(658,10000),
    F(660,10000),
    F(6794,10000),
    F(13978,10000),
    F(13988,10000),
    F(21030,10000),
    F(21034,10000),
]

TARGET = [
    F(1),
    F(1),
    F(4,3),
    F(2),
    F(13,4),
    F(101,18),
    F(12809,1260),
]

def solve(A,b):
    A=[row[:] + [rhs] for row,rhs in zip(A,b)]
    n=len(A)
    for col in range(n):
        piv=next(r for r in range(col,n) if A[r][col] != 0)
        A[col],A[piv]=A[piv],A[col]
        z=A[col][col]
        A[col]=[v/z for v in A[col]]
        for r in range(n):
            if r==col: continue
            q=A[r][col]
            if q:
                A[r]=[u-q*v for u,v in zip(A[r],A[col])]
    return [A[i][-1] for i in range(n)]

def D(m):
    return F((4**m)*(factorial(m)**2), factorial(2*m+1))

def beta(x,m):
    t=F(2)*x/(F(1)+x*x)
    p=F(0)
    for j in range(m+1):
        p += F((-1)**j * comb(m,j), 2*j+1) * t**(2*j+1)
    return p/D(m)

def main():
    A=[[x**k for x in NODES] for k in range(7)]
    w=solve(A,TARGET)
    assert all(v>0 for v in w)

    for k,mk in enumerate(TARGET):
        got=sum(wi*xi**k for wi,xi in zip(w,NODES))
        assert got==mk,(k,got,mk)

    q3=sum(wi*beta(xi,3) for wi,xi in zip(w,NODES))
    threshold=F(179,200)

    assert q3 < threshold

    print("nodes =",NODES)
    print("weights =",w)
    print("q3 exact =",q3)
    print("q3 decimal =",float(q3))
    print("threshold =",float(threshold))
    print("gap threshold-q3 =",float(threshold-q3))
    print("RESULT: WP84_B3_RADAU_SURROGATE_FALSIFIED_EXACT")

if __name__=="__main__":
    main()
