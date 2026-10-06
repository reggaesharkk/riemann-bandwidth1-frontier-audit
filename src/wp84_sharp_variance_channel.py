#!/usr/bin/env python3
"""WP84 exact discrete analogue of the sharp mixed variance channel.

On an N-point interval define the non-cyclic partial shifts
  (S_r^+ f)[i] = f[i+r] for i+r<N,
  S_r^- = (S_r^+)^T.

For diagonal A=diag(a_0,...,a_{N-1}), exactly
  S_r^+ A S_r^- = diag(1_{i+r<N} a_{i+r}),
  S_r^- A S_r^+ = diag(1_{i>=r} a_{i-r}).

Therefore
  sum_{r=1}^{N-1} r (S_r^+ A S_r^- + S_r^- A S_r^+)
is diagonal with i-th entry
  sum_j |i-j| a_j.

This is the finite exact analogue of the continuum kernel
  (K a)(x) = integral_0^1 |x-u| a(u) du.
"""
from fractions import Fraction as F

def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def add(A,B):
    return [[x+y for x,y in zip(ra,rb)] for ra,rb in zip(A,B)]

def smul(c,A):
    return [[c*x for x in row] for row in A]

def diag(vals):
    n=len(vals)
    return [[vals[i] if i==j else F(0) for j in range(n)] for i in range(n)]

def shift_plus(n,r):
    # (S+ f)_i = f_{i+r}
    return [[F(1) if j==i+r else F(0) for j in range(n)] for i in range(n)]

def transpose(A):
    return [list(row) for row in zip(*A)]

def main():
    N=11
    vals=[F((7*j*j+5*j+3)%23-4, 5) for j in range(N)]
    A=diag(vals)
    Z=[[F(0) for _ in range(N)] for _ in range(N)]
    lhs=Z
    for r in range(1,N):
        Sp=shift_plus(N,r)
        Sm=transpose(Sp)
        term=add(mm(mm(Sp,A),Sm),mm(mm(Sm,A),Sp))
        lhs=add(lhs,smul(F(r),term))

    rhs=diag([sum(F(abs(i-j))*vals[j] for j in range(N)) for i in range(N)])
    assert lhs==rhs
    # Off-diagonal entries vanish exactly.
    assert all(lhs[i][j]==0 for i in range(N) for j in range(N) if i!=j)
    print("N =",N)
    print("sample diagonal =",[str(lhs[i][i]) for i in range(5)])
    print("RESULT: WP84_SHARP_VARIANCE_CHANNEL_PASS")

if __name__=="__main__":
    main()
