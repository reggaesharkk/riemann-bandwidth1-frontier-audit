from __future__ import annotations
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parent
data = json.loads((ROOT / "terminal17_authentic_input.json").read_text(encoding="utf-8-sig"))["children"]["left"]
reindex = json.loads((ROOT / "terminal17_catalog_reindex.json").read_text(encoding="utf-8"))
local = {int(k): int(v) for k, v in reindex["local_index_by_global_index"].items()}
rows = data["fifteen_models"]
assert len(rows) == 15 and all(r["kind"] == "segmented_constant" for r in rows)
assert sum(len(r["segments"]) for r in rows) == 375

def rat(s: str) -> str:
    x = Fraction(s)
    return f"⟨({x.numerator}), {x.denominator}⟩"

def q(s: str) -> str:
    x = Fraction(s)
    return f"({x.numerator}/{x.denominator})"

out = [
    "import Catalog17AllLookups",
    "import Zeta23.ThmD.Sextuple.CompositionalLeaf",
    "open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype",
    "noncomputable section",
    "namespace AuthenticCompact17",
    "open A1294FifteenBridge A1294Compact",
    "def catalog : Array MacroPiece := Catalog17.catalog",
]
for row in rows:
    i = int(row["pair_index_zero_based"])
    segs = []
    for seg in row["segments"]:
        source_ix = int(seg["catalog_index_zero_based"])
        assert local[source_ix] >= 0
        segs.append(
            "{ lo := " + rat(seg["segment"][0])
            + ", hi := " + rat(seg["segment"][1])
            + f", pieceRef := {local[source_ix]} }}"
        )
    out.append(f"def row{i} : CompactRow := .floor {rat(row['base'])} [\n" + ",\n".join(segs) + "]")

out.append(
    "def rows (p : Fin 15) : CompactRow := match p.val with "
    + " ".join(f"| {i} => row{i}" for i in range(14))
    + " | _ => row14"
)
box = data["box_exact"]
out.append(
    "def box : GapBox where\n"
    + "  lo := fun i => match i.val with "
    + " ".join(f"| {i} => {q(interval[0])}" for i, interval in enumerate(box[:4]))
    + f" | _ => {q(box[4][0])}\n"
    + "  hi := fun i => match i.val with "
    + " ".join(f"| {i} => {q(interval[1])}" for i, interval in enumerate(box[:4]))
    + f" | _ => {q(box[4][1])}"
)
out += [
    "def anchor : Fin 5 → ℚ := box.lo",
    "set_option maxRecDepth 4000 in",
    "theorem accepted : compactQuadraticLeafCheck catalog (647/50000) (1094977/5000000000) box anchor rows = true := by decide",
    "theorem accepted_original : compactQuadraticLeafCheck Catalog17.original (647/50000) (1094977/5000000000) box anchor rows = true := by",
    "  rw [Catalog17Identity.original_eq_catalog]",
    "  exact accepted",
    "theorem leaf_sound : ∀ ⦃g : Fin 5 → ℝ⦄, box.Holds g →",
    "    ((647/50000 : ℚ) : ℝ) ≤ sextupleEnergy g + ((1094977/5000000000 : ℚ) : ℝ) * sextupleSpan g :=",
    "  compactQuadraticLeafCheck_sound accepted_original",
    "#print accepted",
    "#print accepted_original",
    "#print leaf_sound",
    "#print axioms accepted",
    "#print axioms accepted_original",
    "#print axioms leaf_sound",
    "end AuthenticCompact17",
    "",
]
(ROOT / "AuthenticCompact17.lean").write_text("\n".join(out), encoding="utf-8")
print("generated AuthenticCompact17.lean with 15 rows and 375 segments")
