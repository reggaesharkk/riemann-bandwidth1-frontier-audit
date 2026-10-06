#!/usr/bin/env python3
"""Regression gate for the fixed-displacement Loewner tail identity.

This is a finite numerical check of the exact Hilbert--Schmidt formula and
the Hoffman--Wielandt/Lipschitz transfer used in the companion note.
"""
import numpy as np

def r2(x):
    return 1.0-((x-1.0)**2/(x*x+1.0))**2

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
    rng=np.random.default_rng(8413)

    for d in (41,83,127):
        alpha=rng.normal(size=d)/2
        beta=rng.normal(size=d)/3
        H=build(alpha,beta,None)

        for R in (2,5,11):
            HR=build(alpha,beta,R)
            D=H-HR

            lhs=np.linalg.norm(D,'fro')**2/d

            rhs=0.0
            for i in range(d):
                for j in range(d):
                    if i!=j and abs(i-j)>R:
                        rhs += (
                            (alpha[i]-alpha[j])**2
                            /(np.pi**2*(i-j)**2)
                        )
            rhs/=d
            assert abs(lhs-rhs)<1e-12,(d,R,lhs,rhs)

            crude=(
                8.0/(np.pi**2*R)
                *np.dot(alpha,alpha)/d
            )
            assert lhs<=crude*(1+1e-12),(d,R,lhs,crude)

            ev=np.linalg.eigvalsh(H)
            evr=np.linalg.eigvalsh(HR)
            stat=abs(np.mean(r2(ev))-np.mean(r2(evr)))

            # Use the fully elementary safe global bound Lip(r2)<=8.
            hw=8.0*np.sqrt(lhs)
            assert stat<=hw*(1+1e-10),(d,R,stat,hw)

            print(
                "d",d,"R",R,
                "HS2",lhs,
                "crude",crude,
                "r2_diff",stat,
                "HW_bound",hw
            )

    print("RESULT: WP84_R2_DISPLACEMENT_TAIL_GATE_PASS")

if __name__=="__main__":
    main()
