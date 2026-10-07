"""Exact unique-factorization carrier grouping and interval/support certificate."""
from itertools import product
from fractions import Fraction as F
from math import prod
from pathlib import Path
import json
ROOT=Path(__file__).resolve().parents[1]

def exponent_key(labels,signs,primes):
    return tuple(sum(e for p,e in zip(labels,signs) if p==q) for q in primes)
def carrier_ratio(labels,signs):
    return F(prod(p for p,e in zip(labels,signs) if e==1),prod(p for p,e in zip(labels,signs) if e==-1))
def main():
    primes=(2,3,5);sets={};counts={}
    for b in (5,6):
        keys={};count=0
        for choices in product(tuple((p,e) for p in primes for e in (-1,1)),repeat=b):
            labels,signs=zip(*choices);key=exponent_key(labels,signs,primes)
            ratio=carrier_ratio(labels,signs)
            assert sum(abs(t) for t in key)%2==b%2
            if ratio in keys:assert keys[ratio]==key
            keys[ratio]=key;count+=1
        sets[b]=set(keys);counts[b]={'ordered_signed_tuple_count':count,'exact_ratio_class_count':len(keys),
                                    'zero_frequency_present':F(1) in keys}
    assert not sets[5]&sets[6]
    # Proper powers are essential to the scope of the no-common-carrier theorem.
    r5=carrier_ratio((4,3,5,7,11),(1,-1,1,-1,1))
    r6=carrier_ratio((2,2,3,5,7,11),(1,1,-1,1,-1,1))
    assert r5==r6==F(220,21)
    # Reciprocals preserve degree parity, as do all signed configurations.
    assert all(1/r in sets[b] for b in (5,6) for r in sets[b])
    out={'parent':'c402000ac35b9d06c05f7981d9c3ece7bde35807','decision':'D',
         'theorem':'ordinary prime leaf count b implies Omega(A_reduced)+Omega(B_reduced) congruent b mod 2',
         'proof':'b=sum_p(r_p+s_p); reduced mass=sum_p abs(r_p-s_p)=b-2 sum_p min(r_p,s_p)',
         'ordinary_common_fifth_sixth_carrier_classes':[],
         'ratio_interval_certificate':{'common_domain':'EMPTY EXACTLY','fifth_only_A6':'0',
             'rho_on_fifth_only':'undefined; denominator zero','rho_on_sixth_only':'0 when A6 nonzero',
             'common_real_concentration_claim':'inapplicable'},
         'enumeration':counts,'proper_power_raw_counterexample_ratio':str(r5),
         'proper_power_raw_common_classes_can_exist':True,
         'proper_power_deletion_scope':'complete bounded signed-gate equivalence, not per-class L1 smallness',
         'aliases_change_exact_frequency':True,
         'phase_uniform_TV_identity':'|c5| TV(A5)+c6 TV(A6) for c6>=0; no cross-degree carrier cancellation',
         'phase_uniform_counting_L2_identity':'c5^2 ||A5||2^2+c6^2 ||A6||2^2',
         'true_complex_dual_lower_bound_obtained':False,'strict_gt79':False,
         'consumer_search_stopped_at_gate_2':True,'order8_optimization_performed':False}
    (ROOT/'notes/WP84_CARRIER_AWARE_EXACT_GROUPING_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n')
    (ROOT/'notes/WP84_CARRIER_AWARE_RATIO_INTERVAL_CERTIFICATE.json').write_text(json.dumps(out['ratio_interval_certificate'],indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
