"""Deterministic finite-T ordinary-prime cell reconnaissance, not certification.
Reports complete zero-lag cell sums and explicitly limited full-R path samples.
No extrapolation is made; chosen candidate section is not theorem-certified.
"""
from bisect import bisect_left,bisect_right
from itertools import product
from math import log,exp,floor,pi,sqrt,prod
from pathlib import Path
import argparse
import json
import numpy as np
import mpmath as mp
from scipy.signal import fftconvolve


def primes_upto(n):
    sieve=bytearray(b'\1')*(n+1);sieve[:2]=b'\0\0'
    for p in range(2,int(sqrt(n))+1):
        if sieve[p]: sieve[p*p:n+1:p]=b'\0'*(((n-p*p)//p)+1)
    return [p for p in range(2,n+1) if sieve[p]]


def gamma(ss,signs,R):
    # Full finite lag closure, via convolution; each labelled edge remains separate.
    shifts=np.arange(-R,R+1); a=np.array([1+0j]); previous=0
    for s,e in zip(ss,signs):
        u=np.arange(-previous*R,previous*R+1)
        a=a*np.exp(2j*pi*e*u*s)
        f=np.empty(2*R+1,dtype=complex);f[R]=1-s
        nz=shifts!=0
        f[nz]=(1-np.exp(2j*pi*shifts[nz]*s))/(2j*pi*shifts[nz])
        if e==-1: f=np.conjugate(f)
        a=fftconvolve(a,f);previous+=1
    return complex(a[previous*R])


def kernel(T,L,k0,dprime,lam):
    if not lam: return mp.mpc(1)
    x=lam/mp.mpf(L)
    D=mp.exp(1j*mp.pi*(dprime-1)*x)*mp.sin(mp.pi*dprime*x)/(dprime*mp.sin(mp.pi*x))
    return mp.exp(1j*(mp.mpf(T)+2*mp.pi*k0/mp.mpf(L))*lam)*D


def run(T,H,R,sample_limit):
    mp.mp.dps=40
    L=log(T/(2*pi));X=exp(L);N=floor(exp(L-sqrt(L)))
    d=floor(T*L/(2*pi));q=floor(d/sqrt(L));k0=q//2;dprime=d-2*k0
    plist=primes_upto(N)
    def window(alpha):
        j=floor(alpha*log(X,2));low=2**j;high=min(2**(j+1),N)
        return [p for p in plist if low<p<=high], [low,high]
    high,high_range=window(.6);low,low_range=window(.4)
    rows=[]
    for b in [5,6]:
        if b==5:
            pos=list(product(high,repeat=2)); neg=list(product(low,repeat=3)); signs=[1,-1,1,-1,-1]
        else:
            pos=list(product(low,repeat=3));neg=list(product(low,repeat=3));signs=[1,-1,1,-1,1,-1]
        pos=[p for p in pos if len(set(p))==len(p)]
        neg=sorted((prod(p),p) for p in neg if len(set(p))==len(p));values=[v for v,p in neg]
        zero=mp.mpc(0); sample=mp.mpc(0);count=0;samples=[]
        for p in pos:
            A=prod(p)
            left=bisect_left(values,A*exp(-H/T)-1e-7);right=bisect_right(values,A*exp(H/T)+1e-7)
            for B,n in neg[left:right]:
                if A==B or len(set(p+n))!=b: continue
                lam=mp.log(mp.mpf(A)/B)
                if abs(lam)>mp.mpf(H)/T: continue
                labels=(p[0],n[0],p[1],n[1],n[2]) if b==5 else (p[0],n[0],p[1],n[1],p[2],n[2])
                ss=[log(v)/L for v in labels]
                cs=prod(-log(v)/(L*sqrt(v)) for v in labels)
                consumer=-11501/12500 if b==5 else 137641/250000
                K=kernel(T,L,k0,dprime,lam)
                zero+=consumer*cs*prod(1-s for s in ss)*K;count+=1
                if len(samples)<sample_limit:
                    G=gamma(ss,signs,R)
                    value=consumer*cs*G*complex(K);sample+=value
                    samples.append({'labels':labels,'A':A,'B':B,'T_lambda':float(T*lam),
                                    'Gamma_real':G.real,'Gamma_imag':G.imag,'signed_real_contribution':value.real})
        rows.append({'degree':b,'signs':signs,'distinct_nonexact_tuple_count':count,
                     'zero_lag_complete_cell_real':float(zero.real),
                     'full_R_sample_count':len(samples),'full_R_sample_real_sum':float(sample.real),
                     'full_R_sample_is_complete_cell':len(samples)==count,'samples':samples})
    return {'T':T,'H_diagnostic_only':H,'R_band':R,'L':L,'N':N,'candidate_section':[k0,k0+dprime-1],
            'candidate_section_theorem_certified':False,'a_phi_diagnostic':1,
            'high_prime_dyadic_range':high_range,'low_prime_dyadic_range':low_range,
            'prime_counts':[len(high),len(low)],'cells':rows}


def regressions(rows):
    # Independent enumeration validates the lag phases and convolution indexing.
    for signs in ([1,-1,1,-1,-1],[1,-1,1,-1,1,-1]):
        ss=[.13,.27,.31,.19,.23,.17][:len(signs)]
        direct=0j
        for ls in product([-1,0,1],repeat=len(signs)):
            if sum(ls): continue
            u=0; value=1+0j
            for s,e,l in zip(ss,signs,ls):
                f=1-s if l==0 else (1-np.exp(2j*pi*l*s))/(2j*pi*l)
                if e==-1: f=np.conjugate(f)
                value*=f*np.exp(2j*pi*e*u*s);u+=l
            direct+=value
        assert abs(direct-gamma(ss,signs,1))<5e-13
    last=[r for r in rows if r['T']==10000000]
    assert [c['distinct_nonexact_tuple_count'] for r in last for c in r['cells']]==[756,504,5868,2520]
    assert last[0]['cells'][0]['zero_lag_complete_cell_real']>0
    assert last[1]['cells'][0]['zero_lag_complete_cell_real']<0


def main():
    parser=argparse.ArgumentParser();parser.add_argument('--write',action='store_true');args=parser.parse_args()
    rows=[run(T,H,6000,8) for T in [100000,1000000,10000000] for H in [1,4]]
    regressions(rows)
    data={'regressions':'PASS: direct R=1 lag replay and preserved diagnostic sign flip','evidence':'NUMERICAL RECONNAISSANCE ONLY; no rigorous arithmetic error or asymptotic theorem',
          'sampling':'lexicographic first eight resolved tuples; all label multiplicities retained in counts',
          'rows':rows}
    if args.write:
        (Path(__file__).resolve().parents[1]/'notes/WP84_SIGNED_NEAR_PRODUCT_CELL_RECON.json').write_text(json.dumps(data,indent=2)+'\n')
    for row in rows:
        for cell in row['cells']:
            print(row['T'],row['H_diagnostic_only'],'b=',cell['degree'],'tuples=',cell['distinct_nonexact_tuple_count'],
                  'zero-lag real=',cell['zero_lag_complete_cell_real'],'full-R first-eight real=',cell['full_R_sample_real_sum'])
    print('NO CERTIFICATE: H not optimized; full-R partial samples are not full cell sums.')


if __name__=='__main__':main()
