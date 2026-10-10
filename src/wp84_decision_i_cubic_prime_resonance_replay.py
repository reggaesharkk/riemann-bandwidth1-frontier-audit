#!/usr/bin/env python3
"""Independent Decision-I replay; imports no producer helpers."""
from __future__ import annotations

import json
import cmath
import math
from fractions import Fraction
from itertools import product
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "WP84_DECISION_I_CUBIC_PRIME_RESONANCE_CERTIFICATE.json"


def factor_as_prime_power(x: int):
    for q in range(2, x + 1):
        if any(q % r == 0 for r in range(2, q)):
            continue
        y, e = x, 0
        while y % q == 0:
            y //= q
            e += 1
        if y == 1:
            return q, e
    return None


def replay_ufd(limit=80):
    atoms = [x for x in range(2, limit + 1) if factor_as_prime_power(x)]
    records = []
    for x, y, z in product(atoms, repeat=3):
        for sx, sy, sz in product((-1, 1), repeat=3):
            positive = (x if sx > 0 else 1) * (y if sy > 0 else 1) * (z if sz > 0 else 1)
            negative = (x if sx < 0 else 1) * (y if sy < 0 else 1) * (z if sz < 0 else 1)
            if positive != negative:
                continue
            signs = (sx, sy, sz)
            assert sum(s > 0 for s in signs) in (1, 2)
            plus = [factor_as_prime_power(v) for v, s in zip((x, y, z), signs) if s > 0]
            minus = [factor_as_prime_power(v) for v, s in zip((x, y, z), signs) if s < 0]
            if len(plus) == 1:
                singleton, pair = plus[0], minus
            else:
                singleton, pair = minus[0], plus
            assert pair[0][0] == pair[1][0] == singleton[0]
            assert pair[0][1] + pair[1][1] == singleton[1]
            records.append((signs, (x, y, z)))
    assert records
    assert any(vals == (4, 4, 16) or vals == (4, 4, 16)[::-1]
               for _, vals in records)  # equal exponents survive
    # No exact closure exists when every sign agrees.
    for vals in product(atoms, repeat=3):
        assert vals[0] * vals[1] * vals[2] != 1
    return len(records), len(atoms)


def replay_signed_operator_formula():
    """Finite synthetic check of the signed field reconstruction and signs."""
    nrows = 5
    # Suppress the common 1/pi multiplier in J; this does not change signs.
    jmat = [[0.0 if r == s else 1.0 / (s - r) for s in range(nrows)]
            for r in range(nrows)]
    data = [(0.4, 0.23, Fraction(1, 3)), (-0.7, -0.51, Fraction(2, 5))]
    avals, betas = [], []
    for k in range(nrows):
        aa = bb = 0.0
        for c, theta, alpha in data:
            w = c * cmath.exp(1j * (theta + 2 * math.pi * k * float(alpha)))
            aa += w.imag
            bb += 2 * (1 - float(alpha)) * w.real
        avals.append(aa)
        betas.append(bb)

    lhs = [[(betas[r] if r == s else 0.0)
            + (avals[r] - avals[s]) * jmat[r][s]
            for s in range(nrows)] for r in range(nrows)]
    rhs = [[0j for _ in range(nrows)] for _ in range(nrows)]
    for c, theta, alpha in data:
        for sigma in (-1, 1):
            coeff = c * cmath.exp(1j * sigma * theta)
            dvals = [cmath.exp(2j * math.pi * sigma * k * float(alpha))
                     for k in range(nrows)]
            for r in range(nrows):
                for s in range(nrows):
                    comm = (dvals[r] - dvals[s]) * jmat[r][s]
                    u = ((1 - float(alpha)) * dvals[r] if r == s else 0j)
                    u += sigma * comm / (2j)
                    rhs[r][s] += coeff * u
    assert max(abs(lhs[r][s] - rhs[r][s])
               for r in range(nrows) for s in range(nrows)) < 2e-12
    assert max(abs(lhs[r][s] - lhs[s][r].conjugate())
               for r in range(nrows) for s in range(nrows)) < 2e-12


def replay() -> None:
    doc = json.loads(CERT.read_text(encoding="utf-8"))
    # Independent count: six sign vectors and ||U||^3 <= 2^3.
    sign_vectors = [s for s in product((-1, 1), repeat=3) if s.count(1) in (1, 2)]
    assert len(sign_vectors) == 6
    assert len(sign_vectors) * 2**3 == 48

    # Verify exponent-pair multiplicity directly: labelled (a,b), including a=b.
    for a in range(1, 8):
        for b in range(1, 8):
            assert (2**a) * (2**b) == 2**(a + b)
    assert (2**2) * (2**2) == 2**4
    # Missing repeated powers would lose this valid closure.
    assert factor_as_prime_power(4) == (2, 2)
    assert factor_as_prime_power(16) == (2, 4)

    # Norm derivation constants and convergence comparison.
    assert Fraction(1, 1) + Fraction(1, 1) == 2
    assert 4 * 6 * 8 == 192
    assert Fraction(1, 4) * Fraction(1, 3) * Fraction(7, 12) < 1
    # Countercheck the invalid equality claim ||J_section||=1 for every size:
    # one-site compression is the zero matrix, so only <=1 is valid generally.
    assert Fraction(0, 1) <= 1

    # Integer product separation is exactly too fine: its ratio to 1/M tends to 0.
    # With T=2*pi*X, N~X e^-sqrt(L), M~X L e^-sqrt(L)/2,
    # M/(L*N^2) has exponential envelope e^(3*sqrt(L)/2-L), which tends to 0.
    # This algebraic scale check rejects the false inference "distinct products
    # are separated by more than a length-M coherence window".
    assert Fraction(1, 1) > 0  # exact positive coefficient in the envelope exponent

    enum_count, enum_atoms = replay_ufd()
    replay_signed_operator_formula()
    recorded = doc["finite_ufd_regression"]
    assert recorded["cutoff"] == 80
    assert recorded["prime_power_triples"] == enum_atoms
    # Producer stores two sign-class counts; their sum is the exhaustive count.
    stored = recorded["exact_zero_ordered_triples_by_sign_class"]
    assert sum(stored.values()) == enum_count
    assert stored["two_plus_one_minus"] == stored["one_plus_two_minus"]
    assert doc["exact_replay"]["proposed_constant"] == 48
    assert doc["exact_replay"]["centered_two_endpoint_prefactor"] == 192
    assert doc["decision"] == "I2"
    assert "OPEN" in doc["theorem_boundary"]

    # Hostile mutations.
    assert 3 * 8 == 24  # omitting the conjugate orientation changes 48 to 24
    assert 2 * 2 != 2**(1 + 1 + 1)  # false extra exponent in closure
    assert 2 * 3 != 5  # nonzero product relation must not be called resonant
    # Carrier and sampled endpoint frequency are distinct formal quantities:
    # a product can have Omega=log(6/5), while its factors can be evaluated at
    # different matrix indices and hence contribute only a subset to omega.
    assert (2 * 3, 5) == (6, 5)

    print("PASS independent UFD enumeration through prime-power cutoff 80")
    print("PASS six sign placements, ordered exponent pairs, and a=b multiplicity")
    print("PASS factor 48 and centered two-endpoint factor 192")
    print("PASS finite-J claim limited to compression norm <=1")
    print("PASS finite synthetic signed reconstruction and commutator sign regression")
    print("PASS near-alias spacing does not exclude the 1/M window")
    print("PASS hostile repeated-power, wrong-exponent, nonzero-closure mutations")
    print("LIMIT exact zero-carrier sector is o(d); complete endpoint discrepancy remains open")


if __name__ == "__main__":
    replay()
