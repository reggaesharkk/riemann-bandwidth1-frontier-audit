#!/usr/bin/env python3
"""Regression gate for the sharp partial-shift derivative identities and BV decomposition."""
import numpy as np

def Uplus(d,s):
    U=np.empty((d,d),dtype=complex)
    for k in range(d):
        for l in range(d):
            if k==l:
                U[k,l]=(1-s)*np.exp(2j*np.pi*k*s)
            else:
                U[k,l]=(np.exp(2j*np.pi*k*s)-np.exp(2j*np.pi*l*s))/(
                    2j*np.pi*(l-k)
                )
    return U

def dUplus_exact(d,s):
    U=Uplus(d,s)
    D=np.diag(np.arange(d,dtype=float))
    e=np.exp(2j*np.pi*np.arange(d)*s)
    one=np.ones(d)
    return 2j*np.pi*U@D-np.outer(e,one)

def main():
    rng=np.random.default_rng(8410)
    for d in (7,19,41):
        D=np.diag(np.arange(d,dtype=float))
        one=np.ones(d)
        for s in (0.07,0.31,0.73,0.94):
            U=Uplus(d,s)
            Um=U.conj().T
            e=np.exp(2j*np.pi*np.arange(d)*s)

            # Central finite-difference check of the exact derivative.
            h=1e-7
            fd=(Uplus(d,s+h)-Uplus(d,s-h))/(2*h)
            pred=2j*np.pi*U@D-np.outer(e,one)
            rel=np.linalg.norm(fd-pred)/max(1.0,np.linalg.norm(pred))
            assert rel<2e-7,(d,s,rel)

            fdm=(Uplus(d,s+h).conj().T-Uplus(d,s-h).conj().T)/(2*h)
            predm=-2j*np.pi*D@Um-np.outer(one,e.conj())
            relm=np.linalg.norm(fdm-predm)/max(1.0,np.linalg.norm(predm))
            assert relm<2e-7,(d,s,relm)

        # Check the collapsed derivative formula for g_R(s).
        Y=rng.normal(size=(d,d))
        H=(Y+Y.T)/2
        z=.17+1.6j
        R=np.linalg.inv(H-z*np.eye(d))
        s=.43
        U=Uplus(d,s); Um=U.conj().T
        e=np.exp(2j*np.pi*np.arange(d)*s)

        gp=(
            2j*np.pi*np.trace(Um@R@U@(D@R-R@D))/d
            -np.trace(R@np.outer(e,one)@R@Um)/d
            -np.trace(R@U@R@np.outer(one,e.conj()))/d
        )

        h=2e-7
        def g(x):
            V=Uplus(d,x)
            return np.trace(R@V@R@V.conj().T)/d
        fdg=(g(s+h)-g(s-h))/(2*h)
        err=abs(fdg-gp)
        assert err<2e-7,(d,fdg,gp,err)
        print("d",d,"g derivative error",err)

    print("RESULT: WP84_RESONANT_D2_BV_DERIVATIVE_PASS")

if __name__=="__main__":
    main()
