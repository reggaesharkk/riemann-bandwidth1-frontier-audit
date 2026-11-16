#!/usr/bin/env python3
"""Regression gate for the exact-frontier bounded Christoffel-Cayley consumer."""

from fractions import Fraction as F
import numpy as np

A=F(43428,13891)
B=F(37704,13891)
C=F(9660,13891)
W0=F(1415,13891)

def exact_gate():
    # a_*^3=1/C.  Since C<1, a_*>1.
    assert C<F(1)

    # The two only nontrivial even-coefficient sign checks.
    d2=A*A+2*B-3
    d4=B*B+2*A*C-3

    assert d2==F(2354604069,192959881)
    assert d4==F(1681740933,192959881)
    assert d2>0
    assert d4>0

    # At a_*^6=1/C^2 the y^6 coefficient cancels exactly.
    # The remaining y, y^3, y^5 coefficients are manifestly positive.
    assert A>0 and B>0 and C>0

    model_defect=W0
    model_simple=1-2*W0
    cushion=F(21,200)-W0

    assert model_simple==F(11061,13891)
    assert cushion==F(8711,2778200)
    assert model_simple>F(79,100)

    print("A^2+2B-3 =",d2,"~",float(d2))
    print("B^2+2AC-3 =",d4,"~",float(d4))
    print("model defect =",model_defect,"~",float(model_defect))
    print("model simple =",model_simple,"~",float(model_simple))
    print(">79 defect cushion =",cushion,"~",float(cushion))

def build_loewner(alpha,beta):
    d=len(alpha)
    H=np.diag(beta.astype(float)).astype(float)
    for i in range(d):
        for j in range(d):
            if i!=j:
                H[i,j]+=(alpha[i]-alpha[j])/(np.pi*(j-i))
    return H

def q_coeffs(a):
    Af=float(A); Bf=float(B); Cf=float(C)
    return np.array([
        (Af*a-Cf*a**3 +1j*(-1+Bf*a*a))/8,
        (-Af*a-3*Cf*a**3 +1j*(3+Bf*a*a))/8,
        (-Af*a-3*Cf*a**3 +1j*(-3-Bf*a*a))/8,
        (Af*a-Cf*a**3 +1j*(1-Bf*a*a))/8,
    ],dtype=complex)

def finite_matrix_gate():
    a=(float(F(13891,9660)))**(1/3)
    q=q_coeffs(a)

    # Scalar factor identity at deterministic sample points.
    for x in (-4.0,-1.3,0.0,0.7,2.2,7.0):
        u=(x+1j*a)/(x-1j*a)
        lhs=sum(q[k]*u**k for k in range(4))
        px=1-float(A)*x+float(B)*x*x-float(C)*x**3
        rhs=a**3*px/(x-1j*a)**3
        assert abs(lhs-rhs)<3e-13,(x,lhs,rhs)

    rng=np.random.default_rng(84627)
    for d in (23,41,67):
        H=build_loewner(rng.normal(size=d)/2,rng.normal(size=d)/3)
        I=np.eye(d,dtype=complex)
        D=np.diag(np.arange(d,dtype=float))

        U=(H+1j*a*I)@np.linalg.inv(H-1j*a*I)
        Q=sum(q[k]*np.linalg.matrix_power(U,k) for k in range(4))
        CQ=D@Q-Q@D

        assert np.linalg.norm(U.conj().T@U-I,2)<3e-11
        assert np.linalg.norm(Q.T-Q,'fro')<3e-10
        assert np.linalg.norm(CQ.T+CQ,'fro')<3e-9

        sv=np.linalg.svd(CQ,compute_uv=False)
        rank=int(np.sum(sv>1e-8*max(1.0,sv[0])))
        assert rank<=6,(d,rank,sv[:10])

        assert abs(sv[0]-sv[1])<3e-8
        assert abs(sv[2]-sv[3])<3e-8
        assert abs(sv[4]-sv[5])<3e-8

        # Positive-energy displacement identity.
        total=np.trace(Q.conj().T@Q).real/d
        diag=np.sum(np.abs(np.diag(Q))**2)/d
        off=sum(
            abs(CQ[i,j])**2/((i-j)**2)
            for i in range(d)
            for j in range(d)
            if i!=j
        )/d
        assert abs(total-diag-off)<3e-10

        print(
            "d",d,
            "rank[D,Q*]",rank,
            "paired singular values",sv[:6],
            "energy residual",abs(total-diag-off),
        )

    print("a_* =",a)
    print("q_* coefficients =",q)
    print("RESULT: WP84_EXACT_FRONTIER_RANK6_CHRISTOFFEL_CAYLEY_PASS")

def main():
    exact_gate()
    finite_matrix_gate()

if __name__=="__main__":
    main()
