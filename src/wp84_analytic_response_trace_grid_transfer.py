"""Exact rational certificate producer for fixed-pole response analyticity.

It proves pointwise Bohr coefficient bounds and fixed signed-contour L2 bounds.
It deliberately does not promote these to a global absolute-frequency weight.
"""
from fractions import Fraction as F
from pathlib import Path
from math import prod
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
START = "59856c2c4f2e5cbf1191f7ea84d3dc8b479a9654"
A = F(131, 200)
THETA = F(1, 2)
K_CHAOS = 32
DELTA = F(1, 100000)


def primes_upto(n):
    out = []
    for k in range(2, n + 1):
        if all(k % d for d in range(2, int(k**0.5) + 1)):
            out.append(k)
    return out


def consumer_constants():
    # Source-certified |q_1|,|q_2|<221/500, |q_3|<317/500.
    qabs = {1: F(221, 500), 2: F(221, 500), 3: F(317, 500)}
    # From the exact Cayley polynomial formula, |z|<3/2 and
    # |eta/delta^3|=(|z|/(2a))^3. The rational p_j bounds below give |q_0|<22.
    pbound = [F(1), F(16, 5), F(14, 5), F(7, 10)]
    prefactor = F(150, 131) ** 3
    bracket = pbound[0] + pbound[1]*F(3,2) + pbound[2]*F(9,4) + pbound[3]*F(27,8)
    q0_upper = prefactor * bracket
    assert q0_upper < 22
    assert F(3142,2415)**2 + A**2 < F(9,4)

    qsum = F(22) + sum(qabs[j] * 5**j for j in range(1,4))
    assert qsum == F(22902,200)
    resolvent = 1 / (A * (1-THETA))
    assert resolvent == F(400,131)
    u_norm = 1 + 2*A*resolvent
    assert u_norm == 5
    # Complexification of the source real input map: 6*sqrt(2)<9.
    # D U and D^2 U bounds at ||R||<=2/a, then compose with map norm 9.
    d1 = F(72,1) / A
    d2 = F(2592,1) / A**2
    q1 = d1 * sum(qabs[j] * j * 5**(j-1) for j in range(1,4))
    q2 = sum(qabs[j] * (
        j * 5**(j-1) * d2
        + j*(j-1)*F(5)**(j-2)*d1**2
    ) for j in range(1,4))
    M1 = 4*qsum*q1
    M2 = 4*(q1**2 + qsum*q2)
    assert M1 < 10**7 and M2 < 10**9
    return {
        "q0_abs_upper": "22",
        "q123_abs_upper": ["221/500", "221/500", "317/500"],
        "Q_sup_upper": str(qsum),
        "complex_input_map_upper": "9",
        "resolvent_norm_upper": str(resolvent),
        "Cayley_U_norm_upper": str(u_norm),
        "D_U_input_norm_upper": str(d1),
        "D2_U_input_norm_upper": str(d2),
        "D_Q_input_norm_upper": str(q1),
        "D2_Q_input_norm_upper": str(q2),
        "M1_R1_upper": str(M1),
        "M2_R2_upper": str(M2),
        "M1_decimal": f"{float(M1):.12e}",
        "M2_decimal": f"{float(M2):.12e}",
        "certified_simple_upper": "M1_R1<10^7; M2_R2<10^9",
        "scope": "fixed R, uniform over Gaussian variables and states in the complex resolvent domain; scalar norm-square is continued by its real-analytic bilinear polarization"
    }


def primorial_family(y):
    qs = [q for q in primes_upto(y) if q != 2]
    X = 2 * prod(qs)
    return qs, X


def source_hashes():
    paths = [
        "notes/WP84_PRIME_BASE_GROUPED_LINDEBERG.md",
        "notes/WP84_LOCALIZE_FIRST_HERMITE_PROJECTION.md",
        "notes/WP84_LOCALIZE_FIRST_HERMITE_PROJECTION_CERTIFICATE.json",
        "notes/WP84_FIXED_R_ARITHMETIC_FILTERED_MOMENT_TRANSFER.md",
        "notes/WP84_COMPILED_MEHLER_PRIME_LINDEBERG.md",
        "notes/WP84_POSITIVE_LAG_GAUSSIAN_VIABILITY_AND_PHASE_RESPONSE.md",
        "notes/WP84_DEPENDENT_PHASE_PRIME_ADIC_FIREWALL.md",
        "notes/WP84_DEPENDENT_PHASE_PRIME_ADIC_FIREWALL_CERTIFICATE.json",
        "src/wp84_dependent_phase_prime_adic_firewall.py",
        "src/wp84_dependent_phase_prime_adic_firewall_replay.py",
    ]
    return {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}


def build():
    cc = consumer_constants()
    qs31, X31 = primorial_family(31)
    s31 = len(qs31)
    assert qs31 == [3,5,7,11,13,17,19,23,29,31]
    assert X31 > 1323*32 and X31 < 2**38
    # e<3 and e^3<21 imply e^7<1323. Since log X<38 and sqrt(38)<7,
    # X exp(-sqrt(log X))>X/e^7>32, so all ten bases are below N.
    assert len(str(X31)) >= 12

    old_eta = F(393,51200)  # L>6, support size two
    old_height_lower = 253891 + 173308  # log 3>1 and log 5>1
    old_gamma_lower = old_eta * old_height_lower
    assert old_gamma_lower > 3279
    old_bounds = {
        f"R1 coefficient <= M1/2^3279": str(F(cc["M1_R1_upper"]) / 2**3279),
        f"R2 coefficient <= M2/2^3279": str(F(cc["M2_R2_upper"]) / 2**3279),
        "certified_decimal_upper": "R1 coefficient<10^-974; R2 coefficient<10^-972, since 2^3279>10^981",
        "reason": "Gamma>3279 and e>2; these are bounds only, not existence claims for the response coefficients"
    }

    return {
        "schema": "wp84-analytic-response-trace-grid-transfer-v1",
        "starting_head": START,
        "branch": "codex/c5-c6-attack-20261006",
        "decision": "C",
        "frozen": {"K": K_CHAOS, "delta": str(DELTA), "a": str(A), "theta": str(THETA), "cutoff": "N=floor(X exp(-sqrt(log X)))", "quantifiers": "fixed R, then T->infinity"},
        "prior_count_reconciliation": {
            "certificate_named_hostile_scenarios": 20,
            "prior_replay_hostile_inference_evidence_checks": 21,
            "distinction": "The replay checks that the evidence rejects invalid inferences; it does not mutate the source files at runtime.",
            "ordinary_rational_arithmetic_assert_statements": 8,
            "source_hash_comparisons": 6,
            "certificate_schema_field_consistency_assertions": 7,
            "corrected_prior_note": "The previous note's 19 count was a typo. The prior replay's 21 describes hostile-inference checks, not named mutation scenarios.",
            "additional_math_correction": "The prior certificate's claimed O(1) direct coefficient l1 bound for A1 was false. The source envelope sum_{p<=N} log(p)/(L sqrt(p)) is asymptotic to 2 sqrt(N)/L by PNT and diverges; this does not prove the signed A1 diverges."
        },
        "source_grouped_block": {
            "one_power_bound": "||B_(q^j)||op <= 4 log(q)/(L q^(j/2))",
            "same_phase": "all q^j use z_q^j from one base z_q",
            "J_q": "max{j>=1:q^j<=N}",
            "complex_radial_difference": "Delta_q(s)=sum_{j<=J_q}[(e^{js}-1)A_(q,j)+(e^{-js}-1)A_(q,-j)]",
            "coefficient_bound": "||A_(q,+/-j)||op <= 4 log(q)/(L q^(j/2)) by Fourier coefficient extraction from the real-phase block",
            "B_q_rho": "8 log(q)/L * sum_{j=1}^{J_q} q^(-j/2)*(exp(j*rho)-1), valid for |s|<=rho"
        },
        "complex_resolvent_domain": {
            "pole": "z=3142/2415 + i*131/200 and conjugate",
            "theta": "1/2",
            "base_hermitian_resolvent": "||R(H,z)||<=1/a",
            "complexified": "||R(H+Delta,z)||<=1/[a(1-theta)]=400/131",
            "proof": "R(H+Delta)=(I+R(H)Delta)^(-1)R(H); ||R(H)Delta||<=theta<1, so Neumann series converges",
            "consumer_bounds": cc,
            "warning": "After complexification the Hermitian 1/a bound is not used; both conjugate pole branches use the Neumann bound."
        },
        "one_variable_fourier": {
            "strip_choice": "rho_q=eta*log(q), 0<eta<=1/4",
            "cost_bound": "B_q(eta log q)<=128*eta/L",
            "proof": "q^(-j(1/2-eta))-q^(-j/2)<=eta*j*log(q)*q^(-j/4); sum_j j q^(-j/4)=q^(-1/4)/(1-q^(-1/4))^2 and (log q)^2 q^(-1/4)/(1-q^(-1/4))^2<=16",
            "single_variable_eventual_strip": "if L>=100, eta=1/4 gives B_q<=32/L<=8/25<131/400=theta*a",
            "coefficient_bound": "||c_(j,p,nu)||_(L2_g, response norm) <= M_(j,R)*exp(-rho_q*|nu_q|), j=1,2; other torus variables remain on unit circles",
            "M1_R": cc["M1_R1_upper"],
            "M2_R": cc["M2_R2_upper"]
        },
        "multi_index_optimization": {
            "feasible_constraint": "sum_(q in S) B_q(rho_q)<=theta*a",
            "Gamma_definition": "sup_{rho_q>=0, sum B_q(rho_q)<=theta*a} sum_(q in S)|nu_q|rho_q",
            "exact_optimizer": "For nonzero nu_q, the unique optimizer satisfies |nu_q|=mu*B_q'(rho_q), sum B_q(rho_q)=theta*a, mu>0; B_q is strictly convex and increasing.",
            "B_q_prime": "8 log(q)/L * sum_{j<=J_q} j*q^(-j/2)*exp(j*rho)",
            "height": "h(nu)=sum_q |nu_q| log(q)",
            "rigorous_lower_bound": "Gamma_T(nu)>=eta_T(S)*h(nu), eta_T(S)=min(1/4,131*L/(51200*|S|))",
            "support_condition": "This bound is valid for every finite support S subset of the retained primes; it uses a simultaneous perturbation budget, not a product of separate strips.",
            "proof_cost": "At rho_q=eta log(q), B_q<=128 eta/L, so the total is <=128 eta |S|/L<=131/400.",
            "global_weight_caveat": "Gamma pointwise Cauchy does not itself prove sum_nu exp(2 Gamma_T(nu)) E||c_nu||^2<infinity."
        },
        "old_adversarial_atom": {
            "p": 2,
            "r": 1,
            "prior_l2_only_lemma": "FALSE for L2 coefficient control alone",
            "response_character": "z_3^253891 z_5^-173308",
            "T": 7800,
            "frequency_interval": ["1286529/1000000000000", "1286530/1000000000000"],
            "support_size": 2,
            "Gamma_lower": str(old_gamma_lower),
            "R1_coefficient_upper": old_bounds["R1 coefficient <= M1/2^3279"],
            "R2_coefficient_upper": old_bounds["R2 coefficient <= M2/2^3279"],
            "certified_decimal_upper": old_bounds["certified_decimal_upper"],
            "interpretation": "Analyticity crushes this hypothetical coefficient. No claim that it occurs in the actual response."
        },
        "many_small_exponent_exact_alias": {
            "family": "For y>=3, X_y=2*product_{3<=q<=y, q prime} q; T_y=2*pi*X_y; p=2,r=1, nu_q=+1 on every odd prime q<=y.",
            "alias": "lambda_nu+log(2)=log(X_y)=L_y; exact m=1 periodic alias.",
            "exponent_bound": "max_q |nu_q|=1",
            "explicit_y": 31,
            "explicit_support_primes": qs31,
            "explicit_support_size": s31,
            "explicit_X": str(X31),
            "explicit_cutoff_check": "X_31>1323*32 and X_31<2^38; e<3, e^3<21 imply e^7<1323, log(X_31)<38, hence X_31 exp(-sqrt(log X_31))>32 and N_31>=32.",
            "asymptotic_cutoff": "PNT gives L_y=log X_y~y and log N_y=L_y-sqrt(L_y)+o(1)~y, so all q<=y are retained for large y.",
            "Gamma": "Gamma_T(nu)>=min(1/4,131*L_y/(51200*(pi(y)-1)))*(L_y-log 2); since (pi(y)-1)/L_y->0, Gamma>= (L_y-log 2)/4 eventually.",
            "coefficient_status": "The kernel is exactly modulus one, but any actual response coefficient at this index is bounded by M_j,R*exp(-Gamma). Its existence and the sum over the full alias family are not inferred."
        },
        "valid_weighted_l2": {
            "statement": "For every fixed finite signed shift vector s with sum_q B_q(|s_q|)<=theta*a, sum_nu exp(2*sum_q s_q*nu_q) E_g||c_(j,p,nu,g)||^2 <= M_(j,R)^2, j=1,2.",
            "proof": "Shift the selected finite torus coordinates to z_q=exp(i theta_q+s_q), apply Parseval on that shifted torus, and use the uniform response bound M_(j,R).",
            "not_proved": "No single global weight exp(2*Gamma_T(nu)) has a proved finite weighted l2 norm. Splitting by all sign orthants costs 2^|S| and does not yield a useful uniform bound when the retained prime support grows."
        },
        "A1_weighted_dual_mass": {
            "exact_source_form": "sum_p sum_{a>=1} sum_{epsilon=+/-} gamma_(p,a,epsilon) sum_nu <c1_(p,nu),.> K_I(lambda_nu+epsilon*a*log(p)); current coefficients retain masks, carrier and proper powers.",
            "valid_fixed_contour_bound": "For each fixed feasible signed contour and each sign orthant, Cauchy gives M1_R times [sum_{nu in orthant}|K_I(lambda_nu+epsilon*a log p)|^2 exp(-2 sum_q rho_q|nu_q|)]^(1/2), multiplied by |gamma_(p,a)|.",
            "status": "OPEN after summing over p, a, all sign orthants, masks and aliases; no o(1) bound."
        },
        "A2_weighted_dual_mass": {
            "exact_source_form": "(1/2)sum_p sum_{a,b,epsilon,epsilon'}' gamma_(p,a,epsilon)gamma_(p,b,epsilon') sum_nu c2_(p,nu)[.] K_I(lambda_nu+(epsilon*a+epsilon'*b)log(p)); prime denotes removal of opposite equal powers by Sigma_p.",
            "valid_fixed_contour_bound": "For each feasible signed contour and sign orthant, Cauchy uses M2_R and the corresponding squared-kernel sum; multiply by |gamma_(p,a)gamma_(p,b)|/2.",
            "status": "OPEN after p,a,b and all aliases are summed."
        },
        "alias_split": {
            "m0": "exact current-base resonance impossible for nonzero current p-adic exponent r by unique factorization; covariance diagonal already removed in A2",
            "m_nonzero": "not excluded. The explicit primorial family is an exact m=1 alias; its individual coefficient upper bound decays, but total family mass is not bounded.",
            "near": "the kernel can have modulus 1 in the O(1/T) window; analytic pointwise decay is available but no count/weighted-l2 summation theorem closes the full family",
            "far": "use |K_I(omega)|<=min(1,C/[T dist(omega,L Z)]); no source-matched aggregate estimate after response expansion is proved"
        },
        "low_degree_reuse": {
            "closed_existing_degree_1_2": ["exact grouped covariance diagonal", "ordinary unweighted covariance normalization in its previously proved scope"],
            "closed_new_analytic_weight": ["individual high-height response coefficient bounds from Gamma"],
            "still_open": ["p-excluded response coefficients paired with the trace grid, including the multi-support alias family; generic degree-1/2 transfer does not apply to the unbounded response degree"]
        },
        "signed_cancellation_audit": {
            "conjugation": "pairs conjugates into 2*Re(term); not identically zero",
            "current_power_pairing": "only equal opposite powers are exact and are subtracted; other pairings retain p-adic frequencies",
            "translation_or_carrier": "common K path and carrier phases remain in K_I; no exact sign reversal identity found",
            "U_minus_delta": "Psi is a difference, but no fixed sign or exact cancellation identity for A1/A2 is established"
        },
        "consistency": "Even if this one fixed-R cylinder comparison closed, it would establish only E Psi_R(X)-E Psi_R(G) for the selected bounded cylinder; it would not imply full-vector Gaussian convergence or settle prior fifth-moment/nonexact-correlation audits.",
        "first_remaining_theorem": "For each fixed R prove a source-matched p-summed signed or weighted-l2 estimate for A1 and A2 on the common trace-index path, with the actual response coefficients, the exact grouped current weights, all sign orthants, near aliases, and m!=0 periodic aliases. Fixed-contour Parseval and pointwise Cauchy decay alone do not imply the required total o(1).",
        "dependent_phase_law": "OPEN",
        "strict_gt79": "OPEN",
        "prior_source_hashes": source_hashes()
    }


def main():
    obj = build()
    out = ROOT / "notes/WP84_ANALYTIC_RESPONSE_TRACE_GRID_TRANSFER_CERTIFICATE.json"
    out.write_text(json.dumps(obj, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: rational resolvent strip, simultaneous-support budget, Cauchy and fixed-contour Parseval bounds.")
    print("OPEN: aggregate A1/A2 weighted trace-grid mass; decision C; strict >79 remains OPEN.")


if __name__ == "__main__":
    main()
