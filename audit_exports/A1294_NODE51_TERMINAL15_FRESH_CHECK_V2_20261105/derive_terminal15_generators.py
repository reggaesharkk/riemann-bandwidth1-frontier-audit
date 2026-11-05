from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
V4 = ROOT.parent / "A1294_NODE53_TERMINAL16_20261105"

def replace_exact(text: str, old: str, new: str, label: str) -> str:
    if old not in text:
        raise SystemExit(f"missing expected source fragment while deriving {label}: {old}")
    return text.replace(old, new)

catalog = (V4 / "generate_terminal16_catalog.py").read_text(encoding="utf-8-sig")
catalog = catalog.replace("terminal16", "terminal15").replace("Catalog16", "Catalog15")
(ROOT / "generate_terminal15_catalog.py").write_text(catalog, encoding="utf-8")

leaf = (V4 / "generate_terminal16_compositional.py").read_text(encoding="utf-8-sig")
leaf = (leaf.replace("terminal16", "terminal15")
        .replace("terminal-16", "terminal-15")
        .replace("Terminal16", "Terminal15")
        .replace("Catalog16", "Catalog15")
        .replace("AuthenticCompact16", "AuthenticCompact15"))
leaf = replace_exact(
    leaf,
    'assert len(rows) == 15 and all(r["kind"] == "segmented_constant" for r in rows)\nassert sum(len(r["segments"]) for r in rows) == 357\nassert all(Fraction(r["weight"]) == 0 and Fraction(r["offset"]) == 0 for r in rows)',
    'if len(rows) != 15 or not all(r["kind"] == "segmented_constant" for r in rows):\n    raise SystemExit("terminal 15 must have exactly fifteen segmented-constant rows")\nif sum(len(r["segments"]) for r in rows) != 369:\n    raise SystemExit("terminal 15 segment occurrence count mismatch")\nif not all(Fraction(r["weight"]) == 0 and Fraction(r["offset"]) == 0 for r in rows):\n    raise SystemExit("terminal 15 model weights/offsets are not the source constants")',
    "compositional leaf generator",
)
(ROOT / "generate_terminal15_compositional.py").write_text(leaf, encoding="utf-8")
print("derived terminal-15 catalog and compositional generators; optimizer-independent input guards are explicit")
