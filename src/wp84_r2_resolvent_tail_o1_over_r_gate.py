#!/usr/bin/env python3
"""Numerical regression for the O(1/R) one-point displacement-tail mechanism."""
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
    rng=np.random.default_rng(8415)
    for d in (81,121):
        alpha=rng.normal(size=d)/2
        beta=rng.normal(size=d)/2
        H=build(alpha,beta,None)
        q=np.dot(alpha,alpha)/d

        for bw in (3,7,15,25):
            HR=build(alpha,beta,bw)
            Delta=H-HR
            tail=np.linalg.norm(Delta,'fro')**2/d
            assert tail <= 8*q/(np.pi**2*bw)*(1+1e-12)

            for eta in (0.8,1.0,1.4):
                z=.17+1j*eta
                G=np.linalg.inv(H-z*np.eye(d))
                S=np.linalg.inv(HR-z*np.eye(d))

                lhs=abs(np.trace(G-S)/d)
                bound=24*q/(np.pi**2*eta**3*bw)
                assert lhs <= bound*(1+1e-10),(d,bw,eta,lhs,bound)

            print("d",d,"R",bw,"tailHS2",tail)

    print("RESULT: WP84_R2_RESOLVENT_TAIL_O1_OVER_R_PASS")

if __name__=="__main__":
    main()
