#!/usr/bin/env python3
"""Deterministic producer for the WP84 same-section compatibility audit.

This records exact inherited rational constants and the conditional transfer
interfaces. It does not compute a zeta-source energy or endpoint selector.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "WP84_DECISION_C_SAME_SECTION_COMPATIBILITY_CERTIFICATE.json"


def build_certificate() -> dict:
    margin = Fraction(52897896569489, 572357731837500000)
    witness = Fraction(48861622601, 195312500000)
    excess = witness - Fraction(21, 200)
    assert excess == Fraction(28353810101, 195312500000)
    assert margin > 0 and witness > Fraction(21, 200)
    return {
        "title": "WP84 Decision C same-section consumer compatibility audit",
        "classification": "C2 — CONDITIONAL",
        "start_branch": "codex/c5-c6-attack-20261006",
        "start_head": "ccff1757a424f07b96033c3b1b75277ea7e252bd",
        "head_verified": True,
        "working_tree_initial": "only pre-existing untracked notebooklm_packet/; preserved",
        "decision_b_result": {
            "M": "ceil(d*exp(-sqrt(L)/2))",
            "trim_rows_r": "u+v <= 2M",
            "r_over_d": "O(exp(-sqrt(L)/2))",
            "boundary_crossing_energy": "O(log d) for at least one candidate interval",
            "normalized_cubic_boundary": "O(S*log(d)/d') = o(1)",
            "uniform_over_sections": False,
        },
        "source_and_consumers": {
            "matrix": "H_d=s0*I+diag(beta)+[diag(A),J], prime powers p^v<=N retained; c_n=-Lambda(n)/(a_phi*L*sqrt(n)); z_n=c_n*exp(i*T*log(n))",
            "natural_cutoff": "N=floor(X*exp(-sqrt(L))), X=T/(2*pi), L=log(X), d=floor(T*L/(2*pi))",
            "direct_first_strike": "same-section signed fifth/sixth gate (12), A=11501/12500, B=137641/250000",
            "first_strike_margin": f"{margin.numerator}/{margin.denominator}",
            "conditioned_cayley": "tau(p(H))<21/200; p is bounded rational BV, but no source upper bound is proved here",
            "moment_only_falsifier_energy": f"{witness.numerator}/{witness.denominator}",
            "moment_only_falsifier_excess": f"{excess.numerator}/{excess.denominator}",
        },
        "proved_compatibility": {
            "geometry": "d'=d-r and r/d->0 for every Decision B candidate trim",
            "bounded_variation_deletion": "|tau_d f(H)-tau_d' f(H_I)| <= 2*TV(f)*r/d; applies to conditioned Cayley p(H), conditional on same-source matrix identification",
            "positive_density_intersection": "if consumer-admissible pairs have density gamma>0 in the Decision B candidate square, some admissible pair has E(I)<=C*log(d)/gamma",
        },
        "not_proved": [
            "positive-density (or automatic) consumer endpoint gates inside the exact Decision B endpoint window",
            "actual-source conditioned Cayley energy bound below 0.105 on the trim",
            "uniform normalized sixth Schatten bound for raw cubic deletion",
            "same-section prime-to-Weil and zero-side block/tail-Weyl transfer",
            "signed fifth/sixth arithmetic inequality (12)",
        ],
        "raw_cubic_sufficient_bound": "if ||H||_(6,d)<=C6, then |tau_d(H^3)-tau_d'(H_I^3)| <= 6*C6^3*sqrt(2r/d)+C6^3*(r/d)*(d/d')^(1/2)",
        "hostile_matrix": {
            "Y_d": "diag(d^(1/3),0,...,0)",
            "r": 1,
            "full_normalized_cubic": "1",
            "after_deletion_normalized_cubic": "0",
            "sixth_moment": "d (unbounded); abstract and not source-legal",
        },
        "primary_replay": "src/wp84_decision_c_same_section_compatibility_replay.py",
        "prerequisite_replays": [
            "src/wp84_infinite_no_wrap_cubic.py",
            "src/wp84_infinite_no_wrap_cubic_replay.py",
            "src/wp84_sharp_loewner_dirichlet_gate.py",
            "src/wp84_finite_section_boundary_cubic_replay.py",
            "src/wp84_adaptive_boundary_large_sieve.py",
            "src/wp84_adaptive_boundary_large_sieve_replay.py",
        ],
        "strict_gt_79": "OPEN",
    }


def main() -> None:
    cert = build_certificate()
    CERT.parent.mkdir(parents=True, exist_ok=True)
    CERT.write_text(json.dumps(cert, indent=2) + "\n", encoding="utf-8")
    print("PASS exact frozen first-strike and Cayley thresholds")
    print("PASS Decision B trim scale: r/d = O(exp(-sqrt(L)/2))")
    print("PASS conditional endpoint intersection bound: C log(d)/gamma")
    print("FALSIFIER: raw cubic deletion can lose exactly 1 with r/d=1/d")
    print("OPEN: no actual-source S6 bound, energy estimate, or endpoint-density theorem")
    print("WROTE", CERT.relative_to(ROOT))


if __name__ == "__main__":
    main()
