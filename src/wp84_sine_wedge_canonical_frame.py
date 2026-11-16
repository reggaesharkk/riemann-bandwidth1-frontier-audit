#!/usr/bin/env python3
"""Regression gate for the canonical two-vector wedge frame."""
import numpy as np

def build(alpha,beta):
    d=len(alpha)
    H=np.diag(beta.astype(float)).astype(float)
    for i in range(d):
        for j in range(d):
            if i!=j:
                H[i,j]+=(alpha[i]-alpha[j])/(np.pi*(j-i))
    return H

def invsqrt2(G):
    w,V=np.linalg.eigh(G)
    return V@np.diag(w**(-0.5))@V.conj().T

def main():
    rng=np.random.default_rng(8422)

    a=63/50
    t=17/16
    coeff=4*t*t*a*a/3

    for d in (17,37,61):
        alpha=rng.normal(size=d)/2
        beta=rng.normal(size=d)/3
        H=build(alpha,beta)
        R=np.linalg.inv(H-1j*a*np.eye(d))

        u=R@np.ones(d)
        v=R@alpha
        W=np.column_stack([u,v])
        G=W.conj().T@W

        detG=np.linalg.det(G).real
        assert detG>1e-12

        M=detG**0.25*invsqrt2(G)
        assert abs(np.linalg.det(M)-1)<1e-9

        Wc=W@M
        Gc=Wc.conj().T@Wc
        target=np.sqrt(detG)*np.eye(2)
        assert np.linalg.norm(Gc-target)<1e-8

        # Wedge invariance.
        X=np.outer(u,v)-np.outer(v,u)
        uc=Wc[:,0]
        vc=Wc[:,1]
        Xc=np.outer(uc,vc)-np.outer(vc,uc)
        assert np.linalg.norm(X-Xc)<1e-8

        ell=np.sum(np.abs(Wc)**2,axis=1)/np.sqrt(detG)
        assert abs(np.sum(ell)-2)<1e-9
        assert np.min(ell)>-1e-12
        assert np.max(ell)<1+1e-9

        kappa=d*np.dot(ell,ell)
        gamma=detG/d**2

        # Exact direct off-diagonal energy.
        D=np.diag(np.arange(d,dtype=float))
        Q=np.eye(d)-t*a*(R+R.conj())
        CQ=D@Q-Q@D

        eoff=0.0
        for i in range(d):
            for j in range(d):
                if i!=j:
                    eoff += abs(CQ[i,j])**2/(i-j)**2
        eoff/=d

        major=coeff*gamma*kappa
        assert eoff<=major*(1+1e-9)

        print(
            "d",d,
            "gamma",gamma,
            "kappa",kappa,
            "offdiag",eoff,
            "major",major
        )

    print("RESULT: WP84_SINE_CANONICAL_FRAME_PASS")

if __name__=="__main__":
    main()
