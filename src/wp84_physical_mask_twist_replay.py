"""Independent character/Mobius/norm replay and actual prime-matrix regression."""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
from math import factorial,pi,log,sqrt
from copy import deepcopy
import numpy as np,json
ROOT=Path(__file__).resolve().parents[1]
def rgs(n):
    def rec(a):
        if len(a)==n:yield a;return
        for j in range(max(a)+2):yield from rec(a+[j])
    yield from rec([0])
def norm(n):
    total=0
    for a in rgs(n):
        mu=1
        for b in range(max(a)+1):mu*=factorial(a.count(b)-1)
        total+=mu
    return total
c=json.loads((ROOT/'notes/WP84_PHYSICAL_MASK_TWIST_CERTIFICATE.json').read_text())
def check(c):
    for n in (2,3,4):assert norm(n)==int(c['distinctness_mobius_norms'][str(n)])==factorial(n)
    ex=c['Delta_only_counterexample'];M,C=ex['M'],ex['competitor']
    assert -(M[0][2]+M[1][2])==-(C[0][2]+C[2][2])==-2
    assert [v[2] for v in M]!=[v[2] for v in C]
    assert ex['character_measurement_rank']==1 and ex['mask_augmented_rank']==2
    w=json.loads((ROOT/'notes/WP84_FULL_PAIR_TRANSFER_OPERATOR_AND_DEGREE8_CERTIFICATE.json').read_text())['SOS_witness'];c7=F(w['p_coefficients'][7]);B=F(14157,2401);pair=F(343,8921088)
    Chard=24*2*B/pair/abs(c7)
    assert F(c['hard_trimmed_inverse_norm_bound_consumer_scaled'])==Chard
    assert F(c['uniform_aux_error_needed_for_ideal_comparison'])==F(c['degree6_ideal_slack_comparison_only'])/Chard
    assert F(c['raw_order7_mask_norm_bound'])==24
    assert F(c['uniform_aux_error_needed_for_relaxed_comparison'])==F(c['degree6_relaxed_slack_comparison_only'])/Chard
    # Separate Taylor certificate with a different truncation from the producer.
    def exp_interval(x):
        x=F(x);v=sum((x**n/F(factorial(n)) for n in range(61)),F(0))
        tail=x**61/F(factorial(61))/(1-x/62)
        return v,v+tail
    assert exp_interval(F(5,4))[1]<5<exp_interval(F(5,3))[0]
    assert exp_interval(F(11,2))[1]<379<401<exp_interval(F(13,2))[0]
    assert exp_interval(F(7,2))[1]<47<61<exp_interval(F(9,2))[0]
    assert exp_interval(6)[0]>401 and exp_interval(10)[1]<22027
    assert F(44,7)*22027*F(28,151951)<32
    assert c['paid_degree8_budget']=='UNCERTIFIED'
check(c)
for field in ('raw_order7_mask_norm_bound','hard_trimmed_inverse_norm_bound_consumer_scaled'):
    bad=deepcopy(c);bad[field]='0'
    try:
        check(bad);assert F(bad['raw_order7_mask_norm_bound'])==24
    except AssertionError:pass
    else:raise AssertionError('corruption accepted')
# Matrix assembled from actual ordinary-prime Dirichlet coefficients, same filters.
L,T=7.,13.;I=tuple(range(2,6));R=1;A=np.zeros((4,4),complex)
for p in (2,3,5):
    alpha=log(p)/L;cp=-log(p)/(L*sqrt(p))
    for e in (-1,1):
        for i,r in enumerate(I):
            for j,t in enumerate(I):
                l=t-r
                if abs(l)>R:continue
                f=1-alpha if l==0 else (1-np.exp(e*2j*pi*l*alpha))/(e*2j*pi*l)
                A[i,j]+=cp*f*np.exp(1j*e*(T+2*pi*r/L)*log(p))
assert np.max(abs(A-A.conj().T))<1e-13
q=5;Delta=1;values=[]
for k in range(q):
    theta=2*pi*k/q;Q=np.diag(np.exp(1j*theta*np.array(I)));B=Q@A@Q.conj().T
    values.append(np.trace(B@B@A@A)/4)
project=sum(z*np.exp(-2j*pi*k*Delta/q) for k,z in enumerate(values))/q
explicit=0j
for i,j,k,l in product(range(4),repeat=4):
    defect=-((I[j]-I[i])+(I[k]-I[j]))
    if defect==Delta:explicit+=A[i,j]*A[j,k]*A[k,l]*A[l,i]/4
assert abs(project-explicit)<1e-13
Q=np.diag(np.exp(0.37j*np.array(I)))
assert abs(np.trace(np.linalg.matrix_power(Q@A@Q.conj().T,4))-np.trace(np.linalg.matrix_power(A,4)))<1e-12
print('PASS independent exact masks/norms, two corruptions; actual-prime matrix identities numerical regression only')
