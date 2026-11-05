from __future__ import annotations

import json
from pathlib import Path
from typing import Callable

DomainAdapter = Callable[[dict, Path], tuple[bool, str]]


def _ev_by_role(claim: dict, role: str) -> list[dict]:
    return [ev for ev in claim.get("evidence", []) if ev.get("role") == role]


def verify_lrsc_claim(claim: dict, root: Path) -> tuple[bool, str]:
    d = claim.get("domain", {})
    if d.get("system") != "LRSC" or d.get("kind") != "finite_benchmark":
        return False, "LRSC domain kind/system mismatch"
    p = d.get("parameters", {})
    pred = d.get("predicate", {})
    expected = {"M": 99, "k_idx": 49, "A": "1/2", "theta": "0.07", "relative_L2_tolerance": "1e-3"}
    if p != expected:
        return False, f"LRSC parameters differ from demonstrator definition: {p}"
    if pred != {"metric": "minimum_passing_channel_subset_cardinality", "operator": "=", "value": 14}:
        return False, f"LRSC predicate mismatch: {pred}"
    expected_text = (
        "For the specified LRSC M=99, k_idx=49, A=1/2, theta=0.07 finite benchmark, "
        "the minimum passing channel-subset cardinality at relative residual tolerance 1e-3 is K_0.001=14."
    )
    if claim.get("claim_text") != expected_text:
        return False, "human-readable claim text does not equal canonical LRSC statement"
    expected_dependency = [{
        "claim_id": "lrsc.m99.theta007.mask83",
        "relation": "assumes_mask_cell",
        "claim_digest": "257ca3fed058db097058328a8dadd9698101f5f4e331a32ea72ee4d334b123da",
    }]
    if claim.get("dependencies") != expected_dependency:
        return False, "LRSC dependency version differs from frozen mask83 dependency"

    definitions = _ev_by_role(claim, "definition")
    if len(definitions) != 1 or not definitions[0].get("path"):
        return False, "exactly one local definition required"
    witnesses = _ev_by_role(claim, "passing_witness")
    if len(witnesses) != 1 or not witnesses[0].get("path"):
        return False, "exactly one local passing witness required"
    w = json.loads((root / witnesses[0]["path"]).read_text(encoding="utf-8"))
    if int(w.get("M", -1)) != 99 or str(w.get("theta")) != "0.07" or str(w.get("relative_tolerance")) != "1e-3":
        return False, "witness parameters mismatch"
    if len(w.get("subset", [])) != 14:
        return False, "witness cardinality is not 14"

    exclusions = _ev_by_role(claim, "exclusion_certificate")
    coverage = _ev_by_role(claim, "coverage_certificate")
    independent = _ev_by_role(claim, "independent_verification")
    if len(exclusions) != 1 or exclusions[0].get("plugin") != "lrsc_execute_full_replay":
        return False, "v0.3 requires one full-replay exclusion certificate"
    if len(coverage) != 1 or coverage[0].get("plugin") != "lrsc_execute_full_replay":
        return False, "v0.3 requires one full-replay coverage certificate"
    if len(independent) != 1 or independent[0].get("plugin") != "lrsc_execute_independent_recheck":
        return False, "v0.3 requires one independent post-run recheck"
    return True, "LRSC canonical statement + local definition + full K0..K13 replay + K14 witness agree"


def verify_n11_k36_claim(claim: dict, root: Path) -> tuple[bool, str]:
    d = claim.get("domain", {})
    if d.get("system") != "NS_GALERKIN" or d.get("kind") != "finite_validated_trajectory":
        return False, "finite N11 domain kind/system mismatch"
    p = d.get("parameters", {})
    expected = {
        "N": 11,
        "nu": "0.1",
        "T": "0.003",
        "observable": "K36_F_equals_I_minus_9O",
        "certificate_sha256": "d29224e1dd4ad9f9454951415a3b080bc9f092839e24caaeddd056013785cfbe",
    }
    if p != expected:
        return False, f"finite N11 parameters differ from frozen certificate: {p}"
    pred = d.get("predicate", {})
    if pred != {"metric": "exists_K36_90pct_crossing", "operator": "=", "value": True}:
        return False, f"finite N11 predicate mismatch: {pred}"
    expected_text = (
        "For the fixed post-hoc finite N11 Fourier-Galerkin trajectory at nu=0.1, "
        "the frozen K36 absolute-mass fraction has at least one 90% threshold crossing in t in (0,0.003)."
    )
    if claim.get("claim_text") != expected_text:
        return False, "human-readable finite N11 claim text does not equal canonical statement"
    scope = claim.get("scope", {})
    excluded = set(scope.get("does_not_imply", []))
    required_exclusions = {
        "continuum Navier-Stokes regularity",
        "finite-time blowup",
        "all-cutoff persistence",
        "Millennium-problem solution",
    }
    if not required_exclusions.issubset(excluded):
        return False, "finite N11 continuum firewall incomplete"
    by_role = {role: _ev_by_role(claim, role) for role in ("definition", "interval_certificate", "verifier")}
    if any(len(v) != 1 for v in by_role.values()):
        return False, "finite N11 requires exactly one definition, interval_certificate and verifier binding"
    expected_repo = "reggaesharkk/navier-stokes-bridge-audit"
    expected_commit = "d43135047dae40a42da715f1082d87ccf1b70691"
    expected_paths = {
        "definition": "notes/WP16_036_N11_VALIDATED_TURNOVER_2026_09_28.md",
        "interval_certificate": "results/wp16_n17_holdout/wp16_036_n11_turnover_certificate_identity.json",
        "verifier": "notes/WP16_036_TURNOVER_CERTIFICATE_VERIFIER_SPEC_2026_09_28.md",
    }
    for role, records in by_role.items():
        ext = records[0].get("external", {})
        if ext.get("repository") != expected_repo or ext.get("commit") != expected_commit or ext.get("path") != expected_paths[role]:
            return False, f"finite N11 {role} external binding mismatch"
    return True, "finite N11 canonical statement and immutable certificate/verifier bindings agree"


DOMAIN_ADAPTERS: dict[str, DomainAdapter] = {"LRSC": verify_lrsc_claim, "NS_GALERKIN": verify_n11_k36_claim}
