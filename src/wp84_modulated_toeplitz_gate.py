#!/usr/bin/env python3
"""WP84 numerical gate for the modulated-Toeplitz factorisation."""
import cmath

N=17
INV2=pow(2,-1,N)

def main():
    omega=cmath.exp(2j*cmath.pi/N)
    phi=[7+3*min(u,N-u)+5*min(u,N-u)**2 for u in range(N)]
    phihat=[sum(phi[u]*omega**(k*u) for u in range(N)) for k in range(N)]

    def V(a,tau):
        return phihat[(tau-a)%N]

    def A(r,y):
        yh=(y*INV2)%N
        return N*sum(
            phi[(x-yh)%N]*phi[(x+yh)%N]*omega**(-r*x)
            for x in range(N)
        )

    worst=0.0
    checks=0
    for y in range(N):
        yh=(y*INV2)%N
        for a in range(N):
            for b in range(N):
                lhs=sum(V(a,tau)*V(b,tau)*omega**(tau*y) for tau in range(N))
                rhs=omega**(((a+b)*yh)%N)*A((a-b)%N,y)
                err=abs(lhs-rhs)
                worst=max(worst,err)
                checks+=1
    assert worst < 1e-7, worst
    print("checks",checks,"worst_abs_error",worst)
    print("RESULT: WP84_MODULATED_TOEPLITZ_GATE_PASS")

if __name__=="__main__":
    main()
