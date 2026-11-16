#!/usr/bin/env python3
"""WP71 G9-A exact welding reindexing gate.

For arbitrary integer weights a_m and b_n, fixed b1,b2 and j-window,
define
    A(j)=sum_m a_m b_n,  n=(b2*m+j)/b1,
over integral n and the chosen supports.

Expanding sum_j A(j)^2 and setting
    g=gcd(b1,b2), r=b1/g, q=b2/g
gives the exact off-diagonal welding identity

    S1_off = sum_{k!=0} sum_n b_n b_{n-qk} w_k(n)

with
    w_k(n)=sum_m a_m a_{m-rk}
over the simultaneous range/j constraints.

This script checks the identity in pure integer arithmetic on several
deterministic finite families.  It is an algebraic indexing gate only; it
does not estimate the prime weights.
"""
from math import gcd

def direct(b1,b2,J,lo,hi,a,b):
    A={}
    for j in range(-J,J+1):
        if j==0:
            continue
        s=0
        for m in range(lo,hi+1):
            num=b2*m+j
            if num%b1:
                continue
            n=num//b1
            s+=a.get(m,0)*b.get(n,0)
        A[j]=s
    S1=sum(x*x for x in A.values())

    diag=0
    for j in range(-J,J+1):
        if j==0:
            continue
        for m in range(lo,hi+1):
            num=b2*m+j
            if num%b1:
                continue
            n=num//b1
            x=a.get(m,0)*b.get(n,0)
            diag+=x*x
    return S1,diag,A

def welded(b1,b2,J,lo,hi,a,b):
    g=gcd(b1,b2)
    r,q=b1//g,b2//g
    total=0
    rows=[]
    # Safe finite k range from simultaneous m,m-rk support.
    kmax=(hi-lo)//r+1
    nkeys=sorted(b)
    for k in range(-kmax,kmax+1):
        if k==0:
            continue
        part=0
        for n in nkeys:
            np=n-q*k
            if np not in b:
                continue
            wk=0
            for m in range(lo,hi+1):
                mp=m-r*k
                if not (lo<=mp<=hi):
                    continue
                j=b1*n-b2*m
                if j==0 or abs(j)>J:
                    continue
                # Same-j condition for the partner is automatic.
                jp=b1*np-b2*mp
                assert jp==j
                wk+=a.get(m,0)*a.get(mp,0)
            part+=b[n]*b[np]*wk
        rows.append((k,part))
        total+=part
    return total,rows

def run_case(b1,b2,J,lo,hi):
    # Deliberately non-prime arbitrary signed/positive integer weights:
    # the identity is combinatorial, not number-theoretic.
    a={m:(m*m+3*m+7)%17-4 for m in range(lo,hi+1)}
    # Broad n support so boundary effects are explicit rather than hidden.
    nlo=(b2*lo-J)//b1-3
    nhi=(b2*hi+J)//b1+3
    b={n:(5*n*n+2*n+11)%19-5 for n in range(nlo,nhi+1)}

    S1,diag,_=direct(b1,b2,J,lo,hi,a,b)
    off=S1-diag
    weld,rows=welded(b1,b2,J,lo,hi,a,b)
    assert off==weld,(b1,b2,J,lo,hi,off,weld)
    return {
      "b1":b1,"b2":b2,"J":J,"lo":lo,"hi":hi,
      "S1":S1,"diag":diag,"offdiag":off,"welded":weld,
      "nonzero_k":sum(1 for _,x in rows if x),
    }

def main():
    cases=[
      (5,3,7,2,18),
      (5,4,9,3,21),
      (6,4,8,2,19),
      (7,9,11,4,25),
      (8,12,10,3,20),
    ]
    for c in cases:
        out=run_case(*c)
        print(out)
    print("RESULT: WP71_G9_A_WELDING_REINDEXING_PASS")

if __name__=="__main__":
    main()
