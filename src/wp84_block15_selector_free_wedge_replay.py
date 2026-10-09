"""Independent exact replay of the block-15 exterior-power audit.

This file does not import the constructor. It independently rebuilds the
realified generator and sixth-exterior transitions, checks the grade bound,
and hostile-mutates the claim fields. It intentionally refuses rank promotion.
"""
from __future__ import annotations

from copy import deepcopy
from hashlib import sha256
from itertools import combinations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "notes/WP84_BLOCK15_SELECTOR_FREE_WEDGE_CERTIFICATE.json"
EXPECTED_BLOCK = [15, 20, 26, 28, 31, 32]


def replay_operator():
    d = 14
    k = 6
    basis = list(combinations(range(d), k))
    lookup = {x: j for j, x in enumerate(basis)}
    # Independent construction from the differential rule on (Re, Im) pairs.
    images = {}
    for h in range(1, 7):
        images[2 * (h - 1)] = (2 * h + 1, 1)
        images[2 * (h - 1) + 1] = (2 * h, -1)
    edge_rows = []
    for source_blade_no, blade in enumerate(basis):
        for place, coordinate in enumerate(blade):
            if coordinate not in images:
                continue
            replacement, scalar = images[coordinate]
            if replacement in blade:
                continue
            candidate = list(blade)
            candidate[place] = replacement
            # Sign of the sorting permutation, computed independently by parity.
            inversions = sum(candidate[i] > candidate[j]
                             for i in range(k) for j in range(i + 1, k))
            edge_rows.append((lookup[tuple(sorted(candidate))], source_blade_no,
                              scalar * (-1 if inversions % 2 else 1)))
    generator = []
    for h in range(1, 7):
        generator.extend([(2 * h, 2 * (h - 1) + 1, -1),
                          (2 * h + 1, 2 * (h - 1), 1)])
    return basis, edge_rows, generator


def validate(cert):
    basis, edges, generator = replay_operator()
    assert cert["decision"] == "E_SOURCE_INPUT_STILL_MISSING"
    assert cert["block_ids"] == EXPECTED_BLOCK
    assert cert["R"] == 6000
    assert cert["ambient_real_dimension"] == 14
    assert cert["sixth_exterior_dimension"] == len(basis) == 3003
    assert cert["N_over_eta_entries"] == [list(x) for x in generator]
    canonical = "\n".join(f"{r},{c},{v}" for r, c, v in generator).encode()
    assert cert["N_over_eta_sha256"] == sha256(canonical).hexdigest()
    assert cert["exterior_generator_nonzero_entries"] == len(edges)
    h = [sum(i // 2 for i in blade) for blade in basis]
    assert (min(h), max(h)) == (6, 30)
    assert all(h[r] == h[c] + 1 for r, c, _ in edges)
    assert cert["exterior_grade_min"] == 6
    assert cert["exterior_grade_max"] == 30
    assert cert["wedge_polynomial_degree_bound"] == 24
    assert cert["source_object"]["iterator_requires_external_source_mask"] is True
    assert cert["source_object"]["historical_selector_required_for_this_audit"] is False
    assert "source_mask callback" in cert["source_object"]["first_unavailable_input"]
    assert cert["source_object"]["source_mask_implementation_present"] is False
    assert cert["source_object"]["source_amplitude_entry_is_evaluated_matrix"] is False
    assert cert["source_object"]["actual_P_B"] is None
    assert cert["source_object"]["actual_V_B"] is None
    assert cert["source_object"]["actual_projected_wedge"] is None
    assert cert["source_object"]["actual_wedge_nonzero_seed"] is None
    assert cert["moment_support_K_B"] is None
    assert cert["block_rank_certified"] is False
    assert cert["old_fifth_rank_bounds"] == [38, 72]
    assert cert["new_fifth_rank_bounds"] == [38, 72]
    assert cert["rank_promotion"] == 0
    assert cert["strict_gt79"] == "OPEN"
    assert cert["not_a_source_rank_certificate"] is True


def hostile_mutations(cert):
    tests = []
    for name, mutate in [
        ("wrong block", lambda x: x.update(block_ids=[15, 20, 26, 28, 31, 33])),
        ("wrong real-imaginary generator sign", lambda x: x["N_over_eta_entries"][0].__setitem__(2, 1)),
        ("loose degree promoted as exact", lambda x: x.update(wedge_polynomial_degree_bound=36)),
        ("invented projected map", lambda x: x["source_object"].update(actual_P_B="diagnostic")),
        ("invented moment support", lambda x: x.update(moment_support_K_B=[2, 3])),
        ("false rank promotion", lambda x: x.update(rank_promotion=1)),
        ("relaxed source mask", lambda x: x["source_object"].update(source_mask_implementation_present=True)),
        ("invented historical-selector dependency", lambda x: x["source_object"].update(historical_selector_required_for_this_audit=True)),
    ]:
        bad = deepcopy(cert)
        mutate(bad)
        try:
            validate(bad)
        except AssertionError:
            tests.append((name, "rejected"))
        else:
            raise AssertionError(f"hostile mutation accepted: {name}")
    assert len(tests) == 8
    return tests


def main():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    validate(cert)
    mutations = hostile_mutations(cert)
    print("PASS: independent exact 3003-coordinate exterior transition replay")
    print("PASS: every exterior transition raises grade by one; degree bound 24")
    print("PASS: actual P_B/V_B/wedge/K_B remain null; rank remains 38--72")
    print("PASS: hostile mutations rejected:", ", ".join(x for x, _ in mutations))


if __name__ == "__main__":
    main()
