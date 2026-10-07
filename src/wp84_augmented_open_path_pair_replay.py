"""Independent replay: integer defect convolutions, rational lower bound and frozen SOS."""
from pathlib import Path
from fractions import Fraction as F
from math import factorial
from copy import deepcopy
import json
ROOT=Path(__file__).resolve().parents[1]
def check(c):
    for b in (5,6):
        for R in (1,2):
            rows=c['defect_counts_per_prime_before_endpoint_mask'][str(b)][str(R)]
            slots=(b+2)*(b+1)//2
            for d in range(-2*R,2*R+1):
                n=sum(1 for v in range(-R,R+1) if -R<=-d-v<=R)
                assert rows[str(d)]==2*slots*n
            assert sum(rows.values())==2*slots*(2*R+1)**2
    # Separate rational trigonometric envelope calculation.
    M1=F(7,1152);M2=F(7,288);f1=F(49,7744);f0=F(4,9);cos=F(3407,3528)
    lo=cos*(f1*M1)**2*(f0*M2)**2/2
    assert lo==F(c['positive_population']['open_marked_population_liminf_lower']) and lo>0
    w=c['witness'];a=list(map(F,w['q_coefficients']));p=[sum(a[i]*a[j] for i in range(5) for j in range(5) if i+j==k) for k in range(9)]
    assert p==list(map(F,w['p_coefficients'])) and p[4]==0
    m=list(map(F,w['relaxed_completion_moments']));E=sum(p[i]*m[i] for i in range(9))
    assert E==F(w['expectation']);assert F(c['uncharged_defect_slack'])==F(21,200)-E
    var=2*abs(p[2])*F(106,333)**2/6000
    assert F(c['partial_variance_payment'])==var
    assert F(c['relaxed_slack_after_variance_only'])==F(21,200)-E-var
    high=c['incidence']['higher_word'];paths=[0]
    for p,e,l in high:paths.append(paths[-1]+l)
    assert paths[-1]==0 and max(paths)-min(paths)==2
    defects=[]
    for i in range(len(high)):
        for j in range(i+1,len(high)):
            if high[i][0]==high[j][0] and high[i][1]==-high[j][1]:defects.append(-high[i][2]-high[j][2])
    assert defects==c['incidence']['deletion_defects']==[-2,2,0,0]
    assert c['intersection']=='NOT YET CERTIFIABLE' and c['mu7_mu8']=='NO-GO'
c=json.loads((ROOT/'notes/WP84_AUGMENTED_OPEN_PATH_PAIR_CERTIFICATE.json').read_text());check(c)
for kind in range(3):
    bad=deepcopy(c)
    if kind==0:bad['defect_counts_per_prime_before_endpoint_mask']['5']['1']['2']+=1
    if kind==1:bad['positive_population']['open_marked_population_liminf_lower']='0'
    if kind==2:bad['uncharged_defect_slack']='1'
    try:check(bad)
    except AssertionError:pass
    else:raise AssertionError('corruption accepted')
print('PASS independent defect/trace/witness replay; three corruptions rejected')
