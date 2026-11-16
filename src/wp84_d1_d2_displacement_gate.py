#!/usr/bin/env python3
"""Finite verification of the rank-four D1/D2 displacement formulas."""

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

def sharp_hermitian(d,L,T,ys,cs):
    A=np.zeros((d,d),dtype=complex)
    for y,c in zip(ys,cs):
        A += c*np.exp(1j*T*y)*partial_shift(d,L,y)
    return A+A.conj().T

def rank_num(A,tol=1e-10):
    sv=np.linalg.svd(A,compute_uv=False)
    return int(np.sum(sv>tol*max(1.0,sv[0])))

def trace_square_from_displacement(X):
    d=X.shape[0]
    D=np.diag(np.arange(d,dtype=float))
    C=D@X-X@D
    out=np.sum(np.diag(X)**2)
    for i in range(d):
        for j in range(d):
            if i!=j:
                out -= C[i,j]*C[j,i]/((i-j)**2)
    return out,C

def main():
    d=33
    L=9.0
    T=15.0
    D=np.diag(np.arange(d,dtype=float))

    H=0.8*np.eye(d)+sharp_hermitian(
        d,L,T,
        [0.4,1.2,2.4,4.0,6.7],
        [0.31,-0.12,0.08,0.04,-0.018],
    )
    B=sharp_hermitian(d,L,T,[1.7],[0.075])

    z=0.23+1.35j
    R=np.linalg.inv(H-z*np.eye(d))
    X=B@R

    assert rank_num(D@B-B@D)<=2
    assert rank_num(D@R-R@D)<=2
    C=D@X-X@D
    assert rank_num(C)<=4

    tr2=np.trace(X@X)
    tr2_disp,C2=trace_square_from_displacement(X)
    assert abs(tr2-tr2_disp)<2e-10

    # Direct D1/D2 identities.
    D1=np.trace(R@B@R)/d
    D2=np.trace(R@B@R@B@R)/d

    D1_alt=np.trace(B@R@R)/d
    D2_alt=0.5*(
        np.trace(B@R@R@B@R)+np.trace(B@R@B@R@R)
    )/d

    assert abs(D1-D1_alt)<2e-12
    assert abs(D2-D2_alt)<2e-12

    # Symmetric finite difference in z checks the derivative statements.
    h=1e-6
    def Rz(zz):
        return np.linalg.inv(H-zz*np.eye(d))
    Rp=Rz(z+h)
    Rm=Rz(z-h)
    f1p=np.trace(B@Rp)/d
    f1m=np.trace(B@Rm)/d
    f2p=np.trace((B@Rp)@(B@Rp))/d
    f2m=np.trace((B@Rm)@(B@Rm))/d
    fd1=(f1p-f1m)/(2*h)
    fd2=0.5*(f2p-f2m)/(2*h)

    assert abs(fd1-D1)<2e-6
    assert abs(fd2-D2)<2e-6

    print("rank [D,B] =",rank_num(D@B-B@D))
    print("rank [D,R] =",rank_num(D@R-R@D))
    print("rank [D,BR] =",rank_num(C))
    print("trace-square reconstruction error =",abs(tr2-tr2_disp))
    print("D1 derivative error =",abs(fd1-D1))
    print("D2 derivative error =",abs(fd2-D2))
    print("RESULT: WP84_D1_D2_DISPLACEMENT_REDUCTION_PASS")

if __name__=="__main__":
    main()
