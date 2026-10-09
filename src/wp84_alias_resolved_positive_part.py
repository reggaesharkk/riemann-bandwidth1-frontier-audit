"""Build an exact, source-pinned audit of the alias-resolved mask support sum.

This is a census and inequality audit, not a numerical evaluation of the
source amplitudes.  In particular it never supplies the missing source_mask.
"""
from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CSV = ROOT / "notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv"
SUPPORT_CSV = ROOT / "notes/WP84_SIGNED_NEAR_ALIAS_SUPPORT.csv"
MASK_CERT = ROOT / "notes/WP84_SIGNED_AGGREGATE_MASK_UNIFORM_CERTIFICATE.json"
FUNCTIONALS = ROOT / "notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json"
OUT = ROOT / "notes/WP84_ALIAS_RESOLVED_POSITIVE_PART_CERTIFICATE.json"
R = 6000
H400 = 400


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load_rows():
    with CSV.open(newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def build():
    rows = load_rows()
    with SUPPORT_CSV.open(newline="", encoding="utf-8") as f:
        support_rows = list(csv.DictReader(f))
    budget_src = json.loads(MASK_CERT.read_text(encoding="utf-8"))
    func_src = json.loads(FUNCTIONALS.read_text(encoding="utf-8"))
    by_degree_alias = defaultdict(Counter)
    origins = defaultdict(set)
    alias_pairs = defaultdict(set)
    for row in rows:
        b, m = int(row["degree"]), int(row["m"])
        origin = (row["degree"], row["sign_word"], row["equality_labels"])
        origins[b].add(origin)
        by_degree_alias[b][m] += 1
        alias_pairs[b].add((origin, m))

    # Frozen reference budget; all remaining consumer debts are unpaid.
    exact = budget_src["exact_frozen_budget_replay"]
    delta = Fraction(exact["relaxed_allowance"])
    delta400 = Fraction(exact["relaxed_H400_primitive_scale_if_multiplier_201"])
    assert delta / 201 == delta400

    # The source patterns give exact candidate aliases near the selected
    # |delta|<=H/T window.  The long-tail support is bounded only by the
    # nearest-cell combinatorial range |m|<=b, not by an occupancy claim.
    near_aliases = {str(b): sorted(by_degree_alias[b]) for b in (5, 6)}
    near_counts = {str(b): {str(m): by_degree_alias[b][m] for m in sorted(by_degree_alias[b])}
                   for b in (5, 6)}
    tail_candidate_aliases = defaultdict(set)
    tail_candidate_pairs = Counter()
    tail_pattern_rows = Counter()
    for row in support_rows:
        b = int(row["degree"])
        aliases = [int(m) for m in row["asymptotic_support_alias_m"].split(",") if m]
        if aliases:
            tail_pattern_rows[b] += 1
            tail_candidate_pairs[b] += len(aliases)
            tail_candidate_aliases[b].update(aliases)

    # One independent Boolean bit per exact (fid,slots,lag,T,section,m) tuple.
    # No function in this repo fixes the callback bit values, so no grouping
    # across distinct tuples is certified here.
    functionals = budget_src["consumer_coefficients"]["functionals"]
    exact_alpha_signs = Counter()
    per_degree_functionals = Counter()
    for f in functionals:
        b = int(f["degree"])
        per_degree_functionals[b] += 1
        c = Fraction(f["per_raw_origin_consumer_coefficient"])
        exact_alpha_signs[f"{b}:{'positive' if c > 0 else 'negative' if c < 0 else 'zero'}"] += 1

    # Any individual full-band root average has modulus at most one:
    # M<=d' and the root is a sum of M unit phases divided by d'.
    # For b displacement coordinates, b-1 entries determine the final one.
    path_upper = {5: (2 * R + 1) ** 4, 6: (2 * R + 1) ** 5}
    cert = {
        "decision": "E",
        "decision_text": "ONE PRECISE ANALYTIC LEMMA REMAINS",
        "starting_head": "96960fb563aac5144045e5bf7be9cdc528bd9f7f",
        "branch": "codex/c5-c6-attack-20261006",
        "source_hashes": {
            str(CSV.relative_to(ROOT)).replace("\\", "/"): sha(CSV),
            str(SUPPORT_CSV.relative_to(ROOT)).replace("\\", "/"): sha(SUPPORT_CSV),
            str(MASK_CERT.relative_to(ROOT)).replace("\\", "/"): sha(MASK_CERT),
            str(FUNCTIONALS.relative_to(ROOT)).replace("\\", "/"): sha(FUNCTIONALS),
        },
        "source_census": {
            "R": R,
            "complete_prime_pool": "ordinary primes p<=N(T)=floor(exp(L-sqrt(L))) subject to the actual source window indicators; no finite core",
            "raw_origin_counts": {str(b): len(origins[b]) for b in (5, 6)},
            "origin_alias_pair_counts": {str(b): len(alias_pairs[b]) for b in (5, 6)},
            "total_raw_origins": sum(map(len, origins.values())),
            "total_origin_alias_pairs": sum(map(len, alias_pairs.values())),
            "historical_unmasked_functionals": 453,
            "formal_alias_resolved_components_if_full_D_b_x_C2_covariance_were_supplied": 1148,
            "formal_component_size_histogram_conditional": {"2": 7, "4": 10, "6": 44, "10": 79, "12": 290, "20": 58, "24": 660},
            "proved_nontrivial_callback_bit_equalities": 0,
            "callback_tuple": ["fid", "slots", "lag", "T", "section", "m"],
        },
        "alias_decomposition": {
            "exact_formula": "K_{T,I}=disjoint_union_m K_{T,I,m}; P=sum_m P_m; P_m=sum_{k in K_{T,I,m}}[a_k(T,I)]_+ after full callback-key aggregation",
            "near_alias_exact_csv_sets": near_aliases,
            "near_alias_origin_alias_pair_counts": {str(b): sum(near_counts[str(b)].values()) for b in (5, 6)},
            "near_alias_pair_count_by_m": near_counts,
            "tail_nearest_cell": "delta=lambda-mL in [-L/2,L/2), m!=0, |delta|>H/T",
            "tail_full_pattern_support_csv_rows": {str(b): tail_pattern_rows[b] for b in (5, 6)},
            "tail_full_pattern_candidate_alias_sets": {str(b): sorted(tail_candidate_aliases[b]) for b in (5, 6)},
            "tail_full_pattern_candidate_origin_alias_pairs": {str(b): tail_candidate_pairs[b] for b in (5, 6)},
            "tail_status": "source support CSV enumerates asymptotic candidate m for the full sign/equality pattern census; it determines possible alias labels, not occupancy after actual prime-window and source-mask gates",
            "near_survivors_are_subset_of_full_pattern_support": True,
            "full_pattern_support_pairs_beyond_near_survivor_csv": {str(b): tail_candidate_pairs[b] - len(alias_pairs[b]) for b in (5, 6)},
            "tail_candidate_status": "candidate-support enumeration only; no actual-prime/window occupancy count is asserted",
            "disjointness": {
                "premises": ["|lambda-mL|<=H/T", "|lambda-m'L|<=H/T"],
                "contradiction_if": "2H/T < |m-m'| L",
                "integer_alias_sufficient_condition": "2H/T < L",
                "fixed_H_eventual": "true since T*log(T/(2*pi)) -> infinity",
                "H_400_sufficient_for_T_ge_1000": "true: 800/1000 < log(1000/(2*pi)); both sides thereafter move in the favorable direction",
                "meaning": "support disjointness in lambda; not callback-bit equality and not norm orthogonality",
            },
        },
        "canonicalization": {
            "only_legal_key": ["fid", "slots", "lag", "T", "section", "m"],
            "positive_part_order": "aggregate exact duplicate full keys first, then apply [x]_+",
            "consumer_coefficients_per_raw_origin": {"5": "-11501/12500", "6": "137641/250000"},
            "functional_coefficient_sign_census": {k: v for k, v in sorted(exact_alpha_signs.items())},
            "identically_zero_full_key_templates_proved": 0,
            "reason_no_more_zero_claims": "root/path/carrier sums and source masks are executable only as a lazy schema; no exact duplicate-key expansion or source_mask implementation is present",
            "pair_simplification": "[x]_+ + [-x]_+=|x| only when the exact same scalar x occurs at two distinct keys; no such key identity is certified; independent bits prohibit cancellation across keys",
            "finite_template_catalogue": "5: omega_5=-11501/12500; 6: omega_6=137641/250000; each raw real atom is Re(omega_b * phase * path/filter/root/prime weight) under its own exact callback key",
        },
        "norm_additivity": {
            "result": "not implied by alias-window disjointness",
            "actual_root_phase": "exp(2*pi*i*k*(m+delta/L))=exp(2*pi*i*k*delta/L) for integer k",
            "cross_term": "2*Re(sum_{m<m'} F_m*conj(F_m'))",
            "same_path_finite_root_cross_average": "for common lag/root interval j0..j0+M-1 and residuals delta_m,delta_m', the normalized root-character cross term is c_m*conj(c_m')*exp(2*pi*i*j0*D/L)*(1-exp(2*pi*i*M*D/L))/(d'*(1-exp(2*pi*i*D/L))), D=delta_m-delta_m'; the integer (m-m') phase is 1; generally nonzero",
            "reason": "integer m factors disappear on section-index roots, while carrier phases exp(i*T*m*L) remain; no orthogonal projection or averaging theorem is supplied",
            "finite_average_counterexample": "for u(t)=exp(i*xi*t), v(t)=exp(i*eta*t), average_[0,A] u*conj(v)= (exp(i*(xi-eta)*A)-1)/(i*(xi-eta)*A), generally nonzero",
        },
        "quantitative_bounds": {
            "universal_positive_part": "0<=P_near+P_tail<=sum_k |a_k|<=sum_over_all_retained_atoms |omega_b|*product_j(log(p_j)/(a_phi(T)*L*sqrt(p_j)))*1_{all source gates}; exact, but unevaluated",
            "filter_bound": "|f_l^epsilon(alpha)|<=1 for 0<=alpha<=1",
            "root_bound": "|K_l(lambda)|<=M/d'<=1",
            "closed_path_count_upper_by_degree": {str(b): str(path_upper[b]) for b in (5, 6)},
            "separable_L1_majorant": "(11501/12500)*2726*12001^4*S1(T)^5+(137641/250000)*26932*12001^5*S1(T)^6, S1=sum_{p<=N}log(p)/(a_phi(T)*L*sqrt(p)); full pool only, all omitted gates enlarged to 1",
            "S1_PNT_asymptotic_under_inherited_a_phi_to_1": "S1(T)~2*exp((L-sqrt(L))/2)/L",
            "L1_ceiling_leading_order": "(3691166155167398664215326669648/15625)*exp(3L-3sqrt(L))/L^6*(1+o(1)); its ratio to Delta_relaxed has leading coefficient 135210719258045304292826345558006523809164800/52897896569489 and diverges; this is an upper bound, not a lower bound for P",
            "atom_level_square_mass": "S2=sum_p log(p)^2/(a_phi(T)^2*L^2*p)~1/2 under inherited a_phi(T)->1; not the coefficient L2 energy after carrier/key aggregation",
            "mean_value_status": "FAIL/REQUIRES LEMMA: section averages are over roots of near-integer aliases; no independent frequency spacing after folding, and mask keys depend on slots, lag, T and section",
            "PNT_status": "marginal prime mass does not bound the signed, window-intersected product correlations or their positive-part support function",
            "best_numeric_upper_bound": None,
            "best_numeric_lower_bound": "0 (tautological); no positive asymptotic lower bound source-certified",
            "near_bound_status": "unbounded by present proofs; exact sum retained",
            "tail_bound_status": "unbounded by present proofs; exact tail retained",
        },
        "phase_pilot": {
            "identity": "(1/(2*pi))*integral_0^(2*pi) [Re(e^(i*theta)B)]_+ dtheta=|B|/pi for fixed B",
            "fixed_frequency_time_average": "for fixed B and fixed nonzero lambda, long interval average of [Re(B*e^(i*lambda*t))]_+ tends |B|/pi",
            "actual_source_transfer": "NOT established: B, prime windows, section/root factor and admissibility vary with T; no single source-legal nonzero carrier has a certified outer-gate inclusion and nonzero limiting amplitude",
            "signed_saving_earned": "none",
        },
        "budget": {
            "Delta_relaxed_exact": str(delta),
            "Delta_relaxed_decimal": f"{float(delta):.16g}",
            "H400_reference_primitive_scale_exact": str(delta400),
            "H400_reference_primitive_scale_decimal": f"{float(delta400):.16g}",
            "ratio_of_reference_scales": "201",
            "H_dependence": {"alias_separation_condition": "2H(T)/T<L(T)", "near_charge(H)": "not bounded", "tail_charge(H)": "not bounded", "available_budget(H)": "only frozen reference value at H=400 supplied"},
            "actual_upper_bound_over_Delta": None,
            "actual_lower_bound_over_Delta": "0",
            "unpaid_status": "no positive-part estimate, near charge, tail charge or transfer payment certified; the reference allowance is not a result for P",
            "H_optimization": "not justified: near(H), tail(H), and available_budget(H) are not bounded functions in the source artifacts",
        },
        "single_remaining_lemma": "For the exact source-defined callback tuple (fid,slots,lag,T,section,m), complete prime pool p<=N(T), all closed R=6000 paths and root sums, prove uniformly over every admissible section and executable Boolean mask that limsup_{T->infty} sum_k [a_k(T,I(T))]_+ <= 52897896569489/572357731837500000, with near and retained long-tail terms both included.",
        "final_status": "E",
        "strict_gt_79": "OPEN",
    }
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    return cert


if __name__ == "__main__":
    c = build()
    print(json.dumps({"decision": c["decision"], "origins": c["source_census"]["total_raw_origins"],
                      "origin_alias_pairs": c["source_census"]["total_origin_alias_pairs"],
                      "near_aliases": c["alias_decomposition"]["near_alias_exact_csv_sets"],
                      "Delta": c["budget"]["Delta_relaxed_exact"]}, indent=2))
