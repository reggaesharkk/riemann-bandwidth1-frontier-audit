#!/usr/bin/env python3
"""Exact finite-population subset weights for the permutation Lindeberg path.

For a uniform k-subset S of {1,...,M} and a noncommutative word w in block
labels, the inclusion indicator of w depends only on r=#distinct labels:

    E prod_{j in distinct(w)} 1_{j in S} = (k)_r/(M)_r.

This script verifies the exact one-step difference
    alpha_r(k+1)-alpha_r(k)=r (k)_{r-1}/(M)_r
and the order-4 multiplicity ledger.
"""
from fractions import Fraction as F
from math import prod
from collections import Counter
from itertools import product as iproduct

def fall(n,r):
    out=1
    for j in range(r):
        out*=n-j
    return out

def alpha(M,k,r):
    return F(fall(k,r),fall(M,r))

def delta_alpha(M,k,r):
    return alpha(M,k+1,r)-alpha(M,k,r)

def pattern(w):
    return tuple(sorted(Counter(w).values(),reverse=True))

def main():
    for M in range(6,15):
        for k in range(0,M):
            for r in range(1,min(5,k+2,M+1)):
                if r>M: continue
                lhs=delta_alpha(M,k,r)
                rhs=F(r*fall(k,r-1),fall(M,r))
                assert lhs==rhs,(M,k,r,lhs,rhs)

    # Order-four patterns and number of distinct labels.
    expected={
        (4,):1,
        (3,1):2,
        (2,2):2,
        (2,1,1):3,
        (1,1,1,1):4,
    }
    for pat,r in expected.items():
        assert len(pat)==r

    # At k/M -> t the exact finite-population coefficient tends to t^r.
    M=100000
    k=37000
    t=F(k,M)
    for r in range(1,5):
        err=abs(float(alpha(M,k,r))-float(t**r))
        assert err < 1e-4

    print("order-4 distinct-label weights:")
    for pat,r in expected.items():
        print(" pattern",pat,"uses r =",r,
              " coefficient alpha_r=(k)_r/(M)_r")
    print("one-step identity: Delta alpha_r = r (k)_(r-1)/(M)_r")
    print("RESULT: WP84_FINITE_POPULATION_WORD_WEIGHTS_PASS")

if __name__=="__main__":
    main()
