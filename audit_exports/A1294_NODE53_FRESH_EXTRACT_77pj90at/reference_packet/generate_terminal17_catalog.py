from __future__ import annotations
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parent
leaf=json.loads((ROOT/'terminal17_authentic_input.json').read_text(encoding='utf-8-sig'))['children']['left']
rows=leaf['fifteen_models']
refs=sorted({int(s['catalog_index_zero_based']) for row in rows for s in row['segments']} |
            {int(row['direct_catalog_index']) for row in rows if row.get('direct_catalog_index') is not None})
assert len(refs)==175
macro=[x for x in refs if x<56]
v1=[x for x in refs if 56<=x<272]
v3=[x for x in refs if x>=272]
assert (len(macro),len(v1),len(v3))==(21,154,0)
name=lambda ix: f'macroPiece{ix}' if ix<56 else f'refinementPiece{ix-56}' if ix<272 else f'refinement2Piece{ix-272}'
local={global_ix:i for i,global_ix in enumerate(refs)}
def arr(names): return '#['+', '.join(names)+']'

# Catalog declarations use blocks determined by the selected entries: the 21
# stable pieces and two consecutive 77-entry refinement blocks.
block_groups=(macro,v1[:77],v1[77:])
block_names=[[name(i) for i in group] for group in block_groups]
all_names=block_names[0]+block_names[1]+block_names[2]
cat=[]
cat += ['import Zeta23.ThmD.Sextuple.CompositionalLeaf','import GenericArrayIdentity',
        'open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype','noncomputable section',
        'namespace Catalog17']
cat += [f'def block{k} : Array MacroPiece := ([{", ".join(xs)}] : List MacroPiece).toArray'
        for k,xs in enumerate(block_names)]
cat += [f'def original : Array MacroPiece := {arr(all_names)}',
        'def catalog : Array MacroPiece := (block0 ++ block1) ++ block2',
        f'theorem size0 : block0.size = {len(macro)} := by decide',
        f'theorem size1 : block1.size = {len(block_groups[1])} := by decide',
        f'theorem size2 : block2.size = {len(block_groups[2])} := by decide',
        'end Catalog17','']
(ROOT/'Catalog17.lean').write_text('\n'.join(cat),encoding='utf-8')

ident=['import Catalog17','open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype',
       'namespace Catalog17Identity',
       'theorem original_eq_catalog : Catalog17.original = Catalog17.catalog := by',
       '  unfold Catalog17.original Catalog17.catalog Catalog17.block0 Catalog17.block1 Catalog17.block2',
       '  change ((['+', '.join(all_names)+'] : List MacroPiece).toArray) =',
       '    (((['+', '.join(block_names[0])+'] : List MacroPiece).toArray ++',
       '       (['+', '.join(block_names[1])+'] : List MacroPiece).toArray) ++',
       '       (['+', '.join(block_names[2])+'] : List MacroPiece).toArray)',
        '  exact CatalogArrayIdentity.toArray_append3 ['+', '.join(block_names[0])+'] ['+', '.join(block_names[1])+'] ['+', '.join(block_names[2])+']',
       '#print Catalog17Identity.original_eq_catalog',
       '#print axioms Catalog17Identity.original_eq_catalog','end Catalog17Identity','']
(ROOT/'Catalog17Identity.lean').write_text('\n'.join(ident),encoding='utf-8')

lookup=['import Catalog17Identity','open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype',
        'namespace Catalog17AllLookups']
lookup += [f'theorem block0_local_{j} : Catalog17.block0[{j}]? = some {name(g)} := by rfl' for j,g in enumerate(macro)]
lookup += [f'theorem block1_local_{j} : Catalog17.block1[{j}]? = some {name(g)} := by rfl' for j,g in enumerate(v1[:77])]
lookup += [f'theorem block2_local_{j} : Catalog17.block2[{j}]? = some {name(g)} := by rfl' for j,g in enumerate(v1[77:])]
for i,g in enumerate(refs):
    nm=name(g)
    lookup.append(f'theorem catalog_lookup_{i} : Catalog17.catalog[{i}]? = some {nm} := by')
    lookup.append('  unfold Catalog17.catalog')
    if i < len(macro):
        lookup.append('  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]')
        lookup.append('  rw [Array.getElem?_append_left (by rw [Catalog17.size0]; decide)]')
        lookup.append(f'  exact Catalog17.block0_local_{i}')
    elif i < len(macro)+len(v1[:77]):
        lookup.append('  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]')
        lookup.append('  rw [Array.getElem?_append_right (by rw [Catalog17.size0]; decide)]')
        lookup.append('  norm_num only [Catalog17.size0, Nat.reduceSub]')
        lookup.append(f'  exact Catalog17.block1_local_{i-len(macro)}')
    else:
        lookup.append('  rw [Array.getElem?_append_right (by rw [Array.size_append, Catalog17.size0, Catalog17.size1]; decide)]')
        lookup.append('  norm_num only [Array.size_append, Catalog17.size0, Catalog17.size1, Nat.reduceAdd, Nat.reduceSub]')
        lookup.append(f'  exact Catalog17.block2_local_{i-len(macro)-len(v1[:77])}')
    lookup.append(f'theorem original_lookup_{i} : Catalog17.original[{i}]? = some {nm} := by')
    lookup.append('  rw [Catalog17Identity.original_eq_catalog]')
    lookup.append(f'  exact catalog_lookup_{i}')
lookup += ['#print Catalog17Identity.original_eq_catalog',
           '#print Catalog17AllLookups.original_lookup_0',
           f'#print Catalog17AllLookups.original_lookup_{len(refs)-1}',
           '#print axioms Catalog17Identity.original_eq_catalog',
           '#print axioms Catalog17AllLookups.original_lookup_0',
           f'#print axioms Catalog17AllLookups.original_lookup_{len(refs)-1}',
           'end Catalog17AllLookups','']
(ROOT/'Catalog17AllLookups.lean').write_text('\n'.join(lookup),encoding='utf-8')
record={'source_global_indices_sorted':refs,'local_index_by_global_index':{str(g):local[g] for g in refs},
        'block_sizes':[len(block_groups[0]),len(block_groups[1]),len(block_groups[2])],'unique_sources':len(refs),
        'piece_ref_policy':'Each terminal-17 source global catalog reference is replaced by its order-preserving compact local index in the selected subset; model, coefficients, interval endpoints, and selected source declaration are unchanged.'}
(ROOT/'terminal17_catalog_reindex.json').write_text(json.dumps(record,indent=2,sort_keys=True)+'\n',encoding='utf-8')
print(f'generated original/selected catalog with block sizes {len(block_groups[0])}+{len(block_groups[1])}+{len(block_groups[2])}={len(refs)}; lookup theorems={len(refs)*2}')
