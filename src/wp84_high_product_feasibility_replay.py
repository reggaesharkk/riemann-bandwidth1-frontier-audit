"""Independent exact checks; analytic bounds are proved in the accompanying note."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from copy import deepcopy
from itertools import product
from math import factorial
import json
ROOT=Path(__file__).resolve().parents[1]
def verify(d):
    q=[-Q(19101,185500),Q(961,3710),Q(31,50),-Q(371,500)]
    c=[sum((q[i]*q[j] for i,j in product(range(4),repeat=2) if i+j==k),Q(0)) for k in range(7)]
    assert list(map(str,c))==d['coefficients'];A=-c[5];B=c[6]
    band=3*Q(137721,5000)*Q(106,333)**2/6000
    variance=-c[2]*Q(106,333)**2*Q(2,12001)
    cap=Q(21,200)-c[0]-c[2]/3-band-variance
    margin=cap+A/36-B*Q(34,135)
    pair=Q(31498340500050746323,150466924118016000000)
    assert Q(d['budget']['new_Jstar'])==cap
    assert Q(d['budget']['new_reference_margin'])==margin
    assert Q(d['budget']['new_necessary_saving_lower'])==B*pair-cap>0
    assert Q(d['budget']['new_third_ceiling'])==margin/c[3]
    assert d['R']==6000 and d['third_moment_retained'] and d['new_constant_signed_saving']=='0'
    assert d['tails_retained'] and d['carrier_retained'] and not d['proper_power_disposal_unconditional']
    mixed=2**4*factorial(2);same=2**4*factorial(3)
    assert d['cubic_mixed_per_path_bound']['coefficients']==[3*mixed,6*mixed]
    assert d['cubic_mixed_per_path_bound']['eventual_L_bound_coefficients']==[3*mixed,3*mixed//2,6*mixed,12*mixed]
    assert d['same_sign_second_alias']['coefficients']==[3*same,6*same,3*same,same]
    assert Q(d['joint_multiplier'])==6*(c[3]*12001**2+20*A*12001**4)
    for row in d['ranges']:
        pos=list(map(Q,row['positive']));neg=list(map(Q,row['negative']))
        assert all(0<x<1 for x in pos+neg) # eventually below the NATURAL cutoff
        a=sum(pos,Q(0));b=sum(neg,Q(0))
        assert a==Q(row['alpha']) and b==Q(row['beta']) and a-b==row['alias']
        assert Q(row['divisor_bulk_exponent'])==(a+b)/2-1
        assert Q(row['core_width_exponent'])==a-1
    assert d['ranges'][0]['divisor_bulk_exponent']=='1/10'
    assert d['ranges'][1]['divisor_bulk_exponent']=='0'
    for cross in map(Q,d['gram_cross_examples']):
        assert abs(cross)==Q(1,2) and 1-cross*cross==Q(d['gram_determinant'])>0
    for p,v in d['source_pins'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==v['sha256']
def arithmetic_checks():
    # Independent rational shell counting, including an arbitrarily close integer.
    count=0
    for y in [Q(2),Q(17,3),Q(999999,100000),Q(101,7)]:
        for h in [Q(1,10),Q(1),Q(7)]:
            limit=int(3*y)+2
            actual=sum((min(Q(1),h/abs(Q(u)-y)) if Q(u)!=y else Q(1)) for u in range(1,limit))
            # At most 3 near integers; at most 2 in each shell [j,j+1).
            harmonic=sum((Q(1,j) for j in range(1,limit+2)),Q(0))
            assert actual<=3+2*h*harmonic
            count+=1
    # Additive clearing is legal only with its exact denominator and congruence.
    x=Q(7,3);u=12;v=5;offset=Q(u)-x*v
    assert offset==Q(1,3) and x.denominator*offset==3*u-7*v==1
    assert offset.denominator!=1
    # Square-root threshold exponent: v=X^(1/2-epsilon) gives -epsilon.
    for e in [Q(1,100),Q(1,10),Q(1,4)]:
        b=Q(1,2)-e;a=1+b;assert (a+b)/2-1==-e
    # There is no phase oscillation guarantee inside |delta|<=1/(100*T):
    # for t/T in [1,2], |t*delta|<=1/50, so cos(t delta)>=1-1/5000.
    assert 1-Q(1,50)**2/2==Q(4999,5000)
    return count
if __name__=='__main__':
    d=json.loads((ROOT/'notes/WP84_HIGH_PRODUCT_FEASIBILITY_CERTIFICATE.json').read_text())
    verify(d);n=arithmetic_checks();mutants=[]
    for key,value in [('R',400),('third_moment_retained',False),('new_constant_signed_saving','1/1000')]:
        m=deepcopy(d);m[key]=value;mutants.append(m)
    m=deepcopy(d);m['ranges'][0]['divisor_bulk_exponent']='-1/10';mutants.append(m)
    m=deepcopy(d);m['budget']['new_reference_margin']='1/10000';mutants.append(m)
    m=deepcopy(d);m['gram_determinant']='-3/4';mutants.append(m)
    m=deepcopy(d);m['cubic_mixed_per_path_bound']['coefficients'][0]=9;mutants.append(m)
    for key in ['tails_retained','carrier_retained']:
        m=deepcopy(d);m[key]=False;mutants.append(m)
    m=deepcopy(d);m['proper_power_disposal_unconditional']=True;mutants.append(m)
    for m in mutants:
        try:verify(m)
        except AssertionError:pass
        else:raise AssertionError('hostile mutation accepted')
    print('PASS exact gate, five range exponents, Gram obstruction,',n,'rational shell tests and',len(mutants),'hostile mutations')
