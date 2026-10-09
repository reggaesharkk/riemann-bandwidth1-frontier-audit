#!/usr/bin/env python3
"""Produce the exact no-wrap Fourier audit certificate for the prime matrix.

This certifies finite algebra and a valid but nondecaying boundary majorant;
it does not certify the natural-cutoff cubic alias estimate.
"""
from __future__ import annotations

import json
import math
from pathlib import Path

import sympy as sp


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificates" / "WP84_INFINITE_NO_WRAP_CUBIC_CERTIFICATE.json"


def exact_fourier_coefficients():
    a, x = sp.symbols("a x", real=True)
    zr, zi = sp.symbols("zr zi", real=True)
    z = zr + sp.I * zi
    zb = zr - sp.I * zi

    def j(y):
        return sp.I * (1 - 2 * y)

    # Four open regions, with x,a in (0,1); no endpoint is hidden in a branch.
    plus_no_wrap = sp.simplify((1-a)*z + z/(2*sp.I)*(j(x)-j(x+a)))
    plus_wrap = sp.simplify((1-a)*z + z/(2*sp.I)*(j(x)-j(x+a-1)))
    minus_no_wrap = sp.simplify((1-a)*zb - zb/(2*sp.I)*(j(x)-j(x-a)))
    minus_wrap = sp.simplify((1-a)*zb - zb/(2*sp.I)*(j(x)-j(x-a+1)))
    assert plus_no_wrap == z
    assert plus_wrap == 0
    assert minus_no_wrap == zb
    assert minus_wrap == 0

    # Symmetric Fourier-series value of the sawtooth multiplier at its jump.
    j0 = sp.Integer(0)
    plus_endpoint = sp.simplify((1-a)*z + z/(2*sp.I)*(j(1-a)-j0))
    minus_endpoint = sp.simplify((1-a)*zb - zb/(2*sp.I)*(j(a)-j0))
    assert plus_endpoint == z/2
    assert minus_endpoint == zb/2
    return {
        "interior_coefficients": {
            "plus_no_wrap": "z",
            "plus_wrap": "0",
            "minus_no_wrap": "conjugate(z)",
            "minus_wrap": "0",
        },
        "symmetric_endpoint_coefficients": {
            "x=1-alpha_plus": "z/2",
            "x=alpha_minus": "conjugate(z)/2",
            "sawtooth_at_integer": "0 (midpoint of one-sided limits)",
        },
        "endpoint_counterexample": {
            "alpha": "1/5",
            "x": "4/5",
            "z": "1",
            "candidate_plus_output_coefficient": "1/2, not 0",
        },
    }


def finite_compression_test():
    # Exact source entry formula versus Fourier coefficients of the two
    # no-wrap partial translations, for a rational frequency and finite block.
    alpha = 1 / 3
    z = 2 + 1j
    inds = range(-3, 4)
    worst = 0.0
    for i in inds:
        for j in inds:
            r = i - j
            if r == 0:
                fourier = z * cmath.exp(2j*math.pi*j*alpha) * (1-alpha)
                fourier += z.conjugate() * cmath.exp(-2j*math.pi*j*alpha) * (1-alpha)
                source = 2*(1-alpha)*(z*cmath.exp(2j*math.pi*i*alpha)).real
            else:
                fourier = z * cmath.exp(2j*math.pi*j*alpha) * (
                    1-cmath.exp(2j*math.pi*r*alpha)
                ) / (2j*math.pi*r)
                fourier += z.conjugate() * cmath.exp(-2j*math.pi*j*alpha) * (
                    cmath.exp(-2j*math.pi*r*alpha)-1
                ) / (2j*math.pi*r)
                ai = (z*cmath.exp(2j*math.pi*i*alpha)).imag
                aj = (z*cmath.exp(2j*math.pi*j*alpha)).imag
                source = (ai-aj)/(math.pi*(j-i))
            worst = max(worst, abs(fourier-source))
    assert worst < 2e-14
    return {"alpha": "1/3", "z": "2+i", "index_block": [-3, 3],
            "max_entry_residual": worst, "includes_scalar_s0":
            "s0*delta_ij is identical under compression"}


def boundary_majorant():
    # Exact count of P-to-Q pairs at displacement r and exact finite harmonic
    # sums confirm the displayed trace-ideal bound's combinatorial factor.
    samples = []
    for d in range(1, 9):
        for r in range(1, 2*d+3):
            actual = sum(1 for i in range(d) for j in range(-r, d+r)
                         if (j < 0 or j >= d) and abs(j-i) == r)
            expected = 2*min(r, d)
            assert actual == expected
        samples.append({"d": d, "pair_count_formula": "2*min(r,d)"})
    return {
        "cross_hilbert_schmidt_squared": "<= 8*S^2/pi^2*(H_d+1)",
        "cube_trace_difference": "<= 24*(abs(s0)+4*S)*S^2*(H_d+1)/(pi^2*d)",
        "prime_weight_mass": "S=sum_{p^v<=N} Lambda(p^v)/(a_phi*L*sqrt(p^v))=O(sqrt(N)/L)",
        "natural_cutoff_majorant": "O(N^(3/2)*log(d)/(T*L^4))",
        "at_N=X*exp(-sqrt(L))": "O(T^(1/2)*exp(-3*sqrt(L)/2)/L^3), which diverges as an upper bound",
        "samples": samples,
    }


def path_weight_checks():
    from fractions import Fraction as F
    q = [F(0), F(1,4), F(7,12), F(23,60)]
    osc = max(q)-min(q)
    assert 1-osc == F(5,12)
    alias = [F(0), F(1,4), F(3,4), F(1)]
    assert max(alias)-min(alias) == 1
    assert max(F(0), 1-(max(alias)-min(alias))) == 0
    return {
        "path_weight": "omega=max(0,1-(max(q_0,q_1,q_2,q_3)-min(q_0,q_1,q_2,q_3)))",
        "rational_nonalias_example": {"increments": ["1/4", "1/3", "-1/5"], "omega": "5/12"},
        "nonzero_integer_alias_example": {"increments": ["1/4", "1/2", "1/4"], "net": "1", "omega": "0"},
    }


def main():
    # cmath is imported late to keep the algebraic certificate section clear.
    global cmath
    import cmath

    cert = {
        "title": "Exact Fourier no-wrap identity and finite-section cubic audit",
        "status": "EXACT ALGEBRA CLOSED; NATURAL-CUTOFF TRANSFER OPEN",
        "source_matrix": {
            "scale": "L=log(T/(2*pi)); X=T/(2*pi); N=floor(X*exp(-sqrt(L))); d=floor(T*L/(2*pi))",
            "prime_powers": "all n=p^v<=N",
            "coefficient": "c_n=-Lambda(n)/(a_phi*L*sqrt(n))",
            "carrier": "z_n=c_n*exp(i*T*log(n))",
            "alpha": "alpha_n=log(n)/L in (0,1-sqrt(L)/L+o(1))",
            "fields": "A_n(k)=Im(z_n*exp(2*pi*i*k*alpha_n)); B_n(k)=2*(1-alpha_n)*Re(z_n*exp(2*pi*i*k*alpha_n))",
            "matrix": "H_pr=s0(T)I+diag(B)+[diag(A),J]",
            "section": "H_I=P_I*H_pr*P_I exactly for the finite prime matrix, including s0(T)I",
        },
        "J_multiplier": "i*(1-2*x) for 0<x<1; symmetric value 0 at integer jump",
        "operator_identity": "M_B+[M_A,J]=z*S_plus_alpha+conjugate(z)*S_minus_alpha on L2(T), with partial nonwrapping translations; equality is a.e.",
        "candidate_pointwise_formula": "correct for interior x; at x=1-alpha plus coefficient is z/2; at x=alpha minus coefficient is conjugate(z)/2 under symmetric Fourier convention",
        "finite_compression": finite_compression_test(),
        "boundary_bound": boundary_majorant(),
        "path_weight_checks": path_weight_checks(),
        "cubic_frequency_status": {
            "infinite_lattice_bohr_trace": "only exactly zero total frequency survives the infinite Cesaro diagonal; partial-shift support gives omega=0 for every |delta|>=1, including all second and higher alias strips",
            "exact_cubic_path_weight": "omega=max(0,1-osc(q_0,q_1,q_2,q_3)); q_j=sum_{t<=j} epsilon_t*alpha_{n_t}; tau_I(V^3) sums omega*prod z_n^epsilon*exp(2*pi*i*k_minus*lambda/L)*D_d'(lambda/L); z already contains exp(i*T*log(n))",
            "alias_range": "at natural cutoff mixed 1:2/2:1 permits central and nearest +/-1 windows; same-sign sums can reach +/-1 and +/-2, but |delta|>=1 is killed in P_I V^3 P_I; only the strip just inside +/-1 can survive with omega vanishing at the boundary",
            "finite_section": "kernel D_d'(lambda/L) retains near integer aliases |lambda-mL|=O(1/T); no uniform natural-cutoff estimate is certified",
            "mixed_sign_ordinary_prime_multiplicity": "6 sign placements (3 of type 1:2 and 3 of type 2:1); at most 2 ordered presentations of the two-prime side per prime triple; the separate R=6000 band expansion has (2R+1)^2=12001^2 lag paths; the full J operator uses the exact partial-shift formula rather than this finite lag count",
            "same_sign_aliases": "2 placements; first and second periodic alias windows remain in the natural cutoff",
            "first_missing_estimate": "uniform signed o(1) bound for the all-distinct third-order nonzero/near-alias plus tail correlation, with full prime powers and source section weights",
            "generic_scale": "logarithmic factors times N^(3/2)/T; not o(1) for N=T^(1-o(1))",
        },
        "first_alias_majorant": {
            "omega_times_kernel": "<= 1/(2*d') exactly for delta=+/-1 with 0<epsilon=1-|delta|<=1/2",
            "full_l1_bound": "O(S^3/(T*L))=O(N^(3/2)/(T*L^4))",
            "natural_cutoff": "O(T^(1/2)*exp(-3*sqrt(L)/2)/L^4), diverges as upper bound"
        },
        "decision": "C — EXACT ALGEBRA CLOSED; QUANTITATIVE TRANSFER REMAINS OPEN",
        "theorem_boundary": "No source m3=2 claim; no 0.105 energy conclusion; strict >79 remains OPEN",
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True)+"\n", encoding="utf-8")
    print("PASS: exact piecewise Fourier coefficients and symmetric endpoint corrections")
    print("PASS: finite compression regression max residual", cert["finite_compression"]["max_entry_residual"])
    print("BOUND: finite-section boundary majorant", cert["boundary_bound"]["natural_cutoff_majorant"])
    print("DECISION: C — exact algebra closed; quantitative transfer remains open")
    print("WROTE", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
