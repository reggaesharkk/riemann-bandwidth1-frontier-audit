#!/usr/bin/env python3
"""Deterministic exact-algebra certificate producer for WP84 Decision F.

The matrix arithmetic is over Fraction and is an algebra diagnostic.  The
prime-power expressions are recorded symbolically; this program does not
manufacture a prime-source sample or assert an asymptotic cancellation.
"""
from __future__ import annotations

import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificates" / "WP84_DECISION_F_EXACT_SIGNED_DELETED_BLOCK_CUBIC_CERTIFICATE.json"


def mm(a, b):
    return [[sum((a[i][k] * b[k][j] for k in range(len(b))), F(0))
             for j in range(len(b[0]))] for i in range(len(a))]


def tr(a):
    return sum((a[i][i] for i in range(len(a))), F(0))


def add(a, b):
    return [[a[i][j] + b[i][j] for j in range(len(a[0]))] for i in range(len(a))]


def scale(c, a):
    return [[c * x for x in row] for row in a]


def eye(n):
    return [[F(i == j) for j in range(n)] for i in range(n)]


def cube(a):
    return mm(mm(a, a), a)


def spectral_algebra():
    # Rational beta and A on four deleted coordinates. W0=pi*W, so each
    # coefficient of pi^{-j} can be checked exactly and independently.
    beta = [F(2), F(-1), F(3), F(1, 2)]
    aval = [F(0), F(1), F(3), F(-2)]
    r, s0 = len(beta), F(2, 3)
    b = [[beta[i] if i == j else F(0) for j in range(r)] for i in range(r)]
    w0 = [[F(0) if i == j else (aval[i] - aval[j]) / (j - i)
           for j in range(r)] for i in range(r)]
    b2, b3 = mm(b, b), cube(b)
    w02, w03 = mm(w0, w0), cube(w0)
    bw02 = mm(b, w02)
    # Coefficients in Tr((s0 I+B+W0/pi)^3).
    lhs0 = tr(cube(add(scale(s0, eye(r)), b)))
    rhs0 = r*s0**3 + 3*s0**2*tr(b) + 3*s0*tr(b2) + tr(b3)
    assert lhs0 == rhs0
    assert tr(w0) == 0
    assert tr(mm(b2, w0)) == 0
    assert tr(bw02) == sum((beta[i] * w02[i][i] for i in range(r)), F(0))
    # Polynomial coefficient checks at four exact rational pi^{-1} values.
    for q in (F(0), F(1), F(-2), F(3, 5)):
        d = add(add(scale(s0, eye(r)), b), scale(q, w0))
        rhs = (r*s0**3 + 3*s0**2*tr(b)
               + 3*s0*(tr(b2) + q*q*tr(w02))
               + tr(b3) + 3*q*q*tr(bw02) + q**3*tr(w03))
        assert tr(cube(d)) == rhs

    # Three-index witness: trace of the commutator block cube is nonzero.
    a3 = [F(0), F(1), F(3)]
    w03_small = [[F(0) if i == j else (a3[i]-a3[j])/(j-i)
                  for j in range(3)] for i in range(3)]
    assert tr(cube(w03_small)) == F(-18)
    return {
        "dimension": r,
        "beta": [str(x) for x in beta],
        "A": [str(x) for x in aval],
        "TrW0": str(tr(w0)),
        "TrB2W0": str(tr(mm(b2, w0))),
        "TrB3": str(tr(b3)),
        "TrW0_2": str(tr(w02)),
        "TrBW0_2": str(tr(bw02)),
        "TrW0_3": str(tr(w03)),
        "commutator_cube_three_index_witness": str(tr(cube(w03_small))),
        "pi_scaling": "W=W0/pi; C2 has pi^-2, C3 has pi^-3",
        "exact_checks": "cube identity checked coefficientwise at four rational q=1/pi surrogates; algebra only",
        "scope": "abstract rational matrix identity test; not a prime-source counterexample",
    }


def build():
    return {
        "title": "WP84 Decision F exact signed deleted-block cubic attack",
        "classification": "F3 — conditional: one explicit same-window absolute signed-residual estimate remains",
        "start_branch": "codex/c5-c6-attack-20261006",
        "start_head": "31f869c4d60581131ecb06f23892b38a2f27d8cd",
        "verified_start_head": True,
        "push": "NO",
        "notebooklm_packet": "preserved; not read or modified by this artifact",
        "source": {
            "scale": "X=T/(2*pi), L=log(X), N=floor(X*exp(-sqrt(L))), d=floor(T*L/(2*pi))",
            "prime_pool": "P(N)={p^v: p prime, v>=1, p^v<=N}; all powers retained",
            "coefficient": "c_n=-Lambda(n)/(a_phi(T)*L*sqrt(n))",
            "carrier": "z_n=c_n*exp(i*T*log(n)); alpha_n=log(n)/L; w_n(k)=z_n*exp(2*pi*i*k*alpha_n)",
            "fields": "A_k=sum_n Im(w_n(k)); beta_k=sum_n 2*(1-alpha_n)*Re(w_n(k))",
            "kernel": "J_ij=1/(pi*(j-i)) for i!=j, J_ii=0; W_ij=(A_i-A_j)/(pi*(j-i))",
            "section": "I=[b+u,b+d-1-v], Q is its deleted portion in original section I0; r=u+v<=2M, M=ceil(d*exp(-sqrt(L)/2))",
            "known_inputs": [
                "Decision D2: same-section consumer-admissible endpoint-pair density gamma>=1/4",
                "Decision B: uniform pair average E||P V Q||_HS^2<=C_B log(d)",
                "Decision E: on deleted Q, sum beta_i^2 and sum A_i^2=O(M+N*L); ||W||HS^2=O(M+N*L); ||W||op<=4S",
                "S=sum_{p^v<=N}|c_n|=O(sqrt(N)/L); ||V||op<=4S",
            ],
        },
        "deleted_block_identity": {
            "notation": "D=QHQ=s0*I_Q+B+W; B=diag(beta_i:i in Q); W=Q[diag(A),J]Q",
            "identities": "Tr(W)=0 and Tr(B^2 W)=0 because W has zero diagonal",
            "formula": "Tr(D^3)=r*s0^3+3*s0^2*Tr(B)+3*s0*(Tr(B^2)+Tr(W^2))+C1+C2+C3",
            "C1": "Tr(B^3)=sum_{i in Q} beta_i^3",
            "C2": "3*Tr(B W^2)=3/pi^2 * sum_{i in Q} beta_i * sum_{j in Q,j!=i}(A_i-A_j)^2/(j-i)^2",
            "C3": "Tr(W^3)=1/pi^3 * sum_{i,j,k in Q pairwise distinct} (A_i-A_j)(A_j-A_k)(A_k-A_i)/((j-i)(k-j)(i-k))",
            "index_orientation": "W_ij is symmetric real; trace indices are ordered cyclic triples; each unordered triangle occurs six times",
            "low_degree_estimate": "|Tr B|<=sqrt(r)*O(sqrt(M+N*L)); Tr(B^2)+Tr(W^2)=O(M+N*L); after /d each scalar/degree<=2 term is O(M/d + sqrt(r*(M+N*L))/d)=O(exp(-sqrt(L)/2))=o(1)",
            "cubic_absolute_majorant": "|C1|+|C2|+|C3|<=O(S*(M+N*L)) using ||B||op,||W||op<=4S and local square mass; divided by d this is O(S*M/d)=O(sqrt(T)*exp(-sqrt(L))/L), a nonclosing bound",
        },
        "prime_power_signed_expansions": {
            "notation": "u_{n,sigma}(k)=c_n*exp(i*sigma*(T*log(n)+2*pi*k*alpha_n)), sigma in {-1,+1}; beta_k=sum_n(1-alpha_n)*sum_sigma u; A_k=sum_n sum_sigma sigma*u/(2i)",
            "C1": "sum_{n0,n1,n2 in P(N)} product_t((1-alpha_nt)*c_nt) * sum_{sigma in {+-1}^3} exp(i*T*sum_t sigma_t*log(nt) + 2*pi*i*i_index*sum_t sigma_t*alpha_nt); sum over i_index in Q",
            "C2": "-3/(4*pi^2) sum_{i in Q,j in Q,j!=i} 1/(j-i)^2 * sum_{n0,n1,n2 in P(N)} (1-alpha_n0) * sum_{sigma0,sigma1,sigma2} sigma1*sigma2*u_n0sigma0(i)*(u_n1sigma1(i)-u_n1sigma1(j))*(u_n2sigma2(i)-u_n2sigma2(j)); u includes c_n, all ordered tuples retained",
            "C3": "1/((2*i)^3*pi^3) sum_{i,j,k in Q pairwise distinct} 1/((j-i)(k-j)(i-k)) * sum_{n0,n1,n2 in P(N)} sum_{sigma0,sigma1,sigma2} sigma0*sigma1*sigma2 * product_{edge (x,y)=(i,j),(j,k),(k,i)}(u_nedge,sigmaedge(x)-u_nedge,sigmaedge(y)); u includes c_n",
            "frequency_and_alias_rule": "for each sign triple carrier frequency Omega=sum sigma_t log(n_t)=log(prod_{sigma=+}n_t/prod_{sigma=-}n_t); zero carrier iff the integer products are equal. Discrete index aliases additionally occur when Omega/L is an integer; near aliases are nonzero Omega close to an integer multiple of L. None may be discarded from finite endpoint sums.",
            "exact_three_factor_resonances": "With n_t prime powers, a 2-versus-1 product equality is possible exactly when the two factors share a prime base and their exponents add to the exponent on the singleton; the 1-versus-2 cases are its reversals. All same-sign triples have no zero carrier.",
            "near_resonance_example": "2*3/5=6/5 gives nonzero Omega=log(6/5) with all three entries actual prime powers; finite T phases therefore do not vanish by exact resonance classification.",
            "cancellation_verdict": "no exact arithmetic or cyclic identity removes C1+C2+C3; exact three-index matrix witness has Tr(W0^3)=-18 before pi^-3 scaling",
        },
        "normalization_and_selection": {
            "A_kept": "A=PHP on P, d'=d-r",
            "F": "F(I)=Tr(D^3)-r*tau_{d'}(A^3)",
            "target": "F(I)/d -> 0 for a Decision-D2 consumer-admissible pair",
            "correction_status": "not separately o(d) under certified inputs; no bounded actual-source tau_{d'}(A^3) or cancellation with Tr(D^3) is established; retain the term",
            "selection_sufficient_condition": "a_T=(M+1)^(-2)*sum_{u,v} |F(I_uv)|/d ->0 is sufficient with D2 gamma>=1/4 and Decision-B average crossing energy<=C_B log(d): discard at most 1/8 endpoint pairs for E>8*C_B log(d), and at most sqrt(a_T) for |F|/d>sqrt(a_T); the remaining admissible intersection is nonempty eventually",
            "signed_average_warning": "average F=0 does not imply average |F|=o(1); deterministic +/-1 values are a counterexample",
        },
        "exact_algebra_replay": spectral_algebra(),
        "hostile_tests": {
            "cyclic_cancellation": "rejected by rational A=(0,1,3), Tr(W0^3)=-18",
            "prime_powers": "pool includes p^v for every v>=1; e.g. 4 and 8 are retained; 2*4=8 is an exact legal prime-power resonance",
            "near_alias": "2*3 versus 5 gives exact nonzero log(6/5); no phase deletion licensed",
            "normalization": "abstract diagonal spectrum with d'=d-r and tau(A^3) growing like d/r can keep (r/d)*tau(A^3) order one; not prime-source data",
            "endpoint_and_signed_mean": "abstract endpoint arrays can place all large |F| on the admissible quarter or have signed mean zero and absolute mean one; neither is a prime-source counterexample",
            "source_counterexample": False,
        },
        "decision": "F3 — conditional theorem: prove the single full-window estimate average_{u,v}|Tr((QHQ)^3)-r*tau_{d'}((PHP)^3)|/d=o(1) for the original prime-power source and exact endpoint weights, or derive an equally strong admissible-set joint estimate",
        "strict_gt_79": "OPEN",
        "independent_replay": "src/wp84_decision_f_exact_signed_deleted_block_cubic_replay.py",
    }


def main():
    cert = build()
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS exact deleted-block cube identity and zero-diagonal traces")
    print("PASS exact rational commutator-cube falsifier; cyclic cancellation rejected")
    print("RECORDED all-prime-power signed forms and same-section selection condition")
    print("OPEN source-weighted normalized cubic residual; decision F3")
    print("STRICT >79: OPEN")
    print("WROTE", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
