"""Independent exact filter subset expansion and rank-scope replay."""
from pathlib import Path
from fractions import Fraction as Q
from itertools import product
from collections import defaultdict
import hashlib,json,csv,copy
ROOT=Path(__file__).resolve().parents[1]
def subset_expansion(eps,lags,pi):
    n=max(pi)+1;out=defaultdict(Q)
    for choose in product((0,1),repeat=len(pi)):
        z=[0]*n;a=[0]*n;h=0;c=Q(1)
        for j,s in enumerate(choose):
            l=lags[j];e=eps[j];block=pi[j]
            if l==0:a[block]+=s;c*=(-1)**s
            else:z[block]+=s*e*l;h+=1;c*=Q((-1)**s,2*e*l)
        out[tuple(z),tuple(a),h]+=c
    return {k:v for k,v in out.items() if v}

def main():
    from wp84_full_weight_evaluation_map import expand_filters
    cert=json.loads((ROOT/'notes/WP84_EVALUATION_MAP_KERNEL_CERTIFICATE.json').read_text());v=json.loads((ROOT/'notes/WP84_EVALUATION_MAP_CONSTRUCTORS.json').read_text());old=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
    for p,h in cert['source_sha256'].items():assert hashlib.sha256((ROOT/p).read_bytes()).hexdigest()==h
    for x,o in zip(v,old):
        y=copy.deepcopy(x);h=y.pop('source_fingerprint');assert hashlib.sha256(json.dumps(y,sort_keys=True,separators=(',',':')).encode()).hexdigest()==h
        b=x['b'];pi=x['pi'];eps=x['epsilon']
        assert x['id']==o['id'] and x['aliases']==o['aliases'] and x['raw_origins']==o['raw_orbit_members']
        assert ''.join('+' if e==1 else '-' for e in eps)==o['sign_word']
        assert x['nu']==[pi.count(k) for k in range(max(pi)+1)] and sum(x['nu'])==b
        for lag in ([0]*b,[1,-1]+[0]*(b-2),[2,-2]+[0]*(b-2)):
            assert subset_expansion(eps,lag,pi)==expand_filters(eps,lag,pi)
        assert x['normal_form_faithful_to_functions'] is False
    matrix=list(csv.DictReader((ROOT/'notes/WP84_EVALUATION_FORMAL_COEFFICIENT_MATRIX.csv').open()))
    assert len(matrix)==453 and {int(r['functional_column']) for r in matrix}==set(range(453))
    assert all(r['tagged_atom_row']==r['functional_column'] and r['coefficient']=='1' for r in matrix)
    assert cert['formal_fifth_rank']==72 and cert['formal_sixth_rank']==381
    # Exact zero at a legal natural-prime-scale alpha, without treating it
    # as a global functional kernel or a full-rank specialization.
    t=subset_expansion([-1],[2],[0]);assert sum(c*Q(-1)**z[0]*Q(1,2)**a[0] for (z,a,h),c in t.items())==0
    tests=json.loads((ROOT/'notes/WP84_EVALUATION_MAP_CORRUPTION_TESTS.json').read_text())
    assert len(tests)==2265 and all(len([t for t in tests if t[0]==i])==5 for i in range(453))
    # Independently regenerate all five corruptions and verify detector
    # sensitivity; a source hash does not assert functional inequality.
    for x in v:
        good=copy.deepcopy(x);good.pop('source_fingerprint')
        base=hashlib.sha256(json.dumps(good,sort_keys=True,separators=(',',':')).encode()).hexdigest()
        for field in ('consumer_alpha','aliases','pi','nu','full_formula'):
            bad=copy.deepcopy(good)
            if field=='consumer_alpha':bad[field]=str(Q(bad[field])+1)
            elif field in ('aliases','pi','nu'):bad[field][0]+=1
            else:bad[field]['symbolic_atom_coordinates'][3]='changed Fourier displacement constraint'
            assert hashlib.sha256(json.dumps(bad,sort_keys=True,separators=(',',':')).encode()).hexdigest()!=base
    assert cert['analytic_rank'] is None and cert['analytic_kernel_basis'] is None and cert['specialization_rank_witness'] is None
    assert cert['decision']=='F' and cert['new_budget'] is None
    print('PASS independent subset expansion at 1359 paths, 453 source reconstructions, formal identity matrix and analytic-rank firewall')
    print('PASS 2265 corruption records; these detect source-data edits, not analytic inequalities')
if __name__=='__main__':main()
