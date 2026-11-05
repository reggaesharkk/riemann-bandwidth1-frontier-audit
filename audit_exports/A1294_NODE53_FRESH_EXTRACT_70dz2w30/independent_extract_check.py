from __future__ import annotations

import os
import subprocess
import sys
import tempfile
import zipfile
from pathlib import Path, PurePosixPath

def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit(message)

def run_mode(root: Path, script_name: str, mode: str) -> None:
    script = root / script_name
    flags = [] if mode == "normal" else ["-" + mode]
    env = dict(os.environ)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    proc = subprocess.run(
        [sys.executable, *flags, str(script)],
        cwd=root,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )
    print(f"[{script_name} mode={mode} exit={proc.returncode}]")
    print(proc.stdout, end="")
    require(proc.returncode == 0, f"{script_name} failed under Python {mode}: {proc.returncode}")

def main() -> None:
    require(len(sys.argv) == 2, "usage: independent_extract_check.py PACKET.zip")
    archive = Path(sys.argv[1]).resolve()
    require(archive.is_file(), f"missing archive: {archive}")
    root = Path(tempfile.mkdtemp(prefix="A1294_NODE53_FRESH_EXTRACT_", dir=Path(__file__).resolve().parent.parent))
    print(f"FRESH_EXTRACTION_DIRECTORY={root}")
    with zipfile.ZipFile(archive) as zf:
        bad = zf.testzip()
        require(bad is None, f"ZIP CRC failure: {bad}")
        names = zf.namelist()
        for name in names:
            p = PurePosixPath(name)
            require(not p.is_absolute() and ".." not in p.parts, f"unsafe ZIP path: {name}")
        zf.extractall(root)
    require((root / "SHA256SUMS.txt").is_file(), "manifest missing after extraction")
    for script in ("verify_evidence_packet.py", "verify_terminal16_reconstruction.py"):
        for mode in ("normal", "O", "OO"):
            run_mode(root, script, mode)
    print(f"FRESH_EXTRACTION=PASS files={sum(1 for p in root.rglob('*') if p.is_file())}")

if __name__ == "__main__":
    main()
