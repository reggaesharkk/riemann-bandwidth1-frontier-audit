#!/usr/bin/env python3
"""Independent exact point evaluator for the frozen A1294 catalog witness.

This intentionally does not import the branch-and-bound checker.  It reads the
three catalog JSON files and evaluates every catalog model whose closed domain
contains each of the 15 partial sums of the five-coordinate rational point.
Only Python's standard library is used.
"""

from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def need(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def F(value: object) -> Fraction:
    if isinstance(value, Fraction):
        return value
    return Fraction(str(value))


def read_json(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def model(row: dict, *, force_well: bool = False) -> tuple[Fraction, Fraction, Fraction, Fraction, str]:
    lo, hi = F(row["lo"]), F(row["hi"])
    kind = "well" if force_well else row["kind"]
    if kind in ("low", "barrier", "zero"):
        return lo, hi, Fraction(0), F(row.get("a", "0")), kind
    need(kind == "well", f"unknown catalog model kind: {kind!r}")
    m, v, endpoint = F(row["m"]), F(row["v"]), F(row["q"])
    center = endpoint + v / m if row["side"] == "left" else endpoint - v / m
    return lo, hi, center, 2 * m * m, kind


def digest(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as stream:
        for block in iter(lambda: stream.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def run(root: Path) -> dict:
    data = root / "evidence" / "local" / "C_Users_Asus_Downloads" / "A1294_LOCAL_BENCHMARK" / "A1294_LOCAL_BENCHMARK_PACKAGE" / "data"
    stable_path = data / "macro-data-exact.json"
    v1_path = data / "refinement-catalog-v1-exact.json"
    v3_path = data / "refinement-catalog-v3.json"
    stable_rows = read_json(stable_path)["pieces"]
    v1_rows = read_json(v1_path)["pieces"]
    v3_rows = read_json(v3_path)["pieces"]
    need(len(stable_rows) == 56, "stable catalog count changed")
    need(len(v1_rows) == 216, "v1 refinement count changed")
    need(len(v3_rows) == 394, "v3 catalog count changed")

    models = []
    for idx, row in enumerate(stable_rows):
        models.append((model(row), f"stable:{idx}"))
    for idx, row in enumerate(v1_rows):
        models.append((model(row, force_well=True), f"v1:{idx}"))
    for idx, row in enumerate(v3_rows):
        models.append((model(row), f"v3:{idx}"))

    point = tuple(map(F, ("6912667/1048576", "6541989/524288", "860015/131072", "13083885/1048576", "6912651/1048576")))
    need(len(point) == 5 and all(x > 0 for x in point), "witness is not a positive five-vector")
    span = sum(point, Fraction(0))
    partials = [(i, j) for i in range(5) for j in range(i, 5)]
    need(len(partials) == 15, "expected the 15 contiguous partial sums")

    ledger = []
    envelope_sum = Fraction(0)
    for i, j in partials:
        x = sum(point[i : j + 1], Fraction(0))
        candidates = []
        for (lo, hi, center, coefficient, kind), label in models:
            if lo <= x <= hi:
                value = coefficient * (x - center) ** 2 if kind == "well" else coefficient
                candidates.append((value, label, kind, lo, hi, center, coefficient))
        need(bool(candidates), f"catalog gap at exact partial sum {i}:{j}={x}")
        # Maximize the certified pointwise lower model. Stable iteration order
        # gives deterministic tie handling.
        best = max(candidates, key=lambda entry: entry[0])
        value, label, kind, lo, hi, center, coefficient = best
        envelope_sum += value
        ledger.append({
            "partial": [i, j], "x": str(x), "owner": label, "kind": kind,
            "model_interval": [str(lo), str(hi)], "center_or_constant": str(center),
            "quadratic_coefficient": str(coefficient), "exact_value": str(value),
            "candidate_models": len(candidates),
        })

    B = Fraction(1094977, 5000000000)
    value = envelope_sum + B * span
    target_As = [Fraction(n, 100000) for n in (1294, 1295, 1296, 1297, 1298, 1299, 12994, 1300)]
    target_results = []
    for A in target_As:
        margin = value - A
        target_results.append({"A": str(A), "margin_value_minus_A": str(margin), "strictly_exceeds": margin > 0})

    cutoff_1294 = Fraction(1294, 100000) / B
    need(span < cutoff_1294, "witness span exceeds the tightest target cutoff")
    need(span < 60, "witness span is outside the five-variable root domain")
    expected = Fraction(
        1739674247820415045342527228267900485813207074499,
        134217728000000000000000000000000000000000000000000,
    )
    need(value == expected, f"independent catalog evaluation mismatch: got {value}")
    need([entry["strictly_exceeds"] for entry in target_results] == [True, True, True, False, False, False, False, False], "unexpected threshold classification")

    return {
        "point": [str(x) for x in point],
        "span": str(span),
        "B": str(B),
        "tightest_cutoff_A_over_B": str(cutoff_1294),
        "catalog_piece_counts": {"stable": len(stable_rows), "v1": len(v1_rows), "v3": len(v3_rows), "total_models": len(models)},
        "E6_exact": str(envelope_sum),
        "B_span_exact": str(B * span),
        "value_exact": str(value),
        "value_decimal_17dp": f"{float(value):.17f}",
        "target_margins": target_results,
        "partial_ledger": ledger,
        "input_sha256": {p.name: digest(p) for p in (stable_path, v1_path, v3_path)},
        "method": "stdlib Fraction; scans all closed-domain models from the source catalogs; no branch-and-bound checker imported",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = run(args.root.resolve())
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.output:
        args.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")


if __name__ == "__main__":
    main()
