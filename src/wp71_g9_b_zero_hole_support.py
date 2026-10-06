#!/usr/bin/env python3
"""WP71 G9-B j=0 hole support audit.

At a j=0 puncture write n=q*t, m=r*t with gcd(q,r)=1.  The welded partner is
n'=q*(t-k), m'=r*(t-k).  The actual four-von-Mangoldt hole weight is

  Lambda(qt) Lambda(q(t-k)) Lambda(rt) Lambda(r(t-k)).

For k!=0:
  * if q>1 and r>1, this product is identically zero;
  * any nonzero hole therefore lies in q=1 or r=1;
  * because outer b1,b2 are prime powers, q=1 or r=1 means b1,b2
    are powers of the same prime.

The same-prime outer-cell mass is bounded by
  sum_p (log p)^2/(p-1)^2 < infinity,
so it is lower order versus the two-dimensional Mertens pair mass.

This script exhaustively checks the support statement on small integers.
"""
from math import gcd

def is_prime_power(n):
    if n<2:
        return False
    # Return (p,a) or None.
    for p in range(2,n+1):
        prime=all(p%d for d in range(2,int(p**0.5)+1))
        if not prime:
            continue
        x=p
        a=1
        while x<n:
            x*=p; a+=1
        if x==n:
            return (p,a)
    return False

def lam_support(n):
    return bool(is_prime_power(n))

def main():
    checked=0
    for q in range(2,16):
        for r in range(2,16):
            if gcd(q,r)!=1:
                continue
            for t in range(1,80):
                for k in range(-20,21):
                    if k==0 or t-k<=0:
                        continue
                    prod = (
                        lam_support(q*t)
                        and lam_support(q*(t-k))
                        and lam_support(r*t)
                        and lam_support(r*(t-k))
                    )
                    assert not prod,(q,r,t,k)
                    checked+=1
    print("q>1,r>1 off-diagonal states checked =",checked)
    print("RESULT: WP71_G9_B_ZERO_HOLE_SUPPORT_PASS")

if __name__=="__main__":
    main()
