#!/usr/bin/env python3
"""Regression gate for the exact detuning/Dirichlet commutator identity."""
import numpy as np

def main():
    rng=np.random.default_rng(8471)

    for n in (7,19,43):
        for d in (11,32,71):
            s=rng.random(n)
            T=137.0
            L=23.0

            z=np.exp(2j*np.pi*s)
            v=np.exp(1j*T*L*s)

            powers=np.arange(d)
            F=np.exp(2j*np.pi*np.outer(s,powers))/np.sqrt(d)
            D=F@F.conj().T
            K=(v[:,None]*D)*v.conj()[None,:]

            Z=np.diag(z)
            comm=Z@K-K@Z

            a=v*z**d
            b=v*z**(d-1)
            w=v*np.conj(z)

            rhs=(np.outer(a,b.conj())-np.outer(v,w.conj()))/d

            err=np.linalg.norm(comm-rhs,np.inf)
            assert err<2e-10,(n,d,err)

            rank=np.linalg.matrix_rank(comm,tol=1e-9)
            assert rank<=2,(n,d,rank)

            # Exact Hadamard reconstruction for an arbitrary real symmetric
            # residual vanishing on the diagonal.
            X=rng.normal(size=(n,n))
            E=(X+X.T)/2
            np.fill_diagonal(E,0.0)

            H=np.zeros((n,n),dtype=complex)
            for i in range(n):
                for j in range(n):
                    if i!=j:
                        H[i,j]=E[i,j]/(z[i]-z[j])

            lhs=E*K
            rhs2=H*comm
            err2=np.linalg.norm(lhs-rhs2,np.inf)
            assert err2<2e-10,(n,d,err2)

    print("RESULT: WP84_DETUNING_COMMUTATOR_ENDPOINT_PASS")

if __name__=="__main__":
    main()
