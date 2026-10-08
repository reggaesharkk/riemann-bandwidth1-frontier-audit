"""Independent exact replay; a PASS here never certifies the missing P_B.

Does not import the producer or its symbolic operator construction.
Checks coefficient identities, source linkage, packet preservation, and refuses
promotion of an unevaluated actual kernel or wedge test.
"""
from copy import deepcopy
from fractions import Fraction as Q
from hashlib import sha256
from math import comb, factorial
from pathlib import Path
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT/'notes/WP84_SOURCE_JET_INTERTWINING_CERTIFICATE.json'
IDS = [[15,20,26,28,31,32], [10,12,16,17,21,22,25,29],
       [36,38,42,46,47,48,49,50,54,59,61,62,64,65,68,69],
       [34,37,39,43,53,56,60,63]]

def validate(d):
    assert d['input_head'] == '0de8810580164ca442e37043b59d88f2dd9f3f64'
    assert d['status'] == 'ACTUAL_INTERTWINING_UNDECIDED_NOT_AN_A_TO_E_CERTIFICATE'
    assert d['R'] == 6000
    expected = {
        'real_imag_coupling': True, 'rows': 'actual source-legal rows only',
        'source_mask': 'unchanged exact source mask, frozen on one cell',
        'prime_pool': 'all ordinary primes <= N(T), including every cancelled q',
        'moments': list(range(2,11)),
        'root_order': 'i_min+r, r=0,...,n-span-1',
        'Fourier_order': 'original ordered five slots; all closed paths',
        'parameter_test': 'all polynomial coefficients; no sampled translations',
        'kernel_test': 'whole kernel; all independent cell generators',
        'H_scope': 'one induced map per cell, independent of column and moments',
    }
    assert d['contract'] == expected
    assert d['actual_kernel_test_executed'] is False
    assert d['actual_wedge_test_executed'] is False
    assert d['determinant_visible_K'] is None
    assert d['correction_ranks'] is None and d['source_legal_minors'] is None
    assert d['fifth_rank_bounds'] == [38,72] and d['strict_gt79'] == 'OPEN_UNCHANGED'
    funcs = json.loads((ROOT/'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json').read_text())
    for b,ids,h in zip(d['blocks'],IDS,[6,6,8,6]):
        assert b['ids'] == ids and b['size'] == len(ids) and b['hmax'] == h
        assert b['ambient_dimension_per_cell'] == 2*(h+1)
        assert b['wedge_translation_total_degree_bound'] == len(ids)*h
        assert b['master_moment_labels'] == [f'S_{j}(N)' for j in range(2,h+3)]
        hidden=[]; visible=[]; aliases=set()
        for fid in ids:
            f=funcs[fid]; p=list(map(int,f['equality_partition'].split(',')))
            signs=[1 if s=='+' else -1 for s in f['sign_word']]
            e=[sum(signs[i] for i,v in enumerate(p) if v==j) for j in range(max(p)+1)]
            excess=[j for j in range(len(e)) if p.count(j)>abs(e[j])]
            assert len(excess)==1
            (hidden if e[excess[0]]==0 else visible).append(fid)
            aliases.update(f['aliases'])
        assert b['hidden_pair_ids']==hidden and b['visible_excess_ids']==visible
        assert b['aliases']==sorted(aliases)
        for field in ['actual_source_cells','actual_real_row_projection',
                      'actual_coefficient_columns','actual_V_basis','dim_V',
                      'rank_P','dim_kernel','kernel_basis','kernel_residual_rank',
                      'first_actual_nonzero_residual','H',
                      'actual_determinant_subspace','wedge_test']:
            assert b[field] is None
    return True

def multiply(a,b):
    n=len(a)
    return [[sum(a[i][k]*b[k][j] for k in range(n)) for j in range(n)] for i in range(n)]

def replay_operator(o,h):
    n=2*(h+1)
    generator=[[Q(0) for _ in range(n)] for _ in range(n)]
    # Directly from d Re J_h / ds = -eta Im J_(h-1), and its imaginary companion.
    for j in range(1,h+1):
        generator[2*j][2*j-1]=-1
        generator[2*j+1][2*j-2]=1
    serialized=[[Q(0) for _ in range(n)] for _ in range(n)]
    for i,j,v in o['N0_entries']: serialized[i][j]+=Q(v)
    assert serialized==generator
    assert o['coordinates']==[[j,p] for j in range(h+1) for p in ['Re','Im']]
    assert 'NOT alias residual' in o['eta']
    assert o['translation_degree']==h and o['nilpotence_index_ambient']==h+1
    assert o['translation_determinant']=='1' and o['translation_inverse']=='T_x(-s)'
    powers=[]; a=[[Q(i==j) for j in range(n)] for i in range(n)]
    for r,t in enumerate(o['translation_coefficients']):
        assert t['degree_in_eta_s']==r
        got=[[Q(0) for _ in range(n)] for _ in range(n)]
        for i,j,v in t['entries']:got[i][j]+=Q(v)
        assert got==[[v/factorial(r) for v in row] for row in a]
        powers.append(a); a=multiply(a,generator)
    assert len(powers)==h+1 and not any(any(row) for row in a)
    # Polynomial-in-(eta*s,eta*t) composition, every coefficient, not samples.
    cases=0
    for r in range(h+1):
        for s in range(h+1):
            lhs=multiply(powers[r],powers[s])
            rhs=powers[r+s] if r+s<=h else [[Q(0)]*n for _ in range(n)]
            assert lhs==rhs
            if r+s<=h:
                assert Q(1,factorial(r)*factorial(s)) == Q(comb(r+s,r),factorial(r+s))
            cases+=1
    # Inverse polynomial has zero coefficients at every positive degree.
    for r in range(1,2*h+1):
        assert sum(Q((-1)**j,factorial(j)*factorial(r-j))
                   for j in range(max(0,r-h),min(h,r)+1))==0 or r>h
        # For r>h the matrix power is zero, regardless of the scalar sum.
    assert not any(generator[0]) and not any(generator[1])
    return cases

def root_translation_coefficients():
    # Universal polynomial in root a+r and shift s: inspect every monomial.
    cases=0
    for h in range(9):
        for old_degree in range(h+1):
            shift_degree=h-old_degree
            lhs=Q(comb(h,old_degree),factorial(h))
            rhs=Q(1,factorial(old_degree)*factorial(shift_degree))
            assert lhs==rhs
            cases+=1
    return cases

def main():
    d=json.loads(CERT.read_text());validate(d)
    for path,pin in d['source_pins'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest()==pin['sha256']
        got=subprocess.check_output(['git','rev-parse',f"{pin['commit']}:{path}"],cwd=ROOT,text=True).strip()
        assert got==pin['blob']
    for path,expected in d['packet_sha256'].items():
        assert sha256((ROOT/path).read_bytes()).hexdigest()==expected
    files={str(p.relative_to(ROOT)).replace('\\','/') for p in (ROOT/'notebooklm_packet').rglob('*') if p.is_file()}
    assert files==set(d['packet_sha256'])
    cases=root_translation_coefficients()
    for b in d['blocks']:cases+=replay_operator(b['operator'],b['hmax'])
    mutations=[('real_imag_coupling',False),('rows','arbitrary diagnostic rows'),
               ('source_mask','changed'),('prime_pool','finite core'),
               ('moments',[2]),('root_order','reversed'),('Fourier_order','reordered'),
               ('parameter_test','sampled'),('kernel_test','pairwise only'),
               ('H_scope','separate map per column')]
    hostile=0
    for field,value in mutations:
        bad=deepcopy(d);bad['contract'][field]=value
        try:validate(bad)
        except AssertionError:hostile+=1
        else:raise AssertionError('mutation accepted: '+field)
    for field,value in [('R',400),('actual_kernel_test_executed',True),
                        ('actual_wedge_test_executed',True),('determinant_visible_K',[2]),
                        ('status','FULL INTERTWINING PROVED')]:
        bad=deepcopy(d);bad[field]=value
        try:validate(bad)
        except AssertionError:hostile+=1
        else:raise AssertionError('promotion accepted: '+field)
    print(f'PASS {cases} exact polynomial/operator coefficient checks; {hostile} hostile metadata mutations rejected')
    print('ACTUAL SOURCE P/V/KERNEL/WEDGE: UNEVALUATED. No A--E decision, rank promotion, or paid ledger change.')

if __name__=='__main__':main()
