#!/usr/bin/env python3
"""WP71 G9-C j-first four-point identity.

For fixed b1,b2 and finite m/n windows define

  A(j) = sum_m a[m] b[n],
  n = (b2*m+j)/b1,

with the divisibility/window conditions.

Writing g=gcd(b1,b2), r=b1/g, q=b2/g, define for fixed (k,j)

  N4(k,j) =
    sum_m a[m] a[m-rk] b[n] b[n-qk],

with every shifted variable required to lie in its original window.

Then, exactly and pointwise in j,

  A(j)^2 = sum_k N4(k,j).

This is the analytically useful ordering: j and k are kept outside and the
remaining m-sum is long.  It is equivalent to the n-first welding identity
but does not create O(1)-length moving m-windows.

Pure integer arithmetic, arbitrary deterministic weights.
"""
from math import gcd

def A_of_j(b1,b2,j,a,b):
    s=0
    for m,am in a.items():
        z=b2*m+j
        if z%b1:
            continue
        n=z//b1
        if n in b:
            s+=am*b[n]
    return s

def N4_of_kj(b1,b2,k,j,a,b):
    g=gcd(b1,b2); r=b1//g; q=b2//g
    s=0
    for m,am in a.items():
        mp=m-r*k
        if mp not in a:
            continue
        z=b2*m+j
        if z%b1:
            continue
        n=z//b1
        np=n-q*k
        if n in b and np in b:
            # same-lock invariance
            assert b1*np-b2*mp == j
            s+=am*a[mp]*b[n]*b[np]
    return s

def check_case(b1,b2,mlo,mhi,nlo,nhi):
    a={m:((11*m*m+7*m+5)%31)-9 for m in range(mlo,mhi+1)}
    b={n:((5*n*n+13*n+3)%37)-10 for n in range(nlo,nhi+1)}
    g=gcd(b1,b2); r=b1//g
    kmax=(mhi-mlo)//r+2
    # Large enough j-range to include every lock formed by the windows.
    jmin=b1*nlo-b2*mhi
    jmax=b1*nhi-b2*mlo
    tested=0
    for j in range(jmin,jmax+1):
        A=A_of_j(b1,b2,j,a,b)
        rhs=sum(N4_of_kj(b1,b2,k,j,a,b)
                for k in range(-kmax,kmax+1))
        assert A*A==rhs,(b1,b2,j,A*A,rhs)
        tested+=1
    return tested

def main():
    cases=[
      (5,3,2,17,3,22),
      (6,4,1,18,2,20),
      (7,9,3,19,1,24),
      (8,12,2,20,4,25),
      (11,6,5,27,2,31),
    ]
    total=0
    for c in cases:
        n=check_case(*c)
        total+=n
        print("case",c,"j-values",n,"PASS")
    print("total j-values =",total)
    print("RESULT: WP71_G9_C_JFIRST_IDENTITY_PASS")

if __name__=="__main__":
    main()
