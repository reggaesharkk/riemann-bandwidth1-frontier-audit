#!/usr/bin/env python3
"""Exact finite-atomic falsifier for a moment-only conditioned Cayley bound.

This tests only source-certified first/second spectral moments.  It is an
abstract spectral obstruction, not a sample from WP84's Gaussian ensemble.
All arithmetic is rational.
"""
from __future__ import annotations

from fractions import Fraction as F
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
THRESHOLD = F(21, 200)

def energy(x: F) -> F:
    """p(x)=|q((x+i)/(x-i))|^2 for the frozen conditioned cubic q."""
    return (
        F(12502645)*x**6 - F(82863712)*x**5 + F(221347891)*x**4
        - F(303496416)*x**3 + F(224073135)*x**2 - F(84028544)*x
        + F(12502001)
    ) / (F(12500000)*(x*x+1)**3)

def moments(atoms: tuple[tuple[F, F], ...], order: int) -> list[F]:
    return [sum(w*x**k for w,x in atoms) for k in range(order+1)]

def rat(x: F) -> str:
    return f"{x.numerator}/{x.denominator}"

def build() -> dict:
    # Exactly the only two source-closed raw spectral constraints identified
    # for the sharp normalized H.  This law is nonnegative and finite atomic.
    atoms2 = ((F(1,4),F(0)), (F(3,4),F(4,3)))
    mu2 = moments(atoms2,2)
    E2 = sum(w*energy(x) for w,x in atoms2)
    gap2 = E2-THRESHOLD

    # Optional stronger stress test: this law also matches raw m3=2, the
    # pinned/model value corresponding to centered third moment zero.  That
    # third-moment input is NOT treated as source-certified here.
    atoms3 = ((F(1,54),F(-2)), (F(26,27),F(1)), (F(1,54),F(4)))
    mu3 = moments(atoms3,3)
    E3 = sum(w*energy(x) for w,x in atoms3)

    return {
        "schema":"wp84-conditioned-cayley-spectral-falsifier-v1",
        "decision":"MOMENT_ONLY_ROUTE_KILLED_BY_EXACT_ABSTRACT_SPECTRUM",
        "consumer":{
            "q_coefficients_ascending":[["44/5000","2205/5000"],["-5695/5000","169/5000"],["-192/5000","-5495/5000"],["1936/5000","0"]],
            "energy_rational_function":"(12502645*x^6-82863712*x^5+221347891*x^4-303496416*x^3+224073135*x^2-84028544*x+12502001)/(12500000*(x^2+1)^3)",
            "threshold":rat(THRESHOLD),
        },
        "applicable_constraints":{
            "raw_m1":"1",
            "raw_m2":"4/3",
            "evidence":"notes/WP84_SINE_MEAN_VARIANCE_GATE.md, source-closed moments for the sharp normalized state H",
            "not_included":"pinned m3..m6 are model/conditional inputs; Gaussian covariance constrains added W, not the deterministic source spectral measure",
        },
        "primary_counterexample":{
            "atoms_weight_location":[[rat(w),rat(x)] for w,x in atoms2],
            "raw_moments_m0_m2":[rat(x) for x in mu2],
            "energy_at_atoms":[rat(energy(x)) for _,x in atoms2],
            "energy":rat(E2),
            "energy_decimal":float(E2),
            "excess_over_threshold":rat(gap2),
            "excess_decimal":float(gap2),
            "finite_matrix":"H=diag(0,4/3,4/3,4/3), D=diag(0,1,2,3); [D,H]=0 so displacement rank is 0<=2",
        },
        "optional_noncertified_m3_stress_test":{
            "status":"NOT USED AS AN APPLICABLE SOURCE CONSTRAINT",
            "atoms_weight_location":[[rat(w),rat(x)] for w,x in atoms3],
            "raw_moments_m0_m3":[rat(x) for x in mu3],
            "energy":rat(E3),
            "energy_decimal":float(E3),
            "excess_over_threshold":rat(E3-THRESHOLD),
        },
        "scope":{
            "proved":"The first two source-certified moments and rank<=2 alone do not imply tau|q(U)|^2<0.105 for all finite Hermitian spectra.",
            "not_proved":"No counterexample to the actual zeta spectrum, the fixed Gaussian heat ensemble, or any source-specific asymptotic theorem.",
            "strict_gt79":"OPEN",
            "next_obstruction":"Any proof of the conditioned energy target must use additional source-specific information beyond m1,m2 and displacement rank, such as a proved resolvent/energy inequality for the actual prime-generated H (or a genuinely applicable higher-moment/phase constraint).",
        },
    }

def main() -> None:
    cert=build()
    out=ROOT/"notes/WP84_CONDITIONED_CAYLEY_SPECTRAL_FALSIFIER_CERTIFICATE.json"
    out.write_text(json.dumps(cert,indent=2,sort_keys=True)+"\n",encoding="utf-8")
    print("primary moments:",cert["primary_counterexample"]["raw_moments_m0_m2"])
    print("primary energy:",cert["primary_counterexample"]["energy"],"=",cert["primary_counterexample"]["energy_decimal"])
    print("excess over 0.105:",cert["primary_counterexample"]["excess_over_threshold"])
    print("optional m3=2 energy:",cert["optional_noncertified_m3_stress_test"]["energy"])
    print("RESULT: MOMENT_ONLY_ROUTE_FALSIFIED; NO ZETA-SIDE COUNTEREXAMPLE")

if __name__=="__main__":
    main()
