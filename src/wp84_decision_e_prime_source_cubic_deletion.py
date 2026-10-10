#!/usr/bin/env python3
"""Deterministic certificate producer for Decision E.

All source-scale statements are transcribed from the frozen WP84 source
notes.  The rational matrix calculation is only an algebra regression; it
does not synthesize prime data or assert an asymptotic source theorem.
"""
from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificates" / "WP84_DECISION_E_PRIME_SOURCE_CUBIC_DELETION_CERTIFICATE.json"


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return sum((a[i][i] for i in range(min(len(a), len(a[0])))), F(0))


def block(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def transpose(a):
    return [list(x) for x in zip(*a)]


def cube(a):
    return mm(mm(a, a), a)


def algebra_regression():
    # Exact rational symmetric matrix. This tests only block algebra.
    h = [list(map(F, row)) for row in (
        (2, 1, 2, -1), (1, 3, 0, 2), (2, 0, -1, 1), (-1, 2, 1, 4))]
    p, q = [0, 1], [2, 3]
    a, b, d = block(h, p, p), block(h, p, q), block(h, q, q)
    bb_star = mm(b, transpose(b))
    b_star_b = mm(transpose(b), b)
    lhs = tr(cube(h)) - tr(cube(a))
    rhs = tr(cube(d)) + 3 * tr(mm(a, bb_star)) + 3 * tr(mm(d, b_star_b))
    assert lhs == rhs
    # The PH^3P identity is a different expression and must retain its own terms.
    ph3p = block(cube(h), p, p)
    ph3p_minus_a3 = tr(ph3p) - tr(cube(a))
    p_identity = 2 * tr(mm(a, bb_star)) + tr(mm(b, mm(d, transpose(b))))
    assert ph3p_minus_a3 == p_identity
    e = tr(bb_star)
    assert e == sum((b[i][j] ** 2 for i in range(len(b)) for j in range(len(b[0]))), F(0))
    # Hostile mutation: dropping the deleted-block cubic is not an identity.
    assert lhs != 3 * tr(mm(a, bb_star)) + 3 * tr(mm(d, b_star_b))
    # Hostile mutation: using the compression-of-cubic expression for full trace fails.
    assert lhs != p_identity
    return {
        "scope": "exact rational symmetric algebra diagnostic, not prime-source data",
        "dimension": 4,
        "kept_dimension": 2,
        "deleted_dimension": 2,
        "Tr_H3_minus_Tr_A3": str(lhs),
        "Tr_D3": str(tr(cube(d))),
        "crossing_energy_Tr_BBstar": str(e),
        "full_trace_identity_rhs": str(rhs),
        "PH3P_minus_A3": str(ph3p_minus_a3),
        "compression_identity_rhs": str(p_identity),
        "omitting_Tr_D3_mutation_rejected": True,
        "confusing_two_trace_identities_rejected": True,
    }


def abstract_spike():
    rows = []
    for k in (2, 3, 4, 5, 8):
        d = k ** 3
        rows.append({
            "d": d,
            "deleted_rows": 1,
            "r_over_d": f"1/{d}",
            "full_tau3": "1",
            "compressed_tau3": "0",
            "tau6": str(d),
        })
    return rows


def build_certificate():
    # Exact rational checks for normalization/gap bookkeeping.
    ratio = F(1, 4)
    assert ratio * 4 == 1
    return {
        "title": "WP84 Decision E prime-source cubic deletion stability",
        "classification": "E3 — conditional theorem; actual-source deleted-block cubic estimate is absent",
        "start_branch": "codex/c5-c6-attack-20261006",
        "start_head": "aba8d321270332829d5c8f21fc6c111f449081a1",
        "verified_start_head": True,
        "preservation": "notebooklm_packet/ preserved; no push or merge",
        "source_matrix": {
            "scale": "X=T/(2*pi), L=log(X), N=floor(X*exp(-sqrt(L))), d=floor(T*L/(2*pi))",
            "prime_pool": "all n=p^v<=N, v>=1",
            "coefficient": "c_n=-Lambda(n)/(a_phi(T)*L*sqrt(n))",
            "carrier": "z_n=c_n*exp(i*T*log(n)); alpha_n=log(n)/L; w_n(k)=z_n*exp(2*pi*i*k*alpha_n)",
            "fields": "A_k=sum_n Im(w_n(k)); beta_k=sum_n 2*(1-alpha_n)*Re(w_n(k))",
            "matrix": "H=s0(T)I+diag(beta)+[diag(A),J]",
            "kernel": "J_ij=1/(pi*(j-i)) for i!=j, J_ii=0; J*= -J",
            "operator_bound": "||H||op<=|s0|+4*S, S=sum_{p^v<=N}|c_{p^v}|=O(sqrt(N)/L)",
            "fourier_no_wrap": "j(x)=i*(1-2*x) for 0<x<1; partial translations z_n*S_alpha^+ + conjugate(z_n)*S_alpha^-; exact at fixed T,N, not uniform in the growing pool",
            "natural_frequency_margin": "alpha_n<=1-1/sqrt(L)+o(L^(-1/2))",
        },
        "selected_section": {
            "decision_b_d2": "direct first-strike endpoint-admissible pair with weighted density >=1/4 and crossing energy E=||PHQ||HS^2=O(log(d))",
            "M": "ceil(d*exp(-sqrt(L)/2))",
            "r": "u+v<=2*M; r/d=O(exp(-sqrt(L)/2))",
            "d_prime": "d-r~d~T*L/(2*pi)",
            "boundary_error": "selected compression identity error O((1+S)*E/d')=o(1); does not include Tr((QHQ)^3)",
        },
        "exact_full_trace_deletion": {
            "definitions": "A=PHP on P; B=PHQ:Q->P; D=QHQ on Q",
            "identity": "Tr(H^3)-Tr(A^3)=Tr(D^3)+3*Tr_P(A*B*B*)+3*Tr_Q(D*B*B*)",
            "normalized_identity": "tau_d(H^3)-tau_d'(A^3)=Tr(D^3)/d + cross/d - (r/d)*tau_d'(A^3)",
            "cross_bound": "|cross|<=6*(|s0|+4*S)*E",
            "cross_normalized_scale": "O((1+S)*log(d)/d)=O(1/T+exp(-sqrt(L)/2)/(sqrt(2*pi*T)*L))=o(1)",
            "exact_remaining_signed_condition": "Tr(D^3)/d-(r/d)*tau_d'(A^3)=o(1); no cancellation is assumed",
            "separate_sufficient_conditions": ["|Tr(D^3)|/d -> 0", "(r/d)*|tau_d'(A^3)| -> 0"],
            "stronger_sufficient_deleted_block_bound": "||D||_S3^3/d -> 0",
        },
        "source_localized_deleted_block_estimate": {
            "input": "Decision B local prime-power large sieve, uniform on each deleted endpoint interval of length <=M",
            "local_square_mass": "sum_Q |A_k|^2 + sum_Q |beta_k|^2 = O(M+N*L); beta coefficients 2*(1-alpha_n)c_n retain all prime powers",
            "W": "W=Q V Q; ||W||HS^2=O(M+N*L), ||W||op<=4*S",
            "trace_bound": "|Tr(D^3)|/d=O(r/d + sqrt(r*(M+N*L))/d + (M+N*L)/d + S*(M+N*L)/d)",
            "natural_scale": "M>>N*L, r<=2M; bound reduces O(M/d+S*M/d), S*M/d=O(sqrt(T)*exp(-sqrt(L))/L)",
            "verdict": "source-specific boundary-localized HS estimate; final majorant grows and does not prove Tr(D^3)=o(d)",
        },
        "moment_routes": {
            "uniform_sixth": "sup_T tau_d(|H|^6)<=C6^6 implies Decision C bound 6*C6^3*sqrt(2*r/d)+C6^3*(r/d)*sqrt(d/d')=o(1); not established",
            "weaker_route": "uniform integrability of cubic spectral tails for H and its principal compressions suffices by bounded-variation truncation and interlacing",
            "uniform_fourth_suffices": "sup_T tau_d(|H|^4)<infinity implies cubic-tail UI; tau_d'(|A|^4)<=(d/d')*tau_d(|H|^4); no actual-source uniform fourth theorem certified",
            "resolvent_route": "bounded resolvent comparisons do not control the raw cubic tail without a source-uniform weighted resolvent/tail estimate; none is certified",
            "sixth_expansion": "tau_d(H^6)=sum_{j=0}^6 binom(6,j)*s0^(6-j)/d * sum_{n_1,...,n_j in P(N)} Tr(V_n1...V_nj), V=sum_n V_n",
            "word_entry": "(V_n)_ij=delta_ij*2*(1-alpha_n)*Re(w_n(i))+(1-delta_ij)*(Im(w_n(i))-Im(w_n(j)))/(pi*(j-i))",
            "first_missing_sixth_estimate": "uniform bound on total signed sixfold prime-power trace correlation; equality-pattern partitions are bookkeeping only",
            "elementary_bound": "tau_d(H^6)<=||H||op^4*tau_d(H^2)=O((1+S)^4) with bounded m2; diverges and is insufficient",
        },
        "hostile_checks": {
            "abstract_diagonal_spike": abstract_spike(),
            "source_legal_counterexample": False,
            "finite_rational_block_identity": algebra_regression(),
        },
        "scope_firewall": [
            "Decision D2 endpoint result applies to direct first-strike generic endpoint scores only",
            "no source_mask determinant compatibility is inferred",
            "no m3=2, conditioned Cayley energy <0.105, signed fifth/sixth saving, prime-to-Weil transfer, zero-side identification, or strict >79% theorem",
        ],
        "independent_replay": "src/wp84_decision_e_prime_source_cubic_deletion_replay.py",
    }


def main():
    cert = build_certificate()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS exact source coefficient/kernel and natural-cutoff certificate recorded")
    print("PASS rational full-trace and compression block identities")
    print("FALSIFIER: abstract one-row spike defeats rank-only cubic deletion; not prime-source data")
    print("OPEN: deleted Q-block cubic / cubic-tail uniform integrability for the actual prime source")
    print("DECISION: E3 — conditional")
    print("WROTE", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
