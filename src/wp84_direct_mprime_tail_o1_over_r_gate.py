#!/usr/bin/env python3
"""Regression gate for the direct O(1/R) m'(z) tail bound."""
import numpy as np

def build(alpha,beta,R=None):
    d=len(alpha)
    H=np.diag(beta.astype(float)).astype(float)
    for i in range(d):
        for j in range(d):
            if i==j:
                continue
            if R is not None and abs(i-j)>R:
                continue
            H[i,j]+=(alpha[i]-alpha[j])/(np.pi*(j-i))
    return H

def main():
    rng=np.random.default_rng(8420)
    worst=0.0

    for d in (41,81,121):
        alpha=rng.normal(size=d)/2
        beta=rng.normal(size=d)/3
        H=build(alpha,beta,None)
        qalpha=np.dot(alpha,alpha)/d

        for bw in (2,5,11,19):
            HR=build(alpha,beta,bw)

            for eta in (0.8,1.0,1.26,1.6):
                z=.17+1j*eta

                G=np.linalg.inv(H-z*np.eye(d))
                S=np.linalg.inv(HR-z*np.eye(d))

                mpH=np.trace(G@G)/d
                mpR=np.trace(S@S)/d

                lhs=abs(mpH-mpR)

                bound=(
                    72*qalpha
                    /(np.pi**2*eta**4*bw)
                )

                ratio=lhs/bound
                worst=max(worst,ratio)

                assert lhs<=bound*(1+1e-9),(
                    d,bw,eta,lhs,bound
                )

    print("worst_ratio =",worst)
    print("RESULT: WP84_DIRECT_MPRIME_TAIL_O1_OVER_R_PASS")

if __name__=="__main__":
    main()
