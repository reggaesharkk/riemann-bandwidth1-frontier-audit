#!/usr/bin/env python3
"""Exact finite-matrix regression for quadrature covariance cancellation."""

import numpy as np

def main():
    rng=np.random.default_rng(8406)

    for d in (5,11,23):
        for _ in range(7):
            A=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
            X=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))

            C=A+A.conj().T
            S=1j*(A-A.conj().T)

            lhs=0.5*(C@X@C+S@X@S)
            rhs=A@X@A.conj().T+A.conj().T@X@A

            err=np.linalg.norm(lhs-rhs,np.inf)
            assert err<2e-11,(d,err)

    print("quadrature covariance identity verified")
    print("RESULT: WP84_GAUSSIAN_QUADRATURE_MIXED_COVARIANCE_PASS")

if __name__=="__main__":
    main()
