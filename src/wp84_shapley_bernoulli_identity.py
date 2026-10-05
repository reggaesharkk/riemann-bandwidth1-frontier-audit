#!/usr/bin/env python3
"""Exact finite check of the Shapley/Bernoulli identity."""
from fractions import Fraction as F
from itertools import combinations

def beta_int(k,n):
    # int_0^1 t^k (1-t)^n dt = k! n!/(k+n+1)!
    import math
    return F(math.factorial(k)*math.factorial(n),math.factorial(k+n+1))

def main():
    # Arbitrary exact set functions on small Boolean cubes.
    for M in range(1,8):
        vals={}
        U=tuple(range(M))
        for k in range(M+1):
            for S in combinations(U,k):
                mask=sum(1<<j for j in S)
                vals[mask]=F((mask+3)*(mask+7)+5*M,11+M)

        lhs=vals[(1<<M)-1]-vals[0]
        rhs=F(0)

        for p in U:
            others=[q for q in U if q!=p]
            for k in range(M):
                for S in combinations(others,k):
                    mask=sum(1<<j for j in S)
                    w=beta_int(k,M-k-1)
                    rhs += w*(vals[mask|(1<<p)]-vals[mask])

        assert rhs==lhs,(M,lhs,rhs)
        print("M",M,"PASS")
    print("RESULT: WP84_SHAPLEY_BERNOULLI_IDENTITY_PASS")

if __name__=="__main__":
    main()
