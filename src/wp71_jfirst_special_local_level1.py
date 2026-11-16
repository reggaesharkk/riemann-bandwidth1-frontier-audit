#!/usr/bin/env python3
"""WP71 special-prime local table for the j-first four-point model.

This treats the level-p patterns where p divides exactly one, or both, of the
outer coefficients b1,b2.  It records the exact residue counts and their
uniform (k,j)-average in the same one-lock normalization
    p*(1-1/p)^4.

The level-p table is not the full p-adic singular series when higher
valuations v_p(b_i),v_p(j) matter; it is the first exact special-prime gate.
"""
from fractions import Fraction as F
from math import gcd

def count_local(p,e1,e2,k,j):
    b1=p if e1 else 1
    b2=p if e2 else 1
    g=gcd(b1,b2)
    r=b1//g
    q=b2//g
    cnt=0
    for m in range(p):
        mp=(m-r*k)%p
        if m==0 or mp==0:
            continue
        for n in range(p):
            if (b1*n-b2*m-j)%p:
                continue
            np=(n-q*k)%p
            if n and np:
                cnt+=1
    return cnt

def avg_factor(p,e1,e2):
    tot=sum(count_local(p,e1,e2,k,j)
            for k in range(p) for j in range(p))
    base=F(p)*(F(p-1,p)**4)
    return F(tot,p*p)/base

def main():
    for p in (3,5,7,11,13,17):
        # Exactly one outer coefficient divisible by p.
        for pat in ((1,0),(0,1)):
            e1,e2=pat
            for k in range(p):
                for j in range(p):
                    n=count_local(p,e1,e2,k,j)
                    if j==0:
                        want=0
                    elif k==0:
                        want=p-1
                    else:
                        want=p-2
                    assert n==want,(p,pat,k,j,n,want)
            got=avg_factor(p,e1,e2)
            want=F(p,p-1)
            assert got==want,(p,pat,got,want)
            print("p",p,"pattern",pat,"avg",got,"PASS")

        # Both divisible at level p: lock forces j=0 mod p.
        for k in range(p):
            for j in range(p):
                n=count_local(p,1,1,k,j)
                if j!=0:
                    want=0
                elif k==0:
                    want=(p-1)**2
                else:
                    want=(p-2)**2
                assert n==want,(p,(1,1),k,j,n,want)
        got=avg_factor(p,1,1)
        want=F(1)+F(1,(p-1)**3)
        assert got==want,(p,got,want)
        print("p",p,"pattern",(1,1),"avg",got,"PASS")

    print("RESULT: WP71_JFIRST_SPECIAL_LOCAL_LEVEL1_PASS")

if __name__=="__main__":
    main()
