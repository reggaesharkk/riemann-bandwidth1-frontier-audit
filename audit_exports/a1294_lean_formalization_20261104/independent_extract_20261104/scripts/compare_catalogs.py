#!/usr/bin/env python3
"""Exact rational comparison of the frozen V2 catalog JSON with pinned Lean declarations.

This checks model fields and declaration order. The JSON-only `stable_piece_index`
metadata is reported separately because `MacroPiece` does not carry ownership.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from fractions import Fraction
from pathlib import Path


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def q(s: str) -> Fraction:
    return Fraction(s.strip().strip("() "))


def decls(path: Path, prefix: str) -> dict[int, str]:
    raw = path.read_text(encoding="utf-8")
    matches = list(re.finditer(rf"(?m)^def {re.escape(prefix)}(\d+)\s*:\s*MacroPiece\s*:=", raw))
    out: dict[int, str] = {}
    for pos, m in enumerate(matches):
        end = matches[pos + 1].start() if pos + 1 < len(matches) else len(raw)
        out[int(m.group(1))] = raw[m.end():end].strip()
    return out


def parse_piece(expr: str) -> dict:
    box = re.search(r"box\s*:=\s*⟨\s*([^,]+?)\s*,\s*([^⟩]+?)\s*⟩", expr)
    if not box:
        raise ValueError(f"missing box in {expr[:120]!r}")
    lo, hi = q(box.group(1)), q(box.group(2))
    if expr.startswith(".well"):
        vals = {}
        for key in ("side", "positive", "q", "v", "m", "turn"):
            m = re.search(rf"\b{key}\s*:=\s*([^,}}]+)", expr)
            if not m:
                raise ValueError(f"missing {key} in {expr[:120]!r}")
            vals[key] = m.group(1).strip()
        return {
            "kind": "well", "lo": lo, "hi": hi,
            "side": vals["side"].lstrip("."),
            "positive": vals["positive"] == "true",
            "q": q(vals["q"]), "v": q(vals["v"]), "m": q(vals["m"]),
            "turn": int(vals["turn"]),
        }
    if expr.startswith(".base"):
        a = re.search(r"\ba\s*:=\s*([^,}}]+)", expr)
        kind = re.search(r"\bkind\s*:=\s*\.(low|zero|numeric)", expr)
        if not a or not kind:
            raise ValueError(f"missing base fields in {expr[:120]!r}")
        k = {"low": "low", "zero": "zero", "numeric": "barrier"}[kind.group(1)]
        out = {"kind": k, "lo": lo, "hi": hi, "a": q(a.group(1))}
        if k == "barrier":
            cells = re.findall(
                r"\{\s*box\s*:=\s*⟨\s*([^,]+?)\s*,\s*([^⟩]+?)\s*⟩\s*,\s*turn\s*:=\s*(\d+)\s*\}",
                expr,
            )
            out["cells"] = [(q(a), q(b), int(t)) for a, b, t in cells]
        return out
    raise ValueError(f"unknown MacroPiece constructor: {expr[:100]!r}")


def json_piece(raw: dict) -> dict:
    # The v1 refinement schema is all well pieces and omits the redundant kind tag.
    k = raw.get("kind", "well")
    out = {"kind": k, "lo": q(raw["lo"]), "hi": q(raw["hi"])}
    if k == "well":
        out.update({
            "side": raw["side"], "positive": raw["positive"],
            "q": q(raw["q"]), "v": q(raw["v"]), "m": q(raw["m"]),
            "turn": int(raw["turn"]),
        })
    elif k in ("low", "zero"):
        out["a"] = q(raw["a"])
    elif k == "barrier":
        out["a"] = q(raw["a"])
        out["cells"] = [(q(c["lo"]), q(c["hi"]), int(c["turn"])) for c in raw["cells"]]
    else:
        raise ValueError(f"unknown JSON kind {k!r}")
    return out


def compare(label: str, json_path: Path, lean_path: Path, prefix: str, expected: int):
    items = json.loads(json_path.read_text(encoding="utf-8"))["pieces"]
    code = decls(lean_path, prefix)
    mismatches = []
    if len(items) != expected or len(code) != expected or sorted(code) != list(range(expected)):
        mismatches.append({"count_json": len(items), "count_lean": len(code), "expected": expected})
    for i, raw in enumerate(items):
        try:
            got = parse_piece(code[i])
            want = json_piece(raw)
            if got != want:
                mismatches.append({"index": i, "json": repr(want), "lean": repr(got)})
        except Exception as e:
            mismatches.append({"index": i, "error": repr(e)})
    owner = [raw.get("stable_piece_index") for raw in items]
    return {
        "catalog": label,
        "json_count": len(items),
        "lean_declaration_count": len(code),
        "exact_model_field_matches": len(items) - sum(1 for x in mismatches if "index" in x),
        "mismatch_count": len(mismatches),
        "owner_metadata_count": sum(x is not None for x in owner),
        "owner_metadata_sha256_canonical_json": hashlib.sha256(
            json.dumps(owner, separators=(",", ":")).encode()
        ).hexdigest(),
        "json_sha256": sha256(json_path),
        "lean_file_sha256": sha256(lean_path),
        "mismatches": mismatches[:5],
    }


def main() -> int:
    if len(sys.argv) != 3:
        raise SystemExit("usage: compare_catalogs.py <v2-package-root> <pinned-zeta23-root>")
    package, project = Path(sys.argv[1]), Path(sys.argv[2])
    data = package / "data"
    sext = project / "Zeta23/ThmD/Sextuple"
    reports = [
        compare("stable", data / "macro-data-exact.json", sext / "Macro/EnvelopeData.lean", "macroPiece", 56),
        compare("refinement_v1", data / "refinement-catalog-v1-exact.json", sext / "A1275/RefinementData.lean", "refinementPiece", 216),
        compare("refinement_v2", data / "refinement-catalog-v3.json", sext / "A1290/RefinementData2.lean", "refinement2Piece", 394),
    ]
    print(json.dumps(reports, indent=2, sort_keys=True))
    return 0 if all(r["mismatch_count"] == 0 for r in reports) else 1


if __name__ == "__main__":
    raise SystemExit(main())
