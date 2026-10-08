"""Exact census and constants for a source-matched arithmetic reduction.

No prime pool, root samples, diagnostic matrices, or numerical moments.
Analytic estimates are proved in the companion note; the certificate records
their hypotheses and independently replayable combinatorial/algebraic parts.
"""
from collections import Counter
from fractions import Fraction as Q
from hashlib import sha256
from itertools import product
from pathlib import Path
import json
import subprocess

ROOT=Path(__file__).resolve().parents[1]
PARENT='be82c32cc00fce6d1c880ee5a4fe4a1300a194d1'
OUT=ROOT/'notes/WP84_STRICT79_SOURCE_MATCHED_REDUCTION_CERTIFICATE.json'
INPUTS=[
 'notes/WP84_NON_GAUSSIAN_C5_C6_FIRST_STRIKE.md',
 'notes/WP84_NON_GAUSSIAN_C5_C6_FIRST_STRIKE_CERTIFICATE.json',
 'notes/WP84_FIXED_BAND_WEIGHTED_REPROJECTION.md',
 'notes/WP84_FIXED_R_ARITHMETIC_FILTERED_MOMENT_TRANSFER.md',
 'notes/WP84_DIRECT_SIGNED_RESTRICTED_CORRELATION_ATTACK.md',
 'notes/WP84_CARRIER_AWARE_DEGREE6_CONSUMER.md',
 'notes/WP84_SIGNED_NEAR_ALIAS_ATTACK.md',
 'notes/WP84_SIGN_BALANCE_NEAR_RESONANCE_GATE.md',
 'notes/WP84_FIXED_BAND_LOWER_MOMENT_COLLAPSE.md',
 'notes/WP84_SOURCE_JET_INTERTWINING_CERTIFICATE.json',
]

def partitions(n):
    words=[(0,)]
    for _ in range(1,n):
        words=[(*w,j) for w in words for j in range(max(w)+2)]
    return sorted(words)

def label(pi,eps):
    nu=[pi.count(j) for j in range(max(pi)+1)]
    e=[sum(eps[i] for i,j in enumerate(pi) if j==k) for k in range(len(nu))]
    singles=nu.count(1)
    if max(nu)>=3 and singles<=2:return 'closed_absolute_with_linear_L2'
    if all(v==2 for v in nu):
        return 'exact_three_pair_main' if all(v==0 for v in e) else 'closed_oscillatory_pair_field'
    if sorted(nu)==[1,2,2]:
        pair_e=[e[j] for j,v in enumerate(nu) if v==2]
        return 'closed_single_linear_mean' if all(v==0 for v in pair_e) else 'closed_oscillatory_pair_field'
    return 'open_signed_arithmetic'

def census(b):
    counts=Counter(); shapes={}; rows=[]; per_partition=[]
    for pi in partitions(b):
        nu=[pi.count(j) for j in range(max(pi)+1)]
        shape=','.join(map(str,sorted(nu,reverse=True)))
        c=Counter()
        for eps in product((-1,1),repeat=b):
            tag=label(pi,eps);counts[tag]+=1;c[tag]+=1
            shapes.setdefault(shape,Counter())[tag]+=1
            rows.append([b,list(pi),list(eps),tag])
        per_partition.append({'partition':list(pi),'multiplicities':nu,'labels':dict(sorted(c.items()))})
    serialized=json.dumps(rows,separators=(',',':')).encode()
    return {'degree':b,'partition_count':len(partitions(b)),
            'ordered_class_count':len(rows),'classification_counts':dict(sorted(counts.items())),
            'shape_counts':{s:dict(sorted(c.items())) for s,c in sorted(shapes.items())},
            'per_partition':per_partition,'ordered_classification_sha256':sha256(serialized).hexdigest()}

def pin(path):
    return {'commit':PARENT,
            'blob':subprocess.check_output(['git','rev-parse',f'{PARENT}:{path}'],cwd=ROOT,text=True).strip(),
            'sha256':sha256((ROOT/path).read_bytes()).hexdigest()}

def build():
    A=Q(11501,12500);B=Q(137641,250000)
    q=[Q(-19101,185500),Q(961,3710),Q(31,50),Q(-371,500)]
    c=[sum((q[j]*q[k-j] for j in range(4) if 0<=k-j<4),Q()) for k in range(7)]
    assert c[4]==0 and c[5]==-A and c[6]==B
    band=Q(128952763,92407500000);var=Q(26060119,12734908593750)
    cap=Q(21,200)-c[0]-c[2]/3-band-var
    assert cap==Q(64788151489666079,572357731837500000)
    t0=5*A/(3*B);C=A*t0**5/6
    previous=json.loads((ROOT/'notes/WP84_SOURCE_JET_INTERTWINING_CERTIFICATE.json').read_text())
    for path,want in previous['packet_sha256'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest()==want
    return {
      'input_head':PARENT,'R':6000,
      'status':'GLOBAL_COLLISION_REDUCTION_AND_ONE_SIDED_SECTION_TRANSFER; SIGNED_ESTIMATE_OPEN',
      'contract':{
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
      },
      'constants':{'A':str(A),'B':str(B),'signed_cap':str(cap),
        'band_payment':str(band),'variance_payment':str(var),
        'coercive_scale':str(t0),'coercive_constant':str(C),
        'coercive_polynomial':[1,0,0,0,0,-6,5],
        'coercive_factor_1':[1,-2,1],'coercive_factor_2':[1,2,3,4,5]},
      'section_transfer':{
        'assumption':'limsup J(Y_full)<=signed_cap-eta, eta>0',
        'sixth_mass_bound':'tau|Y_full|^6 <= 2*(J(Y_full)+C)/B',
        'rank_bound':'rank(Y_full-P*Y_full*P)<=2*r',
        'fifth_error':'10*||Y_full||_(6,d)^5*(2*r/d)^(1/6)',
        'one_sided_gate':'J(Y_I)<=d/dprime * (J(Y_full)+A*fifth_error)',
        'lower_moment_error':'2*b*||Y_full||_(6,d)^b*(2*r/d)^((6-b)/6), b=1,...,5',
        'rate_for_r_over_d_L_minus_half':'O(L^(-1/12)) for the fifth gate term',
        'arithmetic_assumption_proved':False},
      'census':[census(5),census(6)],
      'globally_small_ordered_classes':{'5':1312,'6':7688},
      'noncentral_globally_small_ordered_classes':{'5':1312,'6':7488},
      'already_closed_lower_exact_classes':{'5':0,'6':200},
      'remaining_ordered_classes':{'5':352,'6':5184},
      'remaining_shapes':{'5':[[1,1,1,1,1],[2,1,1,1]],
                          '6':[[1,1,1,1,1,1],[2,1,1,1,1],[2,2,1,1],[3,1,1,1]]},
      'first_missing_higher_arithmetic_estimate':'limsup Re[-A*S5_full+B*S6_full] <= signed_cap-B*Pair6_6000-eta',
      'lower_third_aggregate':'inherited conditional source input; no weighted triple theorem newly proved',
      'arithmetic_inequality_12_proved':False,'strict_gt79_proved':False,
      'rank_promoted':False,'new_consumer':False,'cutoff_shortened':False,
      'source_pins':{p:pin(p) for p in INPUTS},
      'packet_sha256':previous['packet_sha256'],
    }

if __name__=='__main__':
    data=build();OUT.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    for c in data['census']:print(c['degree'],c['classification_counts'])
    print('WROTE exact census/constants; global removal proofs in companion note; actual signed estimate OPEN')
