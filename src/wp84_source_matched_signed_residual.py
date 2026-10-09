#!/usr/bin/env python3
"""Build the source-matched signed-residual audit certificate (stdlib only).

This records exact algebraic reductions and an exact k_ab sign census on the
lag-zero pair subfamily.  It intentionally does not claim a global sign census
over all R=6000 path geometries or an estimate for the remaining prime sums.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "WP84_SOURCE_MATCHED_SIGNED_RESIDUAL_CERTIFICATE.json"
R = 6000
A = "11501/12500"
B = "137641/250000"
JSTAR = "64788151489666079/572357731837500000"
G9 = "43770221409581023769108432686241/21264421581420459982848000000000000"
PAIR6_LOWER = "31498340500050746323/150466924118016000000"

SOURCES = [
    "notes/WP84_STRICT79_SOURCE_MATCHED_ARITHMETIC_REDUCTION.md",
    "notes/WP84_STRICT79_HOSTILE_AUDIT_AND_BALANCED_PAIR_REDUCTION.md",
    "notes/WP84_JOINT_THIRD_FIFTH_SIXTH_ARITHMETIC_OBSTRUCTION.md",
    "notes/WP84_THIRD_AWARE_SAME_SECTION_THEOREM_OR_OBSTRUCTION.md",
    "notes/WP84_STRICT79_SIGNED_ARITHMETIC_THEOREM_OR_OBSTRUCTION.md",
    "notes/WP84_STRICT79_SIGNED_LEDGER_CERTIFICATE.json",
]


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def lag_zero_census(b: int) -> dict:
    """Census parameter triples (slot pair, relative lag sum d), not paths."""
    placements = []
    positive = negative = zero = 0
    for t in range(b - 1):
        pairs = b - 1 - t
        # t intervening increments sum to d; the other b-2-t increments
        # sum to -d.  Pair-slot increments themselves are fixed at zero.
        M = min(t, b - 2 - t) * R
        pos, neg, zer = 1, 2 * M, 0
        placements.append({
            "intervening_increment_count": t,
            "slot_pair_placements": pairs,
            "max_abs_relative_prefix_difference": M,
            "d_values": [-M, M],
            "positive_d_zero_count": pos,
            "negative_d_nonzero_count": neg,
            "zero_coefficient_count": zer,
            "coefficient": "1/6 if d=0; -1/(2*pi^2*d^2) if d!=0",
            "multiplicity_scope": "(slot-pair placement,d) parameter tuples only; not full closed paths",
        })
        positive += pairs * pos
        negative += pairs * neg
        zero += pairs * zer
    return {
        "scope": "ell_a=ell_b=0 subfamily, all feasible integer d, R=6000",
        "formula": "k_ab=2*integral_0^1 s*(1-s)^2*cos(2*pi*d*s) ds = 1/6 (d=0), -1/(2*pi^2*d^2) (d!=0)",
        "placements": placements,
        "weighted_parameter_tuple_sign_counts": {
            "positive": positive,
            "negative": negative,
            "zero": zero,
        },
        "full_R6000_path_sign_census": "not computed or claimed; general k_ab depends on (ell_a,ell_b,q_(a-1)-q_(b-1))",
        "exact_symmetries": [
            "k(a,b,q)=k(b,a,-q)",
            "k(-a,-b,-q)=k(a,b,q)",
        ],
        "general_exact_formula": "k(a,b,q)=2*Re integral_0^1 s*f_a^+(s)*f_b^-(s)*exp(2*pi*i*q*s) ds",
        "finite_closed_form": "Expand f_a^+*f_b^-*exp(2*pi*i*q*s)=sum_n P_n(s)exp(2*pi*i*n*s), deg(P_n)<=2, with n in {q,q+a,q-b,q+a-b} after omitting duplicate/zero-frequency terms. Then k=2*Re sum_n sum_j P_(n,j)*J_(j+1)(n), where J_0(0)=1, J_j(0)=1/(j+1), J_0(n)=0 for n!=0, and J_j(n)=1/(2*pi*i*n)-j*J_(j-1)(n)/(2*pi*i*n) for n!=0. Coefficients of f are exact rational multiples of (pi*i)^-1; thus this is a finite exact rational/pi expression for every feasible (a,b,q), including zero-lag polynomial factors.",
        "finite_closed_form": "Expand f_a^+*f_b^-*exp(2*pi*i*q*s)=sum_n P_n(s)exp(2*pi*i*n*s), deg(P_n)<=2, with n in {q,q+a,q-b,q+a-b} after omitting duplicate/zero-frequency terms. Then k=2*Re sum_n sum_j P_(n,j)*J_(j+1)(n), where J_0(0)=1, J_j(0)=1/(j+1), J_0(n)=0 for n!=0, and J_j(n)=1/(2*pi*i*n)-j*J_(j-1)(n)/(2*pi*i*n) for n!=0. Coefficients of f are exact rational multiples of (pi*i)^-1; thus this is a finite exact rational/pi expression for every feasible (a,b,q), including zero-lag polynomial factors.",
    }


def build() -> dict:
    source_hashes = {}
    for rel in SOURCES:
        p = ROOT / rel
        source_hashes[rel] = {"sha256": sha256(p)}
    return {
        "title": "WP84 source-matched signed residual attack certificate",
        "status": "audit reduction only; no new signed saving",
        "start_head": "78b056687dfaacf5493334125eaa3120811c1969",
        "branch": "codex/c5-c6-attack-20261006",
        "push": False,
        "parameters": {
            "X": "T/(2*pi)", "L": "log X", "N": "floor(exp(L-sqrt(L)))",
            "R": R, "h": "2*pi/L", "d": "floor(T*L/(2*pi))",
            "section": "I0={0,...,d-1}",
            "section_selection": "canonical full section; no historical selector or synthetic row tuple",
            "prime_coefficient": "c_m=-Lambda(m)/(a_phi(T)*L*sqrt(m)); a_phi(T)->1",
            "kernel": "K_ell(lambda)=exp(i*(T+h*i_min)*lambda)/d * sum_{r=0}^{rho-1} exp(i*h*r*lambda), with original path roots and carrier",
        },
        "exact_reduced_residual": {
            "A": A, "B": B,
            "D5": "sum over original ordered closed R-paths, all signs, pairwise-distinct ordinary primes p_1..p_5<=N of (prod_j c_{p_j} f_(ell_j)^(eps_j)(log p_j/L) exp(2*pi*i*sum_j eps_j*q_(j-1)*log(p_j)/L))*K_ell(sum_j eps_j*log(p_j)); retain original windows, root range, and carrier",
            "Q3": "sum over original degree-5 paths, each of the 10 slot pairs (a,b), all signs and distinct visible ordinary primes p_j<=N (j not a,b), k_ab times their original filtered product and K_ell(sum_visible eps_j log(p_j)); retain visible prime exclusions/windows, root range, and carrier",
            "D6": "same all-distinct definition at degree 6",
            "Q4": "same one-balanced-pair definition at degree 6, sum over all 15 slot pairs",
            "pair_kernel": "phi_ab(s)=2*Re[f_(ell_a)^+(s) f_(ell_b)^-(s) exp(2*pi*i*(q_(a-1)-q_(b-1))*s)]; k_ab=integral_0^1 s*phi_ab(s) ds",
            "F_T": "-A*(D5+Q3)+B*(D6+Q4)",
            "split": {"F_pair": "-A*Q3+B*Q4", "F_distinct": "-A*D5+B*D6", "identity": "F_T=F_pair+F_distinct exactly"},
            "bounded_gate_transfer": "J_full=B*Pair6_6000+Re(F_T)+o(1)",
            "evidence_scope": "signed, unsplit full root sums; no near-alias masking before factorization; prime powers only removed by the previously proved bounded-gate aggregate equivalence",
            "collision_corrections": "distinctness restoration/inclusion-exclusion and previously closed collision classes are retained in the aggregate reduction; no correction is omitted",
        },
        "retained_class_census": {
            "degree5": {"total": 192, "all_distinct": 32, "balanced_one_pair": 160},
            "degree6": {"total": 544, "all_distinct": 64, "balanced_one_pair": 480},
            "interpretation": "orientation/sign/equality summands; not separately estimated or masked populations",
        },
        "k_ab_census": {"degree5": lag_zero_census(5), "degree6": lag_zero_census(6)},
        "operator_identities": {
            "complete_F_T_finite_R_trace_identity": "not established; no exact source derivation was found that expresses all D5,Q3,D6,Q4 as a finite combination of tau(DY^3), tau(V(Y)Y^2), tau(DY^4), tau(V(Y)Y^3), or analogous operators",
            "existing_conditional_cubic_identity": "under the inherited bounded-gate/source reduction, Q3=5*tau(D*Y^3)+5*tau(V(Y)*Y^2)+o(1); this does not represent Q4 or the whole F_T and gives no sign",
            "Y_law": "no Gaussian law for Y; auxiliary Gaussian W encodes only certified prime-square covariance",
            "cumulant": "partition-lattice inclusion/exclusion for prime equality is exact; no source-matched Möbius cumulant identity with a signed positivity conclusion for F_T was obtained",
        },
        "signed_budget": {
            "Jstar": JSTAR,
            "B": B,
            "Pair6_6000_lower_bound": PAIR6_LOWER,
            "required_negative_saving_g9": G9,
            "proved_negative_saving": "0",
            "saving_over_g9": "0",
            "remaining_deficit_at_least": G9,
            "eta": "additional strict positive slack required",
            "strict_gt79": "OPEN",
            "o1_is_sufficient": False,
        },
        "falsifiers": {
            "exact_filter_pair_signs": "for ell_a=ell_b=0, k_ab=1/6 at q=0 and -1/(2*pi^2*q^2) for every nonzero integer q; both signs occur on R=6000 closed paths",
            "matrix_scalar_shortcut": "B*x^6-A*x^5 is negative at x=1 and positive at x=-1; falsifies a universal scalar sign claim only, not a source-compatible arithmetic inequality",
            "alias_warning": "the root kernel retains exp(i*T*m*L); no periodicity or independent alias cancellation is asserted",
            "counterexample_scope": "algebraic sign shortcuts falsified; no source-compatible arithmetic counterexample to the target is claimed",
            "453_use": "not used as mask components, arithmetic compression, or an estimate",
            "cubic_covariance_sign": "D>=I/6 alone does not determine the sign of the path-weighted cubic correlation",
        },
        "first_remaining_theorem": {
            "statement": "For the exact source sums D5,Q3,D6,Q4 defined above, with the natural full prime cutoff, R=6000 original filters and closed paths, original full-section root kernel/carrier, and all retained orientations/windows, prove limsup_{T->infinity} Re[-(11501/12500)(D5+Q3)+(137641/250000)(D6+Q4)] <= 64788151489666079/572357731837500000-(137641/250000)*Pair6_6000-eta for some eta>0.",
            "status": "unproved; existing absolute mean-value bounds establish no positive-magnitude negative saving",
            "current_best": "the closed o(1) collision removals and central one-prime-side cells; zero signed constant saving",
        },
        "source_sha256": source_hashes,
        "hostile_mutations_required": [
            "change_A", "change_B", "change_R", "omit_D_all_distinct", "omit_Q_balanced_pair",
            "change_Pair6", "drop_root_phases", "sharp_overlap_kernel", "split_aliases_early",
            "finite_prime_core", "Gaussian_law_for_Y", "promote_W_covariance_to_Y_law",
            "claim_D_ge_I_over_6_cubic_sign", "omit_collision_corrections", "fake_section_selector",
            "453_as_arithmetic_bound", "claim_o1_suffices", "alter_g9",
            "promote_toy_matrix_to_source_arithmetic", "claim_strict_gt79_without_full_replay",
        ],
        "decision": "E",
    }


if __name__ == "__main__":
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(build(), indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
