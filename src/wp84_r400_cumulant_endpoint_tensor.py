#!/usr/bin/env python3
"""Exact fourth-cumulant endpoint sensitivity and tensor averaging checks.

The finite identities use Fraction and Gaussian-rational arithmetic. This
module deliberately does not assert a source-weighted aggregate estimate.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from itertools import permutations, product
from pathlib import Path


DELTA = F(3675673694911, 148250000000000)
ZERO = (F(0), F(0))
ONE = (F(1), F(0))


def require(ok: bool, message: str) -> None:
    if not ok:
        raise RuntimeError(message)


def cadd(x, y):
    return x[0] + y[0], x[1] + y[1]


def csub(x, y):
    return x[0] - y[0], x[1] - y[1]


def cmul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def cscale(x, scalar):
    return scalar * x[0], scalar * x[1]


def cabs2(x):
    return x[0] * x[0] + x[1] * x[1]


def unit_i(power: int):
    return ((F(1), F(0)), (F(0), F(1)), (F(-1), F(0)), (F(0), F(-1)))[power % 4]


def exp_quarter(k: int, x: F):
    q = 4 * x
    require(q.denominator == 1, f"not a quarter-grid frequency: {x}")
    return unit_i(k * q.numerator)


def set_partitions(items: tuple[int, ...]):
    if not items:
        yield ()
        return
    head, tail = items[0], items[1:]
    for partition in set_partitions(tail):
        for j in range(len(partition)):
            yield partition[:j] + ((head,) + partition[j],) + partition[j + 1 :]
        yield ((head,),) + partition


def ordered_anchored_partitions():
    rows = []
    for partition in set_partitions((0, 1, 2, 3)):
        anchor = next(j for j, block in enumerate(partition) if 0 in block)
        others = tuple(j for j in range(len(partition)) if j != anchor)
        for order in permutations(others):
            blocks = tuple(partition[j] for j in (anchor,) + order)
            rows.append(((-1) ** (len(blocks) - 1), blocks))
    counts = {n: sum(len(blocks) == n for _, blocks in rows) for n in range(1, 5)}
    block_total = sum(len(blocks) for _, blocks in rows)
    require(len(rows) == 26, "fourth cumulant must have 26 ordered partitions")
    require(counts == {1: 1, 2: 7, 3: 12, 4: 6}, "partition-order multiplicities")
    require(block_total == 75, "total number of block factors")
    return rows, counts, block_total


def row_measure(start: int, length: int) -> dict[int, F]:
    require(length > 0, "positive row interval required")
    return {k: F(1, length) for k in range(start, start + length)}


def l1_measure(mu: dict[int, F], nu: dict[int, F]) -> F:
    return sum((abs(mu.get(k, F(0)) - nu.get(k, F(0))) for k in set(mu) | set(nu)), F(0))


def row_mean(start: int, length: int, x: F):
    total = ZERO
    for k in range(start, start + length):
        total = cadd(total, exp_quarter(k, x))
    return cscale(total, F(1, length))


def vector_block_sum(vector, block):
    return sum((vector[j] for j in block), F(0))


def partition_term(coefficient: int, blocks, start: int, length: int, vector):
    value = ONE
    for block in blocks:
        value = cmul(value, row_mean(start, length, vector_block_sum(vector, block)))
    return cscale(value, F(coefficient))


def kappa(start: int, length: int, vector):
    result = ZERO
    for coefficient, blocks in ordered_anchored_partitions()[0]:
        result = cadd(result, partition_term(coefficient, blocks, start, length, vector))
    return result


def kappa_terms(start: int, length: int, vector):
    rows = []
    for index, (coefficient, blocks) in enumerate(ordered_anchored_partitions()[0], start=1):
        rows.append({
            "term": index,
            "coefficient": coefficient,
            "blocks": blocks,
            "value": partition_term(coefficient, blocks, start, length, vector),
        })
    return rows


def partition_deletion_delta(start: int, length: int, side: str, blocks, vector):
    """Exact telescoping expansion for one ordered partition product."""
    require(length >= 2 and side in {"left", "right"}, "valid endpoint deletion")
    new_start = start + (side == "left")
    old_factors = [row_mean(start, length, vector_block_sum(vector, b)) for b in blocks]
    new_factors = [row_mean(new_start, length - 1, vector_block_sum(vector, b)) for b in blocks]
    delta_terms = []
    for j, block in enumerate(blocks):
        difference = csub(new_factors[j], old_factors[j])
        term = difference
        for prior in range(j):
            term = cmul(term, new_factors[prior])
        for later in range(j + 1, len(blocks)):
            term = cmul(term, old_factors[later])
        delta_terms.append(term)
    telescoped = sum_complex(delta_terms)
    full_delta = csub(product_complex(new_factors), product_complex(old_factors))
    require(telescoped == full_delta, "partition-product deletion telescope")
    return telescoped


def product_complex(values):
    result = ONE
    for value in values:
        result = cmul(result, value)
    return result


def tv_cumulant_bound(mu: dict[int, F], nu: dict[int, F]) -> F:
    return F(75) * l1_measure(mu, nu)


def delete_endpoint_mean(start: int, length: int, x: F, side: str):
    """Return (old,new,delta,exact right-hand side) in Gaussian rationals."""
    require(length >= 2 and side in {"left", "right"}, "valid single endpoint deletion")
    old = row_mean(start, length, x)
    if side == "left":
        new_start, endpoint = start + 1, start
    else:
        new_start, endpoint = start, start + length - 1
    new = row_mean(new_start, length - 1, x)
    exact = cscale(csub(new, exp_quarter(endpoint, x)), F(1, length))
    delta = csub(new, old)
    require(delta == exact, f"single {side} deletion identity failed")
    return old, new, delta, exact


def section_tensor_weights(blocks, sections):
    """W_pi(k_B): sections are (start,length,probability), with exact masses."""
    require(sum((mass for _, _, mass in sections), F(0)) == 1, "section masses must sum to one")
    require(all(length > 0 and mass >= 0 for _, length, mass in sections), "valid section probability")
    weights: dict[tuple[int, ...], F] = {}
    order = len(blocks)
    for start, length, mass in sections:
        per_tuple = mass / (length ** order)
        for rows in product(range(start, start + length), repeat=order):
            weights[rows] = weights.get(rows, F(0)) + per_tuple
    require(sum(weights.values(), F(0)) == 1, "each W_pi must have exact unit mass")
    return weights


def weighted_tensor_weights(blocks, sections, section_factor_by_section):
    """Tensor weights with source coefficient/carrier/overlap left in the average.

    Sections are (start,length,probability); section factors are Gaussian
    pairs and may contain the source coefficient, height carrier, and actual
    section-dependent filtered overlap. The row indices below are absolute,
    so the Fourier characters already retain the start phase.
    The resulting weights need not be nonnegative or have total mass one.
    """
    weights = {}
    order = len(blocks)
    total = ZERO
    for start, length, mass in sections:
        section_factor = section_factor_by_section[(start, length)]
        scalar = cscale(section_factor, mass / (length ** order))
        total = cadd(total, cscale(section_factor, mass))
        for rows in product(range(start, start + length), repeat=order):
            weights[rows] = cadd(weights.get(rows, ZERO), scalar)
    require(
        sum_complex(weights.values()) == total,
        "weighted tensor total must retain section overlap and carrier",
    )
    return weights


def sum_complex(values):
    total = ZERO
    for value in values:
        total = cadd(total, value)
    return total


def tensor_fourier_value(weights, blocks, vector):
    result = ZERO
    for rows, weight in weights.items():
        if isinstance(weight, F):
            weight = (weight, F(0))
        character = ONE
        for row, block in zip(rows, blocks):
            character = cmul(character, exp_quarter(row, vector_block_sum(vector, block)))
        result = cadd(result, cmul(weight, character))
    return result


def average_partition_direct(coefficient: int, blocks, sections, vector):
    result = ZERO
    for start, length, mass in sections:
        term = partition_term(coefficient, blocks, start, length, vector)
        result = cadd(result, cscale(term, mass))
    return result


def path_root_interval(start: int, length: int, lags: tuple[int, int, int, int]):
    require(sum(lags) == 0, "closed lag path required")
    q = [0]
    for lag in lags:
        q.append(q[-1] + lag)
    lower = start - min(q)
    upper = start + length - 1 - max(q)
    return {"prefixes": q, "lower": lower, "upper": upper, "count": max(0, upper - lower + 1)}


def path_root_sum(start: int, length: int, lags, x: F):
    interval = path_root_interval(start, length, lags)
    total = ZERO
    for k in range(interval["lower"], interval["upper"] + 1):
        total = cadd(total, exp_quarter(k, x))
    return cscale(total, F(1, length))


def root_deletion_formula(start: int, length: int, lags, x: F, side: str):
    require(side in {"left", "right"}, "side must be left or right")
    old = path_root_sum(start, length, lags, x)
    if side == "left":
        new = path_root_sum(start + 1, length - 1, lags, x)
    else:
        new = path_root_sum(start, length - 1, lags, x)
    interval = path_root_interval(start, length, lags)
    lower, upper = interval["lower"], interval["upper"]
    shared = range(lower + 1, upper + 1) if side == "left" else range(lower, upper)
    edge = lower if side == "left" else upper
    telescoped = ZERO
    for k in shared:
        telescoped = cadd(telescoped, exp_quarter(k, x))
    telescoped = cscale(telescoped, F(1, length * (length - 1)))
    telescoped = csub(telescoped, cscale(exp_quarter(edge, x), F(1, length)))
    require(csub(new, old) == telescoped, f"path root {side} deletion identity")
    return old, new, csub(new, old)


def exact_ledgers():
    parts, counts, total_blocks = ordered_anchored_partitions()
    vector = (F(1, 4), F(-1, 4), F(1, 2), F(-1, 2))
    start, length = 1, 8
    old_measure = row_measure(start, length)
    left_measure = row_measure(start + 1, length - 1)
    right_measure = row_measure(start, length - 1)
    left_tv = l1_measure(old_measure, left_measure)
    right_tv = l1_measure(old_measure, right_measure)
    _, _, left_kappa_delta = (None, None, csub(kappa(start + 1, length - 1, vector), kappa(start, length, vector)))
    _, _, right_kappa_delta = (None, None, csub(kappa(start, length - 1, vector), kappa(start, length, vector)))

    sections = [(0, 6, F(1, 4)), (1, 5, F(1, 4)), (1, 4, F(1, 4)), (2, 4, F(1, 4))]
    weighted_overlap = {
        (0, 6): (F(1), F(0)),
        (1, 5): (F(2, 3), F(1, 3)),
        (1, 4): (F(-1, 2), F(0)),
        (2, 4): (F(1, 3), F(-1, 3)),
    }
    height_carrier = exp_quarter(1, F(1, 4))
    source_coefficient = (F(2, 5), F(0))
    source_factor_by_section = {
        key: cmul(cmul(source_coefficient, value), height_carrier)
        for key, value in weighted_overlap.items()
    }
    weighted_terms = []
    for index, (coefficient, blocks) in enumerate(parts, start=1):
        weights = weighted_tensor_weights(blocks, sections, source_factor_by_section)
        lhs = ZERO
        for s, m, mass in sections:
            term = ONE
            for block in blocks:
                term = cmul(term, row_mean(s, m, vector_block_sum(vector, block)))
            lhs = cadd(
                lhs,
                cscale(
                    cmul(source_factor_by_section[(s, m)], term),
                    mass * coefficient,
                ),
            )
        rhs = cscale(tensor_fourier_value(weights, blocks, vector), F(coefficient))
        require(lhs == rhs, f"weighted tensor identity fails at cumulant term {index}")
        weighted_terms.append({"term": index, "coefficient": coefficient, "exact_identity": True})

    endpoint_term_checks = []
    for index, (coefficient, blocks) in enumerate(parts, start=1):
        left = cscale(partition_deletion_delta(start, length, "left", blocks, vector), F(coefficient))
        left_actual = csub(
            partition_term(coefficient, blocks, start + 1, length - 1, vector),
            partition_term(coefficient, blocks, start, length, vector),
        )
        right = cscale(partition_deletion_delta(start, length, "right", blocks, vector), F(coefficient))
        right_actual = csub(
            partition_term(coefficient, blocks, start, length - 1, vector),
            partition_term(coefficient, blocks, start, length, vector),
        )
        require(left == left_actual and right == right_actual, f"termwise endpoint delta #{index}")
        endpoint_term_checks.append({"term": index, "left_exact": True, "right_exact": True})

    path = (2, -2, 0, 0)
    root_old, root_left, _ = root_deletion_formula(3, 9, path, F(1, 4), "left")
    root_old_r, root_right, _ = root_deletion_formula(3, 9, path, F(1, 4), "right")
    return {
        "partition_ledger": {
            "ordered_terms": [
                {"term": i, "coefficient": c, "blocks": [list(b) for b in blocks]}
                for i, (c, blocks) in enumerate(parts, start=1)
            ],
            "counts_by_blocks": counts,
            "total_terms": len(parts),
            "total_block_factors": total_blocks,
        },
        "total_variation": {
            "theorem": "|kappa_mu(v)-kappa_nu(v)| <= 75*||mu-nu||_1",
            "deletion_left_mu_l1": str(left_tv),
            "deletion_right_mu_l1": str(right_tv),
            "deletion_left_kappa_delta": [str(x) for x in left_kappa_delta],
            "deletion_right_kappa_delta": [str(x) for x in right_kappa_delta],
            "one_deletion_bound": "150/m",
            "two_sections_each_delete_at_most_r_from_d_grid": "300*r/d",
            "scope": "uniform over all real v because |D_mu(x)|<=1",
        },
        "single_endpoint_deletion": {
            "mean_identity": "D_{I'}(x)-D_I(x)=(D_{I'}(x)-exp(2*pi*i*q*x))/m, q=deleted endpoint row",
            "left_carrier_ratio": "exp(2*pi*i*Y/L) when the left endpoint row is deleted",
            "right_carrier_ratio": "1 when the right endpoint row is deleted",
            "termwise_cumulant_rule": "for each of 26 ordered pi, delta(prod_B D_B)=sum_B delta(D_B)*prod_{C before B}D'_C*prod_{C after B}D_C; multiply by the original Mobius coefficient",
            "all_26_terms_checked": endpoint_term_checks,
        },
        "tensor_average": {
            "plain_W_normalization": "sum_(k_B) W_pi(k_B)=1 for every pi",
            "physical_weighted_W_normalization": "sum_(k_B) W_tilde_pi(k_B)=E_s[rho_s*c_sigma*exp(i*T*Y)*Omega_{I_s,pi,R}(v)]; generally complex and not 1; absolute row frequencies k_B in I_s already retain exp(2*pi*i*a_s*Y/L)",
            "physical_weighted_terms_checked": weighted_terms,
            "weighted_section_example": {
                "sections_start_length_mass": [[a, m, str(p)] for a, m, p in sections],
                "section_overlap_Gaussian_pairs": {f"{a}:{m}": [str(z[0]), str(z[1])] for (a, m), z in weighted_overlap.items()},
                "source_coefficient_gaussian_pair": [str(x) for x in source_coefficient],
                "height_carrier": [str(x) for x in height_carrier],
                "all_26_termwise_tensor_equalities": True,
                "scope": "exact algebraic tensorization diagnostic, not WP84 prime-source numerical data",
            },
            "plain_W_by_partition": {
                str(index): {
                    "block_order": [list(block) for block in blocks],
                    "mass": str(sum(section_tensor_weights(blocks, sections).values(), F(0))),
                }
                for index, (_, blocks) in enumerate(parts, start=1)
            },
        },
        "finite_root_boundary": {
            "root_interval": "[a-min(q), a+m-1-max(q)] where q are closed-path prefixes",
            "left_deletion": "old valid-root interval loses its leftmost root if present; new normalized sum uses denominator m-1",
            "right_deletion": "old valid-root interval loses its rightmost root if present; new normalized sum uses denominator m-1",
            "path": list(path),
            "example_old_left_sum": [str(x) for x in root_old],
            "example_new_left_sum": [str(x) for x in root_left],
            "example_old_right_sum": [str(x) for x in root_old_r],
            "example_new_right_sum": [str(x) for x in root_right],
            "per_path_l1_boundary_change": "<=2/m for the root measure; summing source-weighted paths needs an aggregate coefficient bound",
        },
        "source_aggregate_status": {
            "ordinary_products": "A=pq, B=rs; all A!=B and near-alias terms remain",
            "balanced_words": ["".join(w) for w in product(("+", "-"), repeat=4) if w.count("+") == 2],
            "source_coefficient": "prod_j[-log(p_j)/(a_phi(T)*L*sqrt(p_j))]",
            "carrier": "exp(i*T*log(A/B))*exp(2*pi*i*a_I*log(A/B)/L)",
            "missing_estimate": "a source-normalized bound for the full signed sum of endpoint-difference and root-boundary multilinear polynomials, uniform over the admissible sections, below Delta_max",
            "decision": "OPEN",
        },
    }


def report_data():
    return {
        "schema": "wp84.r400.cumulant-endpoint-tensor.v1",
        "base_commit": "0d3bc919451df298ef2a945569d8c3b1eb65192f",
        "audit_branch": "codex/wp84-physical-cumulant-tensor-lift-20261103",
        "decisions": {
            "CUMULANT_ENDPOINT_IDENTITY": "PROVED",
            "TENSOR_AVERAGING": "EXACT",
            "SOURCE_WEIGHTED_CORRECTION": "OPEN",
            "ORDINARY_CONNECTED_RECORD_BOUND": "OPEN",
            "R400_CONSUMER": "CONDITIONAL",
        },
        "exact": exact_ledgers(),
        "quantifier_and_source_limit": "The endpoint and boundary-good density is at least 1/4-epsilon. A record section follows if the mean positive excess is strictly below (1/4-epsilon)*Delta_max. The new tensor identities do not prove this source-weighted hypothesis.",
        "preserved_gates": {"proper_power": "preserved from parent audit", "physical_positive_atom": "preserved; proper-power family, not ordinary-prime aggregate counterexample", "68_820273_percent": "OPEN", "strict_gt_79_percent": "OPEN", "Riemann_Hypothesis": "OPEN"},
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-json", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    data = report_data()
    if args.write_json:
        root = Path(__file__).resolve().parents[1]
        path = root / "evidence" / "WP84_R400_CUMULANT_ENDPOINT_TENSOR_LEDGER.json"
        path.write_text(json.dumps(data, indent=2, sort_keys=True, default=str) + "\n", encoding="utf-8")
        print(f"WROTE {path.relative_to(root)}")
    if args.json:
        print(json.dumps(data, indent=2, sort_keys=True, default=str))
    elif not args.write_json:
        print("PASS 26-term variation identity and tensor normalization")
        print("CUMULANT_ENDPOINT_IDENTITY=PROVED; TENSOR_AVERAGING=EXACT")
        print("SOURCE_WEIGHTED_CORRECTION=OPEN; ORDINARY_CONNECTED_RECORD_BOUND=OPEN")


if __name__ == "__main__":
    main()
