#!/usr/bin/env python3
"""WP71 G9-B ordinary/triangular mean algebra for S(rk)S(qk).

For odd p, tau0 and tau1 are the ordinary twin local factors when p does
not / does divide the shift.  Since gcd(r,q)=1, the local normalized jump
when p|k is:

  generic p∤rq: Rg=((p-1)/(p-2))^2, ag=Rg-1=(2p-3)/(p-2)^2
  special p|rq: Rs=(p-1)/(p-2),     aS=Rs-1=1/(p-2)

Thus 0 <= aS <= ag and ag=O(1/p).  The divisor-expansion coefficients are
squarefree products of a_p, and both
  prod_p (1+a_p/p^(1/2))
and
  prod_p (1+a_p/p^(1/2))
control the elementary mean/tail errors uniformly.

At p=2 the product S(rk)S(qk) is exactly zero for odd k and has local
factor 4 for even k, regardless of the coprime pair (r,q).

The exact Euler mean is supplied by wp71_g9_b_local_factor.py.
"""
from fractions import Fraction as F

def tau0(p):
    p=F(p)
    return 1-F(1,(p-1)**2)

def tau1(p):
    p=F(p)
    return p/(p-1)

def jumps(p):
    if p==2:
        raise ValueError
    rs=tau1(p)/tau0(p)
    rg=rs*rs
    aS=rs-1
    ag=rg-1
    assert aS==F(1,p-2)
    assert ag==F(2*p-3,(p-2)**2)
    assert 0<=aS<=ag
    return rs,rg,aS,ag

def main():
    for p in (3,5,7,11,13,17,19,23,29,31,101,1009):
        rs,rg,aS,ag=jumps(p)
        print(p,"special_jump",aS,"generic_jump",ag)
        # Convenient explicit O(1/p) bound for p>=5.
        if p>=5:
            assert ag <= F(4,p)
    print("p=2 local rule: 4 if 2|k, 0 otherwise")
    print("RESULT: WP71_G9_B_TWIN_PRODUCT_MEAN_ALGEBRA_PASS")

if __name__=="__main__":
    main()
