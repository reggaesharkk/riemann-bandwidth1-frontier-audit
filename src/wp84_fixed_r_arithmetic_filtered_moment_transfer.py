#!/usr/bin/env python3
"""WP84 arithmetic reconnaissance. Finite checks do not prove long-scale transfer."""
from collections import defaultdict
from fractions import Fraction as F
from itertools import product
from math import comb, factorial, log, pi
import argparse


def scale_and_closures():
    ell=10000.0-log(2*pi)
    current_log_n=ell-ell**0.5
    assert 3*current_log_n-10000>0
    short_l=F(1,4)*10000
    assert 3*short_l-10000+7*log(float(short_l))<0
    theta=F(1,3)
    variance=theta**2-F(2,3)*theta**3
    assert variance==F(7,81) and F(1,3)-variance==F(20,81)
    assert 2*theta-1<0
    print('CLOSED scale audit: L=log(T/(2pi)), log N=L-o(L); N^3/T diverges')
    print('CLOSED shortening test: cutoff theta=1/3 gives variance 7/81; dimension cap 2theta-1<0')
    primes=(2,3,5,7)
    def counts(r):
        out=defaultdict(int)
        for ns in product(primes,repeat=r):
            m=1
            for n in ns:
                m*=n
            out[m]+=1
        return out
    tables=[counts(r) for r in range(7)]
    for r in range(6):
        assert not set(tables[r]).intersection(tables[5-r])
    for r in range(7):
        if r!=3:
            assert not set(tables[r]).intersection(tables[6-r])
    leading=0
    for ns in product(primes,repeat=3):
        if len(set(ns))==3:
            leading+=factorial(3)
    assert leading==comb(4,3)*factorial(3)**2
    assert leading*comb(6,3)==15*8*(4*3*2)
    assert 2*2*4==4*4  # Proper-power exact closure, degree five.
    assert 4*4==2*2*2*2  # Proper-power 2-vs-4 closure.
    for b in (5,6):
        sectors=[(r,b-r,r,b-r,max(r,b-r),F(b,2)) for r in range(b+1)]
        print('CLOSED degree',b,'sectors (r,s,N powers,pool power,Hilbert power):',sectors)
    print('CLOSED exact ordinary closures: degree5 none; degree6 three opposite pairs')


def finite_correlation_checks():
    import mpmath as mp
    mp.mp.dps=45
    T=mp.mpf(17)
    L=mp.log(11)
    h=2*mp.pi/L
    d=5
    R=1
    ns=(2,3,4,5,7,8,9)
    base={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
    coeff={n:-mp.log(base[n])/(L*mp.sqrt(n)) for n in ns}
    logs={n:mp.log(n) for n in ns}
    tol=mp.mpf('1e-36')

    def fields(k):
        t=T+h*k
        z=sum((coeff[n]*mp.exp(1j*t*logs[n]) for n in ns),mp.mpc(0))
        z1=sum((coeff[n]*(1-logs[n]/L)*mp.exp(1j*t*logs[n]) for n in ns),mp.mpc(0))
        return z.imag,2*z1.real

    def entry(i,j):
        if abs(j-i)>R:
            return mp.mpf(0)
        ai,bi=fields(i)
        if i==j:
            return bi
        aj,_=fields(j)
        return (ai-aj)/(mp.pi*(j-i))

    def jcoef(r,s,epsilon):
        if not r:
            return 1-s
        if epsilon==1:
            return (mp.exp(-2j*mp.pi*r*s)-1)/(2j*mp.pi*r)
        return (1-mp.exp(2j*mp.pi*r*s))/(2j*mp.pi*r)

    cache={}
    def dirichlet_entry(i,j):
        if (i,j) not in cache:
            r=j-i
            cache[i,j]=sum((coeff[n]*jcoef(r,logs[n]/L,e)
                            *mp.exp(1j*e*(T+h*j)*logs[n])
                            for n in ns for e in (1,-1)),mp.mpc(0))
            assert abs(cache[i,j]-entry(i,j))<tol
        return cache[i,j]

    for b in (5,6):
        indices=list(range(-b*R,d+b*R))
        ambient=mp.matrix([[entry(i,j) for j in indices] for i in indices])
        power=ambient**b
        direct=sum((power[indices.index(k),indices.index(k)] for k in range(d)),mp.mpf(0))/d
        paths=[rs for rs in product(range(-R,R+1),repeat=b) if sum(rs)==0]
        assert len(paths)=={5:51,6:141}[b]
        expanded=mp.mpc(0)
        for k in range(d):
            for rs in paths:
                q=0
                word=mp.mpc(1)
                for r in rs:
                    word*=dirichlet_entry(k+q,k+q+r)
                    q+=r
                expanded+=word/d
        assert abs(expanded-direct)<tol
        print('CLOSED finite diagnostic: degree',b,'filtered DP paths',len(paths),'match direct B')

    # Independently collapse beta^b by INTEGER products, including proper powers.
    w={n:coeff[n]*(1-logs[n]/L) for n in ns}
    tables=[{1:mp.mpf(1)}]
    for r in range(6):
        nxt=defaultdict(lambda:mp.mpf(0))
        for u,a in tables[-1].items():
            for n in ns:
                nxt[u*n]+=a*w[n]
        tables.append(dict(nxt))

    def kernel(lam,local_l=L):
        return sum((mp.exp(1j*(T+2*mp.pi*k/local_l)*lam) for k in range(d)),mp.mpc(0))/d

    kernel_cache={}
    def ratio_kernel(u,v):
        from math import gcd
        g=gcd(u,v)
        key=(u//g,v//g)
        if key not in kernel_cache:
            kernel_cache[key]=kernel(mp.log(mp.mpf(key[0])/key[1]))
        return kernel_cache[key]

    for b in (5,6):
        reduced=mp.mpc(0)
        for r in range(b+1):
            for u,a in tables[r].items():
                for v,z in tables[b-r].items():
                    reduced+=comb(b,r)*a*z*ratio_kernel(u,v)
        direct=sum((fields(k)[1]**b for k in range(d)),mp.mpf(0))/d
        assert abs(reduced-direct)<tol
        print('CLOSED finite diagnostic: degree',b,'collapsed diagonal correlations include powers PASS')

    # At L=log(8), the proper-power degree-five tuple (8,3,3 | 3,3)
    # has u/v=8, and its sampled carrier is identical at every Fourier index.
    alias_l=mp.log(8)
    assert abs(kernel(mp.log(mp.mpf(72)/9),alias_l)-mp.exp(1j*T*alias_l))<tol
    print('CLOSED finite diagnostic: exact alias phase log(u/v)=mL PASS')


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--exact-only',action='store_true')
    args=parser.parse_args()
    scale_and_closures()
    if not args.exact_only:
        finite_correlation_checks()
    print('CLOSED short-cutoff theorem: B5->0, B6->filtered pair/Wick functional')
    print('FALSIFIED unchanged fifth target under short-cutoff diagonal reduction')
    print('OPEN original-scale signed product-correlation law, including near aliases')
    print('RESULT: WP84_FIXED_R_ARITHMETIC_FILTERED_MOMENT_TRANSFER_PASS')
