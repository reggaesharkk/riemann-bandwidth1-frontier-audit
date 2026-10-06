#!/usr/bin/env python3
"""Exact finite combinatorial check of the D2 leave-one-out coupling law."""
from itertools import combinations
from fractions import Fraction as F
from collections import Counter

def main():
    for M in range(3,9):
        U=tuple(range(M))
        for k in range(0,M):
            # Enumerate actual pairs (p,S), all equally likely:
            pairs=[]
            for p in U:
                rest=[q for q in U if q!=p]
                for S in combinations(rest,k):
                    pairs.append((p,tuple(sorted(S))))

            # Apply the coupling distribution exactly.  For each actual pair:
            # weight (1-k/M) on S0=S; weight k/M * 1/k on each swap q in S.
            joint=Counter()
            for p,S in pairs:
                w0=F(1,M*len(list(combinations([q for q in U if q!=p],k))))
                if k==0:
                    joint[(p,S)] += F(1,len(pairs))
                    continue
                # Every actual pair has 1/len(pairs).
                base=F(1,len(pairs))
                joint[(p,S)] += base*F(M-k,M)
                for q in S:
                    S0=tuple(sorted((set(S)-{q})|{p}))
                    joint[(p,S0)] += base*F(k,M)*F(1,k)

            # Product law target: p uniform and S0 uniform k-subset, independent.
            target=F(1,M*len(list(combinations(U,k))))
            assert len(joint)==M*len(list(combinations(U,k)))
            for p in U:
                for S0 in combinations(U,k):
                    assert joint[(p,tuple(S0))]==target,(M,k,p,S0,joint[(p,tuple(S0))],target)

            print("M",M,"k",k,"PASS")
    print("RESULT: WP84_D2_LEAVE_ONE_OUT_COUPLING_PASS")

if __name__=="__main__":
    main()
