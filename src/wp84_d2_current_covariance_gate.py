#!/usr/bin/env python3
"""Regression gate: for fixed state, the D2 primitive is quadratic in alpha,beta."""
import numpy as np

def build_B(alpha,beta,J):
    return np.diag(beta)+np.diag(alpha)@J-J@np.diag(alpha)

def primitive(alpha,beta,R,J):
    B=build_B(alpha,beta,J)
    X=B@R
    return np.trace(X@X)

def main():
    rng=np.random.default_rng(8408)
    d=17
    J=np.zeros((d,d),dtype=float)
    for i in range(d):
        for j in range(d):
            if i!=j:
                J[i,j]=1/(np.pi*(j-i))

    A=rng.normal(size=(d,d))+1j*rng.normal(size=(d,d))
    H=(A+A.conj().T)/2
    z=.2+1.3j
    R=np.linalg.inv(H-z*np.eye(d))

    a1=rng.normal(size=d); b1=rng.normal(size=d)
    a2=rng.normal(size=d); b2=rng.normal(size=d)

    # Homogeneous quadratic polarization identity.
    q1=primitive(a1,b1,R,J)
    q2=primitive(a2,b2,R,J)
    q12=primitive(a1+a2,b1+b2,R,J)
    q1m2=primitive(a1-a2,b1-b2,R,J)

    # q(x+y)+q(x-y)=2q(x)+2q(y)
    err=abs((q12+q1m2)-2*q1-2*q2)
    assert err<1e-9,err

    # Degree-two homogeneity.
    lam=1.731
    err2=abs(primitive(lam*a1,lam*b1,R,J)-lam**2*q1)
    assert err2<1e-9,err2

    print("polarization error =",err)
    print("homogeneity error =",err2)
    print("RESULT: WP84_D2_CURRENT_COVARIANCE_ONLY_PASS")

if __name__=="__main__":
    main()
