#!/usr/bin/env python3
"""Exact finite bookkeeping for the WP84 R400 endpoint/near-product audit.

This checker verifies rational budget arithmetic and finite logical examples.
The asymptotic estimates and the unresolved prime aggregate are stated in the
companion hostile-proof report; the checker does not promote sampled data to
an asymptotic theorem.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from itertools import product
from pathlib import Path


DELTA = F(3675673694911, 148250000000000)
PAIR_CAP = F(266329, 1000000)
JOINT_DENSITY = F(1, 8)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def balanced_words() -> list[str]:
    return ["".join(word) for word in product(("+", "-"), repeat=4) if word.count("+") == 2]


def endpoint_intersection_ledger() -> dict:
    candidate = {0, 1}
    endpoint_good = {0}
    connected_good = {1}
    require(endpoint_good and connected_good, "each independent existence witness must be nonempty")
    require(not (endpoint_good & connected_good), "hostile sets must be disjoint")

    # Existing endpoint and boundary estimates give a common admissible set of
    # density at least 1/8: endpoint-good density >=1/4, and the nonnegative
    # crossing score is <=8 times its global mean outside at most 1/8.
    density = JOINT_DENSITY
    joint_mean_budget = density * DELTA
    require(joint_mean_budget == F(3675673694911, 1186000000000000), "exact joint budget")
    return {
        "independent_existence_counterexample": {
            "candidate_sections": sorted(candidate),
            "endpoint_good_sections": sorted(endpoint_good),
            "connected_good_sections": sorted(connected_good),
            "intersection": sorted(endpoint_good & connected_good),
            "conclusion": "two separate existence statements do not imply a common section",
        },
        "conditional_joint_selection": {
            "already_admissible_density_lower_bound": str(density),
            "record_delta": str(DELTA),
            "sufficient_global_mean_positive_excess": f"mean_I (C_T(I))_+ < {joint_mean_budget}",
            "exact_fraction": str(joint_mean_budget),
            "proof": "Markov gives connected-bad density <1/8; the endpoint-and-boundary-good set has density >=1/8, so the two sets intersect",
        },
    }


def source_product_grouping() -> dict:
    words = balanced_words()
    require(len(words) == 6, "there must be six balanced orientation words")
    require(words == ["++--", "+-+-", "+--+", "-++-", "-+-+", "--++"], "orientation order/multiplicity")

    factors = (101, 103, 97, 107)
    left, right = factors[0] * factors[1], factors[2] * factors[3]
    require(left == 10403 and right == 10379 and left != right, "preserved actual-prime product witness")
    return {
        "balanced_sign_words_each_counted_once": words,
        "ordered_prime_tuple_multiplicity": "all ordered slot tuples retained within each sign word; no extra factor of six",
        "exact_grouping": "A=product_{epsilon_j=+1} p_j; B=product_{epsilon_j=-1} p_j; coefficient K_{A,B}(I,T) retains every labeled split, Omega_{4,400}(v), and physical kappa_m(v)",
        "carrier": "exp(i*T*log(A/B))*exp(2*pi*i*k_minus*log(A/B)/L)",
        "exact_closure": "A=B implies equality of the two prime multisets by unique factorization; those terms are assigned to pair contractions",
        "near_product_source_summand": {
            "positive_primes": [101, 103],
            "negative_primes": [97, 107],
            "products": [left, right],
            "absolute_integer_gap": abs(left - right),
            "scope": "actual ordinary-prime tuple summand in the inherited ledger; not an asymptotic near-collision or aggregate-sign certificate",
        },
        "spacing_observation": {
            "source_cutoff": "N=floor(exp(L-sqrt(L))) with T=2*pi*exp(L)",
            "individual_scale": "N/T tends to zero",
            "product_scale": "N^2/T is asymptotic to T*exp(-2*sqrt(L))/(2*pi), which tends to infinity",
            "integer_grid": "for distinct integers A,B<=N^2, the available integer spacing only gives T*|log(A/B)| >= T/(N^2+1), a lower bound tending to zero",
            "scope": "this shows N/T does not remove the product near-collision range; it does not assert prime products occupy every integer gap",
        },
    }


def decision_ledger() -> dict:
    sum_cap = PAIR_CAP + DELTA
    require(sum_cap == F(43158947944911, 148250000000000), "exact pair plus record budget")
    return {
        "SCHATTEN_TRANSFER": "PROVED",
        "EXISTENTIAL_ENDPOINT_REDUCTION": "NOT_SUFFICIENT",
        "ORDINARY_CONNECTED_AGGREGATE": "OPEN",
        "R400_CONSUMER": "CONDITIONAL",
        "record_budget": {
            "delta_exact": str(DELTA),
            "pair_plus_delta_exact": str(sum_cap),
            "pair_plus_delta_decimal": "0.29112275173633052276559865092748...",
            "conditional_implication": "if the source-connected ordinary-prime aggregate is <= Delta on one common endpoint/consumer admissible section, then the record ceiling follows, subject to the already listed same-normalization gates",
            "68_820273_route": "separate and stronger: it requires the connected contribution <=0; not established",
        },
        "schatten_transfer": {
            "large_sieve": "Montgomery-Vaughan Theorem 1 plus Lemma 1 self-duality, applied to the m consecutive row frequencies and the distinct source points u_n=log(n)/L modulo one",
            "matrix_bound": "||V||_op^2 <= m-1+delta_spacing^(-1); transpose and adjoint have the same operator norm",
            "spacing": "delta_spacing >=1/((N+1)L), including the wrap gap since u_n<=1-1/sqrt(L)",
            "section_uniformity": "m>=d-2*floor(d/sqrt(L)); delta_spacing^(-1)/m=O(exp(-sqrt(L))) uniformly in section start and admissible length",
            "finite_operator": "the exact compressed matrix remains M_beta+[M_alpha,J_400], with hard band and no circular alias; the trace-square formula uses the actual finite entries",
            "constant_dependencies": "fixed R=400 only; |a_phi(T)| is bounded below for all sufficiently large T; no section-position dependence",
        },
    }


def build_report_data() -> dict:
    return {
        "schema": "wp84.r400.endpoint-near-product-audit.v1",
        "base_commit": "6d4d43cea2479966ba0081dfbb38058fe6fffb87",
        "audit_branch": "codex/wp84-r400-endpoint-near-product-20261103",
        "decisions": decision_ledger(),
        "endpoint_logic": endpoint_intersection_ledger(),
        "ordinary_product_grouping": source_product_grouping(),
        "source_matched_kernel": {
            "physical_kernel": "Phi_{4,400,m}(v)=Omega_{4,400}(v)*kappa_m(v), where kappa_m is the 26-term ordered anchored-partition cumulant built from D_m(sum_B v_j)",
            "pair_subtractions": "all 26 terms retained with block counts 1,7,12,6 and signs +,-,+,-; exact balanced product equalities are assigned to the pair layer",
            "explicit_partition_ledger": "evidence/WP84_R400_SCHATTEN_ORDINARY_LEDGER.json retains every labeled anchored ordered block product and coefficient; all 16 sign words and the six balanced words are retained in the same source ledger",
            "kernel_mismatch": "the public nested-overlap B_{4,nc} kernel is not substituted; inherited physical witness remains Omega>0 and physical kappa=1 at m=10 while public OA=2/5 and B4=0",
            "unresolved": "no source-valid cancellation, Gram/Schur identity, or aggregate estimate for the nonexact near-product and off-diagonal groups was established",
        },
        "preserved_evidence": {
            "positive_proper_power_atom": "(p,p^2,p^3,p^2), T=2*pi*p^5; retained as a lower-order proper-power atom with complete one-base family O_R(L^-4)",
            "controlled_proper_power_family": "full proper-power Q absorption via tau(Q^2)=O_400(L^-2), ||Q||_op=O_400(1), and normalized Schatten-4 root perturbation O_400(L^-1/2)",
            "physical_geometric_kernel_discrepancy": "preserved in predecessor report and source interval replay",
            "older_ordinary_near_product": "101*103 versus 97*107 remains a diagnostic actual-prime tuple; its carrier phase and aggregate sign are unresolved",
        },
        "smallest_unproved_inequality": "There exists a common endpoint-, boundary-, and bounded-consumer-admissible section I_T with Re C_T(I_T)<=Delta_max=3675673694911/148250000000000. A sufficient source-independent joint-selection lemma is mean_{I in all candidate pairs}(C_T(I))_+ < Delta_max/8; this exact mean premise is not proved for the physical source weights.",
        "scope_warning": "Finite rational tests validate bookkeeping only. No sampled prime configuration, synthetic weight, or test pass proves the asymptotic aggregate inequality.",
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", action="store_true", help="emit the machine-readable exact ledger")
    parser.add_argument("--write-json", action="store_true", help="write the machine-readable exact ledger under evidence/")
    args = parser.parse_args()
    data = build_report_data()
    if args.write_json:
        root = Path(__file__).resolve().parents[1]
        target = root / "evidence" / "WP84_R400_ENDPOINT_NEAR_PRODUCT_LEDGER.json"
        target.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
        print(f"WROTE {target.relative_to(root)}")
    if args.json:
        print(json.dumps(data, indent=2, sort_keys=True))
    elif not args.write_json:
        print("PASS: exact rational record ledger, six balanced sign words, and endpoint-intersection counterexample")
        print("SCHATTEN_TRANSFER=PROVED; EXISTENTIAL_ENDPOINT_REDUCTION=NOT_SUFFICIENT")
        print("ORDINARY_CONNECTED_AGGREGATE=OPEN; R400_CONSUMER=CONDITIONAL")


if __name__ == "__main__":
    main()
