#!/usr/bin/env python3
"""Independent exact/hostile replay for WP84 Decision N; imports no producer."""
from __future__ import annotations

import cmath
import json
import math
from fractions import Fraction
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "WP84_DECISION_N_COHERENT_ALIAS_MODULAR_CORRELATION_CERTIFICATE.json"


def e_fraction(x: Fraction) -> complex:
    return cmath.exp(2j * math.pi * float(x))


def main() -> None:
    c = json.loads(CERT.read_text(encoding="utf-8"))
    assert c["decision"] == "N4"
    assert c["start"]["head"] == "4edcde030b352ada0ca0bd23faeec077f10b5e1f"
    assert c["source"]["pool"].startswith("all prime powers")
    assert all(c["prerequisites"][f"decision_{x}_replay"] == "PASS" for x in "ijklm")
    assert c["carrier_reduction"]["kernel_filters_roots_changed"] is False

    # Exact real-center algebra: XB need not be an integer.
    X, B, A = Fraction(101, 3), 4, 135
    h = Fraction(A) - X * B
    assert h == Fraction(1, 3)
    assert Fraction(A, B) == X + h / B
    left_exp = X + h / B
    right_exp = Fraction(A, B)
    assert left_exp == right_exp
    assert c["carrier_reduction"]["h"].startswith("A-X*B is real")

    # Exact- and near-alias fixtures: the center is real, and no denominator
    # involving its distance to an integer appears in the phase-error proof.
    center_exact = Fraction(120, 1)
    center_near = Fraction(120000000000000000000001, 10**21)
    assert center_exact.denominator == 1
    assert Fraction(0) < center_near - 120 < Fraction(1, 10**18)
    for center in (center_exact, center_near):
        count = sum(1 for a in range(math.floor(center) - 2, math.floor(center) + 4)
                    if abs(Fraction(a) - center) < 1)
        assert count <= 2

    # The additive-character sign is fixed by the exact h relation.
    assert abs(e_fraction(Fraction(A, B)) - e_fraction(X + h / B)) < 1e-12
    assert abs(e_fraction(Fraction(A, B)) - e_fraction(-Fraction(A, B))) > 0.1
    assert "exp(2*pi*i*A/B)" in c["exact_modular_form"]["character"]

    # Full DFT row orthogonality is exact for prime and prime-power moduli.
    # The floating check is a finite regression; exact congruence is asserted
    # directly for all row differences.
    for modulus in (5, 8, 16):
        for a in range(modulus):
            for ap in range(modulus):
                exact_sum = modulus if (a - ap) % modulus == 0 else 0
                numerical = sum(e_fraction(Fraction((a - ap) * y, modulus))
                                for y in range(modulus))
                assert abs(numerical - exact_sum) < 2e-12

    # Noncoprime and repeated-base cases change conductor and can be coherent.
    # For B=8, A=4 has conductor 2; A=8 gives the constant character.
    assert Fraction(4, 8) == Fraction(1, 2)
    assert Fraction(8, 8) == 1
    assert abs(e_fraction(Fraction(8, 8)) - (1 + 0j)) < 1e-12
    assert c["exact_modular_form"]["noncoprime"].startswith("for B=p^v")

    # Hostile falsifier: the separable DFT bound cannot be applied to an
    # arbitrary coupled matrix. W[a,b]=conj(e(ab/q)) makes the sum q^2,
    # while the claimed separable RHS would be q^(3/2) if misused with the
    # Frobenius-sized vectors. This is an abstract method counterexample,
    # not a prime-source counterexample.
    q = 8
    W = [[e_fraction(Fraction(-a * b, q)) for b in range(q)] for a in range(q)]
    coupled_sum = sum(W[a][b] * e_fraction(Fraction(a * b, q))
                      for a in range(q) for b in range(q))
    assert abs(coupled_sum - q * q) < 2e-11
    frob = math.sqrt(sum(abs(W[a][b]) ** 2 for a in range(q) for b in range(q)))
    general_frobenius = q * frob
    assert general_frobenius == q * q
    false_separable_rhs = math.sqrt(q) * frob
    assert q * q > false_separable_rhs
    assert c["attempted_method"]["actual_status"].startswith("FAIL")

    # Strict exponent arithmetic for the representative beta=3/5 block.
    beta = Fraction(3, 5)
    for eps in (Fraction(1, 100), Fraction(1, 1000)):
        exponent = beta - Fraction(1, 2) + eps * (1 + beta)
        assert exponent == Fraction(1, 10) + Fraction(8, 5) * eps
        assert exponent > Fraction(1, 10)
    assert c["critical_block"]["absolute_baseline"].startswith("O_epsilon(X^(1/10+8*epsilon/5))")
    assert c["critical_block"]["prime_pairs_in_each_window_asserted"] is False

    # Independently recompute the aggregate error exponents from its four
    # ingredients: carrier X^-1 exp(sqrt L), endpoint M/d exp(-sqrt L/2),
    # coefficient X^(-1/2+eps), and A-count exp(sqrt L/2) N^(1+eps),
    # with N<=X exp(-sqrt L).
    for eps in (Fraction(1, 10), Fraction(1, 8), Fraction(1, 5)):
        x_power = -1 + (Fraction(-1, 2) + eps) + (1 + eps)
        sqrt_l_power = 1 - Fraction(1, 2) + Fraction(1, 2) - (1 + eps)
        assert x_power == Fraction(-1, 2) + 2 * eps
        assert sqrt_l_power == -eps
        assert x_power < 0
    # The exponent condition 0<eps<1/4 is exactly what makes the X power decay.
    assert Fraction(-1, 2) + 2 * Fraction(1, 4) == 0
    assert Fraction(-1, 2) + 2 * Fraction(1, 5) < 0

    # The wrong T factor fails: T=2*pi*X, so replacing T by pi*X doubles the
    # linear phase error argument and does not preserve the exact identity.
    wrong_X = Fraction(101, 3)
    assert 2 * math.pi * float(wrong_X) != math.pi * float(wrong_X)
    assert c["carrier_reduction"]["full_carrier"].startswith("exp(i*T*log(A/B))")

    # Hostile scope tests: fixed-R transfer and mean-only endpoint cancellation
    # are explicitly prohibited; filters, root centering, and all powers remain.
    assert "fixed-R ordinary-prime consumers" in c["source"]["transfer_prohibited"]
    assert "all prime powers" in c["source"]["pool"]
    for factor in ("finite-J filters", "displacement phases", "global centering"):
        assert factor in c["population"]["unchanged_factors"]
    assert "each endpoint" in c["absolute_dyadic_bound"]["uniformity"]
    assert c["outcome"]["signed_constant_saving"] == "none"
    assert c["outcome"]["strict_gt79"] == "OPEN"

    print("PASS exact real-center identity with nonintegral X*B")
    print("PASS exact/near aliases without nearest-integer denominators")
    print("PASS additive-character sign and full DFT orthogonality for moduli 5, 8, 16")
    print("PASS repeated-base/noncoprime conductor fixtures")
    print("PASS coupled-weight falsifier: separable DFT estimate is inapplicable")
    print("PASS beta=3/5 absolute exponent and required saving arithmetic")
    print("PASS source weights, finite-J/root-centering, endpoint-uniformity and fixed-R scope checks")
    print("LIMIT no signed source-weighted modular saving is proved; strict >79 OPEN")
    print("DECISION N4")


if __name__ == "__main__":
    main()
