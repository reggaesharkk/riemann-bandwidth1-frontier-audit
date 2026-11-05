from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parent
V4 = ROOT.parent / "A1294_NODE53_TERMINAL16_20261105"
source = (V4 / "verify_terminal16_reconstruction.py").read_text(encoding="utf-8-sig")

old_paths = """ROOT = Path(__file__).resolve().parent
V2ROOT = ROOT / 'reference_packet' / 'reference' / 'v2_source' / 'A1294_SOURCE_FREE_REPLAY_PACKAGE_V2'
V2ZIP = ROOT / 'reference_packet' / 'reference' / 'predecessor' / 'A1294_CATALOG18_IDENTITY_20261105' / 'reference' / 'input' / 'A1294_SOURCE_FREE_REPLAY_PACKAGE_V2.zip'
INPUT = ROOT / 'terminal16_authentic_input.json'
"""
new_paths = """if len(sys.argv) != 4:
    raise SystemExit('usage: verify15_reconstruction.py <V2-package-root> <V2-package.zip> <terminal15-input.json>')
V2ROOT = Path(sys.argv[1]).resolve()
V2ZIP = Path(sys.argv[2]).resolve()
INPUT = Path(sys.argv[3]).resolve()
"""
if old_paths not in source:
    raise SystemExit("could not find exact terminal-16 verifier path block")
source = source.replace(old_paths, new_paths)

replacements = [
    ("top[53:68]", "top[51:68]"),
    ("[4,0,1,0,5,0,3,0,2,0,4,0,1,0,0]", "[2,0,4,0,1,0,5,0,3,0,2,0,4,0,1,0,0]"),
    ("nodes[53][2]==4 and nodes[54][2]==0 and nodes[54][3]==16", "nodes[51][2]==2 and nodes[52][2]==0 and nodes[52][3]==15 and nodes[53][2]==4"),
    ("nodes[54][1]==nodes[53][1]+[(3,'L')]", "nodes[52][1]==nodes[51][1]+[(1,'L')]"),
    ("nodes[55][1]==nodes[53][1]+[(3,'R')]", "nodes[53][1]==nodes[51][1]+[(1,'R')]"),
    ("kinds[16]==1 and list(kinds[16:24])==[1]*8", "kinds[15]==1 and list(kinds[15:24])==[1]*9"),
    ("kinds[:16]", "kinds[:15]"),
    ("anchor_offset==160", "anchor_offset==150"),
    ("nodes[54][0]", "nodes[52][0]"),
    ("nodes[53][0]", "nodes[51][0]"),
    ("node53_axis=3 node54_terminal=16 kind=quadratic node55=right_child", "node51_axis=1 node52_terminal=15 kind=quadratic node53=right_child"),
    ("terminal-16", "terminal-15"),
    ("terminal 16", "terminal 15"),
    ("node 53", "node 51"),
    ("node 54", "node 52"),
    ("topology53_67", "topology51_67"),
    ("node53_box", "node51_box"),
    ("node54_box", "node52_box"),
    ("len(unique)==166 and (macro,v1,v3)==(22,144,0)", "len(unique)==167 and (macro,v1,v3)==(23,144,0)"),
]
for old, new in replacements:
    if old not in source:
        raise SystemExit(f"missing expected source fragment: {old}")
    source = source.replace(old, new)

(ROOT / "verify15_reconstruction.py").write_text(source, encoding="utf-8")
print("generated verify15_reconstruction.py from the preserved terminal-16 independent verifier")
