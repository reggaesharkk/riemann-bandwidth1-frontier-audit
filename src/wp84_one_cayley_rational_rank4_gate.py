#!/usr/bin/env python3
import numpy as np

def main():
    rng=np.random.default_rng(8416)
    for d in (13,27,41):
        X=rng.normal(size=(d,d))
        H=(X+X.T)/2
        D=np.diag(np.arange(d,dtype=float))
        I=np.eye(d,dtype=complex)
        U=(H+1j*I)@np.linalg.inv(H-1j*I)

        b=9/4
        q=(b-1)/(b+1)
        A=np.linalg.inv(I-q*U)

        Ub=(H+1j*b*I)@np.linalg.inv(H-1j*b*I)
        Ub2=(U-q*I)@A
        assert np.linalg.norm(Ub-Ub2)<1e-10

        C=D@U-U@D
        Cb=D@Ub-Ub@D
        Cb2=(1-q*q)*A@C@A
        assert np.linalg.norm(Cb-Cb2)<1e-9

        a=(1-1j)/2
        g=(1+1j)/2
        L1=a*I+g*U
        Lb=a*I+g*Ub
        K=L1@Lb

        CK=D@K-K@D
        CK2=g*C@Lb+g*(1-q*q)*L1@A@C@A
        assert np.linalg.norm(CK-CK2)<1e-9

        assert np.linalg.norm(A,2)<=13/8+1e-10
        print("d",d,"A_norm",np.linalg.norm(A,2),
              "mobius_err",np.linalg.norm(Ub-Ub2),
              "comm_err",np.linalg.norm(CK-CK2))
    print("RESULT: WP84_ONE_CAYLEY_RATIONAL_COMMUTATOR_PASS")

if __name__=="__main__":
    main()
