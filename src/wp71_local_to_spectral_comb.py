#!/usr/bin/env python3
"""WP71 exact local-to-spectral comb reconciliation.

For P=p^s, fixed b1,b2,k, let
  g=gcd(b1,b2), r=b1/g, q=b2/g.

For each lock j mod P, C4(j;k) counts pairs (m,n) mod P satisfying
  b1*n-b2*m=j,
with all four positions
  m, m-rk, n, n-qk
units mod p.

Define the local four-point lock factor by normalizing C4 with
  P*(1-1/p)^4.

Then the exact j-average factorizes:

  (1/P) sum_j C4(j;k) / [P*(1-1/p)^4]
    =
  [Cm(rk)/(P*(1-1/p)^2)]
  [Cn(qk)/(P*(1-1/p)^2)],

where C(h) counts x mod P with x and x-h both units mod p.

Proof: for every admissible pair (m,n), there is exactly one j mod P,
namely j=b1*n-b2*m.  Averaging over j therefore removes the lock and the
m,n restrictions factor.

This is the exact prime-by-prime bridge from the j-first four-point local
model to the product of the two twin local factors in the spectral comb.

It also gives a fail-closed symmetry rule: after j-averaging, swapping
b1<->b2 (hence r<->q) cannot change the local factor.

Pure integer/Fraction arithmetic.
"""
from fractions import Fraction as F
from math import gcd

def pair_count(P,p,h):
    return sum(1 for x in range(P) if x%p and (x-h)%p)

def four_lock_count(P,p,b1,b2,k,j):
    g=gcd(b1,b2); r=b1//g; q=b2//g
    cnt=0
    for m in range(P):
        if m%p==0 or (m-r*k)%p==0:
            continue
        for n in range(P):
            if n%p==0 or (n-q*k)%p==0:
                continue
            if (b1*n-b2*m-j)%P==0:
                cnt+=1
    return cnt

def avg_factor(P,p,b1,b2,k):
    total=sum(four_lock_count(P,p,b1,b2,k,j) for j in range(P))
    base=F(P)*(F(p-1,p)**4)
    return F(total,P)/base

def pair_factor(P,p,h):
    base=F(P)*(F(p-1,p)**2)
    return F(pair_count(P,p,h),1)/base

def check_case(p,s,b1,b2,k):
    P=p**s
    g=gcd(b1,b2); r=b1//g; q=b2//g
    lhs=avg_factor(P,p,b1,b2,k)
    rhs=pair_factor(P,p,r*k)*pair_factor(P,p,q*k)
    assert lhs==rhs,(p,s,b1,b2,k,lhs,rhs)

    # Asymmetry anomaly gate: the averaged factor is invariant under
    # swapping the two outer legs.
    sw=avg_factor(P,p,b2,b1,k)
    assert lhs==sw,(p,s,b1,b2,k,lhs,sw)
    return lhs

def main():
    cases=0
    families=[
      (2,2,1,1),(2,3,2,1),(2,3,4,6),(2,4,8,2),
      (3,2,1,1),(3,2,3,1),(3,3,9,3),(3,3,6,5),
      (5,2,1,1),(5,2,5,1),(5,2,25,5),(5,2,10,3),
      (7,2,7,1),(7,2,49,7),(7,2,14,5),
    ]
    for p,s,b1,b2 in families:
        P=p**s
        for k in range(min(P,8)):
            val=check_case(p,s,b1,b2,k)
            cases+=1
        print("family",(p,s,b1,b2),"PASS")

    print("cases checked =",cases)
    print("RESULT: WP71_LOCAL_TO_SPECTRAL_COMB_PASS")

if __name__=="__main__":
    main()
