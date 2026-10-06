#!/usr/bin/env python3
"""Regression gate for the exact small-integer rank-six Cayley energy."""
import numpy as np

def build_loewner(alpha,beta):
    d=len(alpha)
    H=np.diag(beta.astype(float)).astype(float)
    for i in range(d):
        for j in range(d):
            if i!=j:
                H[i,j]+=(alpha[i]-alpha[j])/(np.pi*(j-i))
    return H

def q_of_U(U):
    I=np.eye(U.shape[0],dtype=complex)
    return (
        72*np.linalg.matrix_power(U,3)
        -(6+106j)*np.linalg.matrix_power(U,2)
        -(44+8j)*U
        -(12-3j)*I
    )/105.0

def main():
    rng=np.random.default_rng(8416)

    for d in (23,41,67):
        alpha=rng.normal(size=d)/2
        beta=rng.normal(size=d)/3
        H=build_loewner(alpha,beta)

        I=np.eye(d,dtype=complex)
        U=(H+1j*I)@np.linalg.inv(H-1j*I)
        Q=q_of_U(U)

        D=np.diag(np.arange(d,dtype=float))
        C=D@U-U@D
        CQ=D@Q-Q@D

        # Verify unitary Cayley transform.
        unerr=np.linalg.norm(U.conj().T@U-I,2)
        assert unerr<2e-11,(d,unerr)

        # Sharp Loewner displacement rank should be <=2 for U.
        s=np.linalg.svd(C,compute_uv=False)
        r2=np.sum(s>1e-9)
        assert r2<=2,(d,r2,s[:8])

        # Exact polynomial commutator factorization.
        q1=-(44+8j)/105
        q2=-(6+106j)/105
        q3=72/105
        pred=(
            C@(q1*I+q2*U+q3*(U@U))
            +U@C@(q2*I+q3*U)
            +(U@U)@C*q3
        )
        ferr=np.linalg.norm(CQ-pred,'fro')
        assert ferr<5e-9,(d,ferr)

        sQ=np.linalg.svd(CQ,compute_uv=False)
        r6=np.sum(sQ>1e-8)
        assert r6<=6,(d,r6,sQ[:10])

        # Positive displacement-energy identity.
        total=np.trace(Q.conj().T@Q).real/d
        diag=np.sum(np.abs(np.diag(Q))**2)/d
        off=0.0
        for i in range(d):
            for j in range(d):
                if i!=j:
                    off += abs(CQ[i,j])**2/((i-j)**2)
        off/=d
        eerr=abs(total-(diag+off))
        assert eerr<2e-10,(d,total,diag,off,eerr)

        print(
            "d",d,
            "rank[D,U]",int(r2),
            "rank[D,Q]",int(r6),
            "unitary_error",unerr,
            "factor_error",ferr,
            "energy_error",eerr
        )

    print("RESULT: WP84_INTEGER_RANK6_ENERGY_GATE_PASS")

if __name__=="__main__":
    main()
