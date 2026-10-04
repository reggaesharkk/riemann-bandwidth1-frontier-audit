#!/usr/bin/env python3
"""WP84 exact fixed-pole rational-minorant hierarchy.

For m>=1 define
    r_m(x)=1-(((x-1)^2)/(x^2+1))^m.

For x<=0, r_m(x)<=0; for x>0, 0<r_m(x)<=1, hence
    1_{x>0} >= r_m(x).

Against the current four-node extremal quadrature (zero atom w0 plus
three positive roots of the Christoffel cubic P), evaluate E[r_m] exactly
without solving the cubic by reducing the rational function modulo P.

This is model reconnaissance only, not an unconditional zeta theorem.
"""
from fractions import Fraction as F

def trim(p):
    p=p[:]
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p

def add(a,b):
    n=max(len(a),len(b))
    c=[F(0) for _ in range(n)]
    for i,v in enumerate(a): c[i]+=v
    for i,v in enumerate(b): c[i]+=v
    return trim(c)

def sub(a,b):
    return add(a,[-v for v in b])

def mul(a,b):
    c=[F(0) for _ in range(len(a)+len(b)-1)]
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

P=[F(1),F(-43428,13891),F(37704,13891),F(-9660,13891)]
w0=F(1415,13891)
m0,m1,m2=F(1),F(1),F(4,3)
full_simple=F(11061,13891)

def evaluate(m):
    base=[F(1),F(0),F(1)]              # 1+x^2
    den=[F(1)]
    for _ in range(m):
        den=mul(den,base)

    xm1=[F(-1),F(1)]
    power=[F(1)]
    for _ in range(2*m):
        power=mul(power,xm1)

    num=sub(den,power)
    inv=invmod_poly(den,P)
    rem=divmod_poly(mul(num,inv),P)[1]
    rem=rem+[F(0)]*(3-len(rem))

    # r_m equals rem on the three positive roots of P.
    # The full moment functional includes the zero atom, but r_m(0)=0.
    E=rem[0]*m0+rem[1]*m1+rem[2]*m2-w0*rem[0]
    simple=2*E-1
    return E,simple

def main():
    prev=None
    for m in range(1,11):
        E,simple=evaluate(m)
        if prev is not None:
            assert simple>prev
        prev=simple
        assert simple<full_simple
        print(f"m={m:2d}  q={float(E):.15f}  simple={float(simple):.15f}")
    E10,S10=evaluate(10)
    assert S10>F(79627,100000)
    gap=full_simple-S10
    print("m10 exact simple =",S10)
    print("full Christoffel simple =",full_simple)
    print("gap =",gap,"~",float(gap))
    print("RESULT: WP84_RM_MODEL_HIERARCHY_PASS")

if __name__=="__main__":
    main()
