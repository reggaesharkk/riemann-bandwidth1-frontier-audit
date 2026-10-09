#!/usr/bin/env python3
"""Inspect whether WP84's fixed-R source-to-response bridge is executable.

This is a fail-closed source inspector, not a constructor for missing WP84
mathematical data.  It deliberately refuses to substitute the determinant
source_mask callback for the fixed-R Lindeberg masks.
"""
from __future__ import annotations

import ast
import hashlib
import json
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_START = "a0dc9a4d604e13f21df57468523d74b489c1b7d1"
EXPECTED_BRANCH = "codex/c5-c6-attack-20261006"
SOURCES = [
    "notes/WP84_LOCALIZE_FIRST_HERMITE_PROJECTION.md",
    "notes/WP84_PRIME_BASE_GROUPED_LINDEBERG.md",
    "notes/WP84_DEPENDENT_PHASE_PRIME_ADIC_FIREWALL.md",
    "notes/WP84_SOURCE_CONTRACTED_DUAL_MASS_AUDIT.md",
    "notes/WP84_SOURCE_CONTRACTED_DUAL_MASS_AUDIT_CERTIFICATE.json",
    "src/wp84_contour_mixture_prime_mass.py",
    "src/wp84_fifth_full_pool_amplitude.py",
    "src/wp84_source_q_mask_extractor.py",
    "src/wp84_compiled_mehler_prime_lindeberg.py",
]


def read(rel: str) -> str:
    return (ROOT / rel).read_text(encoding="utf-8")


def sha256(rel: str) -> str:
    return hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()


def git(*args: str) -> str:
    return subprocess.check_output(["git", *args], cwd=ROOT, text=True).strip()


def defined_python_names() -> set[str]:
    names: set[str] = set()
    for path in (ROOT / "src").glob("*.py"):
        try:
            tree = ast.parse(path.read_text(encoding="utf-8"))
        except (SyntaxError, UnicodeDecodeError):
            continue
        for node in ast.walk(tree):
            if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef, ast.ClassDef)):
                names.add(node.name)
    return names


def inspect() -> dict:
    localize = read("notes/WP84_LOCALIZE_FIRST_HERMITE_PROJECTION.md")
    firewall = read("notes/WP84_DEPENDENT_PHASE_PRIME_ADIC_FIREWALL.md")
    dual = read("notes/WP84_SOURCE_CONTRACTED_DUAL_MASS_AUDIT.md")
    mixture = read("src/wp84_contour_mixture_prime_mass.py")
    determinant = read("src/wp84_fifth_full_pool_amplitude.py")
    qmask = read("src/wp84_source_q_mask_extractor.py")
    names = defined_python_names()

    # Verify the recoverable formula pieces from source text, but do not call
    # their presence a source tensor implementation.
    formula_checks = {
        "ordinary_prime_vector_formula_in_prose": all(x in localize for x in (
            "V_p(K)", "c_p=-\\frac{\\log p}{a_\\phi L\\sqrt p}", "s_p=\\frac{\\log p}{L}")),
        "trace_grid_kernel_formula_in_prose": "mathcal K_I(\\omega)" in firewall and "d'" in firewall,
        "prime_adic_alias_equation_in_prose": "p^r\\prod_{q\\ne p}q^{\\nu_q}=X^m" in firewall,
        "A1_A2_formulas_in_prose": "A_{1,T,R}" in localize and "A_{2,T,R}" in localize,
        "dual_mass_definitions_only_as_json_strings": '"exact_grouped_kernel_definition"' in mixture,
        "determinant_iterator_takes_external_source_mask": "source_mask" in determinant and "def source_mask(" not in determinant,
        "q_mask_helper_is_separate_reconstruction": "q_mask" in qmask,
        "prior_audit_records_missing_constructor": "no routine constructs the contracted tensors" in dual,
    }
    # A merely named symbol in a certificate string does not count.  Require
    # an executable definition and fail closed if no such implementation is
    # found anywhere in src/.
    executable_contractors = sorted(n for n in names if re.search(r"(contract|build|compute).*(k1|k2)|(k1|k2).*(contract|build|compute)", n, re.I))
    hashes = {rel: sha256(rel) for rel in SOURCES}
    status = {
        "exact_prime_power_coordinate_tensor": "MISSING_EXECUTABLE_SOURCE",
        "fixed_R_masks_and_row_gates": "MISSING_EXECUTABLE_SOURCE",
        "section_input_or_uniform_section_certificate": "MISSING_FOR_REPLAY; existential section need not be historically unique",
        "response_fourier_arrays_or_direct_contraction": "MISSING_EXECUTABLE_SOURCE",
        "K1_K2_D1_D2": "SYMBOLIC_ONLY_NOT_INSTANTIATED",
        "ordinary_prime_formula_and_alias_skeleton": "PARTIALLY_RECOVERED_IN_PROSE",
        "determinant_source_mask": "EXTERNAL_CALLBACK_FOR_DIFFERENT_OBJECT; NOT TRANSFERRED",
        "q_mask_extractor": "SEPARATE_RECONSTRUCTED_DETERMINANT_HELPER; NOT TRANSFERRED",
    }
    return {
        "schema": "wp84-executable-source-response-bridge-v1",
        "expected_starting_head": EXPECTED_START,
        "observed_branch": git("branch", "--show-current"),
        "observed_head_at_inspection": git("rev-parse", "HEAD"),
        "working_tree_short_at_inspection": git("status", "--short"),
        "starting_state_matches_task": git("rev-parse", "HEAD") == EXPECTED_START and git("branch", "--show-current") == EXPECTED_BRANCH,
        "decision": "C_SOURCE_INSUFFICIENT_FOR_EXECUTABLE_BRIDGE",
        "recovery_extent": "PARTIAL_FORMULA_RECOVERY; no executable fixed-R source-to-response constructor recovered",
        "scope": {"R": 6000, "prime_cutoff": "N=floor(X*exp(-sqrt(log X)))", "quantifiers": "fixed R then T->infinity", "strict_gt79": "OPEN"},
        "formula_piece_checks": formula_checks,
        "all_formula_piece_checks_pass": all(formula_checks.values()),
        "executable_k1_k2_contractor_names_found": executable_contractors,
        "input_source_sha256": hashes,
        "object_status": status,
        "minimum_missing_specification": [
            "For every prime base p and p^a<=N, an exact realified fixed-R coordinate tensor with normalization and a single explicit carrier-placement convention.",
            "The fixed-R source masks/window gates and their row dependence, including all lag, root/path and alias factors; do not substitute determinant source_mask or q_mask.",
            "Either (i) the actual allowable trace index set I(T), its endpoints/order and d' plus root-count data for a replayable instance, or (ii) a proof uniform over a mathematically specified admissible section class that avoids selecting one historical section.",
            "An executable construction of the p-excluded first/second response Fourier coefficients, or a direct exact contraction that computes the same K1/K2 without materializing them.",
            "A source-backed test fixture with full prime/power cutoff and R=6000 against which an independent replay can compare the instantiated A1/A2 and D1/D2 objects."
        ],
        "still_open_analytic_statement": "For the actual fixed-R source and each admissible section, prove A1_T,R + A2_T,R -> 0 (or a justified sufficient pair D1_T=o(1), D2_T=o(L^4)), retaining all periodic and near aliases and the natural cutoff.",
        "no_claims": ["No A1/A2 estimate is newly proved.", "No source-legal counterexample is produced.", "No synthetic rows, finite prime core, or determinant-mask substitution is used.", "Strict >79% is not proved."]
    }


def main() -> None:
    cert = inspect()
    out = ROOT / "notes/WP84_EXECUTABLE_SOURCE_RESPONSE_BRIDGE_CERTIFICATE.json"
    out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("DECISION:", cert["decision"])
    print("formula pieces recovered:", sum(cert["formula_piece_checks"].values()), "/", len(cert["formula_piece_checks"]))
    print("executable K1/K2 contractors:", cert["executable_k1_k2_contractor_names_found"] or "none")
    print("strict >79%:", cert["scope"]["strict_gt79"])


if __name__ == "__main__":
    main()
