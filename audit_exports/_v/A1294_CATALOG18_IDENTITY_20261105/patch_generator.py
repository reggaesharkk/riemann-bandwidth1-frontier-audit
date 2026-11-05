from pathlib import Path
p=Path('audit_exports/sharkbridge01_worktree/A1294_CATALOG18_IDENTITY_20261105/generate_identity.py')
s=p.read_text(encoding='utf-8')
s=s.replace("import GenericArrayIdentity\\n", "")
s=s.replace("namespace Catalog18Identity\\n\\ntheorem original_eq_catalog", "namespace Catalog18Identity\\n\\ntheorem toArray_append3 {α : Type} (xs ys zs : List α) :\\n    ((xs ++ ys) ++ zs).toArray = (xs.toArray ++ ys.toArray) ++ zs.toArray := by\\n  rw [← List.append_toArray, ← List.append_toArray]\\n\\ntheorem original_eq_catalog")
s=s.replace("CatalogArrayIdentity.toArray_append3", "toArray_append3")
p.write_text(s, encoding='utf-8')
