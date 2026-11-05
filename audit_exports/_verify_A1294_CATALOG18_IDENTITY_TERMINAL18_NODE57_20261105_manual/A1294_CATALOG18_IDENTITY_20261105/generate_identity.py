import pathlib, re
base = pathlib.Path('audit_exports/sharkbridge01_worktree/A1294_VRK_BRIDGE_20261105')
src = (base / 'Catalog18Lookup.lean').read_text(encoding='utf-8')
def block(name):
    m = re.search(rf'^def {name} : Array MacroPiece := #\[(.*?)\]$', src, re.M)
    if not m:
        raise SystemExit(f'missing {name}')
    return [x.strip() for x in m.group(1).split(',')]
blocks = [block('block0'), block('block1'), block('block2')]
orig = block('original')
assert list(map(len, blocks)) == [57, 57, 57]
assert len(orig) == 171
fmt = lambda xs: '[' + ', '.join(xs) + ']'
text = '''import Zeta23.ThmD.Sextuple.CompositionalLeaf
import Catalog18Lookup
import BoundaryBlocks

open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype
namespace Catalog18Identity
theorem toArray_append3 {α : Type} (xs ys zs : List α) :
    ((xs ++ ys) ++ zs).toArray = (xs.toArray ++ ys.toArray) ++ zs.toArray := by
  rw [← List.append_toArray, ← List.append_toArray]


theorem original_eq_catalog : Catalog18.original = Catalog18.catalog := by
  unfold Catalog18.original Catalog18.catalog Catalog18.block0 Catalog18.block1 Catalog18.block2
  change ((%s : List MacroPiece).toArray) =
    (((%s : List MacroPiece).toArray ++ (%s : List MacroPiece).toArray) ++ (%s : List MacroPiece).toArray)
  exact toArray_append3 %s %s %s

''' % (fmt(orig), fmt(blocks[0]), fmt(blocks[1]), fmt(blocks[2]), fmt(blocks[0]), fmt(blocks[1]), fmt(blocks[2]))
for i, ident, bridge in [(0, 'refinementPiece3', 'Catalog18.lookup0'), (57, 'refinementPiece75', 'Catalog18.boundary_57'), (114, 'refinementPiece135', 'Catalog18.boundary_114')]:
    text += f'''theorem original_lookup_{i} : Catalog18.original[{i}]? = some {ident} := by
  rw [original_eq_catalog]
  exact {bridge}

'''
text += '''#print Catalog18Identity.original_eq_catalog
#print Catalog18Identity.original_lookup_0
#print Catalog18Identity.original_lookup_57
#print Catalog18Identity.original_lookup_114
#print axioms Catalog18Identity.original_eq_catalog
#print axioms Catalog18Identity.original_lookup_0
#print axioms Catalog18Identity.original_lookup_57
#print axioms Catalog18Identity.original_lookup_114
end Catalog18Identity
'''
out = pathlib.Path('audit_exports/sharkbridge01_worktree/A1294_CATALOG18_IDENTITY_20261105/Catalog18Identity.lean')
out.write_text(text, encoding='utf-8')
print(f'wrote {out}; block sizes {[len(x) for x in blocks]}, original size {len(orig)}')

