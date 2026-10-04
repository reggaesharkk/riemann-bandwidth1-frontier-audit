#!/usr/bin/env python3
"""WP84 exact finite analogue of the modulated-Toeplitz prime block.

On Z/NZ with N odd, define the unnormalised DFT
    phihat(k)=sum_u phi(u) omega^(k u)
and shifted columns
    V_a(tau)=phihat(tau-a).

For even phi and y in Z/NZ,

    C_y(a,b)=sum_tau V_a(tau)V_b(tau) omega^(tau y)

factors exactly as

    C_y(a,b)
      = omega^(((a+b)y)/2) * A_{a-b}(y),

where

    A_r(y)
      = N sum_x phi(x-y/2)phi(x+y/2)omega^(-r x).

This is the finite cyclic analogue of the continuous
D_y * Toeplitz(A_y) * D_y factorisation.
"""
P=257
N=17
G=3
OMEGA=pow(G,(P-1)//N,P)
INV2=pow(2,-1,N)

assert pow(OMEGA,N,P)==1
assert all(pow(OMEGA,d,P)!=1 for d in range(1,N))

def w(e):
    return pow(OMEGA,e%N,P)

def main():
    # symmetric phi on Z/NZ
    phi=[]
    for u in range(N):
        d=min(u,N-u)
        phi.append((7+3*d+5*d*d)%P)
    assert all(phi[u]==phi[(-u)%N] for u in range(N))

    phihat=[sum(phi[u]*w(k*u) for u in range(N))%P for k in range(N)]

    def V(a,tau):
        return phihat[(tau-a)%N]

    def A(r,y):
        yh=(y*INV2)%N
        return (N*sum(
            phi[(x-yh)%N]*phi[(x+yh)%N]*w(-r*x)
            for x in range(N)
        ))%P

    checks=0
    for y in range(N):
      yh=(y*INV2)%N
      for a in range(N):
        for b in range(N):
          lhs=sum(V(a,tau)*V(b,tau)*w(tau*y) for tau in range(N))%P
          rhs=w((a+b)*yh)*A((a-b)%N,y)%P
          assert lhs==rhs,(a,b,y,lhs,rhs)
          checks+=1

    print("P",P,"N",N,"omega",OMEGA,"checks",checks)
    print("RESULT: WP84_MODULATED_TOEPLITZ_GATE_PASS")

if __name__=="__main__":
    main()
