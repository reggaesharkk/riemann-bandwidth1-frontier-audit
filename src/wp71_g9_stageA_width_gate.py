#!/usr/bin/env python3
"""WP71 Stage-A hard-strip width gate.

The public Stage-A band uses

    |j| T <= C * min(N1,N2),
    j = b1*n - b2*m,
    N2 = b2*m,
    m <= X = floor(T/(2*pi)),
    C = 40.

Hence every admissible m for fixed n satisfies

    |m - b1*n/b2|
      = |j|/b2
      <= C*min(N1,N2)/(T*b2)
      <= C*m/T
      <= C*X/T
      <= C/(2*pi).

Thus all admissible m lie in an interval of total length at most C/pi.
For C=40 and pi>3.14,

    C/pi < 40/3.14 < 13,

so there are at most 13 integer m values before the j=0 deletion.

This is a structural asymptotic fact: the moving welding interval is O(1),
not ambient-scale or merely logarithmically short.

The brute-force portion below corroborates the exact count on a grid.
"""
from __future__ import annotations
import math

C=40.0

def admissible(T,b1,b2,n):
    X=int(T/(2*math.pi))
    out=[]
    # The structural proof says only m near c=b1*n/b2 can occur.
    c=b1*n/b2
    rad=C/(2*math.pi)+2
    lo=max(2,int(math.floor(c-rad))-2)
    hi=min(X,int(math.ceil(c+rad))+2)
    for m in range(lo,hi+1):
        j=b1*n-b2*m
        if j==0:
            continue
        N1=b1*n; N2=b2*m
        mn=min(N1,N2)
        if mn>0 and abs(j)*T <= C*mn:
            out.append(m)
    return out

def main():
    assert 40/3.14 < 13
    worst=(0,None)
    for T in (600,1200,2400,4800,9600,19200):
        X=int(T/(2*math.pi))
        for b1 in range(2,41):
            for b2 in range(2,41):
                # sample n across its natural positive range
                for n in range(2,min(X,300)+1):
                    z=admissible(float(T),b1,b2,n)
                    if len(z)>worst[0]:
                        worst=(len(z),(T,b1,b2,n,z))
                    assert len(z)<=13,worst
    print("analytic hard bound: <= 13 integer m values before any extra support cuts")
    print("sampled worst =",worst)
    print("RESULT: WP71_STAGEA_MOVING_WIDTH_O1_PASS")

if __name__=="__main__":
    main()
