"""Produce exact finite certificates for the WP84 contour-mixture reduction.

This records the measure-mixture Hilbert lemma, the grouped current-prime
mass hierarchy, and the remaining source-weighted A1/A2 dual-mass obligations.
It deliberately does not claim that the open dual masses are small.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
START = "90af6336111e822e67df4eabaa534fbb78fd9360"
A = F(131, 200)
THETA = F(1, 2)


def source_hashes():
    paths = [
        "notes/WP84_ANALYTIC_RESPONSE_TRACE_GRID_TRANSFER.md",
        "notes/WP84_ANALYTIC_RESPONSE_TRACE_GRID_TRANSFER_CERTIFICATE.json",
        "src/wp84_analytic_response_trace_grid_transfer.py",
        "src/wp84_analytic_response_trace_grid_transfer_replay.py",
        "notes/WP84_DEPENDENT_PHASE_PRIME_ADIC_FIREWALL.md",
        "notes/WP84_DEPENDENT_PHASE_PRIME_ADIC_FIREWALL_CERTIFICATE.json",
        "src/wp84_dependent_phase_prime_adic_firewall.py",
        "src/wp84_dependent_phase_prime_adic_firewall_replay.py",
        "notes/WP84_PRIME_BASE_GROUPED_LINDEBERG.md",
    ]
    return {p: hashlib.sha256((ROOT / p).read_bytes()).hexdigest() for p in paths}


def build():
    # With g_p=4 log(p)/(L(sqrt(p)-1)), the PNT leading term in sum g_p^2 is 8.
    # The O(1) errors in sum log^2(p)/p are killed by L^-2.
    return {
        "schema": "wp84-contour-mixture-prime-mass-v1",
        "starting_head": START,
        "branch": "codex/c5-c6-attack-20261006",
        "decision": "C",
        "frozen": {
            "K": 32,
            "delta": "1/100000",
            "a": str(A),
            "theta": str(THETA),
            "cutoff": "N=floor(X*exp(-sqrt(log X)))",
            "quantifiers": "fixed R followed by T->infinity",
            "notebooklm_packet": "read-only; untouched",
        },
        "contour_mixture": {
            "finite_statement": "For each feasible s, sum_{nu in F} exp(2*s.dot(nu))*||c_nu||^2<=M^2. Integrate any probability measure mu on the feasible contour body: sum_{nu in F} W_mu(nu)||c_nu||^2<=M^2, W_mu=integral exp(2*s.dot(nu)) dmu(s).",
            "infinite_statement": "For increasing finite Fourier sets exhausting the countable index set, monotone convergence for nonnegative terms gives sum_nu W_mu(nu)||c_nu||^2<=M^2.",
            "sign_mixture": "Independent uniform signs on a fixed nonnegative feasible radius vector rho give W_rho(nu)=product_q cosh(2*rho_q*nu_q).",
            "pointwise_lower_bound": "W_rho(nu)>=2^(-|supp(nu)|)*exp(2*sum_q rho_q*abs(nu_q)); equality factor 1/2 per nonzero coordinate is sharp as |2*rho_q*nu_q| tends to infinity.",
            "caveat": "Probability averaging costs no factor on the Parseval right side, but the pointwise lower bound retains a support-size factor in reciprocal dual masses.",
            "finite_truncation_duality": "|sum_{nu in F}<c_nu,k_nu>|<=M*sqrt(sum_{nu in F}||k_nu||^2/W_mu(nu)).",
            "optimization": {
                "objective": "D_mu(k)=sum_{nu in F}||k_nu||^2/W_mu(nu)",
                "convexity": "W_mu(nu) is affine and positive in mu; x->1/x is convex on x>0, hence D_mu is convex in mu.",
                "existence": "For finitely many active coordinates, the feasible contour body is compact and W_mu(nu) is bounded away from zero; a minimizing probability measure exists.",
                "finite_support": "If |F|=n, the vector (W_mu(nu))_{nu in F} lies in the convex hull of the compact feature set s->(exp(2*s.dot(nu)))_nu. Caratheodory gives a measure on at most n+1 feasible contours with the same objective value.",
                "warning": "This is one common measure for the whole finite truncation. It does not permit selecting a different optimizer separately for each nu.",
                "numerical_optimizer": "None used; no numerical optimum is asserted."
            }
        },
        "current_prime_mass": {
            "source_block_bound": "||B_(p^a)||<=4*log(p)/(L*p^(a/2)), including source vector/operator factors and the complete retained path block.",
            "envelope": "g_p=4*log(p)/(L*(sqrt(p)-1)); ||V_p||<=g_p by summing every retained power and enlarging to the infinite geometric series.",
            "max_mass": "max_p g_p<=4*log(2)/(L*(sqrt(2)-1))=O(L^-1); x->log(x)/(sqrt(x)-1) decreases for x>=2.",
            "square_mass": "sum_{p<=N} g_p^2 = (16/L^2)*sum_{p<=N} log^2(p)/(sqrt(p)-1)^2 = 8+o(1), hence O(1). Here (sqrt(p)-1)^(-2)=p^(-1)*(1+O(p^(-1/2))) and PNT gives sum_{p<=N}log^2(p)/p~(log N)^2/2, log N~L.",
            "cube_mass": "sum_{p<=N}g_p^3<=64*L^-3*sum_p log^3(p)/(sqrt(p)-1)^3=O(L^-3); the prime series converges.",
            "fourth_mass": "sum_{p<=N}g_p^4<=256*L^-4*sum_p log^4(p)/(sqrt(p)-1)^4=O(L^-4); the prime series converges.",
            "normalization_caveat": "This uses the exact source block envelope 4 log(p)/(L p^(a/2)); it is not the scalar coefficient envelope log(p)/(L sqrt(p)) with an omitted path/operator factor."
        },
        "A1": {
            "exact_grouped_kernel_definition": "For each p,nu, K1_(p,nu)=(1/d')*sum_{k in I} exp(i*tau_k*lambda_nu)*sum_{a:p^a<=N,epsilon=+/-} Gamma_(p,a,epsilon;k)*exp(i*tau_k*epsilon*a*log(p)), tau_k=T+2*pi*k/L. Gamma is the actual realified source coefficient tensor with masks, lag/root/path factors and any k-dependent source gates; it excludes this displayed trace carrier, which occurs exactly once. Conjugates are included exactly once. All current powers/signs are combined at fixed p,nu before norming.",
            "direct_sum_pairing": "A1=sum_p sum_nu <c1_(p,nu),K1_(p,nu)> after the exact source tensor contraction.",
            "mixture_bound": "For feasible mu_p separately for each p, |A1|^2<=M1_R^2*(sum_p g_p^2)*D1_T, D1_T=sum_{p,nu}||K1_(p,nu)||^2/(g_p^2*W_(p,mu_p)(nu)).",
            "target": "D1_T=o(1).",
            "status": "OPEN: no source-matched estimate of this full dual mass is available; contour averaging alone does not control the aliases or the p-sum."
        },
        "A2": {
            "exact_grouped_kernel_definition": "For each p,nu, K2_(p,nu)=(1/d')*sum_{k in I} exp(i*tau_k*lambda_nu)*sum_{a,b:p^a,p^b<=N,epsilon,epsilon'}' [Gamma_(p,a,epsilon;k) tensor Gamma_(p,b,epsilon';k)]*exp(i*tau_k*(epsilon*a+epsilon'*b)*log(p)), tau_k=T+2*pi*k/L. Each Gamma contains the actual realified mask/lag/root/path coefficient and any k-dependent gates but excludes the displayed carrier, so every carrier occurs once. The prime removes only epsilon'=-epsilon and a=b, exactly the Sigma_p diagonal; retain all other pairs.",
            "normalization": "A2=(1/2)*sum_p sum_nu <c2_(p,nu),K2_(p,nu)> with K2 defined before the 1/2 factor.",
            "mixture_bound": "|A2|^2<= (1/4)*M2_R^2*(sum_p g_p^4)*D2_T, D2_T=sum_{p,nu}||K2_(p,nu)||^2/(g_p^4*W_(p,mu_p)(nu)).",
            "target": "D2_T=o(L^4), not merely an unspecified polynomial bound.",
            "status": "OPEN: fourth prime mass improves the sufficient target, but the full residual dual mass is not bounded."
        },
        "alias_falsification": {
            "m_zero": "For current exponent r!=0, p-adic valuation excludes lambda_nu+r*log(p)=0 by unique factorization.",
            "periodic": "lambda_nu+r*log(p)=mL with m!=0 is possible; the retained primorial example is an admissible exact frequency label, not evidence its source coefficient is nonzero.",
            "near": "The sampled geometric kernel can be order one within O(1/T) of mL; contour weight suppresses a high-height coefficient but no total count/dual-mass estimate is proved.",
            "intermediate_far": "The geometric kernel decay applies pointwise, but summing it against all actual response coefficients, paths, masks and p weights remains open.",
            "primorial_test": {
                "family": "p=2,r=1, X_y=2*product_{3<=q<=y prime}q, nu_q=1 on odd primes q<=y, so lambda_nu+log(2)=log(X_y)=L_y.",
                "no_contour": "W=1 for this individual label.",
                "one_contour": "For rho_q=(log q)/4, feasible once 32|S_y|/L_y<=131/400; this holds eventually because |S_y|/L_y~1/log y.",
                "random_sign": "W=product_{q in S_y}cosh((log q)/2), exactly.",
                "lower_bound": "W>=2^(-|S_y|)*exp((1/2)*sum_{q in S_y}log q)=2^(-|S_y|)*(X_y/2)^(1/2).",
                "optimized_single_label_mixture": "For this positive index, minimize the one-label dual term by maximizing 2*sum_q rho_q subject to sum B_q(rho_q)<=131/400. The unique optimizer has active set A: 1=mu*B_q'(rho_q) for q in A; inactive q have rho_q=0 and 1<=mu*B_q'(0); sum B_q(rho_q)=131/400. The point mass at that single feasible contour is an explicit common measure for this one-label truncation. This is not a common optimizer for other labels.",
                "optimized_weight": "W_opt=exp(2*sum_{q in S_y}rho_q^*) with rho_q^* defined by the preceding finite strictly-convex KKT system; no decimal optimizer is claimed.",
                "interpretation": "The exact alias kernel factor is one; under this mixture its individual reciprocal weight decays exponentially in L_y. This is a single-label statement and does not bound the full alias family or prove a nonzero response coefficient."
            }
        },
        "radius_schedule_tests": {
            "uniform_log_radius": "rho_p=eta*log(p), eta=min(1/4,131*L/(51200*s)) on an index support of size s; certified total perturbation cost <=131/400. Useful for sparse/primorial supports, not all primes simultaneously with eta=1/4.",
            "power_decay": "rho_p=c*p^(-alpha), alpha>1/2 and fixed c<=1/4: B_p(rho_p)<=C*c*log(p)/(L*p^(1/2+alpha)); the prime sum converges, so total cost O_c(1/L), but height gained is only c*sum |nu_p|*log(p)*p^(-alpha).",
            "log_weighted_power_decay": "rho_p=c/(sqrt(p)*log(p)^beta), beta>1: linearized cost is O(c/L)*sum_p 1/(p*log(p)^(beta-1)), convergent by PNT; high-prime height weight is weaker still.",
            "prime_square_mass": "rho_p=c*log(p)/(L*sqrt(p)); linearized total cost is O(c/L^2)*sum_{p<=N}log^2(p)/p=O(c), so choose c from the exact B_p sum before use. This schedule gives only the influence-weighted height.",
            "logarithmic_shells": "For a finite shell P_j, rho_p=eta_j*log(p), with sum_j 128*eta_j*|P_j|/L<=131/400; each shell budget is explicit, but summing the dual masses over all shell supports remains unproved.",
            "conclusion": "These feasible schedules establish contour admissibility only. None proves D1=o(1) or D2=o(L^4) without an estimate for the actual kernel sums and growing-support multiplicities."
        },
        "decision": "C",
        "first_unproved_lemma": "Prove D1_T=o(1) and D2_T=o(L^4) for the exact source-contracted grouped kernels, uniformly over the selected section and fixed R, including all nonzero periodic, near, intermediate and far aliases; no such source-matched total estimate is presently proved.",
        "strict_gt79": "OPEN",
        "source_sha256": source_hashes()
    }


def main():
    out = ROOT / "notes/WP84_CONTOUR_MIXTURE_PRIME_MASS_CERTIFICATE.json"
    out.write_text(json.dumps(build(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS: exact mixture, support penalty, convex finite-truncation reduction and prime-mass formulas recorded.")
    print("OPEN: A1 dual mass D1=o(1), A2 dual mass D2=o(L^4); strict >79 remains OPEN.")


if __name__ == "__main__":
    main()
