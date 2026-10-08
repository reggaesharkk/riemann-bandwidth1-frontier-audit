"""Full-weight Fourier numerator expansion; formal rank is not analytic rank."""
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
import json,csv,hashlib,copy
ROOT=Path(__file__).resolve().parents[1]
def expand_filters(signs,lags,labels):
    """Returns coefficients in Q[(pi*i)^-1, alpha_B, z_B^+-1].
    Coordinates: z exponents, alpha exponents, inverse-(pi*i) degree.
    Imposes exact equality blocks and multiplies zero-lag 1-alpha factors.
    No floating alpha, carrier, endpoint or alias is specialized.
    """
    n=max(labels)+1;terms={(tuple([0]*n),tuple([0]*n),0):Q(1)}
    for eps,l,block in zip(signs,lags,labels):
        choices=[(0,0,0,Q(1)),(0,1,0,Q(-1))] if l==0 else [(0,0,1,Q(1,2*eps*l)),(eps*l,0,1,Q(-1,2*eps*l))]
        new=defaultdict(Q)
        for (z,a,h),coef in terms.items():
            for dz,da,dh,c in choices:
                zz=list(z);aa=list(a);zz[block]+=dz;aa[block]+=da
                new[tuple(zz),tuple(aa),h+dh]+=coef*c
        terms={k:v for k,v in new.items() if v}
    return terms

def fingerprint(v):return hashlib.sha256(json.dumps(v,sort_keys=True,separators=(',',':')).encode()).hexdigest()
def main():
    old=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
    full=json.loads((ROOT/'notes/WP84_LRSC_FULL_WEIGHT_FEATURES.json').read_text())
    assert len(old)==len(full)==453
    constructors=[]
    for o,f in zip(old,full):
        pi=list(map(int,o['equality_partition'].split(',')));eps=[1 if x=='+' else -1 for x in o['sign_word']]
        nu=[pi.count(k) for k in range(max(pi)+1)];e=[sum(eps[j] for j in range(len(pi)) if pi[j]==k) for k in range(max(pi)+1)]
        v={'id':o['id'],'b':o['degree'],'epsilon':eps,'pi':pi,'nu':nu,'net_exponents':e,'aliases':o['aliases'],'raw_origins':o['raw_orbit_members'],'consumer_alpha':o['exact_alpha'],'full_formula':f,'Mobius_factors':'NONE in original ordinary-prime functional; exact prime-identity expansions optional, not added coefficients','input_domain':'actual height T, prescribed a_phi(T), fixed H and R6000, selected admissible endpoints; prime sets/cutoff are determined, not free','normal_form_ring':'Q[(pi*i)^-1,alpha_B,z_B,z_B^-1] with z_B=exp(2*pi*i*alpha_B); extended by log(q_B),sqrt(q_B),carrier,mask and root summation at actual evaluation','normal_form_faithful_to_functions':False}
        v['source_fingerprint']=fingerprint(v);constructors.append(v)
    (ROOT/'notes/WP84_EVALUATION_MAP_CONSTRUCTORS.json').write_text(json.dumps(constructors,indent=2)+'\n')
    # Explicit formal tagged incidence minor: identity on 453 retained labels.
    # It is intentionally not presented as a legal evaluation witness.
    with (ROOT/'notes/WP84_EVALUATION_FORMAL_COEFFICIENT_MATRIX.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['tagged_atom_row','functional_column','coefficient','scope']);w.writerows([i,i,1,'formal label incidence only; NOT actual arithmetic atom basis'] for i in range(453))
    tests=[]
    for v in constructors:
        for field in ('consumer_alpha','aliases','pi','nu','full_formula'):
            bad=copy.deepcopy(v)
            if field=='consumer_alpha':bad[field]=str(Q(bad[field])+1)
            elif field=='aliases':bad[field][0]+=1
            elif field=='pi':bad[field][0]+=1
            elif field=='nu':bad[field][0]+=1
            else:bad[field]['symbolic_atom_coordinates'][3]='changed Fourier displacement constraint'
            bad.pop('source_fingerprint');good=copy.deepcopy(v);good.pop('source_fingerprint')
            assert fingerprint(bad)!=fingerprint(good)
            tests.append([v['id'],field,'detected; provenance corruption, not a functional inequality test'])
    (ROOT/'notes/WP84_EVALUATION_MAP_CORRUPTION_TESTS.json').write_text(json.dumps(tests,indent=2)+'\n')
    # Exact identity in the evaluation specialization of the Laurent ring:
    # alpha=log(11)/log(121)=1/2, z=-1, f_2^-=0.
    zero=expand_filters([-1],[2],[0]);assert sum(c*Q(-1)**z[0]*Q(1,2)**a[0] for (z,a,h),c in zero.items())==0
    blocks={b:sum(v['b']==b for v in constructors) for b in (5,6)}
    cert={'decision':'F','parent':'f7391edb664b5cf695778970face063faadd3ad4','functional_count':453,'formal_tagged_rank':453,'formal_tagged_nullity':0,'formal_fifth_rank':blocks[5],'formal_sixth_rank':blocks[6],'formal_cross_intersection':0,'analytic_rank_lower_bound':0,'analytic_rank_upper_bound':453,'analytic_rank':None,'analytic_nullity':None,'analytic_fifth_rank':None,'analytic_sixth_rank':None,'analytic_intersection_dimension':None,'analytic_kernel_basis':None,'faithful_normal_form':False,'specialization_rank_witness':None,'zero_filter_example':{'X':121,'prime':11,'alpha':'1/2','lag':2,'sign':-1,'z':'-1','filter_value':'0','scope':'evaluation ring has relations; single-height zero is NOT a global kernel vector on the 453-span'},'corruption_checks':len(tests),'first_missing_step':'kernel characterization of actual prime/path evaluation; no legal exact specialization minor or faithful atom-independence theorem established','new_budget':None,'strict_gt79':'OPEN','source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in ['notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json','notes/WP84_LRSC_FULL_WEIGHT_FEATURES.json']}}
    (ROOT/'notes/WP84_EVALUATION_MAP_KERNEL_CERTIFICATE.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS 453 full constructors, exact Laurent filter expansion, 2265 corruption detections; formal tagged blocks',blocks)
    print('No analytic rank witness or kernel vector proved; decision F')
if __name__=='__main__':main()
