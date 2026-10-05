#!/usr/bin/env python3
"""Regression gate for the positive rank-four two-pole defect energy."""
import numpy as np

def main():
    rng=np.random.default_rng(8417)
    d=31
    X=rng.normal(size=(d,d))
    H0=(X+X.T)/2
    I=np.eye(d)

    b=9/4
    A=82/25

    R1=np.linalg.inv(H0-1j*I)
    Rb=np.linalg.inv(H0-1j*b*I)

    d1=328/125+1j
    db=-738/125+9j/4

    K=I+d1*R1+db*Rb

    Q=H0@H0-A*H0+b*I
    K2=Q@R1@Rb
    assert np.linalg.norm(K-K2)<2e-10

    evals=np.linalg.eigvalsh(H0)
    defect=((evals**2-A*evals+b)**2)/(
        (evals**2+1)*(evals**2+b*b)
    )

    direct=np.trace(K.conj().T@K).real/d
    scalar=np.mean(defect)
    assert abs(direct-scalar)<2e-11

    D=np.diag(np.arange(d,dtype=float))
    C=D@K-K@D

    diag=np.sum(np.abs(np.diag(K))**2)/d
    off=sum(
        abs(C[i,j])**2/((i-j)**2)
        for i in range(d)
        for j in range(d)
        if i!=j
    )/d

    assert abs(direct-diag-off)<2e-11

    sv=np.linalg.svd(C,compute_uv=False)
    rank=np.sum(sv>1e-10*max(1.0,sv[0]))
    assert rank<=4

    print("defect direct =",direct)
    print("diagonal energy =",diag)
    print("displacement energy =",off)
    print("rank [D,K] =",rank)
    print("RESULT: WP84_TWO_POLE_POSITIVE_ENERGY_PASS")

if __name__=="__main__":
    main()
