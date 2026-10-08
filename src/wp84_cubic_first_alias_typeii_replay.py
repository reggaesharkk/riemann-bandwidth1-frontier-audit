"""Independent formal convolution, exponent and Fourier-mask hostile replay."""
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
from copy import deepcopy
import json
ROOT=Path(__file__).resolve().parents[1]
def formal_check(N,U,V):
    primes=[n for n in range(2,N+1) if all(n%d for d in range(2,int(n**.5)+1))]
    logs=[{} for _ in range(N+1)];L=[{} for _ in range(N+1)];mu=[1]*(N+1)
    for n in range(1,N+1):
        remaining=n;nf=0;repeat=False
        for p in primes:
            exponent=0
            while remaining%p==0:remaining//=p;exponent+=1
            if exponent:logs[n][p]=exponent;nf+=1;repeat|=exponent>1
        mu[n]=0 if repeat else (-1)**nf
        if len(logs[n])==1:L[n]={next(iter(logs[n])):1}
    def scaled_add(dst,v,c):
        for p,x in v.items():dst[p]=dst.get(p,0)+c*x
    # Compute each entire convolution array, independently of the producer's per-n loops.
    vals=[{} for _ in range(N+1)]
    for a in range(1,N+1):
        for b in range(1,N//a+1):
            if a<=U:scaled_add(vals[a*b],logs[b],mu[a])
            for c in range(1,N//(a*b)+1):
                if a<=U and c<=V:scaled_add(vals[a*b*c],L[c],-mu[a])
                if a>U and c>V:scaled_add(vals[a*b*c],L[c],mu[a])
    rows=[]
    for n in range(1,N+1):
        if n<=V:scaled_add(vals[n],L[n],1)
        assert {p:x for p,x in vals[n].items() if x}==L[n]
        if len(logs[n])==1 and sum(logs[n].values())>1:scaled_add(vals[n],L[n],-1)
        target=L[n] if n in primes else {}
        assert {p:x for p,x in vals[n].items() if x}==target
        rows.append({str(p):x for p,x in sorted(vals[n].items()) if x})
    assert L[49]=={7:1} and rows[48]=={} # dropped compensation is false.
    return sha256(json.dumps(rows,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def verify(d):
    old=json.loads((ROOT/'notes/WP84_HIGH_PRODUCT_FEASIBILITY_CERTIFICATE.json').read_text())
    assert d['budget']==old['budget'] and d['coefficients']==old['coefficients'] and d['R']==6000
    assert d['carrier_retained'] and d['source_masks_retained'] and not d['window_covariance_substitution']
    assert d['power_saving_on_actual_window']==d['constant_signed_saving']=='0' and not d['strict_gt79_proved']
    for r in d['prime_ranges']:
        a=Q(r['p']);b=Q(r['q']);c=Q(r['r'])
        assert 0<a<1 and 0<b<1 and a+b-c==1
        assert (a+b+c)/2-1==Q(r['baseline_loss'])==Q(1,10)
        assert Q(r['q_core_interval_exponent'])==b-1<0
    for r in d['denominator_typeii_blocks']:
        a=Q(r['a']);b=Q(r['b']);assert a+b==Q(3,5) and min(a,b)>Q(1,10)
        assert Q(r['inner_core_interval_exponent'])==b-1<0
    l=d['linearization'];assert l['pointwise_error_constant_pi']==16
    assert l['mass_constants']==[32,96] and l['aggregate_error_constants_pi']==[16*32,16*96*2]
    assert l['fixed_H_accuracy_power']=='9/10' and l['source_magnitude_saving']=='0'
    for r in l['H_exponents']:assert Q(r['error_power'])==Q(9,10)-3*Q(r['h'])
    rect=d['rectangular_dft']
    assert rect['constant']==1 and Q(rect['relative_gain'])==Q(3,10)
    assert Q(rect['full_rectangle_after_denominator_sum_exponent'])==Q(4,5)
    assert Q(rect['illegally_subtracted_strip_exponent'])==Q(1,10)-Q(3,10)==-Q(1,5)
    assert not rect['exact_strip_transfer_proved']
    v=d['vaughan'];assert v['proper_power_compensation_retained'] and not v['prime_indicator_kept_on_typeii_factors']
    assert v['prime_only_formal_log_sha256']==formal_check(v['limit'],v['U'],v['V'])
    mask=d['mask_completion'];r=mask['example_modulus']
    assert r==1009 and mask['positive_residues']==[1]
    assert (mask['cancelled_frequency_index']+1)%r==0 and mask['zero_frequency_coefficient_nonzero']
    assert all(r%p for p in range(2,int(r**.5)+1))
    # Reconstruct the completed mask at EVERY residue using exact root-of-unity
    # exponent counts. For n!=1 the exponents cover all residues and sum to 0;
    # for n==1 the resulting polynomial is r*zeta before dividing by r.
    for n in range(r):
        exponents=[((n-1)*a+n)%r for a in range(r)]
        if n==1:assert exponents==[1]*r
        else:assert len(set(exponents))==r
    t=d['toy_envelope'];M=t['M'];X=t['X'];U=t['U'];V=t['V']
    assert X==M**5 and U==X*V==M**8 and V==M**3>=2000
    assert Q(t['lower_prefactor'])==Q(t['cosine_lower'])/4000 and Q(t['absolute_growth_exponent'])==Q(1,10)
    assert sum(v//1000 for v in range(V,2*V))>=Q(V*V,2000)
    assert 1-Q(1,50)**2/2==Q(t['cosine_lower'])
    for p,pin in d['source_pins'].items():assert sha256((ROOT/p).read_bytes()).hexdigest()==pin['sha256']
if __name__=='__main__':
    d=json.loads((ROOT/'notes/WP84_CUBIC_FIRST_ALIAS_TYPEII_CERTIFICATE.json').read_text());verify(d)
    changes=[('carrier_retained',False),('source_masks_retained',False),('window_covariance_substitution',True),
             ('power_saving_on_actual_window','3/10'),('constant_signed_saving','1/1000'),('strict_gt79_proved',True)]
    mutants=[]
    for k,v in changes:m=deepcopy(d);m[k]=v;mutants.append(m)
    for group,key,val in [('rectangular_dft','exact_strip_transfer_proved',True),
                          ('vaughan','proper_power_compensation_retained',False),
                          ('mask_completion','zero_frequency_coefficient_nonzero',False),
                          ('linearization','source_magnitude_saving','9/10')]:
        m=deepcopy(d);m[group][key]=val;mutants.append(m)
    for m in mutants:
        try:verify(m)
        except AssertionError:pass
        else:raise AssertionError('hostile promotion accepted')
    print('PASS formal-log Vaughan identity through 192, source exponent tables, exact mask-zero mode, coherent envelope falsifier and 10 hostile mutations')
