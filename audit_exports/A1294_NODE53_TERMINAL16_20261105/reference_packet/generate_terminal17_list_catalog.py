from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
leaf = json.loads((ROOT / "terminal17_authentic_input.json").read_text(encoding="utf-8-sig"))["children"]["left"]
rows = leaf["fifteen_models"]
refs = sorted(
    {int(s["catalog_index_zero_based"]) for row in rows for s in row["segments"]}
    | {int(row["direct_catalog_index"]) for row in rows if row.get("direct_catalog_index") is not None}
)
assert len(refs) == 175
macro = [x for x in refs if x < 56]
v1 = [x for x in refs if 56 <= x < 272]
v3 = [x for x in refs if x >= 272]
assert (len(macro), len(v1), len(v3)) == (21, 154, 0)
name = lambda ix: f"macroPiece{ix}" if ix < 56 else f"refinementPiece{ix-56}" if ix < 272 else f"refinement2Piece{ix-272}"
local = {global_ix: i for i, global_ix in enumerate(refs)}
groups = (macro, v1[:77], v1[77:])
names = [[name(i) for i in group] for group in groups]
flat_names = names[0] + names[1] + names[2]

def list_expr(xs: list[str]) -> str:
    return "[" + ", ".join(xs) + "]"

cat = [
    "import Zeta23.ThmD.Sextuple.CompositionalLeaf",
    "import GenericArrayIdentity",
    "open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype",
    "noncomputable section",
    "namespace Catalog17",
]
cat += [f"def refs{k} : List MacroPiece := {list_expr(xs)}" for k, xs in enumerate(names)]
cat += [
    f"def original : Array MacroPiece := ({list_expr(flat_names)} : List MacroPiece).toArray",
    "def block0 : Array MacroPiece := refs0.toArray",
    "def block1 : Array MacroPiece := refs1.toArray",
    "def block2 : Array MacroPiece := refs2.toArray",
    "def catalog : Array MacroPiece := (block0 ++ block1) ++ block2",
    f"theorem size0 : block0.size = {len(groups[0])} := by decide",
    f"theorem size1 : block1.size = {len(groups[1])} := by decide",
    f"theorem size2 : block2.size = {len(groups[2])} := by decide",
    "end Catalog17",
    "",
]
(ROOT / "Catalog17.lean").write_text("\n".join(cat), encoding="utf-8")

ident = [
    "import Catalog17",
    "open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype",
    "namespace Catalog17Identity",
    "theorem original_eq_catalog : Catalog17.original = Catalog17.catalog := by",
    "  unfold Catalog17.original Catalog17.catalog Catalog17.block0 Catalog17.block1 Catalog17.block2 Catalog17.refs0 Catalog17.refs1 Catalog17.refs2",
    "  change ((" + list_expr(flat_names) + " : List MacroPiece).toArray) =",
    "    (((" + list_expr(names[0]) + " : List MacroPiece).toArray ++",
    "       (" + list_expr(names[1]) + " : List MacroPiece).toArray) ++",
    "       (" + list_expr(names[2]) + " : List MacroPiece).toArray)",
    "  exact CatalogArrayIdentity.toArray_append3 " + list_expr(names[0]) + " " + list_expr(names[1]) + " " + list_expr(names[2]),
    "#print Catalog17Identity.original_eq_catalog",
    "#print axioms Catalog17Identity.original_eq_catalog",
    "end Catalog17Identity",
    "",
]
(ROOT / "Catalog17Identity.lean").write_text("\n".join(ident), encoding="utf-8")

lookup = [
    "import Catalog17BoundaryBlocks",
    "open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype",
    "namespace Catalog17AllLookups",
]
lookup += [f"theorem block0_local_{j} : Catalog17.block0[{j}]? = some {name(g)} := by rfl" for j, g in enumerate(macro)]
lookup += [f"theorem block1_local_{j} : Catalog17.block1[{j}]? = some {name(g)} := by rfl" for j, g in enumerate(v1[:77])]
lookup += [f"theorem block2_local_{j} : Catalog17.block2[{j}]? = some {name(g)} := by rfl" for j, g in enumerate(v1[77:])]

for i, g in enumerate(refs):
    nm = name(g)
    lookup += [f"theorem catalog_lookup_{i} : Catalog17.catalog[{i}]? = some {nm} := by"]
    if i == 21:
        lookup.append("  exact Catalog17BoundaryBlocks.boundary_block1_0")
    elif i == 98:
        lookup.append("  exact Catalog17BoundaryBlocks.boundary_block2_0")
    else:
        lookup.append("  unfold Catalog17.catalog")
    if i in (21, 98):
        pass
    elif i < len(macro):
        lookup += [
            "  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]",
            "  rw [Array.getElem?_append_left (by rw [Catalog17.size0]; decide)]",
            f"  exact Catalog17AllLookups.block0_local_{i}",
        ]
    elif i < len(macro) + len(v1[:77]):
        lookup += [
            "  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]",
            "  rw [Array.getElem?_append_right (by rw [Catalog17.size0]; decide)]",
            "  norm_num only [Catalog17.size0, Nat.reduceSub]",
            f"  exact Catalog17AllLookups.block1_local_{i-len(macro)}",
        ]
    else:
        lookup += [
            "  rw [Array.getElem?_append_right (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]",
            "  norm_num only [Array.size_append, Catalog17.size0, Catalog17.size1, Nat.reduceAdd, Nat.reduceSub]",
            f"  exact Catalog17AllLookups.block2_local_{i-len(macro)-len(v1[:77])}",
        ]
    lookup += [
        f"theorem original_lookup_{i} : Catalog17.original[{i}]? = some {nm} := by",
        "  rw [Catalog17Identity.original_eq_catalog]",
        f"  exact catalog_lookup_{i}",
    ]

lookup += [
    "#print Catalog17Identity.original_eq_catalog",
    "#print Catalog17AllLookups.original_lookup_0",
    f"#print Catalog17AllLookups.original_lookup_{len(refs)-1}",
    "#print axioms Catalog17Identity.original_eq_catalog",
    "#print axioms Catalog17AllLookups.original_lookup_0",
    f"#print axioms Catalog17AllLookups.original_lookup_{len(refs)-1}",
    "end Catalog17AllLookups",
    "",
]
(ROOT / "Catalog17AllLookups.lean").write_text("\n".join(lookup), encoding="utf-8")

record = {
    "source_global_indices_sorted": refs,
    "local_index_by_global_index": {str(g): local[g] for g in refs},
    "block_sizes": list(map(len, groups)),
    "unique_sources": len(refs),
    "piece_ref_policy": "Each terminal-17 source global catalog reference is remapped to its order-preserving local selected-catalog index. Model declarations, coefficients, interval endpoints, and source selection are unchanged.",
}
(ROOT / "terminal17_catalog_reindex.json").write_text(json.dumps(record, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"generated list-backed original/selected catalog with blocks {len(groups[0])}+{len(groups[1])}+{len(groups[2])}={len(refs)}; lookup theorems={len(refs)*2}")
