#!/usr/bin/env python3
"""Exact finite noncommuting V-sum/V-diff branch gate.

Take non-cyclic shifts S_r on N sites and the symmetric Toeplitz state

    A = I + S_1 + S_1^*.

For r=1, direct exact integer multiplication gives

    Tr(A S_1 A S_1 A + A S_1^* A S_1^* A) = 6N-8,
    Tr(A S_1 A S_1^* A + A S_1^* A S_1 A) = 14N-24.

Thus both same-sign and mixed-sign branches survive at O(N) normalized-trace
scale once the state is not diagonal/multiplication.

This is a falsifier for any theorem step that kills V-sum solely from the
one-block shift geometry.
"""
from fractions import Fraction as F

def eye(n):
    return [[1 if i==j else 0 for j in range(n)] for i in range(n)]

def shift(n,r):
    return [[1 if j==i+r else 0 for j in range(n)] for i in range(n)]

def tr(A):
    return sum(A[i][i] for i in range(len(A)))

def T(A):
    return [list(row) for row in zip(*A)]

def add(*As):
    n=len(As[0])
    return [[sum(A[i][j] for A in As) for j in range(n)] for i in range(n)]

def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def prod(*As):
    out=As[0]
    for A in As[1:]:
        out=mm(out,A)
    return out

def branch_values(N,r=1):
    Sp=shift(N,r)
    Sm=T(Sp)
    A=add(eye(N),shift(N,1),T(shift(N,1)))
    vs=tr(prod(A,Sp,A,Sp,A))+tr(prod(A,Sm,A,Sm,A))
    vd=tr(prod(A,Sp,A,Sm,A))+tr(prod(A,Sm,A,Sp,A))
    return vs,vd

def main():
    for N in range(5,31):
        vs,vd=branch_values(N,1)
        assert vs==6*N-8,(N,vs)
        assert vd==14*N-24,(N,vd)

    for N in (10,20,50,100):
        vs,vd=branch_values(N,1)
        print(
            "N",N,
            "Vsum/N",float(F(vs,N)),
            "Vdiff/N",float(F(vd,N)),
            "ratio",float(F(vs,vd))
        )

    print("limits: Vsum/N -> 6, Vdiff/N -> 14, Vsum/Vdiff -> 3/7")
    print("RESULT: WP84_VSUM_NONCOMMUTING_SURVIVAL_PASS")

if __name__=="__main__":
    main()
