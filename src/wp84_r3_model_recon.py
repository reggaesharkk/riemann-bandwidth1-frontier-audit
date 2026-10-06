#!/usr/bin/env python3
"""WP84 exact rational-resolvent model reconnaissance.

The bounded minorant
    r3(x)=1-((x-1)^2/(x^2+1))^3
satisfies r3(x)<=1_{x>0} for every real x.

Against the extremal four-node quadrature associated with the current exact
six-moment Christoffel certificate (atom w0 at zero plus the three positive
roots of the cubic P), this script evaluates the r3 average exactly without
solving the cubic: reduce r3 modulo P.

This is MODEL RECONNAISSANCE, not an unconditional zeta theorem.
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

def main():
    # P(x)=1-(43428/13891)x+(37704/13891)x^2-(9660/13891)x^3
    P=[F(1),F(-43428,13891),F(37704,13891),F(-9660,13891)]

    # r3 numerator/denominator.
    base=[F(1),F(0),F(1)]
    den=mul(mul(base,base),base)  # (1+x^2)^3
    xm1=[F(-1),F(1)]
    xm1_6=[F(1)]
    for _ in range(6):
        xm1_6=mul(xm1_6,xm1)
    num=sub(den,xm1_6)

    # Exact remainder R with den*R == num mod P.
    D=4976884915749570021691469257
    R=[
        F(4891533619805586683578799376,D),
        F(147647890105813079827661376,D),
        F(-63083037446772628199712840,D),
    ]
    _,rem=divmod_poly(sub(mul(den,R),num),P)
    assert rem==[F(0)],rem

    # Current exact moments m0,m1,m2 and extremal zero atom.
    m0,m1,m2=F(1),F(1),F(4,3)
    w0=F(1415,13891)

    # On the three positive roots of P, r3=R.
    # The full quadrature moment functional includes w0 at x=0, so subtract
    # w0*R(0), because the true r3(0)=0.
    Efull=R[0]*m0+R[1]*m1+R[2]*m2
    Epos=Efull-w0*R[0]
    simple=2*Epos-1

    assert Epos==F(4456797085733462255065788192,D)
    assert simple==F(3936709255717354488440107127,D)
    assert simple>F(79,100)

    print("r3 average =",Epos,"~",float(Epos))
    print("2*r3-1 =",simple,"~",float(simple))
    print("RESULT: WP84_R3_MODEL_RECON_PASS")

if __name__=="__main__":
    main()
