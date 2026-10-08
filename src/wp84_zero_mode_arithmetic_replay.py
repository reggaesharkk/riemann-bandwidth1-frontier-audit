"""Independent exact completion replay; no prime model or numerical limits."""
from pathlib import Path
from fractions import Fraction as Q
from hashlib import sha256
from copy import deepcopy
import json

ROOT = Path(__file__).resolve().parents[1]

def trim(p):
    while len(p)>1 and p[-1]==0: p.pop()
    return p

def divrem(p,d):
    p=p[:]; out=[0]*max(1,len(p)-len(d)+1)
    while len(p)>=len(d) and any(p):
        assert p[-1]%d[-1]==0
        c=p[-1]//d[-1]; k=len(p)-len(d);out[k]=c
        for j,x in enumerate(d):p[k+j]-=c*x
        trim(p)
    return trim(out),trim(p)

def cyclotomics(n):
    polys={}
    for r in range(1,n+1):
        p=[-1]+[0]*(r-1)+[1]
        for d in range(1,r):
            if r%d==0:
                p,rem=divrem(p,polys[d]);assert not any(rem)
        polys[r]=p
    return polys

def completion_checks():
    polys=cyclotomics(31);count=0; transcript=[]
    for r in [5,6,7,8,9,10,11,13,17,31]:
        masks=[[],[0],list(range(r)),list(range(1,min(4,r))),[r-1]]
        for J in masks:
            for sign in [-1,1]:
                for n in range(r):
                    # r times the Fourier identity in Z[z]/Phi_r(z).
                    p=[0]*r
                    for a in range(r):
                        for s in J:p[((a+sign)*n-a*s)%r]+=1
                    if n in J:p[(sign*n)%r]-=r
                    _,rem=divrem(p,polys[r]);assert not any(rem)
                    count+=1
                # Constant-completion index, retaining the complex coefficient.
                a=(-sign)%r
                assert (a+sign)%r==0
                assert all((-a*s)%r==(sign*s)%r for s in J)
            transcript.append([r,J])
    # Exact noninteger-X quotient decomposition for rational product bounds.
    cells=0
    for X in [Q(17,5),Q(9,2),Q(7)]:
        lo=X-Q(1,7);hi=X+Q(2,9)
        for r in range(2,32):
            for n in range(1,201):
                k,s=divmod(n,r)
                J=[t for t in range(r) if r*lo<k*r+t<=r*hi]
                assert (r*lo<n<=r*hi)==(s in J)
                cells+=1
    return count,cells,sha256(json.dumps(transcript,sort_keys=True).encode()).hexdigest()

def phase_checks():
    # Formal independent log coordinates (log p, log q, log X, log r).
    # H carries the original logarithmic coefficients and additive -1;
    # completion index a then gives original phase with additive a.
    for tau in [Q(1),Q(3,7),Q(17,2)]:
        original=[tau,tau,-tau,-tau]
        hp=[tau,0,0,0];hq=[0,tau,0,0];xr=[0,0,-tau,-tau]
        assert [hp[i]+hq[i]+xr[i] for i in range(4)]==original
        for r in [5,6,1009]:
            for a in [0,1,r-1]:
                assert (-1+(a+1))%r==a%r
            assert (r-1)%r!=0 # Completion-zero is not original-phase zero.

def validate(c):
    assert c['input_head']=='0ff4b44d2f7a8eb6b4c700dac7991cd7e102225f'
    assert c['R']==6000
    assert c['exact_original_phase'] and c['real_X_quotient_partition']
    assert c['source_masks_retained'] and c['joint_fifth_path_retained']
    assert not c['zero_is_evaluated_main_term']
    assert not c['zero_sign_controlled']
    assert not c['nonzero_rectangular_transfer']
    assert Q(c['actual_magnitude_saving'])==0
    assert Q(c['signed_constant'])==0
    assert Q(c['strip_loss'])==Q(1,10)
    assert Q(c['quotient_length_relative_product'])==Q(3,8)
    assert Q(c['balanced_inner_interval_exponent'])==Q(-1,5)
    assert c['completion_error']==0 and c['verdict']=='NO-GO'
    assert Q(c['c3'])==Q(21981971,46375000)
    assert Q(c['A'])==Q(11501,12500) and Q(c['B'])==Q(137641,250000)
    # Exact safe cosine bound for the original positive half-core.
    assert 1-(2*Q(22,7)/1000)**2/2 >= Q(4999,5000)
    for path,h in c['source_sha256'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest()==h

if __name__=='__main__':
    c=json.loads((ROOT/'notes/WP84_ZERO_MODE_ARITHMETIC_CERTIFICATE.json').read_text())
    validate(c)
    count,cells,digest=completion_checks()
    phase_checks()
    assert [count,cells,digest]==c['independent_completion_checks']
    mutations={
        'exact_original_phase':False,'real_X_quotient_partition':False,
        'source_masks_retained':False,'joint_fifth_path_retained':False,
        'zero_is_evaluated_main_term':True,'zero_sign_controlled':True,
        'nonzero_rectangular_transfer':True,'actual_magnitude_saving':'3/10',
        'signed_constant':'1/1000','completion_error':1,
        'balanced_inner_interval_exponent':'1/5'}
    for key,value in mutations.items():
        mutant=deepcopy(c);mutant[key]=value
        try:validate(mutant)
        except AssertionError:pass
        else:raise AssertionError('Hostile mutation survived: '+key)
    print(f'PASS {count} exact cyclotomic completion checks, {cells} real-X cell checks, '
          f'coefficients/exponents, source hashes and {len(mutations)} hostile mutations. '
          'Zero/new signed saving; NO-GO.')
