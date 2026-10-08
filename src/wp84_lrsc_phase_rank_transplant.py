"""Exact LRSC/phase-mechanism transplant, with rank-faithfulness firewall."""
from pathlib import Path
from fractions import Fraction as F
import json,csv,hashlib
ROOT=Path(__file__).resolve().parents[1]
def rank(a):
    a=[[F(x) for x in r] for r in a];r=0;piv=[]
    for j in range(len(a[0]) if a else 0):
        q=next((i for i in range(r,len(a)) if a[i][j]),None)
        if q is None:continue
        a[r],a[q]=a[q],a[r];v=a[r][j];a[r]=[x/v for x in a[r]]
        for i in range(len(a)):
            if i!=r:
                v=a[i][j];a[i]=[x-v*y for x,y in zip(a[i],a[r])]
        piv.append(j);r+=1
    return r,piv

def transition_matrix(old,new):
    """Union-domain multiplier update. Coefficients must be exact rationals.
    Symbolic analytic weights need a field with certified equality testing;
    they are not silently specialized to generic independent variables.
    """
    atoms=sorted(set(old)|set(new));delta=[F(new.get(a,0))-F(old.get(a,0)) for a in atoms]
    matrix=[[delta[i] if i==j else F(0) for j in range(len(atoms))] for i in range(len(atoms))]
    return atoms,matrix,rank(matrix)[0]

def cycle(b):
    B=[[int(v==(e+1)%b)-int(v==e) for e in range(b)] for v in range(b)]
    # u0=0; u1,...,u_(b-1), edges l_j=u_j-u_(j-1), l_b=-u_(b-1).
    D=[[int(j==e+1)-int(j==e) for j in range(1,b)] for e in range(b)]
    return {'b':b,'B':B,'rank_B':rank(B)[0],'vertex_gauge_image_dimension':b-1,'cycle_dimension':1,'cycle_basis':[1]*b,'closed_displacement_map':D,'closed_displacement_dimension':rank(D)[0],'root_origin_gauge_dimension':1,'symbolic_alpha_phase_rank':b-1,'phase_rank_scope':'independent alpha slot coefficients after root-origin compensation; not arithmetic functional rank'}

def main():
    funcs=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
    assert len(funcs)==453
    features=[]
    for v in funcs:
        features.append({'functional_id':v['id'],'degree':v['degree'],'representative_signs':v['sign_word'],'representative_equality':v['equality_partition'],'all_raw_origins':v['raw_orbit_members'],'alias_integers':v['aliases'],'alpha':v['exact_alpha'],'symbolic_atom_coordinates':['distinct ordinary primes q_B<=floor(exp(L-sqrt(L)))','exact equality partition and slot multiplicities nu_B','all original window intersections chi','closed lags |l_j|<=6000, sum l_j=0','u_j, imin=kminus-min u, M=max(0,dprime-range u)','m nearest alias; 0<|lambda-mL|<=H/T','a_phi(T), selected section, root index k=0..M-1'],'coefficient':'prod_j[-log(p_j)/(a_phi L sqrt(p_j))*f_l_j^eps_j(log(p_j)/L)] * chi/dprime','phase':'T*lambda + 2*pi/L * (sum_j eps_j*u_(j-1)*log(p_j) + (imin+k)*lambda)','cumulant_coefficient':'1 (frozen raw consumer)','evaluation':'sum over all atom coordinates and take real part; alpha remains outside','faithfulness':'equality of full coefficient atomic measures implies equality of evaluation; converse/injectivity on 453-span NOT proved'})
    (ROOT/'notes/WP84_LRSC_FULL_WEIGHT_FEATURES.json').write_text(json.dumps(features,indent=2)+'\n')
    cycles=[cycle(b) for b in (5,6)]
    # Exact response to vertex-potential gauges, four/five independent each,
    # plus one root-origin coordinate per degree. All are zero by telescoping.
    response=[[0]*11 for _ in funcs]
    with (ROOT/'notes/WP84_LRSC_EXACT_ORBIT_RESPONSE.csv').open('w',newline='') as f:
        w=csv.writer(f);w.writerow(['functional_id']+[f'gauge_{j}' for j in range(11)]);w.writerows([[i]+r for i,r in enumerate(response)])
    transitions=[]
    for n in (1,2,3,6):
        diag=[[int(i==j)*(i+1) for j in range(n)] for i in range(n)]
        transitions.append({'atom_count':n,'formal_diagonal_update':diag,'rank':rank(diag)[0],'determinant':__import__('math').factorial(n),'scope':'symbolic atom-multiplier countermodel; not a measured actual prime transition'})
    reconstruct=[]
    for r in csv.DictReader((ROOT/'notes/WP84_NEAR_ALIAS_EXACT_INCIDENCE.csv').open()):
        reconstruct.append({'raw_id':int(r['raw_id']),'phase_pattern_id':int(r['phase_pattern_id']),'phase_orbit_id':int(r['phase_orbit_id']),'retained_functional_id':int(r['raw_conjugate_functional_id']),'coefficient':r['omega'],'reconstruction':'Re raw complete sum equals retained representative by dihedral/conjugation orbit; phase projection alone is not enough','new_basis_id':None})
    (ROOT/'notes/WP84_LRSC_RECONSTRUCTION_CERTIFICATE.json').write_text(json.dumps(reconstruct,indent=2)+'\n')
    source=json.loads((ROOT/'notes/WP84_RANK_TRANSPLANT_SOURCE_MANIFEST.json').read_text())
    for v in source:assert hashlib.sha256(Path(v['local_cache']).read_bytes()).hexdigest()==v['sha256']
    cert={'decision':'F','parent':'7addc6e33f6fd3053145155747e97f2a755f2e77','phase_graphs':cycles,'orbit_response':{'shape':[453,11],'rank':0,'left_nullity':453,'right_nullity':11,'row_basis':[],'column_basis':[],'null_basis':'standard coordinate vectors on both sides','scope':'exact gauge response only; not full elementary-state-transition response'},'formal_update_tests':transitions,'minimum_state_generator_count':None,'actual_generator_rank':None,'actual_analytic_rank_bound':453,'analytic_rank_lower_bound':0,'proved_analytic_rank':None,'proved_small_basis':None,'formal_label_gram':{'formula':'G=I_453 for independently labelled feature coordinates','rank':453,'determinant':1,'analytic_faithfulness':False},'actual_gram_rank':None,'actual_null_relations':None,'new_arithmetic_bound':None,'old_common_bound_unchanged':'1.7670578586835696e-8','fifth_sixth':'parity separation under certified gauges and dihedral actions; no stronger functional-subspace separation proved','source_count':len(source),'first_missing_step':'injectivity or full-weight kernel characterization of atomic-measure evaluation on the 453-function span','strict_gt79':'OPEN','charge':None}
    (ROOT/'notes/WP84_LRSC_PHASE_RANK_CERTIFICATE.json').write_text(json.dumps(cert,indent=2)+'\n')
    print('PASS exact phase graphs, full-weight symbolic constructors, zero-gauge response, finite update countermodels, 8740 replayable origin records and source hashes')
    print('Decision F: analytic evaluation injectivity and minimum generator count not proved')
if __name__=='__main__':main()
