"""Shared-carrier partition and exact constant-field jet machinery."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict,Counter
from math import factorial
import json,csv,hashlib
from wp84_prime_path_faithfulness import cell_atom_terms
ROOT=Path(__file__).resolve().parents[1]
def compositions(n,k):
    if k==1:yield (n,);return
    for x in range(n+1):
        for tail in compositions(n-x,k-1):yield (x,)+tail

def exact_jets(terms,through):
    """Actual constant-field monomial sums. A nonzero FORMAL monomial
    polynomial is not automatically nonzero after log-prime evaluation.
    Keys: carrier, Taylor order, pi power, real/imag i power, log powers,
    sqrt-prime denominator powers. Equal keys combine rationally.
    """
    out=defaultdict(Q)
    for (lam,rho,power,logs,nu,nh),c in terms.items():
        for k in range(power,through+1):
            n=k-power
            for beta in compositions(n,len(rho)):
                coef=c*2**n
                for r,h in zip(rho,beta):coef*=Q(r**h,factorial(h))
                ip=(n-nh)%4
                if ip>=2:coef=-coef
                key=(lam,k,n-nh,ip%2,tuple(a+h for a,h in zip(logs,beta)),nu)
                out[key]+=coef
    return {k:v for k,v in out.items() if v}

def main():
    fs=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text());groups=defaultdict(list)
    for f in fs:
        b,a,c=f['pattern'];key=min((b,tuple(a),tuple(c)),(b,tuple(c),tuple(a)));groups[key].append(f['id'])
    records=[]
    # Freeze fifth results before sixth; no unsupported upper rank from finite jets.
    for b in (5,6):
        rr=[]
        for key,ids in sorted(groups.items()):
            if key[0]!=b:continue
            rr.append({'support':key,'functional_ids':ids,'size':len(ids),'analytic_rank_lower':1,'analytic_rank_upper':len(ids),'exact_analytic_rank':1 if len(ids)==1 else None,'analytic_nullity_lower':0,'analytic_nullity_upper':len(ids)-1,'leading_u_order':b,'leading_coefficient':'(-1)^b/2 times sum of positive log-prime/sqrt-prime weights of matching assignments; zero-lag root normalization cancels','leading_minor':'any active carrier row and one admitted representative column is nonzero by the parent positivity proof','jet_rows_computed':'leading carrier row only; full higher-jet cell matrix NOT enumerated','finite_jet_kernel':'not a global functional kernel','formal_coefficient_field':'Q(i,pi,log p,sqrt p); actual constants, no assumed algebraic independence'})
        assert sum(r['size'] for r in rr)==(72 if b==5 else 381)
        (ROOT/f'notes/WP84_SHARED_CARRIER_DEGREE{b}_BLOCKS.json').write_text(json.dumps(rr,indent=2)+'\n');records+=rr
    distributions={b:dict(Counter(r['size'] for r in records if r['support'][0]==b)) for b in (5,6)}
    unresolved=sorted((r for r in records if r['size']>1),key=lambda r:(r['size'],r['support']))[0]
    minimal={'degree':5,'support':[5,[],[2,1,1,1]],'functional_ids':[5,7],'through_u_order':8,'normalized_rows':[['1','1'],['-S1+2*pi*i*lambda*mu1']*2,['(1+S2)*e2-2*pi*i*lambda*mu1*S1-2*pi^2*lambda^2*mu2']*2,['-(1+3*S2+S3)*e3+(1+S2)*e2*2*pi*i*lambda*mu1+2*pi^2*lambda^2*mu2*S1+(2*pi*i*lambda)^3*mu3/6']*2],'S3':'K*(K-1)*(3-2*(K+1)/dprime)','S1':'sum_slot log p','e2':'sum_(slot i<j)log p_i log p_j','mu1':'mean_(k in I)k','mu2':'mean_(k in I)k^2','S2':'2*K-K*(K+1)/dprime, K=min(R,dprime-1)','common_nonzero_factor':'6*(-1)^5/2 * prod_slot log p/sqrt(prod_slot p), per reduced carrier p^2*q*r*s; reciprocal orientation conjugates','jet_rank':1,'jet_nullity':1,'jet_kernel_vector':[1,-1],'nonzero_minor':{'row':0,'column':0,'value':'1'},'analytic_rank_bounds':[1,2],'global_kernel_claim':False}
    (ROOT/'notes/WP84_SHARED_CARRIER_SMALLEST_BLOCK_JET.json').write_text(json.dumps(minimal,indent=2)+'\n')
    # Mechanism regression: exact full single tuple/path, Taylor orders b..b+3.
    examples=[]
    for b in (5,6):
        eps=[1,1]+[-1]*(b-2);pi=list(range(b));primes=[2,3,5,7,11,13][:b]
        for lag in ([0]*b,[1,-1]+[0]*(b-2)):
            terms=cell_atom_terms(eps,lag,pi,primes,0,3);jets=exact_jets(terms,b+3)
            examples.append({'b':b,'eps':eps,'pi':pi,'block_primes':primes,'lags':lag,'section':[0,3],'through':b+3,'scope':'algebraic coefficient-builder regression, NOT selected-section rank witness','jet_terms':[{'key':k,'coefficient':str(v)} for k,v in sorted(jets.items())]})
    (ROOT/'notes/WP84_SHARED_CARRIER_JET_EXAMPLES.json').write_text(json.dumps(examples,indent=2)+'\n')
    cert={'decision':'F','parent':'9d637dafa2bcedcf81ba6aad700903de0654041e','fifth_block_sizes':distributions[5],'sixth_block_sizes':distributions[6],'fifth_rank_bounds':[19,72],'sixth_rank_bounds':[35,381],'total_rank_bounds':[35,453],'analytic_intersection_bounds':[0,72],'ordinary_reduced_common_carriers':0,'common_carrier_proof':'sum absolute net prime valuations has parity b; coprime exact rational valuations cannot have both parities','mixed_physical_intersection':None,'normalization':'a_phi^6*(fifth+sixth)=a_phi H5(u)+H6(u), H_b=a_phi^b F_b','fixed_profile_conditional':'If translated boundary profiles are fixed, a_phi=1-c*u, analytic and nonzero at u=0; germ uniqueness proves fixed-section cell intersection zero. Global intersection also needs selector/boundary extension faithfulness. Neither condition is promoted from a_phi->1 alone.','unconditional_mixed_germ_theorem':False,'smallest_unresolved_block':unresolved,'new_strict_lower_bound':False,'global_kernel':None,'compression_closed':False,'strict_gt79':'OPEN','source_sha256':{'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json':hashlib.sha256((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_bytes()).hexdigest()}}
    (ROOT/'notes/WP84_SHARED_CARRIER_JET_RANK_CERTIFICATE.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS fifth frozen:',distributions[5],'sixth:',distributions[6]);print('Smallest unresolved block:',unresolved['support'],unresolved['functional_ids']);print('Decision F; no higher-jet full-cell matrix or unconditional mixed normalization proved')
if __name__=='__main__':main()
