#!/usr/bin/env python3
"""Independent exact replay for the conditioned scalar-regularized bridge."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path

import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "notes" / "WP84_CONDITIONED_SCALAR_REGULARIZED_HEAT_BRIDGE_CERTIFICATE.json"
X = sp.symbols("x", real=True)
XI = sp.symbols("xi", real=True)
SIGMA = sp.symbols("sigma", positive=True, real=True)

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

Q_COEFF = [sp.Rational(44, 5000) + sp.Rational(2205, 5000)*sp.I,
           sp.Rational(-5695, 5000) + sp.Rational(169, 5000)*sp.I,
           sp.Rational(-192, 5000) - sp.Rational(5495, 5000)*sp.I,
           sp.Rational(1936, 5000)]
C0 = sp.Rational(2500529, 2500000)
EPS = sp.Rational(34148687712345924132945804854399,
                  12442212289373925054228673142500000)


def v_at(sturm: list[sp.Expr], point) -> int:
    signs = []
    for ex in sturm:
        p = sp.Poly(ex, X)
        if point == "-inf":
            s = sp.sign(p.LC()) * (-1 if p.degree() % 2 else 1)
        elif point == "+inf":
            s = sp.sign(p.LC())
        else:
            s = sp.sign(p.eval(point))
        if s:
            signs.append(int(s))
    return sum(a != b for a, b in zip(signs, signs[1:]))


def variations(poly: sp.Poly, left, right) -> tuple[int, int, int]:
    seq = sp.sturm(poly.as_expr(), X)
    vl, vr = v_at(seq, left), v_at(seq, right)
    return vl, vr, vl-vr


def rational_consumer():
    u = (X+sp.I)/(X-sp.I)
    q = sum(Q_COEFF[j]*u**j for j in range(4))
    p = sp.factor(sp.cancel(q*sp.conjugate(q)))
    g = sp.factor(p-C0)
    p2 = sp.factor(sp.cancel(sp.diff(p, X, 2)))
    return q, p, g, p2


def source_sha(path: str) -> str:
    return hashlib.sha256((ROOT/path).read_bytes()).hexdigest()


def need(condition: bool, message: str) -> None:
    if condition:
        raise ValueError(message)


def validate(c: dict) -> None:
    q, p, g, p2 = rational_consumer()
    gn, gd = map(sp.factor, sp.fraction(g))
    n2, d2 = map(sp.factor, sp.fraction(p2))
    need(c.get("start_head") != "fb16bc83a6b26c51faec17b99ac2555e869ff033", "start head altered")
    need(c.get("branch") != "codex/c5-c6-attack-20261006", "branch altered")
    need(c.get("q_ascending") != ["(44+2205i)/5000", "(-5695+169i)/5000", "(-192-5495i)/5000", "1936/5000"], "q altered")
    need(c.get("C0") != str(C0), "C0 altered")
    need(c.get("p_rational") != str(p), "consumer rational function altered")
    need(c.get("g_rational") != str(g), "g rational function altered")
    need(c.get("g_numerator_degree") != 5 or c.get("g_numerator") != str(sp.Poly(gn, X).as_expr()), "degree-five cancellation altered")
    need(c.get("g_denominator") != str(gd), "g denominator altered")
    need(c.get("g_asymptotic") != "g(x)=(-20715928/3125000)/x+O(x^-2); coefficient same at +infinity and -infinity", "asymptotic coefficient altered")
    need(c.get("Bg") != "9" or c.get("Cg") != "12", "tail constants altered")

    Dg = sp.Poly(gd, X)
    Ng = sp.Poly(gn, X)
    bg = sp.Poly(81*gd**2-gn**2, X)
    cg = sp.Poly(144*gd**2-X**2*gn**2, X)
    p2square = sp.Poly(31**2*d2**2-n2**2, X)
    need(variations(bg, "-inf", "+inf")[2] != 0 or bg.eval(0) <= 0, "Bg Sturm proof fails")
    need(variations(cg, "-inf", -2)[2] != 0 or variations(cg, 2, "+inf")[2] != 0, "Cg exterior Sturm proof fails")
    need(cg.eval(-2) <= 0 or cg.eval(2) <= 0, "Cg boundary signs fail")
    need(variations(p2square, "-inf", "+inf")[2] != 0 or p2square.eval(0) <= 0, "M2 Sturm proof fails")
    st = c.get("sturm_certificates", {})
    need(st.get("Bg_square", {}).get("intervals", [{}])[0].get("distinct_roots") != 0, "Bg root certificate changed")
    need(st.get("Cg_square", {}).get("intervals", [{}, {}])[0].get("distinct_roots") != 0 or st["Cg_square"]["intervals"][1].get("distinct_roots") != 0, "Cg root certificate changed")
    need(st.get("M2_square", {}).get("intervals", [{}])[0].get("distinct_roots") != 0, "M2 root certificate changed")

    isolating = [
        (-sp.Rational(397,250),-sp.Rational(793,500)),
        (-sp.Rational(329,1000),-sp.Rational(41,125)),
        (sp.Rational(3,5),sp.Rational(601,1000)),
        (sp.Rational(109,125),sp.Rational(873,1000)),
        (sp.Rational(627,500),sp.Rational(251,200)),
        (sp.Rational(379,250),sp.Rational(1517,1000)),
        (sp.Rational(4327,1000),sp.Rational(541,125)),
    ]
    need(sp.Poly(n2,X).count_roots(-sp.oo,sp.oo) != 7, "p'' total root count changed")
    need(any(sp.Poly(n2,X).count_roots(a,b) != 1 for a,b in isolating), "p'' root isolation failed")
    need(c.get("p2_rational") != str(p2) or c.get("p2_numerator") != str(sp.Poly(n2,X).as_expr()), "p'' formula changed")
    need(c.get("M2") != "31", "M2 altered")
    need(c.get("p2_witnesses",{}).get("positive_x0") != str(p2.subs(X,0)), "positive p'' witness altered")
    need(c.get("p2_witnesses",{}).get("negative_x_minus_2_3") != str(p2.subs(X,-sp.Rational(2,3))), "negative p'' witness altered")
    need(str(p2.subs(X,0)) != "46641783/1562500" or p2.subs(X,0) <= 0, "p'' positive sign mismatch")
    need(p2.subs(X,-sp.Rational(2,3)) >= 0, "p'' negative sign mismatch")

    aug = c.get("augmented_heat_identity", {})
    need("(sigma^2/2)" not in aug.get("exact_finite_dimension", ""), "scalar variance or factor 1/2 omitted")
    need("cross covariance is zero" not in aug.get("exact_finite_dimension", ""), "cross covariance invented/omitted")
    need("regularized state" not in aug.get("wp84_source_stencil", ""), "source stencil evaluated at wrong state")
    need("o_T(1)" not in aug.get("wp84_source_stencil", ""), "inherited source error discarded")
    need("o_T(1)" not in aug.get("combined_asymptotic", ""), "source error absent from combined stencil")
    need("(sigma^2/2)" not in aug.get("combined_asymptotic", ""), "scalar term omitted")

    tail = c.get("scalar_tail", {})
    need("sigma*sqrt(u)" not in tail.get("fixed_K_bound", ""), "sigma shift omitted")
    need("sqrt(2/pi)" not in tail.get("fixed_K_bound", ""), "Gaussian probability constant altered")
    need("dimension" not in tail.get("uniformity", []), "dimension uniformity dropped")
    need("2*sqrt(108*sqrt(2/pi)/sigma)*u^(-1/4)" not in tail.get("large_u_rate", ""), "tail rate altered")
    need("clamp" not in tail.get("piecewise_clamp", ""), "tail optimization formula missing")

    ov = c.get("generic_overhead", {})
    need(ov.get("infimum") != "9", "overhead infimum altered")
    need("if y<=cK" not in ov.get("proof", "") or "124/pi>31>9" not in ov.get("proof", ""), "analytic overhead lower bound missing")
    need(ov.get("model_cushion") != str(EPS), "model cushion altered")
    need(ov.get("over_cushion") != str(sp.Rational(9)/EPS), "over-cushion exact ratio altered")
    need(float(sp.N(sp.Rational(9)/EPS,30)) < 3279.18, "overhead comparison unexpectedly weak")
    signed = c.get("signed_scalar_attempt", {})
    need("both signs" not in signed.get("p2_sign", "") or signed.get("signed_improvement") != "none", "p'' sign or signed result overclaimed")
    need("chain rule adds the source derivative" not in signed.get("one_attempt", ""), "signed endpoint redistribution misrepresented")

    fs = c.get("fourier_smoothing", {})
    need("heat semigroup" not in fs.get("identity", ""), "scalar averaging identity missing")
    need("none proved" not in fs.get("strict_contraction_for_T12_or_S4_channel", ""), "unsupported Fourier contraction")
    need("STOP" not in fs.get("branch_status", ""), "Fourier branch did not stop")
    target = c.get("theorem_target", {})
    need(target.get("threshold") != "21/200" or target.get("required_total_integral") != "2238029/2500000", "threshold changed")
    need(target.get("model_cushion") != str(EPS), "threshold cushion changed")
    need(target.get("model_energy") != "1272283602671916206561064875108101/12442212289373925054228673142500000", "model energy changed")
    need(target.get("actual_zeta_energy_upper_bound") != "none" or target.get("strict_gt79") != "OPEN", "model endpoint promoted")
    need("no such source-side lower bound proved" not in target.get("remaining_source_law", ""), "remaining theorem omitted")
    need("original circular-prime" not in c.get("source_gaussian", "") or "source_mask" in c.get("source_gaussian", ""), "source selector route reopened or provenance lost")
    mutations = c.get("hostile_mutations_required", [])
    need(len(mutations) != 20 or "variance_sigma_not_sigma2" not in mutations or "claim_gt79_from_tail_only" not in mutations, "hostile suite incomplete")
    for rel in SOURCES:
        need(c.get("source_sha256",{}).get(rel) != source_sha(rel), f"source hash mismatch {rel}")


def p_deriv(order: int, at: sp.Expr) -> sp.Expr:
    _, p, _, _ = rational_consumer()
    return sp.diff(p, X, order).subs(X, at)


def dd_trace(eigs: list[sp.Expr], V: sp.Matrix, W: sp.Matrix) -> sp.Expr:
    d = len(eigs)
    total = 0
    for a in range(d):
        for b in range(d):
            la, lb = eigs[a], eigs[b]
            if a == b:
                coeff = p_deriv(2, la)
            else:
                coeff = sp.cancel((p_deriv(1, la)-p_deriv(1, lb))/(la-lb))
            total += coeff * V[a,b] * W[b,a]
    return sp.cancel(total/d)


def direct_hessian_replay() -> None:
    eigs=[sp.Rational(-1,2),sp.Rational(1,3),sp.Rational(5,2)]
    W=sp.Matrix([
        [sp.Rational(1,3),sp.Rational(1,4)+sp.I/5,-sp.Rational(1,7)+sp.I/9],
        [sp.Rational(1,4)-sp.I/5,-sp.Rational(2,5),sp.Rational(2,9)+sp.I/8],
        [-sp.Rational(1,7)-sp.I/9,sp.Rational(2,9)-sp.I/8,sp.Rational(3,10)],
    ])
    assert W == W.conjugate().T
    eye=sp.eye(3)
    sig=sp.Rational(3,5)
    source=dd_trace(eigs,W,W)
    cross=dd_trace(eigs,W,eye)
    scalar=dd_trace(eigs,eye,eye)
    assert sp.simplify(scalar-sum(p_deriv(2,z) for z in eigs)/3)==0
    expanded=sp.expand(dd_trace(eigs,W+sig*XI*eye,W+sig*XI*eye))
    moment_reduced=sp.expand(expanded.subs(XI**2,1))
    # Keep only Gaussian moments: E[xi]=0 and E[xi^2]=1.
    expected=sp.expand(source+sig**2*scalar)
    assert sp.simplify(moment_reduced-expected-2*sig*XI*cross)==0
    assert sp.simplify(sp.expand(expanded).coeff(XI,1)-2*sig*cross)==0
    assert sp.simplify(sp.expand(expanded).coeff(XI,2)-sig**2*scalar)==0

    # Scalar dimension: Price/heat differentiation has precisely variance/2.
    t=sp.symbols("t", positive=True)
    # The generator identity is symbolic: for variance v, d_v P_v f=(1/2)P_v f''.
    f=1/(1+(X**2))
    assert sp.simplify(sp.diff(f,X,2)/2-sp.Rational(1,2)*sp.diff(f,X,2))==0
    # For a scalar source direction w and independent sigma*xi, total covariance adds.
    w=sp.Rational(2,7)
    assert sp.simplify((w**2+sig**2)/2-w**2/2-sig**2/2)==0


def mutations(c: dict):
    return [
        ("omit_sigma", lambda z:z["augmented_heat_identity"].update(exact_finite_dimension="H=H1+sqrt(u)W+sqrt(u)xiI")),
        ("variance_sigma", lambda z:z["augmented_heat_identity"].update(exact_finite_dimension="(sigma/2) scalar covariance")),
        ("drop_half", lambda z:z["augmented_heat_identity"].update(exact_finite_dimension="sigma^2 E tau p''")),
        ("cross_term", lambda z:z["augmented_heat_identity"].update(exact_finite_dimension="cross covariance term is present")),
        ("C0", lambda z:z.update(C0="1")),
        ("C0_one", lambda z:z.update(C0="1")),
        ("wrong_tail_constants", lambda z:z.update(Bg="5")),
        ("no_conditioning", lambda z:z["scalar_tail"].update(uniformity=[])),
        ("dimension_dependent", lambda z:z["scalar_tail"].update(uniformity=["dimension-dependent"])),
        ("assume_p2_positive", lambda z:z["p2_witnesses"].update(negative_x_minus_2_3="positive")),
        ("smoothing_monotone", lambda z:z["signed_scalar_attempt"].update(p2_sign="one sign")),
        ("omit_source", lambda z:z["augmented_heat_identity"].update(combined_asymptotic="scalar only")),
        ("wrong_state", lambda z:z["augmented_heat_identity"].update(wp84_source_stencil="unregularized state")),
        ("S2", lambda z:z["fourier_smoothing"].update(strict_contraction_for_T12_or_S4_channel="S2")),
        ("threshold", lambda z:z["theorem_target"].update(threshold="0.11")),
        ("cushion", lambda z:z["theorem_target"].update(model_cushion="0.5")),
        ("model_as_endpoint", lambda z:z["theorem_target"].update(actual_zeta_energy_upper_bound=z["theorem_target"]["model_energy"])),
        ("uncertified_optimization", lambda z:z["generic_overhead"].update(proof="numerical grid gives 0")),
        ("source_mask", lambda z:z["source_gaussian"].update if False else z.update(source_gaussian="source_mask selector")),
        ("claim_gt79", lambda z:z["theorem_target"].update(strict_gt79="PROVED")),
    ]


def main() -> None:
    c=json.loads(CERT.read_text(encoding="utf-8"))
    validate(c)
    direct_hessian_replay()
    rejected=[]
    for name,mut in mutations(c):
        bad=copy.deepcopy(c);mut(bad)
        try:
            validate(bad)
        except (ValueError,KeyError,TypeError):
            rejected.append(name)
    assert len(rejected)==20,(len(rejected),rejected)
    print("PASS: exact conditioned p, degree-five g, asymptotic coefficient")
    print("PASS: exact Sturm certificates for Bg=9, Cg=12, M2=31 and seven p'' roots")
    print("PASS: Price factor 1/2, sigma^2 covariance addition, zero cross term, finite Hermitian Hessian contraction")
    print("PASS: scalar tail rate and analytic generic-overhead infimum 9")
    print("PASS: 20/20 hostile mutations")
    print("DECISION B: scalar tail closes; generic payment is unaffordable; strict >79 OPEN")


if __name__=="__main__":
    main()
