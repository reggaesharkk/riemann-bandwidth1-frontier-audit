#!/usr/bin/env python3
"""Regression gate for the co-moving Gaussian heat-flow identity.

This is a finite-dimensional numerical regression only.
"""
import numpy as np

def r2(x,a=1.5):
    return 1.0-((x-a)**2/(x*x+a*a))**2

def trace_f(H,a=1.5):
    ev=np.linalg.eigvalsh(H)
    return np.mean(r2(ev,a))

def main():
    rng=np.random.default_rng(8413)
    d=5

    Y=rng.normal(size=(d,d))
    P=(Y+Y.T)/2/3
    dirs=[]
    for _ in range(4):
        A=rng.normal(size=(d,d))
        dirs.append((A+A.T)/2/5)

    s0=1.0

    # Common random samples make the two representations directly comparable.
    gs=rng.normal(size=(4000,len(dirs)))

    for t in (0.17,0.39,0.71):
        u=(1-t)/t
        vals_bridge=[]
        vals_heat=[]

        for row in gs:
            W=sum(g*E for g,E in zip(row,dirs))
            Ht=s0*np.eye(d)+t*P+np.sqrt(t*(1-t))*W

            # transported test: f_t(Ht)
            Yt=s0*np.eye(d)+(Ht-s0*np.eye(d))/t
            vals_bridge.append(trace_f(Yt))

            # additive heat-flow representation
            Hu=s0*np.eye(d)+P+np.sqrt(u)*W
            vals_heat.append(trace_f(Hu))

        lhs=float(np.mean(vals_bridge))
        rhs=float(np.mean(vals_heat))
        err=abs(lhs-rhs)
        assert err<2e-13,(t,lhs,rhs,err)
        print("t",t,"u",u,"representation_error",err)

    # Partial-fraction identity at the endpoint.
    H1=s0*np.eye(d)+P
    a=1.5
    z=1j*a
    R=np.linalg.inv(H1-z*np.eye(d))
    m=np.trace(R)/d
    mp=np.trace(R@R)/d
    pf=2*np.real(a*(2+1j)*m-a*a*mp)
    direct=trace_f(H1,a)
    assert abs(pf-direct)<2e-12,(pf,direct)

    print("partial_fraction_error",abs(pf-direct))
    print("RESULT: WP84_R2_COMOVING_HEAT_FLOW_PASS")

if __name__=="__main__":
    main()
