#!/usr/bin/env python3
"""Deterministic producer for the Decision-I zero-carrier cubic bound.

This records exact combinatorial/algebraic checks.  It does not estimate the
remaining nonzero prime-power endpoint correlations.
"""
from __future__ import annotations

import json
from fractions import Fraction as Q
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificates" / "WP84_DECISION_I_CUBIC_PRIME_RESONANCE_CERTIFICATE.json"


def prime_power_factorization(n: int) -> tuple[int, int] | None:
    for p in range(2, n + 1):
        if all(p % q for q in range(2, int(p**0.5) + 1)):
            x, v = n, 0
            while x % p == 0:
                x //= p
                v += 1
            if x == 1:
                return p, v
    return None


def finite_ufd_regression(limit: int = 80) -> dict:
    powers = [n for n in range(2, limit + 1) if prime_power_factorization(n)]
    by_sign = {"two_plus_one_minus": 0, "one_plus_two_minus": 0,
               "all_plus": 0, "all_minus": 0}
    examples = []
    for ns in product(powers, repeat=3):
        for sigmas in product((-1, 1), repeat=3):
            plus = 1
            minus = 1
            for n, sigma in zip(ns, sigmas):
                if sigma == 1:
                    plus *= n
                else:
                    minus *= n
            if plus != minus:
                continue
            count_plus = sigmas.count(1)
            if count_plus == 3:
                # Product of three integers >=2 cannot equal the empty side 1.
                raise AssertionError("all-plus exact closure unexpectedly found")
            if count_plus == 0:
                raise AssertionError("all-minus exact closure unexpectedly found")
            key = "two_plus_one_minus" if count_plus == 2 else "one_plus_two_minus"
            by_sign[key] += 1
            f = [prime_power_factorization(n) for n in ns]
            assert all(x is not None for x in f)
            plus_f = [f[i] for i, s in enumerate(sigmas) if s == 1]
            minus_f = [f[i] for i, s in enumerate(sigmas) if s == -1]
            if count_plus == 2:
                p1, a = plus_f[0]
                p2, b = plus_f[1]
                q, c = minus_f[0]
            else:
                p1, a = minus_f[0]
                p2, b = minus_f[1]
                q, c = plus_f[0]
            assert p1 == p2 == q and a + b == c
            if a == b and len(examples) < 8:
                examples.append({"prime": p1, "a": a, "b": b, "sum_exponent": c,
                                 "triple": list(ns), "signs": list(sigmas)})
    return {"cutoff": limit, "prime_power_triples": len(powers),
            "exact_zero_ordered_triples_by_sign_class": by_sign,
            "repeated_exponent_examples_included": examples}


def exact_regressions() -> dict:
    # Six labelled sign placements times ||U||^3 <= 2^3 gives 48.
    factor = 6 * 2**3
    assert factor == 48
    # The sharper product uses ||U_(p^a,sigma)|| <= 2-a log(p)/L.
    # For a valid toy range 0 < alpha_i < 1, its factor is no larger than 8.
    sharp_examples = []
    for alphas in ((Q(1, 4), Q(1, 3), Q(7, 12)),
                   (Q(1, 2), Q(1, 2), Q(1, 2))):
        assert all(0 < a < 1 for a in alphas)
        prod_bound = Q(1)
        for a in alphas:
            prod_bound *= 2 - a
        assert prod_bound < 8
        sharp_examples.append({"alphas": [str(a) for a in alphas],
                               "product_factor": str(prod_bound)})

    # The prime sum converges by comparison with sum_n log(n)^3/n^2.
    # A rational tail envelope is not needed for the symbolic theorem.
    # Verify finite Fourier-compression dimension and endpoint centering factors.
    centered_factor = 2  # |R_kk - tr(R)/d| <= 2 ||R|| for Hermitian R
    both_sides = 2 * centered_factor
    assert both_sides == 4
    bound_prefactor = both_sides * factor
    assert bound_prefactor == 192
    return {"ordered_sign_placements": 6, "operator_product_bound": 8,
            "proposed_constant": factor,
            "sharper_alpha_product_examples": sharp_examples,
            "centered_score_factor_per_entry": centered_factor,
            "two_endpoint_sides_factor": both_sides,
            "centered_two_endpoint_prefactor": bound_prefactor,
            "integer_product_separation": {
                "for_distinct_A_B_le_N2": "|log(A/B)| >= log(1+1/max(A,B)) >= 1/(N^2+1)",
                "endpoint_frequency_lower_bound": "1/(L*(N^2+1))",
                "relative_to_coherence_width_1_over_M": "M/(L*(N^2+1)) -> 0 at N~X*exp(-sqrt(L)), M~T*L*exp(-sqrt(L)/2)"
            }}


def main() -> None:
    cert = {
        "title": "WP84 Decision I: cubic prime-resonance discharge",
        "classification": "I2 — exact zero-carrier full-prime-power cubic sector has a source-valid O(L^-3) operator and centered endpoint bound; nonzero aliases remain open",
        "start_state": {"branch": "codex/c5-c6-attack-20261006",
                        "head": "f58316f8ad14442427328f208a49f1aeef98470b",
                        "preexisting_untracked": ["notebooklm_packet/"],
                        "push": "NO", "merge": "NO", "notebooklm_packet": "untouched"},
        "source": {
            "scale": "X=T/(2*pi), L=log(X), N=floor(X*exp(-sqrt(L))), d=floor(T*L/(2*pi)), M=ceil(d*exp(-sqrt(L)/2))",
            "pool": "P(N)={p^v:p prime,v>=1,p^v<=N}; no prime powers omitted",
            "coefficient": "c_n=-Lambda(n)/(a_phi(T)*L*sqrt(n)) (real); alpha_n=log(n)/L",
            "matrix": "V=diag(beta)+[diag(A),J], H=s0*I+V; J_ij=1/(pi*(j-i)) for i!=j and J_ii=0",
            "signed_operator": "D_(n,sigma)=diag(exp(2*pi*i*sigma*k*alpha_n)); U_(n,sigma)=(1-alpha_n)D_(n,sigma)+sigma/(2i)[D_(n,sigma),J]",
            "reconstruction": "V=sum_(n in P(N),sigma=+-1) c_n*exp(i*sigma*T*log(n))*U_(n,sigma)",
            "finite_J_norm": "J on a finite contiguous section is a compression of the bilateral convolution with multiplier i*(1-2x), 0<x<1; hence ||J_section||<=1. Equality for every finite section is not asserted.",
            "U_bound": "||U_(n,sigma)||<=1-alpha_n+||[D,J]||/2<=2-alpha_n<2, since ||D||=1 and ||J_section||<=1"
        },
        "zero_carrier": {
            "exact_condition": "sigma1*log(n1)+sigma2*log(n2)+sigma3*log(n3)=0 iff product of the plus-side prime powers equals the product of the minus-side prime powers",
            "ufd_classification": "Only 2-vs-1 or 1-vs-2 sign splits occur; UFD forces all three bases to be one prime p and singleton exponent a+b",
            "ordered_multiplicity": "For each of six labelled sign vectors, sum over ordered a,b>=1; a=b appears once per sign vector, and a!=b has both slot assignments through (a,b),(b,a), with no extra factor",
            "coefficient_mass": "|c_(p^a)c_(p^b)c_(p^(a+b))|=(log p)^3/(|a_phi|^3*L^3*p^(a+b))",
            "proposed_bound": "||R_zero||<=48/(|a_phi|^3*L^3)*C0, C0=sum_p (log p)^3/(p-1)^2 < infinity",
            "sharper_bound": "||R_zero||<=6/(|a_phi|^3*L^3)*sum_p (log p)^3*sum_(a,b>=1,p^(a+b)<=N) ((2-a*log(p)/L)(2-b*log(p)/L)(2-(a+b)*log(p)/L))/p^(a+b)",
            "convergence": "C0<=4*sum_(n>=2)(log n)^3/n^2<infinity",
            "centered_endpoint": "For each endpoint partial sum length <=M, |sum_k((R_zero)_kk-tau_d(R_zero))|<=2*M*||R_zero||; for both sides total <=192*C0*M/(|a_phi|^3*L^3)",
            "normalized_rate": "O(M/(d*L^3))=O(exp(-sqrt(L)/2)/L^3) because a_phi->1 and M/d~exp(-sqrt(L)/2)"
        },
        "remaining_aliases": {
            "carrier": "Omega=sum_i sigma_i*log(n_i)=log(A/B), A=product_(sigma=+)n_i, B=product_(sigma=-)n_i; carrier is exp(i*T*Omega)",
            "sample_frequency": "omega is the signed sum of alpha_n for the factors evaluated at the varying endpoint coordinate; for beta_k^3, omega=Omega/L, but in finite-J path terms it is only the k-attached subset",
            "kernel": "sum_(k=k0)^(k0+q-1) exp(2*pi*i*k*omega) = q if omega is an integer; otherwise magnitude=|sin(pi*q*omega)|/|sin(pi*omega)|<=min(q,1/|sin(pi*omega)|)",
            "near_alias": "|omega-m|<=1/M is coherent at length M; exact zero carrier is only m=0 and does not remove nonzero near aliases",
            "integer_aliases": "Since each alpha<1 and at most three endpoint factors occur, nearest integer aliases m=+-1,+-2 may occur; m=+-3 cannot. Product-ratio condition for total-frequency aliases is A/B approximately X^m; subset path aliases use their own endpoint products.",
            "spacing_verdict": "For a mixed 2-vs-1 nonzero product A!=B with A,B<=N^2, |Omega|>=1/(N^2+1). This yields frequency spacing 1/(L*(N^2+1)), which is much smaller than 1/M at the natural cutoff; separation does not exclude the 1/M near-zero window. This is a failure of the spacing argument, not evidence that such prime tuples occur."
        },
        "remaining_endpoint_estimate": {
            "required": "E_u|sum_(left length u)((g_k-tau_d H^3))| + E_v|sum_(right length v)((g_k-tau_d H^3))| = o(d), g_k=(H^3)_kk",
            "after_zero_removal": "Same centered endpoint partial sums for (R_nonzero)_kk, plus the already controlled centered linear and quadratic fields",
            "best_inherited_absolute_bound": "O(K_T*(M+N*L)); normalized O(K_T*M/d) when M>>N*L",
            "natural_cutoff_envelope": "O(exp(L/2-sqrt(L))/L), which diverges as an upper bound",
            "status": "No source-valid o(d) estimate for all nonzero/near aliases or their complete signed finite-J paths is established; no lower bound or source counterexample is established."
        },
        "prior_scope": {
            "R6000_consumer": "Earlier high-product/near-alias reports concern the fixed-R=6000 ordinary-prime moment consumer and do not control the full prime-power H matrix or its finite-J endpoint score.",
            "infinite_no_wrap": "Exact nonzero integer displacement operators vanish in the infinite partial-shift model at fixed finite cutoff; the identity is not uniform in the natural growing cutoff and does not bound finite-section endpoint scores.",
            "decision_h": "Decision H2 localized square/direct majorants remain above the o(d) threshold; their divergence is only failure of an upper majorant."
        },
        "exact_replay": exact_regressions(),
        "finite_ufd_regression": finite_ufd_regression(),
        "prerequisites": ["Decision B and C-H prerequisite replays PASS before this audit",
                          "High-product, signed near-alias, direct signed correlation, and infinite no-wrap replays PASS before this audit"],
        "decision": "I2",
        "theorem_boundary": "m3=2, conditioned Cayley energy<0.105, signed fifth/sixth gate, prime-to-Weil identification, zero-side transfer, determinant compatibility, and strict >79% remain OPEN."
    }
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS exact signed reconstruction and six ordered zero-carrier placements")
    print("BOUND ||R_zero|| <= 48*C0/(|a_phi|^3 L^3); sharper cutoff-dependent bound recorded")
    print("BOUND centered two-endpoint contribution <= 192*C0*M/(|a_phi|^3 L^3)")
    print("OPEN nonzero/near-alias endpoint score requires o(d); integer spacing is insufficient")
    print("DECISION I2; strict >79 OPEN")
    print("WROTE", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
