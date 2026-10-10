#!/usr/bin/env python3
"""Deterministic producer for the Decision L source-scope certificate."""
from __future__ import annotations

import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificates" / "WP84_DECISION_L_SQUARE_ROOT_PRODUCT_FIRST_ALIAS_CERTIFICATE.json"


def d3(n: int) -> int:
    return sum(1 for a in range(1, n + 1) for b in range(1, n // a + 1)
               if n % (a * b) == 0)


def power_pool(n: int) -> list[int]:
    out: set[int] = set()
    for p in range(2, n + 1):
        if any(p % q == 0 for q in range(2, math.isqrt(p) + 1)):
            continue
        v = p
        while v <= n:
            out.add(v)
            v *= p
    return sorted(out)


def finite_checks() -> dict:
    pp = power_pool(50)
    ordered_checks = 0
    repeated_base_seen = proper_power_seen = False
    for y in range(1, 51):
        grouped: dict[int, int] = {}
        for a in pp:
            for b in pp:
                for c in pp:
                    p = a * b * c
                    if p <= y:
                        grouped[p] = grouped.get(p, 0) + 1
                        repeated_base_seen |= a == b or b == c or a == c
                        proper_power_seen |= any(
                            x == r**k for x in (a, b, c)
                            for r in range(2, math.isqrt(x) + 1)
                            for k in range(2, 10))
        for p, count in grouped.items():
            assert count <= d3(p)
            ordered_checks += 1
    return {"power_pool_limit": 50, "ordered_divisor_checks": ordered_checks,
            "repeated_prime_power_base_seen": repeated_base_seen,
            "proper_power_seen": proper_power_seen,
            "scope": "finite exact combinatorial check only"}


def main() -> None:
    cert = {
        "title": "WP84 Decision L: square-root product separation and first-alias discharge",
        "start": {"branch": "codex/c5-c6-attack-20261006",
                  "head": "c53eaebd18d9da95eefc629d46677798cc699063"},
        "source": {"X": "T/(2*pi)", "L": "log(X)",
                   "N": "floor(X*exp(-sqrt(L)))", "d": "floor(X*L)",
                   "M": "ceil(d*exp(-sqrt(L)/2))",
                   "coefficients": "-Lambda(n)/(a_phi(T)*L*sqrt(n))",
                   "pool": "all prime powers p^v<=N",
                   "operator": "original finite J; every finite path lag retained",
                   "fixed_R_consumer_transfer": "none; ordinary-prime R=6000 estimates are not used"},
        "candidate_A": {
            "product_gap": "A,B positive integers; A*B<=Y and A!=B imply |log(A/B)|>=log(1+1/min(A,B))>=1/(sqrt(Y)+1)",
            "range": "fixed 0<theta<1; Y=X^theta; n1*n2*n3<=Y; Omega!=0",
            "frequency": "1/(L*(sqrt(Y)+1))<=|Omega|/L<=theta; no integer alias",
            "kernel": "|K_center|<=2*theta/sin(pi*theta)*L*(sqrt(Y)+1)",
            "coefficient_sum": "O_theta(sqrt(Y)*log(Y)^5/L^3)",
            "lag_mass": "(1+2*zeta(3/2)/pi^(3/2))^2",
            "endpoint": "O_theta(Y*log(Y)^5/L^2)",
            "normalized": "O_theta(X^(theta-1)*L^2)=o(1)",
            "decision": "proved for every fixed theta<1; not theta=1"},
        "candidate_B": {
            "signs": "+++ and ---",
            "first_bin": "X^(1/2)<=P=n1*n2*n3<=X^(3/2)",
            "exact_group": "sum ordered p_i^v_i factorizations at P; keep coefficient signs, exp(+-i*T*log(P)), all f filters, exact displacement exp(2*pi*i*(sigma2*l1*alpha2+sigma3*(l1+l2)*alpha3)), finite K_center",
            "kernel_near": "X/e<=P<=eX: for P!=X, O(min(M,L*X/|P-X|)); exact P=X charged by O(M)",
            "nearest_integers": "at most two P with |P-X|<1 charged separately by O(M), including noninteger X arbitrarily close to an integer",
            "harmonic_sum": "sum_{X/e<=P<=eX, |P-X|>=1} 1/|P-X|=O(log(X+2))",
            "pointwise_divisor": "d3(P)<<epsilon P^epsilon; near normalized O_epsilon(X^(epsilon-1/2)*(L+exp(-sqrt(L)/2)))",
            "far_kernel": "outside [X/e,eX] within the first bin, |K_center|=O(L)",
            "weighted_divisor": "sum_{P<=Z}d3(P)/sqrt(P)=O(sqrt(Z)*(1+log(Z))^2)",
            "far_normalized": "O(X^(-1/4)*L^2)",
            "conclusion": "complete same-sign m=+1 and m=-1 first-alias bins are o(d)"},
        "surviving_population": {
            "exact_partition": ["Omega=0", "Omega!=0 and total product<=X^theta",
                                "same-sign first bin and total product>X^theta",
                                "mixed-sign total product>X^theta",
                                "same-sign outside first bin and total product>X^theta"],
            "remaining_threshold": "for every fixed 0<epsilon<1 choose theta=1-epsilon; remaining total product>X^(1-epsilon)",
            "mixed_coherent_aliases": "m=+1 for two-plus/one-minus; m=-1 for reciprocal; m=+/-2 centers inaccessible but shrinking fringes remain",
            "mixed_first_alias_product": "A/B>=X*exp(-L/M), B>=2 implies total product AB>=4*X*exp(-L/M)>X^theta for every fixed theta<1 eventually",
            "same_sign": "m=+/-2 centers can occur; m=+/-3 centers inaccessible but O(L^-1/2) frequency fringes remain",
            "other_unpaid": "nonzero central fringe; all shrinking alias fringes; fixed-gap high-product complement"},
        "high_product": {
            "global_absolute": "O(X^(3/2)*exp(-2*sqrt(L))/L^3), grows",
            "fixed_gap": "O_delta(X^(1/2)*exp(-3*sqrt(L)/2)/L^4), grows",
            "mixed_m1_core_and_central_fringe": "O(X^(3/2)*exp(-2*sqrt(L))/L^3), grows",
            "mixed_m2_fringe": "cutoff separation yields kernel O(sqrt(L)); normalized O(X^(1/2)*exp(-3*sqrt(L)/2)/L^(7/2)), grows",
            "same_sign_m2_near": "O_epsilon(X^(2*epsilon)*L), insufficient",
            "same_sign_m2_far": "O(X^(1/4)*L^2), insufficient",
            "same_sign_m3_cutoff_fringe": "kernel O(sqrt(L)); normalized weighted-d3 estimate O(X^(1/2)*exp(-3*sqrt(L)/2)*L^(3/2)), grows",
            "first_missing": "source-weighted signed multilinear estimate for exact dyadic prime-power cubic sums, all phases/filters/finite roots/centering, uniform in T and endpoint position, total o(d)"},
        "decision": "L2",
        "strict_gt79": "OPEN",
        "other_frozen_gates": "m3=2, Cayley energy<0.105, signed fifth/sixth, prime-to-Weil, zero-side, determinant compatibility remain OPEN",
        "finite_checks": finite_checks()}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(cert, indent=2) + "\n", encoding="utf-8")
    print("WROTE", OUT.relative_to(ROOT))
    print("DECISION L2; theta<1 low-product sector and complete same-sign first alias are o(d); high-product mixed and higher aliases remain open")


if __name__ == "__main__":
    main()
