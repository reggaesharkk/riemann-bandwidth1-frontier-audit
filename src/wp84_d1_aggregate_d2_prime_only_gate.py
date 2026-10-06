#!/usr/bin/env python3
"""Finite regression gate for D1 aggregation and D2 proper-power removal algebra.

This checks the exact matrix identities; the O(L^-2) analytic estimate is in
the companion note.
"""
import numpy as np

def main():
    rng=np.random.default_rng(8406)
    d=23
    z=0.2+1.7j

    # Arbitrary Hermitian subset state.
    X=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
    H=(X+X.conj().T)/2
    R=np.linalg.inv(H-z*np.eye(d))

    # Synthetic prime-base groups split into first-power + proper-power tail.
    groups=[]
    primes=[]
    tails=[]
    for _ in range(13):
        A=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        P=(A+A.conj().T)/2/50
        E=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        E=(E+E.conj().T)/2/500
        primes.append(P)
        tails.append(E)
        groups.append(P+E)

    # D1 conditional averaging is exactly linear.
    lhs=sum(np.trace(R@G@R) for G in groups)/len(groups)
    M1=sum(groups)/len(groups)
    rhs=np.trace(R@M1@R)
    assert abs(lhs-rhs)<1e-10,(lhs,rhs)

    # Exact D2 difference expansion.
    total=0j
    expanded=0j
    for P,E,G in zip(primes,tails,groups):
        total += np.trace(R@G@R@G@R)
        expanded += (
            np.trace(R@P@R@P@R)
            + np.trace(R@P@R@E@R)
            + np.trace(R@E@R@P@R)
            + np.trace(R@E@R@E@R)
        )
    assert abs(total-expanded)<1e-9,(total,expanded)

    print("D1 average linearity error =",abs(lhs-rhs))
    print("D2 split expansion error =",abs(total-expanded))
    print("RESULT: WP84_D1_AGGREGATE_D2_PRIME_ONLY_ALGEBRA_PASS")

if __name__=="__main__":
    main()
