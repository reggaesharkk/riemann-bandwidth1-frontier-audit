from pathlib import Path
import json, hashlib

root = Path(".").resolve()
cert = root / "certificate"
data = root / "data"

manifest = json.loads((cert / "manifest.json").read_text(encoding="utf-8"))
assert manifest["schema"] == "a1294-seam-aware-certificate-v1"
assert manifest["visited_nodes"] == 13454121

for p in [
    cert/"topology-u8.bin",
    cert/"terminal-kinds-u8.bin",
    cert/"anchors-u16le.bin",
    data/"macro-data-exact.json",
    data/"refinement-catalog-v1-exact.json",
    data/"refinement-catalog-v3.json",
]:
    assert p.exists(), p

print("PREFLIGHT PASS")
print("package_root:", root)
print("visited_nodes:", manifest["visited_nodes"])
