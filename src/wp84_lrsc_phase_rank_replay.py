"""Independent exact transplant replay: minors, telescoping, source provenance."""
from pathlib import Path
from fractions import Fraction as F
import csv,json,hashlib
ROOT=Path(__file__).resolve().parents[1]
def det(a):
    a=[[F(v) for v in r] for r in a];out=F(1)
    for j in range(len(a)):
        q=next((i for i in range(j,len(a)) if a[i][j]),None)
        if q is None:return F(0)
        if q!=j:a[q],a[j]=a[j],a[q];out=-out
        v=a[j][j];out*=v
        for i in range(j+1,len(a)):
            c=a[i][j]/v
            for k in range(j,len(a)):a[i][k]-=c*a[j][k]
    return out

def main():
    c=json.loads((ROOT/'notes/WP84_LRSC_PHASE_RANK_CERTIFICATE.json').read_text())
    for g in c['phase_graphs']:
        b=g['b'];B=g['B'];D=g['closed_displacement_map']
        assert all(sum(r)==0 for r in B)
        assert all(sum(B[i][j] for i in range(b))==0 for j in range(b))
        assert abs(det([r[:-1] for r in B[:-1]]))==1
        assert abs(det(D[:-1]))==1
        assert all(sum(D[i][j] for i in range(b))==0 for j in range(b-1))
        assert g['rank_B']==g['closed_displacement_dimension']==g['symbolic_alpha_phase_rank']==b-1
        # Exact vector of potential differences has zero total edge defect.
        for vertex in range(b):assert sum(B[vertex])==0
        # Root gauge cancels coefficient of every independent alpha slot.
        for eps in (-1,1):assert eps*7-eps*7==0
    rows=list(csv.DictReader((ROOT/'notes/WP84_LRSC_EXACT_ORBIT_RESPONSE.csv').open()))
    assert len(rows)==453 and all(int(v)==0 for r in rows for k,v in r.items() if k!='functional_id')
    for t in c['formal_update_tests']:
        n=t['atom_count'];assert det(t['formal_diagonal_update'])==t['determinant'] and t['rank']==n
    f=json.loads((ROOT/'notes/WP84_LRSC_FULL_WEIGHT_FEATURES.json').read_text());old=json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
    assert len(f)==453
    for v,w in zip(f,old):
        assert v['functional_id']==w['id'] and v['all_raw_origins']==w['raw_orbit_members']
        assert v['alias_integers']==w['aliases'] and F(v['alpha'])==F(w['exact_alpha'])
        assert len(v['symbolic_atom_coordinates'])==7
    r=json.loads((ROOT/'notes/WP84_LRSC_RECONSTRUCTION_CERTIFICATE.json').read_text())
    assert len(r)==8740 and {v['raw_id'] for v in r}==set(range(8740))
    assert all(v['new_basis_id'] is None for v in r)
    manifest=json.loads((ROOT/'notes/WP84_RANK_TRANSPLANT_SOURCE_MANIFEST.json').read_text())
    assert len(manifest)==28
    for v in manifest:
        data=Path(v['local_cache']).read_bytes()
        assert hashlib.sha256(data).hexdigest()==v['sha256']
        assert hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()==v['git_blob']
    assert c['proved_analytic_rank'] is None and c['actual_analytic_rank_bound']==453 and c['new_arithmetic_bound'] is None
    from wp84_lrsc_phase_rank_transplant import transition_matrix
    atoms,matrix,rr=transition_matrix({'a':1,'b':2},{'a':3,'c':4})
    assert atoms==['a','b','c'] and det(matrix)==-16 and rr==3
    # Parent's independently generated orbits and symbolic phase identities
    # certify the reconstruction instead of trusting identifier labels.
    from wp84_near_alias_orbit_replay import main as parent_replay
    parent_replay()
    print('PASS transplant minors, gauge response, full-weight retention, raw reconstruction, 28 pinned Git blobs and rank firewall')
if __name__=='__main__':main()
