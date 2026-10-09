"""Exact exterior-power audit for the unresolved 6-column fifth block.

This constructs only the source-derived real jet translation generator.  It
does not invent or approximate the source projection P_B or the actual jet
columns V_B.  The certificate therefore proves a conditional polynomial
exception bound, not source-legal nonvanishing.
"""
from __future__ import annotations

from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOCK = [15, 20, 26, 28, 31, 32]
H = 6
DIM = 2 * (H + 1)
K = 6


def generator_entries():
    """Return (row, column, integer) for N0, where N=eta*N0."""
    out = []
    for h in range(1, H + 1):
        # (Re J_h)' = -eta Im J_(h-1); (Im J_h)' = eta Re J_(h-1).
        out.append((2 * h, 2 * (h - 1) + 1, -1))
        out.append((2 * h + 1, 2 * (h - 1), 1))
    return out


def exterior_transitions():
    """Exact sparse entries of dGamma(N0) on the ordered 6-subset basis."""
    basis = list(combinations(range(DIM), K))
    index = {b: i for i, b in enumerate(basis)}
    transitions = []
    for col, blade in enumerate(basis):
        for row0, col0, value in generator_entries():
            if col0 not in blade or row0 in blade:
                continue
            pos = blade.index(col0)
            replaced = list(blade)
            replaced[pos] = row0
            inversions = sum(replaced[i] > replaced[j]
                             for i in range(K) for j in range(i + 1, K))
            target = tuple(sorted(replaced))
            transitions.append((index[target], col, value * (-1) ** inversions))
    return basis, transitions


def grade(blade):
    return sum(i // 2 for i in blade)


def build_certificate():
    source_path = ROOT / "src/wp84_fifth_full_pool_amplitude.py"
    source = source_path.read_text(encoding="utf-8")
    assert "def source_mask(" not in source
    assert "section, prime_stream, source_mask" in source
    assert "return {'id':fid,'T':T" in source
    basis, transitions = exterior_transitions()
    grades = [grade(b) for b in basis]
    gmin, gmax = min(grades), max(grades)
    assert len(basis) == 3003
    # Every nonzero exterior transition raises the integer grade by exactly 1.
    assert all(grades[r] == grades[c] + 1 for r, c, _ in transitions)
    degree_bound = gmax - gmin
    assert (gmin, gmax, degree_bound) == (6, 30, 24)
    entries = generator_entries()
    canonical = "\n".join(f"{r},{c},{v}" for r, c, v in entries).encode()
    return {
        "decision": "E_SOURCE_INPUT_STILL_MISSING",
        "block_ids": BLOCK,
        "R": 6000,
        "source_jet_orders": "h=0,...,6; real and imaginary coordinates retained",
        "ambient_real_dimension": DIM,
        "sixth_exterior_dimension": len(basis),
        "N_over_eta_entries": [list(x) for x in entries],
        "N_over_eta_sha256": sha256(canonical).hexdigest(),
        "exterior_generator_nonzero_entries": len(transitions),
        "exterior_grade_min": gmin,
        "exterior_grade_max": gmax,
        "exact_exterior_identity": "dGamma(N0)=sum_{r=1}^6 I wedge ... wedge N0 wedge ... wedge I",
        "nilpotence_proof": "each nonzero entry raises sum(h_j) by 1; grades on 6-subsets range 6..30; hence dGamma(N0)^25=0",
        "wedge_polynomial_degree_bound": degree_bound,
        "conditional_section_statement": "For fixed source cell, fixed length n, and fixed linear projection P, each coordinate of W(s)=(wedge^6 P) exp(eta*s*dGamma(N0)) v is a polynomial of degree <=24. If W is not identically zero, its common zero set on the one-parameter translation line has at most 24 points. This controls endpoint translations only; it does not compare different lengths or different masks/cells.",
        "source_object": {
            "constructor": "src/wp84_fifth_full_pool_amplitude.py",
            "historical_selector_required_for_this_audit": False,
            "first_unavailable_input": "The exact full-pool source-masked coefficient-column map for these six canonical functionals: the atom iterator requires a source_mask callback but no implementation is present, and source_amplitude_entry returns only a schema. Therefore the actual projected jet columns cannot be instantiated.",
            "iterator_requires_external_source_mask": True,
            "source_mask_implementation_present": False,
            "source_amplitude_entry_is_evaluated_matrix": False,
            "actual_P_B": None,
            "actual_V_B": None,
            "actual_projected_wedge": None,
            "actual_wedge_nonzero_seed": None,
        },
        "moment_support_K_B": None,
        "block_rank_certified": False,
        "old_fifth_rank_bounds": [38, 72],
        "new_fifth_rank_bounds": [38, 72],
        "rank_promotion": 0,
        "strict_gt79": "OPEN",
        "not_a_source_rank_certificate": True,
    }


def main():
    cert = build_certificate()
    out = ROOT / "notes/WP84_BLOCK15_SELECTOR_FREE_WEDGE_CERTIFICATE.json"
    out.write_text(json.dumps(cert, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {out.name}; exterior degree <= {cert['wedge_polynomial_degree_bound']}; source wedge not instantiated")


if __name__ == "__main__":
    main()
