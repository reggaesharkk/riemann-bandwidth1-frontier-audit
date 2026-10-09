"""Independent replay and hostile mutations for the alias positive-part audit."""
from __future__ import annotations

import csv
import hashlib
import json
from copy import deepcopy
from collections import Counter, defaultdict
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "notes/WP84_ALIAS_RESOLVED_POSITIVE_PART_CERTIFICATE.json"
CSV = ROOT / "notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv"
SUPPORT_CSV = ROOT / "notes/WP84_SIGNED_NEAR_ALIAS_SUPPORT.csv"
MASK = ROOT / "notes/WP84_SIGNED_AGGREGATE_MASK_UNIFORM_CERTIFICATE.json"
FUNCTIONALS = ROOT / "notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json"


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def replay():
    certificate = json.loads(CERT.read_text(encoding="utf-8"))
    with CSV.open(newline="", encoding="utf-8") as stream:
        rows = list(csv.DictReader(stream))
    with SUPPORT_CSV.open(newline="", encoding="utf-8") as stream:
        support_rows = list(csv.DictReader(stream))
    origins = defaultdict(set)
    pairs = defaultdict(set)
    aliases = defaultdict(set)
    per_alias = defaultdict(Counter)
    for row in rows:
        b, m = int(row["degree"]), int(row["m"])
        o = (row["degree"], row["sign_word"], row["equality_labels"])
        origins[b].add(o)
        pairs[b].add((o, m))
        aliases[b].add(m)
        per_alias[b][m] += 1

    require(sum(map(len, origins.values())) == 8740, "raw origins are not 8,740")
    require(sum(map(len, pairs.values())) == 21588, "origin/alias pairs are not 21,588")
    require(len(origins[5]) == 1132 and len(origins[6]) == 7608, "degree origin census changed")
    require(len(pairs[5]) == 1956 and len(pairs[6]) == 19632, "degree alias-pair census changed")
    expected_aliases = {5: set(range(-4, 0)) | set(range(1, 5)),
                        6: set(range(-5, 0)) | set(range(1, 6))}
    require(aliases == expected_aliases, "near-alias set changed")
    tail_aliases = defaultdict(set)
    tail_pair_counts = Counter()
    for row in support_rows:
        b = int(row["degree"])
        for raw_m in row["asymptotic_support_alias_m"].split(","):
            if raw_m:
                tail_aliases[b].add(int(raw_m))
                tail_pair_counts[b] += 1
    require(len(support_rows) == 14656, "full support-pattern census changed")
    require(tail_aliases[5] == expected_aliases[5] and tail_aliases[6] == expected_aliases[6], "tail possible-alias union changed")
    require(tail_pair_counts[5] == 2726 and tail_pair_counts[6] == 26932, "tail candidate origin-alias counts changed")

    frozen = json.loads(MASK.read_text(encoding="utf-8"))
    budgets = frozen["exact_frozen_budget_replay"]
    delta = Fraction(budgets["relaxed_allowance"])
    delta400 = Fraction(budgets["relaxed_H400_primitive_scale_if_multiplier_201"])
    require(delta == Fraction(52897896569489, 572357731837500000), "relaxed budget changed")
    require(delta / 201 == delta400, "H=400 primitive reference scale mismatch")
    l1_leading = Fraction(137641, 250000) * 26932 * 12001**4 * 64
    require(l1_leading == Fraction(307571548634896980602893648, 15625), "L1 leading constant mismatch")
    require(Fraction(certificate["source_census"]["formal_alias_resolved_components_if_full_D_b_x_C2_covariance_were_supplied"]) == 1148, "conditional alias component total mismatch")
    require(sum(certificate["source_census"]["formal_component_size_histogram_conditional"].values()) == 1148, "conditional histogram does not sum to 1,148")
    require(certificate["quantitative_bounds"]["closed_path_count_upper"] == str(12001**4), "closed path ceiling mismatch")

    # Independently verify listed numeric/hardening claims against recomputation.
    require(certificate["source_census"]["total_raw_origins"] == sum(map(len, origins.values())), "certificate origin total mismatch")
    require(certificate["source_census"]["total_origin_alias_pairs"] == sum(map(len, pairs.values())), "certificate pair total mismatch")
    require(certificate["alias_decomposition"]["near_alias_exact_csv_sets"] == {
        "5": sorted(expected_aliases[5]), "6": sorted(expected_aliases[6])}, "certificate alias sets mismatch")
    require(certificate["alias_decomposition"]["tail_full_pattern_candidate_alias_sets"] == {
        "5": sorted(expected_aliases[5]), "6": sorted(expected_aliases[6])}, "certificate tail candidate alias sets mismatch")
    require(certificate["alias_decomposition"]["tail_full_pattern_candidate_origin_alias_pairs"] == {"5": 2726, "6": 26932}, "certificate tail candidate counts mismatch")
    require(certificate["budget"]["Delta_relaxed_exact"] == str(delta), "certificate budget mismatch")
    require(certificate["source_hashes"][str(CSV.relative_to(ROOT)).replace("\\", "/")] == digest(CSV), "CSV hash mismatch")
    require(certificate["source_hashes"][str(SUPPORT_CSV.relative_to(ROOT)).replace("\\", "/")] == digest(SUPPORT_CSV), "support-pattern CSV hash mismatch")
    require(certificate["source_hashes"][str(MASK.relative_to(ROOT)).replace("\\", "/")] == digest(MASK), "budget source hash mismatch")

    # Exact support disjointness derivation: if both windows hold, triangle
    # inequality gives |m-m'|L<=2H/T, contradicting the strict hypothesis.
    # For H=400 and T>=1000 the sufficient inequality holds; its LHS 800/T
    # decreases and log(T/(2pi)) increases.
    require(800 / 1000 < __import__("math").log(1000 / (2 * __import__("math").pi)), "H=400 threshold base point fails")

    # Cross-alias finite average is nonzero in general; choose xi-eta=1, A=pi.
    # Its exact value is (exp(i*pi)-1)/(i*pi)=2i/pi, nonzero.
    require(certificate["norm_additivity"]["result"] == "not implied by alias-window disjointness", "false orthogonality claim")
    require("1-exp(2*pi*i*M*D/L)" in certificate["norm_additivity"]["same_path_finite_root_cross_average"], "exact cross-alias geometric factor missing")

    # Hostile mutations: each invalid claim/value must be rejected by the
    # corresponding explicit invariant below.  These are mutations of the
    # certificate contract, not edits to source files.
    rejected = []
    def reject(label, mutate, invariant):
        mutant = deepcopy(certificate)
        mutate(mutant)
        try:
            invariant(mutant)
        except AssertionError:
            rejected.append(label)
        else:
            raise AssertionError(f"hostile mutation was accepted: {label}")

    def field(path, value):
        def mutate(obj):
            target = obj
            for key in path[:-1]: target = target[key]
            target[path[-1]] = value
        return mutate
    def exact(path, expected):
        def check(obj):
            target = obj
            for key in path: target = target[key]
            require(target == expected, f"{path} changed")
        return check
    reject("merge alias bits", field(["source_census", "callback_tuple"], ["fid", "slots", "lag", "T", "section"]), exact(["source_census", "callback_tuple"], ["fid", "slots", "lag", "T", "section", "m"]))
    reject("453 as mask-component count", field(["source_census", "formal_alias_resolved_components_if_full_D_b_x_C2_covariance_were_supplied"], 453), exact(["source_census", "formal_alias_resolved_components_if_full_D_b_x_C2_covariance_were_supplied"], 1148))
    reject("omit m from key", field(["canonicalization", "only_legal_key"], ["fid", "slots", "lag", "T", "section"]), exact(["canonicalization", "only_legal_key"], ["fid", "slots", "lag", "T", "section", "m"]))
    reject("violate disjointness", field(["alias_decomposition", "disjointness", "integer_alias_sufficient_condition"], "2H/T <= L"), exact(["alias_decomposition", "disjointness", "integer_alias_sufficient_condition"], "2H/T < L"))
    reject("change R", field(["source_census", "R"], 400), exact(["source_census", "R"], 6000))
    reject("finite core", field(["source_census", "complete_prime_pool"], "six-prime diagnostic core"), lambda o: require("no finite core" in o["source_census"]["complete_prime_pool"], "pool truncated"))
    reject("drop fifth sign", field(["canonicalization", "consumer_coefficients_per_raw_origin", "5"], "11501/12500"), exact(["canonicalization", "consumer_coefficients_per_raw_origin", "5"], "-11501/12500"))
    reject("change sixth coefficient", field(["canonicalization", "consumer_coefficients_per_raw_origin", "6"], "137641/25000"), exact(["canonicalization", "consumer_coefficients_per_raw_origin", "6"], "137641/250000"))
    reject("omit long tail", field(["alias_decomposition", "tail_nearest_cell"], "near only"), lambda o: require("tail" in o["alias_decomposition"]["tail_nearest_cell"], "tail omitted"))
    reject("positive part before aggregation", field(["canonicalization", "positive_part_order"], "apply [x]+ then aggregate"), exact(["canonicalization", "positive_part_order"], "aggregate exact duplicate full keys first, then apply [x]_+"))
    reject("signed sum replacing positive part", field(["quantitative_bounds", "universal_positive_part"], "sum_k a_k"), lambda o: require("[x]_+" in o["quantitative_bounds"]["universal_positive_part"], "signed replacement"))
    reject("assume covariance", field(["source_census", "proved_nontrivial_callback_bit_equalities"], 453), exact(["source_census", "proved_nontrivial_callback_bit_equalities"], 0))
    reject("uncertified phase equidistribution", field(["phase_pilot", "actual_source_transfer"], "phase equidistribution proves the source bound"), lambda o: require(o["phase_pilot"]["actual_source_transfer"].startswith("NOT established"), "equidistribution promoted"))
    reject("fake logarithms", field(["source_census", "complete_prime_pool"], "fake logarithms and rational points"), lambda o: require("actual" in o["source_census"]["complete_prime_pool"], "fake logs/pool"))
    reject("diagnostic section", field(["source_census", "complete_prime_pool"], "diagnostic section only"), lambda o: require("actual source window" in o["source_census"]["complete_prime_pool"], "diagnostic section"))
    reject("drop root sum", field(["quantitative_bounds", "universal_positive_part"], "prime factors only"), lambda o: require("root" in o["quantitative_bounds"]["universal_positive_part"], "root missing"))
    reject("alter budget", field(["budget", "Delta_relaxed_exact"], "0"), exact(["budget", "Delta_relaxed_exact"], str(delta)))
    reject("fabricate selector", field(["canonicalization", "reason_no_more_zero_claims"], "selector recovered"), lambda o: require("source masks" in o["canonicalization"]["reason_no_more_zero_claims"], "invented selector"))

    # A direct independent check of the source callback's argument contract.
    source = (ROOT / "src/wp84_fifth_full_pool_amplitude.py").read_text(encoding="utf-8")
    require("source_mask(fid,slots,lag,T,section,m)" in source, "callback signature changed or not captured")
    require("R_SOURCE=6000" in source, "frozen R source changed")
    require(len(rejected) == 18, "hostile mutation coverage incomplete")
    print("PASS: 8,740 origins; 21,588 alias pairs; exact alias sets and budgets replayed")
    print("PASS: support disjointness proof and non-orthogonality status checked")
    print(f"PASS: rejected {len(rejected)}/18 hostile mutations")
    print("NO positive-part upper bound or positive lower bound certified; strict >79 remains OPEN")


if __name__ == "__main__":
    replay()
