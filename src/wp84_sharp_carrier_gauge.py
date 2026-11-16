#!/usr/bin/env python3
"""WP84 exact finite gauge identity for sharp partial shifts."""
from fractions import Fraction as F

def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def diag(v):
    n=len(v)
    return [[v[i] if i==j else 0 for j in range(n)] for i in range(n)]

def shift_plus(n,r):
    return [[F(1) if j==i+r else F(0) for j in range(n)] for i in range(n)]

def transpose(A):
    return [list(row) for row in zip(*A)]

def main():
    # Work over rationals with q^i in place of a unit-modulus phase.
    # The identity is algebraic and remains valid after q=e^{i theta}.
    N=12
    q=F(3,2)
    Q=diag([q**i for i in range(N)])
    Qi=diag([q**(-i) for i in range(N)])

    checks=0
    for r in range(1,N):
        Sp=shift_plus(N,r)
        Sm=transpose(Sp)
        lhs_p=mm(mm(Qi,Sp),Q)
        lhs_m=mm(mm(Qi,Sm),Q)
        rhs_p=[[q**r*x for x in row] for row in Sp]
        rhs_m=[[q**(-r)*x for x in row] for row in Sm]
        assert lhs_p==rhs_p
        assert lhs_m==rhs_m
        checks+=2

    print("checks",checks)
    print("RESULT: WP84_SHARP_CARRIER_GAUGE_PASS")

if __name__=="__main__":
    main()
