"""Exact direct signed gate, exponent cells, prime identities and soft-norm falsifier."""
from pathlib import Path
from fractions import Fraction as F
from math import comb
from itertools import product
import json,csv,sympy as s
ROOT=Path(__file__).resolve().parents[1]
def scalar_conv(a,b,N):
    out=[0]*(N+1)
    for i in range(1,N+1):
        if not a[i]:continue
        for j in range(1,N//i+1):out[i*j]+=a[i]*b[j]
    return out
def vector_conv(a,b,N):
    out=[{} for _ in range(N+1)]
    for i in range(1,N+1):
        if not a[i]:continue
        for j in range(1,N//i+1):
            for p,v in b[j].items():out[i*j][p]=out[i*j].get(p,0)+a[i]*v
    return [{p:v for p,v in row.items() if v} for row in out]
def add_vectors(terms,N):
    out=[{} for _ in range(N+1)]
    for scale,seq in terms:
        for n in range(1,N+1):
            for p,v in seq[n].items():out[n][p]=out[n].get(p,0)+scale*v
    return [{p:v for p,v in row.items() if v} for row in out]
def identities(N=250,z=7,k=3,U=5,V=7):
    mu=[0]+[int(s.mobius(n)) for n in range(1,N+1)];one=[0]+[1]*N
    log=[{}]+[dict(s.factorint(n)) for n in range(1,N+1)]
    lam=[{}]+[({next(iter(s.factorint(n))):1} if len(s.factorint(n))==1 else {}) for n in range(1,N+1)]
    mz=[mu[n] if n<=z else 0 for n in range(N+1)];delta=[0]*(N+1);delta[1]=1;hb=[]
    for j in range(1,k+1):
        a=delta[:]
        for _ in range(j):a=scalar_conv(a,mz,N)
        for _ in range(j-1):a=scalar_conv(a,one,N)
        hb.append(((-1)**(j-1)*comb(k,j),vector_conv(a,log,N)))
    assert N<=z**k and add_vectors(hb,N)==lam
    ml=[mu[n] if n<=U else 0 for n in range(N+1)];mh=[mu[n] if n>U else 0 for n in range(N+1)]
    ll=[lam[n] if n<=V else {} for n in range(N+1)];lh=[lam[n] if n>V else {} for n in range(N+1)]
    vaughan=add_vectors([(1,vector_conv(ml,log,N)),(-1,vector_conv(scalar_conv(ml,one,N),ll,N)),(1,ll),(1,vector_conv(scalar_conv(mh,one,N),lh,N))],N)
    assert vaughan==lam
    powers=[lam[n] if n>1 and not s.isprime(n) else {} for n in range(N+1)]
    ordinary=add_vectors([(1,vaughan),(-1,powers)],N)
    assert ordinary==[({n:1} if s.isprime(n) else {}) for n in range(N+1)]
    return {'N':N,'HB_k':k,'HB_z':z,'Vaughan_U':U,'Vaughan_V':V,'exact_formal_log_identity':True,'proper_power_compensation_retained':True}
def classify(r,boxes):
    up=sum((b for a,b in boxes[:r]),F(0));um=sum((b for a,b in boxes[r:]),F(0))
    lp=sum((a for a,b in boxes[:r]),F(0));lm=sum((a for a,b in boxes[r:]),F(0))
    if up<lm or um<lp:return 'central_resonance_support_empty'
    if up==lm or um==lp:return 'resonance_boundary'
    if up+um<2:return 'fixed_gap_mean_value_short'
    if lp+lm>2:return 'supercritical_long'
    return 'critical_or_length_transition'
def main():
    A=F(11501,12500);B=F(137641,250000);J=F(64788151489666079,572357731837500000)
    c0=F(364848201,34410250000);c2=F(-26060119,430128125);band=F(128952763,92407500000);var=F(26060119,12734908593750)
    assert J==F(21,200)-c0-c2/3-band-var
    ideal=J+A/F(36)-B*F(157,630);relaxed=J+A/F(36)-B*F(34,135)
    assert ideal==F(27704610381502,17886179119921875) and relaxed==F(52897896569489,572357731837500000)
    bins=[(F(i,4),F(i+1,4)) for i in range(4)];rows=[];counts={}
    for b,r in ((5,2),(6,2),(6,3)):
        counts[str((b,r))]={}
        for box in product(bins,repeat=b):
            label=classify(r,box);counts[str((b,r))][label]=counts[str((b,r))].get(label,0)+1
            rows.append([b,r,*[f'{a}:{v}' for a,v in box],*([''] if b==5 else []),label])
    with (ROOT/'notes/WP84_DIRECT_CORRELATION_EXPONENT_CELLS.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['degree','plus_count','window1','window2','window3','window4','window5','window6','class']);w.writerows(rows)
    # Soft coefficient counterexample: n~m^6,T=m^5,K=floor(m/100).
    m=1000;T=m**5;N0=m**6;K=m//100;lower=F(4999,5000)*(K-1)
    assert F(2*T*(K-1),N0)<F(2,100) and lower>1
    result={'decision':'F','prime_identities':identities(),'A':str(A),'B':str(B),'Jstar':str(J),'ideal_joint_allowance':str(ideal),'relaxed_joint_allowance':str(relaxed),'cell_counts':counts,'cell_scope':'rational exponent geometry, not existence of prime tuples','hard_cell':{'positive_exponents':['3/5','3/5'],'negative_exponents':['2/5','2/5','2/5'],'product_exponent':'6/5','central_shift_exponent_in_Ncell':'1/6','generic_MV_loss_exponent_in_X':'1/5'},'vaughan_balanced_piece':{'U_V_exponent':'1/10','positive_bilinear_lengths':['X^(3/10)','X^(3/10)'],'negative_bilinear_lengths':['X^(1/5)','X^(1/5)'],'grouped_factors':'four-vs-six factor variables; original two-vs-three products','dominance':'NOT CERTIFIED'},'soft_l2_counterexample':{'m':m,'T':T,'Ncell':N0,'cluster_length':K,'each_coefficient_l2_squared':1,'nonexact_real_correlation_lower':str(lower),'scope':'generic arrays only, not prime-compatible or PNT/BV counterexample'},'new_uniform_twist_gain':'NONE CERTIFIED','mu7_mu8':'NOT COMPUTED','strict_gt79':'OPEN'}
    (ROOT/'notes/WP84_DIRECT_SIGNED_CORRELATION_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact Vaughan/HB and prime-power compensation; gate budgets');print('Ideal',float(ideal),'relaxed',float(relaxed));print('Cells',counts)
if __name__=='__main__':main()
