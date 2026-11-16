#!/usr/bin/env python3
"""Exact-algebra numerical gate for the Hadamard covariance-map formula."""

import numpy as np

def main():
    rng=np.random.default_rng(8407)

    for d in (5,9,17):
        J=np.zeros((d,d),dtype=float)
        for i in range(d):
            for j in range(d):
                if i!=j:
                    J[i,j]=1.0/(np.pi*(j-i))

        for r in (1,3,7):
            avec=[rng.normal(size=d) for _ in range(r)]
            hvec=[rng.normal(size=d) for _ in range(r)]

            A=sum(np.outer(a,a) for a in avec)
            H=sum(np.outer(h,h) for h in hvec)
            C=sum(np.outer(h,a) for h,a in zip(hvec,avec))

            X=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))

            direct=np.zeros((d,d),dtype=complex)
            for a,h in zip(avec,hvec):
                W=np.diag(h)+np.diag(a)@J-J@np.diag(a)
                direct += W@X@W

            pred=(
                H*X
                +(C*X)@J
                -C*(X@J)
                +(C.T*(J@X))
                -J@(C.T*X)
                +(A*(J@X))@J
                -A*(J@X@J)
                -J@(A*X)@J
                +J@(A*(X@J))
            )

            err=np.linalg.norm(direct-pred,np.inf)
            assert err<2e-11,(d,r,err)
            print("d",d,"directions",r,"inf_error",err)

    print("RESULT: WP84_GAUSSIAN_COVARIANCE_HADAMARD_PASS")

if __name__=="__main__":
    main()
