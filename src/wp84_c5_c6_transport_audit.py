#!/usr/bin/env python3
"""Exact algebra and falsifiers; no arithmetic transport theorem is claimed."""
from fractions import Fraction as F
from itertools import product
from random import Random
import argparse
from wp84_c5_pointwise_supercritical_sign import compile_terms, set_partitions
from math import factorial
from pathlib import Path
import importlib.util
import hashlib


def kernel(v, terms):
    assert sum(v) == 0
    sums = {(): F(0)}
    for _, masks in terms:
        for mask in masks:
            if mask not in sums:
                sums[mask] = sum((v[j] for j in mask), F(0))
    value = F(0)
    for sign, masks in terms:
        positions = [F(0)] + [sums[m] for m in masks]
        value += sign * max(F(0), 1 - max(positions) + min(positions))
    return value


def outer(v):
    pos = [F(0)]
    for x in v[:-1]:
        pos.append(pos[-1] + x)
    return max(F(0), 1 - max(pos) + min(pos))


def cell_data(v):
    """Exact active affine branch and full hyperplane signature at a point.

    Zero signature entries explicitly mark arrangement boundaries. A selected
    tie branch is valid only on its adjacent cell, not a differentiability claim.
    """
    terms=compile_terms(6)
    forms=[]
    for j in range(6):
        forms.append(tuple(int(k==j) for k in range(5)) if j<5 else (-1,)*5)
    def mask_form(mask):
        return tuple(sum(forms[j][k] for j in mask) for k in range(5))
    families=[[(0,)*5]+[mask_form(m) for m in masks] for _,masks in terms]
    families.append([(0,)*5]+[mask_form(tuple(range(k))) for k in range(1,6)])
    walls=set()
    for family in families:
        for a in family:
            for b in family:
                delta=tuple(x-y for x,y in zip(a,b))
                if not any(delta):
                    continue
                for c in (-1,0,1):
                    first=next(x for x in delta if x)
                    walls.add((delta,c) if first>0 else (tuple(-x for x in delta),-c))
    assert len(walls)==93
    x=v[:-1]
    def dot(a):
        return sum((F(t)*z for t,z in zip(a,x)),F(0))
    signature=[]
    for a,c in sorted(walls):
        t=dot(a)-c
        signature.append((t>0)-(t<0))
    constant=0
    gradient=[0]*5
    for (sign,_),family in zip(terms,families):
        low=min(family,key=dot); high=max(family,key=dot)
        if dot(high)-dot(low)<1:
            constant+=sign
            for k in range(5):
                gradient[k]+=sign*(low[k]-high[k])
    assert F(constant)+sum((F(g)*z for g,z in zip(gradient,x)),F(0))==kernel(v,terms)
    return constant,tuple(gradient),tuple(signature)


def upstream_convention_gate():
    base=Path(__file__).resolve().parents[1]/'certificates'/'wp84_c5_c6_upstream'
    path=base/'exact_connected.py'
    raw=path.read_bytes()
    blob=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    assert blob=='2983c1e03217d55cdebae45210d7f2b8861435cc',blob
    path2=base/'exact_polytope.py'
    raw2=path2.read_bytes()
    blob2=hashlib.sha1(b'blob '+str(len(raw2)).encode()+b'\0'+raw2).hexdigest()
    assert blob2=='8738e1f9f6ac30730c9e84b2d4a469959714cca9',blob2
    spec=importlib.util.spec_from_file_location('wp84_pinned_connected',path)
    upstream=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(upstream)
    for degree in (4,5,6):
        assert compile_terms(degree)==upstream.compile_terms(degree)
    print('CLOSED: pinned upstream source hashes and term-by-term conventions agree')
    from wp79_independent_connected_archive_verify import parse_cycle, parse_42, EXPECTED_SHA, blob_sha
    for name,sha in EXPECTED_SHA.items():
        assert blob_sha(base/name)==sha,(name,blob_sha(base/name))
    c5,_=parse_cycle(base/'exact_c5.txt',150)
    c6,_=parse_cycle(base/'exact_c6.txt',1082)
    values=parse_42(base/'exact_42.txt')
    spec42=6*values[1]+6*values[2]+3*values[3]
    assert (c5,c6,spec42)==(F(1,36),-F(1,126),-F(23,420))
    # Frozen triple-pair class values, inspected in exact_t222.py; not reintegrated.
    assert 5*F(3,70)+6*F(1,90)+3*F(1,180)+F(1,70)==F(131,420)
    print('CLOSED model archive sums: C5=',c5,'C6=',c6,'{4,2}=',spec42)
    print('CONDITIONAL model class assembly {2,2,2}=131/420; no reintegration or prime transport')


def error_budget():
    A, B = F(11501,12500), F(137641,250000)
    pi_lo = F(333,106)
    erob = F(240421959557,2322691875000)
    band = 3*F(137721,5000)/(pi_lo*pi_lo*6000)
    variance = F(26060119,430128125)*2/(pi_lo*pi_lo*6000)
    M = F(21,200)-erob-band-variance
    assert M == F(52897896569489,572357731837500000)
    print('CLOSED: joint budget', A, '* eps5 +', B, '* eps6 <', M)
    print('axis limits eps5, eps6:', M/A, M/B)
    print('axis limits decimals:', float(M/A), float(M/B))
    # Full model sixth value improves the relaxed ceiling by 1/378.
    assert F(34,135)-F(157,630) == F(1,378)
    print('eps5 allowance if sixth equals model:', (M+B/F(378))/A)
    assert F(131,420)-F(23,420)-F(1,126) == F(157,630)
    assert F(131,420)-F(23,420)-F(1,189) == F(34,135)


def compression_falsifier():
    # d=2, y/L=1/2. U has diagonal (1/2,-1/2),
    # off-diagonal -i/pi. tau(U U*)=1/4+1/pi^2.
    # tau(P U_y U_-y P)=1/2. pi>333/106 gives a strict gap.
    gap_lo = F(1,4)-1/F(333,106)**2
    assert gap_lo > 0
    print('CLOSED: compression witness d=2, s=1/2, R>=1')
    print('actual compressed pair trace = 1/4 + 1/pi^2')
    print('single-compression spread trace = 1/2')
    print('gap greater than', gap_lo)


def cumulant(values):
    """Joint cumulant over a uniform finite root-index ensemble, exactly."""
    n=len(values)
    count=len(values[0])
    assert count and all(len(v)==count for v in values)
    total=F(0)
    for part in set_partitions(list(range(n))):
        term=F((-1)**(len(part)-1)*factorial(len(part)-1))
        for block in part:
            moment=F(0)
            for k in range(count):
                p=F(1)
                for j in block:
                    p*=values[j][k]
                moment+=p
            term*=moment/count
        total+=term
    return total


def sector_ledger():
    for degree, expected in [(5,{(5,):1,(2,3):10}),
                             (6,{(2,2,2):15,(2,4):15,(3,3):10,(6,):1})]:
        parts=list(set_partitions(list(range(degree))))
        counts={}
        values=[[F((j+1)*(k+2)%7-3,5) for k in range(4)]
                for j in range(degree)]
        total=F(0)
        for part in parts:
            shape=tuple(sorted(map(len,part)))
            counts[shape]=counts.get(shape,0)+1
            term=F(1)
            for block in part:
                term*=cumulant([values[j] for j in block])
            total+=term
        moment=sum((product_value([v[k] for v in values]) for k in range(4)),F(0))/4
        assert total==moment
        assert all(counts[s]==c for s,c in expected.items())
        print('CLOSED: degree',degree,'partition counts',counts)
    print('CLOSED: finite empirical moment-cumulant reconstruction, including singletons')


def product_value(xs):
    p=F(1)
    for x in xs:
        p*=x
    return p


def finite_word_diagnostic():
    """50-digit numerical check of the prime branch/path identity, not transport."""
    import mpmath as mp
    mp.mp.dps=50
    T=mp.mpf(19)
    L=mp.log(T)
    d=int(mp.floor(T*L/(2*mp.pi)))
    R=1
    primes=(2,3,5,7)
    tau=[T+2*mp.pi*i/L for i in range(d)]
    Q=[sum((-mp.log(p)/(L*mp.sqrt(p))*mp.exp(1j*t*mp.log(p))
            for p in primes),mp.mpc(0)) for t in tau]
    Qp=[sum((-mp.log(p)/(L*mp.sqrt(p))*1j*mp.log(p)*mp.exp(1j*t*mp.log(p))
             for p in primes),mp.mpc(0)) for t in tau]
    X=mp.matrix(d)
    for i in range(d):
        for j in range(d):
            if abs(j-i)>R:
                X[i,j]=0
            elif i==j:
                X[i,j]=2*Q[i].real-2*Qp[i].imag/L
            else:
                X[i,j]=(Q[i].imag-Q[j].imag)/(mp.pi*(j-i))
    def branch_entry(i,r):
        z=mp.mpc(0)
        for p in primes:
            y=mp.log(p); s=y/L; c=-y/(L*mp.sqrt(p))
            f=1-s if r==0 else (1-mp.exp(2j*mp.pi*r*s))/(2j*mp.pi*r)
            plus=c*mp.exp(1j*tau[i]*y)*f
            z+=plus+mp.conj(plus)
        return z
    entry_error=max(abs(branch_entry(i,j-i)-X[i,j])
                    for i in range(d) for j in range(d) if abs(j-i)<=R)
    assert entry_error<mp.mpf('1e-45')
    for degree in (5,6):
        actual=sum((X**degree)[i,i] for i in range(d))/d
        path_total=mp.mpc(0)
        for steps in product(range(-R,R+1),repeat=degree):
            if sum(steps):
                continue
            offsets=[0]
            for r in steps:
                offsets.append(offsets[-1]+r)
            for root in range(-min(offsets),d-max(offsets)):
                term=mp.mpc(1)
                for j,r in enumerate(steps):
                    term*=branch_entry(root+offsets[j],r)
                path_total+=term/d
        error=abs(actual-path_total)
        assert error<mp.mpf('1e-45')
        print('NUMERICAL finite prime path check degree',degree,'residual',mp.nstr(error,6))


def sixth_recon(samples):
    terms = compile_terms(6)
    assert len(terms) == 1082
    rng = Random(20261006)
    found = {}
    # Generate rational outer walks, ensuring positive outer overlap.
    for _ in range(samples):
        positions = [F(rng.randrange(0,10),10) for _ in range(6)]
        v = tuple(positions[(j+1)%6]-positions[j] for j in range(6))
        C = kernel(v,terms)
        if C and (1 if C>0 else -1) not in found:
            found[1 if C>0 else -1] = (v,C,outer(v))
        if len(found)==2:
            break
    assert len(found)==2, found
    for sign in (-1,1):
        v,C,O = found[sign]
        assert sum(v)==0 and O>0 and sign*C>0
        print('CLOSED: C6 sign witness', ','.join(map(str,v)), 'C6=',C,'O6=',O)
    # Kernel symmetry checks, finite diagnostic only.
    for v,C,_ in found.values():
        assert kernel(tuple(-x for x in v),terms)==C
        for k in range(6):
            assert kernel(v[k:]+v[:k],terms)==C
        constant,gradient,signature=cell_data(v)
        print('C6 affine branch constant, gradient:',constant,gradient,
              'boundary walls:',signature.count(0),'of',len(signature))
    print('CLOSED: 1082-term evaluator; mixed signs falsify negative-Gram identity')
    return found


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--samples',type=int,default=1000)
    parser.add_argument('--point',help='six comma-separated rational coordinates, sum zero')
    args=parser.parse_args()
    if args.point:
        v=tuple(map(F,args.point.split(',')))
        assert len(v)==6 and sum(v)==0
        print('C6=',kernel(v,compile_terms(6)),'O6=',outer(v))
        constant,gradient,signature=cell_data(v)
        print('affine branch:',constant,gradient)
        print('93-wall signature:',signature)
        return
    upstream_convention_gate()
    error_budget()
    compression_falsifier()
    sector_ledger()
    finite_word_diagnostic()
    sixth_recon(args.samples)
    print('RESULT: WP84_C5_C6_TRANSPORT_AUDIT_PASS')


if __name__=='__main__':
    main()
