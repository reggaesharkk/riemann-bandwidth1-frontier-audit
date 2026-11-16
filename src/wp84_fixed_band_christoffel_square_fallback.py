#!/usr/bin/env python3
"""Numerical conditioning reconnaissance for the fixed-band Christoffel-square fallback.

This script does NOT certify the pole enclosures.  It evaluates the exact
formula for the band constant at high precision and prints the resulting
first->79 fixed-band budget.
"""

import mpmath as mp

mp.mp.dps=80

A=mp.mpf(43428)/13891
B=mp.mpf(37704)/13891
C=mp.mpf(9660)/13891
W0=mp.mpf(1415)/13891

def P(z):
    return 1-A*z+B*z*z-C*z**3

def Pp(z):
    return -A+2*B*z-3*C*z*z

def roots_and_residues(delta):
    delta=mp.mpf(delta)
    roots=[]
    for sgn in (+1,-1):
        coeff=[
            -C,
            B,
            -A,
            1-sgn*1j*mp.sqrt(delta),
        ]
        roots.extend(mp.polyroots(coeff,maxsteps=1000,error=False))
    residues=[
        -delta*(delta+1)/(2*P(z)*Pp(z))
        for z in roots
    ]
    return roots,residues

def h(delta,w):
    delta=mp.mpf(delta)
    return (delta+1)*w/(delta+w)

def hinv(delta,y):
    delta=mp.mpf(delta)
    return delta*y/(delta+1-y)

def band_constant(delta):
    roots,res=roots_and_residues(delta)
    Cband=sum(
        6*abs(c)/(mp.pi**2*abs(mp.im(z))**3)
        for z,c in zip(roots,res)
    )
    eta=min(abs(mp.im(z)) for z in roots)
    return Cband,eta

def one(delta,R):
    Cband,eta=band_constant(delta)
    charge=Cband/R
    cap=h(delta,W0)
    total=cap+charge
    ceiling=mp.mpf(105)/1000
    residual=ceiling-total
    y=ceiling-charge
    square_ceiling=hinv(delta,y) if y>0 else mp.nan
    allowance=square_ceiling-W0 if y>0 else mp.nan
    print("delta =",delta,"R =",R)
    print("min |Im pole| =",mp.nstr(eta,24))
    print("C_band =",mp.nstr(Cband,24))
    print("band charge =",mp.nstr(charge,24))
    print("Jensen model cap =",mp.nstr(cap,24))
    print("model total incl band =",mp.nstr(total,24))
    print("margin below 0.105 =",mp.nstr(residual,24))
    print("required tau P(H_R)^2 <",mp.nstr(square_ceiling,24))
    print("allowance above w0 =",mp.nstr(allowance,24))
    print()

def main():
    for delta,R in [
        (61,40000),
        (85,40000),
        (101,40000),
        (144,40000),
    ]:
        one(delta,R)

    print("STATUS: numerical reconnaissance only; certify pole/residue enclosures before freezing R")

if __name__=="__main__":
    main()
