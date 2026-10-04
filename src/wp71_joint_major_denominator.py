#!/usr/bin/env python3
"""WP71 exact joint-major denominator algebra.

Let alpha0=a/q be reduced.  Under dilation by b,

    b*a/q

has reduced denominator q/gcd(q,b).

If both dilated denominators are <= P, then with g=gcd(b1,b2),

    q <= P*b1,
    q <= P*b2,
    q <= P^2*g.

The last inequality follows from

    gcd(q,b1)*gcd(q,b2) <= q*gcd(b1,b2),

checked prime-by-prime.

This is the exact arithmetic core of the public joint-near-major
classification.  Arc-width separation is a separate analytic gate.
"""
from math import gcd

def reduced_den(q,b):
    return q//gcd(q,b)

def check(limit_b=80,limit_q=300,limit_P=20):
    n=0
    for b1 in range(1,limit_b+1):
        for b2 in range(1,limit_b+1):
            g=gcd(b1,b2)
            for q in range(1,limit_q+1):
                d1=gcd(q,b1); d2=gcd(q,b2)
                assert d1*d2 <= q*g
                q1=q//d1; q2=q//d2
                for P in range(max(q1,q2),limit_P+1):
                    assert q <= P*b1
                    assert q <= P*b2
                    assert q <= P*P*g
                    n+=1
    return n

def main():
    n=check()
    print("exact denominator cases checked =",n)
    print("RESULT: WP71_JOINT_MAJOR_DENOMINATOR_PASS")

if __name__=="__main__":
    main()
