#!/usr/bin/env python3
"""Finite-height face for the logarithmic prime-power measure used in WP71."""
import math
import numpy as np

def von_mangoldt_weights(N):
    lam=np.zeros(N+1,dtype=float)
    # prime sieve
    isprime=np.ones(N+1,dtype=bool); isprime[:2]=False
    for p in range(2,int(N**0.5)+1):
        if isprime[p]: isprime[p*p::p]=False
    primes=np.nonzero(isprime)[0]
    for p in primes:
        lp=math.log(int(p)); q=int(p)
        while q<=N:
            lam[q]=lp
            if q>N//int(p): break
            q*=int(p)
    return lam

def discrepancy(l):
    N=int(math.exp(l))
    lam=von_mangoldt_weights(N)
    n=np.arange(1,N+1)
    w=lam[1:]/n
    c=np.cumsum(w)/l
    u=np.log(n)/l
    # right- and left-limit CDF errors at every atom
    before=np.r_[0.0,c[:-1]]
    err=max(float(np.max(np.abs(c-u))),float(np.max(np.abs(before-u))))
    small_prime_mass=sum(math.log(p)/(p-1) for p in (2,3,5,7) if p<=N)/l
    diag=float(np.sum(w*w)/(l*l))
    return N,err,small_prime_mass,diag,c[-1]

def main():
    print("l,N,sup_CDF_discrepancy,small_prime_2357_mass,diagonal_pair_mass,total_mass")
    vals=[]
    for l in (5.0,6.0,7.0,8.0,9.0,10.0,11.0):
        N,e,s,d,m=discrepancy(l)
        vals.append((l,e))
        print(f"{l:.1f},{N},{e:.9f},{s:.9f},{d:.9e},{m:.9f}")
    scaled=[l*e for l,e in vals]
    print("l_times_discrepancy =",",".join(f"{x:.6f}" for x in scaled))
    print("RESULT: LOG_PRIME_MEASURE_FACE_COMPLETE")

if __name__=="__main__":
    main()
