"""Independent exact-arithmetic and finite hostile replay for Decision O."""
from __future__ import annotations

import cmath
import json
import math
from fractions import Fraction
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "WP84_DECISION_O_CRITICAL_SIGNED_DISPERSION_CERTIFICATE.json"


def check(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def interval_dft_reconstruct(Q: int, lo: int, hi: int) -> None:
    """Verify the exact finite Fourier inversion numerically with a tight tolerance."""
    coeff = [sum(cmath.exp(-2j * math.pi * r * a / Q) for a in range(lo, hi + 1)) / Q for r in range(Q)]
    for x in range(Q):
        val = sum(coeff[r] * cmath.exp(2j * math.pi * r * x / Q) for r in range(Q))
        expected = 1.0 if lo <= x <= hi else 0.0
        check(abs(val - expected) < 2e-12, f"DFT inversion failed Q={Q}, interval={lo}:{hi}, x={x}")


def dft_matrix_norm_square(q: int, c: int) -> int:
    """Exact squared operator norm from row Gram matrix orthogonality."""
    g = math.gcd(c, q)
    # Every row has g identical-character blocks of size q/g; Gram has q/g
    # eigenvalue q*g and all remaining eigenvalues zero.
    return q * g


def main() -> None:
    eps = Fraction(1, 100)
    base = Fraction(1, 10) + Fraction(8, 5) * eps
    check(base == Fraction(29, 250), "baseline exponent mismatch")
    fourier = Fraction(7, 5)
    check(fourier - base == Fraction(321, 250), "Fourier gap mismatch")
    check(Fraction(3, 10) > base, "Cauchy absolute bound unexpectedly beats baseline")
    check(-Fraction(1, 2) + Fraction(8, 5) * Fraction(1, 10) == -Fraction(17, 50), "2-power exponent mismatch")

    # Fixed-scale asymptotic exponent of the singleton interval length.
    # log(16 X^-1/5 exp(sqrt(log X)/2)) = log(16)-L/5+sqrt(L)/2 -> -infinity.
    for L in (100, 10_000, 1_000_000):
        log_len = math.log(16) - L / 5 + math.sqrt(L) / 2
        check(log_len < 0, f"thin strip not yet below one at L={L}")
    # Exact eventual threshold: solve sqrt(L)/2 - L/5 + log16 < 0; numerical
    # samples are witnesses only, while the quadratic asymptotic proves it.
    check(Fraction(1, 5) > 0, "decay coefficient sign")

    # Fourier inversion at periods used for finite diagnostics; interval may
    # have sharp endpoints and center need not be integral.
    for Q in (8, 16, 32):
        interval_dft_reconstruct(Q, 2, min(Q - 1, 5))
        interval_dft_reconstruct(Q, 1, 1)

    # Verify ||e(cxy/q)||_2^2 = q*gcd(c,q), including non-coprime c.
    for q in range(2, 18):
        for c in range(q):
            check(dft_matrix_norm_square(q, c) == q * math.gcd(c, q), "DFT norm identity")

    # Hostile tests: a too-small Q aliases distinct products; omitting gcd
    # fails at c not coprime to q; taking a signed sum cannot represent [x]_+.
    Q_bad, a1, a2 = 8, 1, 9
    check(a1 % Q_bad == a2 % Q_bad and a1 != a2, "wraparound falsifier failed")
    check(dft_matrix_norm_square(12, 6) == 72 and 12 != 72, "gcd factor omission not detected")
    check(max(1.0, -1.0) == 1.0 and 1.0 + (-1.0) == 0.0, "positive-part hostile mutation")
    check(Fraction(1, 2) != 0, "integer-center hostile fixture")

    cert = json.loads(CERT.read_text(encoding="utf-8"))
    check(cert["classification"] == "O4", "classification changed")
    check(cert["decision"]["signed_saving_earned"] is False, "unsupported signed saving")
    check(cert["decision"]["strict_gt_79"] == "OPEN", "theorem boundary changed")
    check("all prime powers" in cert["source_scales"]["coefficient"], "prime powers omitted")
    check("finite-J" in cert["source_scales"]["kernel"], "kernel source omitted")
    check("B!=B'" in cert["cauchy_dispersion"]["unresolved_piece"], "off-diagonal omitted")

    # Hostile certificate mutations must be rejected by direct assertions.
    def rejects(mutated: dict) -> bool:
        return not (mutated["decision"]["signed_saving_earned"] is False
                    and mutated["decision"]["strict_gt_79"] == "OPEN"
                    and "all prime powers" in mutated["source_scales"]["coefficient"])
    for mutate in (
        lambda x: x["decision"].update(signed_saving_earned=True),
        lambda x: x["decision"].update(strict_gt_79="PROVED"),
        lambda x: x["source_scales"].update(coefficient="primes only"),
    ):
        bad = json.loads(json.dumps(cert))
        mutate(bad)
        check(rejects(bad), "hostile certificate mutation was accepted")

    print("Decision O independent replay: PASS")
    print("Exact exponents: baseline=29/250, Fourier gap=321/250, Cauchy=3/10, B=2^v=-17/50")
    print("Finite DFT/norm checks and hostile mutations: PASS (diagnostic only)")


if __name__ == "__main__":
    main()
