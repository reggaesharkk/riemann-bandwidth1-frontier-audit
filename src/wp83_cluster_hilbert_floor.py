#!/usr/bin/env python3
"""WP83 exact confluent-cluster Hilbert floor.

For a cluster jet basis on a unit interval, the normalized moment Gram is the
s x s Hilbert matrix H_ij = 1/(i+j+1), 0<=i,j<s.

For any positive semidefinite s x s matrix,
    lambda_min >= det(H) / lambda_max^(s-1)
and lambda_max <= tr(H), hence
    lambda_min(H) >= det(H) / tr(H)^(s-1).

The script computes these lower bounds exactly for s<=4.
"""
from fractions import Fraction as F

def det(A):
    A=[row[:] for row in A]
    n=len(A); out=F(1); sign=1
    for i in range(n):
        p=next(j for j in range(i,n) if A[j][i])
        if p!=i:
            A[i],A[p]=A[p],A[i]
            sign=-sign
        piv=A[i][i]
        out*=piv
        for j in range(i+1,n):
            q=A[j][i]/piv
            for k in range(i,n):
                A[j][k]-=q*A[i][k]
    return out*sign

def main():
    expected={
        1:F(1,1),
        2:F(1,16),
        3:F(5,25392),
        4:F(49,1395654656),
    }
    for s in range(1,5):
        H=[[F(1,i+j+1) for j in range(s)] for i in range(s)]
        D=det(H)
        tr=sum(H[i][i] for i in range(s))
        floor=D/(tr**(s-1)) if s>1 else D
        assert floor==expected[s],(s,floor,expected[s])
        print(f"s={s} det={D} trace={tr} floor={floor} ~ {float(floor):.12g}")
    print("RESULT: WP83_CLUSTER_HILBERT_FLOOR_PASS")

if __name__=="__main__":
    main()
