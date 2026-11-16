#!/usr/bin/env python3
"""Regression gate for the scalar K2 wedge identity."""
import numpy as np

def main():
    rng=np.random.default_rng(8423)

    for d in (11,29,53):
        u=rng.normal(size=d)+1j*rng.normal(size=d)
        v=rng.normal(size=d)+1j*rng.normal(size=d)

        K=np.zeros((d,d),dtype=float)
        for i in range(d):
            for j in range(d):
                if i!=j:
                    K[i,j]=1/(i-j)**2

        W=np.outer(u,v)-np.outer(v,u)

        lhs=np.sum(K*(np.real(W)**2))

        A=np.abs(u)**2
        B=np.abs(v)**2
        C=u*np.conj(v)
        P=u**2
        Q=v**2
        S=u*v

        rhs=(
            A@K@B
            -np.real(np.vdot(C,K@C))
            +np.real(P@K@Q-S@K@S)
        )

        assert abs(lhs-rhs)<1e-9

        print("d",d,"wedge_sum",lhs,"scalar_sum",rhs)

    print("RESULT: WP84_SINE_SCALAR_K2_WEDGE_PASS")

if __name__=="__main__":
    main()
