"""Independent exact replay and hostile mutations for the mask-uniform LP."""
from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT_PATH = ROOT / "notes/WP84_SIGNED_AGGREGATE_MASK_UNIFORM_CERTIFICATE.json"
PATTERNS_PATH = ROOT / "notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv"
FUNCS_PATH = ROOT / "notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json"
AUDIT_INPUTS = [
    "notes/WP84_NEAR_ALIAS_SURVIVOR_LEMMA.md",
    "notes/WP84_SIGNED_NEAR_ALIAS_ATTACK.md",
    "notes/WP84_DIRECT_SIGNED_RESTRICTED_CORRELATION_ATTACK.md",
    "notes/WP84_NEAR_ALIAS_SURVIVOR_ORBIT_COMPRESSION.md",
    "src/wp84_fifth_full_pool_amplitude.py",
]


def fraction(text: str) -> F:
    return F(text)


def fracstr(value: F) -> str:
    return f"{value.numerator}/{value.denominator}"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def independent_sources() -> dict:
    patterns = list(csv.DictReader(PATTERNS_PATH.open(encoding="utf-8", newline="")))
    fs = json.loads(FUNCS_PATH.read_text(encoding="utf-8"))
    pclasses = {(int(x["degree"]), x["sign_word"], x["equality_labels"]) for x in patterns}
    degree_classes = Counter(k[0] for k in pclasses)
    degree_alias_rows = Counter(r["degree"] for r in patterns)
    origins = {}
    expected_func_rows = []
    mass = F(0)
    for f in fs:
        b = int(f["degree"])
        w = -F(11501, 12500) if b == 5 else F(137641, 250000)
        orbit = [tuple([int(o[0]), o[1], o[2]]) for o in f["raw_orbit_members"]]
        for origin in orbit:
            if origin in origins:
                raise AssertionError("overlapping raw orbit provenance")
            origins[origin] = int(f["id"])
        alpha = F(f["exact_alpha"])
        if alpha != w * len(orbit):
            raise AssertionError("functional coefficient is not raw-orbit size times omega_b")
        mass += abs(alpha)
        expected_func_rows.append({
            "functional_id": int(f["id"]),
            "degree": b,
            "sign_word": f["sign_word"],
            "equality_partition": f["equality_partition"],
            "aliases": f["aliases"],
            "raw_origin_count": len(orbit),
            "per_raw_origin_consumer_coefficient": str(w),
            "orbit_collapsed_coefficient_if_mask_is_covariant": fracstr(alpha),
        })
    if set(origins) != pclasses:
        raise AssertionError("raw orbit data do not partition survivor class set")
    if degree_classes != Counter({5: 1132, 6: 7608}):
        raise AssertionError("raw survivor class counts mismatch")
    if degree_alias_rows != Counter({"5": 1956, "6": 19632}):
        raise AssertionError("class-alias pair counts mismatch")
    if len(fs) != 453 or mass != F(163444421, 31250):
        raise AssertionError("functional count or exact coefficient mass mismatch")

    q = [F(-19101, 185500), F(961, 3710), F(31, 50), F(-371, 500)]
    coeffs = []
    for k in range(7):
        coeffs.append(sum((q[j] * q[k-j] for j in range(4) if 0 <= k-j < 4), F(0)))
    a, b = F(11501, 12500), F(137641, 250000)
    eb, ev = F(128952763, 92407500000), F(26060119, 12734908593750)
    js = F(21, 200) - coeffs[0] - coeffs[2] / 3 - eb - ev
    ideal = js + a / 36 - b * F(157, 630)
    relaxed = js + a / 36 - b * F(34, 135)
    return {
        "n_raw": len(pclasses), "n_functionals": len(fs), "n_alias_rows": len(patterns),
        "raw_by_degree": dict(sorted(degree_classes.items())),
        "alias_by_degree": dict(sorted((int(k), v) for k, v in degree_alias_rows.items())),
        "functional_rows": expected_func_rows,
        "mass": fracstr(mass), "q": [fracstr(x) for x in q], "q2": [fracstr(x) for x in coeffs],
        "Jstar": fracstr(js), "ideal": fracstr(ideal), "relaxed": fracstr(relaxed),
        "h400": fracstr(relaxed / 201),
        "input_hashes": {
            "notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv": sha(PATTERNS_PATH),
            "notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json": sha(FUNCS_PATH),
        },
        "audit_input_hashes": {rel: sha(ROOT / rel) for rel in AUDIT_INPUTS},
    }


def validate(cert: dict, expected: dict) -> None:
    assert cert["decision"].startswith("C.")
    assert cert["frozen_starting_state"]["branch"] == "codex/c5-c6-attack-20261006"
    assert cert["frozen_starting_state"]["head"] == "9401b38a8d2b8be8fc9f9597988dd93c1d6c86c1"
    assert cert["frozen_starting_state"]["parent"] == "4f0375b2ebc7a263ca3a59133e46d3449bf89989"
    assert cert["pinned_mathematical_source_inputs"] == expected["audit_input_hashes"]
    assert cert["source_inputs"]["survivor_patterns_csv"]["sha256"] == expected["input_hashes"]["notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv"]
    assert cert["source_inputs"]["canonical_functionals_json"]["sha256"] == expected["input_hashes"]["notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json"]
    counts = cert["survivor_counts"]
    assert counts["raw_sign_equality_class_total"] == expected["n_raw"]
    assert counts["raw_sign_equality_classes"] == {str(k): v for k, v in expected["raw_by_degree"].items()}
    assert counts["class_alias_pair_total"] == expected["n_alias_rows"]
    assert counts["class_alias_rows"] == {str(k): v for k, v in expected["alias_by_degree"].items()}
    assert counts["reduced_real_functionals"] == expected["n_functionals"]
    consumer = cert["consumer_coefficients"]
    assert consumer["omega5"] == "-11501/12500"
    assert consumer["omega6"] == "137641/250000"
    assert consumer["exact_absolute_mass_after_covariant_orbit_collapse"] == expected["mass"]
    assert consumer["functionals"] == expected["functional_rows"]
    budget = cert["exact_frozen_budget_replay"]
    assert budget["q_polynomial"] == expected["q"]
    assert budget["q_squared_coefficients_c0_to_c6"] == expected["q2"]
    assert budget["Jstar"] == expected["Jstar"]
    assert budget["ideal_allowance"] == expected["ideal"] == "27704610381502/17886179119921875"
    assert budget["relaxed_allowance"] == expected["relaxed"] == "52897896569489/572357731837500000"
    assert budget["relaxed_H400_primitive_scale_if_multiplier_201"] == expected["h400"]
    assert cert["mask_dependence"]["type"].startswith("linear in Boolean")
    assert "optional_known_covariance_constraints" in cert["mask_dependence"]
    assert "literal callback API does not enforce" in cert["mask_dependence"]["optional_known_covariance_constraints"]
    assert cert["mask_dependence"]["callback_key"] == "(fid, slots, lag, T, section, m)"
    assert cert["mask_dependence"]["exact_objective"] == "S_T(chi)=sum_(k in K_T) chi_k * a_k(T,I), chi_k in {0,1}."
    assert cert["mask_dependence"]["exact_extrema"]["sup_S"] == "sum_k max(a_k,0)"
    assert cert["mask_dependence"]["exact_extrema"]["inf_S"] == "sum_k min(a_k,0)"
    assert cert["mask_dependence"]["exact_extrema"]["sup_abs_S"].startswith("max(")
    assert "chi_k=1 iff a_k>0" in cert["mask_dependence"]["exact_extrema"]["maximizer"]
    assert "equivariant" in cert["mask_dependence"]["orbit_compression_condition"]
    flags = cert["full_pool_and_band_flags"]
    assert flags == {
        "ordinary_prime_cutoff": "N(T)=floor(exp(L-sqrt(L)))",
        "complete_prime_pool": True,
        "finite_core_substitution": False,
        "R": 6000,
        "closed_paths": True,
        "exact_carrier_and_equality_partition": True,
        "near_alias_and_long_tail_both_retained": True,
        "diagnostic_rows_used": False,
        "source_selector_invented": False,
    }
    assert cert["analytic_status"]["proved_signed_saving"] == "NONE"
    assert cert["analytic_status"]["relaxed_budget"] == "UNPAID"
    assert cert["analytic_status"]["strict_gt_79"] == "OPEN"
    assert cert["uniform_theorem_needed"].endswith("before other unpaid transfers.")
    assert "Delta_available is at most 52897896569489/572357731837500000" in cert["uniform_theorem_needed"]


def lp_bruteforce_check() -> int:
    checks = 0
    for coeffs in ((F(2), F(-3), F(0)), (F(-5, 7), F(11, 9)), (F(1), F(1), F(-4), F(6))):
        vals = []
        for bits in product((0, 1), repeat=len(coeffs)):
            vals.append(sum((c * x for c, x in zip(coeffs, bits)), F(0)))
            checks += 1
        pos = sum((max(c, F(0)) for c in coeffs), F(0))
        neg = sum((min(c, F(0)) for c in coeffs), F(0))
        assert max(vals) == pos and min(vals) == neg
        assert max(abs(x) for x in vals) == max(pos, -neg)
    return checks


def run() -> dict:
    cert = json.loads(CERT_PATH.read_text(encoding="utf-8"))
    expected = independent_sources()
    validate(cert, expected)
    lp_checks = lp_bruteforce_check()
    mutations = []

    def reject(label: str, mutate) -> None:
        changed = json.loads(json.dumps(cert))
        mutate(changed)
        try:
            validate(changed, expected)
        except (AssertionError, KeyError, TypeError, ValueError):
            mutations.append(label)
            return
        raise AssertionError(f"hostile mutation was accepted: {label}")

    reject("consumer sign reversal", lambda x: x["consumer_coefficients"].update(omega5="11501/12500"))
    reject("omitted survivor family", lambda x: x["survivor_counts"]["raw_sign_equality_classes"].update({"6": 0}))
    reject("dropped natural prime restriction", lambda x: x["full_pool_and_band_flags"].update(ordinary_prime_cutoff="unrestricted integers"))
    reject("changed R", lambda x: x["full_pool_and_band_flags"].update(R=400))
    reject("six-prime core substitution", lambda x: x["full_pool_and_band_flags"].update(complete_prime_pool=False, finite_core_substitution=True))
    reject("deleted alias sector", lambda x: x["consumer_coefficients"]["functionals"][0].update(aliases=[]))
    reject("changed sixth consumer coefficient", lambda x: x["consumer_coefficients"].update(omega6="-137641/250000"))
    reject("illegal atomwise absolute-value replacement", lambda x: x["mask_dependence"].update(exact_objective="sum_k chi_k*abs(a_k)"))
    reject("fake carrier/equality gate", lambda x: x["full_pool_and_band_flags"].update(exact_carrier_and_equality_partition=False))
    reject("omitted long tail", lambda x: x["full_pool_and_band_flags"].update(near_alias_and_long_tail_both_retained=False))
    reject("diagnostic rows substituted", lambda x: x["full_pool_and_band_flags"].update(diagnostic_rows_used=True))
    reject("invented source selector", lambda x: x["full_pool_and_band_flags"].update(source_selector_invented=True))
    reject("perturbed exact coefficient/matrix functional", lambda x: x["consumer_coefficients"]["functionals"][0].update(orbit_collapsed_coefficient_if_mask_is_covariant="1/3"))
    reject("positive-part theorem budget perturbed", lambda x: x.update(uniform_theorem_needed=x["uniform_theorem_needed"].replace("52897896569489/572357731837500000", "1/100")))
    if len(mutations) != 14:
        raise AssertionError("hostile mutation count changed")
    return {
        "independent_source_reconstruction": "PASS",
        "exact_budget_replay": "PASS",
        "boolean_lp_bruteforce_assignments": lp_checks,
        "hostile_mutations_rejected": mutations,
        "mutation_count": len(mutations),
        "mask_uniform_bound_value": "not evaluated; reduced exactly to positive-part sum",
        "proved_saving": "NONE",
        "strict_gt_79": "OPEN",
    }


if __name__ == "__main__":
    print(json.dumps(run(), indent=2, sort_keys=True))
