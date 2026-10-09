#!/usr/bin/env python3
"""Independent verifier for WP84_SOURCE_MATCHED_SIGNED_RESIDUAL_CERTIFICATE.

Does not import the certificate producer.  Python standard library only.
"""
from __future__ import annotations

import copy
import hashlib
import json
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "notes" / "WP84_SOURCE_MATCHED_SIGNED_RESIDUAL_CERTIFICATE.json"
R = 6000
SOURCES = [
    "notes/WP84_STRICT79_SOURCE_MATCHED_ARITHMETIC_REDUCTION.md",
    "notes/WP84_STRICT79_HOSTILE_AUDIT_AND_BALANCED_PAIR_REDUCTION.md",
    "notes/WP84_JOINT_THIRD_FIFTH_SIXTH_ARITHMETIC_OBSTRUCTION.md",
    "notes/WP84_THIRD_AWARE_SAME_SECTION_THEOREM_OR_OBSTRUCTION.md",
    "notes/WP84_STRICT79_SIGNED_ARITHMETIC_THEOREM_OR_OBSTRUCTION.md",
    "notes/WP84_STRICT79_SIGNED_LEDGER_CERTIFICATE.json",
]


def sha(path: Path) -> str:
    z = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(65536), b""):
            z.update(block)
    return z.hexdigest()


def fail_if(condition: bool, message: str) -> None:
    if condition:
        raise ValueError(message)


def rebuild_census(degree: int) -> dict:
    rows = []
    pos_total = neg_total = zero_total = 0
    for gap in range(degree - 1):
        placements = degree - gap - 1
        bound = min(gap, degree - gap - 2) * R
        row = {
            "intervening_increment_count": gap,
            "slot_pair_placements": placements,
            "max_abs_relative_prefix_difference": bound,
            "d_values": [-bound, bound],
            "positive_d_zero_count": 1,
            "negative_d_nonzero_count": 2 * bound,
            "zero_coefficient_count": 0,
            "coefficient": "1/6 if d=0; -1/(2*pi^2*d^2) if d!=0",
            "multiplicity_scope": "(slot-pair placement,d) parameter tuples only; not full closed paths",
        }
        rows.append(row)
        pos_total += placements
        neg_total += placements * 2 * bound
    return {
        "scope": "ell_a=ell_b=0 subfamily, all feasible integer d, R=6000",
        "formula": "k_ab=2*integral_0^1 s*(1-s)^2*cos(2*pi*d*s) ds = 1/6 (d=0), -1/(2*pi^2*d^2) (d!=0)",
        "placements": rows,
        "weighted_parameter_tuple_sign_counts": {"positive": pos_total, "negative": neg_total, "zero": 0},
        "full_R6000_path_sign_census": "not computed or claimed; general k_ab depends on (ell_a,ell_b,q_(a-1)-q_(b-1))",
        "exact_symmetries": ["k(a,b,q)=k(b,a,-q)", "k(-a,-b,-q)=k(a,b,q)"],
        "general_exact_formula": "k(a,b,q)=2*Re integral_0^1 s*f_a^+(s)*f_b^-(s)*exp(2*pi*i*q*s) ds",
        "finite_closed_form": "Expand f_a^+*f_b^-*exp(2*pi*i*q*s)=sum_n P_n(s)exp(2*pi*i*n*s), deg(P_n)<=2, with n in {q,q+a,q-b,q+a-b} after omitting duplicate/zero-frequency terms. Then k=2*Re sum_n sum_j P_(n,j)*J_(j+1)(n), where J_0(0)=1, J_j(0)=1/(j+1), J_0(n)=0 for n!=0, and J_j(n)=1/(2*pi*i*n)-j*J_(j-1)(n)/(2*pi*i*n) for n!=0. Coefficients of f are exact rational multiples of (pi*i)^-1; thus this is a finite exact rational/pi expression for every feasible (a,b,q), including zero-lag polynomial factors.",
    }


def cadd(x, y):
    return x[0] + y[0], x[1] + y[1]


def cmul(x, y):
    return x[0] * y[0] - x[1] * y[1], x[0] * y[1] + x[1] * y[0]


def cscale(a, x):
    return a * x[0], a * x[1]


def formal_add(dst, power, z):
    dst[power] = cadd(dst.get(power, (Fraction(0), Fraction(0))), z)


def formal_mul(x, y):
    out = {}
    for px, zx in x.items():
        for py, zy in y.items():
            formal_add(out, px + py, cmul(zx, zy))
    return out


def fourier_factor(lag: int, plus: bool):
    # Terms are (integer frequency, s-degree, inverse-pi exponent, Gaussian-rational coefficient).
    if lag == 0:
        return [(0, 0, 0, (Fraction(1), Fraction(0))),
                (0, 1, 0, (Fraction(-1), Fraction(0)))]
    if plus:
        return [(0, 0, 1, (Fraction(0), Fraction(-1, 2 * lag))),
                (lag, 0, 1, (Fraction(0), Fraction(1, 2 * lag)))]
    return [(0, 0, 1, (Fraction(0), Fraction(1, 2 * lag))),
            (-lag, 0, 1, (Fraction(0), Fraction(-1, 2 * lag)))]


def fourier_product(a: int, b: int, q: int):
    # Map (frequency, degree) -> Laurent polynomial in pi^{-1} with Q(i) coefficients.
    out = {}
    for na, ja, ka, za in fourier_factor(a, True):
        for nb, jb, kb, zb in fourier_factor(b, False):
            key = (q + na + nb, ja + jb)
            poly = out.setdefault(key, {})
            formal_add(poly, ka + kb, cmul(za, zb))
    return out


def exponential_moment(degree: int, frequency: int):
    if frequency == 0:
        return {0: (Fraction(1, degree + 1), Fraction(0))}
    prev = {}
    inv_a = {1: (Fraction(0), Fraction(-1, 2 * frequency))}  # (2*pi*i*n)^-1
    for j in range(1, degree + 1):
        nxt = dict(inv_a)
        if prev:
            correction = formal_mul(inv_a, prev)
            for power, z in correction.items():
                formal_add(nxt, power, cscale(Fraction(-j), z))
        prev = nxt
    return prev


def exact_k_formal(a: int, b: int, q: int):
    """Return exact coefficients C_j in k=sum_j C_j*pi^-j."""
    total = {}
    for (freq, degree), coeffs in fourier_product(a, b, q).items():
        moment = exponential_moment(degree + 1, freq)  # the extra s in k
        for cp, zc in coeffs.items():
            for jp, zj in moment.items():
                z = cmul(zc, zj)
                formal_add(total, cp + jp, (2 * z[0], Fraction(0)))
    return {power: real for power, (real, imag) in total.items() if real and not imag}


def validate(c: dict) -> None:
    fail_if(c.get("start_head") != "78b056687dfaacf5493334125eaa3120811c1969", "start HEAD altered")
    fail_if(c.get("branch") != "codex/c5-c6-attack-20261006", "branch altered")
    p = c["parameters"]
    for key, expected in {
        "X": "T/(2*pi)", "L": "log X", "N": "floor(exp(L-sqrt(L)))",
        "R": R, "h": "2*pi/L", "d": "floor(T*L/(2*pi))",
        "section": "I0={0,...,d-1}",
        "section_selection": "canonical full section; no historical selector or synthetic row tuple",
        "prime_coefficient": "c_m=-Lambda(m)/(a_phi(T)*L*sqrt(m)); a_phi(T)->1",
    }.items():
        fail_if(p.get(key) != expected, f"parameter {key} changed")
    obj = c["exact_reduced_residual"]
    fail_if(obj.get("A") != "11501/12500", "A changed")
    fail_if(obj.get("B") != "137641/250000", "B changed")
    for key in ("D5", "Q3", "D6", "Q4"):
        fail_if(not isinstance(obj.get(key), str) or not obj[key], f"sector {key} omitted")
    fail_if(obj.get("pair_kernel") != "phi_ab(s)=2*Re[f_(ell_a)^+(s) f_(ell_b)^-(s) exp(2*pi*i*(q_(a-1)-q_(b-1))*s)]; k_ab=integral_0^1 s*phi_ab(s) ds", "pair coefficient changed")
    fail_if(obj.get("F_T") != "-A*(D5+Q3)+B*(D6+Q4)", "joint residual changed")
    fail_if(obj.get("split") != {"F_pair": "-A*Q3+B*Q4", "F_distinct": "-A*D5+B*D6", "identity": "F_T=F_pair+F_distinct exactly"}, "pair/distinct split changed")
    kernel = p.get("kernel", "")
    fail_if("exp(i*(T+h*i_min)*lambda)" not in kernel or "sum_{r=0}^{rho-1} exp(i*h*r*lambda)" not in kernel, "root/carrier phase removed or kernel replaced")
    fail_if("sharp" in kernel.lower(), "sharp-overlap substitution")
    fail_if("no near-alias masking before factorization" not in obj.get("evidence_scope", ""), "aliases split before global factorization")
    fail_if("full prime pool" not in c["title"] and p.get("N") != "floor(exp(L-sqrt(L)))", "natural full cutoff absent")
    fail_if("full_R6000_path_sign_census" not in c["k_ab_census"]["degree5"], "global sign scope disclaimer absent")
    fail_if(c["k_ab_census"]["degree5"] != rebuild_census(5), "degree-five pair census mutated")
    fail_if(c["k_ab_census"]["degree6"] != rebuild_census(6), "degree-six pair census mutated")
    closed_form = c["k_ab_census"]["degree5"].get("finite_closed_form", "")
    fail_if("J_(j+1)(n)" not in closed_form or "rational/pi" not in closed_form, "finite pair evaluation formula missing")
    ops = c["operator_identities"]
    fail_if("not established" not in ops.get("complete_F_T_finite_R_trace_identity", ""), "unsupported complete operator identity")
    fail_if("no Gaussian law" not in ops.get("Y_law", ""), "Gaussian law for Y assumed")
    fail_if("only certified prime-square" not in ops.get("Y_law", ""), "W covariance promoted to law for Y")
    fail_if("gives no sign" not in ops.get("existing_conditional_cubic_identity", ""), "cubic sign overclaimed")
    fail_if("no correction is omitted" not in obj.get("collision_corrections", ""), "collision corrections omitted")
    fail_if(c["falsifiers"].get("453_use") != "not used as mask components, arithmetic compression, or an estimate", "453 disclaimer altered")
    fail_if(c["falsifiers"].get("counterexample_scope") != "algebraic sign shortcuts falsified; no source-compatible arithmetic counterexample to the target is claimed", "toy matrix promoted to source arithmetic")
    budget = c["signed_budget"]
    fail_if(budget.get("Pair6_6000_lower_bound") != "31498340500050746323/150466924118016000000", "Pair6 altered")
    fail_if(budget.get("required_negative_saving_g9") != "43770221409581023769108432686241/21264421581420459982848000000000000", "g9 altered")
    fail_if(budget.get("proved_negative_saving") != "0" or budget.get("saving_over_g9") != "0", "unsupported signed saving")
    fail_if(budget.get("o1_is_sufficient") is not False, "o(1) incorrectly declared sufficient")
    fail_if(budget.get("strict_gt79") != "OPEN", "strict >79 status altered")
    fail_if(c.get("decision") != "E", "decision altered")
    fail_if(len(c.get("hostile_mutations_required", [])) != 20, "hostile suite incomplete")
    for rel in SOURCES:
        fail_if(c.get("source_sha256", {}).get(rel, {}).get("sha256") != sha(ROOT / rel), f"source hash mismatch: {rel}")


def hostile_mutations(c: dict) -> list[tuple[str, callable]]:
    return [
        ("change_A", lambda x: x["exact_reduced_residual"].update(A="1")),
        ("change_B", lambda x: x["exact_reduced_residual"].update(B="1")),
        ("change_R", lambda x: x["parameters"].update(R=400)),
        ("omit_D_all_distinct", lambda x: x["exact_reduced_residual"].update(D5="")),
        ("omit_Q_balanced_pair", lambda x: x["exact_reduced_residual"].update(Q4="")),
        ("change_Pair6", lambda x: x["signed_budget"].update(Pair6_6000_lower_bound="0")),
        ("drop_root_phases", lambda x: x["parameters"].update(kernel="sharp overlap")),
        ("sharp_overlap_kernel", lambda x: x["exact_reduced_residual"].update(pair_kernel="sharp overlap")),
        ("split_aliases_early", lambda x: x["exact_reduced_residual"].update(evidence_scope="alias-split first")),
        ("finite_prime_core", lambda x: x["parameters"].update(N="six-prime diagnostic core")),
        ("Gaussian_law_for_Y", lambda x: x["operator_identities"].update(Y_law="Y is Gaussian")),
        ("promote_W_covariance_to_Y_law", lambda x: x["operator_identities"].update(Y_law="W covariance proves law of Y")),
        ("claim_D_ge_I_over_6_cubic_sign", lambda x: x["operator_identities"].update(existing_conditional_cubic_identity="D>=I/6 proves positive cubic")),
        ("omit_collision_corrections", lambda x: x["exact_reduced_residual"].update(collision_corrections="none")),
        ("fake_section_selector", lambda x: x["parameters"].update(section_selection="synthetic selected determinant rows")),
        ("453_as_arithmetic_bound", lambda x: x["falsifiers"].update({"453_use": "453 components bound arithmetic"})),
        ("claim_o1_suffices", lambda x: x["signed_budget"].update(o1_is_sufficient=True)),
        ("alter_g9", lambda x: x["signed_budget"].update(required_negative_saving_g9="0")),
        ("promote_toy_matrix_to_source_arithmetic", lambda x: x["falsifiers"].update(counterexample_scope="toy matrix proves source inequality false")),
        ("claim_strict_gt79_without_full_replay", lambda x: x["signed_budget"].update(strict_gt79="PROVED")),
    ]


def main() -> None:
    c = json.loads(CERT.read_text(encoding="utf-8"))
    validate(c)
    assert Fraction(c["signed_budget"]["proved_negative_saving"]) == 0
    assert Fraction(c["signed_budget"]["saving_over_g9"]) == 0
    assert Fraction(c["signed_budget"]["required_negative_saving_g9"]) > 0
    assert c["k_ab_census"]["degree5"]["weighted_parameter_tuple_sign_counts"] == {"positive": 10, "negative": 60000, "zero": 0}
    assert c["k_ab_census"]["degree6"]["weighted_parameter_tuple_sign_counts"] == {"positive": 15, "negative": 144000, "zero": 0}
    assert exact_k_formal(0, 0, 0) == {0: Fraction(1, 6)}
    assert exact_k_formal(0, 0, 1) == {2: Fraction(-1, 2)}
    assert exact_k_formal(0, 0, -1) == {2: Fraction(-1, 2)}
    assert exact_k_formal(0, 0, 2) == {2: Fraction(-1, 8)}
    for a, b, q in ((1, -1, 2), (0, 3, -1), (2, 0, 0)):
        assert exact_k_formal(a, b, q) == exact_k_formal(b, a, -q)
        assert exact_k_formal(a, b, q) == exact_k_formal(-a, -b, -q)
    A = Fraction(11501, 12500)
    B = Fraction(137641, 250000)
    assert B - A < 0 and B + A > 0  # scalar-polynomial sign falsifier
    # Independently recompute the exact path-placement multiplicity identity.
    for b in (5, 6):
        assert sum(row["slot_pair_placements"] for row in rebuild_census(b)["placements"]) == b * (b - 1) // 2
    failed = []
    for label, mutate in hostile_mutations(c):
        changed = copy.deepcopy(c)
        mutate(changed)
        try:
            validate(changed)
        except (ValueError, KeyError, TypeError):
            failed.append(label)
    assert len(failed) == 20, f"hostile mutations rejected {len(failed)}/20: {failed}"
    print("PASS: source hashes, exact residual split, budget, pair-sign census, and 20/20 hostile mutations")
    print("PROVED NEGATIVE SAVING = 0; g9 requirement remains positive; strict >79 OPEN")


if __name__ == "__main__":
    main()
