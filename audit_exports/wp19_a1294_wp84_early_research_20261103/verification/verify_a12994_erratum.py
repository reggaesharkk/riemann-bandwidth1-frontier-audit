#!/usr/bin/env python3
"""Exact, standard-library replay of the 666-model A1294 point witness.

Run from the packet root with:
    python verification/verify_a12994_erratum.py

The target list uses explicit fractions so the historical A12994 denominator
error cannot be reintroduced by a shared integer-scaling shortcut.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from fractions import Fraction
from pathlib import Path


def need(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def F(x: object) -> Fraction:
    return x if isinstance(x, Fraction) else Fraction(str(x))


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1 << 20), b""):
            h.update(block)
    return h.hexdigest()


def model(row: dict, force_well: bool = False):
    lo, hi = F(row["lo"]), F(row["hi"])
    kind = "well" if force_well else row["kind"]
    if kind in ("low", "barrier", "zero"):
        return lo, hi, Fraction(0), F(row.get("a", "0")), kind
    need(kind == "well", f"unexpected model kind: {kind!r}")
    m, v, q = F(row["m"]), F(row["v"]), F(row["q"])
    center = q + v / m if row["side"] == "left" else q - v / m
    return lo, hi, center, 2 * m * m, kind


TARGETS = [
    ("A1294", Fraction(1294, 100000)),
    ("A1295", Fraction(1295, 100000)),
    ("A1296", Fraction(1296, 100000)),
    ("A1297", Fraction(1297, 100000)),
    ("A1298", Fraction(1298, 100000)),
    ("A1299", Fraction(1299, 100000)),
    ("A12994", Fraction(12994, 1000000)),
    ("A1300", Fraction(1300, 100000)),
]
EXPECTED_MARGINS = [
    Fraction(2896847500415045342527228267900485813207074499, 134217728000000000000000000000000000000000000000000),
    Fraction(1554670220415045342527228267900485813207074499, 134217728000000000000000000000000000000000000000000),
    Fraction(212492940415045342527228267900485813207074499, 134217728000000000000000000000000000000000000000000),
    Fraction(-1129684339584954657472771732099514186792925501, 134217728000000000000000000000000000000000000000000),
    Fraction(-2471861619584954657472771732099514186792925501, 134217728000000000000000000000000000000000000000000),
    Fraction(-3814038899584954657472771732099514186792925501, 134217728000000000000000000000000000000000000000000),
    Fraction(-4350909811584954657472771732099514186792925501, 134217728000000000000000000000000000000000000000000),
    Fraction(-5156216179584954657472771732099514186792925501, 134217728000000000000000000000000000000000000000000),
]
EXPECTED_VALUE = Fraction(
    1739674247820415045342527228267900485813207074499,
    134217728000000000000000000000000000000000000000000,
)


def run(root: Path) -> dict:
    data = root / "evidence" / "catalogs"
    files = [data / "macro-data-exact.json", data / "refinement-catalog-v1-exact.json", data / "refinement-catalog-v3.json"]
    docs = [json.loads(p.read_text(encoding="utf-8")) for p in files]
    rows = [docs[0]["pieces"], docs[1]["pieces"], docs[2]["pieces"]]
    need([len(x) for x in rows] == [56, 216, 394], "catalog piece counts changed")
    models = []
    for i, row in enumerate(rows[0]):
        models.append((model(row), f"stable:{i}"))
    for i, row in enumerate(rows[1]):
        models.append((model(row, True), f"v1:{i}"))
    for i, row in enumerate(rows[2]):
        models.append((model(row), f"v3:{i}"))

    g = tuple(map(F, ("6912667/1048576", "6541989/524288", "860015/131072", "13083885/1048576", "6912651/1048576")))
    need(len(g) == 5 and all(x > 0 for x in g), "witness positivity failed")
    span = sum(g, Fraction(0))
    partials = [(i, j) for i in range(5) for j in range(i, 5)]
    need(len(partials) == 15, "expected 15 contiguous partial sums")
    envelope = Fraction(0)
    ledger = []
    for i, j in partials:
        x = sum(g[i:j + 1], Fraction(0))
        candidates = []
        for (lo, hi, center, coeff, kind), label in models:
            if lo <= x <= hi:
                y = coeff * (x - center) ** 2 if kind == "well" else coeff
                candidates.append((y, label))
        need(bool(candidates), f"catalog gap at partial {i}:{j}={x}")
        best, owner = max(candidates, key=lambda t: t[0])
        envelope += best
        ledger.append({"partial": [i, j], "x": str(x), "owner": owner, "candidate_models": len(candidates), "value": str(best)})

    B = Fraction(1094977, 5000000000)
    value = envelope + B * span
    need(value == EXPECTED_VALUE, "exact catalog evaluation differs from frozen witness")
    need(span < Fraction(1294, 100000) / B and span < 60, "witness is outside the tightest admissible cutoff")
    margins = []
    for (label, A), expected in zip(TARGETS, EXPECTED_MARGINS):
        margin = value - A
        need(margin == expected, f"exact margin mismatch for {label}")
        margins.append({"target": label, "A": str(A), "V_minus_A": str(margin), "sign": "positive" if margin > 0 else "negative"})
    need(str(TARGETS[6][1]) == "6497/500000", "A12994 denominator guard failed")
    return {
        "status": "PASS",
        "point": [str(x) for x in g],
        "span": str(span),
        "B": str(B),
        "catalog_piece_counts": [56, 216, 394],
        "catalog_model_count": len(models),
        "contiguous_partial_sum_count": len(partials),
        "E6_exact": str(envelope),
        "B_span_exact": str(B * span),
        "V_exact": str(value),
        "V_decimal_20dp": f"{float(value):.20f}",
        "margins": margins,
        "partial_sum_ledger": ledger,
        "catalog_sha256": {p.name: sha(p) for p in files},
        "arithmetic": "fractions.Fraction; explicit target fractions; no project checker imported",
    }


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    p.add_argument("--output", type=Path)
    a = p.parse_args()
    result = run(a.root.resolve())
    encoded = json.dumps(result, sort_keys=True, indent=2) + "\n"
    if a.output:
        a.output.parent.mkdir(parents=True, exist_ok=True)
        a.output.write_text(encoded, encoding="utf-8")
    print(encoded, end="")


if __name__ == "__main__":
    main()
