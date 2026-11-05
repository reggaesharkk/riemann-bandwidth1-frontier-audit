import pathlib, re
src=pathlib.Path('audit_exports/sharkbridge01_worktree/A1294_NODE57_20261105/Terminal18.lean').read_text(encoding='utf-8-sig')
src=src.replace('import Zeta23.ThmD.Sextuple.CompositionalLeaf\n', 'import Zeta23.ThmD.Sextuple.CompositionalLeaf\nimport Catalog18AllLookups\n', 1)
pat=r'^def catalog : Array MacroPiece := #\[.*?\]$'
src,n=re.subn(pat,'def catalog : Array MacroPiece := Catalog18.original',src,count=1,flags=re.M)
if n!=1: raise SystemExit(f'catalog declaration replacements: {n}')
pat=r'^theorem catalog_ref_(\d+) : catalog\[(\d+)\]\? = some ([A-Za-z0-9_]+) := by simp \[catalog\]$'
def repl(m):
    i,j,entry=m.groups()
    if i!=j: raise SystemExit(f'index mismatch {i}/{j}')
    return (f'theorem catalog_ref_{i} : catalog[{j}]? = some {entry} := by\n'
            f'  change Catalog18.original[{j}]? = some {entry}\n'
            f'  exact Catalog18AllLookups.original_lookup_{i}')
src,n=re.subn(pat,repl,src,flags=re.M)
if n!=171: raise SystemExit(f'catalog ref replacements: {n}, expected 171')
out=pathlib.Path('audit_exports/sharkbridge01_worktree/A1294_CATALOG18_IDENTITY_20261105/Terminal18Compositional.lean')
out.write_text(src,encoding='utf-8')
print(f'wrote {out}, replaced catalog definition and {n} lookups, {out.stat().st_size} bytes')
