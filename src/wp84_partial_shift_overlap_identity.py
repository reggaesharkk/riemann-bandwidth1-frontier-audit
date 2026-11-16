#!/usr/bin/env python3
"""WP84 exact partial-shift word trace = overlap-walk identity.

On {0,...,N-1}, S_r is the non-cyclic translation by integer r:
  (S_r f)[i] = f[i+r] if 0<=i+r<N, else 0.

For a word S_{r1}...S_{rb}, let partial sums
  p0=0, pj=r1+...+rj.
Then:
  - if pb != 0, trace(word)=0;
  - if pb = 0,
      trace(word)=max(0, N-(max p_j-min p_j)).
This is the exact lattice version of
  O_b = (1 - spread(partial walk))_+
used by the connected/cumulant model.
"""
from fractions import Fraction as F
from itertools import product

def mm(A,B):
    n=len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n))
             for j in range(n)] for i in range(n)]

def tr(A):
    return sum(A[i][i] for i in range(len(A)))

def shift(n,r):
    return [[F(1) if j==i+r and 0<=j<n else F(0)
             for j in range(n)] for i in range(n)]

def word(n,steps):
    A=[[F(1) if i==j else F(0) for j in range(n)] for i in range(n)]
    for r in steps:
        A=mm(A,shift(n,r))
    return A

def predicted(n,steps):
    p=[0]
    s=0
    for r in steps:
        s+=r
        p.append(s)
    if s!=0:
        return 0
    return max(0,n-(max(p)-min(p)))

def main():
    checks=0
    for n in (5,7,11):
        for b in (2,3,4,5):
            for steps in product(range(-2,3),repeat=b):
                got=tr(word(n,steps))
                want=predicted(n,steps)
                assert got==want,(n,b,steps,got,want)
                checks+=1
    print("exact word checks =",checks)
    print("RESULT: WP84_PARTIAL_SHIFT_OVERLAP_IDENTITY_PASS")

if __name__=="__main__":
    main()
