#!/usr/bin/env python3
"""Numerical gate for the exact sharp displacement-rank identities.

The theorem is algebraic and proved in the companion note.  This script checks
representative finite matrices, arbitrary subset sums, Hermitian closure, and
the inherited resolvent commutator rank.
"""
import numpy as np

def partial_shift_matrix(d,L,y):
    s=y/L
    k=np.arange(d)
    U=np.empty((d,d),dtype=complex)
    for a in range(d):
        for b in range(d):
            if a==b:
                U[a,b]=(1.0-s)*np.exp(1j*2*np.pi*b*s)
            else:
                U[a,b]=(np.exp(1j*2*np.pi*a*s)-np.exp(1j*2*np.pi*b*s))/(
                    1j*2*np.pi*(b-a)
                )
    return U

def rank_num(A,tol=1e-10):
    sv=np.linalg.svd(A,compute_uv=False)
    return int(np.sum(sv>tol*max(1.0,sv[0]))),sv

def main():
    d=37
    L=9.0
    D=np.diag(np.arange(d,dtype=float))
    one=np.ones(d,dtype=complex)

    ys=[0.4,1.1,2.3,4.7,7.2]
    coeff=[0.7,-0.2,0.11,0.05,-0.03]
    T=13.25

    A=np.zeros((d,d),dtype=complex)
    q=np.zeros(d,dtype=complex)

    for y,c in zip(ys,coeff):
        U=partial_shift_matrix(d,L,y)
        s=y/L
        u=np.exp(1j*2*np.pi*np.arange(d)*s)

        comm=D@U-U@D
        rhs=1j/(2*np.pi)*(np.outer(u,one)-np.outer(one,u))
        assert np.linalg.norm(comm-rhs,np.inf)<2e-12

        a=c*np.exp(1j*T*y)
        A += a*U
        q += a*u

    commA=D@A-A@D
    rhsA=1j/(2*np.pi)*(np.outer(q,one)-np.outer(one,q))
    assert np.linalg.norm(commA-rhsA,np.inf)<1e-11
    rA,svA=rank_num(commA)
    assert rA<=2

    H=A+A.conj().T
    commH=D@H-H@D
    rH,svH=rank_num(commH)
    assert rH<=2

    z=0.37+1.4j
    R=np.linalg.inv(H-z*np.eye(d))
    commR=D@R-R@D
    rhsR=-R@commH@R
    assert np.linalg.norm(commR-rhsR,np.inf)<2e-11
    rR,svR=rank_num(commR)
    assert rR<=2

    print("rank [D,A+] =",rA)
    print("rank [D,H]  =",rH)
    print("rank [D,R]  =",rR)
    print("third singular [D,H] =",svH[2] if len(svH)>2 else 0.0)
    print("third singular [D,R] =",svR[2] if len(svR)>2 else 0.0)
    print("RESULT: WP84_LRSC_DISPLACEMENT_RANK_CLOSURE_PASS")

if __name__=="__main__":
    main()
