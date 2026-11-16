#!/usr/bin/env python3
"""WP83 exact finite Fourier-energy identity over a prime field.

This is a finite algebraic analogue of the full-lattice two-dimensional
Parseval identity used in the Proposition-R reconstruction.

For N | (p-1), omega an Nth root of unity, let

  H[t,s] = phi[t] phi[s] F[t+s mod N]

and its unnormalised 2D DFT

  C[k,l] = sum_{t,s} H[t,s] omega^(-k t-l s).

Then exactly in F_p,

  sum_{k,l} C[k,l] C[-k,-l]
    = N^2 sum_{t,s} H[t,s]^2
    = N^2 sum_u g[u] F[u]^2,

where
  g[u] = sum_t phi[t]^2 phi[u-t]^2.

The continuous Gabor identity has the same normalization:
sum_{k,l in Z}|Q_kl|^2 = L^2 int g(u)|F(u)|^2 du.
"""
P=97
N=8

def inv(a): return pow(a,P-2,P)

# primitive root 5 mod 97; omega has order 8
OMEGA=pow(5,(P-1)//N,P)
assert pow(OMEGA,N,P)==1
assert all(pow(OMEGA,d,P)!=1 for d in (1,2,4))

def w(e):
    return pow(OMEGA,e%N,P)

def main():
    phi=[(3*t*t+5*t+7)%P for t in range(N)]
    F=[(11*u*u+2*u+13)%P for u in range(N)]
    H=[[phi[t]*phi[s]*F[(t+s)%N]%P for s in range(N)] for t in range(N)]

    C=[[sum(H[t][s]*w(-(k*t+l*s))
              for t in range(N) for s in range(N))%P
        for l in range(N)] for k in range(N)]

    lhs=sum(C[k][l]*C[(-k)%N][(-l)%N]
            for k in range(N) for l in range(N))%P

    e2=sum(H[t][s]*H[t][s]
           for t in range(N) for s in range(N))%P
    rhs1=(N*N*e2)%P

    g=[]
    for u in range(N):
        gu=sum(phi[t]*phi[t]*phi[(u-t)%N]*phi[(u-t)%N]
               for t in range(N))%P
        g.append(gu)
    e1=sum(g[u]*F[u]*F[u] for u in range(N))%P
    rhs2=(N*N*e1)%P

    assert lhs==rhs1==rhs2,(lhs,rhs1,rhs2)
    print("p",P,"N",N,"omega",OMEGA)
    print("lhs",lhs,"rhs_time",rhs1,"rhs_convolution",rhs2)
    print("RESULT: WP83_FULL_LATTICE_ENERGY_IDENTITY_PASS")

if __name__=="__main__":
    main()
