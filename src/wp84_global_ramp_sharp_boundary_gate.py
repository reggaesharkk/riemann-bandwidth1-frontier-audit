#!/usr/bin/env python3
"""Finite algebra gate for the global ramp-to-sharp factorization.

The proof-level statement is algebraic.  This script checks it on finite
non-cyclic shift matrices and verifies that summing shifts before estimating
gives the same exact boundary-factorized error.
"""
import numpy as np

def shift(N,r):
    S=np.zeros((N,N))
    if r>=0:
        for i in range(N-r):
            S[i,i+r]=1.0
    else:
        return shift(N,-r).T
    return S

def main():
    N=31
    w=3

    chi=np.ones(N)
    phi=np.ones(N)
    # fixed boundary ramps
    ramp=np.linspace(0.25,0.75,w)
    phi[:w]=ramp
    phi[-w:]=ramp[::-1]
    r=chi-phi

    Mchi=np.diag(chi)
    Mphi=np.diag(phi)
    Mr=np.diag(r)

    shifts=[1,3,5,7,9]
    coeff=[0.7,-0.2,0.11,0.05,-0.03]

    actual=np.zeros((N,N))
    sharp=np.zeros((N,N))
    K=np.zeros((N,N))

    for y,c in zip(shifts,coeff):
        U=shift(N,y)
        actual += c*(Mphi@U@Mphi)
        sharp  += c*(Mchi@U@Mchi)
        K      += c*U

    direct=actual-sharp
    factored= -Mr@K@Mchi - Mchi@K@Mr + Mr@K@Mr

    err=np.linalg.norm(direct-factored,ord=np.inf)
    print("positive-branch factorization error =",err)
    assert err < 1e-13

    # Add the adjoint branch.
    direct_real=direct+direct.T
    factored_real=factored+factored.T
    err2=np.linalg.norm(direct_real-factored_real,ord=np.inf)
    print("real factorization error =",err2)
    assert err2 < 1e-13

    # Exact finite support statement: every algebraic term contains Mr.
    boundary=np.flatnonzero(np.abs(r)>0)
    print("boundary sites =",boundary.tolist())
    print("boundary count =",len(boundary))
    print("RESULT: WP84_GLOBAL_RAMP_SHARP_BOUNDARY_FACTOR_PASS")

if __name__=="__main__":
    main()
