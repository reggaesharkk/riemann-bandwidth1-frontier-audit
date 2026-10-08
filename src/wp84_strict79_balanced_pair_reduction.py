"""Exact certificates, not a numerical prime-moment surrogate.

The analytic assertions have proofs and scopes in the companion audit note.
This program enumerates all equality/sign classes and evaluates a Gaussian
pinching LOWER bound on the already proved exact three-pair main term.
"""
from collections import Counter
from fractions import Fraction as F
from hashlib import sha256
from itertools import product
from math import lcm
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT/'notes/WP84_STRICT79_BALANCED_PAIR_CERTIFICATE.json'
PARENT = '06e51fbdb4150d2dbbbb4ddda6097575d9d2dcfa'

def partitions(n):
    words = [(0,)]
    for _ in range(n-1):
        words = [w+(j,) for w in words for j in range(max(w)+2)]
    return words

def classify(pi, eps):
    sizes = [pi.count(k) for k in range(max(pi)+1)]
    sums = [sum(eps[i] for i in range(len(pi)) if pi[i]==k) for k in range(len(sizes))]
    shape = sorted(sizes)
    if max(sizes)>=3 and sizes.count(1)<=2: return 'prior_closed'
    if all(v==2 for v in sizes):
        return 'exact_pair_main' if all(v==0 for v in sums) else 'prior_closed'
    if shape==[1,2,2]: return 'prior_closed'
    if shape==[1,1,2,2]:
        return 'new_unconditional_degree_two' if all(sums[k]==0 for k,v in enumerate(sizes) if v==2) else 'new_orientation_summed_self_bound'
    if shape==[1,1,1,3]: return 'new_orientation_summed_self_bound'
    if 2 in sizes:
        k = sizes.index(2)
        return 'surviving_balanced_pair' if sums[k]==0 else 'new_orientation_summed_self_bound'
    return 'surviving_all_distinct'

def census(n):
    count = Counter(); rows = []
    for pi in partitions(n):
        for eps in product((-1,1), repeat=n):
            tag = classify(pi,eps); count[tag]+=1
            rows.append([list(pi),list(eps),tag])
    return {'degree':n,'counts':dict(sorted(count.items())),
            'class_count':len(rows),'sha256':sha256(json.dumps(rows,separators=(',',':')).encode()).hexdigest()}

def matchings(xs):
    if not xs: yield (); return
    for j in range(1,len(xs)):
        for rest in matchings(xs[1:j]+xs[j+1:]):
            yield ((xs[0],xs[j]),)+rest

def covariance(e,f):
    i,j=e; k,l=f
    if i==j and k==l:
        return (0,F(1,6)) if i==k else (1,-F(1,2*(i-k)**2))
    if i==j or k==l: return (0,F(0))
    return (1,F(int(i==k)-int(i==l)-int(j==k)+int(j==l),4*(j-i)*(l-k)))

def direct_pair_polynomial(m=9):
    edges=[(i,j) for i in range(m) for j in range(i,m)]
    ids={e:k for k,e in enumerate(edges)}
    cov={(i,j):covariance(e,f) for i,e in enumerate(edges) for j,f in enumerate(edges)}
    den=lcm(*(v.denominator for _,v in cov.values()))
    tab={(i,j):(d,int(v*den)) for (i,j),(d,v) in cov.items()}
    pairing=list(matchings(tuple(range(6)))); totals=[0]*4
    for walk in product(range(m),repeat=6):
        es=[ids[tuple(sorted((walk[j],walk[(j+1)%6])))] for j in range(6)]
        for pairs in pairing:
            degree=0; val=1
            for a,b in pairs:
                d,v=tab[es[a],es[b]]; degree+=d;val*=v
                if not val: break
            if val: totals[degree]+=val
    return [F(v,m*den**3) for v in totals]

def evaluate(p,x): return sum(v*x**j for j,v in enumerate(p))

def build():
    previous=json.loads((ROOT/'notes/WP84_STRICT79_SOURCE_MATCHED_REDUCTION_CERTIFICATE.json').read_text())
    p=direct_pair_polynomial()
    lower=evaluate(p,F(7,22)**2)
    A=F(11501,12500);B=F(137641,250000)
    cap=F(64788151489666079,572357731837500000)
    paths=['notes/WP84_STRICT79_SOURCE_MATCHED_ARITHMETIC_REDUCTION.md',
           'notes/WP84_STRICT79_SOURCE_MATCHED_REDUCTION_CERTIFICATE.json',
           'notes/WP84_NON_GAUSSIAN_C5_C6_FIRST_STRIKE.md',
           'notes/WP84_PNT_PRIME_SQUARE_MEASURE_UPGRADE.md',
           'notes/WP84_GOOD_ENDPOINT_TRIMMING.md',
           'src/wp84_repaired_open_diagonal.py']
    pins={p:{'sha256':sha256((ROOT/p).read_bytes()).hexdigest(),
             'git_blob':subprocess.check_output(['git','rev-parse',PARENT+':'+p],cwd=ROOT,text=True).strip()} for p in paths}
    return {'input_head':PARENT,'R':6000,'cutoff':'floor(exp(L-sqrt(L))), L=log(T/(2*pi))',
            'original_masks':True,'alias_carrier_retained':True,'proper_powers_retained_before_gate_reduction':True,
            'scope':'complete orientation-summed populations; never individual sign or frequency masks',
            'census':[census(5),census(6)],
            'constants':{'A':str(A),'B':str(B),'Jstar':str(cap),
                         'frozen_reference_margin':str(F(52897896569489,572357731837500000))},
            'gaussian_pinching':{'block_size':9,'purpose':'lower bound on exact Pair6_6000 only; no prime-row model',
                                 'x':'1/pi^2','coefficients':list(map(str,p)),
                                 'pi_lower':'333/106','pi_upper':'22/7','lower':str(lower),
                                 'required_negative_residual_at_least':str(B*lower-cap),
                                 'upper_bound_on_full_Pair6':False},
            'self_bound':{'error':'e_T*(1+(J_full+C)^(2/3)), e_T -> 0',
                          'young':'e*U^(2/3) <= U/2 + 16*e^3/27',
                          'sixth_bound_unconditional':False,'bounded_gate_equivalence_proved':True},
            'arithmetic_inequality_12_proved':False,'strict_gt79_proved':False,
            'new_signed_saving_proved':False,'source_pins':pins,'packet_sha256':previous['packet_sha256']}

if __name__=='__main__':
    data=build();OUT.write_text(json.dumps(data,indent=2)+'\n',encoding='utf-8')
    for c in data['census']: print(c)
    print('Pair lower:',data['gaussian_pinching']['lower'])
    print('Necessary negative residual:',data['gaussian_pinching']['required_negative_residual_at_least'])
