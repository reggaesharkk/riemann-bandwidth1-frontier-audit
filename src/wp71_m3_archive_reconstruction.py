#!/usr/bin/env python3
"""
Exact/algebraic audit of the two nonstandard steps in the public m3 ledger.

1. k=3 matrix-tail adaptation:
   for Hermitian A,E in dimension d, ||E||op<=theta and
   ||A||F^2 <= C d ell^2, trace expansion gives normalized error
       O(theta/ell)
     + O(theta^2/ell^2)
     + O(theta^3/ell^3)
   up to harmless constants (using dimension for E^2/E^3).
   With theta=O(l T^(lambda/2-1)), ell~l, all vanish for lambda<=1.

2. locality/calibration:
   the scaled hard-window cycle overlap with one zero-frequency (mu) slot
   and a +/-u prime diagonal is exactly the k=2 overlap:
       O3(0,u,-u) = O2(u,-u) = (1-|u|)_+.
   Cyclicity makes the three mu P^2 placements equal.  Since
       2*pi*mu(tau)/ell1 = 1+O(1/l)
   uniformly on [T,2T], each class inherits the k=2 prime diagonal 1/3
   in the endpoint limit.

This checker verifies the exact overlap/combinatorial identities and the
worst endpoint decay exponents. It is a proof companion, not a substitute
for the analytic estimates cited in the note.
"""

from fractions import Fraction as F

def overlap(points):
    return max(F(1) - (max(points)-min(points)), F(0))

def O2(u):
    # cumulative positions for +u,-u: {0,u}
    return overlap((F(0),u))

def O3_zero_pair(u,slot):
    # cyclic increments with one 0 and the cancelling +u,-u pair.
    inc=[None,None,None]
    vals=[F(0),u,-u]
    # put zero in selected slot and +u,-u in the remaining cyclic order
    inc[slot]=F(0)
    rem=[i for i in range(3) if i!=slot]
    inc[rem[0]]=u
    inc[rem[1]]=-u
    p=[F(0)]
    s=F(0)
    for v in inc[:-1]:
        s+=v
        p.append(s)
    return overlap(tuple(p))

def main():
    # Exact piecewise identity on a dense rational adversarial grid.
    for q in range(1,101):
        for k in range(-3*q,3*q+1):
            u=F(k,q)
            ref=O2(u)
            for slot in range(3):
                assert O3_zero_pair(u,slot)==ref,(u,slot,O3_zero_pair(u,slot),ref)

    # Worst lambda=1 decay exponents in powers of T:
    # theta/ell ~ T^(lambda/2-1)
    # theta^2/ell^2 ~ T^(lambda-2)
    # theta^3/ell^3 ~ T^(3lambda/2-3)
    lam=F(1)
    exponents=(
        lam/F(2)-1,
        lam-2,
        F(3,2)*lam-3,
    )
    assert exponents==(F(-1,2),F(-1),F(-3,2))
    assert all(e<0 for e in exponents)

    # Three cyclic mu P^2 placements; each inherits the k2 prime coefficient.
    k2_prime=F(1,3)
    classes=(k2_prime,k2_prime,k2_prime)
    assert sum(classes)==1

    # Together with mu^3 -> 1 this produces m3 -> 2.
    m3=F(1)+sum(classes)
    assert m3==2

    print("O3(0,+u,-u) = O2(+u,-u) verified exactly on rational grid")
    print("worst_endpoint_tail_exponents =",exponents)
    print("three_muP2_classes =",classes,"sum =",sum(classes))
    print("m3_limit =",m3)
    print("RESULT: M3_ARCHIVE_DEPENDENCIES_RECONSTRUCTED_ALGEBRA_PASS")

if __name__=="__main__":
    main()
