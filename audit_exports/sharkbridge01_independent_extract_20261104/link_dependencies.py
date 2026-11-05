"""Read-only link overlay; never link the three files this experiment compiles."""
from pathlib import Path
import sys,hashlib,json
src=Path(sys.argv[1]).resolve();dst=Path(sys.argv[2]).resolve()
skip={'CompositionalLeaf.olean','CompositionalRight.olean','A1294CompactParent.olean'}
inventory=[]
for p in src.rglob('*'):
    if not p.is_file() or p.name in skip:continue
    rel=p.relative_to(src);out=dst/rel
    out.parent.mkdir(parents=True,exist_ok=True)
    if not out.exists():out.symlink_to(p)
    if not out.is_symlink() or out.resolve()!=p.resolve():raise RuntimeError('unsafe overlay collision')
    inventory.append({'path':str(p),'relative':str(rel),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
(dst.parent.parent/'upstream_dependency_objects.json').write_text(json.dumps(inventory,indent=2))
print('Read-only linked dependency files:',len(inventory),'bytes:',sum(x['bytes'] for x in inventory))
