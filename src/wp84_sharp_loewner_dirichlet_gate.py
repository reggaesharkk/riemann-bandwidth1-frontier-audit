#!/usr/bin/env python3
"""Exact-form numerical gate for the sharp Loewner/Calderon representation."""

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

def main():
    d=41
    L=11.0
    T=17.25
    ys=np.array([0.31,0.83,1.9,3.2,5.7,8.4])
    cs=np.array([0.4,-0.17,0.09,0.055,-0.021,0.013])

    tau=T+2*np.pi*np.arange(d)/L

    A=np.zeros((d,d),dtype=complex)
    for y,c in zip(ys,cs):
        A += c*np.exp(1j*T*y)*partial_shift(d,L,y)
    P=A+A.conj().T

    Q=np.zeros(d,dtype=complex)
    Qp=np.zeros(d,dtype=complex)
    for y,c in zip(ys,cs):
        z=np.exp(1j*tau*y)
        Q += c*z
        Qp += 1j*c*y*z

    a=Q.imag
    b=Q.real
    ap=Qp.imag

    Pred=np.zeros((d,d),dtype=float)
    for k in range(d):
        for l in range(d):
            if k==l:
                Pred[k,l]=2*b[k]-2*ap[k]/L
            else:
                Pred[k,l]=(a[k]-a[l])/(np.pi*(l-k))

    err=np.linalg.norm(P-Pred,np.inf)
    assert err<5e-12

    J=np.zeros((d,d),dtype=float)
    for k in range(d):
        for l in range(d):
            if k!=l:
                J[k,l]=1/(np.pi*(l-k))
    comm=np.diag(a)@J-J@np.diag(a)
    P2=np.diag(2*b-2*ap/L)+comm
    assert np.linalg.norm(P2-Pred,np.inf)<1e-13

    D=np.diag(np.arange(d,dtype=float))
    disp=D@Pred-Pred@D
    rhs=-(np.outer(a,np.ones(d))-np.outer(np.ones(d),a))/np.pi
    assert np.linalg.norm(disp-rhs,np.inf)<2e-12

    sv=np.linalg.svd(disp,compute_uv=False)
    rank=int(np.sum(sv>1e-10*max(1.0,sv[0])))
    assert rank<=2

    print("matrix reconstruction inf-error =",err)
    print("rank [D,P] =",rank)
    print("third displacement singular value =",sv[2])
    print("RESULT: WP84_SHARP_LOEWNER_DIRICHLET_GATE_PASS")

if __name__=="__main__":
    main()
