import pathlib, re
base=pathlib.Path('audit_exports/sharkbridge01_worktree/A1294_VRK_BRIDGE_20261105')
src=(base/'Catalog18Lookup.lean').read_text(encoding='utf-8')
def block(name):
    m=re.search(rf'^def {name} : Array MacroPiece := #\[(.*?)\]$',src,re.M)
    if not m: raise SystemExit(f'missing {name}')
    return [x.strip() for x in m.group(1).split(',')]
blocks=[block(f'block{i}') for i in range(3)]
assert [len(b) for b in blocks]==[57,57,57]
out=['import Catalog18Identity','open Zeta23.ThmD.Sextuple Zeta23.ThmD.Sextuple.MacroPrototype','namespace Catalog18AllLookups']
for i,ident in enumerate(sum(blocks,[])):
    b,j=divmod(i,57)
    out += [f'theorem blocked_lookup_{i} : Catalog18.catalog[{i}]? = some {ident} := by','  unfold Catalog18.catalog']
    if i == 57:
        out += ['  exact Catalog18.boundary_57']
    elif i == 114:
        out += ['  exact Catalog18.boundary_114']
    elif b==0:
        out += ['  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog18.size0, Catalog18.size1]; decide)]',
                '  rw [Array.getElem?_append_left (by rw [Catalog18.size0]; decide)]','  rfl']
    elif b==1:
        out += ['  rw [Array.getElem?_append_left (by rw [Array.size_append, Catalog18.size0, Catalog18.size1]; decide)]',
                '  rw [Array.getElem?_append_right (by rw [Catalog18.size0]; decide)]',
                '  norm_num only [Catalog18.size0, Nat.reduceSub]','  rfl']
    else:
        out += ['  rw [Array.getElem?_append_right (by rw [Array.size_append, Catalog18.size0, Catalog18.size1]; decide)]',
                '  norm_num only [Array.size_append, Catalog18.size0, Catalog18.size1, Nat.reduceAdd, Nat.reduceSub]','  rfl']
    out += [f'theorem original_lookup_{i} : Catalog18.original[{i}]? = some {ident} := by',
            '  rw [Catalog18Identity.original_eq_catalog]',
            f'  exact blocked_lookup_{i}','']
out += ['#print axioms blocked_lookup_0','#print axioms blocked_lookup_56','#print axioms blocked_lookup_57','#print axioms blocked_lookup_113','#print axioms blocked_lookup_114','#print axioms blocked_lookup_170','#print axioms original_lookup_170','end Catalog18AllLookups']
path=pathlib.Path('audit_exports/sharkbridge01_worktree/A1294_CATALOG18_IDENTITY_20261105/Catalog18AllLookups.lean')
path.write_text('\n'.join(out)+'\n',encoding='utf-8')
print(f'generated 171 blocked and original lookup theorems; source bytes {path.stat().st_size}')

