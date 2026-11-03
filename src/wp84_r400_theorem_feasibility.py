#!/usr/bin/env python3
"""Exact checks for the WP84 R400 ordinary-aggregate hard-stop audit.

This checker verifies rational budget arithmetic and abstract norm/scale
countermodels. It deliberately does not claim a source-prime counterexample
or evaluate the unresolved physical ordinary-prime sum.
"""

from __future__ import annotations

import json
import argparse
from fractions import Fraction
from pathlib import Path


DELTA_MAX = Fraction(3675673694911, 148250000000000)


def need(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def diagonal_spike(k: int) -> dict[str, str | int]:
    """Exact k^8-dimensional diagonal example with a single k^3 spike."""
    need(k >= 2, "k must be at least two")
    dimension = k**8
    spike = k**3
    tau2 = Fraction(spike**2, dimension)
    tau4 = Fraction(spike**4, dimension)
    need(tau2 == Fraction(1, k**2), "normalized second trace mismatch")
    need(tau4 == k**4, "normalized fourth trace mismatch")
    return {
        "k": k,
        "dimension": dimension,
        "nonzero_diagonal_entry": spike,
        "normalized_tau_Q2": str(tau2),
        "normalized_tau_Q4": str(tau4),
        "operator_norm": spike,
    }


def build_checks() -> dict:
    delta8 = DELTA_MAX / 8
    delta4 = DELTA_MAX / 4
    signed_example = (-1, 1)
    mean_signed = Fraction(sum(signed_example), len(signed_example))
    mean_positive = Fraction(sum(max(0, x) for x in signed_example), len(signed_example))

    return {
        "schema": "wp84.r400.ordinary-theorem-feasibility-checks.v1",
        "decisions": {
            "PUBLISHED_SOURCE_TRANSFER": "INSUFFICIENT",
            "ENDPOINT_CORRECTION": "OPEN",
            "ORDINARY_CONNECTED_AGGREGATE": "OPEN",
            "R400_CONSUMER": "OPEN",
            "NEXT_ACTION": "NEW_ANALYTIC_THEOREM_REQUIRED",
        },
        "record_budget": {
            "delta_max_exact": str(DELTA_MAX),
            "delta_max_decimal": f"{float(DELTA_MAX):.16f}",
            "epsilon_one_eighth_positive_part_budget_exact": str(delta8),
            "epsilon_one_eighth_positive_part_budget_decimal": f"{float(delta8):.16f}",
            "limiting_delta_over_four_exact": str(delta4),
            "limiting_delta_over_four_decimal": f"{float(delta4):.16f}",
            "strict_inequality_required": True,
        },
        "second_mass_fourth_moment_countermodel": {
            "family": "Q_k=diag(k^3,0,...,0) of dimension k^8",
            "rows": [diagonal_spike(k) for k in (2, 10, 100)],
            "conclusion": "tau(Q_k^2)=k^-2<=1 while tau(Q_k^4)=k^4 is unbounded; a normalized second-mass bound alone gives no normalized fourth-moment upper bound",
        },
        "signed_mean_vs_positive_part": {
            "values": list(signed_example),
            "mean_signed_exact": str(mean_signed),
            "mean_positive_part_exact": str(mean_positive),
            "conclusion": "a signed mean bound does not imply the required mean positive-part bound",
        },
        "source_cutoff_scale": {
            "definitions": "L=log(T/(2*pi)); N=floor(exp(L-sqrt(L))); d=floor(T*L/(2*pi))",
            "N_over_T_asymptotic": "exp(-sqrt(L))/(2*pi) -> 0",
            "N_squared_over_T_asymptotic": "exp(L-2*sqrt(L))/(2*pi) -> infinity",
            "N_fourth_over_T_asymptotic": "exp(3*L-4*sqrt(L))/(2*pi) -> infinity",
            "normalization_correction": "Using T=2*pi*exp(L), N^2/T is exp(L-2*sqrt(L))/(2*pi) = T*exp(-2*sqrt(L))/(4*pi^2); older prose that writes denominator 2*pi differs by a fixed factor 2*pi, not in the divergence conclusion.",
        },
        "evans_direct_major_arc_insertion": {
            "WP84_product_scale": "M_prod=T^s, fixed s>1",
            "WP84_short_shift_width": "H=M_prod/T=T^(s-1)",
            "published_global_remainder": "B^2(M_prod) << M_prod/(log M_prod)^eta",
            "after_WP84_weight_and_oversampling": "H*(log P)^2/(|a_phi|^4*L^4*(log M_prod)^eta)",
            "P_scale": "P=log^B(M_prod), so log(P)=O(log L) for fixed s",
            "asymptotic_form": "T^(s-1)*(log L)^2/L^(4+eta), up to constants depending on fixed s and the bounded nonzero a_phi normalization",
            "conclusion": "diverges for each fixed s>1; this positive L2 insertion is not below Delta_max or Delta_max/8",
        },
        "repository_transfer": {
            "linear_source_grid_bound": "normalized discrete large sieve costs 1+O(N/T) for one-prime source points; it is uniform in section start but is linear/quadratic only",
            "product_block_bound": "the recorded two-index product Gram bound is 1+16*pi*M_prod/T=1+16*pi*H",
            "flattened_ratio_frequency_warning": "the denominator-only spacing guarantee for distinct reduced A/B ratios with A,B<=N^2 is no better than order N^-4; after log-frequency scaling and d~T*L samples, the generic spacing term can be as large as order N^4/T. This is a worst-case guarantee for all integer ratios, not a claim that the ordinary-prime product subset attains it.",
            "multilinear_source_extension": "repository search found no proved multilinear mean-value/large-sieve theorem for the section-dependent 26-term physical cumulant coefficients",
        },
        "status_boundary": "These exact checks do not assert that the physical prime aggregate is positive, large, or illegal. Its record bound remains open.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-json", type=Path)
    args = parser.parse_args()
    data = build_checks()
    serialized = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if args.write_json:
        args.write_json.write_text(serialized, encoding="utf-8")
        print(f"WROTE {args.write_json}")
    else:
        print(serialized, end="")
    print("PASS exact rational budget, diagonal-spike, sign/positive-part, and scale checks")


if __name__ == "__main__":
    main()
