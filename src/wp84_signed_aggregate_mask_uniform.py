"""Exact source-data reconstruction for the signed aggregate mask LP.

The program records the Boolean-mask dependence and exact frozen rational
budget.  It intentionally does not choose a source selector or evaluate the
astronomical prime/path sums.
"""
from __future__ import annotations

import csv
import hashlib
import json
from collections import Counter
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SURVIVORS = ROOT / "notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv"
FUNCTIONALS = ROOT / "notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json"
OUT = ROOT / "notes/WP84_SIGNED_AGGREGATE_MASK_UNIFORM_CERTIFICATE.json"
FROZEN_START_HEAD = "9401b38a8d2b8be8fc9f9597988dd93c1d6c86c1"
FROZEN_BRANCH = "codex/c5-c6-attack-20261006"
AUDIT_INPUTS = [
    "notes/WP84_NEAR_ALIAS_SURVIVOR_LEMMA.md",
    "notes/WP84_SIGNED_NEAR_ALIAS_ATTACK.md",
    "notes/WP84_DIRECT_SIGNED_RESTRICTED_CORRELATION_ATTACK.md",
    "notes/WP84_NEAR_ALIAS_SURVIVOR_ORBIT_COMPRESSION.md",
    "src/wp84_fifth_full_pool_amplitude.py",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def sfrac(x: F) -> str:
    return f"{x.numerator}/{x.denominator}"


def raw_key(degree: int, signs: str, part: str) -> tuple[int, str, str]:
    return degree, signs, part


def reconstruct() -> dict:
    rows = list(csv.DictReader(SURVIVORS.open(encoding="utf-8", newline="")))
    functionals = json.loads(FUNCTIONALS.read_text(encoding="utf-8"))
    raw_rows = {
        raw_key(int(r["degree"]), r["sign_word"], r["equality_labels"])
        for r in rows
    }
    row_counts = Counter(int(r["degree"]) for r in rows)
    raw_counts = Counter(k[0] for k in raw_rows)
    alias_counts: dict[str, int] = {"5": 0, "6": 0}
    for r in rows:
        alias_counts[r["degree"]] += 1

    raw_to_fid: dict[tuple[int, str, str], int] = {}
    descriptors = []
    alpha_mass = F(0)
    per_degree_mass = Counter()
    for fun in functionals:
        degree = int(fun["degree"])
        orbit = fun["raw_orbit_members"]
        omega = -F(11501, 12500) if degree == 5 else F(137641, 250000)
        exact_alpha = F(fun["exact_alpha"])
        if exact_alpha != len(orbit) * omega:
            raise AssertionError("canonical orbit coefficient mismatch")
        alpha_mass += abs(exact_alpha)
        per_degree_mass[degree] += abs(exact_alpha)
        for b, signs, part in orbit:
            key = raw_key(int(b), signs, part)
            if key in raw_to_fid:
                raise AssertionError("raw sign/equality class appears in multiple orbits")
            raw_to_fid[key] = int(fun["id"])
        descriptors.append({
            "functional_id": int(fun["id"]),
            "degree": degree,
            "sign_word": fun["sign_word"],
            "equality_partition": fun["equality_partition"],
            "aliases": fun["aliases"],
            "raw_origin_count": len(orbit),
            "per_raw_origin_consumer_coefficient": sfrac(omega),
            "orbit_collapsed_coefficient_if_mask_is_covariant": sfrac(exact_alpha),
        })
    if raw_rows != set(raw_to_fid):
        raise AssertionError("the 8740 survivor raw classes and canonical orbit origins disagree")
    if len(functionals) != 453 or len(raw_rows) != 8740:
        raise AssertionError("survivor cardinality changed")
    if dict(raw_counts) != {5: 1132, 6: 7608}:
        raise AssertionError("survivor degree census changed")
    if dict(row_counts) != {5: 1956, 6: 19632}:
        raise AssertionError("survivor class/alias census changed")
    if alpha_mass != F(163444421, 31250):
        raise AssertionError("exact coefficient mass changed")

    # Recompute the frozen quartic consumer and joint allowances from q(x)^2.
    q = [F(-19101, 185500), F(961, 3710), F(31, 50), F(-371, 500)]
    c = [sum((q[i] * q[k - i] for i in range(max(0, k - 3), min(3, k) + 1)), F(0))
         for k in range(7)]
    A, B = F(11501, 12500), F(137641, 250000)
    e_band = F(128952763, 92407500000)
    e_var = F(26060119, 12734908593750)
    jstar = F(21, 200) - c[0] - c[2] / 3 - e_band - e_var
    ideal = jstar + A / 36 - B * F(157, 630)
    relaxed = jstar + A / 36 - B * F(34, 135)
    if (c[5], c[6]) != (-A, B):
        raise AssertionError("fifth/sixth consumer signs or coefficients changed")
    if ideal != F(27704610381502, 17886179119921875):
        raise AssertionError("ideal allowance replay mismatch")
    if relaxed != F(52897896569489, 572357731837500000):
        raise AssertionError("relaxed allowance replay mismatch")

    return {
        "decision": "C. SURVIVOR COMPRESSED TO AN EXACT MASK SUPPORT-FUNCTION THEOREM",
        "frozen_starting_state": {
            "branch": FROZEN_BRANCH,
            "head": FROZEN_START_HEAD,
            "parent": "4f0375b2ebc7a263ca3a59133e46d3449bf89989",
            "worktree_at_start": "tracked-clean; pre-existing untracked notebooklm_packet/ excluded and preserved",
        },
        "scope": "conditional at each fixed T and supplied section I; source-mask uniformity over the product Boolean class allowed by the callback interface",
        "pinned_mathematical_source_inputs": {p: sha(ROOT / p) for p in AUDIT_INPUTS},
        "source_inputs": {
            "survivor_patterns_csv": {"path": "notes/WP84_NEAR_ALIAS_SURVIVOR_PATTERNS.csv", "sha256": sha(SURVIVORS), "class_alias_rows": len(rows)},
            "canonical_functionals_json": {"path": "notes/WP84_NEAR_ALIAS_CANONICAL_FUNCTIONALS.json", "sha256": sha(FUNCTIONALS), "functionals": len(functionals)},
        },
        "survivor_counts": {
            "raw_sign_equality_classes": dict(sorted(raw_counts.items())),
            "raw_sign_equality_class_total": len(raw_rows),
            "class_alias_rows": dict(sorted(alias_counts.items())),
            "class_alias_pair_total": len(rows),
            "reduced_real_functionals": len(functionals),
        },
        "consumer_coefficients": {
            "omega5": sfrac(-A),
            "omega6": sfrac(B),
            "exact_absolute_mass_after_covariant_orbit_collapse": sfrac(alpha_mass),
            "exact_absolute_mass_decimal_diagnostic": f"{float(alpha_mass):.12f}",
            "functionals": descriptors,
        },
        "exact_frozen_budget_replay": {
            "q_polynomial": [sfrac(x) for x in q],
            "q_squared_coefficients_c0_to_c6": [sfrac(x) for x in c],
            "e_band": sfrac(e_band),
            "e_variance": sfrac(e_var),
            "Jstar": sfrac(jstar),
            "ideal_allowance": sfrac(ideal),
            "relaxed_allowance": sfrac(relaxed),
            "relaxed_H400_primitive_scale_if_multiplier_201": sfrac(relaxed / 201),
            "interpretation": "budget reference only; no survivor or long-tail charge is certified",
        },
        "signed_aggregate_definition": {
            "near_alias": "Q_surv(T;chi)=Re sum over the 8740 surviving raw sign/equality classes and their frozen listed alias integers, all injective ordinary-prime assignments p<=N(T), all closed R=6000 paths, exact root sums, actual carrier phases, original mask chi, and indicator 0<|delta|<=H/T; each raw degree-b origin has coefficient omega_b.",
            "long_tail": "Q_tail(T;chi)=the exact signed source sum for all remaining noncentral raw sign/equality/alias terms on |delta|>H/T in the nearest residual cell [-L/2,L/2), with m!=0 and delta!=0; retain the complete natural prime pool, R=6000 paths, root sums, carrier phases, exact equality masks, and omega_b. No unproved family is set to zero.",
            "combined_debt": "S_T(chi)=Q_surv(T;chi)+Q_tail(T;chi); the m=0 central contribution is outside this near-alias/dilated-product debt and remains in its separately frozen ledger.",
            "per_raw_origin_formula": "Re[ omega_b * chi(key) * W_(epsilon,lag)(p) * K_lag(lambda) * known_admission_indicators ], where W=prod_j[-log(p_j)/(a_phi(T)*L*sqrt(p_j))*f_(lag_j)^(epsilon_j)(log(p_j)/L)]*exp(2*pi*i*sum_j epsilon_j*u_(j-1)*log(p_j)/L), lambda=sum_j epsilon_j log(p_j), K=exp(i*T*lambda+2*pi*i*i_min*lambda/L)/dprime * sum_(r=0)^(M_lag-1) exp(2*pi*i*r*lambda/L).",
            "no_substitutions": ["no absolute-value replacement of the signed aggregate", "no sharp/continuum kernel substitution", "no selected-prime core", "no fabricated section/selector", "no dropped long tail"],
        },
        "mask_dependence": {
            "type": "linear in Boolean callback values after grouping all summands with identical callback key",
            "callback_key": "(fid, slots, lag, T, section, m)",
            "coefficient_definition": "a_k(T,I)=sum over every raw near/tail atom mapping to key k of omega_b * known_indicator * Re(W*K); all duplicate-key contributions are combined before taking positive parts.",
            "exact_objective": "S_T(chi)=sum_(k in K_T) chi_k * a_k(T,I), chi_k in {0,1}.",
            "exact_extrema": {
                "sup_S": "sum_k max(a_k,0)",
                "inf_S": "sum_k min(a_k,0)",
                "sup_abs_S": "max(sum_k max(a_k,0), -sum_k min(a_k,0))",
                "maximizer": "chi_k=1 iff a_k>0; ties arbitrary",
            },
            "structure_classification": "a diagonal linear functional on the Boolean hypercube; an exact finite LP/support-function reduction for fixed T,I. No Gram/PSD cancellation follows from arbitrary independent bits.",
            "optional_known_covariance_constraints": "If a chosen mask class explicitly requires chi(g*k)=chi(k) for the certified cyclic/reversal/conjugation actions, group callback keys into generated orbits C and replace each a_k by A_C=sum_(k in C)a_k; then sup S=sum_C max(A_C,0). The literal callback API does not enforce these equalities.",
            "orbit_compression_condition": "The 453 coefficient vector c_alpha=|O_alpha|*omega_b is valid only when chi is equivariant under every slot rotation/reversal/conjugation used to form O_alpha. Without such a source-independent covariance axiom the 8740 raw origins must remain separate.",
            "adversarial_mask": "for the finite fixed-(T,I) key set, the Boolean table chi_k=1[a_k>0] realizes sup_S exactly. This is a falsifier of cancellation based solely on orbit symmetry/API constraints, not a source-authentic historical selector and not a numerical violation of the budget.",
        },
        "uniform_theorem_needed": "limsup_(T->infinity) sum_(k in K_T) max(a_k(T,I(T)),0) <= Delta_available, uniformly over every admissible supplied section I(T) and every executable-contract Boolean mask; Delta_available is at most 52897896569489/572357731837500000 before other unpaid transfers.",
        "analytic_status": {
            "positive_part_sum_evaluated_or_bounded": False,
            "proved_signed_saving": "NONE",
            "relaxed_budget": "UNPAID",
            "long_tail_charge": None,
            "source_authentic_mask": None,
            "global_fifth_rank": "38-72 unchanged",
            "strict_gt_79": "OPEN",
        },
        "full_pool_and_band_flags": {
            "ordinary_prime_cutoff": "N(T)=floor(exp(L-sqrt(L)))",
            "complete_prime_pool": True,
            "finite_core_substitution": False,
            "R": 6000,
            "closed_paths": True,
            "exact_carrier_and_equality_partition": True,
            "near_alias_and_long_tail_both_retained": True,
            "diagnostic_rows_used": False,
            "source_selector_invented": False,
        },
        "first_remaining_unproved_lemma": "The source-weighted positive-part majorant displayed in uniform_theorem_needed; to recover the signed 453 coefficient cancellation one additionally needs a proved equivariance/feature restriction linking callback bits along the raw symmetry orbits, with an exact source definition.",
    }


def main() -> None:
    cert = reconstruct()
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS exact survivor/orbit census and rational joint-budget replay")
    print("Raw classes:", cert["survivor_counts"]["raw_sign_equality_class_total"],
          "canonical functionals:", cert["survivor_counts"]["reduced_real_functionals"])
    print("Mask dependence: exact diagonal Boolean LP; positive-part arithmetic theorem remains unproved")
    print("Relaxed allowance:", cert["exact_frozen_budget_replay"]["relaxed_allowance"])
    print("Decision C; no charge paid; strict >79 OPEN")


if __name__ == "__main__":
    main()
