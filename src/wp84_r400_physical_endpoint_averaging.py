#!/usr/bin/env python3
"""Exact endpoint-kernel weights and source-correction ledger for WP84 R400.

All finite combinatorial checks use Fraction arithmetic. The module does not
assert a source-weighted ordinary-prime aggregate estimate.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path

DELTA = F(3675673694911, 148250000000000)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def balanced_words() -> list[str]:
    return ["".join(w) for w in product(("+", "-"), repeat=4) if w.count("+") == 2]


def set_partitions(items: tuple[int, ...]):
    if not items:
        yield ()
        return
    head, tail = items[0], items[1:]
    for part in set_partitions(tail):
        for j in range(len(part)):
            yield part[:j] + ((head,) + part[j],) + part[j + 1 :]
        yield ((head,),) + part


def anchored_ordered_partitions():
    rows = []
    for part in set_partitions((0, 1, 2, 3)):
        anchor = next(j for j, block in enumerate(part) if 0 in block)
        others = tuple(j for j in range(len(part)) if j != anchor)
        for order in permutations(others):
            blocks = tuple(part[j] for j in (anchor,) + order)
            rows.append(((-1) ** (len(blocks) - 1), blocks))
    counts = {j: sum(len(blocks) == j for _, blocks in rows) for j in range(1, 5)}
    require(len(rows) == 26 and counts == {1: 1, 2: 7, 3: 12, 4: 6}, "26-partition ledger")
    return rows, counts


def endpoint_pairs(d: int, M: int, b: int = 0) -> list[tuple[int, int, int]]:
    require(d > 0 and M >= 0 and 2 * M < d, "positive source-admissible sections required")
    return [(u, v, d - u - v) for u in range(M + 1) for v in range(M + 1)]


def endpoint_kernel_weights(
    d: int, M: int, b: int = 0, selected: set[tuple[int, int]] | None = None
) -> dict[int, F]:
    """Weights in E_I[(1/|I|)sum_{k in I} e(k theta)]."""
    pairs = endpoint_pairs(d, M, b)
    if selected is not None:
        pairs = [row for row in pairs if (row[0], row[1]) in selected]
        require(bool(pairs), "selected section family must be nonempty")
    rho = F(1, len(pairs))
    weights: dict[int, F] = {k: F(0) for k in range(b, b + d)}
    for u, v, m in pairs:
        for k in range(b + u, b + d - v):
            weights[k] += rho / m
    require(all(w >= 0 for w in weights.values()), "endpoint weights are nonnegative")
    require(sum(weights.values(), F(0)) == 1, "endpoint weights have total mass one")
    return weights


def endpoint_kernel_weights_measure(
    d: int, M: int, rho: dict[tuple[int, int], F], b: int = 0
) -> dict[int, F]:
    """Exact endpoint weights for any probability measure on candidate pairs."""
    pairs = {(u, v): m for u, v, m in endpoint_pairs(d, M, b)}
    require(bool(rho), "endpoint measure must be nonempty")
    require(all(pair in pairs for pair in rho), "measure contains a noncandidate section")
    require(all(weight >= 0 for weight in rho.values()), "endpoint measure must be nonnegative")
    require(sum(rho.values(), F(0)) == 1, "endpoint measure must have mass one")
    weights = {k: F(0) for k in range(b, b + d)}
    for (u, v), mass in rho.items():
        m = pairs[(u, v)]
        for k in range(b + u, b + d - v):
            weights[k] += mass / m
    require(all(weight >= 0 for weight in weights.values()), "endpoint weights are nonnegative")
    require(sum(weights.values(), F(0)) == 1, "endpoint weights have total mass one")
    return weights


def gaussian_unit_quarter(k: int) -> tuple[int, int]:
    return ((1, 0), (0, 1), (-1, 0), (0, -1))[k % 4]


def gaussian_weighted_sum(weights: dict[int, F], phase_shift: int = 0) -> tuple[F, F]:
    real = F(0)
    imag = F(0)
    for k, weight in weights.items():
        a, b = gaussian_unit_quarter(k + phase_shift)
        real += weight * a
        imag += weight * b
    return real, imag


def d_half(m: int, x: F) -> F:
    """Exact D_m(x) for integer or half-integer x (all values are real)."""
    if x.denominator == 1:
        return F(1)
    require((2 * x).denominator == 1, "half-grid input expected")
    return F(0) if m % 2 == 0 else F(1, m)


def kappa_half(m: int, vector: tuple[F, F, F, F]) -> F:
    total = F(0)
    for coefficient, blocks in anchored_ordered_partitions()[0]:
        term = F(coefficient)
        for block in blocks:
            block_sum = sum((vector[j] for j in block), F(0))
            term *= d_half(m, block_sum)
        total += term
    return total


def kappa_length_correction_bound(d: int, m: int) -> F:
    """|kappa_m(v)-kappa_d(v)| <= 150*(d-m)/d when |D_j|<=1."""
    require(0 < m <= d, "section length must not exceed the base length")
    return F(150 * (d - m), d)


def path_boundary_count(m: int, lags: tuple[int, int, int, int]) -> dict:
    require(sum(lags) == 0, "closed lag path required")
    q = [0]
    for lag in lags:
        q.append(q[-1] + lag)
    span = max(q) - min(q)
    require(span < m, "test section must contain at least one valid path root")
    return {
        "prefix_vertices": q,
        "span": span,
        "roots_in_full_section": m,
        "roots_surviving_principal_compression": m - span,
        "fractional_path_correction_at_Y_zero": F(-span, m),
        "absolute_correction_bound": F(span, m),
    }


def joint_selection_ledger(epsilon: F) -> dict:
    require(F(0) < epsilon < F(1, 4), "epsilon must leave a positive common density")
    common_density = F(1, 4) - epsilon
    mean_budget = common_density * DELTA
    require(mean_budget > 0, "positive connected budget")
    return {
        "endpoint_good_pair_density": "at least 1/4 from two separately half-dense endpoint sets",
        "boundary_bad_fraction": str(epsilon),
        "boundary_good_threshold": f"E(I) <= C_B*log(d)/({epsilon})",
        "endpoint_and_boundary_good_density": str(common_density),
        "connected_positive_excess": "G_T(I)=max(0, Re C_T(I))",
        "sufficient_global_mean": f"mean_(u,v) in W_T G_T(I_uv) < {mean_budget}",
        "exact_mean_budget": str(mean_budget),
        "proof": "boundary Markov removes at most epsilon; connected Markov removes less than (1/4-epsilon); the endpoint-good set has density at least 1/4, so a common section remains",
    }


def exact_ledgers() -> dict:
    d, M, b = 6, 2, 0
    weights = endpoint_kernel_weights(d, M, b)
    selected = {(0, 0), (0, 1), (1, 0), (1, 1)}
    selected_weights = endpoint_kernel_weights(d, M, b, selected)
    vector = (F(1, 2), F(-1, 2), F(1, 2), F(-1, 2))
    kappa_rows = {str(m): str(kappa_half(m, vector)) for m in range(2, d + 1)}
    average_kappa = sum(
        (kappa_half(m, vector) for _, _, m in endpoint_pairs(d, M)), F(0)
    ) / (M + 1) ** 2
    positive_part_example = {
        "section_values": ["1", "-1"],
        "average_signed": "0",
        "average_positive_part": "1/2",
        "positive_part_of_average": "0",
    }
    require(average_kappa != kappa_half(d, vector), "row-cumulant averaging correction must be nonzero")
    require(positive_part_example["average_positive_part"] != positive_part_example["positive_part_of_average"], "positive part does not commute")
    rows, counts = anchored_ordered_partitions()
    words = balanced_words()
    require(len(words) == 6, "six balanced orientation words")
    return {
        "finite_endpoint_example": {
            "d": d,
            "M_end": M,
            "b": b,
            "uniform_all_pair_weights": {str(k): str(w) for k, w in weights.items()},
            "weights_sum": str(sum(weights.values(), F(0))),
            "conditioned_selected_pair_set": sorted([list(p) for p in selected]),
            "conditioned_weights": {str(k): str(w) for k, w in selected_weights.items()},
            "conditioned_weights_sum": str(sum(selected_weights.values(), F(0))),
            "unnormalized_row_sum_weights_total": str(F(1, (M + 1) ** 2) * sum(d - u - v for u, v in product(range(M + 1), repeat=2))),
            "quarter_phase_average": [str(x) for x in gaussian_weighted_sum(weights)],
        },
        "section_dependent_cumulant_example": {
            "v": [str(x) for x in vector],
            "kappa_m": kappa_rows,
            "uniform_section_average_kappa": str(average_kappa),
            "kappa_at_untrimmed_length_d": str(kappa_half(d, vector)),
            "exact_length_correction": str(average_kappa - kappa_half(d, vector)),
            "scope": "exact row-cumulant algebraic witness; pair-product closure, not an ordinary nonpair aggregate counterexample",
        },
        "path_endpoint_correction_example": path_boundary_count(9, (2, -2, 0, 0)),
        "ordinary_prime_product_diagnostics": {
            "near_comparable_products": {"A": 101 * 103, "B": 97 * 107, "gap": 24},
            "unequal_scale_products": {"A": 2 * 3, "B": 101 * 103, "all_factors_prime": True},
            "scope": "finite source tuples once N admits these primes; neither example estimates an asymptotic aggregate",
        },
        "positive_part_noncommutation": positive_part_example,
        "partitions": {
            "total": len(rows),
            "block_counts": counts,
            "sum_of_block_counts": sum(len(blocks) for _, blocks in rows),
            "sign_word_total": 16,
            "balanced_words": words,
            "ordered_terms": [
                {
                    "term": index,
                    "coefficient": coefficient,
                    "ordered_blocks_zero_based": [list(block) for block in blocks],
                    "row_product": "*".join(
                        f"D_m(sum_(j in {list(block)}) v_j)" for block in blocks
                    ),
                }
                for index, (coefficient, blocks) in enumerate(rows, start=1)
            ],
        },
        "joint_selection": {
            "epsilon_1_8": joint_selection_ledger(F(1, 8)),
            "epsilon_1_16": joint_selection_ledger(F(1, 16)),
            "supremal_mean_budget": str(DELTA / 4),
            "prior_delta_over_8_budget": str(DELTA / 8),
        },
    }


def build_report_data() -> dict:
    exact = exact_ledgers()
    return {
        "schema": "wp84.r400.physical-endpoint-averaging.v1",
        "base_commit": "1139e81c5fdfc0ecfc054b892697c6f76f78db31",
        "audit_branch": "codex/wp84-physical-endpoint-averaging-20261103",
        "decisions": {
            "AVERAGED_FOURIER_KERNEL": "EXACT",
            "PHYSICAL_CUMULANT_AVERAGING": "CORRECTION_REQUIRED",
            "JOINT_ENDPOINT_SELECTION": "CONDITIONAL",
            "ORDINARY_CONNECTED_AGGREGATE": "OPEN",
            "R400_CONSUMER": "CONDITIONAL",
        },
        "actual_endpoint_family": {
            "source": "WP84 Decision B/D exact windows",
            "X": "T/(2*pi)=exp(L)",
            "d": "floor(T*L/(2*pi))",
            "M_end": "ceil(d*exp(-sqrt(L)/2))",
            "I_uv": "[b+u,b+d-1-v], 0<=u,v<=M_end",
            "m_uv": "d-u-v >= d-2*M_end",
            "original_pair_measure": "uniform 1/(M_end+1)^2 on W_T={0,...,M_end}^2",
            "trim_scale": "M_end/d=exp(-sqrt(L)/2)+o(1); h*M_end=(1+o(1))*T*exp(-sqrt(L)/2)",
            "historical_correction": "The prior endpoint-near-product note's heuristic M~T*sqrt(L), U~T/sqrt(L) is not the Decision-B window. This revision uses M_end~(TL/(2*pi))*exp(-sqrt(L)/2) and U~T*exp(-sqrt(L)/2). The older commit remains unchanged.",
        },
        "endpoint_identity": {
            "K_uv": "K_uv(Y)=exp(i*T*Y)/(m_uv)*sum_{k=b+u}^{b+d-1-v} exp(2*pi*i*k*Y/L)",
            "average": "E_rho K_uv(Y)=exp(i*T*Y)*sum_{k=b}^{b+d-1} w_k(rho)*exp(2*pi*i*k*Y/L)",
            "weights": "w_k(rho)=sum_{(u,v) in S} rho_uv * 1_{b+u<=k<=b+d-1-v}/(d-u-v)",
            "conditions": "rho_uv>=0, sum_S rho_uv=1; for uniform W_T use rho=1/(M_end+1)^2; for any source-selected nonempty S use its normalized conditional measure",
            "properties": "each w_k>=0 exactly and sum_k w_k=1 exactly; no section endpoint, start phase, or row-normalization factor is dropped",
            "closed_form": "Re K_uv(Y)=sin(pi*m_uv*Y/L)/(m_uv*sin(pi*Y/L))*cos(omega_uv*Y), omega_uv=T+2*pi*(b+u)/L+pi*(m_uv-1)/L",
        },
        "physical_source_correction": {
            "source_coefficient": "c_p=-log(p)/(a_phi(T)*L*sqrt(p)); four-slot coefficient product and all six balanced sign words retained",
            "physical_term": "Re[(prod_j c_{p_j})*Omega_{4,400}(v)*exp(i*T*Y)*exp(2*pi*i*(b+u)*Y/L)*kappa_{m_uv}(v)]",
            "exact_average": "(prod c)*Omega*exp(i*T*Y)*sum_S rho_uv*exp(2*pi*i*(b+u)*Y/L)*kappa_{m_uv}(v)",
            "reference_factorization": "(prod c)*Omega*exp(i*T*Y)*[kappa_d(v)*sum_S rho_uv*exp(2*pi*i*(b+u)*Y/L) + sum_S rho_uv*exp(2*pi*i*(b+u)*Y/L)*(kappa_{m_uv}(v)-kappa_d(v))]",
            "exact_row_correction_bound": "|D_m(x)-D_d(x)|<=2*(d-m)/d for |x| arbitrary; hence |kappa_m(v)-kappa_d(v)|<=150*(d-m)/d from block counts 1,7,12,6 and |D|<=1",
            "finite_principal_section_path": "for closed lag path r with prefixes q_j, span ell=max(q)-min(q), valid roots are [k_- - min(q), k_+ - max(q)]; exact path correction is -(1/m)*sum_{k in I but invalid for r} exp(i*T*Y+2*pi*i*k*Y/L), with magnitude <=ell/m<=4R/m",
            "block_products": "the 26-term cumulant average is sum_pi mu(pi)*E_S[exp(i phase)*prod_{B in pi}D_{m_uv}(Y_B/L)]; the common m_uv couples block factors, so E(prod D_m) is not prod(E D_m)",
            "termwise_26_correction": "exactly one term per ordered partition in exact_checks.partitions.ordered_terms; each correction is coefficient(pi)*[prod_B D_m(v_B)-prod_B D_d(v_B)] with coefficient (-1)^(|pi|-1)",
            "summed_block_count_for_lipschitz_bound": 75,
            "orientation": "six balanced words each counted once; the inherited C24=4*C6=C8 normalization is retained; no extra factor six",
            "status": "the Fourier-kernel identity is exact; factoring Omega and a fixed kappa out of the actual section average requires the displayed row-length correction and finite path-boundary correction",
        },
        "joint_selection": exact["joint_selection"],
        "e2_principal_arc": {
            "source_window": "for product scale M_prod and shift h=pq-rs, H=M_prod/T; |h|<=H gives |log(pq/rs)|<=-log(1-1/T) in the dyadic product cell",
            "major_arc": "the inherited geometry places the important weighted E2 frequencies in the q=1 principal major arc",
            "normalization": "the positive-L2 oversampling insertion pays H=M_prod/T; on fixed supercritical scales M_prod=T^s, s>1, H=T^(s-1), so the published global major-arc L2 bound alone is insufficient",
            "safe_lobe": "the inherited Re(exp(i*T*Y)D_d(Y/L))>=0 lobe is for the public scalar finite trace and public B4_nc sign identity; the latter is not source-matched to Omega_4,400*kappa_m and does not include arbitrary selected starts/section-dependent m",
            "source_decision": "no q=1 source-matched signed remainder or local H^(-1) saving is proved here; no generic minor-arc bound is used to claim closure",
        },
        "exact_checks": exact,
        "smallest_missing_source_estimate": "For C_T(I_uv)=Re of the source-matched ordinary-prime connected aggregate after exact A=B pair contractions, prove limsup_T E_{(u,v) uniform on W_T}[max(0,C_T(I_uv))] < Delta_max/4 (or a direct common-section bound C_T(I_T)<=Delta_max). The strict < Delta_max/4 is the supremal joint-selection threshold from endpoint-good density >=1/4; the parent Delta_max/8 is the epsilon=1/8 instance. This source estimate is open.",
        "decisions_boundary": "Averaging the scalar Fourier kernel does not average the physical cumulant, path boundary, orientation sum, or positive connected excess. Tests verify exact finite identities only.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--write-json", action="store_true")
    args = parser.parse_args()
    data = build_report_data()
    if args.write_json:
        root = Path(__file__).resolve().parents[1]
        target = root / "evidence" / "WP84_R400_PHYSICAL_ENDPOINT_AVERAGING_LEDGER.json"
        target.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
        print(f"WROTE {target.relative_to(root)}")
    if args.json:
        print(json.dumps(data, indent=2, sort_keys=True, default=str))
    elif not args.write_json:
        print("PASS exact endpoint weights, 26-term row-cumulant correction, and joint-selection fractions")
        print("AVERAGED_FOURIER_KERNEL=EXACT; PHYSICAL_CUMULANT_AVERAGING=CORRECTION_REQUIRED")
        print("JOINT_ENDPOINT_SELECTION=CONDITIONAL; ORDINARY_CONNECTED_AGGREGATE=OPEN")


if __name__ == "__main__":
    main()
