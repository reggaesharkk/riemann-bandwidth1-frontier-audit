#!/usr/bin/env python3
"""Finite regression gate for the rank-three BR displacement sharpening."""

import numpy as np

def partial_shift(d,L,y):
    s=y/L
    U=np.empty((d,d),dtype=complex)
    for k in range(d):
        for l in range(d):
            if k==l:
                U[k,l]=(1-s)*np.exp(1j*2*np.pi*k*s)
            else:
                U[k,l]=(np.exp(1j*2*np.pi*k*s)-np.exp(1j*2*np.pi*l*s))/(
                    1j*2*np.pi*(l-k)
                )
    return U

def sharp_block(d,L,T,ys,cs):
    tau=T+2*np.pi*np.arange(d)/L
    A=np.zeros((d,d),dtype=complex)
    Q=np.zeros(d,dtype=complex)
    Qp=np.zeros(d,dtype=complex)
    for y,c in zip(ys,cs):
        A += c*np.exp(1j*T*y)*partial_shift(d,L,y)
        zz=np.exp(1j*tau*y)
        Q += c*zz
        Qp += 1j*c*y*zz
    return A+A.conj().T,Q,Qp

def numerical_rank(A,tol=1e-10):
    sv=np.linalg.svd(A,compute_uv=False)
    return int(np.sum(sv>tol*max(1.0,sv[0])))

def main():
    d=37
    L=10.0
    T=18.25
    D=np.diag(np.arange(d,dtype=float))

    P,Q,Qp=sharp_block(
        d,L,T,
        [0.31,0.8,1.6,2.7,4.4,7.2],
        [0.27,-0.13,0.081,0.043,-0.019,0.011],
    )
    B,Qb,Qbp=sharp_block(
        d,L,T,
        [1.3,3.9],
        [0.073,0.008],
    )

    H=0.91*np.eye(d)+P
    z=0.17+1.41j
    R=np.linalg.inv(H-z*np.eye(d))

    a=Q.imag
    alpha=Qb.imag
    beta=2*Qb.real-2*Qbp.imag/L

    one=np.ones(d)
    u=R@one
    v=R@a
    w=R@alpha

    CB=D@B-B@D
    CR=D@R-R@D

    CB0=(np.outer(one,alpha)-np.outer(alpha,one))/np.pi
    CR0=(np.outer(v,u)-np.outer(u,v))/np.pi

    assert np.linalg.norm(CB-CB0,np.inf)<5e-12
    assert np.linalg.norm(CR-CR0,np.inf)<5e-12

    X=B@R
    CX=D@X-X@D

    s=B@v
    t=B@u
    CX3=(
        np.outer(one,w)
        + np.outer(s-alpha,u)
        - np.outer(t,v)
    )/np.pi

    assert np.linalg.norm(CX-CX3,np.inf)<1e-11
    assert numerical_rank(CX)<=3

    K2=np.zeros((d,d),dtype=float)
    for i in range(d):
        for j in range(d):
            if i!=j:
                K2[i,j]=1.0/(i-j)**2

    La=np.diag(alpha)@K2-K2@np.diag(alpha)
    assert np.linalg.norm(La+La.T,np.inf)<1e-13

    rdiag=np.diag(R)
    xdiag=np.diag(X)
    xpred=(
        beta*rdiag
        +(u*(La@v)-v*(La@u))/np.pi**2
    )
    assert np.max(np.abs(xdiag-xpred))<2e-12

    tr1=np.trace(X)
    tr1pred=np.dot(beta,rdiag)+(2/np.pi**2)*(u.T@La@v)
    assert abs(tr1-tr1pred)<2e-11

    tr2=np.trace(X@X)
    tr2pred=np.sum(xpred*xpred)
    for i in range(d):
        for j in range(d):
            if i!=j:
                tr2pred -= CX3[i,j]*CX3[j,i]/((i-j)**2)
    assert abs(tr2-tr2pred)<2e-10

    print("rank [D,B] =",numerical_rank(CB))
    print("rank [D,R] =",numerical_rank(CR))
    print("rank [D,BR] =",numerical_rank(CX))
    print("BR displacement factorization error =",np.linalg.norm(CX-CX3,np.inf))
    print("diag(BR) max error =",np.max(np.abs(xdiag-xpred)))
    print("tr(BR) error =",abs(tr1-tr1pred))
    print("tr((BR)^2) error =",abs(tr2-tr2pred))
    print("RESULT: WP84_BR_RANK3_SCALAR_D1_GATE_PASS")

if __name__=="__main__":
    main()
