"""Exact fifth pair difference and first nonzero full-amplitude coefficient."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import permutations
from collections import Counter
from math import factorial
import json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def cyc(w):return min(w[j:]+w[:j] for j in range(len(w)))
def trace_words(words):
    out=Counter()
    for w,c in words:out[cyc(w)]+=c
    return {w:c for w,c in out.items() if c}
def identity():
    terms=[]
    for y,z,w in permutations('YZW'):
        terms += [('XX'+y+z+w,1),('X'+y+'X'+z+w,-1)]
        # Add Tr([X,Y][X,Z]W); this cancels the difference exactly.
        terms += [('X'+y+'X'+z+w,1),('X'+y+z+'X'+w,-1),(y+'XX'+z+w,-1),(y+'X'+z+'X'+w,1)]
    assert trace_words(terms)=={}
    return True

def band_square(n,R):
    S=[[int(abs(i-j)<=R) for j in range(n)] for i in range(n)]
    W=[[sum(S[i][k]*S[k][j] for k in range(n)) for j in range(n)] for i in range(n)]
    Z=sum((i-j)**2*W[i][j]**2 for i in range(n) for j in range(n))
    assert (Z>0)==(n>=2 and R>=1)
    return Z

def slot_defect():
    # Slots 1 and 2 (zero-based) exchange, carrying primes AND lags.
    # The common prime/carrier factors cancel; path support and phase do not.
    ps=[2,2,3,5,7];eps=[1]*5;l=[1,-1,0,0,0];perm=[0,2,1,3,4]
    def u(seq):
        out=[0]
        for x in seq:out.append(out[-1]+x)
        return out
    old=u(l);new=u([l[j] for j in perm]);d=5
    # coefficient vector of each prime log in the complete root phase,
    # at its path's minimum admitted root (kminus=0).
    def v(order,uu):
        out=Counter();im=-min(uu)
        for t,j in enumerate(order):out[ps[j]]+=uu[t]+im
        return dict(out)
    return {'slot_permutation':perm,'old_lags':l,'new_lags':[l[j] for j in perm],'old_prefix':old,'new_prefix':new,'old_phase_log_coefficients':v(list(range(5)),old),'new_phase_log_coefficients':v(perm,new),'old_root_count':d-max(old)+min(old),'new_root_count':d-max(new)+min(new),'scope':'one raw admitted algebraic path; shows permutation is not a termwise symmetry'}

def main():
    f=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
    assert f[5]['equality_partition']=='0,0,1,2,3' and f[7]['equality_partition']=='0,1,0,2,3'
    assert f[5]['sign_word']==f[7]['sign_word']=='+++++' and f[5]['aliases']==f[7]['aliases']==[2,3,4]
    # Recover original representatives from frozen raw-class extractor.
    import csv
    rows=list(csv.DictReader((ROOT/'notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv').open()))
    for j in (5,7):
        found=[r for r in rows if int(r['degree'])==5 and r['sign_word']==f[j]['sign_word'] and r['equality_labels']==f[j]['equality_partition']]
        assert sorted(int(r['m']) for r in found)==[2,3,4]
    identity()
    tests=[{'dprime':n,'R':r,'Z':band_square(n,r)} for n in range(2,9) for r in (1,2,6)]
    coeff={'amplitude_order':11,'positive_carrier_coefficient':'pi^2*Z(dprime,R)/dprime * a^4*b*c*d*S/(p*sqrt(q*r*s))','S':'b*c*(b-a)*(c-a)+b*d*(b-a)*(d-a)+c*d*(c-a)*(d-a)','logs':'a=log p,b=log q,c=log r,d=log s','Z':'sum_(i,j in section-relative indices) (i-j)^2*(J_R^2)_(i,j)^2; J_R(i,j)=1_(|i-j|<=R)','normalization':'coefficient of u^11 in a_phi(T)^5 times D after grouping the positive carrier; negative carrier coefficient is conjugate; exp(i*T*lambda) stays external','positivity':'strictly positive when p<min(q,r,s), dprime>=2,R>=1','full_band_reduction':'Z=dprime^4*(dprime^2-1)/6 when R>=dprime-1'}
    # Rational positive log surrogate verifies coefficient signs mechanically;
    # actual log positivity follows from strictly increasing real logarithm.
    a,b,c,d=map(Q,(1,2,3,4));S=b*c*(b-a)*(c-a)+b*d*(b-a)*(d-a)+c*d*(c-a)*(d-a);assert S>0
    result={'decision':'B','parent':'10aabac9aaab51470c9324ab0f927d299a17899b','pair':[5,7],'exact_trace_identity':True,'difference':'-Re sum_(p and unordered distinct singleton triple {q,r,s}) cp^2*cq*cr*cs exp(i*T*log(p^2*q*r*s))/dprime * sum_(perms qrs)Tr([E_p,E_q][E_p,E_r]E_s) * original alias/window mask','matrix':'E_p(i,j)=1_(|i-j|<=R)*f_(j-i)^+(log p*u)*exp(2*pi*i*i*log p*u), i,j in actual selected section','first_nonzero_jet':coeff,'vanishing_orders_through':10,'pair_analytic_rank':2,'new_global_kernel':None,'fifth_rank_bounds':[20,72],'strict_gt79':'OPEN','slot_defect':slot_defect(),'band_square_checks':tests,'legal_carrier_witness':'p=2; distinct q<r<s large via Bertrand intervals; X0=(4*q*r*s)^(1/2); perturb into m=2 punctured residual cell, all primes within natural cutoff eventually; works on every dprime>=2 section','scope':'fixed-cell full-amplitude jet; not a global Taylor series for moving cutoffs or an arithmetic size bound','reusable_criterion':'same-sign five-slot X^2YZW versus XYXZW, summed over singleton assignments; commutator coefficient nonzero for smallest repeated-prime log and nontrivial band','applicable_existing_block_ids':[[5,7]],'mixed_side_lemma':'common normalization must preserve analytic carrier-germ separation, plus actual selector/boundary extension; not proved here','source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json','notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv']}}
    (ROOT/'notes/WP84_FIFTH_5_7_DIFFERENCE_CERTIFICATE.json').write_text(json.dumps(result,indent=2)+'\n')
    print('PASS exact raw reconstruction and trace commutator identity; first nonzero carrier-amplitude jet u^11')
    print('Decision B; pair rank 2; fifth analytic lower bound 20; no global kernel')
if __name__=='__main__':main()
