#!/usr/bin/env python3
"""Regression gate for the F61 trace-Hessian identity."""
import mpmath as mp

mp.mp.dps=70
a=mp.mpf(43428)/13891
b=mp.mpf(37704)/13891
c=mp.mpf(9660)/13891
delta=mp.mpf(61)

def P(x):
    return 1-a*x+b*x*x-c*x**3

def Pp(x):
    return -a+2*b*x-3*c*x*x

def f(x):
    g=P(x)**2
    return 62*g/(g+61)

def fp(x):
    return mp.diff(f,x)

def fpp(x):
    return mp.diff(f,x,2)

def roots_and_residues():
    roots=[]
    for sgn in (+1,-1):
        coeff=[-c,b,-a,1-sgn*1j*mp.sqrt(delta)]
        roots.extend(mp.polyroots(coeff,maxsteps=500,error=False))
    residues=[-delta*(delta+1)/(2*P(z)*Pp(z)) for z in roots]
    return roots,residues

def kpole(x,y,roots,residues):
    total=0
    for z,r in zip(roots,residues):
        total += r*(1/(x-z)**2/(y-z)+1/(y-z)**2/(x-z))/2
    return total

def kdiff(x,y):
    if x==y:
        return fpp(x)/2
    return (fp(x)-fp(y))/(2*(x-y))

def main():
    roots,residues=roots_and_residues()
    pts=[mp.mpf("-3.1"),mp.mpf("-0.7"),mp.mpf("0.2"),
         mp.mpf("1.1"),mp.mpf("2.4"),mp.mpf("5.3")]
    worst=mp.mpf("0")
    for x in pts:
        for y in pts:
            worst=max(worst,abs(kpole(x,y,roots,residues)-kdiff(x,y)))
    assert worst < mp.mpf("1e-55")

    mineta=min(abs(mp.im(z)) for z in roots)
    c3=sum(abs(r)/(abs(mp.im(z))**4) for z,r in zip(roots,residues))

    print("min pole |Im| =",mp.nstr(mineta,20))
    print("C3 =",mp.nstr(c3,20))
    print("worst identity error =",mp.nstr(worst,8))
    print("RESULT: WP84_F61_TRACE_HESSIAN_GATE_PASS")

if __name__=="__main__":
    main()
