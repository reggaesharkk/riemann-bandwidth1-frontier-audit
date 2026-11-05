import json
from pathlib import Path
root = Path(__file__).resolve().parent
leaf = json.loads((root / "terminal17_authentic_input.json").read_text(encoding="utf-8-sig"))["children"]["left"]
rows = leaf["fifteen_models"]
refs = sorted({int(s["catalog_index_zero_based"]) for row in rows for s in row["segments"]} | {int(row["direct_catalog_index"]) for row in rows if row.get("direct_catalog_index") is not None})
macro = [x for x in refs if x < 56]
v1 = [x for x in refs if 56 <= x < 272]
groups = (macro, v1[:77], v1[77:])
def name(ix): return f"macroPiece{ix}" if ix < 56 else f"refinementPiece{ix-56}"
indices = [0, 20, 21, 97, 98, 174]
out = ["import Catalog17BoundaryBlocks", "open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype", "namespace Catalog17LookupSmoke"]
for i in indices:
    g = refs[i]
    if i < 21:
        block, j = 0, i
    elif i < 98:
        block, j = 1, i-21
    else:
        block, j = 2, i-98
    out += [f"theorem catalog_{i} : Catalog17.catalog[{i}]? = some {name(g)} := by"]
    if i == 21:
        out += ["  exact Catalog17BoundaryBlocks.boundary_block1_0"]
    elif i == 98:
        out += ["  exact Catalog17BoundaryBlocks.boundary_block2_0"]
    else:
        out += ["  unfold Catalog17.catalog"]
    if i in (21, 98):
        pass
    elif block == 0:
        out += ["  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]", "  rw [Array.getElem?_append_left (by rw [Catalog17.size0]; decide)]", f"  rfl"]
    elif block == 1:
        out += ["  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]"]
        if i != 21:
            out += ["  rw [Array.getElem?_append_right (by rw [Catalog17.size0]; decide)]", "  norm_num only [Catalog17.size0, Nat.reduceSub]", "  rfl"]
    else:
        out += ["  rw [Array.getElem?_append_right (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]"]
        if i != 98:
            out += ["  norm_num only [Array.size_append, Catalog17.size0, Catalog17.size1, Nat.reduceAdd, Nat.reduceSub]", "  rfl"]
    out += [f"theorem original_{i} : Catalog17.original[{i}]? = some {name(g)} := by", f"  rw [Catalog17Identity.original_eq_catalog]", f"  exact catalog_{i}", f"#print axioms original_{i}"]
out += ["end Catalog17LookupSmoke", ""]
(root / "Catalog17LookupSmoke.lean").write_text("\n".join(out), encoding="utf-8")
print("generated boundary lookups", indices)
