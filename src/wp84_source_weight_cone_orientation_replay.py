#!/usr/bin/env python3
"""Regenerate the outward-rounded R400 overlap table for all atom orders."""

import json
import re
from fractions import Fraction as Q
from itertools import permutations
from pathlib import Path

from mpmath import iv

from wp84_source_weight_cone_audit import WITNESS, orientation_vectors
from wp84_r400_filtered_connected_kernel import omega_interval


ROOT = Path(__file__).resolve().parents[1]


def main():
    iv.dps = 28
    oriented = orientation_vectors()
    if len(oriented) != 24 or any(sum(v, Q(0)) != 0 for v in oriented):
        raise RuntimeError("balanced orientation ledger changed")
    if len(set(oriented)) != 12:
        raise RuntimeError("orientation duplicate structure changed")
    conjugate_oriented = tuple(tuple(-x for x in v) for v in oriented)
    all_oriented = oriented + conjugate_oriented
    if len(all_oriented) != 48 or len(set(all_oriented)) != 24:
        raise RuntimeError("conjugate orientation multiplicity changed")

    ordered_unique = []
    seen = set()
    for vector in permutations(WITNESS):
        if vector not in seen:
            seen.add(vector)
            ordered_unique.append(("source", vector))
    conjugate_witness = tuple(-x for x in WITNESS)
    for vector in permutations(conjugate_witness):
        if vector not in seen:
            seen.add(vector)
            ordered_unique.append(("conjugate", vector))
    if {vector for _, vector in ordered_unique} != set(all_oriented):
        raise RuntimeError("orientation generation disagrees with source/conjugate permutations")

    cache = {}
    records = []
    lines = [f"CERTIFIED: {len(all_oriented)} labeled source/conjugate orientations; {len(ordered_unique)} unique interval FFTs",
             "CERTIFIED: every R400 filtered overlap interval is strictly positive"]
    for family, vector in ordered_unique:
        value = omega_interval(vector, 400, iv, cache)
        if not value > 0:
            raise RuntimeError("nonpositive interval in balanced source orientation")
        if not value > (iv.mpf(799) / 4000):
            raise RuntimeError("certified overlap lower bound 799/4000 failed")
        match = re.fullmatch(r"\[([^,]+),\s*([^\]]+)\]", str(value))
        if match is None:
            raise RuntimeError("unexpected interval rendering")
        records.append({
            "family": family,
            "v": [str(x) for x in vector],
            "omega": [match.group(1).strip(), match.group(2).strip()],
        })
        lines.append(f"{family} {[str(x) for x in vector]} {records[-1]['omega']}")

    evidence = {
        "schema": "wp84.source-weight-cone-orientation-intervals.v1",
        "method": "Outward-rounded mpmath interval FFT via src/wp84_r400_filtered_connected_kernel.py::omega_interval; R=400; dps=28. Source and conjugate families each cover 6 balanced sign orthants x 2 positive orders x 2 negative orders, with duplicate vectors collapsed because repeated shifts coincide.",
        "scope": "Filtered external overlap Omega_4,400(v), not the full prime-pool arithmetic aggregate.",
        "orientation_cases_before_duplicate_collapse": len(all_oriented),
        "unique_rational_orderings": len(ordered_unique),
        "all_intervals_strictly_positive": True,
        "permutation_invariance": {
            "row_cumulant": "Invariant under all 48 labeled cases (24 per family); its exact rational-grid value is 1 when 5 divides m, with the same m>=10 positive bound for every ordering.",
            "conjugation": "The sign-reversed family has the same positive coefficient and real kappa on S=0; both filtered overlaps are interval-certified positive.",
            "source_admission_and_closed_carrier": "Invariant under these permutations and conjugation.",
            "external_filtered_overlap": "Not invariant under permutation; the certified intervals show distinct positive values for different orderings in both families.",
        },
        "intervals": records,
        "positive_cumulant_bound": "For every m>=10 and each source/conjugate vector, kappa_m(v)>=384/625. Every overlap exceeds 799/4000, so Phi_4,400,m(v)>9588/78125.",
        "aggregate_warning": "These 24 unique legal prime-power tuples do not determine the sign of the complete signed arithmetic sum.",
    }
    target = ROOT / "evidence" / "WP84_SOURCE_WEIGHT_CONE_ORIENTATION_INTERVALS.json"
    target.write_text(json.dumps(evidence, indent=2) + "\n", encoding="utf-8")
    lines.append(f"WROTE {target.relative_to(ROOT)}")
    log_path = ROOT / "evidence" / "WP84_SOURCE_WEIGHT_CONE_ORIENTATION_REPLAY.log"
    log_path.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print("\n".join(lines))


if __name__ == "__main__":
    main()
