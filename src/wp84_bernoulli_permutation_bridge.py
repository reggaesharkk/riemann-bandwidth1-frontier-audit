#!/usr/bin/env python3
"""Exact Fraction check of permutation-to-Bernoulli beta weights."""

from fractions import Fraction as F
from itertools import permutations

def popcount(x):
    return x.bit_count()

def value(mask,j):
    # Arbitrary exact test function of state and current index.
    return F(
        3 + 5*j + 7*mask + 11*popcount(mask) + 13*((mask>>(j%5))&1),
        17 + j
    )

def main():
    for M in range(2,8):
        # permutation average of the telescoping-style sum
        total=F(0)
        perms=list(permutations(range(M)))
        for pi in perms:
            mask=0
            s=F(0)
            for j in pi:
                s += value(mask,j)
                mask |= 1<<j
            total += s
        perm_avg=total/F(len(perms))

        # Bernoulli integral expanded exactly with Beta(s+1,M-s)
        bern=F(0)
        full=(1<<M)-1
        for j in range(M):
            for mask in range(1<<M):
                if (mask>>j)&1:
                    continue
                s=popcount(mask)
                beta=F(1,1)
                # s! (M-1-s)! / M!
                num=1
                for k in range(2,s+1):
                    num*=k
                for k in range(2,M-s):
                    num*=k
                den=1
                for k in range(2,M+1):
                    den*=k
                beta=F(num,den)
                bern += beta*value(mask,j)

        assert bern==perm_avg,(M,bern,perm_avg)
        print("M",M,"exact average",perm_avg)

    print("RESULT: WP84_BERNOULLI_PERMUTATION_BRIDGE_PASS")

if __name__=="__main__":
    main()
