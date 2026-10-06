#!/usr/bin/env python3
"""WP71 generic-prime local four-point factor for the j-first model.

Assume p does not divide b1*b2.  Put
  g=gcd(b1,b2), r=b1/g, q=b2/g, L=lcm(b1,b2)=b2*r=b1*q.

For fixed residues k,j mod p, the four prime positions are affine functions
of one free m residue.  After scaling by units, the forbidden m-residues are

  {0, r*k, -j/b2, r*k-j/b2}.

Hence the local admissible count is N_p=p-D, where D is the number of
distinct residues in that parallelogram.

For odd p:
  k=0,j=0:                 D=1
  exactly one of k,j=0:    D=2
  k,j nonzero and j=±L*k:  D=3
  otherwise:               D=4.

Averaging over all p^2 pairs (k,j) gives the exact normalized local factor

  1 + 1/(p-1)^3.

At p=2 the normalized average is exactly 2.

Therefore the generic-prime Euler product of the j-first four-point mean is

  2 * prod_{p>2} (1 + 1/(p-1)^3),

which exactly matches the public E2(1,1) anchor.

This proves that the cross-relations j=±lcm(b1,b2)k are not noise: they are
the local coincidences responsible for the E2 factor.

Pure exact arithmetic.
"""
from fractions import Fraction as F
from math import gcd

def inv(a,p):
    return pow(a%p,-1,p)

def count_direct(p,b1,b2,k,j):
    assert b1%p and b2%p
    g=gcd(b1,b2); r=b1//g; q=b2//g
    cnt=0
    for m in range(p):
        mp=(m-r*k)%p
        if m==0 or mp==0:
            continue
        # unique n because b1 is a unit mod p
        n=((b2*m+j)*inv(b1,p))%p
        np=(n-q*k)%p
        if n and np:
            cnt+=1
    return cnt

def count_formula(p,b1,b2,k,j):
    g=gcd(b1,b2); r=b1//g
    y=(j*inv(b2,p))%p
    pts={0,(r*k)%p,(-y)%p,(r*k-y)%p}
    return p-len(pts)

def local_average_factor(p,b1=1,b2=1):
    tot=0
    for k in range(p):
        for j in range(p):
            a=count_direct(p,b1,b2,k,j)
            b=count_formula(p,b1,b2,k,j)
            assert a==b,(p,b1,b2,k,j,a,b)
            tot+=a
    baseline=F(p)*(F(p-1,p)**4)
    return F(tot,p*p)/baseline

def main():
    for p in (2,3,5,7,11,13,17,19,23,29,31):
        got=local_average_factor(p)
        want=F(2) if p==2 else F(1)+F(1,(p-1)**3)
        assert got==want,(p,got,want)
        print("p",p,"average local factor",got,"PASS")

    # Check nontrivial unit outer coefficients too.
    for p,b1,b2 in [(5,2,3),(7,3,5),(11,4,9),(13,5,8)]:
        got=local_average_factor(p,b1,b2)
        want=F(1)+F(1,(p-1)**3)
        assert got==want,(p,b1,b2,got,want)
        L=b1*b2//gcd(b1,b2)
        # Verify the only nontrivial D=3 collisions for odd p are j=+-Lk.
        for k in range(1,p):
            specials=set()
            for j in range(1,p):
                n=count_formula(p,b1,b2,k,j)
                if n==p-3:
                    specials.add(j)
            assert specials=={(L*k)%p,(-L*k)%p}
        print("p",p,"outer",(b1,b2),"cross-relation PASS")

    print("RESULT: WP71_JFIRST_GENERIC_LOCAL_FACTOR_PASS")

if __name__=="__main__":
    main()
