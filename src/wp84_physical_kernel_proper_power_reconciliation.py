#!/usr/bin/env python3
"""Independent exact reconciliation of the WP84 fourth-order kernels.

This checker uses only the standard library and Fraction arithmetic.  It
rebuilds set partitions, their anchored orders, the public nested-path
overlaps, and the physical empirical-row factors independently of the
existing WP84 audit scripts.
"""

from __future__ import annotations

import argparse
import json
from collections import Counter
from fractions import Fraction as F
from itertools import permutations
from pathlib import Path


V = (F(1, 5), F(-2, 5), F(3, 5), F(-2, 5))
M_TEST = 10


def set_partitions(items: tuple[int, ...]):
    if not items:
        yield ()
        return
    head, tail = items[0], items[1:]
    for part in set_partitions(tail):
        for i in range(len(part)):
            yield part[:i] + ((head,) + part[i],) + part[i + 1 :]
        yield ((head,),) + part


def ordered_anchored_partitions():
    """Return the 26 anchored ordered block lists and Möbius signs."""
    rows = []
    for part in set_partitions((0, 1, 2, 3)):
        anchor = next(i for i, block in enumerate(part) if 0 in block)
        others = tuple(i for i in range(len(part)) if i != anchor)
        for order in permutations(others):
            rows.append(((-1) ** (len(part) - 1), tuple(part[i] for i in (anchor,) + order)))
    return rows


def subset_sum(block: tuple[int, ...], point: tuple[F, ...] = V) -> F:
    return sum((point[j] for j in block), F(0))


def overlap(positions: tuple[F, ...]) -> F:
    return max(F(0), F(1) - (max(positions) - min(positions)))


def public_nested_overlap(
    ordered_blocks: tuple[tuple[int, ...], ...], point: tuple[F, ...] = V
) -> F:
    """The public term: overlap of its nested ordered-partition path."""
    positions = [F(0)]
    running = F(0)
    for block in ordered_blocks[:-1]:
        running += subset_sum(block, point)
        positions.append(running)
    positions.append(sum(point, F(0)))
    return overlap(tuple(positions))


def source_prefix_overlap(point: tuple[F, ...] = V) -> tuple[F, tuple[F, ...]]:
    points = [F(0)]
    running = F(0)
    for value in point:
        running += value
        points.append(running)
    return overlap(tuple(points)), tuple(points)


def block_row_factor(block: tuple[int, ...], m: int) -> int:
    """Exact D_m(sum_B v_j) at this fifth-grid point when 5 divides m."""
    if m % 5:
        raise ValueError("the exact rational-grid row indicator needs 5 | m")
    u = subset_sum(block)
    return int(u.denominator == 1)


def physical_row_product(ordered_blocks: tuple[tuple[int, ...], ...], m: int) -> int:
    out = 1
    for block in ordered_blocks:
        out *= block_row_factor(block, m)
    return out


def rational_grid_term_vector(point: tuple[F, ...], m: int) -> list[int]:
    """Exact row-factor vector when every tested block frequency is m-grid."""
    values = []
    for sign, blocks in ordered_anchored_partitions():
        product = 1
        for block in blocks:
            u = sum((point[j] for j in block), F(0))
            if (m * u).denominator != 1:
                raise ValueError("block frequency is not on the 1/m rational grid")
            product *= int(u.denominator == 1)
        values.append(sign * product)
    return values


def fraction_text(x: F) -> str:
    return str(x.numerator) if x.denominator == 1 else f"{x.numerator}/{x.denominator}"


def build_ledger() -> dict:
    rows = []
    for index, (sign, blocks) in enumerate(ordered_anchored_partitions(), 1):
        path_overlap = public_nested_overlap(blocks)
        row_product = physical_row_product(blocks, M_TEST)
        rows.append(
            {
                "term": index,
                "mobius_coefficient": sign,
                "ordered_blocks_zero_based": [list(b) for b in blocks],
                "block_frequency_sums": [fraction_text(subset_sum(b)) for b in blocks],
                "public_nested_overlap": fraction_text(path_overlap),
                "public_signed_term": fraction_text(sign * path_overlap),
                "physical_row_product_at_m10": row_product,
                "physical_signed_term_at_m10": sign * row_product,
            }
        )

    oa, prefix = source_prefix_overlap()
    b4 = sum((F(r["public_signed_term"]) for r in rows), F(0))
    kappa10 = sum(r["physical_signed_term_at_m10"] for r in rows)
    counts = Counter(len(r["ordered_blocks_zero_based"]) for r in rows)
    if len(rows) != 26 or dict(counts) != {1: 1, 2: 7, 3: 12, 4: 6}:
        raise RuntimeError("partition ledger count mismatch")
    if oa != F(2, 5) or b4 != 0 or kappa10 != 1:
        raise RuntimeError("exact kernel reconciliation failed")
    if [r["physical_signed_term_at_m10"] for r in rows] != [1] + [0] * 25:
        raise RuntimeError("physical term vector is not e_1")

    zero_point = (F(-3, 4), F(-1, 2), F(1, 2), F(3, 4))
    zero_vector = rational_grid_term_vector(zero_point, 4)
    zero_nonzero = [(i + 1, x) for i, x in enumerate(zero_vector) if x]
    if zero_nonzero != [(1, 1), (8, -1)] or sum(zero_vector) != 0:
        raise RuntimeError("zero-margin witness did not replay")

    abstract_point = (F(1, 6), F(-1, 6), F(11, 12), F(-11, 12))
    abstract_terms = [
        sign * public_nested_overlap(blocks, abstract_point)
        for sign, blocks in ordered_anchored_partitions()
    ]
    abstract_unweighted = sum(abstract_terms, F(0))
    abstract_weighted = abstract_terms[0] + sum(abstract_terms[1:], F(0)) / 100
    if abstract_unweighted != F(-1, 12) or abstract_weighted != F(1187, 1200):
        raise RuntimeError("positive-weight abstract counterexample did not replay")

    # Exact source-admissible p,p^2,p^3,p^2 family.  Its full same-base
    # coefficient sum is O(L^-4), since sum_p log(p)^4/p^4 converges.
    power_family = {
        "prime_exponents": [1, 2, 3, 2],
        "signs": [1, -1, 1, -1],
        "signed_exponent_sum": 0,
        "product_exponent": 8,
        "square_root_product_exponent": 4,
        "coefficient_product": "+(log p)^4/(a_phi(T)^4 L^4 p^4)",
        "slot_coefficients": "c_(p^e)=-(log p)/(a_phi(T) L p^(e/2)); the four minus signs multiply to +",
        "summed_same_base_coefficient_mass": "O(L^-4), using sum_p (log p)^4/p^4 < infinity",
        "source_admission": "for p>=5, p^5 exp(-sqrt(5 log p)) > p^3, so all four slots are <= N on T=2 pi p^5 and L=5 log p",
        "source_scales": "T=2*pi*p^5; L=log(T/(2*pi))=5 log p; N=floor(exp(L-sqrt(L))); h=2*pi/L; d=floor(TL/(2*pi)); q=floor(d/sqrt(L)); selected m>=d-2q",
        "root_intervals_in_slot_order": [["0", "4/5"], ["2/5", "1"], ["0", "2/5"], ["2/5", "1"]],
        "carrier": "1 because the signed logarithmic sum is exactly zero",
        "section_uniformity": "S=0 makes exp(i*T*L*S) exp(2*pi*i*k_minus*S)=1 for every common selected section; m>=10 eventually",
        "orientation_multiplicity_envelope": 48,
        "physical_kernel_envelope": "|(Phi_4,R,m)| <= (13/3) G_R^4; G_R=1+2 H_R/pi",
        "interval_certificate": "48 labeled source/conjugate placements, 24 unique rational vectors; every R400 Omega interval >799/4000; source ordering intervals lie near 0.199750432 or 0.399748481",
        "family_aggregate_bound": "O_R(L^-4); this controls this complete one-base resonance family only",
    }

    return {
        "schema": "wp84.physical-kernel-proper-power-reconciliation.v1",
        "point": [fraction_text(x) for x in V],
        "m_test": M_TEST,
        "partition_counts": {str(k): counts[k] for k in sorted(counts)},
        "common_first_overlap_OA": fraction_text(oa),
        "source_prefix_positions": [fraction_text(x) for x in prefix],
        "public_geometric_B4": fraction_text(b4),
        "physical_kappa_m10": fraction_text(F(kappa10)),
        "physical_term_vector_m10": [str(r["physical_signed_term_at_m10"]) for r in rows],
        "physical_uniform_lower_bound_m_ge_10": "1 - 7*(2/m)^2 - 12*(2/m)^3 - 6*(2/m)^4 >= 384/625",
        "zero_margin_diagnostic": {
            "point": [fraction_text(x) for x in zero_point],
            "m": 4,
            "nonzero_term_vector_entries_one_based": [[i, value] for i, value in zero_nonzero],
            "unweighted_bracket": "0",
            "reweighting": "weight term 1 by 1+delta and term 8 by 1; exact bracket becomes delta for every rational delta",
            "classification": "rational-grid diagnostic only; not asserted source-admissible",
        },
        "abstract_positive_weight_counterexample": {
            "point": [fraction_text(x) for x in abstract_point],
            "positive_term_weights": ["1"] + ["1/100"] * 25,
            "unweighted_public_bracket": fraction_text(abstract_unweighted),
            "positively_reweighted_bracket": fraction_text(abstract_weighted),
            "classification": "abstract weight-mask counterexample only; not actual source-admissible arithmetic evidence",
        },
        "public_and_physical_partition_term_ledger": rows,
        "kernel_reconciliation": {
            "same": ["26 anchored ordered partitions", "Möbius coefficients", "original tuple coefficient", "carrier", "R400 cutoff", "root intervals", "source-selected section", "label/orientation accounting"],
            "divergence": "public factor is a nested-path overlap for each partition; physical factor is the product over blocks of empirical row averages D_m(sum_B v_j), multiplied by one common external filtered overlap Omega_4,R(v)",
            "pair_subtraction": "not the divergence at the fixed tuple: pair contraction is separated only in B4=Pair4+Connected4,row+o(1); both connected ledgers use the same partition Möbius signs",
            "finite_section": "at m=10 the physical term vector is e_1 exactly; for every selected m>=10 the independent 25-term bound gives kappa_m>=384/625",
        },
        "proper_power_ledger_entry": power_family,
        "global_proper_power_sector": {
            "exact_square_mass": "(1/(|a_phi|^2 L^2))*sum_p (log p)^2/[p(p-1)]",
            "uniform_bound": "<=64/(|a_phi|^2 L^2) <=256/L^2 once |a_phi|>=1/2",
            "proof_bound": "log x<=4*x^(1/4) and p(p-1)>=p^2/2; sum_{n>=2} n^(-3/2)<=2",
            "absolute_first_mass": "O(1), not o(1)",
            "what_square_mass_does_not_prove": "the complete quartic aggregate containing a proper-power label, without an independent prime fourth-moment/Schatten bound or signed multilinear estimate",
            "conditional_quartic_removal": "if the ordinary-prime band matrix Y has normalized Schatten-4 norm O(1) on the same section, and the proper-power matrix P has ||P||op=O_R(1), tau(P^2)=O_R(L^-2), then ||P||4=O_R(L^-1/2) and |tau((Y+P)^4)-tau(Y^4)|=O_R(L^-1/2); this hypothesis is not proved here",
        },
        "ordinary_prime_sector": {
            "exact_nonpair_closure": "impossible by unique factorization; exact p0*p2=p1*p3 forces pairings for ordinary primes",
            "near_products_and_near_aliases": "retained and uncontrolled by the kernel pointwise sign or proper-power square mass",
            "pair_subtraction": "the exact pair layer is removed by Pair4; no source-admissible positive ordinary-prime non-pair aggregate was established in this audit",
        },
        "r400_consumer": {
            "pair_bound": "Pair_400 < 0.266329+o(1)",
            "needed_inequality": "Re integral Phi_4,400,m(v) dmu_T,I(v) <= Delta_400+o(1), Delta_400 <= 0, or a quantified nonpositive allowance compatible with the consumer",
            "previous_conditional_positive_error_budget": "3675673694911/148250000000000 = 0.024793751736...",
            "status": "OPEN; the ordinary-prime signed near-product/near-alias aggregate is not bounded here",
        },
        "decision": "PROPER_POWER_EXCEPTION_CONTROLLED",
        "decision_scope": "the reported (p,p^2,p^3,p^2) positive resonance family is proper-power-containing and its complete same-base/permutation aggregate is O_R(L^-4); this does not close the full R400 aggregate or consumer",
        "pointwise_physical_sign": "positive: Omega_4,400>799/4000 and kappa_m>=384/625, hence Phi_4,400,m>9588/78125 for the admitted family",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    result = build_ledger()
    encoded = json.dumps(result, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        args.json.write_text(encoded, encoding="utf-8")
    print(encoded, end="")
    print("EXACT: public O_A=2/5, B4=0; physical kappa_10=1 from 26-term e1 vector")
    print("EXACT: 1/7/12/6 partition counts; positive source-family aggregate O_R(L^-4)")
    print("DECISION: PROPER_POWER_EXCEPTION_CONTROLLED (scope limited to the reported atom family)")


if __name__ == "__main__":
    main()
