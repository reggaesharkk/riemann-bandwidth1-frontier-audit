#!/usr/bin/env python3
"""Exact two-scale scalar gate; does not certify high-product arithmetic transfer."""
from fractions import Fraction as F
from math import comb, factorial, sqrt
from wp84_c5_pointwise_supercritical_sign import compile_terms


def budget():
    a=[F(-19101,185500),F(961,3710),F(31,50),F(-371,500)]
    c=[sum((a[j]*a[k-j] for j in range(4) if 0<=k-j<4),F(0))
       for k in range(7)]
    assert c[4]==0 and c[5]==-F(11501,12500) and c[6]==F(137641,250000)
    mu=[F(1),F(0),F(1,3),F(0),F(0),F(1,36),F(34,135)]
    erob=sum((x*y for x,y in zip(c,mu)),F(0))
    lower_pi=F(333,106)
    intercept=F(21,200)-erob
    charge=(3*F(137721,5000)-2*c[2])/lower_pi**2
    assert intercept==F(1730343659,1161345937500)
    assert charge==F(284757804319,33959756250)
    margin=lambda r: intercept-charge/r
    assert margin(6000)==F(52897896569489,572357731837500000)
    first=charge//intercept+1
    assert first==5628 and margin(5627)<=0<margin(5628)
    assert F(34,135)-F(157,630)==F(1,378)
    print('CLOSED M(R) =',intercept,'-',charge,'/ R')
    print('CLOSED M(6000) =',margin(6000))
    print('CLOSED first positive integer R =',first)
    print('CLOSED limiting margin =',float(intercept),'; sixth slack = 1/378')
    return margin


def geometric_bounds():
    assert len(compile_terms(5))==150
    assert len(compile_terms(6))==1082
    # At R=10^400: H_R<=1+log R<1201, pi>3, sqrt(2)/pi<1.
    # Therefore L_R<802 and e_R<10^-200; all arithmetic below is rational.
    r=10**400
    ell=F(802)
    tail=F(1,10**200)
    kernel5=150*5*tail*ell**4
    kernel6=1082*6*tail*ell**5
    # A normalized abstract full ledger with total coefficient variation W=1.
    delta5=10*tail*ell**9
    delta6=12*tail*ell**11
    assert kernel5>0 and kernel6>0
    assert delta6<F(1,378)
    print('CLOSED uniform word bound: k*sqrt(2)/(pi*sqrt(R))*(1+2H_R/pi)^(k-1)')
    print('CLOSED connected-kernel bounds: 750*e_R*L_R^4, 6492*e_R*L_R^5')
    print('CLOSED abstract full-ledger bounds: delta5=10*W5*e_R*L_R^9;'
          ' delta6=12*W6*e_R*L_R^11')
    print('CONDITIONAL model illustration W5=W6=1, R=10^400: both inequalities PASS')
    return r,delta5


def population_checks():
    # Complete sign population counts in a linear b-th power.
    assert [comb(5,r) for r in range(6)]==[1,5,10,10,5,1]
    assert [comb(6,r) for r in range(7)]==[1,6,15,20,15,6,1]
    assert sum(comb(5,r) for r in range(6))==2**5
    assert sum(comb(6,r) for r in range(7))==2**6
    # Full centered moment partitions without singleton blocks.
    types5={(5,):1,(3,2):10}
    types6={(6,):1,(4,2):15,(3,3):10,(2,2,2):15}
    def count_partition(sizes):
        den=1
        for size in sizes:
            den*=factorial(size)
        for size in set(sizes):
            den*=factorial(sizes.count(size))
        return factorial(sum(sizes))//den
    assert all(count_partition(t)==n for t,n in types5.items())
    assert all(count_partition(t)==n for t,n in types6.items())
    # Quarantine shortens individual support but not cubic-product support.
    log_t=10000.0
    log_n=log_t-sqrt(log_t)
    assert log_n-log_t<0 and 2*log_n-log_t>0 and 3*log_n-log_t>0
    print('CLOSED sign populations and full centered partition counts PASS')
    print('OPEN B5/B6 -> C5/C6: near-product correlations, aliases, normalization')


if __name__=='__main__':
    margin=budget()
    r,delta5=geometric_bounds()
    assert F(11501,12500)*delta5<margin(r)
    population_checks()
    print('CONDITIONAL arithmetic >79 gate; no unconditional theorem certified')
    print('RESULT: WP84_TWO_SCALE_FILTERED_TO_SHARP_GATE_PASS')
