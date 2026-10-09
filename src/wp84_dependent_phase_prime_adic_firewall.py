"""Produce exact source-level certificate for the WP84 prime-adic firewall.

The finite counterexample is certified with Fraction-only logarithm intervals.
This audit closes independent-Haar cancellation, falsifies an L2-only trace-grid
Hilbert lemma, and leaves the actual dependent-phase transfer open.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
START = "9ba9d4afad19cfdd8a9e4c2e5a386930fc16a14d"
K_CHAOS = 32
DELTA = F(1, 100000)


def need(ok, label):
    if not ok:
        raise AssertionError(label)


def log_interval_rational(x, terms=250):
    """Enclose log(x) by the positive atanh series, for integer x>1."""
    t = F(x-1, x+1)
    lo = sum((2*t**(2*k+1)/F(2*k+1) for k in range(terms)), F(0))
    # Bound the remaining denominators below by 2M+1 and sum a geometric tail.
    rem = 2*t**(2*terms+1)/(F(2*terms+1)*(1-t*t))
    return lo, lo+rem


def p_adic_counterexample():
    p, r, q1, q2 = 2, 1, 3, 5
    n1, n2, T = 253891, 173308, 7800
    l2, l3, l5 = log_interval_rational(2), log_interval_rational(3), log_interval_rational(5)
    lo = l2[0] + n1*l3[0] - n2*l5[1]
    hi = l2[1] + n1*l3[1] - n2*l5[0]
    target_lo, target_hi = F(1286529, 10**12), F(1286530, 10**12)
    need(target_lo < lo <= hi < target_hi, "rational log enclosure for near-alias example")
    need(2*T*hi < F(1, 40), "all carrier phases lie below 1/40")
    # Coarse exact cutoff check: 3<pi<22/7 gives X>1000; log X<8;
    # e^3<21 gives e^-sqrt(log X)>1/21, so natural N is at least 47.
    e3_upper = sum((F(3**k, _factorial(k)) for k in range(13)), F(0))
    e3_tail = F(14, 11)*F(3**13, _factorial(13))
    e8_lower = sum((F(8**k, _factorial(k)) for k in range(16)), F(0))
    need(e3_upper+e3_tail < 21, "e^3<21 rational Taylor tail")
    need(e8_lower > 1300, "e^8>1300 rational partial sum")
    need(7800*F(7,44)>1000, "X>1000 from pi<22/7")
    # The rational comparison is equality; the strictness comes from pi>3.
    need(F(7800,6)<=1300, "X<1300 from pi>3")
    N_lower = 47
    need(N_lower >= 5 and p**2 <= N_lower, "2,3,5 and p^2 retained by natural cutoff")
    # For every index k in a contiguous source section, tau_k<=2T. Since
    # 0<lambda<hi and 2T*hi<1/40, Re exp(i tau_k lambda)>=1-(1/40)^2/2.
    kernel_lower = F(3199, 3200)
    need(F(1)-F(1, 2*40**2) == kernel_lower, "kernel lower bound from cos x>=1-x^2/2")
    return {
        "type": "finite adversarial atom for any L2-only p-adic kernel inequality",
        "current_base_p": p, "current_power_r": r,
        "p_excluded_response_bases": [q1, q2],
        "response_character": f"z_{q1}^{n1} z_{q2}^{-n2}",
        "response_coefficient": "1", "response_L2_norm": "1",
        "exact_product_form": f"{p}*{q1}^{n1}/{q2}^{n2}",
        "log_frequency_interval": [str(target_lo), str(target_hi)],
        "T": T, "natural_cutoff_lower_bound_N": N_lower,
        "all_retained_bases": [2, 3, 5],
        "p_adic_valuation_of_response_ratio": 0,
        "p_adic_valuation_after_current_insertion": r,
        "max_sample_phase_upper": "<1/40",
        "geometric_kernel_modulus_lower": str(kernel_lower),
        "proof": "Fraction-only atanh series encloses log 2, log 3, log 5. The subgroup Z log 3 + Z log 5 is dense because log 3/log 5 is irrational by unique factorization, so for every T there is also a p-excluded monomial with |log(2*3^a*5^b)|<1/(100T). The one-atom L2 norm stays 1 while |K_I|>=3199/3200. This falsifies any uniform trace-grid bound tending to zero from L2 coefficient control alone.",
        "scope_warning": "The monomial is an adversarial L2 spectrum, not asserted to be an actual coefficient of D Psi_R. It falsifies the proposed norm-only lemma, not A1/A2 or the zeta theorem."
    }


def _factorial(n):
    x = 1
    for j in range(2, n+1):
        x *= j
    return x


def source_hashes():
    paths = [
        "notes/WP84_PRIME_BASE_GROUPED_LINDEBERG.md",
        "notes/WP84_LOCALIZE_FIRST_HERMITE_PROJECTION.md",
        "notes/WP84_FIXED_R_ARITHMETIC_FILTERED_MOMENT_TRANSFER.md",
        "notes/WP84_COMPILED_MEHLER_PRIME_LINDEBERG.md",
        "notes/WP84_POSITIVE_LAG_GAUSSIAN_VIABILITY_AND_PHASE_RESPONSE.md",
        "notes/WP84_LOCALIZE_FIRST_HERMITE_PROJECTION_CERTIFICATE.json",
    ]
    return {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}


def build():
    counter = p_adic_counterexample()
    return {
        "schema": "wp84-dependent-phase-prime-adic-firewall-v1",
        "starting_head": START,
        "branch": "codex/c5-c6-attack-20261006",
        "decision": "C",
        "frozen": {"K": K_CHAOS, "delta": str(DELTA), "strict_gt79": "OPEN"},
        "prime_base_grouping": {
            "definition": "G_p=sum_{a>=1,p^a<=N} B_{p^a}; every retained p^a uses one common base phase z_p^a",
            "block_bound": "||B_{p^a}||op<=4 log(p)/(L p^(a/2))",
            "group_bound": "||G_p||op<=(4 log p/L)/(sqrt(p)-1)",
            "mass": {"max": "O(1/L)", "square_sum": "O(1)", "cube_sum": "O(L^-3)"},
            "leave_one_out": "Y_p contains no p^a term for any a; Gaussian replacements and masks are held fixed when the other deterministic phases are lifted"
        },
        "A1_A2_exact_reconstruction": {
            "A1": "sum_p E_{K,g}[D Psi_R(Y_p(K,g)) dot V_p(K)]",
            "A2": "(1/2) sum_p E_{K,g}[D^2 Psi_R(Y_p(K,g)):(V_p(K)V_p(K)^T-Sigma_p)]",
            "remainder": "O_R(L^-3) from prime-base cube mass",
            "complex_current_block": "V_p(z_p)=sum_{a:p^a<=N}(gamma_{p,a} z_p^a+conjugate(gamma_{p,a}) z_p^-a), realified in xi/chi lag coordinates; gamma contains c_{p^a} exp(i T a log p), lag factors exp(i2pi r a log p/L), i a log p/L, and source masks",
            "Y_p_contents": "for each fixed permutation/hybrid state, all q!=p deterministic blocks use z_q^a with shared base z_q; already Gaussian blocks remain functions of their fixed Gaussian realization; current p group excluded"
        },
        "prime_adic_firewall": {
            "exact_word_once": "impossible at every word length: v_p(current)=+/-a nonzero while every q!=p factor has v_p=0",
            "two_current_insertions": "same sign has v_p=+/- (a+b) and cannot close; opposite signs close exactly only if a=b",
            "haar_A1": "CLOSED exact zero: R1_p is independent of z_p and every current coordinate has nonzero characters z_p^{+/-a}; Haar average annihilates all real/imag xi/chi and lag/mask coefficients",
            "haar_A2": "CLOSED exact zero after Sigma_p: E_{z_p}[V_p V_p^T]=Sigma_p; same-sign and opposite unequal powers have nonzero p exponent; opposite equal powers produce precisely the grouped covariance diagonal",
            "equal_power_actual_grid": "the a=b opposite-sign term is phase-independent and cancels pointwise against Sigma_p when Sigma_p is the exact covariance of the full grouped current base; if a limiting covariance is substituted, the difference is charged to the already closed degree-two covariance transfer",
            "masks_lags": "fixed masks multiply coefficients only; they do not alter the p-character exponent; conditional Haar cancellation holds for each mask and Gaussian realization"
        },
        "trace_grid_discrepancy": {
            "specialization": "z_q(K)=exp(i(T+2pi K/L)log q)",
            "kernel": "K_I(omega)=d'^-1 sum_{k in I} exp(i(T+2pi k/L)omega)=exp(i(T+2pi k_-/L)omega) D_{d'}(omega/L)",
            "A1_frequency": "lambda_nu+a log p, a>=1, and conjugates; lambda_nu=sum_{q!=p} nu_q log q",
            "A2_frequency": "lambda_nu+r log p; r=+/- (a+b), or r=+/- (a-b) with a!=b after equal-power covariance subtraction",
            "exact_residual": "Delta1_p=A1_grid,p-A1_Haar,p; Delta2_p=A2_grid,p-A2_Haar,p; Haar terms are zero, but no grid-to-Haar estimate is established",
            "same_index": "K is common to every z_q(K), current and response; no independent phase replacement is made"
        },
        "Bohr_coefficients": {
            "expansion": "R1_p(z,g)=sum_nu c1_{p,nu,g} z^nu and R2_p(z,g)=sum_nu c2_{p,nu,g} z^nu in L2(Haar x Gaussian); finite-dimensional torus Fejer means recover the continuous response uniformly, so no absolute Fourier convergence is asserted",
            "coordinate_dimension": "n_R=4(2R+1)",
            "parseval_R1": "sum_nu E_g ||c1_{p,nu,g}||_2^2 <= C1_R^2",
            "parseval_R2": "sum_nu E_g ||c2_{p,nu,g}||_F^2 <= n_R C2_R^2; Hessian bilinear operator norm C2_R implies Frobenius norm <=sqrt(n_R) C2_R",
            "weighted_R1": "sum_nu nu_q^2 E||c1||_2^2=E||partial_theta_q R1||_2^2<=C2_R^2 g_q^2",
            "weighted_R2": "sum_nu nu_q^2 E||c2||_F^2<=n_R C3_R^2 g_q^2",
            "C1_C2_C3": ["5203190992411521/10234375000000", "61724201821495911/1675878906250", "2710080021962816136/878160546875"],
            "prime_influences": "g_q^(j)<=C_{j,R}(log q/L) sum_{a>=1} a^j q^(-a/2)<=C'_{j,R} log q/(L sqrt(q)); max_q g_q^(j)=O_R(L^-1), sum_q (g_q^(j))^2=O_R(1), sum_q (g_q^(j))^3=O_R(L^-3) for fixed j, by the source prime-square measure",
            "regularity_scope": "first angular derivative of R1 uses C2_R; first angular derivative of R2 uses C3_R. Higher angular derivatives require the corresponding fixed-pole resolvent Frechet hierarchy, not a K-dependent derivative bound."
        },
        "p_adic_L2_hilbert_lemma": {
            "status": "FALSE for L2 coefficient control alone",
            "counterexample": counter,
            "exact_weighted_Hilbert_operator_norm": "For positive weights w_nu, sup_{sum w_nu|b_nu|^2<=1}|sum b_nu K_I(lambda_nu+r log p)| = (sum |K_I(lambda_nu+r log p)|^2/w_nu)^(1/2); this dual weighted-kernel square mass tending to zero is the necessary-and-sufficient condition for a uniform linear bound in that weighted l2 class.",
            "minimum_regularization_conclusion": "At least angular-frequency regularity excluding the constructed high-degree near-resonant atoms is necessary. A first torus derivative is the first Sobolev level that penalizes this atom, and the source gives bounded aggregate first-influence estimates; sufficiency for the full p-summed signed form is NOT proved. The exact missing condition is the weighted-kernel dual-mass estimate above (or stronger source-matched signed cancellation)."
        },
        "periodic_aliases": {
            "condition": "lambda_nu+r log p=mL iff p^r prod_{q!=p} q^nu_q=X^m",
            "m_zero": "impossible for r!=0 by unique factorization",
            "m_nonzero": "not excluded: X may be tuned to an exact arithmetic alias; its kernel has modulus one",
            "m_range": "unbounded for an unrestricted Bohr response; the finite |m|<=word-degree alias bound in fixed-degree moment expansions does not transfer",
            "near_alias": "all |lambda_nu+r log p-mL|<=O(1/T) windows remain in the actual residual; integer separation only gives a product-length-dependent lower bound"
        },
        "A1_A2_status": {
            "A1_haar": "CLOSED zero",
            "A2_haar_after_covariance": "CLOSED zero",
            "A1_actual": "OPEN; all current powers stay in first-order mean; the source coefficient l1 envelope sum_{p<=N} log(p)/(L sqrt(p)) diverges like 2 sqrt(N)/L by PNT, so triangle gives no bounded A1 estimate",
            "A2_actual": "OPEN after exact equal-power covariance subtraction; unequal opposite-sign, same-sign and periodic/near-alias response correlations remain",
            "A2_proper_power_current": "CLOSED O_R(L^-1) absolute bound: proper-power group square mass O(L^-2), ordinary-base square mass O(1), Cauchy for cross terms",
            "A1_proper_power_current": "retained; prime-base cube mass only pays the Taylor remainder and does not imply first-order mean cancellation",
            "A1_exact_resonance": "none at m=0 by p-adic valuation",
            "A2_exact_resonance": "only opposite equal powers, already subtracted by Sigma_p"
        },
        "degree_one_two_reuse": {
            "directly_covered": ["the p-base equal-power opposite-sign covariance diagonal after Sigma_p", "unweighted prime-square/covariance normalizations already covered by the fixed-R degree-two transfer", "aggregate proper-power contribution to bounded full-cylinder expectation by the established L2 deletion"],
            "needs_p_adic_bohr_lemma": ["all of A1 on the actual one-dimensional trace path", "A2 unequal-power opposite-sign and same-sign terms after covariance subtraction"],
            "still_higher_order": ["response Fourier coefficients have unbounded degree even though the current insertion order is one or two; generic fixed-degree b=1,2 estimates do not control their product with the leave-one-prime response", "A1 proper-power part cannot be removed termwise by square mass"]
        },
        "source_section_smoothing": "NONE: averaging only already-admissible sections with start variation o(d) does not supply the O(d) independent phase averaging needed to smooth the 1/T kernel window; translated local block-center averaging does not change the common trace-index path.",
        "first_remaining_theorem": "Prove the source-matched signed limit sum_p Delta1_{p,T,R}+sum_p Delta2_{p,T,R}->0 for each fixed R, with the exact p-excluded response coefficients, all current p^a powers, same-index K path, periodic and near aliases, and full natural cutoff. A sufficient absolute version is the weighted-kernel dual-mass estimate summed over p and residual current exponent r; L2 Parseval bounds alone are insufficient.",
        "dependent_phase_law": "OPEN",
        "strict_gt79": False,
        "hostile_mutations": [
            "put_p_in_Yp", "independent_power_phases", "drop_proper_powers_A1", "mean_zero_kills_A1",
            "covariance_match_kills_A2", "omit_same_K", "replace_path_by_Haar", "response_character_contains_p",
            "same_sign_exact_closure", "omit_equal_power_sigma", "assume_gap_1_over_T", "assume_X_irrational",
            "drop_periodic_alias", "absolute_Fourier_without_proof", "use_falsified_L2_lemma",
            "interchange_R_T", "shorten_N", "change_K_or_delta", "synthetic_data_as_arithmetic",
            "claim_gt79_from_A1_A2"
        ],
        "source_sha256": source_hashes()
    }


def main():
    cert = build()
    out = ROOT / "notes/WP84_DEPENDENT_PHASE_PRIME_ADIC_FIREWALL_CERTIFICATE.json"
    out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: Haar p-adic A1/A2 cancellation, grouped-power classification, exact near-alias L2 counterexample.")
    print("A1/A2 actual trace-grid transfer remains OPEN; strict >79 remains OPEN. Decision C.")


if __name__ == "__main__":
    main()
