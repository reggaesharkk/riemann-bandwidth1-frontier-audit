#!/usr/bin/env python3
"""Fail-closed replay of the WP84 good-endpoint/determinant compatibility audit.

This records source-level facts and the exact failed object-identification
gate. It intentionally does not construct a selector or evaluate determinants.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PIN = "908f6c2b5b4c1dbf9d35461b5701b5a475fe96c5"
PINNED_FILES = [
    "notes/WP84_GOOD_ENDPOINT_TRIMMING.md",
    "notes/WP84_R400_PRINCIPAL_SECTION_PAIR_STABILITY.md",
    "notes/WP84_R400_FIRST_RECORD_ASSEMBLY.md",
    "src/wp84_r400_first_record_assembly.py",
]
CURRENT_FILES = [
    "src/wp84_fifth_full_pool_amplitude.py",
    "src/wp84_exact_determinant_coefficient_builder.py",
    "notes/WP84_FIFTH_FULL_POOL_LIFT_CERTIFICATE.json",
]


def git(*args: str) -> str:
    return subprocess.check_output(
        ["git", *args], cwd=ROOT, text=True, encoding="utf-8"
    ).strip()


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def main() -> None:
    assert git("rev-parse", PIN) == PIN, "pinned PR #5 commit is unavailable"
    actual_head = git("rev-parse", "HEAD")

    pinned = {}
    for path in PINNED_FILES:
        blob = git("rev-parse", f"{PIN}:{path}")
        body = git("show", f"{PIN}:{path}").encode("utf-8")
        pinned[path] = {"blob": blob, "sha256": sha256(body)}

    trim = git("show", f"{PIN}:notes/WP84_GOOD_ENDPOINT_TRIMMING.md")
    pair = git("show", f"{PIN}:notes/WP84_R400_PRINCIPAL_SECTION_PAIR_STABILITY.md")
    assembly = git("show", f"{PIN}:notes/WP84_R400_FIRST_RECORD_ASSEMBLY.md")
    assert "tau_k" in trim and "2 pi/L" in trim
    assert "epsilon_L = L^(-1/2)" in trim
    assert "source_mask" not in trim and "a_phi(T)" not in trim
    assert "(P_R)_I" in pair and "R=400" in pair
    assert "R=400" in assembly and "R=6000" not in assembly

    current = {}
    for path in CURRENT_FILES:
        raw = (ROOT / path).read_bytes()
        current[path] = sha256(raw)
    amplitude = (ROOT / CURRENT_FILES[0]).read_text(encoding="utf-8")
    coeff = (ROOT / CURRENT_FILES[1]).read_text(encoding="utf-8")
    lift = json.loads((ROOT / CURRENT_FILES[2]).read_text(encoding="utf-8"))
    assert "def iter_source_atoms" in amplitude
    assert "source_mask(fid,slots,lag,T,section,m)" in amplitude
    assert "R_SOURCE=6000" in amplitude
    assert "a_phi(T)" in amplitude
    assert lift["R"] == 6000
    assert len(lift["four_blocks"]) == 4

    result = {
        "decision": "C",
        "label": "GOOD-ENDPOINT THEOREM IS A DIFFERENT OBJECT",
        "first_incompatibility": (
            "The pinned endpoint score's generic feature coefficients are not"
            " identified with, nor shown to dominate, the current source-masked"
            " full-pool R=6000 determinant atoms and their a_phi(T)^-5 / root"
            " normalization. The current iterator requires an external exact"
            " source_mask callback; the four pinned sources do not define it."
        ),
        "pinned_source_commit": PIN,
        "local_head_audited": actual_head,
        "pinned_sources": pinned,
        "current_source_sha256": current,
        "compatible_geometry": {
            "Fourier_grid": "tau_k=T+(2pi/L)k",
            "section": "contiguous inclusive integer interval [k_-,k_+]",
            "dimension": "both allow d'/d -> 1; trimming has o(d) loss",
        },
        "failed_identity": "good-endpoint feature score <-> exact source_mask determinant atoms",
        "routes_A_B_entered": False,
        "determinant_computed": False,
        "strict_gt79": "OPEN",
        "notebooklm_packet_touched": False,
    }
    output = ROOT / "notes/WP84_GOOD_ENDPOINT_DETERMINANT_COMPATIBILITY_CERTIFICATE.json"
    output.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("GOOD-ENDPOINT / DETERMINANT SOURCE COMPATIBILITY: FAIL CLOSED")
    print("Decision: C — GOOD-ENDPOINT THEOREM IS A DIFFERENT OBJECT")
    print("First incompatibility: theorem score is not identified with source-masked determinant atoms")
    print(f"Certificate: {output.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
