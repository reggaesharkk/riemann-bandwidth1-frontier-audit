#!/usr/bin/env python3
"""Exact finite-section gate for the long-shift low-rank quarantine."""
from fractions import Fraction as F

def shift(n,r):
    return [[F(1) if j==i+r else F(0) for j in range(n)] for i in range(n)]

def add(A,B):
    return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(A,B)]

def transpose(A):
    return [list(row) for row in zip(*A)]

def rank_q(A):
    A=[row[:] for row in A]
    m=len(A); n=len(A[0]); r=0
    for c in range(n):
        p=next((i for i in range(r,m) if A[i][c]),None)
        if p is None:
            continue
        A[r],A[p]=A[p],A[r]
        q=A[r][c]
        A[r]=[x/q for x in A[r]]
        for i in range(m):
            if i!=r and A[i][c]:
                q=A[i][c]
                A[i]=[x-q*y for x,y in zip(A[i],A[r])]
        r+=1
        if r==m: break
    return r

def main():
    for N in (12,19,31):
        for M in range(1,min(7,N)):
            H=[[F(0) for _ in range(N)] for _ in range(N)]
            for r in range(N-M,N):
                S=shift(N,r)
                C=add(S,transpose(S))
                coef=F(3*r+5,2*r+1)
                H=[[H[i][j]+coef*C[i][j] for j in range(N)]
                   for i in range(N)]
            # Every nonzero entry must touch the first M and last M coordinates.
            middle=set(range(M,N-M))
            for i in middle:
                for j in range(N):
                    assert H[i][j]==0
                    assert H[j][i]==0
            assert rank_q(H)<=min(N,2*M)
    print("RESULT: WP84_ENDPOINT_SHIFT_LOW_RANK_PASS")

if __name__=="__main__":
    main()
