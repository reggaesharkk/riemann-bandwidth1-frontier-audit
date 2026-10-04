#!/usr/bin/env python3
"""WP83 algebraic falsifier: one large hyperbolic block need not survive aggregation.

Each off-line zero pair contributes, before pullback, a real symmetric
hyperbolic form of signature (1,1).  Signature information alone gives no
monotone lower bound for an even trace moment after summing such forms.

The exact 2x2 control below has two arbitrarily large signature-(1,1) blocks
whose sum is zero.
"""
from fractions import Fraction as F

def matadd(A,B):
    return [[A[i][j]+B[i][j] for j in range(2)] for i in range(2)]

def matmul(A,B):
    return [[sum(A[i][k]*B[k][j] for k in range(2)) for j in range(2)]
            for i in range(2)]

def trace(A):
    return A[0][0]+A[1][1]

def mpow(A,n):
    I=[[F(1),F(0)],[F(0),F(1)]]
    R=I
    for _ in range(n):
        R=matmul(R,A)
    return R

def main():
    for M in (F(1),F(7),F(10**6)):
        H1=[[F(0),M],[M,F(0)]]
        H2=[[F(0),-M],[-M,F(0)]]
        G=matadd(H1,H2)
        assert trace(mpow(H1,4))==2*M**4
        assert trace(mpow(H2,4))==2*M**4
        assert G==[[F(0),F(0)],[F(0),F(0)]]
        assert trace(mpow(G,4))==0
        print("M =",M,
              "individual tr(H^4) =",2*M**4,
              "aggregate tr((H1+H2)^4) = 0")
    print("RESULT: WP83_HYPERBOLIC_AGGREGATION_CANCELLATION_PASS")

if __name__=="__main__":
    main()
