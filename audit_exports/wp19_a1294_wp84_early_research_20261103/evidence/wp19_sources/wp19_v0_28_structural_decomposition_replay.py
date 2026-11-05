#!/usr/bin/env python3
"""Exact-rational decomposition and impact replay for WP19 v0.28.

Inputs are the frozen M15-support weighted replay, forced-radius replay, and
the GitHub artifact ZIP from run 37049588602. This checks the artifact digest,
reconstructs the updated quadratic aggregate, reports 20-step shard sums,
and computes the uniform radius shrink required for a nonnegative budget.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import zipfile
from decimal import Decimal, getcontext
from fractions import Fraction
from pathlib import Path

ARTIFACT_SHA256 = "7186f6922efcaec2f3e612c18d68b2335319fa1c61a48a900703712f4828801f"
EXPECTED_Q = Fraction(Decimal("114093007395768.650060299107920939981122"))
EXPECTED_B = Fraction(Decimal("49545386543507.498269542068"))
EXPECTED_L = Fraction(Decimal("240063.832492240296"))
EXPECTED_P = Fraction(Decimal("5758574435.605829673039071"))


def frac(text: str) -> Fraction:
    return Fraction(Decimal(text))


def decimal(value: Fraction, places: int = 12) -> str:
    getcontext().prec = 80
    d = Decimal(value.numerator) / Decimal(value.denominator)
    return f"{d:.{places}f}"


def outward(value: Fraction, places: int = 24, upward: bool = True) -> str:
    scale = 10 ** places
    num = value.numerator * scale
    den = value.denominator
    units = -((-num) // den) if upward else num // den
    sign = "-" if units < 0 else ""
    digits = str(abs(units)).zfill(places + 1)
    return sign + digits[:-places] + "." + digits[-places:]


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--weighted", type=Path, required=True)
    ap.add_argument("--radius", type=Path, required=True)
    ap.add_argument("--artifact", type=Path, required=True)
    ap.add_argument("--output", type=Path, required=True)
    args = ap.parse_args()

    digest = hashlib.sha256(args.artifact.read_bytes()).hexdigest()
    if digest != ARTIFACT_SHA256:
        raise SystemExit(f"artifact digest mismatch: {digest}")
    weighted = json.loads(args.weighted.read_text())
    radius = json.loads(args.radius.read_text())
    with zipfile.ZipFile(args.artifact) as zf:
        target = json.loads(zf.read("target_steps_220_239.json"))
        aggregate = json.loads(zf.read("targeted_m15_quadratic_replay.json"))

    assert weighted["coverage"] == [0, 239]
    assert len(weighted["steps_detail"]) == len(radius["steps_detail"]) == 240
    assert [r["step"] for r in target["steps"]] == list(range(220, 240))
    assert aggregate["target_steps"] == [220, 239]

    H = Fraction(1, 80000)
    old_target = sum((frac(r["M15_support_corrected_quadratic_upper"])
                      for r in weighted["steps_detail"] if r["step"] >= 220), Fraction())
    new_target = sum((H * frac(radius["steps_detail"][n]["forced_error_L2_upper"]) ** 2
                      * frac(target["steps"][n - 220]["young_M15_support_upper"])
                      for n in range(220, 240)), Fraction())
    q_old = frac(weighted["M15_support_corrected_quadratic_integral_upper"])
    q_new = q_old - old_target + new_target
    L = frac(weighted["adjoint_defect_integral_upper"])
    B = frac(weighted["terminal_saved_adjoint_boundary_product_upper"])
    P = frac(weighted["frozen_signed_dual_integral_lower"])
    total = q_new + L + B
    margin = P - total

    expected = {
        "quadratic": frac(aggregate["full_path_quadratic_upper_with_target_replacement"]),
        "boundary": frac(aggregate["terminal_boundary_upper_retained"]),
        "linear": frac(aggregate["adjoint_defect_upper_retained_steps_0_239"]),
        "total": frac(aggregate["remainder_total_upper"]),
        "margin": frac(aggregate["signed_margin_lower"]),
    }
    if outward(q_new) != aggregate["full_path_quadratic_upper_with_target_replacement"]:
        raise SystemExit("quadratic outward-decimal mismatch")
    if outward(total) != aggregate["remainder_total_upper"]:
        raise SystemExit("total outward-decimal mismatch")
    # The workflow's ceil-decimal helper is also used on this negative lower
    # margin, which rounds it upward by less than one final-place unit. Report
    # the corrected floor below and flag the serialized direction issue.
    corrected_margin_lower = P - frac(aggregate["remainder_total_upper"])
    corrected_margin_lower_text = outward(corrected_margin_lower, upward=False)
    published_margin = aggregate["signed_margin_lower"]
    if frac(published_margin) - margin > Fraction(1, 10**24):
        raise SystemExit("published margin differs by more than one 24-place unit")

    shard_sums = []
    step_sums: list[tuple[int, Fraction]] = []
    for start in range(0, 240, 20):
        if start < 220:
            vals = [frac(r["M15_support_corrected_quadratic_upper"])
                    for r in weighted["steps_detail"][start:start + 20]]
        else:
            vals = [H * frac(radius["steps_detail"][n]["forced_error_L2_upper"]) ** 2
                    * frac(target["steps"][n - 220]["young_M15_support_upper"])
                    for n in range(start, start + 20)]
        step_sums.extend((start + i, v) for i, v in enumerate(vals))
        shard_sums.append({"steps": [start, start + 19],
                           "quadratic_upper_sum": decimal(sum(vals, Fraction()))})

    # If all path radii are uniformly multiplied by alpha, Q scales as alpha^2,
    # while L and B scale as alpha. Solve Q*a^2+(L+B)*a=P exactly by a
    # high-precision Decimal quadratic root, then report the corresponding E(T).
    getcontext().prec = 80
    qd = Decimal(q_new.numerator) / Decimal(q_new.denominator)
    sd = Decimal((L + B).numerator) / Decimal((L + B).denominator)
    pd = Decimal(P.numerator) / Decimal(P.denominator)
    alpha = (-sd + (sd * sd + 4 * qd * pd).sqrt()) / (2 * qd)
    Efinal = frac(radius["final_forced_error_L2_upper"])

    out = {
        "schema": "wp19-v0.28-structural-decomposition-replay-v1",
        "status": "PASS_EXACT_RATIONAL_AGGREGATE_REPLAY",
        "artifact_run": 37049588602,
        "artifact_id": 11251177469,
        "artifact_sha256": digest,
        "frozen_input_hashes": weighted["frozen_inputs"],
        "terms": {
            "whole_path_quadratic_upper": aggregate["full_path_quadratic_upper_with_target_replacement"],
            "terminal_boundary_upper": decimal(B, 24),
            "adjoint_defect_upper": decimal(L, 24),
            "signed_integral_lower": decimal(P, 24),
            "remainder_total_upper": decimal(total, 24),
            "signed_margin_lower_exact_difference": decimal(margin, 24),
            "signed_margin_lower_outward_floor_from_published_total": corrected_margin_lower_text,
            "published_signed_margin_decimal": published_margin,
            "published_margin_rounding_direction_issue": True,
            "remainder_to_signed_lower_ratio": decimal(total / P, 8),
        },
        "quadratic_20_step_shards": shard_sums,
        "largest_updated_step_quadratic_bounds": [
            {"step": n, "upper": decimal(v, 12)}
            for n, v in sorted(step_sums, key=lambda nv: nv[1], reverse=True)[:10]
        ],
        "impact": {
            "boundary_fraction_of_remainder": decimal(B / total, 8),
            "quadratic_fraction_of_remainder": decimal(q_new / total, 8),
            "margin_if_boundary_removed_only": decimal(P - (q_new + L), 12),
            "margin_if_quadratic_removed_only": decimal(P - (B + L), 12),
            "uniform_radius_scale_alpha_for_closure": str(alpha),
            "required_uniform_radius_reduction_factor": str(Decimal(1) / alpha),
            "corresponding_terminal_error_radius": decimal(Fraction(alpha) * Efinal, 12),
        },
        "method": "Parse all decimal strings as exact rationals; recompute the 220–239 replacement from the 192-bit Arb step coefficients and exact M15 radii; verify the published quadratic and total aggregates at their outward decimal precision.",
        "claim_boundary": "Finite-path remainder arithmetic only. This does not certify a joint signed estimate, an omitted terminal Taylor remainder, an all-cutoff result, or continuum regularity.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(out, indent=2, sort_keys=True) + "\n")
    print(json.dumps(out, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
