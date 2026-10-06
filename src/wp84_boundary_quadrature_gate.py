#!/usr/bin/env python3
"""Finite boundary-quadrature gate for WP84.

Checks the exact formulas numerically on representative finite matrices and
prints the analytic rank/error bound.

No theorem claim depends on floating-point output; the proof is in the note.
"""
import math
import numpy as np
from numpy.polynomial.legendre import leggauss

def concentration(d,L,W):
    k=np.arange(d)
    D=k[:,None]-k[None,:]
    out=np.empty((d,d),dtype=complex)
    out[D==0]=W/L
    nz=(D!=0)
    xi=2*np.pi*D[nz]/L
    out[nz]=2*np.sin(xi*W/2)/(L*xi)
    return out

def quadrature_matrix(d,L,W,p):
    z,w=leggauss(p)
    x=(W/2)*z
    wt=(W/2)*w
    k=np.arange(d)
    V=np.exp(1j*2*np.pi*np.outer(k,x)/L)
    return (V*wt[None,:])@V.conj().T/L

def analytic_bound(d,L,W,p):
    Z=np.pi*(d-1)*W/L
    # log-safe evaluation of (TW/pi) is replaced here by the exact finite prefactor
    log_ratio=2*p*math.log(Z)-math.lgamma(2*p+1) if Z>0 else -math.inf
    return (2*d*W/L)*math.exp(log_ratio), Z

def main():
    cases=[
        (32,100.0,4.0),
        (48,120.0,6.0),
        (64,160.0,8.0),
    ]
    for d,L,W in cases:
        Z=np.pi*(d-1)*W/L
        p=max(1,math.ceil(math.e*Z))
        Q=concentration(d,L,W)
        R=quadrature_matrix(d,L,W,p)
        err=np.linalg.norm(Q-R,2)
        bnd,_=analytic_bound(d,L,W,p)
        eig=np.linalg.eigvalsh(Q)
        tail=eig[-p-1] if p<d else 0.0
        print({
            "d":d,"L":L,"W":W,"Z":Z,"p":p,
            "p_over_d":p/d,
            "op_error":err,
            "analytic_entry_to_op_bound":bnd,
            "lambda_pplus1":tail,
        })
        # Once the analytic bound drops below binary64 roundoff, the direct
        # matrix comparison is roundoff-limited rather than theorem-limited.
        roundoff_floor=100*np.finfo(float).eps*d
        assert err <= max(bnd*(1+1e-8),roundoff_floor)
        if p<d:
            assert tail <= max(err,roundoff_floor)+1e-12

    print("RESULT: WP84_BOUNDARY_QUADRATURE_GATE_PASS")

if __name__=="__main__":
    main()
