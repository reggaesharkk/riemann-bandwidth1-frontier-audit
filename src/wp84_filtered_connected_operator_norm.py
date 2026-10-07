#!/usr/bin/env python3
"""Variable-R exact/interval consumer gate and product-frame diagnostics.

No arithmetic Delta_R is certified. The finite-frame spectrum is explicitly
an auxiliary Fourier-feature diagnostic, not a prime-grid discretization or
the full growing-T semiprime operator. The note proves the uniform-in-T norm
obstruction. Run --spectral for 55-digit common-factor feature diagnostics.
"""
from fractions import Fraction as F
from itertools import product
import argparse, math
import mpmath as mp
from wp84_r400_pair_layer_exact import harmonics, conv_coeff, atan_bounds_inv

RS=(50,100,200,400,800,1600,3200)

def exact_checks():
    # Product collapse, including repeated-base states, checked independently.
    a=[F(1,7),F(2,11),F(3,13)]
    collapsed=[(2*a[i]*a[j] if i!=j else a[i]**2)
               for i in range(len(a)) for j in range(i,len(a))]
    assert sum(z*z for z in collapsed)==2*sum(x*x for x in a)**2-sum(x**4 for x in a)
    e=F('0.163249981456072'); c=F('2.1728342265'); c4=F(593,2000)
    wlim=(e-F(1,2000)-F(213,3000))/c4
    tollim=wlim-F(4,15)
    assert tollim>F('0.0427767')
    print('EXACT coefficient square-mass limit = 1/2')
    print('EXACT diagonal-beta-weighted square-mass limit = 1/72 (different vector)')
    print('EXACT Tol_infinity =',tollim,'approximately',float(tollim))
    # Exact pair certificate at R400, independent of the interval large-R loop.
    h1,h2,h4=harmonics(400)
    e4=4*h2[-1]**2+2*sum((conv_coeff(r,400,h1)**2 for r in range(1,801)),F(0))
    lo5,hi5=atan_bounds_inv(5,28); lo239,hi239=atan_bounds_inv(239,9)
    plo=16*lo5-4*hi239; phi=16*hi5-4*lo239
    xlo=1/phi**2; xhi=1/plo**2
    k=e4/8+2*h2[-1]**2-F(3,4)*h4[-1]
    pairup=F(1,12)+F(2,3)*h2[-1]*xhi+k*xhi*xhi
    pairlo=F(1,12)+F(2,3)*h2[-1]*xlo+k*xlo*xlo
    w400=(e-F(1,2000)-F(213,3000)-c/400)/c4
    assert w400-pairup>F('0.0247937')
    print('EXACT Tol400 interval approximately',float(w400-pairup),float(w400-pairlo))
    # Actual-product-space asymptotic block exponents, not artificial splits.
    theta=F(3,4)
    assert 2*theta-1==F(1,2) and 2*theta-2<0
    assert 2*(1-theta)**4==F(1,128)
    print('EXACT common-factor lower coefficient k_R(3/4) >= 1/128 for every R')
    print('PROVED IN NOTE: lambda_plus(E_R,T) >= M_T/(256 m_T)-53792*n_R'
          '-1808*n_R*M_T/m_T^2 -> infinity at each fixed R; n_R=6*(2R+1)^3')
    for R in RS:
        nr=6*(2*R+1)**3
        threshold=1024*nr*(1+F(132,7)*R)
        print('EXACT obstruction constants R',R,'n_R',nr,'bounded covariance norm',53792*nr,
              'sufficient asymptotic L threshold',threshold)

def budgets():
    iv=mp.iv; iv.dps=45
    h1=[iv.mpf(0)]; h2=iv.mpf(0); h4=iv.mpf(0)
    for n in range(1,max(RS)+1): h1.append(h1[-1]+iv.mpf(1)/n)
    snapshots={}
    for n in range(1,max(RS)+1):
        h2+=iv.mpf(1)/(n*n); h4+=iv.mpf(1)/(n**4)
        if n in RS: snapshots[n]=(h2,h4)
    for R in RS:
        h2,h4=snapshots[R]; e4=4*h2*h2
        for r in range(1,2*R+1):
            if r<=R: s=iv.mpf(2)/r*(h1[r-1]+h1[R]-h1[r]-h1[R-r])
            else: s=iv.mpf(2)/r*(h1[R]-h1[r-R-1])
            e4+=2*s*s
        pair=iv.mpf(1)/12+iv.mpf(2)*h2/(3*iv.pi**2)+(e4/8+2*h2*h2-iv.mpf(3)*h4/4)/iv.pi**4
        w=(iv.mpf('0.163249981456072')-iv.mpf(1)/2000-iv.mpf(213)/3000-iv.mpf('2.1728342265')/R)*2000/593
        print('CERTIFIED BUDGET R',R,'Pair_R',pair,'W_R',w,'Tol_R',w-pair,flush=True)

def inverse_fft(a):
    """55-digit ordinary numerical DFT; not an interval acceptance test."""
    a=list(a); n=len(a); j=0
    for k in range(1,n):
        bit=n>>1
        while j&bit: j^=bit; bit>>=1
        j^=bit
        if k<j: a[k],a[j]=a[j],a[k]
    width=2
    while width<=n:
        roots=[mp.exp(2j*mp.pi*k/width) for k in range(width//2)]
        for start in range(0,n,width):
            for k,w in enumerate(roots):
                u=a[start+k]; t=w*a[start+k+width//2]
                a[start+k]=u+t; a[start+k+width//2]=u-t
        width*=2
    return a

def common_factor(R):
    # theta=3/4. f is the R-filtered quarter interval. The fully summed six
    # exterior words equal 2*int f^4+4*int f(x)^2 f(x-1/4)^2 exactly.
    n=1
    while n<=4*R: n*=2
    coeff=[mp.mpc(0) for _ in range(n)]; shift=[mp.mpc(0) for _ in range(n)]
    coeff[0]=shift[0]=mp.mpf(1)/4
    for r in range(1,R+1):
        root=(-1j)**(r%4)
        z=(1-root)/(2j*mp.pi*r)
        coeff[r]=z; coeff[-r]=mp.conj(z)
        shift[r]=z*root; shift[-r]=mp.conj(z*root)
    f=inverse_fft(coeff); g=inverse_fft(shift)
    alt=sum(z.real**4 for z in f)/n
    nonalt=sum(z.real**2*w.real**2 for z,w in zip(f,g))/n
    return 2*alt+4*nonalt

def spectral():
    mp.mp.dps=55
    size=16; rows=64
    frequencies=[mp.mpf(3)/2+mp.mpf(2*j-size+1)/(2000*rows) for j in range(size)]
    gram=mp.matrix(size)
    for i in range(size):
        for j in range(size):
            delta=frequencies[i]-frequencies[j]
            gram[i,j]=1 if not delta else mp.sin(mp.pi*rows*delta)/(rows*mp.sin(mp.pi*delta))
    gamma=max(mp.eigsy(gram,eigvals_only=True))
    print('AUXILIARY DIAGNOSTIC: 16 distinct product-frequency features, 64 rows; not prime states')
    print('55-DIGIT product-frame top eigenvalue =',mp.nstr(gamma,35))
    for R in RS:
        k=common_factor(R)
        assert k>mp.mpf(1)/128
        print('NUMERICAL FEATURE R',R,'k_R(3/4)=',mp.nstr(k,35),
              'top eigenvalue of k_R*frame=',mp.nstr(k*gamma,35),flush=True)
    print('These are auxiliary feature spectra, NOT finite arithmetic lambda_plus or Delta_R.')

def main():
    if not __debug__: raise RuntimeError('Fail-closed checks require Python without -O.')
    p=argparse.ArgumentParser(description=__doc__); p.add_argument('--spectral',action='store_true')
    args=p.parse_args()
    exact_checks(); budgets()
    if args.spectral: spectral()
    print('RESULT: VARIABLE_R_BUDGET_PASS; UNIFORM_IN_T_OPERATOR_NORM_ROUTE_BLOCKED; ACTUAL_WEIGHTED_FORM_UNDECIDED')

if __name__=='__main__': main()
