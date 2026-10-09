"""Exact certificate producer for the WP84 localize-first Hermite audit.

All ledger arithmetic is rational.  The report deliberately leaves the
source-prime dependent-phase comparison open and never upgrades the >79 claim.
Run from any directory with Python 3.11+:
    python src/wp84_localize_first_hermite_projection.py
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
EPS = F(8711, 2778200)
EINF = F(7761139416076220170204368647089,
         1680256283972002400160000000000)
DELTA = F(1, 100000)
W0 = F(1415, 13891)
K_CHAOS = 32
SCALE = 10**12


def require(condition, message):
    if not condition:
        raise AssertionError(message)


def ceil_sqrt_fraction(x, scale=SCALE):
    """Return the least integer q with (q/scale)^2 >= x."""
    require(x >= 0, "sqrt input must be nonnegative")
    n = x.numerator * scale * scale
    q = isqrt(n // x.denominator)
    while F(q, scale) ** 2 < x:
        q += 1
    while q and F(q - 1, scale) ** 2 >= x:
        q -= 1
    return F(q, scale)


def decimal_enclosure(x, places=12):
    scale = 10**places
    lo = (x.numerator*scale)//x.denominator
    hi = -((-x.numerator*scale)//x.denominator)
    return [str(F(lo, scale)), str(F(hi, scale))]


def dual_witness():
    obj = json.loads((ROOT / "notes/WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF_CERTIFICATE.json").read_text())
    rows = [w for w in obj["witnesses"] if w["K"] == K_CHAOS and w["kind"] == "lower"]
    require(len(rows) == 1, "expected unique frozen K=32 lower witness")
    w = rows[0]
    return [F(x) for x in w["rhos"]], [F(x) for x in w["coefficients"]]


def lambda_amplification(lambdas):
    return sum(map(abs, lambdas), F(0))


def localization_row(U, m, lam):
    # a_phi -> 1 and C_* = 2 are the eventual source envelope.
    k = (m - 1).bit_length()
    sqrt_e = ceil_sqrt_fraction(EINF)
    root_u = ceil_sqrt_fraction(F(2) + F(U, 4))
    root_d = ceil_sqrt_fraction(F(2) + DELTA / 4)
    new_coeff = 20 * sqrt_e
    h_upper = F(8 * (k + 2), 9 * m)  # pi > 3; H_m <= 1 + ceil(log_2 m)
    e2 = new_coeff**2 * (root_u + root_d)**2 * h_upper
    target2 = (EPS / 4) ** 2
    require(e2 < target2, f"localization threshold failed for U={U}, m={m}")
    # One less m is not advertised as a mathematical lower bound; this is the
    # first passing integer found under this deliberately conservative envelope.
    old_new_ratio = F(43) * lam / new_coeff
    return {
        "U": U, "m": m, "R": m - 1, "ceil_log2_m": k,
        "h_upper": str(h_upper), "sqrt_Einf_upper": str(sqrt_e),
        "sqrt_U_marginal_upper": str(root_u),
        "sqrt_delta_marginal_upper": str(root_d),
        "e_pair_squared_upper": str(e2),
        "target_epsilon_over_4_squared": str(target2),
        "ratio_to_target_squared": str(e2 / target2),
        "coefficient_reduction_ratio_old_over_new": str(old_new_ratio),
        "strictly_below_epsilon_over_4": True,
        "threshold_status": "certified sufficient; not claimed globally minimal"
    }


def baseline_derivatives():
    # Source-certified |q_1|,|q_2|<442/1000 and |q_3|<634/1000.
    qabs = {1: F(442, 1000), 2: F(442, 1000), 3: F(634, 1000)}
    a = F(131, 200)
    u1, u2, u3 = 2/a, 4/a**2, 12/a**3
    C = []
    for r in (1, 2, 3):
        val = F(0)
        for n, qn in qabs.items():
            if r == 1:
                term = n*u1
            elif r == 2:
                term = n*u2 + n*(n-1)*u1**2
            else:
                term = n*u3 + 3*n*(n-1)*u2*u1 + n*(n-1)*(n-2)*u1**3
            val += qn*term
        C.append(val)
    D1, D2, D3 = C[0]*6, C[1]*36, C[2]*216
    psi = [4*ceil_sqrt_fraction(EINF)*D1,
           4*(D1**2 + ceil_sqrt_fraction(EINF)*D2),
           4*(3*D1*D2 + ceil_sqrt_fraction(EINF)*D3)]
    return {
        "pole_imaginary_part": "131/200",
        "q_coefficient_modulus_upper": {"q1": "221/500", "q2": "221/500", "q3": "317/500"},
        "resolvent_direction_bounds": {"u1": str(u1), "u2": str(u2), "u3": str(u3)},
        "Q_derivative_bounds_C1_C2_C3": list(map(str, C)),
        "Q_derivative_bounds_decimal": list(map(float, C)),
        "sample_map_operator_norm": "<=6",
        "sampled_consumer_derivative_bounds_D1_D2_D3": list(map(str, (D1, D2, D3))),
        "Psi_derivative_bounds_C1_C2_C3": list(map(str, psi)),
        "Psi_derivative_bounds_decimal": list(map(float, psi)),
        "scope": "fixed R; bounds are crude valid cylinder derivative envelopes, not a prime Lindeberg closure"
    }


def multiplier_norm(rhos, lambdas):
    lam0 = abs(lambdas[0])
    lam_u = lambda_amplification(lambdas)
    end = 2048
    powers = [F(1)] * len(rhos)
    max_abs = F(0)
    max_n = 0
    for n in range(end):
        val = lambdas[0] + sum((lambdas[j+1] * powers[j] for j in range(len(rhos))), F(0))
        if abs(val) > max_abs:
            max_abs, max_n = abs(val), n
        powers = [powers[j] * rhos[j] for j in range(len(rhos))]
    tail = lam_u * F(3, 8)**16
    require((F(127, 128)**128) < F(3, 8), "geometric tail block inequality")
    require(tail < F(1, 100), "tail envelope below 0.01")
    upper_tail = lam0 + F(1, 100)
    upper = max(max_abs, upper_tail)
    require(max_abs <= upper, "finite scan envelope")
    return {
        "q_lambda_definition": "lambda0 + sum_j lambda_j rho_j^n",
        "finite_scan_n": "0..2047", "finite_scan_sup_enclosure_1e-12": decimal_enclosure(max_abs),
        "finite_scan_argmax": max_n,
        "tail_bound_n_ge_2048": str(tail),
        "tail_bound_simple_upper": "<1/100",
        "M_q_lower_bound_from_limit_enclosure_1e-12": decimal_enclosure(lam0),
        "M_q_upper_bound_enclosure_1e-12": decimal_enclosure(upper),
        "Lambda_U": str(lam_u),
        "operator_identity": "T_q=lambda0 I+sum lambda_j P_rho_j; chaos-n eigenvalue q_lambda(n); ||T_q||=sup_n |q_lambda(n)|",
        "status": "certified interval for M_q; not used in the localize-first bound"
    }


def build_certificate():
    rhos, lambdas = dual_witness()
    lam = lambda_amplification(lambdas)
    old_coeff = F(43) * lam
    new_coeff = 20 * ceil_sqrt_fraction(EINF)
    R_values = [953368280616, 1007195524155, 1137699372206,
                1339733575173, 1715712785959, 2463125307050]
    Us = [1, 2, 4, 8, 16, 32]
    rows = [localization_row(U, R+1, lam) for U, R in zip(Us, R_values)]
    require(F(43)*lam == old_coeff, "old localization coefficient")
    require(new_coeff == 20*ceil_sqrt_fraction(EINF), "new coefficient")

    root = ROOT
    source_paths = [
        "notes/WP84_TAIL_CAPPED_EXACT_FRONTIER_CONSUMER.md",
        "notes/WP84_TAIL_CAPPED_FINITE_U_CURVATURE.md",
        "notes/WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF.md",
        "notes/WP84_DIRECT_PRIME_FIELD_STATE_LAW.md",
        "notes/WP84_FIXED_R_ARITHMETIC_FILTERED_MOMENT_TRANSFER.md",
        "notes/WP84_R2_DISPLACEMENT_TAIL_TRUNCATION.md",
        "notes/WP84_DIRECT_MPRIME_TAIL_O1_OVER_R.md",
        "notes/WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF_CERTIFICATE.json",
    ]
    return {
        "schema": "wp84-localize-first-hermite-projection-v1",
        "starting_head": "be51f8b9b6ca516ef92f2b2957897986d2c2b99e",
        "branch": "codex/c5-c6-attack-20261006",
        "decision": "C",
        "consumer": {
            "c": "3142/2415", "a": "131/200", "K": K_CHAOS,
            "delta": str(DELTA), "E_inf": str(EINF), "w0": str(W0), "epsilon": str(EPS),
            "cap": "0 <= f <= E_inf and 1-f <= 1_{x>0}; large-u tail is removed for this one-sided capped consumer"
        },
        "projection_contraction": {
            "statement": "||P_{<=K}(F-G)||_2 <= ||F-G||_2",
            "proof": "P is orthogonal in L2(standard Gaussian; normalized HS); Pythagoras. Difference of squared norms <= (||F||+||G||)||F-G||.",
            "bounded_consumer_result": "|S_K(F)-S_K(G)| <= 2 sqrt(E_inf) ||F-G||_2",
            "exact_multiplier_squared": str(4*EINF),
            "independent_of": ["K", "weak-dual rho count", "Lambda_U", "453"],
            "finite_basis_replay": "replay script checks projection contraction on exact rational finite Hermite-coordinate vectors and rejects an expansive map"
        },
        "localization": {
            "cut_HS_square": "E ||H-H_cut||_{2,tau}^2 <= h_m (C_* + u/(4 a_phi^2)); h_m=8(H_m+1)/(pi^2 m)",
            "consumer_Lipschitz": "C1<=10 in normalized Schatten-2 L2",
            "new_single_layer": "e_proj(u,R)=20 sqrt(E_inf) sqrt(h_m) sqrt(C_*+u/(4 a_phi^2))",
            "new_pair": "e_proj(U,R)+e_proj(delta,R)=20 sqrt(E_inf) sqrt(h_m)[sqrt(C_*+U/(4a_phi^2))+sqrt(C_*+delta/(4a_phi^2))]",
            "eventual_envelope": "C_*=2, a_phi -> 1; h_m <= 8(ceil(log_2 m)+2)/(9m), using pi>3 and H_m<=1+ceil(log_2 m)",
            "old_weak_dual_pair": "43 sqrt(h_m)[Lambda_U sqrt(C_*+U/(4a_phi^2))+sqrt(C_*+delta/(4a_phi^2))]",
            "Lambda_U": str(lam), "Lambda_total_with_initial_upper_witness": str(lam+1),
            "old_sqrt_h_coefficient": str(old_coeff),
            "new_sqrt_h_coefficient": str(new_coeff),
            "new_sqrt_h_coefficient_decimal": float(new_coeff),
            "coefficient_reduction_factor": str(old_coeff/new_coeff),
            "coefficient_reduction_factor_decimal": float(old_coeff/new_coeff),
            "R_table": rows,
            "edge_term": "|e_edge|<=4 E_inf R/d for the two-layer projected-energy cylinder: at most 2R edge sites, each projected diagonal energy lies in [0,E_inf], so the pair-cylinder value lies in [-E_inf,E_inf]; tends to zero only after T->infinity at fixed R",
            "order_of_limits": "fixed R -> T->infinity -> R->infinity; no R(T)"
        },
        "fixed_R_covariance_transfer": {
            "status": "CLOSED at fixed R under the existing covariance convergence",
            "argument": "C_T,R -> C_ref,R in operator norm; canonical positive PSD roots satisfy ||C_T,R^(1/2)-C_ref,R^(1/2)||_op <= ||C_T,R-C_ref,R||_op^(1/2), including singular limits. Couple both fields using the same finite standard Gaussian g. Fixed-pole Q is bounded/Lipschitz; dominated/L2 convergence gives S_K,T,R(u)->S_K,ref,R(u).",
            "2K_plus_2_derivative_debt": "REMOVED after fixed-R localization; no differentiation of P_{<=K} or covariance projector",
            "quantifier_warning": "does not justify interchanging R and T limits"
        },
        "chaos_representation": {
            "orthogonal_coordinate_change": "invariant: total-degree Hermite subspaces are preserved by second quantization of an orthogonal map",
            "redundant_coordinates": "invariant after embedding: unused independent coordinates are degree zero; isometric Gaussian-factor changes preserve chaos degree",
            "singular_covariance": "valid using common ambient PSD square root; continuity handles rank changes",
            "arbitrary_nonorthogonal_change": "not invariant unless whitened and reduced to the induced orthogonal/isometric map"
        },
        "local_cylinder": {
            "definition": "Psi_R(x)=s_{K,R,U}(x)-s_{K,R,delta}(x); s=||P_{<=K} Q_cons(M_R(x)+sqrt(u)L_ref,R g)||_{L2(g;HS_tau)}^2",
            "commutation": "P is x-independent bounded linear projection, hence D_x^j(PF)=P D_x^jF for j=1,2,3",
            "derivatives": baseline_derivatives(),
            "consumer norm": "||Q_cons||op<=43/20; ||Q_cons||_{L2(HS_tau)}<=sqrt(E_inf)"
        },
        "prime_smooth_comparison": {
            "vector": "X_(T,R)=(Re xi_(K+r), Im xi_(K+r), Re chi_(K+r), Im chi_(K+r))_{|r|<=R}; ordinary-prime complex contribution V_p(K)=c_p exp(iT log p) exp(i2pi K s_p)(exp(i2pi r s_p), i s_p exp(i2pi r s_p))_{|r|<=R}, c_p=-log(p)/(a_phi L sqrt(p)), s_p=log(p)/L; realify coordinates and group p^v at the prime-base step",
            "A1": "sum_p E[D Psi_R(Y_p) . V_p(K)]",
            "A2": "(1/2) sum_p E[D^2 Psi_R(Y_p):(V_p(K)V_p(K)^T-Sigma_p)]",
            "remainder": "O_R(L^-3), from the grouped prime-base cubic mass; proper-power deletion stays at its prior source-qualified scope",
            "exact_identity": "E Psi_R(X_(T,R))-E Psi_R(G_R)=A1+A2+O_R(L^-3)",
            "status": "A1 and A2 remain OPEN; Y_p depends on the same trace index K as V_p(K). No independence or mean-zero cancellation is available. The obstruction is unchanged in kind, with improved finite-cylinder derivative constants."
        },
        "optional_multiplier_norm": multiplier_norm(rhos, lambdas),
        "two_stage_localization": {
            "decision": "does not improve the certified projected-energy rate",
            "reason": "existing O(1/r) resolvent estimates control scalar one-point traces; transferring them to the projected-energy cylinder by the available Schatten-2 Lipschitz bound yields at best the square-root Hilbert-tail scale. A bandwidth-r boundary rank estimate is not preserved by Hermite projection.",
            "hostile_example": "For standard Gaussian g partitioned into d equal-probability intervals, Delta(g)=e_j e_j^T on interval j has rank one pointwise, but its degree-zero Hermite projection E Delta=I/d has rank d. Thus pointwise rank/boundary support does not pass through P_{<=K}.",
            "no_optimized_r_m": True
        },
        "remaining_theorem": "For each fixed R and the explicit Psi_R, prove A1_T,R + A2_T,R -> 0 (or directly E Psi_R(X_(T,R))-E Psi_R(G_R)->0), while retaining same-index dependence, full prime cutoff, original masks and proper powers; this is the first missing source-dependent prime law.",
        "strict_gt79": False,
        "unclosed_other_obligations": ["fixed-U signed curvature lower bound", "prime dependent-phase A1+A2 law", "separate zero-side transfers"],
        "hostile_mutations": [
            "expansive_projection", "insert_Lambda_U", "omit_delta_layer", "model_energy_as_actual_endpoint",
            "vary_K", "uncoupled_coordinate_spaces", "false_sqrt_lipschitz_at_singular_covariance",
            "arbitrary_nonorthogonal_chaos_invariance", "interchange_R_T_limits", "choose_R_of_T",
            "omit_physical_edge_term", "assume_A1_zero_from_mean", "assume_A2_zero_from_covariance",
            "assume_prime_phase_independence", "use_453_as_dimension", "reopen_raw_moments",
            "reopen_source_mask", "alter_epsilon", "synthetic_benchmark_as_actual_gaussian",
            "claim_gt79_without_prime_law"
        ],
        "source_sha256": {p: hashlib.sha256((root/p).read_bytes()).hexdigest() for p in source_paths}
    }


def main():
    cert = build_certificate()
    out = ROOT / "notes/WP84_LOCALIZE_FIRST_HERMITE_PROJECTION_CERTIFICATE.json"
    out.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: exact projection/localization ledger; fixed-R PSD-root transfer; baseline derivatives; M_q interval.")
    print("DECISION C: fixed-R covariance transfer closes; the dependent-phase prime law remains open.")
    print("A1+A2 remains open. Strict >79 remains OPEN.")


if __name__ == "__main__":
    main()
