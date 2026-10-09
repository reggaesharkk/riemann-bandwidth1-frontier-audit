"""Build a source-limited identifiability certificate for block 15's mask."""
from __future__ import annotations

import hashlib
import json
import subprocess
from pathlib import Path

from wp84_source_mask_contract_extractor import ROOT, extract_contract, sha256

OUT = ROOT / "notes/WP84_BLOCK15_SOURCE_MASK_IDENTIFIABILITY_CERTIFICATE.json"
REFERENCE_OUTPUTS = {
    "notes/WP84_BLOCK15_SOURCE_MASK_IDENTIFIABILITY_CERTIFICATE.json",
    "notes/WP84_BLOCK15_SOURCE_MASK_SEMANTIC_RECONSTRUCTION.md",
}
REFERENCE_TOKENS = ("source_mask", "iter_source_atoms", "source_amplitude_entry")


def tracked_references() -> list[dict]:
    """Index literal callback/API mentions in current tracked files only."""
    listing = subprocess.run(
        ["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True
    ).stdout.decode("utf-8").split("\0")
    hits = []
    for rel in filter(None, listing):
        if rel.startswith("notebooklm_packet/") or rel in REFERENCE_OUTPUTS:
            continue
        if Path(rel).name in {
            "wp84_source_mask_contract_extractor.py",
            "wp84_source_mask_constraint_builder.py",
            "wp84_source_mask_semantics_replay.py",
        }:
            continue
        path = ROOT / rel
        try:
            lines = path.read_text(encoding="utf-8").splitlines()
        except (UnicodeDecodeError, OSError):
            continue
        for line_no, line in enumerate(lines, 1):
            matched = [token for token in REFERENCE_TOKENS if token in line]
            if matched:
                hits.append({
                    "path": rel.replace("\\", "/"),
                    "line": line_no,
                    "tokens": matched,
                    "text": line.strip(),
                })
    return hits


def evidence(path: str, needles: list[str]) -> dict:
    p = ROOT / path
    lines = p.read_text(encoding="utf-8").splitlines()
    found = []
    for i, line in enumerate(lines, 1):
        if any(needle.casefold() in line.casefold() for needle in needles):
            found.append({"line": i, "text": line.strip()})
    return {"path": path, "sha256": sha256(p), "matches": found}


def build() -> dict:
    contract = extract_contract()
    evidence_files = [
        evidence("src/wp84_fifth_full_pool_amplitude.py", ["source_mask", "def paths", "def root_count"]),
        evidence("notes/WP84_FIFTH_LEGAL_STENCIL_AND_PRIME_REALIZATION.md", [
            "An individual prime/path atom is admissible iff", "original slot-window intersections",
            "nearest alias", "source's boundary/taper normalization", "COMPLETE carrier-amplitude",
            "these conditions are necessary and sufficient",
        ]),
        evidence("notes/WP84_FULL_WEIGHT_EVALUATION_MAP_KERNEL.md", [
            "Retain the original slot-window intersections", "F_j=Re sum", "selected section",
        ]),
        evidence("notes/WP84_FIFTH_FULL_POOL_LARGE_SECTION_LIFT.md", [
            "chi_j is the complete source mask", "original slot-window intersections",
            "actual source cells and their source-selected I(T)",
        ]),
        evidence("notes/WP84_DETERMINANT_VISIBLE_HIDDEN_PRIME_COMPRESSION.md", [
            "executable source_mask", "source-selected row identities", "source-selected endpoints",
        ]),
    ]
    conditions = [
        {"id": "D1", "condition": "frozen descriptor sign/equality partition/alias list", "status": "executable data", "source": "canonical JSON"},
        {"id": "D2", "condition": "ordinary primes p<=N and original slot-window intersections", "status": "cutoff stated; slot-window formula absent in callback implementation", "source": "legal stencil note; iterator docstring"},
        {"id": "D3", "condition": "different equality blocks injective; equal slots share one block prime", "status": "injectivity executable; equality assignment executable", "source": "iterator lines 87-95"},
        {"id": "D4", "condition": "signed valuation carrier equals requested target carrier", "status": "executable", "source": "iterator lines 90-94"},
        {"id": "D5", "condition": "alias is allowed, nearest, and 0<|lambda-mL|<=H/T", "status": "mathematical condition stated; H/window predicate not supplied to callback as data and no callback implementation", "source": "legal stencil note"},
        {"id": "D6", "condition": "closed Fourier path with |lag_j|<=6000", "status": "executable generator at R=6000; R is configurable outside callback", "source": "paths(R), iterator"},
        {"id": "D7", "condition": "root interval nonempty and every intermediate endpoint lies in section", "status": "root positivity executable after callback; callback is not passed computed root interval", "source": "root_count; iterator lines 98-102"},
        {"id": "D8", "condition": "selected source section I(T), exact endpoints, source row/cell membership and normalization", "status": "section passed in; selector/row map not executable here; normalization is downstream", "source": "legal stencil note; determinant compression note"},
        {"id": "D9", "condition": "complete carrier amplitude sums every admitted assignment/path/root/full prime pool", "status": "caller contract only; completeness not runtime-verified; core_primes can restrict", "source": "amplitude docstring and iterator signature"},
        {"id": "D10", "condition": "conjugate orientation / original mask factors", "status": "prose condition; no executable callback or per-row expected bit table", "source": "full-pool lift note"},
    ]
    # Only exact finite descriptors are enumerated.  Atom membership varies with
    # T, N(T), external section selection, primes, paths and unresolved masks.
    references = tracked_references()
    cert = {
        "decision": "E. SOURCE SEMANTICS INCOMPLETE",
        "target_block": [15, 20, 26, 28, 31, 32],
        "R": 6000,
        "local_head_checked_by_operator": subprocess.run(["git", "rev-parse", "HEAD"], cwd=ROOT, capture_output=True, text=True, check=True).stdout.strip(),
        "contract": contract,
        "tracked_source_mask_api_reference_occurrences": references,
        "tracked_source_mask_api_reference_occurrence_count": len(references),
        "documented_condition_families": conditions,
        "documented_condition_family_count": len(conditions),
        "source_constraints_that_fix_specific_membership_bits": 0,
        "explicit_expected_membership_rows": 0,
        "candidate_row_count": None,
        "candidate_row_count_reason": "No executable source-selected row/cell universe or exact source-section selector; across T the prime cutoff and endpoint selection vary. The mathematical membership predicate also references original slot-window intersections whose functions are not supplied by the callback/module.",
        "admissible_mask_count": None,
        "admissible_mask_count_reason": "The intended predicate's domain and one required factor (the original slot-window family) are unspecified, so a finite Boolean constraint system cannot be formed. This is not a claim that there are 2^n actual source masks.",
        "candidate_masks": [],
        "candidate_mask_policy": "No masks proposed: source-defined constraints are not sufficient to instantiate complete membership, and ad hoc restrictions would violate the source-only condition.",
        "known_exact_outer_iterator_inclusion_rule": "yield iff all outer generator gates pass, at least one listed alias has truthy source_mask(fid,slots,lag,T,section,m), and root_count(section,lag)>0; the mask result is only a truthiness filter, not a weight or index-set object.",
        "membership_equivalence_to_complete_source_definition": "not established; no callback implementation or exact executable original-window predicate",
        "mask_independence": "not decidable from current source semantics",
        "source_admissible_projected_rank_min": None,
        "source_admissible_projected_rank_max": None,
        "formal_linear_algebra_rank_range_only": [0, 6],
        "actual_K_B": None,
        "genuine_nonzero_source_wedge_seed": None,
        "degree_24_exceptional_endpoint_theorem_usable": False,
        "global_fifth_analytic_rank_bounds_before_after": [38, 72],
        "strict_gt_79": "OPEN",
        "source_files": evidence_files,
        "replay_policy": "independent replay re-parses source, checks hashes/signature/call-site semantics, verifies the incomplete-predicate evidence, and rejects mutations that fabricate an implementation, alter callback arity/consumption, or claim executable window/section data.",
    }
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return cert


if __name__ == "__main__":
    print(json.dumps(build(), indent=2, sort_keys=True))
