#!/usr/bin/env python3
"""WP83 PT-star endpoint-transfer falsifier.

Take equally spaced frequencies omega_j=j/L, j=0,...,M-1, all with equal
positive multiplicity 1 and equal depth.  On the endpoint interval
J=[(1-2 theta)L,(1-theta)L], x=v/L stays away from 0 mod 2*pi, so

  q(v)=sum_{j=0}^{M-1} exp(i j v/L)
      = exp(i(M-1)x/2) sin(Mx/2)/sin(x/2)

has |q(v)| <= csc((1-2 theta)/2), independent of M.

Choosing M~T L saturates only O(L) points per unit ordinate interval, while
the endpoint energy is O(L).  Hence energy/M=O(1/T), smaller than every
negative power of L.  PT-star as a uniform polynomial-in-L endpoint floor is
therefore false under local-count + positivity alone.
"""
import math

THETA=1/8
c=1.0/(math.sin((1-2*THETA)/2.0)**2)

def main():
    print("theta =",THETA)
    print("endpoint energy coefficient <= theta*c =",THETA*c)
    # diagnostic scaling only; the proof is analytic in the companion note.
    for L in (20,40,80,160):
        T=math.exp(L/2)  # any exponential-in-L height relation suffices
        M=max(1,int(T*L/4))
        ratio=(THETA*c*L)/M
        print(f"L={L:3d}  M~{M:.4e}  energy/M <= {ratio:.4e}")
        # Compare against a few inverse powers of L.
        if L>=40:
            assert ratio < L**-2
    print("RESULT: WP83_PT_STAR_COUNTEREXAMPLE_DIAGNOSTIC_PASS")

if __name__=="__main__":
    main()
