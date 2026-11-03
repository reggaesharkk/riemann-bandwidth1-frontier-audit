#!/usr/bin/env python3
"""Additive replay of the source atom's 48 labeled R400 placements.

Writes only the new audit evidence file.  Interval arithmetic is delegated to
the existing outward-rounded physical overlap routine; source ordering and
conjugation multiplicities are reconstructed here.
"""

from __future__ import annotations

import json
import re
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path

from mpmath import iv

from wp84_r400_filtered_connected_kernel import omega_interval
from wp84_source_weight_cone_audit import (
    WITNESS,
    exact_source_atom_data,
    ordered_partitions,
    orientation_vectors,
)


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "evidence" / "WP84_R400_SOURCE_INTERVAL_REPLAY.json"


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def unique_permutations(vector):
    found = []
    seen = set()
    for candidate in permutations(vector):
        if candidate not in seen:
            seen.add(candidate)
            found.append(candidate)
    return found


def build() -> dict:
    iv.dps = 28
    labeled_source = orientation_vectors()
    labeled_conjugate = tuple(tuple(-x for x in vector) for vector in labeled_source)
    labeled = labeled_source + labeled_conjugate
    require(len(labeled) == 48, "source/conjugate label count changed")
    require(len(set(labeled)) == 24, "expected 24 rational vectors after duplicate collapse")

    # Reconstruct by all slot permutations of the displayed source atom and
    # its conjugate.  Equality checks the six balanced orthants and orders.
    source_orders = unique_permutations(WITNESS)
    conjugate_orders = unique_permutations(tuple(-x for x in WITNESS))
    all_orders = source_orders + conjugate_orders
    require(len(source_orders) == 12 and len(conjugate_orders) == 12,
            "permutation multiplicities changed")
    require(set(all_orders) == set(labeled),
            "orthant generation and source/conjugate permutations disagree")

    for vector in all_orders:
        require(sum(vector, F(0)) == 0, "orientation is not closed")
        exact_grid_terms = []
        for coefficient, blocks in ordered_partitions():
            product_value = 1
            if len(blocks) == 1:
                exact_grid_terms.append(coefficient)
                continue
            for block in blocks:
                block_sum = sum((vector[index] for index in block), F(0))
                require(block_sum.denominator != 1,
                        f"nonleading block sum unexpectedly integral: {vector}, {block}")
                require((10 * block_sum).denominator == 1,
                        f"m=10 does not close a rational block frequency: {vector}, {block}")
                product_value = 0
            exact_grid_terms.append(coefficient * product_value)
        require(exact_grid_terms == [1] + [0] * 25,
                f"m=10 row-cumulant vector changed: {vector}")
    m10_lower = F(1) - 7 * F(2, 10) ** 2 - 12 * F(2, 10) ** 3 - 6 * F(2, 10) ** 4
    require(m10_lower == F(384, 625), "uniform row-cumulant lower bound arithmetic changed")

    cache = {}
    records = []
    for family, vector in (("source", v) for v in source_orders):
        records.append((family, vector, omega_interval(vector, 400, iv, cache)))
    for family, vector in (("conjugate", v) for v in conjugate_orders):
        records.append((family, vector, omega_interval(vector, 400, iv, cache)))

    threshold = iv.mpf(799) / 4000
    for _, vector, value in records:
        require(value > threshold, f"R400 overlap lower bound failed at {vector}: {value}")

    intervals = []
    for family, vector, value in records:
        match = re.fullmatch(r"\[([^,]+),\s*([^\]]+)\]", str(value))
        require(match is not None, "unexpected interval rendering")
        intervals.append({
            "family": family,
            "v": [str(x) for x in vector],
            "omega_interval": [match.group(1).strip(), match.group(2).strip()],
            "strictly_above_799_over_4000": True,
        })

    exact_source = exact_source_atom_data()
    require(exact_source["v"] == [str(x) for x in WITNESS], "source atom did not replay")
    return {
        "schema": "wp84.r400.source-interval-replay.v1",
        "source_atom": exact_source,
        "r400_overlap": {
            "labeled_source_placements": len(labeled_source),
            "labeled_conjugate_placements": len(labeled_conjugate),
            "total_labeled_placements": len(labeled),
            "unique_source_vectors": len(source_orders),
            "unique_conjugate_vectors": len(conjugate_orders),
            "unique_interval_evaluations": len(records),
            "method": "outward-rounded mpmath interval FFT using the inherited physical Omega_4,400 routine",
            "uniform_lower_bound": "every unique source/conjugate placement has Omega_4,400 > 799/4000",
            "placements": intervals,
        },
        "row_cumulant": {
            "exact_grid_replay": "at m=10, the signed 26-term vector is e_1 for every ordering",
            "uniform_m_ge_10_bound": "kappa_m >= 1 - 7*(2/m)^2 - 12*(2/m)^3 - 6*(2/m)^4 >= 384/625",
            "exact_rational_m10_lower_bound": str(m10_lower),
            "reason": "every proper block sum in all 48 placements is a noninteger multiple of 1/5; sin(pi/5)>1/2, so each finite geometric average has modulus <2/m; the full sum is zero and the one-block term is exactly 1",
        },
        "pointwise_result": "physical Omega_4,400*kappa_m > 9588/78125 for all 48 labeled source/conjugate placements and every m>=10",
        "scope_warning": "this is a pointwise proper-power-containing source atom family, not the ordinary-prime aggregate sign",
    }


def main() -> None:
    result = build()
    OUTPUT.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS source atom admission and all 48 labeled placements")
    print("PASS 24 outward-rounded R400 overlap intervals above 799/4000")
    print("PASS exact source/conjugate multiplicity and m>=10 row-cumulant bound")
    print(f"WROTE {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
