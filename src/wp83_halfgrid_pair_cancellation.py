#!/usr/bin/env python3
"""WP83 numerical falsifier: half-grid cancellation of deep off-line pair blocks.

Uses an admissible C3 monotone smoothstep taper
    rho(t)=35t^4-84t^5+70t^6-20t^7, 0<=t<=1,
with w=1 and phi_L(u)=rho((L/2-|u|)/w).

For a fixed off-line depth delta, build the sampled evaluation vector
    u_gamma(k)=phi_hat(gamma+i*delta-tau_k)
on a large local portion of the critical Gabor grid tau_k=2*pi*k/L.

The real pair matrix is
    H(u)=u u^T + conj(u) conj(u)^T = 2 Re(u u^T).

Compare gamma=0 with gamma=pi/L, half one Gabor spacing.  The expected
asymptotic is H_{pi/L} ~ -H_0 for fixed delta>0.

This is a numerical falsifier/corroboration, not a theorem proof.
"""
import math
import numpy as np

def rho(t):
    t=np.clip(t,0.0,1.0)
    return 35*t**4-84*t**5+70*t**6-20*t**7

def phihat_vec(L,delta,gamma,K=120,Nu=8001,w=1.0):
    u=np.linspace(-L/2,L/2,Nu)
    phi=rho((L/2-np.abs(u))/w)
    h=2*math.pi/L
    tau=np.arange(-K,K+1)*h
    z=gamma+1j*delta
    out=[]
    for i in range(0,len(tau),64):
        x=(z-tau[i:i+64])[:,None]
        vals=np.trapezoid(phi[None,:]*np.exp(1j*x*u[None,:]),u,axis=1)
        out.append(vals)
    return np.concatenate(out)

def frob_data(u,v):
    # <H(u),H(v)>_F = 2 Re[(u^T v)^2 + (u^T conj(v))^2].
    uv=2*np.real(np.dot(u,v)**2 + np.dot(u,np.conj(v))**2)
    uu=2*np.real(np.dot(u,u)**2 + np.dot(u,np.conj(u))**2)
    vv=2*np.real(np.dot(v,v)**2 + np.dot(v,np.conj(v))**2)
    corr=uv/math.sqrt(uu*vv)
    relsum=math.sqrt(max(0.0,(uu+vv+2*uv)/uu))
    return corr,relsum

def main():
    delta=0.2
    rows=[]
    for L in (20,40,80,120,160):
        u0=phihat_vec(L,delta,0.0)
        u1=phihat_vec(L,delta,math.pi/L)
        corr,relsum=frob_data(u0,u1)
        phase_rel=np.linalg.norm(u1+1j*u0)/np.linalg.norm(u0)
        rows.append((L,corr,relsum,phase_rel))
        print(f"L={L:3d} pair_corr={corr: .12f} "
              f"||H0+H1||/||H0||={relsum:.12f} "
              f"||u1+i*u0||/||u0||={phase_rel:.12f}")

    assert rows[-1][1] < -0.98
    assert rows[-1][2] < 0.20
    assert rows[-1][3] < 0.10
    print("RESULT: WP83_HALFGRID_PAIR_CANCELLATION_FALSIFIER_PASS")

if __name__=="__main__":
    main()
