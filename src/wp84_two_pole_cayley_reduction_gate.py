#!/usr/bin/env python3
"""Regression gate for the two-pole Cayley geometric reduction."""
import numpy as np

def main():
    rng=np.random.default_rng(8416)
    for d in (9,21,37):
        X=rng.normal(size=(d,d))
        H=(X+X.T)/2
        I=np.eye(d)
        Ri=np.linalg.inv(H-1j*I)
        U=(H+1j*I)@Ri
        assert np.linalg.norm(U.conj().T@U-I)<1e-10

        b=9/4
        q=(b-1)/(b+1)
        Rb=np.linalg.inv(H-1j*b*I)

        # Exact functional identity.
        rhs=(U-I)/(1j*(1+b)) @ np.linalg.inv(I-q*U)
        assert np.linalg.norm(Rb-rhs)<1e-10

        for N in (4,6,8,10):
            S=np.zeros_like(U,dtype=complex)
            P=np.eye(d,dtype=complex)
            for n in range(N):
                S += (q**n)*P
                P=P@U
            approx=(U-I)/(1j*(1+b)) @ S
            err=np.linalg.norm(Rb-approx,2)
            assert err<=q**N*(1+1e-10),(d,N,err,q**N)
            print("d",d,"N",N,"operator_error",err,"bound",q**N)

    print("RESULT: WP84_TWO_POLE_CAYLEY_REDUCTION_PASS")

if __name__=="__main__":
    main()
