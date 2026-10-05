#!/usr/bin/env python3
"""Regression gate for cubic Bernoulli-vs-Gaussian Lindeberg scaling."""
import numpy as np

def one_compare(scale,t=.41,d=11,nsamp=200000,seed=8414):
    rng=np.random.default_rng(seed)
    X=rng.normal(size=(d,d))
    H=(X+X.T)/2
    Y=rng.normal(size=(d,d))
    G=scale*(Y+Y.T)/2
    z=.17+1.7j

    # Bernoulli centered variable.
    vals=[]
    for xi,p in ((1-t,t),(-t,1-t)):
        R=np.linalg.inv(H+xi*G-z*np.eye(d))
        vals.append(p*np.trace(R)/d)
    eb=sum(vals)

    # Deterministic Gauss-Hermite quadrature instead of Monte Carlo.
    nodes,weights=np.polynomial.hermite.hermgauss(40)
    sig=np.sqrt(t*(1-t))
    eg=0j
    for node,w in zip(nodes,weights):
        g=np.sqrt(2)*node
        R=np.linalg.inv(H+sig*g*G-z*np.eye(d))
        eg += (w/np.sqrt(np.pi))*np.trace(R)/d

    return abs(eb-eg)

def main():
    e1=one_compare(1/50)
    e2=one_compare(1/100)
    e3=one_compare(1/200)

    assert e2 < .2*e1 + 1e-15,(e1,e2)
    assert e3 < .2*e2 + 1e-15,(e2,e3)

    print("errors",e1,e2,e3)
    print("ratios",e2/e1,e3/e2)
    print("RESULT: WP84_BERNOULLI_GAUSSIAN_CUBIC_PASS")

if __name__=="__main__":
    main()
