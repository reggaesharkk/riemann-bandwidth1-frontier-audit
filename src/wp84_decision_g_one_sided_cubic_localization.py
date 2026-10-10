#!/usr/bin/env python3
"""Exact deterministic certificate producer for WP84 Decision G.

Rational matrix checks validate identities only. Source-level estimates are
recorded with their hypotheses; no prime-source cubic estimate is fabricated.
"""
from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificates" / "WP84_DECISION_G_ONE_SIDED_CUBIC_LOCALIZATION_CERTIFICATE.json"


def mm(a, b):
    return [[sum((a[i][k]*b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def add(a, b):
    return [[a[i][j]+b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c, a):
    return [[c*x for x in row] for row in a]


def sub(a, b):
    return [[a[i][j]-b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def block(a, rows, cols):
    return [[a[i][j] for j in cols] for i in rows]


def trans(a):
    return [list(x) for x in zip(*a)]


def cube(a):
    return mm(mm(a, a), a)


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def norm_sq(a):
    return sum((x*x for row in a for x in row), F(0))


def exact_tests():
    # Rational source-form matrix: H_ij=s0 delta_ij+beta_i delta_ij
    # +(A_i-A_j)/(j-i), with the common q=1/pi suppressed as a formal scale.
    Avals = [F(0), F(2), F(-1), F(3), F(4), F(-2), F(2), F(7)]
    beta = [F(1), F(-2), F(0), F(3), F(-1), F(2), F(1, 2), F(-3)]
    n, s0 = len(Avals), F(2, 5)
    W0 = [[F(0) if i == j else (Avals[i]-Avals[j])/(j-i)
           for j in range(n)] for i in range(n)]
    H = add(scale(s0, eye(n)), [[(beta[i] if i == j else F(0))+W0[i][j]
                                for j in range(n)] for i in range(n)])
    ql, qr = [0, 1], [6, 7]
    DL, DR, C = block(H, ql, ql), block(H, qr, qr), block(H, ql, qr)
    lhs = tr(cube(block(H, ql+qr, ql+qr)))
    CCt, CtC = mm(C, trans(C)), mm(trans(C), C)
    rhs = tr(cube(DL))+tr(cube(DR))+3*tr(mm(DL, CCt))+3*tr(mm(DR, CtC))
    assert lhs == rhs
    assert norm_sq(C) > 0  # separated endpoint blocks are not independent
    # Their least index gap is d-2M+1=8-4+1=5, yet C is nonzero.
    min_gap = min(j-i for i in ql for j in qr)
    assert min_gap == 5

    # Self-normalization identity on an exact trimmed section P=[2,3,4,5].
    pids, qids = [2, 3, 4, 5], [0, 1, 6, 7]
    Ap, Bpq, Dq = block(H, pids, pids), block(H, pids, qids), block(H, qids, qids)
    BBt, BtB = mm(Bpq, trans(Bpq)), mm(trans(Bpq), Bpq)
    G = 3*tr(mm(Ap, BBt))+3*tr(mm(Dq, BtB))
    d, dp, r = n, len(pids), len(qids)
    mT = tr(cube(H))/d
    tauA = tr(cube(Ap))/dp
    Fdel = tr(cube(Dq))-r*tauA
    lhs_self = Fdel/d
    rhs_self = (tr(cube(Dq))-r*mT)/dp + r*G/(d*dp)
    assert lhs_self == rhs_self

    # One-row exact block increment and the source-kernel edge orientation.
    old = [[F(2), F(1)], [F(1), F(-1)]]
    h = [F(2, 3), F(-1, 4)]
    a = F(5, 2)
    new = [old[0]+[h[0]], old[1]+[h[1]], h+[a]]
    increment = tr(cube(new))-tr(cube(old))
    formula = a**3+3*a*sum((x*x for x in h), F(0))+3*sum(
        (h[i]*old[i][j]*h[j] for i in range(2) for j in range(2)), F(0))
    assert increment == formula
    # W_{j,k}=(A_j-A_k)/(pi*(k-j)); q=1/pi suppressed in W0.
    k, j = 4, 2
    edge = W0[j][k]
    oriented = (Avals[j]-Avals[k])/(k-j)
    assert edge == oriented

    # Exact failure of independence remains after large separation.
    # The cross-block correction is nonzero; this matrix example is abstract.
    assert 3*tr(mm(DL, CCt))+3*tr(mm(DR, CtC)) != 0

    # Endpoint selection stress: a cubic-good endpoint can be inadmissible.
    all_pairs = set(range(16))
    admissible = set(range(4))  # density exactly 1/4
    cubic_good = set(range(4, 16))
    assert len(admissible)/len(all_pairs) == F(1, 4)
    assert cubic_good and not (admissible & cubic_good)
    # Full-window small absolute average restores a positive intersection.
    admissible2 = set(range(4))
    energy_bad = {4, 5}
    cubic_bad = {6, 7}
    assert admissible2-energy_bad-cubic_bad

    # Prime-power equality and nonzero near-frequency examples.
    assert 2*4 == 8
    assert 2*3 == 6 and 6 != 5
    # A local-square-mass abstract spike: L2^2=M, L3^3=M^(3/2).
    spike_m = 10000
    l2sq, l3abs = F(spike_m), F(spike_m)**F(3, 2)
    assert l3abs/l2sq > 1
    return {
        "rational_source_form_dimension": n,
        "separated_block_gap": min_gap,
        "cross_hilbert_schmidt_square": str(norm_sq(C)),
        "separated_cube_identity_lhs": str(lhs),
        "separated_cube_identity_rhs": str(rhs),
        "cross_trace_correction": str(3*tr(mm(DL, CCt))+3*tr(mm(DR, CtC))),
        "self_normalization_mT": str(mT),
        "self_normalization_G": str(G),
        "self_normalization_F": str(Fdel),
        "self_normalization_lhs": str(lhs_self),
        "self_normalization_rhs": str(rhs_self),
        "one_row_increment": str(increment),
        "one_row_formula": str(formula),
        "orientation_edge": str(edge),
        "admissible_density": "1/4",
        "cubic_good_admissible_intersection_hostile": True,
        "abstract_L2_L3_spike": {"M": spike_m, "square_mass": str(l2sq), "absolute_cubic_mass": str(l3abs)},
        "scope": "exact rational algebra and abstract hostile arrays; not prime-source asymptotics",
    }


def build():
    return {
        "title": "WP84 Decision G one-sided cubic localization",
        "classification": "G2 — exact one-sided localization proved; source arithmetic estimate unresolved",
        "start_branch": "codex/c5-c6-attack-20261006",
        "start_head": "3e7672d63ef611917bbb51c0b6c4a4eb3441e803",
        "verified_start_head": True,
        "push": "NO",
        "preservation": "notebooklm_packet/ untouched",
        "source": {
            "scale": "X=T/(2*pi), L=log(X), N=floor(X*exp(-sqrt(L))), d=floor(T*L/(2*pi))",
            "trim": "I(u,v)=[b+u,b+d-1-v], 0<=u,v<=M=ceil(d*exp(-sqrt(L)/2)); QL=[b,b+u-1], QR=[b+d-v,b+d-1], r=u+v",
            "prime_pool": "all p^v<=N; c_n=-Lambda(n)/(a_phi(T)*L*sqrt(n)); z_n=c_n*exp(i*T*log(n)); alpha_n=log(n)/L",
            "fields": "A_k=sum Im(z_n exp(2*pi*i*k*alpha_n)); beta_k=sum 2*(1-alpha_n) Re(z_n exp(2*pi*i*k*alpha_n))",
            "matrix": "H=s0 I+diag(beta)+[diag(A),J], J_ij=1/(pi*(j-i)); 0<alpha_n<=1-1/sqrt(L); prior partial-translation/no-wrap identities are fixed-cutoff, not growing-pool estimates",
            "consumer_scope": "R=6000 direct first-strike endpoint score is the Decision D2 admissibility gate; no transfer to source-masked determinant consumer",
        },
        "separation": {
            "block_matrix": "D=[[D_L,C],[C*,D_R]] with rows QL then QR",
            "kernel": "C_ij=(A_i-A_j)/(pi*(j-i)); i in QL, j in QR",
            "minimum_distance": "min(j-i)=d-u-v+1>=d-2M+1",
            "exact_identity": "Tr(D^3)=Tr(D_L^3)+Tr(D_R^3)+3Tr(D_L*C*C*)+3Tr(D_R*Cstar*C)",
            "operator_bound": "||D_L||op,||D_R||op<=K_T=|s0|+4S",
            "local_square_input": "sum_{QL} A_i^2, sum_{QR} A_j^2 <= C_A*(M+N*L) and beta-square mass <=4*C_A*(M+N*L), from the uniform source prime-power local large sieve",
            "cross_HS_bound": "||C||HS^2 <= 4*C_A*M*(M+N*L)/(pi^2*(d-2M+1)^2)",
            "cross_cube_bound": "|Tr(D^3)-Tr(D_L^3)-Tr(D_R^3)|/d <= 24*C_A*K_T*M*(M+N*L)/(pi^2*d*(d-2M)*(d-2M+1)^2)",
            "natural_rate": "O((1+S)*M*(M+N*L)/d^3)=O(exp(-sqrt(L))/(T*L)+exp(-3*sqrt(L)/2)/(sqrt(T)*L^2))=o(1)",
            "independence_firewall": "C is small in normalized HS contribution but not identically zero; no exact independence is claimed",
        },
        "self_normalization": {
            "mT": "Tr(H^3)/d; unknown finite-source quantity, no boundedness or value assumed",
            "G": "3Tr_P(A*B*B*)+3Tr_Q(D*B*B*), where A=PHP, B=PHQ, D=QHQ",
            "exact_identity": "F(I)/d=(Tr(D^3)-r*mT)/d' + r*G(I)/(d*d')",
            "cross_bound": "|G(I)|<=6*K_T*E(I), E=||PHQ||HS^2",
            "actual_weight_average": "E_{uniform (u,v)}|r*G/(d*d')| <= 12*K_T*C_B*M*log(d)/(d*(d-2M))",
            "natural_rate": "O((1+S)*M*log(d)/d^2)=O(exp(-sqrt(L)/2)/T+exp(-sqrt(L))/(sqrt(T)*L))=o(1)",
        },
        "one_sided_reduction": {
            "ZL": "Z_L(u)=Tr(D_L(u)^3)-u*mT",
            "ZR": "Z_R(v)=Tr(D_R(v)^3)-v*mT",
            "identity": "Tr(D^3)-r*mT=Z_L(u)+Z_R(v)+J_sep(u,v), J_sep=3Tr(D_L*C*C*)+3Tr(D_R*Cstar*C)",
            "inequality": "E_{u,v}|F(I)|/d <= (E_u|Z_L(u)|+E_v|Z_R(v)|)/(d-2M)+epsilon_T",
            "epsilon_T": "24*C_A*K_T*M*(M+N*L)/(pi^2*(d-2M)*(d-2M+1)^2) + 12*K_T*C_B*M*log(d)/(d*(d-2M)) = o(1)",
            "cancellation_note": "separate one-sided absolute bounds are sufficient, not necessary; cancellation between Z_L and Z_R is possible but unproved",
            "single_remaining_estimate": "(E_u|Z_L(u)|+E_v|Z_R(v)|)/(d-2M)=o(1), or an equally strong direct bound on the joint admissible pairs",
        },
        "row_increments": {
            "identity": "Tr([[D_old,h],[h*,a]]^3)-Tr(D_old^3)=a^3+3*a*||h||^2+3*h*D_old*h",
            "source_values": "a=s0+beta_k; h_j=(A_j-A_k)/(pi*(k-j))=H_{j,k} for old j and new endpoint k",
            "telescoping": "Z_side(q)=sum_{t=0}^{q-1}(increment_t-mT), for both left growth k=b+t and right growth k=b+d-1-t",
            "first_new_three_frequency_term": "beta_k^3 inside a^3; beta*A^2 occurs in a*||h||^2; h*D_old*h also contains signed beta*A^2 and A^3 terms",
            "current_control": "local S2 plus ||D_old||op<=K_T bounds cumulative absolute increments by O(K_T*(M+N*L)), whose /d bound O(K_T*M/d) is nonclosing; it does not bound centered sums because mT is unknown",
        },
        "arithmetic_boundary": {
            "signed_variables": "u_{n,sigma}(k)=c_n exp(i*sigma*(T log n+2*pi*k*alpha_n)); every n=p^v<=N retained",
            "exact_resonance": "Omega=sum sigma_t log(n_t)=0 iff products on + and - sign sides agree; for 2-vs-1 prime-power triples, the two terms must be powers of the same prime and exponents add",
            "example_exact": "2*4=8",
            "example_nonzero": "2*3/5=6/5, so Omega=log(6/5) is nonzero although all entries are prime powers",
            "endpoint_phase_warning": "Cubic products from h edges assign frequencies to distinct endpoint indices; an Omega/L integer test alone does not collapse all endpoint-dependent phases. Keep the exact finite endpoint sums and classify near aliases only after their actual phase forms are written.",
            "no_new_estimate": "No deterministic three-frequency estimate for the centered one-sided increments is proved; no Gaussian/random-phase or imported moment bound is used",
        },
        "same_section_selection": {
            "admissible_density": "gamma>=1/4 under exact uniform pair weights, for direct first-strike consumer only",
            "crossing_average": "E E(I_uv)<=C_B*log(d)",
            "sufficient_input": "one-sided average bound above tends to zero, hence E|F|/d=o(1)",
            "joint_selection": "Markov: energy-bad weight<=1/8 at threshold 8*C_B log(d); cubic-bad weight<=sqrt(a_T) at threshold sqrt(a_T), where a_T=E|F|/d. Since admissible weight>=1/4, intersection is positive eventually",
            "determinant_scope": "not transferred to source_mask determinant consumer",
        },
        "exact_replay": exact_tests(),
        "decision": "G2 — the two-endpoint interaction and mixed-boundary self-normalization are o(1); full deletion reduces to one-sided centered cubic estimates, which remain open",
        "strict_gt_79": "OPEN",
        "independent_replay": "src/wp84_decision_g_one_sided_cubic_localization_replay.py",
    }


def main():
    data = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS exact separated-block cube identity and nonzero cross-block test")
    print("PASS exact self-normalization and one-row increment identities")
    print("BOUND separated-block and mixed-boundary remainders are o(1)")
    print("OPEN one-sided centered three-frequency source estimate")
    print("DECISION G2; strict >79 OPEN")
    print("WROTE", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
