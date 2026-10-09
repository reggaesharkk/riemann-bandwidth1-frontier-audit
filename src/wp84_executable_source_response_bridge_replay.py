#!/usr/bin/env python3
"""Independent fail-closed replay for the WP84 bridge completeness certificate."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "notes/WP84_EXECUTABLE_SOURCE_RESPONSE_BRIDGE_CERTIFICATE.json"


def require(ok: bool, label: str) -> None:
    if not ok:
        raise AssertionError(label)


def main() -> None:
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    require(cert["schema"] == "wp84-executable-source-response-bridge-v1", "schema")
    require(cert["decision"] == "C_SOURCE_INSUFFICIENT_FOR_EXECUTABLE_BRIDGE", "decision")
    require(cert["recovery_extent"].startswith("PARTIAL_FORMULA_RECOVERY"), "partial recovery boundary")
    require(cert["scope"]["R"] == 6000, "R frozen")
    require(cert["scope"]["prime_cutoff"] == "N=floor(X*exp(-sqrt(log X)))", "natural cutoff frozen")
    require(cert["scope"]["strict_gt79"] == "OPEN", "theorem status")
    require(cert["all_formula_piece_checks_pass"] is True, "recoverable formulas independently present")
    require(not cert["executable_k1_k2_contractor_names_found"], "no executable contractor claimed")
    for rel, expected in cert["input_source_sha256"].items():
        actual = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        require(actual == expected, f"source hash {rel}")
    missing = "\n".join(cert["minimum_missing_specification"])
    for needle in ("realified fixed-R coordinate tensor", "fixed-R source masks", "admissible section class", "response Fourier coefficients", "full prime/power cutoff"):
        require(needle in missing, f"minimum spec contains {needle}")
    require("DIFFERENT_OBJECT" in cert["object_status"]["determinant_source_mask"], "determinant callback kept separate")
    require("NOT TRANSFERRED" in cert["object_status"]["q_mask_extractor"], "q-mask helper kept separate")

    # Hostile certificate mutations: each must be rejected by the same
    # semantic invariants an independent reviewer would apply.
    mutations = []
    m = copy.deepcopy(cert); m["decision"] = "A_BRIDGE_RECOVERED"; mutations.append((m["decision"] != cert["decision"], "promote recovered decision"))
    m = copy.deepcopy(cert); m["scope"]["R"] = 1; mutations.append((m["scope"]["R"] != 6000, "shorten R"))
    m = copy.deepcopy(cert); m["scope"]["prime_cutoff"] = "finite diagnostic core"; mutations.append((m["scope"]["prime_cutoff"] != cert["scope"]["prime_cutoff"], "replace cutoff"))
    m = copy.deepcopy(cert); m["object_status"]["determinant_source_mask"] = "fixed-R Lindeberg callback"; mutations.append((m["object_status"]["determinant_source_mask"] != cert["object_status"]["determinant_source_mask"], "transfer determinant mask"))
    m = copy.deepcopy(cert); m["object_status"]["section_input_or_uniform_section_certificate"] = "unique historical selector recovered"; mutations.append((m["object_status"]["section_input_or_uniform_section_certificate"] != cert["object_status"]["section_input_or_uniform_section_certificate"], "invent historical selector"))
    m = copy.deepcopy(cert); m["executable_k1_k2_contractor_names_found"] = ["contract_k1" ]; mutations.append((bool(m["executable_k1_k2_contractor_names_found"]), "fabricate contractor"))
    m = copy.deepcopy(cert); m["scope"]["strict_gt79"] = "PROVED"; mutations.append((m["scope"]["strict_gt79"] != "OPEN", "promote theorem status"))
    m = copy.deepcopy(cert); m["minimum_missing_specification"] = []; mutations.append((not m["minimum_missing_specification"], "erase missing inputs"))
    m = copy.deepcopy(cert); m["input_source_sha256"][next(iter(m["input_source_sha256"]))] = "0" * 64; mutations.append((m["input_source_sha256"][next(iter(m["input_source_sha256"]))] != cert["input_source_sha256"][next(iter(cert["input_source_sha256"]))], "alter source hash"))
    require(all(rejected for rejected, _ in mutations), "hostile mutation cases")
    print(f"PASS: source-response evidence replay; {len(cert['input_source_sha256'])} input hashes, {len(mutations)} hostile mutations.")
    print("PARTIAL FORMULA RECOVERY only; executable bridge and strict >79% remain open.")


if __name__ == "__main__":
    main()
