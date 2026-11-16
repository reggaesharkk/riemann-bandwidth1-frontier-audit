#!/usr/bin/env python3
"""WP84 bounded beta-polynomial positive-index minorants.

Let
  t(x)=2x/(1+x^2) in [-1,1],
and
  p_m(t)= [int_0^t (1-s^2)^m ds] / [int_0^1 (1-s^2)^m ds].

Then p_m is odd, monotone on [-1,1], maps [-1,1] to [-1,1], and
  1_{x>0} >= p_m(t(x))
for every real x.

Against the current extremal four-node quadrature, evaluate each rational
minorant exactly by reduction modulo the Christoffel cubic.
"""
from fractions import Fraction as F
from math import comb

def trim(p):
    p=p[:]
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b)); c=[F(0)]*n
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return trim(c)

def sub(a,b):
    return add(a,[-v for v in b])

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return trim(c)

def divmod_poly(a,b):
    a=trim(a); b=trim(b)
    q=[F(0)]*max(1,len(a)-len(b)+1)
    while len(a)>=len(b) and not (len(a)==1 and a[0]==0):
        d=len(a)-len(b); z=a[-1]/b[-1]; q[d]+=z
        for j in range(len(b)):
            a[d+j]-=z*b[j]
        a=trim(a)
    return trim(q),trim(a)

def invmod(a,p):
    r0,r1=p[:],a[:]
    s0,s1=[F(0)],[F(1)]
    while not (len(r1)==1 and r1[0]==0):
        q,r2=divmod_poly(r0,r1)
        r0,r1=r1,r2
        s0,s1=s1,sub(s0,mul(q,s1))
    assert len(r0)==1 and r0[0]
    return divmod_poly([x/r0[0] for x in s0],p)[1]

P=[F(1),F(-43428,13891),F(37704,13891),F(-9660,13891)]
w0=F(1415,13891)
mom=[F(1),F(1),F(4,3)]
christoffel_simple=F(11061,13891)

def beta_den(m):
    return sum(F((-1)**j*comb(m,j),2*j+1) for j in range(m+1))

def rational_num_den(m):
    # common denominator (1+x^2)^(2m+1)
    D=beta_den(m)
    base=[F(1),F(0),F(1)]
    den=[F(1)]
    for _ in range(2*m+1):
        den=mul(den,base)

    xpoly=[F(0),F(1)]
    num=[F(0)]
    for j in range(m+1):
        power=2*j+1
        xp=[F(1)]
        for _ in range(power):
            xp=mul(xp,xpoly)
        rest=[F(1)]
        for _ in range(2*m+1-power):
            rest=mul(rest,base)
        coeff=F((-1)**j*comb(m,j)*(2**power),2*j+1)/D
        num=add(num,[coeff*v for v in mul(xp,rest)])
    return num,den,D

def evaluate(m):
    num,den,D=rational_num_den(m)
    inv=invmod(den,P)
    rem=divmod_poly(mul(num,inv),P)[1]+[F(0)]*3
    # q_m(0)=0, so subtract the artificial zero-atom contribution rem(0).
    E=sum(rem[i]*mom[i] for i in range(3))-w0*rem[0]
    return E,2*E-1,D

def main():
    prev=None
    for m in range(0,11):
        E,S,D=evaluate(m)
        if prev is not None:
            assert S>prev
        prev=S
        assert -1<E<1
        assert S<christoffel_simple
        print(f"m={m:2d} pole_order={2*m+1:2d} q={float(E):.15f} simple={float(S):.15f}")

    E10,S10,D10=evaluate(10)
    assert S10>F(79,100)
    print("m10 exact q =",E10)
    print("m10 exact simple =",S10)
    print("q margin over 0.895 =",E10-F(895,1000))
    print("gap to Christoffel =",christoffel_simple-S10)
    print("RESULT: WP84_BOUNDED_BETA_MINORANT_PASS")

if __name__=="__main__":
    main()
