"""Prime/path faithfulness: exact carrier support witnesses and partial ranks."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import csv,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def prime_vector(numbers,signs):
    out=defaultdict(int)
    for n,e in zip(numbers,signs):
        p=2
        while p*p<=n:
            while n%p==0:out[p]+=e;n//=p
            p+=1
        if n>1:out[n]+=e
    return tuple((p,e) for p,e in sorted(out.items()) if e)
def support(v):
    _,a,b=v['pattern'];return min((v['degree'],tuple(a),tuple(b)),(v['degree'],tuple(b),tuple(a)))
def cell_atom_terms(eps,lags,pi,block_primes,kminus,kplus):
    """Full sampled-root/filter normal form of ONE admitted tuple/path.
    Admission masks must be checked from the actual cell by the caller.
    Outputs exact constant-field monomials, not independent field symbols.
    Includes real-part pairing and all roots. No rank inference from output.
    """
    from wp84_full_weight_evaluation_map import expand_filters
    b=len(eps);n=max(pi)+1
    assert len(set(block_primes))==n and len(lags)==b and sum(lags)==0
    nu=[pi.count(j) for j in range(n)]
    e=[sum(eps[i] for i in range(b) if pi[i]==j) for j in range(n)]
    u=[0]
    for l in lags:u.append(u[-1]+l)
    d=kplus-kminus+1;assert d>0
    imin=kminus-min(u);M=max(0,d-max(u)+min(u));out=defaultdict(Q)
    base=[sum(eps[i]*u[i] for i in range(b) if pi[i]==j) for j in range(n)]
    for (zf,af,nh),coef in expand_filters(eps,lags,pi).items():
        for k in range(M):
            rho=tuple(base[j]+(imin+k)*e[j]+zf[j] for j in range(n))
            logs=tuple(nu[j]+af[j] for j in range(n));power=b+sum(af)
            key=(tuple(e),rho,power,logs,tuple(nu),nh)
            out[key]+=Q((-1)**b,2*d)*coef
            neg=(tuple(-v for v in e),tuple(-v for v in rho),power,logs,tuple(nu),nh)
            out[neg]+=Q((-1)**(b+nh),2*d)*coef
    return {k:v for k,v in out.items() if v}

def main():
    funcs=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text());groups=defaultdict(list)
    for v in funcs:groups[support(v)].append(v)
    witnesses=[]
    for key,vs in sorted(groups.items()):
        v=min(vs,key=lambda x:x['id']);pi=list(map(int,v['equality_partition'].split(',')));eps=[1 if x=='+' else -1 for x in v['sign_word']]
        es=[sum(eps[i] for i in range(v['degree']) if pi[i]==k) for k in range(max(pi)+1)]
        ap=sum(max(0,e) for e in es);am=sum(max(0,-e) for e in es)
        m=v['aliases'][0];assert -am<m<ap and m!=0
        t=Q(m+am,ap+am);gamma=[t if e>0 else 1-t if e<0 else Q(1,2) for e in es]
        assert all(0<g<1 for g in gamma) and sum(e*g for e,g in zip(es,gamma))==m
        witnesses.append({'functional_id':v['id'],'b':v['degree'],'reciprocal_carrier_support':key,'equality_partition':pi,'signs':eps,'block_exponents':es,'m':m,'rational_prime_growth_exponents':[str(g) for g in gamma],'prime_constructor':'q_B in [C_B Y^gamma_B, 2 C_B Y^gamma_B], C_B=3^B; Bertrand guarantees primes for large Y; equal gamma intervals disjoint','center':'X_Y=(prod_B q_B^e_B)^(1/m), so log X_Y=log Y+O(1)','cell_witness':'perturb center on one side within H/(2pi X_Y), avoid finite combinatorial boundaries; retain known tuple','leading_carrier_coefficient':'(-1)^b/2 * sum_matching_assignments prod_B (log q_B)^nu_B/q_B^(nu_B/2), nonzero, zero-lag root count cancels dprime','scope':'symbolic global independence within each degree; no finite-height interval minor'})
    assert len(witnesses)==54 and sum(w['b']==5 for w in witnesses)==19
    (ROOT/'notes/WP84_PRIME_PATH_CARRIER_WITNESSES.json').write_text(json.dumps(witnesses,indent=2)+'\n')
    # Rational constant-coefficient character test example, distinct carriers.
    # Vandermonde coefficients use integer exponents on one prime only;
    # this is a uniqueness-mechanism check, not a legal 453 evaluation.
    assert prime_vector([2,3,6],[1,1,-1])==()
    assert prime_vector([2,3],[1,-1])!=prime_vector([3,2],[1,-1])
    source={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json','notes/WP84_EVALUATION_MAP_KERNEL_CERTIFICATE.json']}
    cert={'decision':'F','parent':'73802f59532c2eb10db8f9689c886fc8ac901b64','K_formal_on_labelled_span':'{0}, formal incidence only','K_global':'UNKNOWN','K_T':'kernel of one Q-linear real evaluation; no inference to global kernel','fifth_lower':19,'fifth_upper':72,'sixth_lower':35,'sixth_upper':381,'total_lower':35,'total_upper':453,'normalized_joint_carrier_support_witness_count':54,'normalized_joint_scope':'degree-dependent normalization removes a_phi; not a proved common scaling of original mixed family','analytic_nullity_bounds':[0,418],'global_kernel_basis':None,'intersection_dimension':None,'interval_rank_witness':None,'interval_engines':{'python_flint':False,'sage':False,'mpmath':'available; ordinary values not rank certificates'},'cell_normal_form_faithfulness':'PROVED within one degree after combining actual constant-field coefficients indexed by lambda,rho,z-power; full matrix rank not computed','within_degree_carrier_uniqueness':'PROVED for analytic germs in 1/log(T/2pi), common nonzero degree normalization removed','free_carrier_diagonal_implication':'PROVED for actual fixed-cell same-degree lifts via germ lemma; FALSE for unrestricted analytic lifts, counterexample exp(i*t*lambda)-exp(i*2pi*X*lambda)','general_analytic_amplitude_uniqueness':'FALSE; a1(T)=1,a2(T)=-exp(i*T*(lambda1-lambda2))','remaining_obstruction_symbolic':'rank of combined lambda,rho,power coefficient matrices inside same-carrier supports; mixed-degree normalization and intersection','remaining_obstruction_interval':'complete actual fixed-R outward-rounded evaluations with certified admissible endpoints and taper not constructed; ordinary zero-lag diagnostics insufficient','compression_closed':False,'strict_gt79':'OPEN','source_sha256':source}
    (ROOT/'notes/WP84_PRIME_PATH_FAITHFULNESS_CERTIFICATE.json').write_text(json.dumps(cert,indent=2)+'\n')
    with (ROOT/'notes/WP84_PRIME_PATH_PARTIAL_SUPPORT_MATRIX.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['carrier_support_row','representative_functional','degree','coefficient','scope']);w.writerows([j,v['functional_id'],v['b'],1,'support incidence; analytic independence uses germ lemma and legal-cell existence proof'] for j,v in enumerate(witnesses))
    print('PASS rational carrier witnesses: fifth >=19, sixth >=35; total >=35; no global kernel or complete rank claimed')
if __name__=='__main__':main()
