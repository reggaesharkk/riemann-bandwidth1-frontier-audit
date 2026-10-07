"""Independent Fraction LDL/Schur replay; rejects deliberate certificate corruption."""
from fractions import Fraction as F
from pathlib import Path
from copy import deepcopy
import json
ROOT=Path(__file__).resolve().parents[1]
def solve(M,v):
    a=[list(r)+[v[i]] for i,r in enumerate(M)];n=len(v)
    for i in range(n):
        pivot=a[i][i];assert pivot
        a[i]=[x/pivot for x in a[i]]
        for j in range(n):
            if j!=i:
                t=a[j][i];a[j]=[x-t*y for x,y in zip(a[j],a[i])]
    return [r[-1] for r in a]
def dot(a,b):return sum(x*y for x,y in zip(a,b))
def replay(c):
    m=list(map(F,['1','0','1/3','0','1/4','1/36','157/630']))
    H=[[m[i+j] for j in range(4)] for i in range(4)]
    # Independent LDL positivity, without Sympy.
    K=deepcopy(H)
    for i in range(4):
        assert K[i][i]>0
        for j in range(i+1,4):
            for k in range(i+1,4):K[j][k]-=K[j][i]*K[i][k]/K[i][i]
    a=[F(x,117559) for x in (-449,-1128,-12720,14400)];t=F(144000,117559)
    def val(z):
        h=m[4:]+[z];return dot(a,[dot(row,a) for row in H])+2*t*dot(a,h)+t*t*dot(h,solve(H,h))
    f0=val(F(0));fp=val(F(1));fm=val(F(-1));quad=(fp+fm)/2-f0;lin=(fp-fm)/2
    z=-lin/(2*quad);lo=val(z)
    mc=c['moment_certificate']
    assert F(mc['lower_bound'])==lo
    assert F(mc['completion_mu7_minimizer'])==z
    assert F(mc['square_coefficient'])==quad
    assert F(mc['percentage_upper_bound'])==100*(1-2*lo)
    assert lo>F(21,200)
    for n,bell in ((7,877),(8,4140)):
        rows=c['partitions'][str(n)];assert sum(x['count'] for x in rows.values())==bell
        # Mobius convolution over partitions of k blocks equals zero for k>1.
        S=[[0]*9 for _ in range(9)];S[0][0]=1
        for i in range(1,9):
            for j in range(1,i+1):S[i][j]=S[i-1][j-1]+j*S[i-1][j]
        from math import factorial
        for k in range(2,n+1):assert sum(S[k][j]*(-1)**(j-1)*factorial(j-1) for j in range(1,k+1))==0
    return lo
c=json.loads((ROOT/'notes/WP84_DEGREE8_PAIR_INSERTION_AND_MODEL_CERTIFICATE.json').read_text());print('Independent lower bound',replay(c))
for field in ('lower_bound','square_coefficient','percentage_upper_bound'):
    bad=deepcopy(c);bad['moment_certificate'][field]=str(F(bad['moment_certificate'][field])+1)
    try:replay(bad)
    except AssertionError:continue
    raise AssertionError('corruption accepted '+field)
bad=deepcopy(c);next(iter(bad['partitions']['8'].values()))['count']+=1
try:replay(bad)
except AssertionError:pass
else:raise AssertionError('partition corruption accepted')
print('PASS: independent replay and four deliberate corruptions rejected')
