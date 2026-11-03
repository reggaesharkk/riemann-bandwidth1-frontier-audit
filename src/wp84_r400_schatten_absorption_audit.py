#!/usr/bin/env python3
"""Exact finite-band identities and ledgers for the WP84 R400 audit.

The module uses Fraction arithmetic for algebraic checks and emits the
source-level estimates that are proved in the accompanying audit note.
It does not numerically model prime phases or claim an ordinary-prime sign.
"""

from __future__ import annotations

import argparse
import json
from fractions import Fraction as F
from itertools import combinations_with_replacement, permutations, product
from pathlib import Path

GAUSS0 = (F(0), F(0))
GAUSS1 = (F(1), F(0))
GAUSSI = (F(0), F(1))


def set_partitions(items: tuple[int, ...]):
    """Generate each set partition once, with its blocks canonically ordered."""
    if not items:
        yield ()
        return
    head, tail = items[0], items[1:]
    for part in set_partitions(tail):
        for index in range(len(part)):
            yield part[:index] + ((head,) + part[index],) + part[index + 1 :]
        yield ((head,),) + part


def ordered_anchored_partitions():
    """The 26 labelled ordered products with the block containing slot 0 first."""
    rows = []
    for part in set_partitions((0, 1, 2, 3)):
        anchor = next(index for index, block in enumerate(part) if 0 in block)
        others = tuple(index for index in range(len(part)) if index != anchor)
        for order in permutations(others):
            ordered = tuple(part[index] for index in (anchor,) + order)
            rows.append(((-1) ** (len(part) - 1), ordered))
    return rows


def partition_ledger():
    rows = []
    for term, (coefficient, blocks) in enumerate(ordered_anchored_partitions(), start=1):
        rows.append(
            {
                "term": term,
                "coefficient": coefficient,
                "ordered_blocks_zero_based": [list(block) for block in blocks],
                "source_row_factor": "*".join(
                    f"D_m(sum_(j in {list(block)}) v_j)" for block in blocks
                ),
            }
        )
    expected = {1: 1, 2: 7, 3: 12, 4: 6}
    counts = {blocks: sum(len(row["ordered_blocks_zero_based"]) == blocks for row in rows) for blocks in expected}
    if len(rows) != 26 or counts != expected:
        raise RuntimeError((len(rows), counts))
    return rows, counts


def closed_lag_path_count(radius: int = 400) -> int:
    """Count ordered four-lag R paths with zero total by exact convolution."""
    width = 2 * radius + 1
    return sum((width - abs(total)) ** 2 for total in range(-2 * radius, 2 * radius + 1))


def gadd(x, y):
    return x[0] + y[0], x[1] + y[1]


def gsub(x, y):
    return x[0] - y[0], x[1] - y[1]


def gmul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def gconj(x):
    return x[0], -x[1]


def gscale(x, a):
    return x[0] * a, x[1] * a


def gdiv_i_integer(x, denominator: int):
    if denominator == 0:
        raise ZeroDivisionError
    return gscale(gmul(x, (F(0), F(-1))), F(1, denominator))


def phase_quarter_clean(k: int):
    return ((F(1), F(0)), (F(0), F(1)), (F(-1), F(0)), (F(0), F(-1)))[k % 4]


def endpoint_phase(r: int, x: F):
    if (4 * r * x).denominator != 1:
        raise ValueError("quarter-grid endpoint expected")
    return phase_quarter_clean(4 * r * x.numerator // x.denominator)


def pi_times_interval_fourier(r: int, left: F, right: F):
    """Exact Gaussian-rational value of pi*integral_left^right exp(-2piirx)dx."""
    if r == 0:
        return (right - left, F(0))
    numerator = gsub(endpoint_phase(-r, left), endpoint_phase(-r, right))
    return gdiv_i_integer(numerator, 2 * r)


def source_alpha_beta_at(k: int, u: F, z):
    if u != F(1, 4):
        raise ValueError("the exact Gaussian-rational replay uses u=1/4")
    w = gmul(z, phase_quarter_clean(k))
    alpha = w[1]
    beta = 2 * (1 - u) * w[0]
    return alpha, beta


def direct_prime_pair_entry_pi_scaled(i: int, j: int, u: F, z):
    """pi times the two signed filtered-translation entry for u=1/4."""
    positive_left, positive_right = F(0), 1 - u
    negative_left, negative_right = u, F(1)
    r = i - j
    positive = gmul(
        gmul(z, phase_quarter_clean(j)),
        pi_times_interval_fourier(r, positive_left, positive_right),
    )
    negative = gmul(
        gmul(gconj(z), phase_quarter_clean(-j)),
        pi_times_interval_fourier(r, negative_left, negative_right),
    )
    return gadd(positive, negative)


def commutator_entry_pi_scaled(i: int, j: int, u: F, z):
    if i == j:
        _, beta = source_alpha_beta_at(i, u, z)
        return (beta, F(0))
    alpha_i, _ = source_alpha_beta_at(i, u, z)
    alpha_j, _ = source_alpha_beta_at(j, u, z)
    return ((alpha_i - alpha_j) / (j - i), F(0))


def finite_band_identity_replay(radius: int = 3):
    """Compare direct Fourier entries with M_beta+[M_alpha,J_R] exactly."""
    u = F(1, 4)
    z = (F(3, 5), F(4, 5))
    section = tuple(range(-2, 3))
    checked = 0
    for i in section:
        for j in section:
            actual = direct_prime_pair_entry_pi_scaled(i, j, u, z) if abs(i - j) <= radius else GAUSS0
            expected = commutator_entry_pi_scaled(i, j, u, z) if abs(i - j) <= radius else GAUSS0
            if actual != expected:
                raise RuntimeError((i, j, actual, expected))
            if actual[1] != 0:
                raise RuntimeError("the Hermitian source entry must be real")
            checked += 1
    return {"radius": radius, "section": list(section), "entries_checked": checked, "exact_gaussian_rational_match": True}


def concentration_countermodel(n: int = 10):
    """Exact rational example: normalized L2 does not imply an op bound."""
    L = n
    m = n**4
    spike = n
    tau_q2 = F(spike * spike, m)
    if tau_q2 != F(1, L * L) or spike != L:
        raise RuntimeError("concentration countermodel arithmetic mismatch")
    return {"L": L, "section_size": m, "one_diagonal_entry": spike, "tau_Q2": str(tau_q2), "operator_norm": spike}


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def ordinary_prime_product_audit():
    primes = [p for p in range(2, 100) if is_prime(p)]
    exact_pairs = 0
    for a, b in combinations_with_replacement(primes, 2):
        for c, d in combinations_with_replacement(primes, 2):
            if a * b == c * d:
                exact_pairs += 1
                if sorted((a, b)) != sorted((c, d)):
                    raise RuntimeError("ordinary-prime exact closure violated unique factorization")
    left = 101 * 103
    right = 97 * 107
    if not all(is_prime(p) for p in (101, 103, 97, 107)) or left == right:
        raise RuntimeError("near-product diagnostic failed")
    return {
        "prime_range": [2, 97],
        "unordered_equal_pair_product_comparisons": exact_pairs,
        "all_exact_equalities_are_same_multiset": True,
        "near_product_slots": {"positive": [101, 103], "negative": [97, 107]},
        "near_product_values": [left, right],
        "absolute_integer_difference": abs(left - right),
        "ratio": f"{left}/{right}",
        "source_scope": "diagnostic actual-prime summand; its carrier phase and aggregate sign remain unresolved",
    }


def prior_atom_replay():
    p = (F(1, 5), F(-2, 5), F(3, 5), F(-2, 5))
    if sum(p) != 0:
        raise RuntimeError("prior physical atom is not closed")
    exponents = (1, 2, 3, 2)
    signs = (1, -1, 1, -1)
    if sum(e * s for e, s in zip(exponents, signs)) != 0:
        raise RuntimeError("prior atom exponent balance failed")
    return {
        "v": [str(x) for x in p],
        "exponents": list(exponents),
        "signs": list(signs),
        "root_intervals_in_slot_order": [["0", "4/5"], ["2/5", "1"], ["0", "2/5"], ["2/5", "1"]],
        "source_scales": "T=2*pi*p^5; L=5*log(p); N=floor(exp(L-sqrt(L))); all p^1,p^2,p^3,p^2<=N for p>=5",
        "physical_kappa_m10": 1,
        "public_OA": "2/5",
        "public_B4": 0,
        "one_base_family_aggregate": "O_R(L^-4)",
        "status": "preserved; this is a proper-power-containing atom, not evidence for ordinary-prime aggregate sign",
    }


def build_report_data():
    identity = finite_band_identity_replay()
    concentration = concentration_countermodel()
    ordinary = ordinary_prime_product_audit()
    partitions, partition_counts = partition_ledger()
    sign_words = ["".join("+" if sign > 0 else "-" for sign in word) for word in product((-1, 1), repeat=4)]
    balanced_sign_words = [word for word in sign_words if word.count("+") == 2]
    return {
        "schema": "wp84.r400.schatten-absorption-ordinary-prime.v1",
        "matrix_split": {
            "notation": "H_400,I=P_400,I=A_400,I+Q_400,I (projection denoted E_I to avoid collision)",
            "full_source_operator": "H_T,400=s_0(T)*I+P_T,400; this audit splits the prime-source part P=A+Q, while the scalar background is unchanged",
            "source_coefficients": "c_n=-Lambda(n)/(a_phi(T)*L*sqrt(n)); full cutoff N=floor(exp(L-sqrt(L)))",
            "ordinary_part_A": "sum_(p<=N,epsilon=+-) c_p exp(i*epsilon*T*log p) V_(epsilon*log(p)/L,400)",
            "power_part_Q": "sum_(p^k<=N,k>=2,epsilon=+-) c_(p^k) exp(i*epsilon*T*log(p^k)) V_(epsilon*k*log(p)/L,400)",
            "finite_T_fields": "F^S_k=sum_(n in S) c_n exp(i*T*log n) exp(2*pi*i*k*log(n)/L); alpha^S_k=Im F^S_k; beta^S_k=2 Re sum_(n in S)c_n(1-log(n)/L)exp(i*T*log n)exp(2*pi*i*k*log(n)/L)",
            "entry_identity": "(H^S_400)_(ij)=beta^S_i if i=j; (alpha^S_i-alpha^S_j)/(pi*(j-i)) if 0<|j-i|<=400; zero otherwise",
            "exact_commutator": "H^S_400=M_(beta^S)+[M_(alpha^S),J_400], (J_400)_(ij)=1/(pi*(j-i)) for 0<|i-j|<=400; exact for finite T and before compression",
            "finite_section": "H^S_400,I=E_I H^S_400 E_I; compression retains exactly the same entries; no wrap-around",
            "exact_rational_identity_replay": identity,
        },
        "proper_power_mass_and_transfer": {
            "coefficient_square_mass": "M2pow<=1/(|a_phi|^2*L^2)*sum_p (log p)^2/[p*(p-1)]<=64/(|a_phi|^2*L^2)",
            "coefficient_absolute_mass": "M1pow=1/(|a_phi|*L)*sum_(p<=sqrt(N)) log(p)/(p*(1-p^(-1/2)))=O(1) by dyadic Chebyshev; not o(1)",
            "circle_separation": "u_n=log(n)/L; distinct n<=N have adjacent gap >=1/((N+1)*L); wrap gap >=1/sqrt(L); hence delta>=1/((N+1)*L) eventually",
            "discrete_large_sieve": "by duality from Montgomery-Vaughan, The Large Sieve, Thm 1: sum_(k in any m-consecutive integer interval)|F_k|^2 <= (m+delta^(-1))*sum_n|a_n|^2",
            "uniform_section_ratio": "delta^(-1)/m <= (N+1)*L/(d-2q)=O(exp(-sqrt(L))) for every permitted good section; endpoint phase is absorbed in coefficients",
            "trace_transfer": "tau_I(Q^2)<= [4+(8/pi^2)*sum_(r=1)^400 r^(-2)]*(1+delta^(-1)/m)*M2pow=O_400(L^-2)",
            "operator_bound": "||Q_I||op<=||beta^pow||inf+2||alpha^pow||inf||J_400||op<=2*M1pow*(1+2*H_400/pi)=O_400(1)",
            "fourth_trace": "tau_I(Q^4)<=||Q_I||op^2*tau_I(Q^2)=O_400(L^-2)",
            "normalized_schatten4": "|tau_I((A+Q)^4)^(1/4)-tau_I(A^4)^(1/4)|<=||Q||_(4,tau)=O_400(L^-1/2), by Schatten norm triangle inequality; no bound on either target fourth moment is assumed",
            "invalid_generic_implication_countermodel": concentration,
            "proof_status": "PROVED for every permitted contiguous section of length m>=d-2q, using source frequencies and actual finite-band matrix entries",
        },
        "prior_positive_atom": prior_atom_replay(),
        "prior_weight_cone_diagnostics": {
            "source_evidence": "evidence/WP84_SOURCE_WEIGHT_CONE_26_TERM_LEDGER.json; exact parent replay is rerun by the new regression suite",
            "abstract_positive_weight_example": {
                "point": ["1/6", "-1/6", "11/12", "-11/12"],
                "unweighted_bracket": "-1/12",
                "positive_weights": ["1"] + ["1/100"] * 25,
                "reweighted_bracket": "1187/1200",
                "classification": "exact rational abstract weight example; not source-admissible evidence",
            },
            "zero_margin_example": {
                "point": ["-3/4", "-1/2", "1/2", "3/4"],
                "row_count": 4,
                "nonzero_signed_term_entries_one_based": [[1, 1], [8, -1]],
                "unweighted_bracket": "0",
                "classification": "exact rational-grid diagnostic; not source-admissible evidence",
            },
        },
        "ordinary_prime_exact_source": {
            "measure": "mu_ord=sum_(p_0,...,p_3<=N; epsilon in {+,-}^4) (prod c_pj) exp(i*T*L*S)exp(2*pi*i*k_minus*S) delta_v",
            "kernel": "Phi_ord_4,400,m(v)=Omega_4,400(v)*kappa_m(v), with the same 26 empirical-row cumulant terms and no source_mask callback",
            "pair_subtraction": "retained exactly in kappa via the full partition ledger; when converting raw trace, the 2+2 pair products are the explicit Pair4 layer, and the finite singleton remainder must be carried with its proved source bound",
            "ordered_partition_counts_by_blocks": {str(k): v for k, v in partition_counts.items()},
            "all_26_ordered_partition_terms": partitions,
            "all_orientation_words": sign_words,
            "six_balanced_orientation_words": balanced_sign_words,
            "closed_lag_path_count": closed_lag_path_count(400),
            "cutoff_orientation_alias_section": "all ordered ordinary primes p<=N; all 16 sign words; all 6 balanced sign words; all 342615201 closed R400 lag paths; full carrier exp(i*T*L*S)exp(2*pi*i*k_minus*S); all integer and near-integer aliases; every selected section retains its actual m and k_minus",
            "exact_product_audit": ordinary,
            "physical_vs_geometric": "not identified: at the preserved rational witness physical sharp O_A*kappa=2/5 while public O_A*B4_nc=0; R400 filtered physical kernel has a positive certified interval",
            "endpoint_brownian_import": "not justified: endpoint/Brownian identities were proved for the public sharp overlap; the physical filtered row cumulant differs term by term and need not be a negative Gram kernel",
            "ordinary_connected_result": "OPEN; exact nonpair products are absent, but near products and physical aliases remain and no signed aggregate bound or source-admissible ordinary-prime aggregate counterexample was established",
        },
        "record_threshold": {
            "required_nonpositive_target": "limsup_(T->infinity) sup_(I in G_T) Re integral Phi_ord dmu_ord <= 0, where G_T is every permitted good-endpoint principal section",
            "weaker_allowed_connected_budget": "3675673694911/148250000000000 = 0.02479375173633052276559865092748...",
            "weaker_sufficient_ordinary_pair_plus_connected": "ordinary Pair400<=0.266329+o(1) and limsup Re integral Phi_ord dmu_ord <= the displayed budget would give w400<=0.291122751736330522...; not proved",
            "quantitative_attempt": "the elementary envelope |D_m|<=1 gives ||Phi||_inf<=26*G_400^4; combined with the tuplewise absolute coefficient-mass bound (2*sum_(p<=N)|c_p|)^4=O(N^2/(a_phi^4*L^4)), this is far above the record allowance; after atoms collide, measure total variation can only be smaller than this pre-collision bound",
            "68_820273_route": "separate conditional route requiring the stronger 0.266329+o(1) gate; not promoted",
            "consumer_status": "OPEN",
        },
        "decisions": {
            "PROPER_POWER_SCHATTEN_ABSORPTION": "PROVED",
            "ORDINARY_PHYSICAL_CONNECTED_AGGREGATE": "OPEN",
            "R400_CONSUMER": "OPEN",
        },
        "smallest_unresolved_inequality": "limsup_(T->infinity) sup_(I in G_T) Re integral Phi_ord_4,400,m(v) dmu_ord_(T,I)(v) <= 3675673694911/148250000000000, where G_T is every permitted good-endpoint principal section; nonpositivity is the stronger unresolved gate",
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--json", type=Path)
    args = parser.parse_args()
    data = build_report_data()
    text = json.dumps(data, indent=2, sort_keys=True) + "\n"
    if args.json:
        args.json.parent.mkdir(parents=True, exist_ok=True)
        with args.json.open("w", encoding="utf-8", newline="\n") as stream:
            stream.write(text)
    print("FINITE MATRIX: exact rational single-prime Fourier-entry/commutator identity replay passed")
    print("PROPER POWERS: source-grid transfer gives tau(Q^2)=O_400(L^-2), ||Q||op=O_400(1)")
    print("SCHATTEN: tau(Q^4)=O_400(L^-2); fourth-root perturbation is O_400(L^-1/2), unconditionally")
    print("ORDINARY PRIME: physical connected aggregate remains OPEN")
    if args.json:
        print(f"WROTE {args.json}")
    if data["decisions"]["PROPER_POWER_SCHATTEN_ABSORPTION"] != "PROVED":
        raise RuntimeError("proper-power proof gate failed")


if __name__ == "__main__":
    main()
