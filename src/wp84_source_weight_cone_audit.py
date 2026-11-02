#!/usr/bin/env python3
"""Exact rational audit of WP84's fourth-order row-cumulant weights.

This checker reconstructs the 26 anchored ordered partitions, exact rational
Dirichlet-grid vectors, a positive actual prime-power atom, an exact zero
margin case, and the previously supplied abstract countermodel. It does not
claim a sign for the complete prime-pool sum.
"""

from __future__ import annotations

import argparse
import json
import math
from fractions import Fraction as Q
from itertools import combinations, permutations
from pathlib import Path


WITNESS = (Q(1, 5), -Q(2, 5), Q(3, 5), -Q(2, 5))
ZERO_WITNESS = (-Q(3, 4), -Q(1, 2), Q(1, 2), Q(3, 4))
ABSTRACT_SHIFTS = (Q(1, 6), -Q(1, 6), Q(11, 12), -Q(11, 12))


def _require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def _set_partitions(items: list[int]):
    if not items:
        yield []
        return
    first, rest = items[0], items[1:]
    for part in _set_partitions(rest):
        for index in range(len(part)):
            yield part[:index] + [[first] + part[index]] + part[index + 1:]
        yield [[first]] + part


def ordered_partitions():
    """Return the 26 source terms, retaining the anchored block order."""
    output = []
    for partition in _set_partitions([0, 1, 2, 3]):
        anchor = next(i for i, block in enumerate(partition) if 0 in block)
        tail = [i for i in range(len(partition)) if i != anchor]
        for order in permutations(tail):
            blocks = tuple(tuple(sorted(partition[i])) for i in (anchor,) + order)
            output.append(((-1) ** (len(blocks) - 1), blocks))
    _require(len(output) == 26, "ordered-partition count changed")
    counts = {k: sum(len(blocks) == k for _, blocks in output) for k in range(1, 5)}
    _require(counts == {1: 1, 2: 7, 3: 12, 4: 6}, "ordered-partition multiplicities changed")
    return output


def _sum_block(v: tuple[Q, ...], block: tuple[int, ...]) -> Q:
    return sum((v[j] for j in block), Q(0))


def exact_grid_term_vector(v: tuple[Q, ...], rows: int):
    """Exact term vector when every block frequency is a Fourier-grid point."""
    if len(v) != 4 or rows <= 0:
        raise ValueError("four shifts and a positive row count are required")
    if any(rows % x.denominator for x in v):
        raise ValueError("each shift denominator must divide the row count")
    vector = []
    for sign, blocks in ordered_partitions():
        factor = 1
        for block in blocks:
            total = _sum_block(v, block)
            factor *= int(total.denominator == 1)
        vector.append(sign * factor)
    return tuple(vector)


def rational_grid_zero(v: tuple[Q, ...], rows: int) -> bool:
    return sum(exact_grid_term_vector(v, rows)) == 0


def orientation_vectors():
    """Six balanced orthants, two positive orders, two negative orders."""
    result = []
    for positive_slots in combinations(range(4), 2):
        for positive_values in permutations((Q(1, 5), Q(3, 5))):
            for negative_values in permutations((-Q(2, 5), -Q(2, 5))):
                p_iter = iter(positive_values)
                n_iter = iter(negative_values)
                result.append(tuple(next(p_iter) if j in positive_slots else next(n_iter)
                                    for j in range(4)))
    _require(len(result) == 24, "six-by-four orientation multiplicity changed")
    _require(len(set(result)) == 12, "expected 12 unique vectors after repeated negative shifts")
    return tuple(result)


def exact_source_atom_data():
    """Symbolic source admission and sign for n=(p,p^2,p^3,p^2)."""
    exponents = (1, 2, 3, 2)
    signs = (1, -1, 1, -1)
    v = tuple(Q(s * e, 5) for s, e in zip(signs, exponents))
    _require(v == WITNESS, "prime-power realization changed")
    _require(sum(v, Q(0)) == 0, "source atom is not log-product closed")
    # At L=5 log p and N=floor(p^5 exp(-sqrt(5 log p))), p>=5 gives N>p^3.
    # Thus all four entries are in the actual complete prime-power pool.
    _require(max(exponents) == 3, "cutoff exponent changed")
    return {
        "n_exponents_of_p": list(exponents),
        "epsilon": list(signs),
        "v": [str(x) for x in v],
        "L": "5*log(p)",
        "T": "2*pi*p^5",
        "cutoff": "N=floor(exp(L-sqrt(L)))=floor(p^5*exp(-sqrt(5*log(p))))",
        "admission_proof": "for every prime p>=5, 2*log(p)>sqrt(5*log(p)), hence p^5*exp(-sqrt(5*log(p)))>p^3; all n_j=p^(1,2,3,2)<=N",
        "lambda_n": "Lambda(p^e)=log(p) for e=1,2,3",
        "coefficient_product": "+(log(p))^4/(a_phi(T)^4*L^4*p^4), positive for all sufficiently large T since a_phi(T)->1",
        "physical_closure_S": "0",
        "carrier_phase": "exp(i*T*L*S)*exp(2*pi*i*k_minus*S)=1 for every selected section",
        "selected_section": "I=[k_minus,k_plus], m=|I|>=d-2q, d=floor(TL/(2*pi)), q=floor(d/sqrt(L)); therefore m>=10 for all sufficiently large p, uniformly in the selected endpoints",
        "filters": "R=400; J_v=[max(0,-v),min(1,1-v)] for |v|<1; all four intervals are nonempty",
    }


def actual_weight_bound(rows_min: int = 10):
    """Exact rational domination of the 25 nontrivial partition terms."""
    if rows_min < 1:
        raise ValueError("rows_min must be positive")
    tail = (Q(7) * Q(2, rows_min) ** 2
            + Q(12) * Q(2, rows_min) ** 3
            + Q(6) * Q(2, rows_min) ** 4)
    return Q(1) - tail, tail


def term_ledger(v: tuple[Q, ...] = WITNESS):
    result = []
    for index, (sign, blocks) in enumerate(ordered_partitions(), start=1):
        sums = [_sum_block(v, block) for block in blocks]
        result.append({
            "term": index,
            "partition_coefficient": sign,
            "block_count": len(blocks),
            "ordered_blocks_zero_based": [list(block) for block in blocks],
            "block_frequency_sums": [str(x) for x in sums],
            "actual_row_factor": "*".join(f"D_m({x})" for x in sums),
            "term_factor_when_5_divides_m": sign * int(all(x.denominator == 1 for x in sums)),
        })
    return result


def abstract_countermodel():
    """Reproduce the supplied abstract 26-walk positive reweighting exactly."""
    terms = []
    for partition in _set_partitions([0, 1, 2, 3]):
        sign = (-1) ** (len(partition) - 1)
        anchor = next(i for i, block in enumerate(partition) if 0 in block)
        tail = [i for i in range(len(partition)) if i != anchor]
        for order in permutations(tail):
            chain = [anchor] + list(order)
            used: set[int] = set()
            masks = []
            for index in chain[:-1]:
                used.update(partition[index])
                masks.append(tuple(sorted(used)))
            terms.append((sign, tuple(masks)))
    _require(len(terms) == 26, "abstract ordered term count changed")

    def overlap(masks, shifts):
        positions = [Q(0)]
        for mask in masks:
            positions.append(sum((shifts[j] for j in mask), Q(0)))
        positions.append(sum(shifts, Q(0)))
        return max(Q(0), Q(1) - (max(positions) - min(positions)))

    weighted = Q(0)
    unweighted = Q(0)
    for index, (sign, masks) in enumerate(terms):
        atom = sign * overlap(masks, ABSTRACT_SHIFTS)
        unweighted += atom
        weighted += atom * (Q(1) if index == 0 else Q(1, 100))
    _require(unweighted == -Q(1, 12), "abstract unweighted bracket changed")
    _require(weighted == Q(1187, 1200), "abstract reweighting changed")
    return {
        "balanced_shifts": [str(x) for x in ABSTRACT_SHIFTS],
        "unweighted_bracket": str(unweighted),
        "positive_weights": ["1"] + ["1/100"] * 25,
        "reweighted_bracket": str(weighted),
        "classification": "ABSTRACT_ONLY; not source-admissible WP84 evidence",
    }


def build_evidence():
    m10_vector = exact_grid_term_vector(WITNESS, 10)
    zero_vector = exact_grid_term_vector(ZERO_WITNESS, 4)
    margin, tail = actual_weight_bound(10)
    _require(sum(m10_vector) == 1 and m10_vector[0] == 1 and sum(x != 0 for x in m10_vector) == 1,
             "denominator-five exact vector changed")
    _require(sum(zero_vector) == 0 and sum(x != 0 for x in zero_vector) == 2,
             "zero-margin witness changed")
    _require(margin == Q(384, 625) and tail == Q(241, 625), "rational margin changed")
    positive_family = orientation_vectors()
    conjugate_family = tuple(tuple(-x for x in v) for v in positive_family)
    orientations = positive_family + conjugate_family
    _require(len(orientations) == 48 and len(set(orientations)) == 24,
             "source/conjugate orientation multiplicity changed")
    orientation_term_ledgers = []
    for family_name, family_vectors in (("source", positive_family),
                                        ("conjugate", conjugate_family)):
        seen_family = set()
        for vector in family_vectors:
            if vector in seen_family:
                continue
            seen_family.add(vector)
            orientation_term_ledgers.append({
                "family": family_name,
                "v": [str(x) for x in vector],
                "source_atom_coefficient_product": "positive; same magnitude for all label permutations",
                "carrier_phase": "1 because S=0",
                "ordered_partition_terms": term_ledger(vector),
            })
    for v in orientations:
        _require(sum(v, Q(0)) == 0, "orientation left the balanced closed sector")
        _require(exact_grid_term_vector(v, 10)[0] == 1
                 and sum(exact_grid_term_vector(v, 10)) == 1,
                 "an orientation changed the exact cumulant")

    return {
        "schema": "wp84.source-weight-cone-fourth-order.v1",
        "source_basis": {
            "repository_commit": "861bdad5f6f6495c5b755546b4b2fa43367e2901",
            "fourth_order_definition": "finite empirical row cumulant of actual hard-band filtered prime matrix; see WP84_R400_FILTERED_CONNECTED_KERNEL.md §§1-3",
            "source_mask": "1_{n_j is a prime power <=N} times 1_{epsilon_j in {+1,-1}}; common to all 26 partitions; no fifth-order callback is used",
            "selected_section_mask": "k in I=[k_minus,k_plus], m=|I|; row averages D_m; selected endpoints common to terms",
        },
        "source_operator_and_admission": {
            "scale": "L=log(T/(2*pi)); h=2*pi/L; d=floor(T*L/(2*pi))",
            "prime_power_cutoff": "N=floor(exp(L-sqrt(L))); n=p^e with 2<=n<=N; Lambda(p^e)=log(p)",
            "coefficient": "c_n=-Lambda(n)/(a_phi(T)*L*sqrt(n)); a_phi(T)->1",
            "sign_domain": "epsilon_j in {-1,+1}; v_j=epsilon_j*log(n_j)/L; all 16 sign words retained; balanced sector has 6 two-positive/two-negative placements",
            "root_interval": "J_v=[max(0,-v),min(1,1-v)] if |v|<1; empty if |v|>=1",
            "section_selection": "I=[k_minus,k_plus] common; m=|I|>=d-2q, q=floor(d/sqrt(L)); selection is by the shared endpoint-score rule",
            "row_normalization": "E_I=m^(-1)*sum_(k in I); D_m(u)=m^(-1)*sum_(j=0)^(m-1) exp(2*pi*i*j*u)",
            "hard_band_cutoff": "R=400; closed row-index paths have r_j in [-400,400], sum r_j=0; source note count=342615201 paths",
            "filtered_overlap": "Omega_4,400(v)=integral_0^1 product_(j=0)^3 (F_400 1_{J_vj})(x+p_j) dx; p_j=sum_(a<j)v_a",
            "overlap_fourier_phase": "sum_(|r_j|<=400,sum r_j=0) product_j a_r(v_j)*exp(2*pi*i*sum_j r_j*p_j), a_r(v)=integral_(J_v) exp(-2*pi*i*r*x) dx",
            "source_carrier": "exp(i*T*L*S)*exp(2*pi*i*k_minus*S), common to all 26 terms; equals 1 on S=0",
            "conjugation": "for nonclosed S, use the common midpoint phase exp(pi*i*(m-1)*S) and centered real Dirichlet factors; the kernel may be complex; on S=0 each term is real",
            "alias_conditions": "physical alias variable S=sum_j epsilon_j*log(n_j)/L; exact row aliases are S in Z and near-alias windows have width O(1/(T*L)); no alias or non-pair term is deleted in the full aggregate",
            "source_selection_scope": "the row selector is the common selected section from the fixed-band endpoint-score construction; no termwise section or diagnostic prime pool is substituted",
        },
        "partition_counts": {str(k): sum(len(blocks) == k for _, blocks in ordered_partitions()) for k in range(1, 5)},
        "grouped_cumulant_coefficients": {
            "one_block": "+1",
            "four_one_plus_three_splits": "-1 each; 4 terms",
            "three_pair_pair_splits": "-1 each; 3 terms",
            "six_one_one_two_splits": "+2 each after 2 anchored orders; 6 grouped terms",
            "four_singletons": "-6 after 6 anchored orders",
        },
        "actual_source_atom": exact_source_atom_data(),
        "row_factor_relations": {
            "definition": "for each ordered partition pi, t_pi(v)=(-1)^(|pi|-1)*product_(B in pi) D_m(sum_(j in B) v_j)",
            "D_m": "D_m(u)=m^(-1)*sum_(k=0)^(m-1) exp(2*pi*i*k*u)",
            "common_outer_factor": "(product_j c_nj)*exp(i*T*L*S)*exp(2*pi*i*k_minus*S)*Omega_4,R(v), identical across all 26 terms",
            "not_a_common_nonnegative_factor_globally": "D_m block products differ by partition and may be signed/complex away from closure; the common tuple coefficient is not globally nonnegative after carrier and filtered overlap",
        },
        "witness_term_vector_at_m_10": list(m10_vector),
        "witness_kappa_at_m_10": str(sum(m10_vector)),
        "witness_cone": {
            "evaluated_source_vector": "e_1 (first one-block coordinate is +1; other 25 coordinates vanish) at m=10",
            "nonpositive_multiplier_cone": "{u in R^26 : u_1<=0}; no vector with every u_j>0 belongs",
            "actual_unreweighted_multiplier": "(1,...,1), giving +1",
            "for_every_selected_m_ge_10": {
                "proper_block_bound": "|D_m(r/5)|<2/m for noninteger r/5",
                "sum_of_25_term_magnitudes_at_m10": str(tail),
                "strict_positive_lower_bound": str(margin),
                "formula": "kappa_m >= 1 - 7*(2/m)^2 - 12*(2/m)^3 - 6*(2/m)^4 >= 384/625 > 0",
            },
        },
        "orientation_multiplicity": {
            "balanced_orthants_per_family": 6,
            "families": ["source", "conjugate"],
            "orders_per_orthant": 4,
            "ordered_cases_per_source_or_conjugate_family": 24,
            "ordered_cases_both_families": 48,
            "unique_vectors_after_equal_negative_shifts": len(set(orientations)),
            "kappa_invariance": "The row cumulant is symmetric under label permutation; exact grid evaluation is 1 for all 48 labeled cases when 5 divides m, and the m>=10 lower bound is permutation-uniform",
            "conjugation": "The sign-reversed family has the same positive coefficient and real kappa on S=0; both filtered overlaps are interval-certified positive",
            "source_admission_and_carrier_invariance": "The complete prime-power cutoff indicator and closed carrier are unchanged by these permutations and by conjugation",
            "external_overlap_invariance": "Omega_4,400 is order-dependent; all 24 unique values across both conjugate families are separately interval-certified positive",
            "orientation_interval_certificate": "R400 external Omega interval values for source and conjugate families are in WP84_SOURCE_WEIGHT_CONE_ORIENTATION_INTERVALS.json",
        },
        "zero_margin_test": {
            "v": [str(x) for x in ZERO_WITNESS],
            "rows": 4,
            "term_vector": list(zero_vector),
            "nonzero_term_indices_one_based": [i + 1 for i, x in enumerate(zero_vector) if x],
            "kappa": str(sum(zero_vector)),
            "reweighting": "multiply first nonzero term by 1+delta and keep the second at 1; bracket=delta, so either sign occurs arbitrarily near delta=0",
            "classification": "exact finite-grid zero-margin diagnostic; not used as the legal positive source atom",
        },
        "abstract_countermodel": abstract_countermodel(),
        "aggregate_gate": "OPEN: positivity of a legal atom disproves a pointwise nonpositive kernel claim, but does not determine the complete signed sum over the full prime-power pool",
        "decision": "LEGAL_SOURCE_COUNTEREXAMPLE",
        "decision_scope": "pointwise source-admissible balanced fourth-order kernel atom; full arithmetic aggregate remains unproved",
        "theorem_claims": {"strict_gt_79_percent": "OPEN", "unconditional_RH": "OPEN"},
        "ledger": term_ledger(),
        "orientation_term_ledgers": orientation_term_ledgers,
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--write-evidence", action="store_true")
    args = parser.parse_args()
    evidence = build_evidence()
    rendered = json.dumps(evidence, indent=2, sort_keys=True) + "\n"
    if args.write_evidence:
        root = Path(__file__).resolve().parents[1]
        path = root / "evidence" / "WP84_SOURCE_WEIGHT_CONE_26_TERM_LEDGER.json"
        path.write_text(rendered, encoding="utf-8")
        print(f"WROTE {path.relative_to(root)}")
    else:
        print(rendered, end="")
    print("EXACT: 26 ordered partitions; source atom is cutoff-admissible and closed")
    print("EXACT: kappa_m >= 384/625 for every selected m>=10 on the positive witness")
    print("EXACT: zero-margin finite-grid diagnostic and abstract countermodel reproduced")
    print("DECISION: LEGAL_SOURCE_COUNTEREXAMPLE (pointwise atom); full-pool aggregate OPEN")


if __name__ == "__main__":
    main()
