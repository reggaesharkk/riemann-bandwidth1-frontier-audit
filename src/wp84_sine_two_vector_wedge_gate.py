#!/usr/bin/env python3
"""Regression gate for the two-vector wedge representation of [D,Q]."""
import numpy as np

def build(alpha,beta):
    d=len(alpha)
    H=np.diag(beta.astype(float)).astype(float)
    for i in range(d):
        for j in range(d):
            if i!=j:
                H[i,j]+=(alpha[i]-alpha[j])/(np.pi*(j-i))
    return H

def main():
    rng=np.random.default_rng(8421)

    a=63/50
    t=17/16

    for d in (13,31,57):
        alpha=rng.normal(size=d)/2
        beta=rng.normal(size=d)/3
        H=build(alpha,beta)

        D=np.diag(np.arange(d,dtype=float))
        I=np.eye(d)

        R=np.linalg.inv(H-1j*a*I)
        Rm=np.linalg.inv(H+1j*a*I)

        Q=I-t*a*(R+Rm)
        X=D@Q-Q@D

        u=R@np.ones(d)
        v=R@alpha

        X2=(
            2*t*a/np.pi
            *
            np.real(
                np.outer(u,v)
                -np.outer(v,u)
            )
        )

        assert np.linalg.norm(X-X2)<1e-9

        ediag=np.mean(np.diag(Q)**2).real

        eoff=0.0
        for i in range(d):
            for j in range(d):
                if i!=j:
                    eoff += abs(X[i,j])**2/(i-j)**2
        eoff/=d

        rho=np.abs(u)**2+np.abs(v)**2
        major=(
            4*t*t*a*a/(3*d)
            *
            np.dot(rho,rho)
        )

        assert eoff<=major*(1+1e-10)

        direct=np.trace(Q@Q).real/d
        assert abs(direct-(ediag+eoff))<1e-9

        print(
            "d",d,
            "direct",direct,
            "offdiag",eoff,
            "rho_majorant",major
        )

    print("RESULT: WP84_SINE_TWO_VECTOR_WEDGE_PASS")

if __name__=="__main__":
    main()
