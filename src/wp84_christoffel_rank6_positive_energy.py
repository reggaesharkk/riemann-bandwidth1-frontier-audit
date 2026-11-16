#!/usr/bin/env python3
"""Regression gate for the bounded Christoffel rank-six positive energy."""

import numpy as np

P1=-43428/13891
P2= 37704/13891
P3=-9660/13891

def build_loewner(alpha,beta):
    d=len(alpha)
    H=np.diag(beta.astype(float)).astype(float)
    for i in range(d):
        for j in range(d):
            if i!=j:
                H[i,j]+=(alpha[i]-alpha[j])/(np.pi*(j-i))
    return H

def polyH(H):
    I=np.eye(H.shape[0],dtype=complex)
    return I+P1*H+P2*(H@H)+P3*(H@H@H)

def main():
    rng=np.random.default_rng(8461)

    for d in (17,29,43):
        alpha=rng.normal(size=d)/2
        beta=rng.normal(size=d)/3
        H=build_loewner(alpha,beta).astype(complex)
        I=np.eye(d,dtype=complex)
        D=np.diag(np.arange(d,dtype=float))

        C=D@H-H@D
        rC=int(np.sum(np.linalg.svd(C,compute_uv=False)>1e-9))
        assert rC<=2,(d,rC)

        A=polyH(H)
        CP=D@A-A@D
        rP=int(np.sum(np.linalg.svd(CP,compute_uv=False)>1e-7))
        assert rP<=6,(d,rP)

        for delta in (61.0,161.0,752.0,10000.0):
            s=np.sqrt(delta)
            R=np.linalg.inv(A+1j*s*I)
            Q=np.sqrt(delta+1.0)*A@R

            F=(delta+1.0)*(A@A)@np.linalg.inv(A@A+delta*I)
            ferr=np.linalg.norm(Q.conj().T@Q-F,'fro')
            assert ferr<2e-9,(d,delta,ferr)

            CQ=D@Q-Q@D
            pred=1j*np.sqrt(delta*(delta+1.0))*R@CP@R
            cerr=np.linalg.norm(CQ-pred,'fro')
            assert cerr<2e-8,(d,delta,cerr)

            rQ=int(np.sum(np.linalg.svd(CQ,compute_uv=False)>1e-7))
            assert rQ<=6,(d,delta,rQ)

            total=np.trace(Q.conj().T@Q).real/d
            diag=np.sum(np.abs(np.diag(Q))**2)/d
            off=0.0
            for i in range(d):
                for j in range(d):
                    if i!=j:
                        off += abs(CQ[i,j])**2/((i-j)**2)
            off/=d
            eerr=abs(total-(diag+off))
            assert eerr<2e-8,(d,delta,eerr)

            print(
                "d",d,
                "delta",delta,
                "rank[D,H]",rC,
                "rank[D,P(H)]",rP,
                "rank[D,Q_delta]",rQ,
                "factor_error",ferr,
                "commutator_error",cerr,
                "energy_error",eerr,
            )

    print("RESULT: WP84_CHRISTOFFEL_RANK6_ENERGY_PASS")

if __name__=="__main__":
    main()
