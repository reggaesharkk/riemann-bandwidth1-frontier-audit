"""Independent exact replay of census, collision coarsenings, and constants.

No imports from the producer; no synthetic primes/rows or sampled phases.
The analytic prime estimates are proofs in the note, not numerical tests here.
"""
from collections import Counter
from copy import deepcopy
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import subprocess

ROOT=Path(__file__).resolve().parents[1]

def rgs(n):
    # Independent exhaustive restricted-growth words.
    for word in product(range(n),repeat=n):
        if word[0]!=0:continue
        if all(word[i]<=1+max(word[:i]) for i in range(1,n)):yield word

def classify(word,signs):
    groups=[[i for i,v in enumerate(word) if v==j] for j in range(max(word)+1)]
    sizes=[len(g) for g in groups];nets=[sum(signs[i] for i in g) for g in groups]
    if any(v>=3 for v in sizes) and sum(v==1 for v in sizes)<=2:
        return 'closed_absolute_with_linear_L2'
    if len(word)==6 and sorted(sizes)==[2,2,2]:
        if all(v==0 for v in nets):return 'exact_three_pair_main'
        return 'closed_oscillatory_pair_field'
    if len(word)==5 and sorted(sizes)==[1,2,2]:
        return ('closed_single_linear_mean' if all(nets[j]==0 for j,v in enumerate(sizes) if v==2)
                else 'closed_oscillatory_pair_field')
    return 'open_signed_arithmetic'

def canonical(word):
    lookup={};out=[]
    for j in word:
        if j not in lookup:lookup[j]=len(lookup)
        out.append(lookup[j])
    return tuple(out)

def multiply(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,v in enumerate(a):
        for j,w in enumerate(b):out[i+j]+=v*w
    return out

def validate_contract(d):
    assert d['input_head']=='be82c32cc00fce6d1c880ee5a4fe4a1300a194d1'
    assert d['R']==6000 and not d['cutoff_shortened']
    assert d['contract']=={
        'cutoff':'N=floor(exp(L-sqrt(L))), L=log(T/(2*pi))',
        'prime_pool':'all retained prime powers initially; complete ordinary pool after signed-gate equivalence',
        'kernel':'exp(i*T*lambda+2*pi*i*i_min*lambda/L)/dprime * sum_(r=0)^(rho-1) exp(2*pi*i*r*lambda/L)',
        'path':'every ordered closed displacement word, |ell_j|<=6000',
        'aliases':'all aliases and tails retained in the full grid average',
        'proper_powers':'complete signed-gate equivalence only; no per-mask disposal',
        'closure_scope':'global unmasked sums; no independent near/far zero assertion',
        'historical_P_required':False,'historical_unique_selector_required':False,
        'selection':'existential common good section; no invented row data',
        'continuum':'only exact three-pair diagonal after reduction; no sharp substitution',
    }
    assert not d['arithmetic_inequality_12_proved'] and not d['strict_gt79_proved']
    assert not d['rank_promoted'] and not d['new_consumer']
    assert d['section_transfer']['arithmetic_assumption_proved'] is False

def main():
    d=json.loads((ROOT/'notes/WP84_STRICT79_SOURCE_MATCHED_REDUCTION_CERTIFICATE.json').read_text())
    validate_contract(d)
    q=[F(-19101,185500),F(961,3710),F(31,50),F(-371,500)]
    c=multiply(q,q);A=-c[5];B=c[6];v=d['constants']
    assert c[4]==0 and A==F(v['A']) and B==F(v['B'])
    cap=F(21,200)-c[0]-c[2]/3-F(v['band_payment'])-F(v['variance_payment'])
    assert cap==F(v['signed_cap'])==F(64788151489666079,572357731837500000)
    t=F(v['coercive_scale']);C=F(v['coercive_constant'])
    assert 3*B*t==5*A and 6*C==A*t**5 and B*t**6/2==5*C
    assert multiply(list(map(F,v['coercive_factor_1'])),list(map(F,v['coercive_factor_2'])))==list(map(F,v['coercive_polynomial']))
    assert all(j>=0 for j in v['coercive_factor_2'])
    # Exact Holder exponents with the defect in S_(6/(7-b)).
    for b in range(1,6):
        assert F(7-b,6)+F(b-1,6)==1
        assert F(7-b,6)-F(1,6)==F(6-b,6)>0
    rows_checked=0;coarsenings=0
    for cert in d['census']:
        b=cert['degree'];words=list(rgs(b));counts=Counter();rows=[];shapes={};lower_exact=0
        assert len(words)=={5:52,6:203}[b]==cert['partition_count']
        assert [list(w) for w in words]==[p['partition'] for p in cert['per_partition']]
        for word,pc in zip(words,cert['per_partition']):
            size=[word.count(j) for j in range(max(word)+1)];local=Counter()
            shape=','.join(map(str,sorted(size,reverse=True)))
            for signs in product((-1,1),repeat=b):
                tag=classify(word,signs);counts[tag]+=1;local[tag]+=1
                shapes.setdefault(shape,Counter())[tag]+=1
                rows.append([b,list(word),list(signs),tag]);rows_checked+=1
                if tag.startswith('closed_'):
                    if all(sum(signs[i] for i,v in enumerate(word) if v==j)==0 for j in range(max(word)+1)):
                        lower_exact+=1
                    # Every equality correction of the block-distinctness
                    # projector still has a proved small-mass shape.
                    for merged in rgs(max(word)+1):
                        w=canonical(tuple(merged[j] for j in word))
                        assert classify(w,signs).startswith('closed_')
                        coarsenings+=1
            assert dict(sorted(local.items()))==pc['labels'] and size==pc['multiplicities']
        assert dict(sorted(counts.items()))==cert['classification_counts']
        assert {s:dict(sorted(c.items())) for s,c in sorted(shapes.items())}==cert['shape_counts']
        assert len(rows)==cert['ordered_class_count']
        assert sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()==cert['ordered_classification_sha256']
        assert counts['open_signed_arithmetic']=={5:352,6:5184}[b]
        main=counts['exact_three_pair_main']
        assert main=={5:0,6:120}[b]
        assert sum(v for k,v in counts.items() if k.startswith('closed_'))=={5:1312,6:7688}[b]
        assert lower_exact=={5:0,6:200}[b]==d['already_closed_lower_exact_classes'][str(b)]
        assert sum(v for k,v in counts.items() if k.startswith('closed_'))-lower_exact==d['noncentral_globally_small_ordered_classes'][str(b)]
        surviving_shapes={tuple(sorted([w.count(j) for j in range(max(w)+1)],reverse=True))
                          for w in words if any(classify(w,s)=='open_signed_arithmetic' for s in product((-1,1),repeat=b))}
        assert surviving_shapes=={tuple(s) for s in d['remaining_shapes'][str(b)]}
    for path,pin in d['source_pins'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest()==pin['sha256']
        assert subprocess.check_output(['git','rev-parse',f"{pin['commit']}:{path}"],cwd=ROOT,text=True).strip()==pin['blob']
    for path,want in d['packet_sha256'].items():assert sha256((ROOT/path).read_bytes()).hexdigest()==want
    hostile=0
    mutations=[('R',400),('cutoff_shortened',True),('rank_promoted',True),('arithmetic_inequality_12_proved',True),('strict_gt79_proved',True)]
    for key,value in mutations:
        bad=deepcopy(d);bad[key]=value
        try:validate_contract(bad)
        except AssertionError:hostile+=1
        else:raise AssertionError('unsupported promotion accepted')
    for key in ['kernel','prime_pool','path','aliases','proper_powers','closure_scope','selection','continuum']:
        bad=deepcopy(d);bad['contract'][key]='unmatched replacement'
        try:validate_contract(bad)
        except AssertionError:hostile+=1
        else:raise AssertionError('source mutation accepted')
    print(f'PASS {rows_checked} source sign/equality classifications; {coarsenings} collision coarsenings; exact coercivity/Holder/budget checks')
    print(f'PASS {hostile} hostile mutations and immutable source/packet hashes')
    print('NEW ANALYTIC REMOVALS proved in note; remaining signed arithmetic bound and strict >79 OPEN')

if __name__=='__main__':main()
