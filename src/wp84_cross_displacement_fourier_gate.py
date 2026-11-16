#!/usr/bin/env python3
"""Regression gate for the exact cross-displacement Fourier identity."""
import numpy as np
import math

def S2(t):
    return math.pi**2/3-math.pi*t+t*t/2

def main():
    rng=np.random.default_rng(8405)
    for d in (8,15,27):
        for ra,rb in ((1,1),(2,2),(2,4),(4,3)):
            GA=rng.normal(size=(d,ra))+1j*rng.normal(size=(d,ra))
            HA=rng.normal(size=(d,ra))+1j*rng.normal(size=(d,ra))
            GB=rng.normal(size=(d,rb))+1j*rng.normal(size=(d,rb))
            HB=rng.normal(size=(d,rb))+1j*rng.normal(size=(d,rb))
            CA=GA@HA.T
            CB=GB@HB.T

            lhs=0j
            for i in range(d):
                for j in range(d):
                    if i!=j:
                        lhs += CA[i,j]*CB[j,i]/((i-j)**2)

            n=65536
            idx=np.arange(d)
            rhs=0j
            for q in range(n):
                t=(q+0.5)*(2*np.pi/n)
                phase=np.exp(1j*t*idx)
                A=HA.T@(phase[:,None]*GB)
                B=HB.T@(phase.conj()[:,None]*GA)
                rhs += S2(float(t))*np.trace(A@B)
            rhs/=n

            rel=abs(lhs-rhs)/max(1.0,abs(lhs))
            assert rel<2e-8,(d,ra,rb,rel)
            print("d",d,"ranks",ra,rb,"relative_error",rel)

    # Direct cross trace reconstruction check with arbitrary diagonals.
    d=19
    ra,rb=2,2
    GA=rng.normal(size=(d,ra))+1j*rng.normal(size=(d,ra))
    HA=rng.normal(size=(d,ra))+1j*rng.normal(size=(d,ra))
    GB=rng.normal(size=(d,rb))+1j*rng.normal(size=(d,rb))
    HB=rng.normal(size=(d,rb))+1j*rng.normal(size=(d,rb))
    CA=GA@HA.T; CB=GB@HB.T
    da=rng.normal(size=d)+1j*rng.normal(size=d)
    db=rng.normal(size=d)+1j*rng.normal(size=d)

    A=np.diag(da.astype(complex))
    B=np.diag(db.astype(complex))
    for i in range(d):
        for j in range(d):
            if i!=j:
                A[i,j]=CA[i,j]/(i-j)
                B[i,j]=CB[i,j]/(i-j)

    direct=np.trace(A@B)
    cross=sum(CA[i,j]*CB[j,i]/((i-j)**2)
              for i in range(d) for j in range(d) if i!=j)
    recon=np.dot(da,db)-cross
    assert abs(direct-recon)<1e-9
    print("direct cross trace error",abs(direct-recon))
    print("RESULT: WP84_CROSS_DISPLACEMENT_FOURIER_PASS")

if __name__=="__main__":
    main()
