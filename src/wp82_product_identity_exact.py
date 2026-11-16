#!/usr/bin/env python3
"""WP82 exact finite product-identity gate.

For finite integer-valued sequences f_i,g_i on Z, define a lock vector
j=(j_2,...,j_b) relative to slot 1 by

  N_f(j) = sum_x f_1(x) prod_{i=2}^b f_i(x+j_i).

Then

  sum_j N_f(j) N_g(j)
    = sum_t prod_i C_i(t),

where

  C_i(t)=sum_x f_i(x) g_i(x+t).

This is the exact finite identity consumed by the higher-cycle spectral
frame.  The proof is the bijection y_i-x_i=t forced by equality of all
relative locks.

The checker uses exact Python integers and unrelated deterministic
sequences for b=2,...,6.
"""
from itertools import product

def corr(f,g,t):
    return sum(v*g.get(x+t,0) for x,v in f.items())

def N(seq,locks):
    f0=seq[0]
    total=0
    for x,v in f0.items():
        z=v
        for i,j in enumerate(locks,1):
            z*=seq[i].get(x+j,0)
            if z==0:
                break
        total+=z
    return total

def check(b):
    # Different exact integer weights/supports in every slot.
    F=[]; G=[]
    for i in range(b):
        F.append({x:((x+2*i+3)**2+5*i+7)%11-4 for x in range(-3,5)})
        G.append({x:((3*x-i+8)**2+2*i+5)%13-5 for x in range(-4,4)})

    # All nonzero relative locks lie inside the support-difference range.
    lock_range=range(-8,9)
    lhs=0
    for locks in product(lock_range, repeat=b-1):
        lhs+=N(F,locks)*N(G,locks)

    t_range=range(-9,10)
    rhs=0
    for t in t_range:
        z=1
        for i in range(b):
            z*=corr(F[i],G[i],t)
        rhs+=z

    assert lhs==rhs,(b,lhs,rhs)
    return lhs

def main():
    for b in range(2,7):
        val=check(b)
        print("b",b,"exact total",val,"PASS")
    print("RESULT: WP82_PRODUCT_IDENTITY_EXACT_PASS")

if __name__=="__main__":
    main()
