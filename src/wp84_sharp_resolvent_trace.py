#!/usr/bin/env python3
"""WP84 exact discrete sharp-resolvent trace identities.

For non-cyclic partial shifts S_r^+, S_r^-=(S_r^+)^T and diagonal
R=diag(r_i):

  tr(R S_r^+ R) = tr(R S_r^- R) = 0,

  tr(R S_r^+ R S_r^+ R) =
  tr(R S_r^- R S_r^- R) = 0,

while

  tr(R S_r^+ R S_r^- R)
    = sum_{i=0}^{N-r-1} r_i^2 r_{i+r},

  tr(R S_r^- R S_r^+ R)
    = sum_{i=r}^{N-1} r_i^2 r_{i-r}.

This is the finite exact analogue of the sharp continuum drift/sum-frequency
vanishing and mixed variance functional.
"""
from fractions import Fraction as F

def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def tr(A):
    return sum(A[i][i] for i in range(len(A)))

def diag(vals):
    n=len(vals)
    return [[vals[i] if i==j else F(0) for j in range(n)] for i in range(n)]

def shift_plus(n,r):
    return [[F(1) if j==i+r else F(0) for j in range(n)] for i in range(n)]

def transpose(A):
    return [list(row) for row in zip(*A)]

def prod(*Ms):
    out=Ms[0]
    for M in Ms[1:]:
        out=mm(out,M)
    return out

def main():
    N=13
    vals=[F((13*i*i+7*i+11)%29+1,7) for i in range(N)]
    R=diag(vals)
    checks=0
    for r in range(1,N):
        Sp=shift_plus(N,r)
        Sm=transpose(Sp)

        assert tr(prod(R,Sp,R))==0
        assert tr(prod(R,Sm,R))==0
        assert tr(prod(R,Sp,R,Sp,R))==0
        assert tr(prod(R,Sm,R,Sm,R))==0

        mixp=tr(prod(R,Sp,R,Sm,R))
        mixm=tr(prod(R,Sm,R,Sp,R))
        wantp=sum(vals[i]**2*vals[i+r] for i in range(N-r))
        wantm=sum(vals[i]**2*vals[i-r] for i in range(r,N))
        assert mixp==wantp
        assert mixm==wantm
        checks+=6

    print("dimension",N,"checks",checks)
    print("RESULT: WP84_SHARP_RESOLVENT_TRACE_PASS")

if __name__=="__main__":
    main()
