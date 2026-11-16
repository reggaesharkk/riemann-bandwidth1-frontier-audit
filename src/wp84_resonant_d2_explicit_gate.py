#!/usr/bin/env python3
"""Regression gate for the explicit resonant D2 state functional."""
import numpy as np

def main():
    rng=np.random.default_rng(8409)
    for d in (9,17,31):
        J=np.zeros((d,d),dtype=float)
        K2=np.zeros((d,d),dtype=float)
        for i in range(d):
            for j in range(d):
                if i!=j:
                    J[i,j]=1/(np.pi*(j-i))
                    K2[i,j]=1/((i-j)**2)

        X=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
        H=(X+X.conj().T)/2
        z=.31+1.7j
        R=np.linalg.inv(H-z*np.eye(d))
        # Complex symmetric because H is Hermitian, not transpose-symmetric in
        # general.  For the sharp real-symmetric WP84 core use a real-symmetric H.
        Y=rng.normal(size=(d,d))
        H=(Y+Y.T)/2
        R=np.linalg.inv(H-z*np.eye(d))
        assert np.max(np.abs(R-R.T))<1e-12

        a=1.0
        ca=1/(4*a*a)
        cb=1/(6*a*a)
        gam=1/(2*a*a*np.pi**2)

        # Exact alpha covariance contraction by summing coordinate basis.
        alpha_exact=0j
        for m in range(d):
            alpha=np.zeros(d); alpha[m]=1.0
            C=np.diag(alpha)@J-J@np.diag(alpha)
            alpha_exact += ca*np.trace(C@R@C@R)

        r=np.diag(R)
        h=np.diag(J@R)
        q=np.diag(J@R@J)
        alpha_formula=(1/(2*a*a))*(np.dot(h,h)-np.dot(r,q))
        assert abs(alpha_exact-alpha_formula)<2e-10,(d,alpha_exact,alpha_formula)

        # Exact beta covariance contraction.
        Cbb=cb*np.eye(d)-gam*K2
        M=R*R.T
        beta_exact=np.sum(Cbb*M)
        beta_formula=(
            cb*np.dot(r,r)
            -gam*sum(R[i,j]**2/((i-j)**2)
                     for i in range(d) for j in range(d) if i!=j)
        )
        assert abs(beta_exact-beta_formula)<2e-10,(d,beta_exact,beta_formula)

        print(
            "d",d,
            "alpha_error",abs(alpha_exact-alpha_formula),
            "beta_error",abs(beta_exact-beta_formula)
        )

    print("RESULT: WP84_RESONANT_D2_EXPLICIT_FUNCTIONAL_PASS")

if __name__=="__main__":
    main()
