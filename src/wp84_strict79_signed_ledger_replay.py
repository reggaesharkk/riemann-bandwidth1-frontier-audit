"""Independent exact replay; tests bounds/identities, never sampled prime moments."""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import permutations, product
from math import factorial
from pathlib import Path
import json
import subprocess

ROOT=Path(__file__).resolve().parents[1]

def choose(n,k):return F(factorial(n),factorial(k)*factorial(n-k))

def verify(d):
    assert d['input_head']=='d6e5de5b1247f8fe1c7b64b235c81b186115d82e'
    assert d['R']==6000 and d['cutoff']=='floor(exp(L-sqrt(L))), L=log(T/(2*pi))'
    assert d['kernel']=='original geometric grid sum with original path root interval and exp(i*T*m*L)'
    assert d['prime_windows']=='arbitrary original exact masks; no factor-restricted window is dropped'
    assert d['central_error_multiplier']=='N*(1+log(3*N))/T'
    assert d['negative_saving_proved']=='0' and d['central_o1_proved'] and not d['all_aliases_removed']
    assert not d['arithmetic_inequality_12_proved'] and not d['strict_gt79_proved']
    assert not d['frequency_supports']['cross_degree_exact_cancellation']
    totals={};cursor=0
    for name,b,k,c,w in [('D5',5,5,1,-F(11501,12500)),('Q3',5,3,10,-F(11501,12500)),
                        ('D6',6,6,1,F(137641,250000)),('Q4',6,4,15,F(137641,250000))]:
        total=F(0)
        for r in range(k+1):
            row=d['rows'][cursor];cursor+=1;s=k-r
            assert (row['family'],row['original_degree'],row['visible_degree'],row['positive'],row['negative'])==(name,b,k,r,s)
            assert row['ordered_sign_placements']==choose(k,r) and row['pair_choices']==c and F(row['signed_weight'])==w
            assert row['factor_length_exponents']==[r,s]
            assert row['possible_near_aliases']==[m for m in range(1-s,r) if m or (r and s)]
            removed=(r==1 and s>=1) or (s==1 and r>=1)
            assert row['central_window_empty']==(r*s==0) and row['central_one_prime_removed']==removed
            if removed:
                expected=F(176,7)*2**k*factorial(r)*factorial(s)*choose(k,r)*c*12001**(b-1)*(2 if k<b else 1)
                assert F(row['absolute_central_error_constant'])==expected;total+=abs(w)*expected
            else:assert row['absolute_central_error_constant'] is None
        totals[name]=str(total)
    assert cursor==len(d['rows'])==22 and totals==d['signed_absolute_error_constants']
    assert F(d['total_absolute_error_constant'])==sum(map(F,totals.values()))
    old=json.loads((ROOT/'notes/WP84_STRICT79_BALANCED_PAIR_CERTIFICATE.json').read_text())
    assert d['Jstar']==old['constants']['Jstar']
    assert d['necessary_saving_lower']==old['gaussian_pinching']['required_negative_residual_at_least'] and F(d['necessary_saving_lower'])>0
    for path,pin in d['source_pins'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest()==pin['sha256']
        assert subprocess.check_output(['git','rev-parse',d['input_head']+':'+path],cwd=ROOT,text=True).strip()==pin['git_blob']
    for path,expected in d['packet_sha256'].items():assert sha256((ROOT/path).read_bytes()).hexdigest()==expected

def analytic_checks():
    # Exact integer harmonic majorant, for arbitrary masks of candidate pairs.
    for n in range(2,31):
        H=sum(F(1,j) for j in range(1,3*n+1))
        actual=sum(F(1,abs(u-v)) for v in range(1,n+1) for u in range(1,3*n+1) if u!=v)
        assert actual<=2*n*H
    # Factor ordering multiplicity and UF support parity; diagnostics only.
    primes=(2,3,5,7,11,13)
    for k in (3,4,5,6):
        for r in range(k+1):
            values=Counter()
            for slots in permutations(primes,k):
                u=v=1
                for j,p in enumerate(slots):
                    if j<r:u*=p
                    else:v*=p
                value=F(u,v);assert value!=1
                values[value]+=1
            assert max(values.values())==factorial(r)*factorial(k-r)
            # Any frequency encodes exactly k nonzero +/-1 prime valuations.
            for z in values:
                count=sum(z.numerator%p==0 or z.denominator%p==0 for p in primes)
                assert count==k
    # Source filter covariance: 2 int s(1-s)^2 ds=1/6;
    # for nonzero integer mode: twice (-4+3)/(2*pi*m)^2=-1/(2*pi^2*m^2).
    assert 2*(F(1,2)-F(2,3)+F(1,4))==F(1,6)
    assert 2*(-4+3)/F(4)==-F(1,2)
    # Real x fifth/sixth joint gate has either sign: no generic negative bound.
    A=F(11501,12500);B=F(137641,250000)
    assert -A+B<0 and A+B>0  # x=1 and x=-1
    return 29

if __name__=='__main__':
    d=json.loads((ROOT/'notes/WP84_STRICT79_SIGNED_LEDGER_CERTIFICATE.json').read_text());verify(d);analytic_checks()
    hostile=[('R',400),('cutoff','N=T^0.1'),('kernel','carrier erased'),('prime_windows','unrestricted products'),
             ('negative_saving_proved','1/1000'),('all_aliases_removed',True),('arithmetic_inequality_12_proved',True),('strict_gt79_proved',True)]
    for k,v in hostile:
        bad=json.loads(json.dumps(d));bad[k]=v
        try:verify(bad)
        except AssertionError:pass
        else:raise AssertionError('accepted '+k)
    print('PASS 22 signed ledger cells; 8 central removals; exact error budgets; UF parity; harmonic majorant; filter signs;',len(hostile),'hostile mutations')
    print('No prime sampling/extrapolation; no positive-magnitude saving certified.')
