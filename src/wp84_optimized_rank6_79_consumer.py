#!/usr/bin/env python3
"""Exact regression gate for the rank-six 79.5197% bounded consumer."""

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

def scale(a,s):
    return trim([s*x for x in a])

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

def egcd(a,b):
    r0,r1=trim(a),trim(b)
    s0,s1=[F(1)],[F(0)]
    t0,t1=[F(0)],[F(1)]
    while not (len(r1)==1 and r1[0]==0):
        q,r=divmod_poly(r0,r1)
        r0,r1=r1,r
        s0,s1=s1,sub(s0,mul(q,s1))
        t0,t1=t1,sub(t0,mul(q,t1))
    lead=r0[-1]
    return scale(r0,1/lead),scale(s0,1/lead),scale(t0,1/lead)

def mod_poly(a,m):
    return divmod_poly(a,m)[1]

def inv_mod(a,m):
    g,s,_=egcd(a,m)
    assert g==[F(1)]
    return mod_poly(s,m)

def main():
    # Exact support identity:
    # p(x)-1 = S(x)/[500000(1+x^2)^3].
    # Coefficients are ascending in x.
    S=[
        1313,
        -3398722,
        7613939,
        -12370084,
        7506675,
        -3353410,
        1313,
    ]
    # For x=-y, all coefficients are positive.
    Sy=[F(S[k])*(-1)**k for k in range(len(S))]
    assert all(c>0 for c in Sy),Sy

    base=[F(1),F(0),F(1)]
    den=scale(mul(mul(base,base),base),F(500000))
    pnum=add(den,[F(v) for v in S])

    # Christoffel cubic.
    P=[F(1),F(-43428,13891),F(37704,13891),F(-9660,13891)]

    # Reduce p=pnum/den modulo P.
    R=mod_poly(mul(pnum,inv_mod(den,P)),P)
    R += [F(0)]*(3-len(R))

    # Frozen model moments and zero atom.
    m0,m1,m2=F(1),F(1),F(4,3)
    w0=F(1415,13891)

    # p(0)=501313/500000 from the support identity.
    p0=F(501313,500000)

    # R agrees with p on the three positive roots of P.
    Efull=R[0]*m0+R[1]*m1+R[2]*m2
    Ep=Efull-w0*R[0]+w0*p0
    simple=1-2*Ep

    expected_E=F(
        254819740781074726741910188950681,
        2488442457874785010845734628500000,
    )
    expected_simple=F(
        989401488156317778680957125299319,
        1244221228937392505422867314250000,
    )

    assert Ep==expected_E,(Ep,expected_E)
    assert simple==expected_simple,(simple,expected_simple)
    assert simple>F(79,100)
    assert Ep<F(105,1000)

    print("support coefficients at x=-y:",Sy)
    print("model defect =",Ep,"~",float(Ep))
    print("model simple =",simple,"~",float(simple))
    print("79% defect cushion =",float(F(105,1000)-Ep))
    print("RESULT: WP84_OPTIMIZED_RANK6_79_CONSUMER_PASS")

if __name__=="__main__":
    main()
