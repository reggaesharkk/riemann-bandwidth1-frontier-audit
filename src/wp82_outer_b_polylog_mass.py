#!/usr/bin/env python3
"""WP82 diagnostic: polylog cutoff versus the actual prime-power Mertens mass.

For the Stage-A outer prime-power measure the natural mass is

    M(X)=sum_{n<=X} Lambda(n)/n ~ log X.

If P=(log X)^B, then M(P)/M(X) ~ B log log X / log X -> 0.

So a statement that literally discards the outer prime-power variables
b1,b2 above P cannot be a negligible-tail truncation: it removes
asymptotically all of their normalized Mertens mass.

This script is a finite diagnostic only; the asymptotic proof is Mertens/PNT.
"""
import math

def primes_upto(n):
    sieve=bytearray(b"\x01")*(n+1)
    if n>=0: sieve[0]=0
    if n>=1: sieve[1]=0
    for p in range(2,int(n**0.5)+1):
        if sieve[p]:
            sieve[p*p:n+1:p]=b"\x00"*(((n-p*p)//p)+1)
    return [p for p in range(2,n+1) if sieve[p]]

def mangoldt_mass(X):
    s=0.0
    for p in primes_upto(X):
        lp=math.log(p)
        q=p
        while q<=X:
            s+=lp/q
            if q>X//p: break
            q*=p
    return s

def main():
    for X in (10_000,100_000,1_000_000):
        MX=mangoldt_mass(X)
        for B in (2,4,6):
            P=min(X,max(2,int(math.log(X)**B)))
            MP=mangoldt_mass(P)
            print("X",X,"B",B,"P",P,
                  "one_leg_fraction",MP/MX,
                  "two_leg_fraction",(MP/MX)**2)
    print("ASYMPTOTIC: M((log X)^B)/M(X) -> 0 for fixed B")
    print("RESULT: WP82_OUTER_B_POLYLOG_CUTOFF_CANNOT_BE_TAIL")

if __name__=="__main__":
    main()
