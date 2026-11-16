#!/usr/bin/env python3
"""Regression gate for the repeated-pole positive displacement identity."""

import numpy as np

def build_loewner(alpha,beta):
    d=len(alpha)
    H=np.diag(beta.astype(float)).astype(float)
    for i in range(d):
        for j in range(d):
            if i!=j:
                H[i,j]+=(alpha[i]-alpha[j])/(np.pi*(j-i))
    return H

def main():
    rng=np.random.default_rng(8420)
    for d in (19,31,47):
        alpha=rng.normal(size=d)/2
        beta=rng.normal(size=d)/3
        H=build_loewner(alpha,beta)
        I=np.eye(d,dtype=complex)
        U=(H+1j*I)@np.linalg.inv(H-1j*I)
        D=np.diag(np.arange(d,dtype=float))

        C=D@U-U@D
        s=np.linalg.svd(C,compute_uv=False)
        r2=int(np.sum(s>1e-9))
        assert r2<=2,(d,r2,s[:8])

        unerr=np.linalg.norm(U.conj().T@U-I,2)
        assert unerr<2e-10,(d,unerr)

        S=(U-U.conj().T)/(2j)

        for m in (3,10):
            A=I+1j*U
            Q=np.linalg.matrix_power(A,m)/(2.0**(m/2.0))

            defect1=Q.conj().T@Q
            defect2=np.linalg.matrix_power(I-S,m)
            derr=np.linalg.norm(defect1-defect2,'fro')
            assert derr<3e-8,(d,m,derr)

            Cm=D@Q-Q@D
            sm=np.linalg.svd(Cm,compute_uv=False)
            rm=int(np.sum(sm>1e-7))
            assert rm<=2*m,(d,m,rm,sm[:2*m+4])

            total=np.trace(Q.conj().T@Q).real/d
            diag=np.sum(np.abs(np.diag(Q))**2)/d
            off=0.0
            for i in range(d):
                for j in range(d):
                    if i!=j:
                        off += abs(Cm[i,j])**2/((i-j)**2)
            off/=d
            eerr=abs(total-(diag+off))
            assert eerr<2e-8,(d,m,total,diag,off,eerr)

            print(
                "d",d,
                "m",m,
                "rank[D,U]",r2,
                "rank[D,Qm]",rm,
                "unitary_error",unerr,
                "defect_identity_error",derr,
                "energy_error",eerr,
            )

    print("RESULT: WP84_RM_POSITIVE_DISPLACEMENT_ENERGY_PASS")

if __name__=="__main__":
    main()
