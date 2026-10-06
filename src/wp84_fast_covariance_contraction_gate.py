#!/usr/bin/env python3
"""Algebra gate: entrywise-small fast covariance gives a small normalized quadratic trace."""
import numpy as np

def main():
    rng=np.random.default_rng(8411)
    for d in (16,48,96):
        eps=3e-4
        C=eps*(rng.normal(size=(d,d))+1j*rng.normal(size=(d,d)))/np.sqrt(2)
        C*=eps/max(eps,np.max(np.abs(C)))

        A=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        B=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))

        # Normalize operator norms to <=1.
        A/=max(1.0,np.linalg.norm(A,2))
        B/=max(1.0,np.linalg.norm(B,2))

        val=sum(C[i,j]*A[i,j]*B[j,i]
                for i in range(d) for j in range(d))/d
        bound=np.max(np.abs(C))*np.linalg.norm(A,'fro')*np.linalg.norm(B,'fro')/d

        assert abs(val)<=bound*(1+1e-12)
        assert bound<=np.max(np.abs(C))*(1+1e-10)

        print("d",d,"|value|",abs(val),"HS bound",bound)

    print("RESULT: WP84_FAST_COVARIANCE_CONTRACTION_PASS")

if __name__=="__main__":
    main()
