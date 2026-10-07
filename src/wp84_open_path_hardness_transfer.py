"""Exact projection factorization test and complete signed population index ledger."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
import json,subprocess
from wp84_full_pair_transfer_degree8 import carrier,offsets,marked_deletions,admissible
from wp84_repaired_open_diagonal import diagonal
ROOT=Path(__file__).resolve().parents[1]
def closed_lag_count(n,R):
    counts={0:1}
    for _ in range(n):
        nxt={}
        for d,v in counts.items():
            for l in range(-R,R+1):nxt[d+l]=nxt.get(d+l,0)+v
        counts=nxt
    return counts.get(0,0)
def ledger(b,R):
    # Distinct lower prime labels/signs; inserted prime outside all lower windows.
    total=closed_lag_count(b+2,R)
    closed_delete=(2*R+1)*closed_lag_count(b,R)
    open_lags=total-closed_delete
    arrangements=factorial(b+2) # pair +/- leaves are separately labelled.
    return {'lower_order':b,'R':R,'closed_lags':total,'closed_delete_lags_per_position':closed_delete,'open_delete_lags_per_position':open_lags,'leaf_arrangements':arrangements,'open_resolved_channels_before_root_mask':arrangements*open_lags,'pair_multiplicity':1,'raw_cumulant_coefficient':1,'coefficient_phase':'complex; real sign cannot be assigned before path/carrier summation'}
def certificate():
    lower=((379,1,0),(401,1,0),(47,-1,0),(53,-1,0),(61,-1,0))
    A=((5,1,1),(5,-1,1))+tuple((p,e,-1 if j in (0,2) else 0) for j,(p,e,l) in enumerate(lower))
    B=((5,1,-1),(5,-1,-1))+tuple((p,e,1 if j in (0,2) else 0) for j,(p,e,l) in enumerate(lower))
    assert carrier(A)==carrier(B)==carrier(lower)
    assert admissible(A,5,(0,30),1) and admissible(B,5,(0,30),1)
    assert len(list(marked_deletions(A)))==len(list(marked_deletions(B)))==1
    # Contributions include all filter/root factors in amplitude coordinates.
    # A and B put mass on the SAME carrier/root atom. Aggregation S=[1,1].
    S=[F(1),F(1)];P=[F(1),F(0)];v=[F(1),F(-1)]
    assert sum(a*b for a,b in zip(S,v))==0 and sum(a*b for a,b in zip(P,v))==1
    pair_lo=F(343,8921088);Mlo=F(49,99)*F(49,143)
    inverse=2/(pair_lo*Mlo)
    c={'decision':'E','parent':'cb3c859958ce9ae75d976ec911193465a39a03be','same_carrier_states':{'M':A,'non_M':B,'root':5,'section':[0,30]},'kernel_dual_certificate':{'aggregation':[1,1],'mask':[1,0],'vector':[1,-1],'aggregated_mass':0,'masked_mass':1,'scope':'free resolved amplitude space; not a realizable arithmetic cancellation asserted'},'population_ledger':[ledger(b,R) for b in (5,6) for R in (0,1,2)],'pair_limit_lower':str(pair_lo),'filter_multiplier_lower':str(Mlo),'eventual_resolved_TV_inverse_bound':str(inverse),'projection_on_resolved_TV':'bounded','projection_on_aggregated_carrier_primitive':'does not factor on free resolved space','actual_prime_weight_restricted_bound':'UNCERTIFIED','R1_open_diagonal':[str(v) for v in diagonal(1)],'R6000_diagonal':'same exact fixed-R covariance formula; not evaluated','paid_budget':'UNCERTIFIED','mu7_mu8':'NOT COMPUTED','strict_gt79':'OPEN'}
    files=['src/wp84_repaired_open_signed_arithmetic.py','src/wp84_repaired_open_diagonal.py','notes/WP84_REPAIRED_OPEN_PATH_SIGNED_ARITHMETIC.md']
    c['source_blobs']={p:subprocess.check_output(['git','rev-parse','cb3c859:'+p],cwd=ROOT,text=True).strip() for p in files}
    return c
if __name__=='__main__':
    c=certificate();(ROOT/'notes/WP84_OPEN_PATH_HARDNESS_TRANSFER_CERTIFICATE.json').write_text(json.dumps(c,indent=2)+'\n')
    print('PASS exact carrier/observable kernel certificate; Decision E')
    print(c['population_ledger'])
