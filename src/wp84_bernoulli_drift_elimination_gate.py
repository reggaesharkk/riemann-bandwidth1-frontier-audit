#!/usr/bin/env python3
"""Regression gate for the Bernoulli drift-elimination identity.

The finite one-coordinate identity is second-order accurate; halving G should
reduce its defect cubically.
"""
import numpy as np

def check(scale,d=13,t=.37):
    rng=np.random.default_rng(8413)
    X=rng.normal(size=(d,d))
    H=(X+X.T)/2
    Y=rng.normal(size=(d,d))
    G=scale*(Y+Y.T)/2
    z=.21+1.6j

    Rm=np.linalg.inv(H-z*np.eye(d))
    Rp=np.linalg.inv(H+G-z*np.eye(d))

    Fm=np.trace(Rm@G@Rm)/d
    Fp=np.trace(Rp@G@Rp)/d

    Bm=np.trace(Rm@G@Rm@G@Rm)/d
    Bp=np.trace(Rp@G@Rp@G@Rp)/d

    A=(1-t)*Fm+t*Fp
    B=(1-t)*Bm+t*Bp
    C=t*Fp

    defect=C-(t*A-2*t*(1-t)*B)
    return abs(defect)

def main():
    e1=check(1/80)
    e2=check(1/160)
    e3=check(1/320)

    assert e2 < .2*e1 + 1e-15,(e1,e2)
    assert e3 < .2*e2 + 1e-15,(e2,e3)

    print("defects",e1,e2,e3)
    print("ratios",e2/e1,e3/e2)
    print("RESULT: WP84_BERNOULLI_DRIFT_ELIMINATION_PASS")

if __name__=="__main__":
    main()
