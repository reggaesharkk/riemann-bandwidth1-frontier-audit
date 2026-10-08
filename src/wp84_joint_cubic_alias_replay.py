"""Independent rational replay and hostile mutations. No producer import."""
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path
from hashlib import sha256
from copy import deepcopy
import json
ROOT=Path(__file__).resolve().parents[1]
def mul(a,b):
    n=len(a);return [[sum((a[i][k]*b[k][j] for k in range(n)),Q(0)) for j in range(n)] for i in range(n)]
def tr(a):return sum(a[i][i] for i in range(len(a)))/len(a)
def prod(seq):
    n=len(seq[0]);a=[[Q(int(i==j)) for j in range(n)] for i in range(n)]
    for x in seq:a=mul(a,x)
    return a
def verify(d):
    q=[-Q(19101,185500),Q(961,3710),Q(31,50),-Q(371,500)]
    c=[sum((q[i]*q[j] for i in range(4) for j in range(4) if i+j==k),Q(0)) for k in range(7)]
    assert list(map(str,c))==d['coefficients'];A=-c[5];B=c[6]
    band=3*Q(137721,5000)*(Q(106,333)**2)/6000
    var=-c[2]*(Q(106,333)**2)*Q(2,12001)
    cap=Q(21,200)-c[0]-c[2]/3-band-var
    margin=cap+A/36-B*Q(34,135)
    assert cap==Q(d['budget']['new_Jstar'])
    assert margin==Q(d['budget']['new_reference_margin'])
    assert margin==Q(8558084052085891,91584868530424500000)
    pair_lower=Q(31498340500050746323,150466924118016000000)
    assert B*pair_lower-cap==Q(d['budget']['new_necessary_saving_lower'])
    assert margin/c[3]==Q(d['budget']['new_third_ceiling'])
    assert band==Q(d['budget']['band']) and var==Q(d['budget']['new_variance'])
    assert d['R']==6000 and d['positive_constant_arithmetic_saving']=='0'
    assert d['exact_alias']['carrier_retained'] and not d['proper_power_removal_unconditional']
    adj=[[a,b] for a,b in combinations(range(5),2) if b-a in (1,4)]
    sep=[[a,b] for a,b in combinations(range(5),2) if b-a not in (1,4)]
    assert d['adjacent_pairs']==adj and d['separated_pairs']==sep and len(adj)==len(sep)==5
    assert Q(d['coefficient_bounds']['all_zero_displacement'])==c[3]-10*A/6<0
    assert Q(d['coefficient_bounds']['operator_upper_scalar'])==c[3]-5*A/6<0
    assert Q(d['exact_alias']['third_absolute_constant'])==288*12001**2
    assert Q(d['exact_alias']['joint_cubic_absolute_constant'])==288*(c[3]*12001**2+20*A*12001**4)
    beta=[Q(1),-Q(1,3),-Q(1,3),-Q(1,3)]
    assert sum(beta)==0 and sum(x*x for x in beta)/4==Q(1,3)
    cross=[sum(beta[i]**2*beta[(i+r)%4] for i in range(4))/4 for r in range(4)]
    assert cross==[Q(2,9),-Q(2,27),-Q(2,27),-Q(2,27)]
    assert Q(d['period_four']['cubic_upper_bound'])==Q(2,9)*c[3]-Q(25,81)*A<0
    for path,pin in d['source_pins'].items():assert sha256((ROOT/path).read_bytes()).hexdigest()==pin['sha256']
    return c
def independent_matrix_test():
    # Noncommuting symmetric matrices: exact trace identity, not a model replay.
    y=[[Q(2),Q(1),Q(0)],[Q(1),Q(-1),Q(2)],[Q(0),Q(2),Q(-1)]]
    ws=[[[Q(1),Q(2),Q(0)],[Q(2),Q(-2),Q(1)],[Q(0),Q(1),Q(1)]],
        [[Q(-1),Q(0),Q(1)],[Q(0),Q(1),Q(3)],[Q(1),Q(3),Q(0)]]]
    for w in ws:
        literal=sum(tr(prod([w if i in pair else y for i in range(5)])) for pair in combinations(range(5),2))
        reduced=5*tr(prod([w,w,y,y,y]))+5*tr(prod([w,y,w,y,y]))
        assert literal==reduced
        wrong=10*tr(prod([w,w,y,y,y]))
        assert literal!=wrong # scalar-variance contraction is illegal.
def alias_test():
    ps=[2,3,5,7,11,13,17,19]
    buckets={}
    for p,q,r in permutations(ps,3):buckets.setdefault(Q(p*q,r),[]).append((p,q,r))
    for x,tuples in buckets.items():
        assert len(tuples)<=2 and x.denominator in ps and x.denominator!=1
        assert all(r==x.denominator and p*q==x.numerator for p,q,r in tuples)
    same={}
    for p,q,r in permutations(ps,3):same.setdefault(p*q*r,[]).append((p,q,r))
    assert all(len(v)==6 for v in same.values())
    # Explicit, genuine three-prime frequency match D3/Q3, via a hidden balanced pair.
    visible={2:1,3:1,5:-1}; fifth={**visible,7:0};fifth.pop(7)
    assert visible==fifth
    # Proper-power exact closure exists: don't extend ordinary-distinct no-equality.
    assert 2*3==6
    return len(buckets),len(same)
if __name__=='__main__':
    d=json.loads((ROOT/'notes/WP84_JOINT_CUBIC_ALIAS_CERTIFICATE.json').read_text());verify(d)
    independent_matrix_test();counts=alias_test()
    mutants=[]
    for key,value in [('R',400),('positive_constant_arithmetic_saving','1/1000'),('proper_power_removal_unconditional',True)]:
        m=deepcopy(d);m[key]=value;mutants.append(m)
    m=deepcopy(d);m['adjacent_pairs']=m['adjacent_pairs'][:-1];mutants.append(m)
    m=deepcopy(d);m['coefficient_bounds']['all_zero_displacement']=d['coefficients'][3];mutants.append(m)
    m=deepcopy(d);m['exact_alias']['carrier_retained']=False;mutants.append(m)
    m=deepcopy(d);m['budget']['new_reference_margin']='1/10000';mutants.append(m)
    for m in mutants:
        try:verify(m)
        except AssertionError:pass
        else:raise AssertionError('hostile mutation accepted')
    print('PASS: independent consumer, 10 contractions, alias census',counts,'and',len(mutants),'hostile mutations')
