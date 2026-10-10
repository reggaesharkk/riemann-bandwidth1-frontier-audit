#!/usr/bin/env python3
"""Decision-J producer: exact finite-section full-frequency path certificate."""
from __future__ import annotations

import cmath
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "certificates" / "WP84_DECISION_J_FULL_FREQUENCY_CUBIC_PATH_CERTIFICATE.json"


def f_l(ell: int, sigma: int, alpha: float) -> complex:
    if ell == 0:
        return 1.0 - alpha
    return sigma * (1.0 - cmath.exp(2j * math.pi * sigma * ell * alpha)) / (2j * math.pi * ell)


def u_entry(i: int, j: int, sigma: int, alpha: float) -> complex:
    return cmath.exp(2j * math.pi * sigma * i * alpha) * f_l(j - i, sigma, alpha)


def mm(a, b):
    return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))]
            for i in range(len(a))]


def tr(a):
    return sum(a[i][i] for i in range(len(a)))


def build_source_subset():
    # A finite algebra regression using actual prime powers 2, 3, 4 and the
    # source coefficient formula, but not claiming a complete natural cutoff.
    L, a_phi = 5.0, 1.0
    T = 2 * math.pi * math.exp(L)
    atoms = [(2, 1, 2), (3, 1, 3), (2, 2, 4)]  # (prime, exponent, integer)
    values = []
    for p, v, n in atoms:
        c = -math.log(p) / (a_phi * L * math.sqrt(n))
        alpha = math.log(n) / L
        assert 0.0 < alpha < 1.0
        values.append((n, c, alpha))
    return T, L, values


def source_v_matrix(indices, T, atoms):
    count = len(indices)
    A = [0.0] * count
    beta = [0.0] * count
    for r, k in enumerate(indices):
        for n, c, alpha in atoms:
            w = c * cmath.exp(1j * (T * math.log(n) + 2 * math.pi * k * alpha))
            A[r] += w.imag
            beta[r] += 2 * (1 - alpha) * w.real
    J = [[0.0 if r == s else 1 / (math.pi * (indices[s] - indices[r]))
          for s in range(count)] for r in range(count)]
    return [[(beta[r] if r == s else 0.0) + (A[r] - A[s]) * J[r][s]
             for s in range(count)] for r in range(count)]


def run_exact_regression():
    T, L, atoms = build_source_subset()
    indices = list(range(-2, 5))
    count = len(indices)
    V = source_v_matrix(indices, T, atoms)
    # Signed U reconstruction, each finite U entry uses the actual finite-J
    # kernel 1/(pi*(j-i)); no lag cutoff is imposed.
    V_signed = [[0j for _ in indices] for _ in indices]
    u_tables = {}
    for n, c, alpha in atoms:
        for sigma in (-1, 1):
            mat = [[u_entry(i, j, sigma, alpha) for j in indices] for i in indices]
            u_tables[(n, sigma)] = mat
            carrier = c * cmath.exp(1j * sigma * T * math.log(n))
            for r in range(count):
                for s in range(count):
                    V_signed[r][s] += carrier * mat[r][s]
    err_signed = max(abs(V[r][s] - V_signed[r][s]) for r in range(count) for s in range(count))
    assert err_signed < 2e-12

    V3 = mm(mm(V, V), V)
    full_diag_error = 0.0
    all_path_count = 0
    for r, k in enumerate(indices):
        expanded = 0j
        for atoms3 in itertools.product(atoms, repeat=3):
            ns = [x[0] for x in atoms3]
            cs = [x[1] for x in atoms3]
            alphas = [x[2] for x in atoms3]
            for sigmas in itertools.product((-1, 1), repeat=3):
                omega = sum(s * math.log(n) for s, n in zip(sigmas, ns))
                coeff = math.prod(cs) * cmath.exp(1j * T * omega)
                for ell1 in range(-count + 1, count):
                    for ell2 in range(-count + 1, count):
                        ell3 = -ell1 - ell2
                        q1, q2 = ell1, ell1 + ell2
                        q = (0, q1, q2)
                        roots = [root for root in indices if all(root + shift in indices for shift in q)]
                        if k not in roots:
                            continue
                        path_f = math.prod(f_l(e, s, a) for e, s, a in zip((ell1, ell2, ell3), sigmas, alphas))
                        displacement = cmath.exp(2j * math.pi * (sigmas[1] * q1 * alphas[1]
                                                                + sigmas[2] * q2 * alphas[2]))
                        expanded += coeff * path_f * displacement * cmath.exp(2j * math.pi * k * omega / L)
                        all_path_count += 1
        full_diag_error = max(full_diag_error, abs(expanded - V3[r][r]))
    assert full_diag_error < 5e-10
    Rzero = [[0j for _ in indices] for _ in indices]
    for atoms3 in itertools.product(atoms, repeat=3):
        ns = [x[0] for x in atoms3]
        cs = [x[1] for x in atoms3]
        alphas = [x[2] for x in atoms3]
        for sigmas in itertools.product((-1, 1), repeat=3):
            omega = sum(s * math.log(n) for s, n in zip(sigmas, ns))
            if abs(omega) > 1e-12:
                continue
            coeff = math.prod(cs) * cmath.exp(1j * T * omega)
            for r in range(count):
                for s in range(count):
                    for t in range(count):
                        Rzero[r][r] += coeff * u_tables[(ns[0], sigmas[0])][r][s] * \
                            u_tables[(ns[1], sigmas[1])][s][t] * u_tables[(ns[2], sigmas[2])][t][r]
    Rnonzero = [[V3[r][s] - Rzero[r][s] for s in range(count)] for r in range(count)]

    def lag_centered(E_positions):
        # E_positions are integer matrix positions, e.g. first two rows.
        u = len(E_positions)
        total = 0j
        path_count = 0
        wrong_missing_displacement = 0j
        for atoms3 in itertools.product(atoms, repeat=3):
            ns = [x[0] for x in atoms3]
            cs = [x[1] for x in atoms3]
            alphas = [x[2] for x in atoms3]
            for sigmas in itertools.product((-1, 1), repeat=3):
                omega = sum(s * math.log(n) for s, n in zip(sigmas, ns))
                if abs(omega) < 1e-12:
                    continue
                coeff = math.prod(cs) * cmath.exp(1j * T * omega)
                for ell1 in range(-count + 1, count):
                    for ell2 in range(-count + 1, count):
                        ell3 = -ell1 - ell2
                        q = (0, ell1, ell1 + ell2)
                        roots = [k for k in indices if all(k + shift in indices for shift in q)]
                        if not roots:
                            continue
                        # In this regression index labels are the actual indices.
                        coef = math.prod(f_l(e, s, a) for e, s, a in zip((ell1, ell2, ell3), sigmas, alphas))
                        disp = cmath.exp(2j * math.pi * (sigmas[1] * q[1] * alphas[1]
                                                        + sigmas[2] * q[2] * alphas[2]))
                        moved = [k for k in E_positions if k in roots]
                        root_sum = sum(cmath.exp(2j * math.pi * k * omega / L) for k in moved)
                        full_sum = sum(cmath.exp(2j * math.pi * k * omega / L) for k in roots)
                        centered = root_sum - (u / count) * full_sum
                        total += coeff * coef * disp * centered
                        wrong_missing_displacement += coeff * coef * centered
                        path_count += 1
        return total, path_count, wrong_missing_displacement

    E_left = indices[:2]
    lag_value, paths, mutated = lag_centered(E_left)
    direct = sum(Rnonzero[indices.index(k)][indices.index(k)] for k in E_left)
    direct -= (len(E_left) / count) * tr(Rnonzero)
    err_path = abs(lag_value - direct)
    assert err_path < 3e-10
    assert abs(lag_value - mutated) > 1e-9

    # Verify every relative-root set is an interval and exact span count.
    root_records = 0
    for ell1 in range(-count + 1, count):
        for ell2 in range(-count + 1, count):
            ell3 = -ell1 - ell2
            q = (0, ell1, ell1 + ell2)
            roots = [k for k in indices if all(k + shift in indices for shift in q)]
            span = max(q) - min(q)
            expected_count = max(0, count - span)
            assert len(roots) == expected_count
            assert not roots or roots == list(range(roots[0], roots[-1] + 1))
            root_records += 1

    return {"source_subset": [{"n": n, "c": c, "alpha": a} for n, c, a in atoms],
            "dimension": count, "signed_reconstruction_max_error": err_signed,
            "full_relative_lag_diagonal_max_error": full_diag_error,
            "full_relative_lag_terms": all_path_count,
            "nonzero_centered_path_max_error": err_path,
            "lag_root_patterns_checked": root_records, "expanded_paths_in_centered_test": paths,
            "omitted_displacement_mutation_detected": abs(lag_value - mutated) > 1e-9,
            "s0": "omitted; this tests V^3 only, as required for R_nonzero"}


def main():
    reg = run_exact_regression()
    cert = {
        "title": "WP84 Decision J: full-frequency cubic path reduction",
        "classification": "J2 — exact finite-section full-frequency path representation established and the fixed-gap far-alias sector has a stronger source-valid absolute bound; near aliases and full transfer remain open",
        "start_state": {"branch": "codex/c5-c6-attack-20261006",
                        "head": "fd5dc616f0780dc33e40278647d1826ec5bc85f2",
                        "preexisting_untracked": ["notebooklm_packet/"],
                        "push": "NO", "merge": "NO", "notebooklm_packet": "untouched"},
        "entry_formula": {
            "U_entry": "U_(n,sigma)(i,j)=exp(2*pi*i*sigma*i*alpha_n)*f_(j-i)^sigma(alpha_n)",
            "f_zero": "f_0^sigma(alpha)=1-alpha",
            "f_nonzero": "f_ell^sigma(alpha)=sigma*(1-exp(2*pi*i*sigma*ell*alpha))/(2*pi*i*ell), ell!=0",
            "adjoint": "U_(n,sigma)^*=U_(n,-sigma); J_ij=1/(pi*(j-i)) is used with the stated (j-i) orientation",
            "finite_lag_scope": "No R=6000 truncation; all integer lags are retained, with root set empty outside the actual finite section."
        },
        "relative_lag_identity": {
            "lags": "ell1+ell2+ell3=0; q0=0, q1=ell1, q2=ell1+ell2",
            "indices": "k, k+q1, k+q2",
            "root_set": "K_ell={k in I0:k+q0,k+q1,k+q2 all in I0}; for I0=[b,b+d-1], this is [b-min(q), b+d-1-max(q)] intersected with integers, empty if max(q)-min(q)>d-1",
            "root_count": "|K_ell|=max(0,d-(max(q)-min(q)))",
            "endpoint_intersection": "For either contiguous endpoint interval E_u or E_v, E intersect K_ell is contiguous or empty",
            "phase": "exp(2*pi*i*k*Omega/L)*exp(2*pi*i*(sigma2*q1*alpha2+sigma3*q2*alpha3)); Omega=sum sigma_j*log(n_j)",
            "path_weight": "product_j f_(ell_j)^sigma_j(alpha_j)",
            "carrier": "product_j c_(n_j)*exp(i*T*Omega); all prime powers n_j=p^v<=N retained"
        },
        "centered_endpoint_formula": {
            "kernel": "K_center(E,ell,Omega)=sum_(k in E intersect K_ell) exp(2*pi*i*k*Omega/L) - (|E|/d)*sum_(k in K_ell) exp(2*pi*i*k*Omega/L)",
            "sum": "Y_E_nonzero=sum_(n1,n2,n3 in P(N), sigmas, Omega!=0) (c_n1*c_n2*c_n3*exp(i*T*Omega))*product_j f_(ell_j)^sigma_j(alpha_j)*exp(2*pi*i*(sigma2*q1*alpha2+sigma3*q2*alpha3))*K_center",
            "normalization": "The global centering is u/d (or v/d) times the full K_ell sum; it is retained and is not replaced by a signed mean estimate.",
            "alias_coherence": "|Omega/L-m|<=1/M; m=0,±1,±2 are distinct classes, with exact Omega=0 already discharged only by Decision I."
        },
        "lag_summability": {
            "weights": "w_0=1; w_ell=1/(pi*|ell|), ell!=0",
            "full_bound": "sum_(ell1+ell2+ell3=0) product_j w_ellj <= ||w||_(3/2)^3=(1+2*zeta(3/2)/pi^(3/2))^2",
            "tail_bound": "sum_(sum ell=0, max_j|ell_j|>R) product_j w_ellj <= 3*||w*1_(|ell|>R)||_(3/2)*||w||_(3/2)^2 <= 3*4^(2/3)/pi*(1+2*zeta(3/2)/pi^(3/2))^(4/3)*R^(-1/3), R>=1",
            "prime_mass": "S(T)=sum_(n in P(N))|c_n|=O(sqrt(N)/L); summing the triple coefficient mass contributes S(T)^3 and all eight sign vectors",
            "centered_kernel_bound": "|K_center|<=2*|E|<=2*M; both endpoint sides together therefore have absolute lag-tail bound <=32*M*S(T)^3*tail(R)",
            "normalized_natural_scale": "O((M/d)*N^(3/2)/L^3*R^(-1/3))=O(exp(3L/2-2*sqrt(L))*R^(-1/3)/L^3); this does not tend to zero for fixed R and does not justify deleting long lags",
            "scope": "The lag-only summability is valid, but after coefficient and endpoint weights it is not a negligible tail estimate. All lags remain in the exact formula."
        },
        "quantitative_gate": {
            "target": "E_u|Y_L_nonzero(u)|+E_v|Y_R_nonzero(v)|=o(d)",
            "far_sector": "For fixed delta in (0,1/2), dist(Omega/L,Z)>=delta implies |K_center|<=2/sin(pi*delta). Summing all lags and the full prime-power coefficient mass gives E_u|Y_far,L|+E_v|Y_far,R|<=32*||w||_(3/2)^3*S(T)^3/sin(pi*delta). After division by d this is O_delta(N^(3/2)/(T*L^4))=O_delta(exp(L/2-3*sqrt(L)/2)/L^4), a genuine improvement over the inherited O(K_T*M/d)=O(exp(L/2-sqrt(L))/L) envelope by factor O_delta(exp(-sqrt(L)/2)/L^3), but it still diverges.",
            "alias_neighborhoods": "The complementary fixed neighborhoods of m=0,+-1,+-2 retain the O(M) coherent endpoint kernel; the exact zero-carrier part alone is controlled by Decision I. No bound closes the remaining nonzero near aliases.",
            "decisive_obstruction": "The exact phase reunification does not bound the signed weighted sum over source triples near Omega/L=m; coefficient L1 mass times the full lag norm gives a growing natural-cutoff upper envelope.",
            "first_missing_estimate": "A uniform source-weighted centered endpoint estimate for the exact K_center sum above, retaining m=0 nonzero near aliases and m=±1,±2 aliases, full P(N), and all finite-section paths, with total o(d).",
            "new_saving": "No signed or positive constant saving is certified; the far-sector upper bound is absolute, source-valid, stronger than the inherited global envelope, and insufficient because it grows."
        },
        "comparison": {
            "decision_i": "Exact zero-carrier UFD sector bound O(L^-3) remains valid and separate.",
            "decision_g_h": "Prior diagonal-score and one-sided endpoint expansions retain root/finite-path dependence but did not expose one common endpoint phase in every cubic path summand.",
            "infinite_no_wrap": "The older infinite partial-translation formula already has a full displacement frequency with continuum overlap weight; the present formula adds the exact finite-J discrete root set and exact endpoint centering. It is an exact organization, not a new asymptotic saving."
        },
        "finite_regression": reg,
        "decision": "J2",
        "theorem_boundary": "m3=2, conditioned Cayley energy<0.105, signed fifth/sixth gate, prime-to-Weil identification, zero-side transfer, determinant compatibility, and strict >79% remain OPEN."
    }
    OUT.write_text(json.dumps(cert, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print("PASS exact finite-J entry identity and relative-lag root enumeration")
    print("PASS full carrier Omega/L and retained displacement phase")
    print("PASS centered endpoint kernel compared against direct nonzero matrix cubic")
    print("BOUND lag-only tail O(R^-1/3); coefficient-weighted natural-cutoff payment does not close")
    print("DECISION J2; far sector upper envelope improved but grows; no complete endpoint saving; strict >79 OPEN")
    print("WROTE", OUT.relative_to(ROOT))


if __name__ == "__main__":
    main()
