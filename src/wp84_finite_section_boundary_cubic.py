#!/usr/bin/env python3
"""Produce the exact block identity and source-bound scalar boundary certificate.

This certifies the scalar-background part of the finite-section cubic boundary
correction as o(1) at the natural prime cutoff.  It intentionally leaves the
signed V-cubic boundary remainder open.
"""
from __future__ import annotations

import json
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificates" / "WP84_FINITE_SECTION_BOUNDARY_CUBIC_CERTIFICATE.json"


def exact_block_replay():
    """Exact rational/algebraic finite Hermitian source-form regression."""
    I = sp.I
    pi = sp.pi
    inds = list(range(-3, 5))
    section = [0, 1, 2]
    alpha = sp.Rational(1, 3)
    z = 2 + I
    s0 = sp.Rational(3, 5)
    root = -sp.Rational(1, 2) + I * sp.sqrt(3) / 2

    def field(k):
        w = z * root ** (k % 3)
        return sp.simplify(sp.im(w)), sp.simplify(2 * (1-alpha) * sp.re(w))

    vals = {k: field(k) for k in inds}
    V = sp.zeros(len(inds), len(inds))
    for a, i in enumerate(inds):
        Ai, betai = vals[i]
        V[a, a] = betai
        for b, j in enumerate(inds):
            if i != j:
                Aj, _ = vals[j]
                V[a, b] = sp.simplify((Ai-Aj)/(pi*(j-i)))
    H = V + s0 * sp.eye(len(inds))
    pidx = [inds.index(k) for k in section]
    qidx = [a for a in range(len(inds)) if a not in pidx]

    def sub(M, rows, cols):
        return M.extract(rows, cols)

    App = sub(H, pidx, pidx)
    Bpq = sub(H, pidx, qidx)
    Cqp = sub(H, qidx, pidx)
    Dqq = sub(H, qidx, qidx)
    lhs = sp.trace(sub(H**3, pidx, pidx)) - sp.trace(App**3)
    rhs = 2*sp.trace(App*Bpq*Cqp) + sp.trace(Bpq*Dqq*Cqp)
    assert sp.simplify(lhs-rhs) == 0
    assert sp.simplify(Cqp-Bpq.conjugate().T) == sp.zeros(len(qidx), len(pidx))
    assert sp.simplify(H-H.conjugate().T) == sp.zeros(len(inds), len(inds))

    Vpp = sub(V, pidx, pidx)
    Vpq = sub(V, pidx, qidx)
    Vqp = sub(V, qidx, pidx)
    Vqq = sub(V, qidx, qidx)
    scalar_piece = 3*s0*sp.trace(Vpq*Vqp)
    v_cubic = 2*sp.trace(Vpp*Vpq*Vqp) + sp.trace(Vpq*Vqq*Vqp)
    assert sp.simplify(lhs - scalar_piece - v_cubic) == 0
    assert sp.simplify(sp.trace(Vpq*Vqp) - sum(Vpq[a,b]*Vqp[b,a]
                                              for a in range(Vpq.rows)
                                              for b in range(Vpq.cols))) == 0
    return {
        "diagnostic_only": True,
        "index_set": inds,
        "section": section,
        "alpha": "1/3",
        "z": "2+i (algebra regression only; not the natural prime pool)",
        "s0": "3/5",
        "exact_lhs_minus_rhs": "0",
        "hermiticity_residual": "0",
        "scalar_difference_identity_residual": "0",
        "scalar_cross_energy": str(sp.simplify(sp.trace(Vpq*Vqp))),
        "scalar_boundary_contribution": str(sp.simplify(scalar_piece)),
        "finite_dimension": len(inds),
        "section_dimension": len(pidx),
        "complement_dimension": len(qidx),
    }


def crossing_pair_counts(max_d=12):
    rows = []
    for d in range(1, max_d+1):
        for r in range(1, 3*d+1):
            actual = sum(1 for i in range(d) for j in range(-r, d+r)
                         if (j < 0 or j >= d) and abs(j-i) == r)
            assert actual == 2*min(r, d)
        rows.append({"d": d, "verified_displacements": f"1..{3*d}",
                     "pairs_at_abs_displacement_r": "2*min(r,d)"})
    return rows


def main():
    finite = exact_block_replay()
    cert = {
        "title": "Finite-section cubic block identity and scalar boundary sector",
        "decision": "B — scalar-background boundary sector is source-valid o(1); signed V-cubic boundary transfer remains open",
        "source": {
            "scale": "L=log X, X=T/(2*pi), N=floor(X*exp(-sqrt(L))), d=floor(T*L/(2*pi)); d'/d->1",
            "prime_powers": "all n=p^v<=N",
            "coefficient": "c_n=-Lambda(n)/(a_phi(T)*L*sqrt(n))",
            "carrier": "z_n=c_n*exp(i*T*log(n))",
            "frequency": "alpha_n=log(n)/L",
            "fields": "A_n(k)=Im(z_n*exp(2*pi*i*k*alpha_n)); beta_n(k)=2*(1-alpha_n)*Re(z_n*exp(2*pi*i*k*alpha_n))",
            "operator": "H=s0(T)I+V; V=diag(beta)+[diag(A),J], J_ij=1/(pi*(j-i)) for i!=j, J_ii=0",
            "section": "I=[k_-,k_-+d'-1], P=P_I, Q=I-P",
            "inherited_gates": "a_phi(T)->1, s0(T)->1, d'~T*L, full natural prime-power cutoff",
        },
        "block_identity": {
            "definitions": "A=PHP on P-space; B=PHQ:Q->P; C=QHP=B*:P->Q; D=QHQ on Q-space",
            "statement": "Tr_P(PH^3P)-Tr_P((PHP)^3)=2*Tr_P(A*B*C)+Tr_P(B*D*C)",
            "source_split": "B=PVQ; A=s0*P+V_PP; D=s0*Q+V_QQ",
            "scalar_background_exact": "3*s0*||PVQ||_HS^2",
            "remaining_signed_cubic": "2*Tr_P(V_PP*B*B*)+Tr_P(B*V_QQ*B*)",
            "trace_class_basis": "B is Hilbert-Schmidt; B*B and B V_QQ B* are trace class; traces are on the finite P-space",
        },
        "source_expansion": {
            "entry": "v_ij=delta_ij*beta_i+(1-delta_ij)*(A_i-A_j)/(pi*(j-i)); A_i=sum_n Im(z_n exp(2*pi*i*i*alpha_n)); beta_i=sum_n 2*(1-alpha_n) Re(z_n exp(2*pi*i*i*alpha_n))",
            "scalar_cross_energy": "||PVQ||_HS^2=pi^-2*sum_{i in I,j notin I}(A_i-A_j)^2/(j-i)^2",
            "exact_finite_prime_power_triple_expansion": "R= sum_{n1,n2,n3<=N prime powers} [2 Tr_P(Vn1_PP Vn2_PQ Vn3_QP)+Tr_P(Vn1_PQ Vn2_QQ Vn3_QP)]",
            "index_trace_interpretation": "for each fixed T,N, the index sums are the trace-class pairings of the displayed blocks; no rearrangement into unsigned nonconvergent sums is assumed",
            "all_signs_and_aliases": "retained in z_n and conjugation implicit in real/imaginary fields; no frequency/alias class is discarded",
        },
        "scalar_sector_bound": {
            "crossing_count": "number of ordered (i in I,j notin I) with |j-i|=r is 2*min(r,d')",
            "field_bound": "|A_i|<=S, S=sum_{p^v<=N}|c_{p^v}|",
            "hilbert_schmidt": "||PVQ||_HS^2<=8*S^2/pi^2*(H_d'+1)",
            "normalized_scalar": "|3*s0|*||PVQ||_HS^2/d'<=24*|s0|*S^2*(H_d'+1)/(pi^2*d')",
            "prime_power_mass": "PNT/Chebyshev with a_phi bounded away from zero gives S=O(sqrt(N)/L), including all prime powers",
            "natural_cutoff": "d'~T*L, H_d'=O(L), N~(T/(2*pi))*exp(-sqrt(L)); normalized scalar sector=O(exp(-sqrt(L))/L^2)=o(1)",
            "scope": "only the exact scalar-background summand is shown o(1); this is not the complete boundary correction",
        },
        "remaining_terms": {
            "decomposition": "R=2 Tr_P((diag(beta)_P+O_PP)*B*B*)+Tr_P(B*(diag(beta)_Q+O_QQ)*B*) where O=[diag(A),J]",
            "sign": "no positivity follows: diagonal beta is signed and the commutator blocks are Hermitian but indefinite",
            "repeated_vs_distinct": "the finite n1,n2,n3 expansion permits exact grouping by repeated base/proper power/all-distinct; previously proved full-section moment removals do not transfer to these boundary weights",
            "aliases": "actual phases exp(i*T*sum epsilon_j log(n_j)) and section endpoint kernel remain; no exact or near-alias cancellation is certified here",
            "best_inherited_absolute_bound": "|R|/d'=O(S^3*(H_d'+1)/d')=O(N^(3/2)/(T*L^3))=O(T^(1/2)*exp(-3*sqrt(L)/2)/L^3), not a useful vanishing majorant",
            "first_unresolved_sum": "uniform source-weighted signed bound for R/d' at natural N, over the original admissible contiguous sections, with all prime powers and carrier phases",
        },
        "independent_exact_replay": finite,
        "crossing_pair_count_samples": crossing_pair_counts(),
        "claim_boundary": "No m3=2, 0.105 conditioned-energy conclusion, prime-to-Weil transfer, or strict >79 theorem is claimed.",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print("PASS exact finite Hermitian block identity and scalar separation")
    print("PASS crossing-pair formula 2*min(r,d) for d=1..12")
    print("BOUND source scalar boundary sector O(exp(-sqrt(L))/L^2)=o(1)")
    print("OPEN signed V-cubic remainder at natural cutoff")
    print("WROTE", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
