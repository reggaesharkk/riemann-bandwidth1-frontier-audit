#!/usr/bin/env python3
"""Exact gate for the minimal-radius exact-frontier semicircle.

The support proof uses Fraction arithmetic plus rational bounds for r_*.
Floating calculations at c=4/5 are diagnostics only.
"""

from fractions import Fraction as F
import cmath
import math

A=F(43428,13891)
B=F(37704,13891)
C=F(9660,13891)
W0=F(1415,13891)

def exact_support_gate():
    # r_*^3 = 1/C.
    r3=F(13891,9660)

    # Prove 1 < r_* < 6/5 and r_*^2 > 5/4 using rational powers.
    assert r3 > 1
    assert r3 < F(6,5)**3
    assert r3**2 > F(5,4)**3

    # At c=r_* every coefficient is minimal on 0<=c<=r_*.
    # These strict rational inequalities imply positivity there.
    checks=[
        A-F(3),
        (A*A+2*B)*F(5,4)-F(15),
        A*B/C-F(9),
        (2*A*C+B*B)*F(25,16)-F(15),
        B/C-F(18,5),
    ]
    assert all(x>0 for x in checks),checks

    assert 1-2*W0 == F(11061,13891)

    print("support rational margins:")
    for j,x in enumerate(checks,1):
        print(j,x,"~",float(x))
    print("model defect =",W0,"~",float(W0))
    print("model simple =",1-2*W0,"~",float(1-2*W0))

def conv(p,q):
    out=[0j]*(len(p)+len(q)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(q):
            out[i+j]+=x*y
    return out

def poly_pow(p,n):
    out=[1+0j]
    for _ in range(n):
        out=conv(out,p)
    return out

def q_coeffs(c,a,r3):
    # q(u)= i r^3/(8 a^3) (u-1)^3
    #       P(((-c+ia)+(c+ia)u)/(u-1)).
    d=[-1+0j,1+0j]
    xn=[-c+1j*a,c+1j*a]

    d3=poly_pow(d,3)
    xnd2=conv(xn,poly_pow(d,2))
    xn2d=conv(poly_pow(xn,2),d)
    xn3=poly_pow(xn,3)

    out=[
        d3[k]
        -float(A)*xnd2[k]
        +float(B)*xn2d[k]
        -float(C)*xn3[k]
        for k in range(4)
    ]
    fac=1j*r3/(8*a**3)
    return [fac*x for x in out]

def heat_coeffs(q,a):
    c1=q[1]*q[0].conjugate()+q[2]*q[1].conjugate()+q[3]*q[2].conjugate()
    c2=q[2]*q[0].conjugate()+q[3]*q[1].conjugate()
    c3=q[3]*q[0].conjugate()

    Ah=2j*a*(c1+2*c2+3*c3)
    Bh=(2j*a)**2*(c2+3*c3)
    Ch=(2j*a)**3*c3/2
    return Ah,Bh,Ch

def diagnostic_point():
    r3=float(F(13891,9660))
    r=r3**(1/3)
    c=0.8
    a=math.sqrt(r*r-c*c)

    q=q_coeffs(c,a,r3)
    Ah,Bh,Ch=heat_coeffs(q,a)

    # q(1)=-r^3 C=-1 exactly at the algebraic level.
    q1=sum(q)
    assert abs(q1+1)<2e-12

    raw=abs(Ah)+abs(Bh)+abs(Ch)
    weighted=abs(Ah)/a+abs(Bh)/a**2+2*abs(Ch)/a**3

    print("r_* =",r)
    print("c0 =",c)
    print("a0 =",a)
    print("q(1) =",q1)
    print("A0 =",Ah)
    print("B0 =",Bh)
    print("C0 =",Ch)
    print("raw coefficient proxy =",raw)
    print("eta-weighted proxy =",weighted)

    assert abs(a-0.796243923908096)<2e-15
    assert raw < 2.815
    assert weighted < 4.367

def main():
    exact_support_gate()
    diagnostic_point()
    print("RESULT: WP84_MINIMAL_RADIUS_EXACT_FRONTIER_FAMILY_PASS")

if __name__=="__main__":
    main()
