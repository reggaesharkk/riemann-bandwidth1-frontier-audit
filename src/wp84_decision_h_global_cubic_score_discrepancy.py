#!/usr/bin/env python3
"""Deterministic Decision-H certificate producer.

The analytic inequalities are proved in the accompanying note.  This script
records their exact hypotheses/scales and runs a rational finite-matrix check
of the cubic-diagonal and trace-normalization identities.  It does not estimate
the unresolved natural-cutoff prime correlations.
"""
from __future__ import annotations

import json
from fractions import Fraction as Q
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificates" / "WP84_DECISION_H_GLOBAL_CUBIC_SCORE_DISCREPANCY_CERTIFICATE.json"


def matmul(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), Q(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def trace(a):
    return sum((a[i][i] for i in range(len(a))), Q(0))


def cube(a):
    return matmul(matmul(a, a), a)


def submatrix(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def transpose(a):
    return [list(x) for x in zip(*a)]


def cubic_diagonal_formula(h, diagonal, w):
    n = len(h)
    out = []
    for k in range(n):
        value = diagonal[k] ** 3
        value += sum(((2 * diagonal[k] + diagonal[j]) * w[k][j] ** 2
                      for j in range(n) if j != k), Q(0))
        value += sum((w[k][j] * w[j][ell] * w[ell][k]
                      for j in range(n) for ell in range(n)
                      if len({k, j, ell}) == 3), Q(0))
        out.append(value)
    return out


def exact_regression():
    avals = [Q(0), Q(2), Q(-1), Q(3), Q(4), Q(-2)]
    beta = [Q(1), Q(-2), Q(0), Q(3), Q(-1), Q(2)]
    s0 = Q(2, 5)
    diagonal = [s0 + x for x in beta]
    n = len(avals)
    # The common 1/pi factor is suppressed for this polynomial identity test.
    w = [[Q(0) if i == j else (avals[i] - avals[j]) / (j - i)
          for j in range(n)] for i in range(n)]
    h = [[(diagonal[i] if i == j else Q(0)) + w[i][j]
          for j in range(n)] for i in range(n)]
    h3 = cube(h)
    g_direct = [h3[k][k] for k in range(n)]
    g_formula = cubic_diagonal_formula(h, diagonal, w)
    assert g_direct == g_formula

    p, q = [1, 2, 3, 4], [0, 5]
    a, b, d = submatrix(h, p, p), submatrix(h, p, q), submatrix(h, q, q)
    bt, bb, btb = transpose(b), matmul(b, transpose(b)), matmul(transpose(b), b)
    full_dim, retained_dim = n, len(p)
    mt = trace(h3) / full_dim
    lhs = trace(h3) / full_dim - trace(cube(a)) / retained_dim
    score = sum((g_direct[k] - mt for k in q), Q(0)) / retained_dim
    mixed = (2 * trace(matmul(a, bb)) + trace(matmul(d, btb))) / retained_dim
    assert lhs == score + mixed
    assert trace(submatrix(h3, p, p)) != trace(cube(a))

    # Hostile mutations: a wrong diagonal coefficient and omitted 3-cycle fail.
    wrong_coeff = []
    for k in range(n):
        v = diagonal[k] ** 3
        v += sum(((diagonal[k] + diagonal[j]) * w[k][j] ** 2
                  for j in range(n) if j != k), Q(0))
        v += sum((w[k][j] * w[j][ell] * w[ell][k]
                  for j in range(n) for ell in range(n)
                  if len({k, j, ell}) == 3), Q(0))
        wrong_coeff.append(v)
    assert wrong_coeff != g_direct
    no_cycles = []
    for k in range(n):
        no_cycles.append(diagonal[k] ** 3 + sum(
            ((2 * diagonal[k] + diagonal[j]) * w[k][j] ** 2
             for j in range(n) if j != k), Q(0)))
    assert no_cycles != g_direct

    # Exact abstract global-spike check, not a prime-source example.
    big = 64  # dimensions q^3 make the selected eigenvalue integral
    height = 4
    spike = [[Q(height) if i == j == big - 1 else Q(0)
              for j in range(big)] for i in range(big)]
    spike3 = cube(spike)
    spike_m = trace(spike3) / big
    endpoint_window = list(range(4))
    endpoint_score_sq = sum(((spike3[k][k] - spike_m) ** 2
                             for k in endpoint_window), Q(0))
    assert endpoint_score_sq == Q(4)
    assert trace(cube(spike)) / big == 1
    assert trace(cube(submatrix(spike, list(range(big - 1)),
                                list(range(big - 1))))) == 0
    deleted_score = (spike3[big - 1][big - 1] - spike_m) / (big - 1)
    assert deleted_score == 1

    return {
        "dimension": n,
        "g_diagonal": [str(x) for x in g_direct],
        "trace_identity_lhs": str(lhs),
        "trace_identity_score_term": str(score),
        "trace_identity_mixed_term": str(mixed),
        "wrong_2a_plus_aj_mutation_rejected": True,
        "omitted_three_cycle_mutation_rejected": True,
        "PH3P_distinguished_from_PHP_cubed": True,
        "abstract_interior_spike_endpoint_centered_square_mass": str(endpoint_score_sq),
        "abstract_deleted_row_spike_normalized_discrepancy": str(deleted_score),
    }


def main():
    finite = exact_regression()
    cert = {
        "title": "WP84 Decision H: global cubic-score discrepancy",
        "classification": "H2 — a source-derived localized cubic-score square bound is proved, but its natural-cutoff majorant does not reach the discrepancy threshold",
        "start_state": {
            "branch": "codex/c5-c6-attack-20261006",
            "head": "13e87db74bd273349dc6db94aeb2e38e95a34fe7",
            "preexisting_untracked": ["notebooklm_packet/"],
            "push": "NO",
            "merge": "NO",
            "notebooklm_packet": "untouched",
        },
        "source": {
            "scale": "X=T/(2*pi), L=log(X), N=floor(X*exp(-sqrt(L))), d=floor(T*L/(2*pi)), M=ceil(d*exp(-sqrt(L)/2))",
            "pool": "P(N)={p^v:p prime,v>=1,p^v<=N}; all proper powers retained",
            "coefficients": "c_n=-Lambda(n)/(a_phi(T)*L*sqrt(n)); z_n=c_n*exp(i*T*log(n)); alpha_n=log(n)/L",
            "fields": "A_k=sum_n Im(z_n exp(2*pi*i*k*alpha_n)); beta_k=sum_n 2*(1-alpha_n) Re(z_n exp(2*pi*i*k*alpha_n))",
            "matrix": "H=s0*I+diag(beta)+[diag(A),J], J_ij=1/(pi*(j-i)) for i!=j, J_ii=0",
            "operator": "||H||op<=K_T=|s0|+4*S, S=sum_{n in P(N)}|c_n|=O(sqrt(N)/L); s0->1 and a_phi->1",
            "section": "I0=[b,b+d-1]; I_uv=[b+u,b+d-1-v], 0<=u,v<=M; Q=QL union QR, d'=d-u-v>=d-2M",
            "large_sieve": "uniform translated interval J of integer length h: sum_J A_k^2=O(h+NL), sum_J beta_k^2=O(h+NL), with all prime powers and actual carrier phases",
        },
        "exact_identities": {
            "global_score": "tau_d(H^3)-tau_d'(A^3)=[sum_{k in Q}(g_k-m_T)]/d' + [2Tr(A B B*)+Tr(D B* B)]/d', where g_k=(H^3)_kk, m_T=Tr(H^3)/d, A=PHP, B=PHQ, D=QHQ",
            "mixed_bound": "|2Tr(A B B*)+Tr(D B* B)|<=3*K_T*E(I), E(I)=||B||_HS^2",
            "diagonal_score": "g_k=a_k^3+sum_{j!=k}(2*a_k+a_j)W_kj^2+sum_{j,l pairwise distinct from k and each other}W_kj*W_jl*W_lk; a=s0+beta; W_ij=(A_i-A_j)/(pi*(j-i))",
            "endpoint_split": "sum_Q(g_k-m_T)=Y_L(u)+Y_R(v), with Y_L=sum_{k=b}^{b+u-1}(g_k-m_T), Y_R=sum_{k=b+d-v}^{b+d-1}(g_k-m_T)",
            "pair_average": "E_uv|tau_d(H^3)-tau_d'(A^3)| <= (E_u|Y_L|+E_v|Y_R|)/(d-2M) + 3*K_T*C_B*log(d)/(d-2M)",
        },
        "prime_expansion": {
            "u": "u_{n,sigma}(x)=c_n*exp(i*sigma*(T*log(n)+2*pi*x*alpha_n)), sigma in {-1,+1}",
            "fields": "beta_x=sum_n(1-alpha_n)*sum_sigma u_{n,sigma}(x); A_x=(1/(2i))*sum_n sum_sigma sigma*u_{n,sigma}(x)",
            "diagonal": "a_k^3=s0^3+3*s0^2*beta_k+3*s0*beta_k^2+beta_k^3; beta_k^3 is the complete finite signed triple sum over P(N)^3 and sigma^3",
            "pair_kernel": "(2*a_k+a_j)W_kj^2=[3*s0+2*beta_k+beta_j]*(A_k-A_j)^2/(pi^2*(j-k)^2), all j in I0",
            "cycles": "ordered j,l in I0, pairwise distinct with k and each other; product (A_k-A_j)(A_j-A_l)(A_l-A_k)/(pi^3*(j-k)*(l-j)*(k-l))",
            "resonance": "for three prime powers, zero carrier requires a 2-vs-1 equality; unique factorization forces same prime base and exponents add (e.g. 2*4=8). All-plus/all-minus cannot close. Nonzero and near aliases are retained.",
            "sampling": "for each expanded term, after fixing other indices, the varying endpoint index has exact frequency omega equal to the signed sum of alpha factors attached to that index; sum_{k=k0}^{k0+u-1} exp(2*pi*i*k*omega) has magnitude u if omega is integer and otherwise <=min(u,1/|sin(pi*omega)|). Carrier exp(i*T*Omega) remains separate.",
            "boundary_scope": "No infinite-lattice replacement or finite-boundary uniform transfer is used.",
        },
        "localized_score_bound": {
            "q": "q_k=(H^2)_kk=||H e_k||_2^2=a_k^2+sum_{j in I0,j!=k}W_kj^2",
            "endpoint_q_mass": "uniformly for either endpoint window J of length M, sum_J q_k=O(M+NL), by local large sieve and dyadic control of sum_{j in I0} A_j^2*sum_{k in J}(j-k)^(-2)",
            "global_second_trace": "Tr(H^2)=O(d+NL)=O(d), from the same source large sieve on I0 and summability of |j-k|^-2",
            "mean_bound": "|m_T|<=K_T*Tr(H^2)/d=O(K_T); no value or sign is assigned",
            "score_square": "sum_J|g_k-m_T|^2=O(K_T^4*(M+NL)+M*K_T^2), since |g_k|<=K_T*q_k and q_k<=K_T^2",
            "cauchy_sufficient_condition": "if S2=sum_{J_L union J_R}|g_k-m_T|^2=o(d^2/M), then (E|Y_L|+E|Y_R|)/(d-2M)=o(1)",
            "uniform_S6_relation": "uniform tau_d(|H|^6)=O(1) implies the endpoint S2 condition; the endpoint-only condition is strictly weaker (an abstract interior diagonal spike violates global S6 while preserving endpoint S2)",
            "natural_cutoff_ratio": "the proved upper majorant divided by d^2/M is O((K_T^4+K_T^2)*(M/d)^2)=O((1+N^2/L^4+N/L^2)*exp(-sqrt(L))); its leading displayed envelope is exp(2L-3sqrt(L))/L^4 and diverges",
            "conclusion": "This local estimate is rigorous but does not certify the required little-o condition; divergence of the majorant is not a lower bound or a source counterexample.",
        },
        "direct_route": {
            "absolute_majorant": "E_u|Y_L|+E_v|Y_R|=O(K_T*(M+NL)); normalized bound O(K_T*M/d) when M>>NL",
            "natural_scale": "K_T*M/d=O((1+sqrt(N)/L)*exp(-sqrt(L)/2)); its leading envelope is exp(L/2-sqrt(L))/L and diverges",
            "signed_mean_warning": "control of a signed mean does not bound the mean absolute partial sum",
        },
        "decision_gate": {
            "mixed_remainder": "3*K_T*C_B*log(d)/(d-2M)=O(C_B/T + C_B*exp(-sqrt(L)/2)/(sqrt(T)*L))=o(1)",
            "endpoint_discrepancy": "unproved: (E_u|Y_L|+E_v|Y_R|)/(d-2M)=o(1)",
            "same_section": "if endpoint discrepancy=o(1), Markov gives an intersection of D2-admissible density >=1/4, energy-good density >=7/8, and score-good density 1-o(1); this applies only to the direct first-strike consumer",
            "first_missing_estimate": "a source-matched centered endpoint partial-sum bound for g_k=(H^3)_kk on the two length-M windows, strong enough that E|Y_L|+E|Y_R|=o(d)",
            "theorem_status": "strict >79%, m3=2, conditioned Cayley energy <0.105, signed fifth/sixth gate, prime-to-Weil, zero-side, and determinant compatibility remain OPEN",
        },
        "finite_exact_replay": finite,
        "prerequisite_replays": [
            "wp84_adaptive_boundary_large_sieve_replay.py PASS",
            "wp84_decision_c_same_section_compatibility_replay.py PASS",
            "wp84_decision_d_endpoint_admissibility_replay.py PASS",
            "wp84_decision_e_prime_source_cubic_deletion_replay.py PASS",
            "wp84_decision_f_exact_signed_deleted_block_cubic_replay.py PASS",
            "wp84_decision_g_one_sided_cubic_localization.py PASS",
            "wp84_decision_g_one_sided_cubic_localization_replay.py PASS",
        ],
        "scope": "Finite rational checks verify algebra only. The local large-sieve consequences use their inherited analytic hypotheses. No source-valid cubic discrepancy estimate or >79 theorem is claimed.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS exact full-score trace identity and cubic diagonal formula")
    print("BOUND source-localized score square mass O(K_T^4*(M+NL)+M*K_T^2)")
    print("OPEN endpoint Cauchy threshold S2=o(d^2/M); available natural-cutoff majorant does not reach it")
    print("DECISION H2; strict >79 OPEN")
    print("WROTE", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
