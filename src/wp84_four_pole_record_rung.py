#!/usr/bin/env python3
"""WP84 exact bounded four-pole record-beating model rung.

This is a MODEL/CONSUMER certificate, not an unconditional zeta theorem.

Using moments through degree four,
    m0=1, m1=1, m2=4/3, m3=2, m4=13/4,
the degree-2 Christoffel minimizer at zero is

    P2(x)=1-(7/4)x+(2/3)x^2

with exact square expectation 5/36.

For fixed delta>0 define the bounded rational consumer

    F_delta(x)=(delta+1)P2(x)^2/(P2(x)^2+delta).

It has four simple nonreal poles.  At delta=6 all poles satisfy |Im z|>1
by an exact radical inequality, and the Jensen model ledger gives the
simple-zero coefficient 151/221 = 0.6832579185...
"""
from fractions import Fraction as F
import cmath, math

M=[F(1),F(1),F(4,3),F(2),F(13,4)]
P=[F(1),F(-7,4),F(2,3)]

def mul(a,b):
    c=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            c[i+j]+=x*y
    return c

def moment(poly):
    return sum(c*M[k] for k,c in enumerate(poly))

def cap(delta):
    d=F(delta)
    return F(5)*(d+1)/(F(36)*d+5)

def simple(delta):
    return 1-2*cap(delta)

def poles(delta):
    # 12*(P2(z) - sigma*i*sqrt(delta)) =
    # 8 z^2 -21 z +12(1-sigma*i*sqrt(delta)).
    # Hence discriminant = 57 + 384 sigma*i*sqrt(delta).
    out=[]
    sd=math.sqrt(delta)
    for sigma in (+1,-1):
        disc=57+384j*sigma*sd
        root=cmath.sqrt(disc)
        out += [(21+root)/16,(21-root)/16]
    return out

def main():
    p2sq=mul(P,P)
    w=moment(p2sq)
    assert w==F(5,36),w

    # Support-free half-line certificate:
    # P2(-u)=1+(7/4)u+(2/3)u^2 >= 1 for u>=0.
    assert P[1]<0 and P[2]>0

    # Jensen cap for h_delta(t)=(delta+1)t/(t+delta).
    d=6
    c=cap(d)
    s=simple(d)
    assert c==F(35,221)
    assert s==F(151,221)
    assert s>F(683,1000)
    assert s>F(6735,10000)  # safely above 67.35%

    # Exact pole-strip proof for delta=6.
    #
    # sqrt(57+384 i sqrt(6)) = u+i v gives
    # v^2=(sqrt(57^2+384^2*6)-57)/2
    #     =(sqrt(887985)-57)/2.
    #
    # |Im pole|=v/16 > 1 iff sqrt(887985)>569.
    rad2=57*57+384*384*6
    assert rad2==887985
    assert rad2>569*569

    zs=poles(d)
    mingap=min(abs(z.imag) for z in zs)
    assert mingap>1
    # P2' vanishes only at z=21/16, where P2 is real, so no pole is multiple.
    crit=F(21,16)
    pcrit=P[0]+P[1]*crit+P[2]*crit*crit
    assert pcrit.denominator!=0  # exact real value
    assert pcrit*pcrit+F(d)>0

    print("P2 coefficients =",P)
    print("P2^2 coefficients =",p2sq)
    print("integral P2^2 dnu =",w,"~",float(w))
    print("positive-index floor =",1-w,"~",float(1-w))
    print("unbounded delta->infty simple ledger =",1-2*w,"~",float(1-2*w))
    print()
    print("delta=6 Jensen cap =",c,"~",float(c))
    print("delta=6 simple ledger =",s,"~",float(s))
    print("delta=6 poles:")
    for z in sorted(zs,key=lambda z:(z.real,z.imag)):
        print(" ",f"{z.real:.15f} {z.imag:+.15f}i")
    print("min |Im pole| =",mingap)
    print()
    print("ladder:")
    for dd in (5,6,7,10,20,30):
        print(dd,simple(dd),float(simple(dd)))
    print("RESULT: WP84_FOUR_POLE_RECORD_RUNG_PASS")

if __name__=="__main__":
    main()
