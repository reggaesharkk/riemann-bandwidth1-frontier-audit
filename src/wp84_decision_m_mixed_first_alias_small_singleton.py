#!/usr/bin/env python3
"""Deterministic symbolic/formal certificate producer for WP84 Decision M."""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificates" / "WP84_DECISION_M_MIXED_FIRST_ALIAS_SMALL_SINGLETON_CERTIFICATE.json"


def d2(n: int) -> int:
    return sum(1 for a in range(1, n + 1) if n % a == 0)


def prime_powers(limit: int) -> set[int]:
    result: set[int] = set()
    for p in range(2, limit + 1):
        if any(p % q == 0 for q in range(2, math.isqrt(p) + 1)):
            continue
        v = p
        while v <= limit:
            result.add(v)
            v *= p
    return result


def finite_checks() -> dict:
    pp = prime_powers(120)
    pair_total = 0
    pp_pair_total = 0
    repeated = proper = False
    products: dict[int, int] = {}
    for a in pp:
        for b in pp:
            products[a * b] = products.get(a * b, 0) + 1
            pair_total += 1
            pp_pair_total += 1
            repeated |= a == b or (a != b and any(
                p ** i == a and p ** j == b
                for p in range(2, 11) for i in range(1, 8) for j in range(1, 8)))
            proper |= any(a == p**k or b == p**k for p in range(2, 11) for k in range(2, 8))
    for product, count in products.items():
        assert count <= d2(product)
    assert {4, 8, 9, 16, 25, 27, 32, 49, 64, 81} <= pp
    assert products[4] >= 1  # ordered (2,2), not discarded
    return {"prime_power_pool_limit": 120, "ordered_prime_power_pairs": pp_pair_total,
            "distinct_products_checked": len(products), "repeated_or_related_bases_seen": repeated,
            "proper_powers_seen": proper,
            "ordered_pair_count_le_d2": True,
            "scope": "finite exact multiplicity regression only"}


def main() -> None:
    cert = {
        "title": "WP84 Decision M: mixed first-alias small-singleton discharge",
        "decision": "M2",
        "start": {"branch": "codex/c5-c6-attack-20261006",
                  "head": "e502bf1ab5fa9b1dd75e8c9de3ccbb9e01186f8d"},
        "source": {"X": "T/(2*pi)", "L": "log(X)",
                   "N": "floor(X*exp(-sqrt(L)))", "d": "floor(X*L)",
                   "M": "ceil(d*exp(-sqrt(L)/2))",
                   "coefficients": "c_n=-Lambda(n)/(a_phi(T)*L*sqrt(n))",
                   "pool": "all prime powers p^v<=N, including proper powers",
                   "operator": "original compressed finite J; all lag paths and exact finite roots",
                   "kernel": "K_center(endpoint intersection) - (|E|/d)*K_center(full root set)",
                   "path_mass": "W3 <= (1+2*zeta(3/2)/pi^(3/2))^2",
                   "consumer_scope": "original direct same-section endpoint cubic only; no fixed-R ordinary-prime transfer"},
        "exact_mixed_source_term": {
            "orientation_plus": "A=n1*n2; B=n3; Omega=log(A/B); delta=log(A/(X*B))",
            "orientation_reflected": "A=n1; B=n2*n3; Omega=log(B/A), reciprocal m=-1 bin",
            "alias_bin": "X^(1/2)*B <= A <= X^(3/2)*B",
            "summand": "c_n1*c_n2*c_n3*exp(i*T*Omega)*product_j f_(ell_j)^sigma_j(alpha_nj)*exp(2*pi*i*(sigma2*q1*alpha_n2+sigma3*q2*alpha_n3))*K_center(E,ell,Omega)",
            "lags": "ell1+ell2+ell3=0; q0=0,q1=ell1,q2=ell1+ell2",
            "retained": ["all prime powers", "actual carrier", "all finite-J roots", "exact displacement phase", "global centering", "ordered factorizations", "both endpoint sides"]},
        "kernel": {
            "global": "|K_center|<=2*min(M,1/|sin(pi*Omega/L)|); exact integer frequency <=2M",
            "near_nonexact": "for C=X*B, A in [C/e,e*C], A!=C: <=C0*min(M,L*C/|A-C|)",
            "near_exact": "A=C separately charged by 2M; never divide by zero",
            "integer_harmonic": "sum_(A integer in [C/e,e*C]) capped(M at equality; min(M,L*C/|A-C|) otherwise) <= C1*(M+L*C*log(C+2))",
            "reason": "at most three integers within distance <1 after equality convention, at most two per unit shell"},
        "divisor_and_weight": {
            "coefficient": "Lambda(n)<=log(n)<L and a_phi(T)->1 imply |c_n1*c_n2*c_B|<=C/sqrt(A*B)",
            "ordered_pair_multiplicity": "<=d2(A), with exact ordered positive-integer pair divisor count",
            "pointwise": "d2(A)<=C_epsilon*A^epsilon; uniform C_epsilon justified by Euler factors (a+1)",
            "weighted": "sum_(A<=Y)d2(A)/sqrt(A)<=C*sqrt(Y)*log(Y+2), from sum_(A<=Y)d2(A)<=Y*(1+log Y) and partial summation",
            "prime_power_handling": "allowed factor pairs and singleton prime powers are subsets of integer sums; no prime-power term is dropped"},
        "candidate_A_near": {
            "claim": "for fixed 0<=eta<1/2 and Z=X^eta, normalized mixed first-alias |delta|<=1 contribution is o(1)",
            "unnormalized": "O_epsilon(X^(epsilon-1/2)*M*Z^epsilon + X^(epsilon+1/2)*L^2*Z^(1+epsilon))",
            "normalized": "O_epsilon,eta(X^(-1/2+epsilon*eta)*exp(-sqrt(L)/2) + X^(-1/2+eta+epsilon*(1+eta))*L)",
            "epsilon_condition": "0<epsilon<(1/2-eta)/(1+eta)",
            "endpoint_eta": "eta=1/2 not proved: no positive epsilon meets condition; eta=0 singleton set is empty"},
        "candidate_B_full_bin": {
            "far_region": "1<|delta|<=L/2; |K_center|<=L",
            "normalized_far": "O(X^(-1/4)*Z*log(X^(3/2)*Z+2)) = O_eta(X^(-1/4+eta)*L)",
            "near_plus_far": "o(1) for every fixed 0<=eta<1/4, with Z=X^eta",
            "endpoint_eta": "eta=1/4 not proved: far estimate is O(L)",
            "requested_form": "implies O(X^(-1/4+epsilon)*Z^(1+epsilon)*L^C), e.g. any epsilon>0 and C=1 after enlargement"},
        "population_partition": {
            "low_cutoff": "choose X^(1/3) within Decision L's fixed-theta<1 low-product theorem",
            "classes_in_order": ["Omega=0 exact (Decision I)", "Omega!=0 and product<=X^(1/3) (Decision L/K)", "same-sign first bin (Decision L)", "mixed-sign first bin with B<=X^eta, split near/far (Decision M)", "all remaining high-product mixed/same-sign populations"],
            "newness": "mixed first bin has total product AB=(A/B)*B^2>=4*sqrt(X)>X^(1/3); unit core has AB=X*exp(delta)*B^2>=4X/e>X^(1/3)",
            "nonoverlap": "mixed-sign M class is disjoint by sign from same-sign L class and by total product from the chosen low class"},
        "residual": {
            "unpaid": ["mixed m=+/-1 with B>X^eta", "mixed m=+/-2 shrinking fringes", "same-sign m=+/-2 core/fringe", "same-sign m=+/-3 cutoff fringe", "fixed-gap high-product complement", "remaining endpoint-centered signed sum"],
            "inherited_global_normalized": "O(X^(3/2)*exp(-2*sqrt(L))/L^3), grows",
            "inherited_fixed_gap_normalized": "O_delta(X^(1/2)*exp(-3*sqrt(L)/2)/L^4), grows",
            "first_required_theorem": "source-weighted signed multilinear estimate for residual dyadic prime-power products retaining carrier, filters, displacement phases, exact roots and centering, uniform in T and endpoint, with combined contribution o(d)",
            "no_counterexample": True},
        "ordinary_prime_R6000_boundary": "WP84_HIGH_PRODUCT_SIGNED_FEASIBILITY and fixed-R near-alias audits concern a distinct ordinary-prime masked moment consumer; no estimate transfers to this full prime-power finite-J matrix.",
        "frozen_gates": {"m3=2": "OPEN", "conditioned_Cayley_energy_lt_0.105": "OPEN",
                         "signed_fifth_sixth_gate": "OPEN", "prime_to_Weil": "OPEN",
                         "zero_side_transfer": "OPEN", "determinant_compatibility": "OPEN",
                         "strict_gt79": "OPEN"},
        "finite_checks": finite_checks(),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(cert, indent=2) + "\n", encoding="utf-8")
    print(f"WROTE {OUT.relative_to(ROOT)}")
    print("DECISION M2; near eta<1/2 and complete first bin eta<1/4 are o(d); residual signed high products remain open")


if __name__ == "__main__":
    main()
