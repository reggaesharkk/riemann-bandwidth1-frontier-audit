#!/usr/bin/env python3
"""Finite falsifier for the WP71 logarithmic bulk/collar count.

For the exact floor/ceiling moving interval, define M=max_n |I~_k(n)|
before the j=0 puncture and, for integer D>=2, call n a collar point when

    0 < |I~_k(n)| < M/D.

The geometric ramp argument predicts

    #collar <= 2*(ceil((M/D)*b2/b1)+3).

This script stress-checks that conservative integer bound over many unrelated
small cells.  It is a falsifier/corroboration of the written ramp proof, not
an asymptotic proof.
"""
from math import gcd, ceil

def cdiv(a,b):
    return -((-a)//b)

def lens(b1,b2,J,lo,hi,k):
    g=gcd(b1,b2); r=b1//g
    A=max(lo,lo+r*k); B=min(hi,hi+r*k)
    if A>B:
        return []
    nlo=cdiv(b2*A-J,b1)-2
    nhi=(b2*B+J)//b1+2
    out=[]
    for n in range(nlo,nhi+1):
        L=max(A,cdiv(b1*n-J,b2))
        U=min(B,(b1*n+J)//b2)
        ell=max(0,U-L+1)
        if ell:
            out.append((n,ell))
    return out

def main():
    cases=0
    for b1 in range(2,20):
        for b2 in range(2,20):
            for J in range(1,24):
                lo,hi=3,36
                r=b1//gcd(b1,b2)
                for k in range(-7,8):
                    z=lens(b1,b2,J,lo,hi,k)
                    if not z:
                        continue
                    M=max(v for _,v in z)
                    for D in (2,4,8,16,32,64):
                        collar=sum(1 for _,v in z if D*v<M)
                        bound=2*(ceil((M/D)*b2/b1)+3)
                        assert collar<=bound,(b1,b2,J,k,M,D,collar,bound)
                        cases+=1
    print("integer collar cases checked =",cases)
    print("RESULT: WP71_G9_BULK_COLLAR_COUNT_PASS")

if __name__=="__main__":
    main()
