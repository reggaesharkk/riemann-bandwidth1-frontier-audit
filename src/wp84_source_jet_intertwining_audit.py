"""Source-linked jet operators; deliberately does not invent a legal stencil.

Produces a certificate of exact operator identities and an explicit UNEVALUATED
actual-kernel gate. The latter is not a successful intertwining certificate.
"""
from fractions import Fraction as Q
from hashlib import sha256
from math import factorial
from pathlib import Path
import json
import subprocess
import wp84_fifth_full_pool_amplitude as source
import wp84_exact_determinant_coefficient_builder as builder

ROOT = Path(__file__).resolve().parents[1]
PARENT = '0de8810580164ca442e37043b59d88f2dd9f3f64'
OUT = ROOT/'notes/WP84_SOURCE_JET_INTERTWINING_CERTIFICATE.json'
INPUTS = [
    'src/wp84_fifth_full_pool_amplitude.py',
    'src/wp84_source_q_mask_extractor.py',
    'src/wp84_exact_determinant_coefficient_builder.py',
    'src/wp84_wedge_support_reducer.py',
    'notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json',
    'notes/WP84_FIFTH_LEGAL_STENCIL_AND_PRIME_REALIZATION.md',
    'notes/WP84_EXACT_Q_MASK_AND_DETERMINANT_VISIBLE_MOMENT_BASIS.md',
    'notes/WP84_DETERMINANT_NATIVE_ENDPOINT_CERTIFICATE.json',
    'notes/WP84_DETERMINANT_NATIVE_ENDPOINT_REINSTANTIATION.md',
    'notes/WP84_LRSC_PHASE_NETWORK_FUNCTIONAL_RANK_TRANSPLANT.md',
    'notes/WP84_LRSC_DISPLACEMENT_RANK_CLOSURE.md',
    'notes/WP84_DETUNING_COMMUTATOR_ENDPOINT.md',
]

def digest(path):
    return sha256((ROOT/path).read_bytes()).hexdigest()

def pin(path):
    blob = subprocess.check_output(
        ['git', 'rev-parse', f'{PARENT}:{path}'], cwd=ROOT, text=True).strip()
    return {'commit': PARENT, 'blob': blob, 'sha256': digest(path)}

def power(hmax, r):
    """Sparse exact N0^r, N0 = lower jet shift tensor [[0,-1],[1,0]]."""
    a = 2*(hmax+1)
    out = []
    for h in range(r, hmax+1):
        for part in range(2):
            # multiplication by i^r on the real/imaginary pair
            rowpart = (part+r) % 2
            sign = (-1)**((part+r)//2)
            out.append([2*h+rowpart, 2*(h-r)+part, sign])
    assert all(0 <= i < a and 0 <= j < a for i,j,_ in out)
    return out

def operator(hmax):
    terms = []
    for r in range(hmax+1):
        terms.append({'degree_in_eta_s': r,
                      'entries': [[i,j,str(Q(v,factorial(r)))]
                                  for i,j,v in power(hmax,r)]})
    return {
        'coordinates': [[h,p] for h in range(hmax+1) for p in ['Re','Im']],
        'eta': '2*pi*lambda_x, lambda_x=sum e_b log(p_b), NOT alias residual',
        'N0_entries': power(hmax,1),
        'infinitesimal_generator': 'N_x=eta_x*N0 on cell x; zero elsewhere',
        'translation': 'T_x(s)=exp(s*N_x)',
        'translation_coefficients': terms,
        'nilpotence_index_ambient': hmax+1,
        'translation_degree': hmax,
        'translation_determinant': '1',
        'translation_inverse': 'T_x(-s)',
        'leading_real_projection_generator': '0',
        'first_real_row_companion': '-eta_x * evaluation(Im, h-1), h>0',
    }

def build():
    old = json.loads((ROOT/INPUTS[7]).read_text())
    assert old['jet_gate']['frozen_real_row_stencil_closed'] is None
    assert old['jet_gate']['intertwining_matrices_H_x'] is None
    packet = {str(p.relative_to(ROOT)).replace('\\','/'): digest(str(p.relative_to(ROOT)))
              for p in sorted((ROOT/'notebooklm_packet').rglob('*')) if p.is_file()}
    assert packet == old['packet_sha256'], 'packet differs from parent snapshot'
    blocks = []
    carriers = ['p*q*r','p^2*q','p*q/r','p^2/r']
    for b,carrier in zip(builder.build()['blocks'],carriers):
        desc = [source.descriptor(fid) for fid in b['ids']]
        h = b['hmax']; m = b['size']
        blocks.append({
            'ids': b['ids'], 'size': m, 'hmax': h, 'carrier': carrier,
            'aliases': sorted(set(a for d in desc for a in d['aliases'])),
            'hidden_pair_ids': [d['id'] for d in desc if d['hidden_canceled_prime']],
            'visible_excess_ids': [d['id'] for d in desc if not d['hidden_canceled_prime']],
            'master_moment_labels': b['moment_variables'],
            'ambient_dimension_per_cell': 2*(h+1),
            'operator': operator(h),
            'wedge_translation_total_degree_bound': m*h,
            'actual_source_cells': None, 'actual_real_row_projection': None,
            'actual_coefficient_columns': None, 'actual_V_basis': None,
            'dim_V': None, 'rank_P': None, 'dim_kernel': None,
            'kernel_basis': None, 'kernel_residual_rank': None,
            'first_actual_nonzero_residual': None, 'H': None,
            'actual_determinant_subspace': None, 'wedge_test': None,
        })
    return {
        'input_head': PARENT,
        'status': 'ACTUAL_INTERTWINING_UNDECIDED_NOT_AN_A_TO_E_CERTIFICATE',
        'R': 6000,
        'contract': {
            'real_imag_coupling': True, 'rows': 'actual source-legal rows only',
            'source_mask': 'unchanged exact source mask, frozen on one cell',
            'prime_pool': 'all ordinary primes <= N(T), including every cancelled q',
            'moments': list(range(2,11)),
            'root_order': 'i_min+r, r=0,...,n-span-1',
            'Fourier_order': 'original ordered five slots; all closed paths',
            'parameter_test': 'all polynomial coefficients; no sampled translations',
            'kernel_test': 'whole kernel; all independent cell generators',
            'H_scope': 'one induced map per cell, independent of column and moments',
        },
        'blocks': blocks,
        'proved': ['exact source root-translation formula at fixed n and masks',
                   'complete realified source-jet generator and polynomial action',
                   'generator/kernel equivalence, conditional on actual V and P',
                   'zeroth real jet is fixed under root translation',
                   'finite exterior degree bounds, not actual wedge intertwining'],
        'actual_kernel_test_executed': False,
        'actual_wedge_test_executed': False,
        'determinant_visible_K': None, 'correction_ranks': None,
        'source_legal_minors': None, 'fifth_rank_bounds': [38,72],
        'strict_gt79': 'OPEN_UNCHANGED',
        'source_pins': {p:pin(p) for p in INPUTS}, 'packet_sha256': packet,
    }

def main():
    data = build()
    OUT.write_text(json.dumps(data,indent=2)+'\n', encoding='utf-8')
    print('WROTE source-linked operator certificate; actual P/V/kernel/wedge UNEVALUATED')

if __name__ == '__main__':
    main()
