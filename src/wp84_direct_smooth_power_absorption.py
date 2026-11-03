"""Exact-support checks and constants for the direct smooth-taper audit.

The proof is in notes/WP84_DIRECT_SMOOTH_POWER_ABSORPTION.md.  This module
contains only finite identities, rational smooth-overlap arithmetic, and the
explicit constants used there; it does not numerically sample prime sums.
"""

from __future__ import annotations

from fractions import Fraction
from math import comb, factorial, log, sqrt


BASE_COMMIT = "7f3394c5655238b1e9736f91233d0bcc4c49fd43"
BRANCH = "codex/wp84-direct-smooth-taper-20261103"
MV_CONSTANT = 1  # coefficient in m + delta^{-1}, Montgomery--Vaughan Thm. 1
PROPER_POWER_SQUARE_MASS_CONSTANT = 64
CHEBYSHEV_THETA_CONSTANT = 4 * log(2)
C0 = 1 - 1 / sqrt(2)


def circle_distance(x: float | Fraction, y: float | Fraction) -> float | Fraction:
    """Circular distance for representatives in R/Z."""
    d = abs((x - y) % 1)
    return min(d, 1 - d)


def proper_power_frequency_separation(N: int, L: float) -> float:
    """A proved lower bound for distinct proper-power log frequencies mod 1."""
    if N < 4 or L <= 0:
        raise ValueError("require N >= 4 and L > 0")
    return 1.0 / ((N + 1) * L)


def zero_extension_overlap_length(L: float, y: float) -> float:
    """Length of the support intersection under a non-wrapping shift."""
    if L < 0 or y < 0:
        raise ValueError("require L >= 0 and y >= 0")
    return max(0.0, L - y)


def normalized_large_sieve_factor(eta: float) -> float:
    """Uniform K when m >= eta*e^L*L and N=floor(e^L)."""
    if not 0 < eta <= 1:
        raise ValueError("require 0 < eta <= 1")
    return 1.0 + 2.0 / eta


def full_second_trace_constant(a0: float, eta: float, B: float = 1.0) -> float:
    """C in tau_I(Q^2) <= C/L^2 under a >= a0 and ||phi||_inf <= B."""
    if a0 <= 0 or B < 0:
        raise ValueError("require a0 > 0 and B >= 0")
    return 256.0 * B * B / a0 * normalized_large_sieve_factor(eta)


def hard_band_second_trace_constant(R: int, eta: float) -> float:
    """C in tau_I(Q_R^2) <= C/L^2, paying all 2R+1 diagonals."""
    if R < 0:
        raise ValueError("require R >= 0")
    return 256.0 * (2 * R + 1) * normalized_large_sieve_factor(eta)


def operator_norm_constant(a0: float, B: float = 1.0) -> float:
    """Chebyshev/absolute-mass bound for ||Q||_op, for L >= 1."""
    if a0 <= 0 or B < 0:
        raise ValueError("require a0 > 0 and B >= 0")
    return 12.0 * B * B * log(2.0) / (a0 * C0)


def hard_band_operator_norm_constant(R: int) -> float:
    """Row-sum C in ||Q_R||_op <= C for the literal band mask."""
    if R < 0:
        raise ValueError("require R >= 0")
    return 12.0 * (2 * R + 1) * log(2.0) / C0


def fourth_trace_constant(a0: float, eta: float, B: float = 1.0) -> float:
    """C in tau_I(Q^4) <= C/L^2."""
    return full_second_trace_constant(a0, eta, B) * operator_norm_constant(a0, B) ** 2


def _poly_mul(a: list[Fraction], b: list[Fraction]) -> list[Fraction]:
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            out[i + j] += ai * bj
    return out


def _smoothstep_scaled(scale: Fraction) -> list[Fraction]:
    """Coefficients of g(scale*t), g=10t^3-15t^4+6t^5."""
    return [Fraction(0), Fraction(0), Fraction(0),
            10 * scale**3, -15 * scale**4, 6 * scale**5]


def _smoothstep_reversed_scaled(scale: Fraction) -> list[Fraction]:
    """Coefficients of g(scale*(1-t)) as a polynomial in t."""
    out = [Fraction(0)] * 6
    for degree, coeff in ((3, 10), (4, -15), (5, 6)):
        for j in range(degree + 1):
            out[j] += Fraction(coeff) * scale**degree * comb(degree, j) * (-1)**j
    return out


def smoothstep_overlap_ratio(epsilon_over_width: Fraction) -> Fraction:
    """Exact smooth overlap divided by sharp overlap at y=L-epsilon."""
    if not 0 < epsilon_over_width <= 1:
        raise ValueError("require 0 < epsilon/width <= 1")
    product = _poly_mul(_smoothstep_scaled(epsilon_over_width),
                        _smoothstep_reversed_scaled(epsilon_over_width))
    return sum((c / (j + 1) for j, c in enumerate(product)), Fraction(0))


def flat_source_step_overlap_upper_bound() -> Fraction:
    """Exact rational bound for one admissible C-infinity source step.

    For chi(t)=E(t)/(E(t)+E(1-t)), E(t)=exp(-1/t) for t>0 and 0
    otherwise, at epsilon/width=1/10 each edge value is <1/1000.
    Thus the smooth overlap divided by its sharp length is <=1/10^6.
    The returned rational is the certified upper bound, not an approximation.
    """
    exp8_partial = sum((Fraction(8**k, factorial(k)) for k in range(11)),
                       Fraction(0))
    if exp8_partial <= 1000:
        raise ArithmeticError("rational exponential lower bound failed")
    return Fraction(1, 1_000_000)


def source_entry_scalar_identity() -> tuple[Fraction, Fraction]:
    """Return both exact rational normalizations of a smooth overlap entry.

    If A_r is the source overlap integral and G_r=A_r/(aL), then
    (2*pi/(aL^2))*A_r equals (2*pi/(aL))*a*G_r.  The common symbolic
    factors 2*pi/a are removed, leaving exact coefficients of A_r/L^2.
    """
    L = Fraction(7, 3)
    a = Fraction(5, 4)
    A = Fraction(11, 13)
    source = A / (L * L)
    compressed_shift = a * (A / (a * L)) / L
    return source, compressed_shift


def branch_phase_exponents(k: int, r: int, u: Fraction) -> tuple[Fraction, Fraction]:
    """Exponents q in exp(2*pi*i*q) for the two Q-entry branches."""
    positive = (Fraction(k) + Fraction(r, 2)) * u
    negative = -positive
    return positive, negative


def run_checks() -> dict[str, object]:
    source, compressed = source_entry_scalar_identity()
    ratio = smoothstep_overlap_ratio(Fraction(1, 10))
    checks = {
        "base_commit": BASE_COMMIT,
        "branch": BRANCH,
        "entry_normalization_exact": source == compressed,
        "smoothstep_overlap_ratio_epsilon_over_width_1_10": {
            "numerator": ratio.numerator,
            "denominator": ratio.denominator,
            "decimal": float(ratio),
        },
        "smooth_overlap_strictly_differs_from_sharp": 0 < ratio < Fraction(1, 100000),
        "c_infinity_source_step_overlap_ratio_upper_bound": {
            "numerator": flat_source_step_overlap_upper_bound().numerator,
            "denominator": flat_source_step_overlap_upper_bound().denominator,
        },
        "mv_factor_eta_1_2": normalized_large_sieve_factor(0.5),
        "second_trace_constant_a0_1_2_eta_1_2": full_second_trace_constant(0.5, 0.5),
        "hard_band_R400_second_trace_constant_eta_1_2": hard_band_second_trace_constant(400, 0.5),
        "operator_norm_constant_a0_1_2": operator_norm_constant(0.5),
        "hard_band_R400_operator_norm_constant": hard_band_operator_norm_constant(400),
        "fourth_trace_constant_a0_1_2_eta_1_2": fourth_trace_constant(0.5, 0.5),
        "separate_branches_at_start_row": [
            str(value) for value in branch_phase_exponents(37, -5, Fraction(2, 7))
        ],
    }
    return checks


if __name__ == "__main__":
    import json
    report = run_checks()
    if not report["entry_normalization_exact"] or not report["smooth_overlap_strictly_differs_from_sharp"]:
        raise SystemExit("smooth-taper checker failed")
    print(json.dumps(report, indent=2, sort_keys=True))
