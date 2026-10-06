#!/usr/bin/env python3
"""WP71 exact local audit for the j-first four-point main.

For each prime p and local outer-coefficient pattern (e1,e2) in {0,1}^2,
choose representatives
    b1 = 1 if e1=0 else p,
    b2 = 1 if e2=0 else p,
and reduce
    g=gcd(b1,b2), r=b1/g, q=b2/g.

For residues k,j mod p count m mod p for which the four affine prime
positions
    m, m-rk, n, n-qk
are all nonzero mod p and
    b1*n - b2*m = j mod p
has a solution n mod p.

Normalize by p*(1-1/p)^4, the local four-prime baseline on one free
residue parameter.

The audit asks:
  1. Does the local factor depend only on zero/nonzero classes of k,j
     together with the fixed outer valuation pattern?
  2. What exact class values occur?
  3. Does the uniform (k,j)-average equal 1 where that normalization is
     appropriate?
  4. Are there additional cross-conditions such as j = c*k mod p which
     split a nominal valuation class?

This is a hostile structural audit.  It does not assume the paper's
singular-series formula.
"""
from fractions import Fraction as F
from collections import defaultdict

def count_local(p,e1,e2,k,j):
    b1=p if e1 else 1
    b2=p if e2 else 1
    # Integer gcd representatives are enough to obtain r,q.
    import math
    g=math.gcd(b1,b2)
    r=b1//g
    q=b2//g

    cnt=0
    for m in range(p):
        mp=(m-r*k)%p
        if m==0 or mp==0:
            continue
        # Count all n satisfying the lock.  In degenerate local outer
        # patterns there can be 0,1, or p solutions.
        for n in range(p):
            if (b1*n-b2*m-j)%p:
                continue
            np=(n-q*k)%p
            if n==0 or np==0:
                continue
            cnt+=1
    return cnt

def cls(k,j):
    return (int(k==0),int(j==0))

def main():
    primes=[3,5,7,11,13]
    any_hidden=False
    for p in primes:
        print("p =",p)
        for e1,e2 in [(0,0),(1,0),(0,1),(1,1)]:
            groups=defaultdict(set)
            rows=defaultdict(list)
            tot=0
            for k in range(p):
                for j in range(p):
                    n=count_local(p,e1,e2,k,j)
                    groups[cls(k,j)].add(n)
                    rows[cls(k,j)].append((k,j,n))
                    tot+=n

            hidden={c:sorted(v) for c,v in groups.items() if len(v)>1}
            if hidden:
                any_hidden=True
            base=F(p)*(F(p-1,p)**4)
            vals={c:[F(n,1)/base for n in sorted(v)]
                  for c,v in groups.items()}
            avg=F(tot,p*p)/base
            print(" outer",e1,e2,
                  "class factors",vals,
                  "uniform avg",avg,
                  "hidden splits",hidden if hidden else "none")

            # If a nominal class splits, print the exact exceptional residue
            # equations observed, for later symbolic reconstruction.
            for c,v in hidden.items():
                byn=defaultdict(list)
                for k,j,n in rows[c]:
                    byn[n].append((k,j))
                print("   split class",c)
                for n,pts in sorted(byn.items()):
                    print("    count",n,"pairs",pts[:30],
                          "..." if len(pts)>30 else "")
        print()

    print("HIDDEN_CROSS_CONSTRAINTS =",any_hidden)
    print("RESULT: WP71_JFIRST_LOCAL_AUDIT_COMPLETE")

if __name__=="__main__":
    main()
