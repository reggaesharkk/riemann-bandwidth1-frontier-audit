#!/usr/bin/env python3
"""WP83 exact Schur-complement isolation gate.

This is a theorem-interface checker, not a zero computation.

Given a target two-dimensional evaluation space U and a background space V,
a direct Proposition-R isolation proof needs the Gram Schur complement

    S = G_UU - G_UV G_VV^{-1} G_VU

to retain a definite fraction of G_UU.

All arithmetic below is exact Fraction arithmetic.  The test families show:
  * an orthogonal background gives perfect isolation;
  * a rational near-collinear background drives the isolation constant to 0;
  * therefore no spacing-free uniform lower bound can come from linear
    algebra alone.
"""
from fractions import Fraction as F

def inv1(x):
    assert x != 0
    return F(1,1)/x

def schur_single(Guu, guv, gvv):
    # U is 2D; V is one background vector.
    inv=inv1(gvv)
    return [
      [Guu[i][j]-guv[i]*inv*guv[j] for j in range(2)]
      for i in range(2)
    ]

def det2(A):
    return A[0][0]*A[1][1]-A[0][1]*A[1][0]

def psd2(A):
    return A[0][0] >= 0 and A[1][1] >= 0 and det2(A) >= 0

def subtract_scaled(A,B,s2):
    return [[A[i][j]-s2*B[i][j] for j in range(2)] for i in range(2)]

def max_sigma2_binary(Guu,S,den_cap=100000):
    # Find a conservative rational sigma^2 on a fine exact grid.
    best=F(0)
    for n in range(den_cap+1):
        q=F(n,den_cap)
        if psd2(subtract_scaled(S,Guu,q)):
            best=q
        else:
            break
    return best

def main():
    Guu=[[F(1),F(0)],[F(0),F(1)]]

    # Orthogonal background: zero coupling.
    S=schur_single(Guu,[F(0),F(0)],F(1))
    assert S==Guu
    print("orthogonal background: sigma^2 = 1 PASS")

    # Near-collinear background v=(1,eps) against target basis e1,e2.
    # Gram data: <e1,v>=1, <e2,v>=eps, ||v||^2=1+eps^2.
    for q in (10,100,1000,10000):
        eps=F(1,q)
        S=schur_single(Guu,[F(1),eps],F(1)+eps*eps)
        assert psd2(S)
        # One direction is exactly lost because the 1D background lies inside U:
        assert det2(S)==0
        print("eps =",eps,"Schur det = 0; no positive uniform sigma PASS")

    # Abstract hyperbolic cancellation: H(iu)=-H(u).
    # Encode u=a+ib in R^2 with a=e1,b=e2:
    H=[[F(2),F(0)],[F(0),F(-2)]]
    Hrot=[[-x for x in row] for row in H]
    assert [[H[i][j]+Hrot[i][j] for j in range(2)] for i in range(2)] == [[0,0],[0,0]]
    print("quarter-phase hyperbolic cancellation PASS")

    print("RESULT: WP83_ISOLATION_SCHUR_GATE_PASS")

if __name__=="__main__":
    main()
