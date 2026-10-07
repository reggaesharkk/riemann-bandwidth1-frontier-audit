"""Independent UF, complete lag counts, and quotient-dual replay."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import factorial
from copy import deepcopy
import json
ROOT=Path(__file__).resolve().parents[1]
c=json.loads((ROOT/'notes/WP84_OPEN_PATH_HARDNESS_TRANSFER_CERTIFICATE.json').read_text())
def check(c):
    states=c['same_carrier_states'];ratios=[]
    for key in ('M','non_M'):
        w=states[key];ratio=F(1);u=[0]
        for p,e,l in w:
            ratio*=F(p)**e;u.append(u[-1]+l)
        assert u[-1]==0 and all(0<=5+t<=30 for t in u)
        ratios.append(ratio)
    assert ratios[0]==ratios[1]==F(379*401,47*53*61)
    k=c['kernel_dual_certificate'];v=k['vector']
    assert sum(a*b for a,b in zip(k['aggregation'],v))==0
    assert sum(a*b for a,b in zip(k['mask'],v))==1
    assert k['scope']=='free resolved amplitude space; not a realizable arithmetic cancellation asserted'
    for row in c['population_ledger']:
        b,R=row['lower_order'],row['R'];lo=range(-R,R+1)
        total=sum(sum(v)==0 for v in product(lo,repeat=b+2))
        lower=sum(sum(v)==0 for v in product(lo,repeat=b))
        closed_delete=(2*R+1)*lower
        assert row['closed_lags']==total and row['closed_delete_lags_per_position']==closed_delete
        assert row['open_resolved_channels_before_root_mask']==factorial(b+2)*(total-closed_delete)
    C=F(49,7744)*F(7,1152);M=F(49,99)*F(49,143)
    assert F(c['pair_limit_lower'])==C and F(c['filter_multiplier_lower'])==M
    assert F(c['eventual_resolved_TV_inverse_bound'])==2/(C*M)
    assert c['paid_budget']=='UNCERTIFIED' and c['strict_gt79']=='OPEN'
check(c)
for kind in range(3):
    bad=deepcopy(c)
    if kind==0:bad['kernel_dual_certificate']['vector']=[1,0]
    if kind==1:bad['population_ledger'][1]['open_resolved_channels_before_root_mask']+=1
    if kind==2:bad['eventual_resolved_TV_inverse_bound']='1'
    try:check(bad)
    except AssertionError:pass
    else:raise AssertionError('corruption accepted')
print('PASS independent quotient obstruction, full population counts, bounds; three corruptions rejected')
