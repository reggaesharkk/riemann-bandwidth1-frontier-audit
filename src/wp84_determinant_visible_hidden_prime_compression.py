"""Fail-closed audit of the source inputs needed for the fifth-block wedges.

The older coefficient constructor stores summand schemas, not evaluated
source-selected matrices.  This module records exactly which inputs prevent
an honest determinant expansion.  It deliberately refuses to label a formal
candidate support as the determinant-visible support.
"""
from __future__ import annotations

import json
import hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BLOCKS = {
    "B6": [15, 20, 26, 28, 31, 32],
    "B8a": [10, 12, 16, 17, 21, 22, 25, 29],
    "B16": [36, 38, 42, 46, 47, 48, 49, 50, 54, 59, 61, 62, 64, 65, 68, 69],
    "B8b": [34, 37, 39, 43, 53, 56, 60, 63],
}
HMAX = {"B6": 6, "B8a": 6, "B16": 8, "B8b": 6}
MOMENTS = {b: list(range(2, HMAX[b] + 3)) for b in BLOCKS}


def audit() -> dict:
    determinant = json.loads((ROOT / "notes/WP84_EXACT_DETERMINANT_COEFFICIENTS.json").read_text())
    qmask = json.loads((ROOT / "notes/WP84_EXACT_Q_MASK_CERTIFICATE.json").read_text())
    visible = json.loads((ROOT / "notes/WP84_VISIBLE_PRIME_SUBSYSTEM.json").read_text())
    section = json.loads((ROOT / "notes/WP84_FIFTH_FULL_POOL_SECTION_REPLAY.json").read_text())

    # These checks are intentional.  The amplitude module leaves both inputs
    # as caller-supplied objects; no executable source implementation exists.
    amplitude_source = (ROOT / "src/wp84_fifth_full_pool_amplitude.py").read_text()
    has_source_mask = "def source_mask(" in amplitude_source
    has_source_row_selector = any(
        token in amplitude_source
        for token in ("def source_row_selector(", "SOURCE_SELECTED_ROWS =", "source_row_ids =")
    )
    has_executable_selected_section = any(
        token in amplitude_source
        for token in ("def selected_section(", "SOURCE_SECTION =", "source_section_endpoints =")
    )

    blocks = []
    for name, ids in BLOCKS.items():
        size = len(ids)
        blocks.append({
            "name": name,
            "layout_ids": ids,
            "size": size,
            "master_moments": [f"S_{j}" for j in MOMENTS[name]],
            "candidate_moment_count": len(MOMENTS[name]),
            "determinant_visible_K": None,
            "K_status": "not determined: evaluated source coefficient entries are absent",
            "formal_first_possible_deficit": size - 1,
            "first_nonzero_deficit": None,
            "C_m_minus_1": "formal cofactor expression only; source entries unevaluated",
            "correction_span_rank": None,
            "correction_span_rank_upper_bound": min(size, len(MOMENTS[name])),
            "visible_only_rank_lower_bound": 0,
            "visible_only_minor": None,
            "promotion": 0,
        })

    missing = []
    if not has_source_mask:
        missing.append("executable source_mask predicate (the atom generator requires it as an argument)")
    if not has_source_row_selector:
        missing.append("source-selected row identities/order and the coefficient-jet selector")
    if not has_executable_selected_section:
        missing.append("executable source section endpoint rule k_-(T), k_+(T), beyond d'/d -> 1")
    missing.extend([
        "evaluated carrier/alias-cell assignments and exact source-state values for each selected row",
        "exact finite source sums for the visible-prime entries and each E_r entry",
        "a coefficient field/equality certificate for the resulting log-prime and phase sums",
    ])

    inputs = [
        "src/wp84_fifth_full_pool_amplitude.py",
        "src/wp84_exact_determinant_coefficient_builder.py",
        "src/wp84_source_q_mask_extractor.py",
        "src/wp84_wedge_support_reducer.py",
        "src/wp84_visible_prime_minor_builder.py",
        "notes/WP84_EXACT_DETERMINANT_COEFFICIENTS.json",
        "notes/WP84_EXACT_Q_MASK_CERTIFICATE.json",
        "notes/WP84_WEDGE_SUPPORT_REDUCTION.json",
        "notes/WP84_VISIBLE_PRIME_SUBSYSTEM.json",
        "notes/WP84_FIFTH_FULL_POOL_SECTION_REPLAY.json",
    ]
    hashes = {
        p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest()
        for p in inputs
    }
    return {
        "status": "BLOCKED_ON_MISSING_SOURCE_MATRIX_DATA",
        "source_head": determinant.get("source_head"),
        "source_sha256": hashes,
        "R": 6000,
        "frozen_basis": {"candidate_coordinates": 73, "master_moments": [f"S_{j}" for j in range(2, 11)], "J": 9},
        "blocks": blocks,
        "global_K": None,
        "global_K_status": "undetermined; cannot remove any S_r as determinant-invisible",
        "correction_ranks": "not determined; only displayed upper bounds follow from number of candidate moment matrices",
        "first_possible_deficit": "m-1 for each block, as structurally replayed",
        "first_nonzero_coefficient": None,
        "visible_only_rank_lower_bounds": {b: 0 for b in BLOCKS},
        "new_fifth_analytic_rank": 0,
        "existing_fifth_rank_bounds": [38, 72],
        "source_input_audit": {
            "source_mask_implemented": has_source_mask,
            "source_row_selector_implemented": has_source_row_selector,
            "selected_section_rule_implemented": has_executable_selected_section,
            "missing_inputs": missing,
            "evidence": {
                "amplitude_constructor": "src/wp84_fifth_full_pool_amplitude.py:iter_source_atoms takes source_mask as an external required argument and source_amplitude_entry returns only a summand schema",
                "section_replay": section.get("section_jet_formula", section.get("verified_orders")),
                "visible_certificate": visible.get("status", visible.get("visible_layout_count")),
                "qmask_source_head": qmask.get("source_head"),
            },
        },
        "decision": "F",
        "decision_qualification": "no compression or nonvanishing can be certified from the currently executable source data; this is an evidence boundary, not a proof that the true source determinant is full-dimensional",
    }


def main() -> None:
    result = audit()
    out = ROOT / "notes/WP84_DETERMINANT_VISIBLE_HIDDEN_PRIME_COMPRESSION.json"
    out.write_text(json.dumps(result, indent=2) + "\n")
    print(result["status"])
    print(f"73 -> 9 -> K=undetermined; R={result['R']}")
    print(f"missing source inputs: {len(result['source_input_audit']['missing_inputs'])}")


if __name__ == "__main__":
    main()
