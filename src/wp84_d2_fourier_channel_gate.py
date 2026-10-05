#!/usr/bin/env python3
"""Numerical regression gate for the exact rank-r Fourier reduction."""
import numpy as np
import math

def S2(t):
    return math.pi**2/3-math.pi*t+t*t/2

def main():
    rng=np.random.default_rng(8404)
    for d in (9,17,31):
        for r in (1,2,4):
            G=rng.normal(size=(d,r))+1j*rng.normal(size=(d,r))
            H=rng.normal(size=(d,r))+1j*rng.normal(size=(d,r))
            C=G@H.T

            lhs=0j
            for i in range(d):
                for j in range(d):
                    if i!=j:
                        lhs += C[i,j]*C[j,i]/((i-j)**2)

            # Trapezoidal rule is spectrally exact here once the grid
            # resolves all Fourier modes of the finite trigonometric
            # polynomial times the degree-2 periodic Bernoulli kernel.
            # Use a very fine grid as an independent numerical regression.
            n=131072
            ts=(np.arange(n)+0.5)*(2*np.pi/n)
            rhs=0j
            idx=np.arange(d)
            for t in ts:
                phase=np.exp(1j*t*idx)
                A=H.T@(phase[:,None]*G)
                Am=H.T@(phase.conj()[:,None]*G)
                rhs += S2(float(t))*np.trace(A@Am)
            rhs/=n
            err=abs(lhs-rhs)
            scale=max(1.0,abs(lhs))
            assert err/scale<3e-8,(d,r,lhs,rhs,err/scale)
            print("d",d,"r",r,"relative_error",err/scale)
    print("RESULT: WP84_D2_FOURIER_CHANNEL_GATE_PASS")

if __name__=="__main__":
    main()
