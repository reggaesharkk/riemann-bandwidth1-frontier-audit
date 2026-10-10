"""Deterministically produce the Decision O exponent/structure certificate.

This records the source-matched scale audit.  It does not claim a bound for the
unresolved signed off-diagonal prime-power correlation.
"""
from __future__ import annotations

import json
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificates" / "WP84_DECISION_O_CRITICAL_SIGNED_DISPERSION_CERTIFICATE.json"


def main() -> None:
    eps = Fraction(1, 100)
    eps_cauchy = Fraction(1, 10)
    baseline = Fraction(1, 10) + Fraction(8, 5) * eps
    fourier_cost = Fraction(7, 5)
    fourier_gap = fourier_cost - baseline
    cauchy_cost = Fraction(3, 10)
    power_two_subfamily = -Fraction(1, 2) + Fraction(8, 5) * eps_cauchy

    cert = {
        "title": "WP84 Decision O: critical signed dispersion feasibility",
        "classification": "O4",
        "starting_state": {
            "branch": "codex/c5-c6-attack-20261006",
            "head": "3fab3a406dcb710cbc7a085626246571c82ed570",
            "preexisting_untracked_preserved": ["notebooklm_packet/"],
        },
        "source_scales": {
            "X": "T/(2*pi)",
            "L": "log(X)",
            "N": "floor(X*exp(-sqrt(L)))",
            "d": "floor(X*L)",
            "M": "ceil(d*exp(-sqrt(L)/2))",
            "H": "exp(sqrt(L)/2)",
            "coefficient": "c_n=-Lambda(n)/(a_phi(T)*L*sqrt(n)); all prime powers n<=N retained",
            "representative_block": "B~X^(3/5), n1,n2~X^(4/5), |n1*n2-X*B|<=4*B*H",
            "kernel": "exact finite-J path/root sum, endpoint choices and centering retained",
        },
        "thin_strip": {
            "n2_interval_length_upper": "16*X^(-1/5)*exp(sqrt(L)/2)",
            "log_length": "log(16)-L/5+sqrt(L)/2 -> -infinity",
            "conclusion": "for sufficiently large X, at most one integer n2 for fixed B,n1",
            "does_not_imply": ["prime-power occupancy", "cancellation", "signed saving"],
        },
        "existing_absolute_baseline": {
            "formula": "O_epsilon(X^(1/10+8*epsilon/5))",
            "epsilon": "1/100",
            "exponent": f"{baseline.numerator}/{baseline.denominator}",
            "decimal": float(baseline),
            "target": "o(1), hence a negative exponent is required",
        },
        "exact_fourier_completion": {
            "period": "power of two Q with 5*X^(8/5)<Q<=10*X^(8/5)",
            "interval_coefficients": "Q^-1 sum_{a in I_B} exp(-2*pi*i*r*a/Q)",
            "completion": "exp(2*pi*i*A/B)*exp(2*pi*i*r*A/Q)=exp(2*pi*i*(Q+rB)*A/(BQ))",
            "odd_prime_power_B": "gcd(B,Q)=1",
            "matrix_norm": "sqrt(B*Q*gcd(r,Q))",
            "weighted_fourier_l1": "O(log(Q)+m_B/sqrt(Q))=O(L)",
            "normalized_bound": "O(L*X^(7/5)*exp(-sqrt(L)/2))",
            "power_gap_over_baseline": f"{fourier_gap.numerator}/{fourier_gap.denominator}-o(1)",
            "status": "exact completion; bound is much worse than baseline",
        },
        "cauchy_dispersion": {
            "exact_cross_phase": "exp(2*pi*i*(h/B-h_prime/B_prime)); h=n1*nu_B(n1)-X*B",
            "unresolved_piece": "signed B!=B' prime-power correlation, including shared-prime/proper-power gcd strata",
            "absolute_bound": "O(X^(3/10)*exp(-sqrt(L)/2))",
            "power_exponent_before_subpower": f"{cauchy_cost.numerator}/{cauchy_cost.denominator}",
            "requires_source_theorem": True,
        },
        "isolated_subfamily": {
            "singleton_modulus": "B=2^v",
            "per_dyadic_block_count": "at most 2",
            "epsilon": "1/10",
            "normalized_exponent": f"{power_two_subfamily.numerator}/{power_two_subfamily.denominator}",
            "conclusion": "this subfamily alone is o(1); full odd-modulus block remains open",
        },
        "decision": {
            "result": "O4: tested Fourier completion and one Cauchy dispersion estimate do not meet the required exponent",
            "signed_saving_earned": False,
            "counterexample_to_target": False,
            "strict_gt_79": "OPEN",
            "smallest_unresolved_estimate": "a source-matched signed bound for the displayed off-diagonal B!=B' correlation strong enough to make the full normalized block o(1)",
        },
        "finite_checks_are_diagnostics_only": True,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(OUT)
    print(f"baseline exponent={baseline}; Fourier gap={fourier_gap}; Cauchy exponent={cauchy_cost}; B=2^v exponent={power_two_subfamily}")


if __name__ == "__main__":
    main()
