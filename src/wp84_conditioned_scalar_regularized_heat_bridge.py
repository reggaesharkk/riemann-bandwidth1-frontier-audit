#!/usr/bin/env python3
"""Build exact rational/Sturm certificate for the scalar-regularized bridge."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "notes" / "WP84_CONDITIONED_SCALAR_REGULARIZED_HEAT_BRIDGE_CERTIFICATE.json"
X = sp.symbols("x", real=True)
I = sp.I

SOURCES = [
    "notes/WP84_CONDITIONED_RANK6_79_CONSUMER.md",
    "notes/WP84_CONDITIONED_RANK6_HEAT_CURVATURE_ATTACK.md",
    "notes/WP84_SCALAR_HEAT_TAIL_AND_TWO_SIDED_SMALL_BALL_AUDIT_2026_10_06.md",
    "notes/WP84_CIRCULAR_GAUSSIAN_Q_FIELD.md",
    "notes/WP84_GAUSSIAN_COVARIANCE_HADAMARD.md",
    "notes/WP84_RESONANT_D2_EXPLICIT_FUNCTIONAL.md",
    "src/wp84_conditioned_rank6_79_consumer.py",
    "src/wp84_conditioned_rank6_heat_curvature.py",
    "src/wp84_conditioned_rank6_heat_curvature_replay.py",
    "src/wp84_gaussian_covariance_hadamard_gate.py",
    "src/wp84_resonant_d2_explicit_gate.py",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def variations_at(sturm: list[sp.Expr], at) -> int:
    signs = []
    for expr in sturm:
        poly = sp.Poly(expr, X)
        if at == "-inf":
            sgn = sp.sign(poly.LC()) * (-1 if poly.degree() % 2 else 1)
        elif at == "+inf":
            sgn = sp.sign(poly.LC())
        else:
            value = poly.eval(at)
            sgn = sp.sign(value)
        if sgn:
            signs.append(int(sgn))
    return sum(a != b for a, b in zip(signs, signs[1:]))


def sturm_record(poly: sp.Poly, intervals: list[tuple[str, sp.Expr, sp.Expr]]) -> dict:
    seq = sp.sturm(poly.as_expr(), X)
    rows = []
    for name, left, right in intervals:
        vl, vr = variations_at(seq, left), variations_at(seq, right)
        rows.append({"name": name, "left": str(left), "right": str(right),
                     "variation_left": vl, "variation_right": vr,
                     "distinct_roots": vl - vr})
    return {"degree": poly.degree(), "sturm_sequence_length": len(seq), "intervals": rows}


def build() -> dict:
    q = (1936 * ((X + I) / (X - I))**3
         + (-192 - 5495*I) * ((X + I) / (X - I))**2
         + (-5695 + 169*I) * ((X + I) / (X - I))
         + (44 + 2205*I)) / 5000
    p = sp.factor(sp.cancel(q * sp.conjugate(q)))
    C0 = sp.Rational(2500529, 2500000)
    g = sp.factor(p - C0)
    gn, gd = map(sp.factor, sp.fraction(g))
    p2 = sp.factor(sp.cancel(sp.diff(p, X, 2)))
    n2, d2 = map(sp.factor, sp.fraction(p2))
    Pgn, Pn2 = sp.Poly(gn, X), sp.Poly(n2, X)

    # Exact global and exterior-square inequalities certify the simple bounds.
    bg_poly = sp.Poly(81 * gd**2 - gn**2, X)
    cg_poly = sp.Poly(144 * gd**2 - X**2 * gn**2, X)
    m2_poly = sp.Poly(31**2 * d2**2 - n2**2, X)
    root_intervals = [
        ("r1", -sp.Rational(1588, 1000), -sp.Rational(1586, 1000)),
        ("r2", -sp.Rational(329, 1000), -sp.Rational(328, 1000)),
        ("r3", sp.Rational(600, 1000), sp.Rational(601, 1000)),
        ("r4", sp.Rational(872, 1000), sp.Rational(873, 1000)),
        ("r5", sp.Rational(1254, 1000), sp.Rational(1255, 1000)),
        ("r6", sp.Rational(1516, 1000), sp.Rational(1517, 1000)),
        ("r7", sp.Rational(4327, 1000), sp.Rational(4328, 1000)),
    ]

    c = "sqrt(2/pi)"
    eps = sp.Rational(34148687712345924132945804854399,
                      12442212289373925054228673142500000)
    ratio = sp.Rational(9) / eps
    tail = {
        "fixed_K_bound": "9*min(1,sqrt(2/pi)*K/y)+12/K; y=sigma*sqrt(u), K>=2",
        "optimized_K": "min(9, min_{2<=K<=y/c}(9*c*K/y+12/K)); c=sqrt(2/pi); if y/c<2, value=9",
        "piecewise_clamp": "for h=y/c>=2: K*=clamp(sqrt(12*y/(9*c)),2,h), Tail=min(9,9*c*K*/y+12/K*); for h<2: Tail=9",
        "large_y_exact_regime": "y>=16*c/3: Tail=2*sqrt(108*c/y)",
        "large_u_rate": "2*sqrt(108*sqrt(2/pi)/sigma)*u^(-1/4) once sigma*sqrt(u)>=16*sqrt(2/pi)/3",
        "uniformity": ["dimension", "deterministic H_1", "realization of W", "T"],
    }
    record = {
        "schema": "WP84-conditioned-scalar-regularized-heat-bridge-v1",
        "start_head": "fb16bc83a6b26c51faec17b99ac2555e869ff033",
        "branch": "codex/c5-c6-attack-20261006",
        "consumer": "frozen conditioned rank-six cubic; no polynomial or threshold optimization",
        "q_ascending": ["(44+2205i)/5000", "(-5695+169i)/5000", "(-192-5495i)/5000", "1936/5000"],
        "C0": str(C0),
        "p_rational": str(p),
        "g_rational": str(g),
        "g_numerator_degree": Pgn.degree(),
        "g_numerator": str(Pgn.as_expr()),
        "g_denominator": str(gd),
        "g_asymptotic": "g(x)=(-20715928/3125000)/x+O(x^-2); coefficient same at +infinity and -infinity",
        "Bg": "9",
        "Cg": "12",
        "sturm_certificates": {
            "Bg_square": sturm_record(bg_poly, [("all-real", "-inf", "+inf")]),
            "Cg_square": sturm_record(cg_poly, [("left-tail", "-inf", sp.Integer(-2)), ("right-tail", sp.Integer(2), "+inf")]),
            "M2_square": sturm_record(m2_poly, [("all-real", "-inf", "+inf")]),
            "p2_roots": sturm_record(Pn2, [(name, left, right) for name, left, right in root_intervals]
                                      + [("all-real", "-inf", "+inf")]),
        },
        "p2_rational": str(p2),
        "p2_numerator": str(Pn2.as_expr()),
        "M2": "31",
        "p2_witnesses": {
            "positive_x0": str(p2.subs(X, 0)),
            "negative_x_minus_2_3": str(p2.subs(X, -sp.Rational(2, 3))),
            "signs_across_roots": ["+", "-", "+", "-", "+", "-", "+", "-"],
            "isolating_intervals": [{"left": str(a), "right": str(b)} for _, a, b in root_intervals],
        },
        "augmented_heat_identity": {
            "exact_finite_dimension": "d/du E tau p(H_1+sqrt(u)W+sigma*sqrt(u)*xi*I)=(1/2)E D^2F_H[W,W]+(sigma^2/2)E tau p''(H), F(H)=tau p(H); cross covariance is zero",
            "wp84_source_stencil": "(1/2)E D^2F_H[W,W]=Re E[A*Xi_z+B*Xi_zz+C*Xi_zzz]+o_T(1), at the regularized state; same inherited source normalization error retained",
            "combined_asymptotic": "E_(u,sigma)'=Re E[A*Xi_z+B*Xi_zz+C*Xi_zzz]+(sigma^2/2)E tau p''(H_(u,sigma))+o_T(1)",
            "scalar_dimension_check": "for d=1, derivative is (sigma^2/2) E p''(h+sqrt(u)w+sigma*sqrt(u)*xi)",
            "cross_term": "0 by independence and E xi=0",
        },
        "scalar_tail": tail,
        "generic_overhead": {
            "formula": "9*min(1,c*K/y)+12/K+(31/2)*y^2; y=sigma*sqrt(U), c=sqrt(2/pi), K>=2",
            "infimum": "9",
            "proof": "if y<=cK, first term is 9; if y>cK>=2c, curvature payment>(31/2)*(2c)^2=124/pi>31>9 using pi<4; inf<=9 along K=n,y=n^-2",
            "model_cushion": str(eps),
            "over_cushion": str(ratio),
            "over_cushion_decimal": str(sp.N(ratio, 16)),
            "decision": "GENERIC PAYMENT KILLED: infimum 9 exceeds the frozen model cushion by the recorded exact factor",
        },
        "signed_scalar_attempt": {
            "p2_sign": "both signs; exact rational witnesses above",
            "one_attempt": "At fixed source variance u, scalar-variance interpolation integrates (1/2)E tau p'' exactly to an endpoint difference. Along the required diagonal path both source variance and scalar variance vary with u; chain rule adds the source derivative, so this is a redistribution and gives no standalone one-sided saving.",
            "signed_improvement": "none",
        },
        "fourier_smoothing": {
            "identity": "xi-averaging is the scalar heat semigroup exp((sigma^2*u/2)*partial_s^2) acting on the real scalar translate s of each resolvent statistic",
            "strict_contraction_for_T12_or_S4_channel": "none proved; heat-semigroup L-infinity contraction has factor 1 only and yields no multiplicative factor below 1 for the grouped channel",
            "branch_status": "STOP after this no-contraction finding",
        },
        "theorem_target": {
            "threshold": "21/200",
            "required_total_integral": "2238029/2500000",
            "model_energy": "1272283602671916206561064875108101/12442212289373925054228673142500000",
            "model_cushion": str(eps),
            "actual_zeta_energy_upper_bound": "none",
            "strict_gt79": "OPEN",
            "remaining_source_law": "integral_0^U [G_source(u,sigma)+G_scalar(u,sigma)]du > 2238029/2500000 + Tail_sigma(U) + eta; no such source-side lower bound proved",
        },
        "source_gaussian": "W is the original circular-prime sharp-Loewner source; scalar xi is independent standard real Gaussian; its covariance changes the state law only, not the source covariance tensor",
        "hostile_mutations_required": [
            "omit_sigma_shift", "variance_sigma_not_sigma2", "drop_heat_half", "invent_cross_covariance", "alter_C0", "assume_C0_one", "reuse_other_consumer_tail_constants", "omit_source_conditioning", "dimension_dependent_tail", "assume_p2_nonnegative", "assume_smoothing_monotone", "omit_Xi_source_curvature", "evaluate_Xi_unregularized", "S2_instead_of_S4", "alter_threshold", "alter_model_cushion", "promote_model_endpoint", "uncertified_numeric_optimization", "reopen_source_mask", "claim_gt79_from_tail_only"
        ],
        "source_sha256": {rel: sha(ROOT / rel) for rel in SOURCES},
    }
    return record


def main() -> None:
    cert = build()
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"wrote {OUT.relative_to(ROOT)}")
    print("Bg=9, Cg=12, M2=31; exact Sturm certificates generated")
    print("generic overhead infimum=9; strict >79 remains OPEN")


if __name__ == "__main__":
    main()
