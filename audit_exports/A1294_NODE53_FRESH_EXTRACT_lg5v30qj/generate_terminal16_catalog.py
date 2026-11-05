from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent
leaf = json.loads((ROOT / "terminal16_authentic_input.json").read_text(encoding="utf-8-sig"))["children"]["left"]
rows = leaf["fifteen_models"]
refs = sorted(
    {int(s["catalog_index_zero_based"]) for row in rows for s in row["segments"]}
    | {int(row["direct_catalog_index"]) for row in rows if row.get("direct_catalog_index") is not None}
)
if len(rows) != 15 or not refs:
    raise SystemExit("terminal 16 data is incomplete")

def name(ix: int) -> str:
    if ix < 56:
        return f"macroPiece{ix}"
    if ix < 272:
        return f"refinementPiece{ix-56}"
    return f"refinement2Piece{ix-272}"

stable_count = sum(ix < 56 for ix in refs)
# The selected source array is kept in source-index order. Split its actual
# refinement tail into two nearly equal consecutive blocks; no prior leaf size
# is assumed.
groups = [refs[:stable_count]]
tail = refs[stable_count:]
cut = (len(tail) + 1) // 2
groups.extend((tail[:cut], tail[cut:]))
if sum(map(len, groups)) != len(refs) or [x for g in groups for x in g] != refs:
    raise SystemExit("catalog block partition is not an exact ordered partition")
names = [[name(ix) for ix in g] for g in groups]
flat = names[0] + names[1] + names[2]
local = {source_ix: local_ix for local_ix, source_ix in enumerate(refs)}

def le(xs: list[str]) -> str:
    return "[" + ", ".join(xs) + "]"

cat = [
    "import Zeta23.ThmD.Sextuple.CompositionalLeaf",
    "import GenericArrayIdentity",
    "open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype",
    "noncomputable section",
    "namespace Catalog16",
]
cat += [f"def refs{k} : List MacroPiece := {le(xs)}" for k, xs in enumerate(names)]
cat += [
    f"def original : Array MacroPiece := ({le(flat)} : List MacroPiece).toArray",
    "def block0 : Array MacroPiece := refs0.toArray",
    "def block1 : Array MacroPiece := refs1.toArray",
    "def block2 : Array MacroPiece := refs2.toArray",
    "def catalog : Array MacroPiece := (block0 ++ block1) ++ block2",
    f"theorem size0 : block0.size = {len(groups[0])} := by decide",
    f"theorem size1 : block1.size = {len(groups[1])} := by decide",
    f"theorem size2 : block2.size = {len(groups[2])} := by decide",
    "end Catalog16",
    "",
]
(ROOT / "Catalog16.lean").write_text("\n".join(cat), encoding="utf-8")

ident = [
    "import Catalog16",
    "open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype",
    "namespace Catalog16Identity",
    "theorem original_eq_catalog : Catalog16.original = Catalog16.catalog := by",
    "  unfold Catalog16.original Catalog16.catalog Catalog16.block0 Catalog16.block1 Catalog16.block2 Catalog16.refs0 Catalog16.refs1 Catalog16.refs2",
    "  change ((" + le(flat) + " : List MacroPiece).toArray) =",
    "    (((" + le(names[0]) + " : List MacroPiece).toArray ++",
    "       (" + le(names[1]) + " : List MacroPiece).toArray) ++",
    "       (" + le(names[2]) + " : List MacroPiece).toArray)",
    "  exact CatalogArrayIdentity.toArray_append3 " + le(names[0]) + " " + le(names[1]) + " " + le(names[2]),
    "#print Catalog16Identity.original_eq_catalog",
    "#print axioms Catalog16Identity.original_eq_catalog",
    "end Catalog16Identity",
    "",
]
(ROOT / "Catalog16Identity.lean").write_text("\n".join(ident), encoding="utf-8")

boundary = [
    "import Catalog16Identity",
    "open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype",
    "namespace Catalog16BoundaryBlocks",
    f"theorem local_block1_0 : Catalog16.block1[0]? = some {names[1][0]} := by rfl",
    f"theorem boundary_block1_0 : Catalog16.catalog[{len(groups[0])}]? = some {names[1][0]} := by",
    "  unfold Catalog16.catalog",
    "  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog16.size0, Catalog16.size1]; decide)]",
    "  rw [Array.getElem?_append_right (by rw [Catalog16.size0])]",
    "  norm_num only [Catalog16.size0, Nat.reduceSub]",
    "  exact local_block1_0",
    f"theorem local_block2_0 : Catalog16.block2[0]? = some {names[2][0]} := by rfl",
    f"theorem boundary_block2_0 : Catalog16.catalog[{len(groups[0])+len(groups[1])}]? = some {names[2][0]} := by",
    "  unfold Catalog16.catalog",
    "  rw [Array.getElem?_append_right (by rw [Array.size_append, Catalog16.size0, Catalog16.size1])]",
    "  norm_num only [Array.size_append, Catalog16.size0, Catalog16.size1, Nat.reduceAdd, Nat.reduceSub]",
    "  exact local_block2_0",
    "#print axioms boundary_block1_0",
    "#print axioms boundary_block2_0",
    "end Catalog16BoundaryBlocks",
    "",
]
(ROOT / "Catalog16BoundaryBlocks.lean").write_text("\n".join(boundary), encoding="utf-8")

lookups = [
    "import Catalog16BoundaryBlocks",
    "open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype",
    "namespace Catalog16AllLookups",
]
for j, source_ix in enumerate(groups[0]):
    lookups.append(f"theorem block0_local_{j} : Catalog16.block0[{j}]? = some {name(source_ix)} := by rfl")
for j, source_ix in enumerate(groups[1]):
    lookups.append(f"theorem block1_local_{j} : Catalog16.block1[{j}]? = some {name(source_ix)} := by rfl")
for j, source_ix in enumerate(groups[2]):
    lookups.append(f"theorem block2_local_{j} : Catalog16.block2[{j}]? = some {name(source_ix)} := by rfl")

cuts = (len(groups[0]), len(groups[0]) + len(groups[1]))
for i, source_ix in enumerate(refs):
    if i == cuts[0]:
        lookups += [f"theorem catalog_lookup_{i} : Catalog16.catalog[{i}]? = some {name(source_ix)} := by", "  exact Catalog16BoundaryBlocks.boundary_block1_0"]
    elif i == cuts[1]:
        lookups += [f"theorem catalog_lookup_{i} : Catalog16.catalog[{i}]? = some {name(source_ix)} := by", "  exact Catalog16BoundaryBlocks.boundary_block2_0"]
    else:
        lookups += [f"theorem catalog_lookup_{i} : Catalog16.catalog[{i}]? = some {name(source_ix)} := by", "  unfold Catalog16.catalog"]
        if i < cuts[0]:
            lookups += [
                "  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog16.size0, Catalog16.size1]; decide)]",
                "  rw [Array.getElem?_append_left (by rw [Catalog16.size0]; decide)]",
                f"  exact Catalog16AllLookups.block0_local_{i}",
            ]
        elif i < cuts[1]:
            lookups += [
                "  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog16.size0, Catalog16.size1]; decide)]",
                "  rw [Array.getElem?_append_right (by rw [Catalog16.size0]; decide)]",
                "  norm_num only [Catalog16.size0, Nat.reduceSub]",
                f"  exact Catalog16AllLookups.block1_local_{i-cuts[0]}",
            ]
        else:
            lookups += [
                "  rw [Array.getElem?_append_right (by rw [Array.size_append, Catalog16.size0, Catalog16.size1]; decide)]",
                "  norm_num only [Array.size_append, Catalog16.size0, Catalog16.size1, Nat.reduceAdd, Nat.reduceSub]",
                f"  exact Catalog16AllLookups.block2_local_{i-cuts[1]}",
            ]
    lookups += [
        f"theorem original_lookup_{i} : Catalog16.original[{i}]? = some {name(source_ix)} := by",
        "  rw [Catalog16Identity.original_eq_catalog]",
        f"  exact catalog_lookup_{i}",
    ]
lookups += [
    "#print Catalog16Identity.original_eq_catalog",
    "#print Catalog16AllLookups.original_lookup_0",
    f"#print Catalog16AllLookups.original_lookup_{len(refs)-1}",
    "#print axioms Catalog16Identity.original_eq_catalog",
    "#print axioms Catalog16AllLookups.original_lookup_0",
    f"#print axioms Catalog16AllLookups.original_lookup_{len(refs)-1}",
    "end Catalog16AllLookups",
    "",
]
(ROOT / "Catalog16AllLookups.lean").write_text("\n".join(lookups), encoding="utf-8")

reindex = {
    "source_global_indices_sorted": refs,
    "local_index_by_global_index": {str(g): local[g] for g in refs},
    "block_sizes": [len(g) for g in groups],
    "unique_sources": len(refs),
    "category_counts": {"stable": sum(i < 56 for i in refs), "refinement_v1": sum(56 <= i < 272 for i in refs), "refinement_v3": sum(i >= 272 for i in refs)},
    "piece_ref_policy": "Original selected catalog declaration references are retained in sorted source-index order. Only local indices are introduced for the compact certificate; declarations and source coefficients are unchanged.",
}
(ROOT / "terminal16_catalog_reindex.json").write_text(json.dumps(reindex, indent=2, sort_keys=True) + "\n", encoding="utf-8")
print(f"terminal16 selected references={len(refs)}; source classes={reindex['category_counts']}; ordered block sizes={reindex['block_sizes']}; original lookups={len(refs)}")
