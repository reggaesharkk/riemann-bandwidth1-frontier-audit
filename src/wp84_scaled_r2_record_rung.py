#!/usr/bin/env python3
"""Exact scaled-r2 model certificate at a=3/2.

Model reconnaissance only; this does not assert an unconditional zeta
percentage.
"""
from fractions import Fraction as F

def trim(p):
    p=p[:]
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b))
    c=[F(0)]*n
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

def main():
    P=[
        F(1),
        F(-43428,13891),
        F(37704,13891),
        F(-9660,13891),
    ]
    w0=F(1415,13891)
    m0,m1,m2=F(1),F(1),F(4,3)

    a=F(3,2)

    # r=1-[(x-a)^2/(x^2+a^2)]^2.
    den=mul([a*a,F(0),F(1)],[a*a,F(0),F(1)])
    xm=[-a,F(1)]
    num=sub(den,mul(mul(xm,xm),mul(xm,xm)))

    inv=invmod_poly(den,P)
    rem=divmod_poly(mul(num,inv),P)[1]
    rem=rem+[F(0)]*(3-len(rem))

    # r(0)=0, so subtract the zero-node evaluation of the polynomial
    # remainder when using the first three full moments.
    q=rem[0]*m0+rem[1]*m1+rem[2]*m2-w0*rem[0]
    simple=2*q-1

    q_expected=F(
        506616611216431521048,
        593746460699485818169,
    )
    s_expected=F(
        419486761733377223927,
        593746460699485818169,
    )

    assert q==q_expected,(q,q_expected)
    assert simple==s_expected,(simple,s_expected)

    record=F(673500037,10**9)
    threshold=(1+record)/2
    assert q>threshold

    print("a =",a)
    print("model r2 average =",q,"~",float(q))
    print("model simple ledger =",simple,"~",float(simple))
    print("record consumer threshold =",threshold,"~",float(threshold))
    print("consumer margin =",q-threshold,"~",float(q-threshold))
    print("pole distance =",float(a))
    print("global Lipschitz bound <=",float(F(8,1)/a))
    print("RESULT: WP84_SCALED_R2_RECORD_RUNG_PASS")

if __name__=="__main__":
    main()
