"""Independent exact replay of SOS/support, Hankel positivity, and channels."""
from fractions import Fraction as F
from math import comb
from pathlib import Path
import json,copy
ROOT=Path(__file__).resolve().parents[1]
def check(c):
    w=c['SOS_witness'];a=list(map(F,w['q_coefficients']));p=[sum(a[i]*a[j] for i in range(5) for j in range(5) if i+j==k) for k in range(9)]
    assert p==list(map(F,w['p_coefficients'])) and p[4]==0
    b=[sum(a[i]*(-1)**i*comb(i,k) for i in range(k,5)) for k in range(5)]
    assert b==list(map(F,w['support_q_minus1_minusy'])) and b[0]==1 and min(b)>=0
    m=list(map(F,w['relaxed_completion_moments']));assert m[:7]==list(map(F,['1','0','1/3','0','1/4','1/36','157/630']))
    A=[[m[i+j] for j in range(5)] for i in range(5)]
    for k in range(5):
        assert A[k][k]>0
        for i in range(k+1,5):
            for j in range(k+1,5):A[i][j]-=A[i][k]*A[k][j]/A[k][k]
    E=sum(p[i]*m[i] for i in range(9));assert E==F(w['expectation']) and E<F(21,200)
    assert 1-2*E==F(w['uncharged_coefficient'])
    ex=c['operator_counterexample'];word=ex['higher_word'];assert sum(t[2] for t in word)==0
    assert sum(t[2] for t in ex['deleted_skeleton'])==-2
    # Independent fixed-consumer Schur optimizer, using the preserved Fraction solver.
    def solve(M,v):
        a=[list(r)+[v[i]] for i,r in enumerate(M)]
        for i in range(len(v)):
            piv=a[i][i];a[i]=[x/piv for x in a[i]]
            for j in range(len(v)):
                if j!=i:
                    r=a[j][i];a[j]=[x-r*y for x,y in zip(a[j],a[i])]
        return [r[-1] for r in a]
    def dot(a,b):return sum(x*y for x,y in zip(a,b))
    H=[[m[i+j] for j in range(4)] for i in range(4)]
    def f(z):
        h=m[4:7]+[z]
        return sum(p[i]*m[i] for i in range(7))+p[7]*z+p[8]*dot(h,solve(H,h))
    f0,fp,fm=f(F(0)),f(F(1)),f(F(-1));A=(fp+fm)/2-f0;B=(fp-fm)/2;z=-B/(2*A)
    opt=c['fixed_consumer_completion_optimum']
    assert F(opt['infimum'])==f(z) and F(opt['mu7_relaxed_optimizer'])==z
    return E
c=json.loads((ROOT/'notes/WP84_FULL_PAIR_TRANSFER_OPERATOR_AND_DEGREE8_CERTIFICATE.json').read_text());print('PASS independent exact witness',check(c))
for key in ('expectation','uncharged_coefficient'):
    bad=copy.deepcopy(c);bad['SOS_witness'][key]=str(F(bad['SOS_witness'][key])+1)
    try:check(bad)
    except AssertionError:pass
    else:raise AssertionError('corruption accepted')
bad=copy.deepcopy(c);bad['SOS_witness']['p_coefficients'][4]='1'
try:check(bad)
except AssertionError:pass
else:raise AssertionError('corruption accepted')
print('PASS three deliberate corruption tests')

