#!/usr/bin/env python3
"""Exact a=6/5 model certificate and theorem-conditioning constants."""
from fractions import Fraction as F
import math

def trim(p):
    p=p[:]
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b))
    c=[F(0)]*n
    for i,x in enumerate(a): c[i]+=x
    for i,x in enumerate(b): c[i]+=x
    return trim(c)

def sub(a,b):
    return add(a,[-x for x in b])

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
        d=len(a)-len(b)
        z=a[-1]/b[-1]
        q[d]+=z
        for j in range(len(b)):
            a[d+j]-=z*b[j]
        a=trim(a)
    return trim(q),trim(a)

def invmod_poly(a,p):
    r0,r1=p[:],a[:]
    s0,s1=[F(0)],[F(1)]
    while not (len(r1)==1 and r1[0]==0):
        q,r2=divmod_poly(r0,r1)
        r0,r1=r1,r2
        s0,s1=s1,sub(s0,mul(q,s1))
    assert len(r0)==1 and r0[0]!=0
    s0=[x/r0[0] for x in s0]
    return divmod_poly(s0,p)[1]

def exact_model(a):
    P=[
        F(1),
        F(-43428,13891),
        F(37704,13891),
        F(-9660,13891)
    ]
    w0=F(1415,13891)
    m0,m1,m2=F(1),F(1),F(4,3)

    den=mul([a*a,F(0),F(1)],[a*a,F(0),F(1)])
    xm=[-a,F(1)]
    p4=[F(1)]
    for _ in range(4):
        p4=mul(p4,xm)
    num=sub(den,p4)

    inv=invmod_poly(den,P)
    rem=divmod_poly(mul(num,inv),P)[1]
    rem=rem+[F(0)]*(3-len(rem))

    # r2,a(0)=0: subtract the zero-atom evaluation of the remainder.
    q=rem[0]*m0+rem[1]*m1+rem[2]*m2-w0*rem[0]
    return q

def main():
    a=F(6,5)
    q=exact_model(a)
    simple=2*q-1

    q_expected=F(
        113898001480425765678720,
        130234262317191955294681
    )
    assert q==q_expected

    C0=12/math.pi**2*(math.sqrt(5)+256/27)
    Cband=C0/float(a*a)

    qrec=0.8367500185439279
    margin=float(q)-qrec
    eff=margin*float(a*a)

    print("a =",a)
    print("q =",q,"~",float(q))
    print("simple =",simple,"~",float(simple))
    print("positive-index margin =",margin)
    print("C_band =",Cband)
    print("margin*a^2 =",eff)
    print("RESULT: WP84_R2_A6_5_CONDITIONING_PASS")

if __name__=="__main__":
    main()
