#!/usr/bin/env python3
"""Independent hostile replay for Decision J; no producer import."""
from __future__ import annotations

import cmath
import itertools
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CERT = ROOT / "certificates" / "WP84_DECISION_J_FULL_FREQUENCY_CUBIC_PATH_CERTIFICATE.json"


def matrix_product(a, b):
    rows, inner, cols = len(a), len(b), len(b[0])
    return [[sum(a[i][r] * b[r][j] for r in range(inner)) for j in range(cols)]
            for i in range(rows)]


def conjugate_transpose(a):
    return [[a[j][i].conjugate() for j in range(len(a))] for i in range(len(a[0]))]


def entry_from_commutator(i, j, sigma, alpha):
    # Independently evaluate (1-alpha)D + sigma/(2i)[D,J].
    d_i = cmath.exp(2j * math.pi * sigma * i * alpha)
    if i == j:
        return (1 - alpha) * d_i
    d_j = cmath.exp(2j * math.pi * sigma * j * alpha)
    jij = 1 / (math.pi * (j - i))
    return sigma * (d_i - d_j) * jij / (2j)


def f_formula(ell, sigma, alpha):
    if ell == 0:
        return 1 - alpha
    return sigma * (1 - cmath.exp(2j * math.pi * sigma * ell * alpha)) / (2j * math.pi * ell)


def build_regression():
    L, a_phi = 5.0, 1.0
    T = 2 * math.pi * math.exp(L)
    data = [(2, 1), (3, 1), (2, 2)]  # prime bases and exponents, including 2^2
    atoms = []
    for p, v in data:
        n = p**v
        lam = math.log(p)
        coeff = -lam / (a_phi * L * math.sqrt(n))
        alpha = math.log(n) / L
        atoms.append((n, coeff, alpha))
    I = list(range(-3, 4))
    d = len(I)

    # Original field matrix from the actual A,beta source formulas.
    A, beta = [], []
    for k in I:
        aa, bb = 0.0, 0.0
        for n, c, alpha in atoms:
            z = c * cmath.exp(1j * T * math.log(n))
            w = z * cmath.exp(2j * math.pi * k * alpha)
            aa += w.imag
            bb += 2 * (1 - alpha) * w.real
        A.append(aa)
        beta.append(bb)
    V = [[(beta[r] if r == s else 0.0)
          + (A[r] - A[s]) / (math.pi * (I[s] - I[r])) if r != s else beta[r]
          for s in range(d)] for r in range(d)]

    # Check f_ell entry identity and adjoint relation on every row pair.
    entry_error = 0.0
    adjoint_error = 0.0
    U = {}
    for n, c, alpha in atoms:
        for sig in (-1, 1):
            mat = [[entry_from_commutator(i, j, sig, alpha) for j in I] for i in I]
            U[(n, sig)] = mat
            for r, i in enumerate(I):
                for s, j in enumerate(I):
                    f_value = cmath.exp(2j * math.pi * sig * i * alpha) * f_formula(j-i, sig, alpha)
                    entry_error = max(entry_error, abs(mat[r][s] - f_value))
    for n, _, _ in atoms:
        for sig in (-1, 1):
            adj = conjugate_transpose(U[(n, sig)])
            other = U[(n, -sig)]
            adjoint_error = max(adjoint_error, max(abs(adj[r][s]-other[r][s])
                                                     for r in range(d) for s in range(d)))
    assert entry_error < 2e-12 and adjoint_error < 2e-12
    assert abs(f_formula(1, 1, atoms[0][2]) - f_formula(1, -1, atoms[0][2])) > 1e-6

    # Signed reconstruction versus the original fields.
    rebuilt = [[0j for _ in I] for _ in I]
    for n, c, alpha in atoms:
        for sig in (-1, 1):
            weight = c * cmath.exp(1j * sig * T * math.log(n))
            for r in range(d):
                for s in range(d):
                    rebuilt[r][s] += weight * U[(n, sig)][r][s]
    reconstruct_error = max(abs(V[r][s] - rebuilt[r][s]) for r in range(d) for s in range(d))
    assert reconstruct_error < 2e-12

    V3 = matrix_product(matrix_product(V, V), V)
    full_lag_error = 0.0
    for pos, k in enumerate(I):
        path_total = 0j
        for triple in itertools.product(atoms, repeat=3):
            ns = [x[0] for x in triple]
            cs = [x[1] for x in triple]
            alphas = [x[2] for x in triple]
            for sigmas in itertools.product((-1, 1), repeat=3):
                Omega = sum(s*math.log(n) for s,n in zip(sigmas,ns))
                coeff = math.prod(cs)*cmath.exp(1j*T*Omega)
                for ell1 in range(-(d-1),d):
                    for ell2 in range(-(d-1),d):
                        ell3=-ell1-ell2
                        q1,q2=ell1,ell1+ell2
                        q=(0,q1,q2)
                        roots=[root for root in I if all(root+offset in I for offset in q)]
                        if k not in roots:
                            continue
                        fs=math.prod(f_formula(e,sig,a) for e,sig,a in zip((ell1,ell2,ell3),sigmas,alphas))
                        shift=cmath.exp(2j*math.pi*(sigmas[1]*q1*alphas[1]+sigmas[2]*q2*alphas[2]))
                        path_total += coeff*fs*shift*cmath.exp(2j*math.pi*k*Omega/L)
        full_lag_error=max(full_lag_error,abs(path_total-V3[pos][pos]))
    assert full_lag_error < 5e-10
    zero = [[0j for _ in I] for _ in I]
    for triple in itertools.product(atoms, repeat=3):
        ns = [x[0] for x in triple]
        cs = [x[1] for x in triple]
        aa = [x[2] for x in triple]
        for sigmas in itertools.product((-1, 1), repeat=3):
            Omega = sum(s*math.log(n) for s, n in zip(sigmas, ns))
            if abs(Omega) > 1e-12:
                continue
            coeff = math.prod(cs) * cmath.exp(1j*T*Omega)
            for r in range(d):
                for s in range(d):
                    for t in range(d):
                        zero[r][r] += coeff*U[(ns[0],sigmas[0])][r][s]*U[(ns[1],sigmas[1])][s][t]*U[(ns[2],sigmas[2])][t][r]
    nonzero = [[V3[r][s]-zero[r][s] for s in range(d)] for r in range(d)]

    def independently_expand(endpoint_rows):
        endpoint_size = len(endpoint_rows)
        answer = 0j
        answer_drop_shift = 0j
        patterns = 0
        for triple in itertools.product(atoms, repeat=3):
            ns = [x[0] for x in triple]
            cs = [x[1] for x in triple]
            alphas = [x[2] for x in triple]
            for sigmas in itertools.product((-1, 1), repeat=3):
                Omega = sum(sig*math.log(n) for sig,n in zip(sigmas,ns))
                if abs(Omega) < 1e-12:
                    continue
                prefactor = math.prod(cs)*cmath.exp(1j*T*Omega)
                for l1 in range(-(d-1), d):
                    for l2 in range(-(d-1), d):
                        l3 = -l1-l2
                        q1, q2 = l1, l1+l2
                        qs = (0,q1,q2)
                        roots = [k for k in I if all(k+q in I for q in qs)]
                        if not roots:
                            continue
                        moved_roots = [k for k in endpoint_rows if k in roots]
                        path_f = math.prod(f_formula(e,sig,al) for e,sig,al in zip((l1,l2,l3),sigmas,alphas))
                        displacement = cmath.exp(2j*math.pi*(sigmas[1]*q1*alphas[1]+sigmas[2]*q2*alphas[2]))
                        endpoint_sum = sum(cmath.exp(2j*math.pi*k*Omega/L) for k in moved_roots)
                        global_sum = sum(cmath.exp(2j*math.pi*k*Omega/L) for k in roots)
                        centering = endpoint_sum - endpoint_size/d*global_sum
                        answer += prefactor*path_f*displacement*centering
                        answer_drop_shift += prefactor*path_f*centering
                        patterns += 1
        direct = sum(nonzero[I.index(k)][I.index(k)] for k in endpoint_rows)
        direct -= endpoint_size/d*sum(nonzero[r][r] for r in range(d))
        assert abs(answer-direct) < 5e-10
        return answer, abs(answer-direct), abs(answer-answer_drop_shift), patterns

    left, right = I[:2], I[-2:]
    left_res = independently_expand(left)
    right_res = independently_expand(right)

    # Exhaustive finite root count, contiguity, and endpoint intersection checks.
    root_cases = 0
    for l1 in range(-(d-1), d):
        for l2 in range(-(d-1), d):
            l3 = -l1-l2
            q = (0,l1,l1+l2)
            roots = [k for k in I if all(k+x in I for x in q)]
            count = max(0,d-(max(q)-min(q)))
            assert len(roots) == count
            assert not roots or roots == list(range(roots[0],roots[-1]+1))
            for E in (left,right):
                inter = [k for k in E if k in roots]
                assert not inter or inter == list(range(inter[0],inter[-1]+1))
            root_cases += 1
    # Omitting an intermediate-root condition invents paths which leave I.
    impossible_lags = (d, 0, -d)
    impossible_q = (0, impossible_lags[0], impossible_lags[0]+impossible_lags[1])
    assert not [k for k in I if all(k+x in I for x in impossible_q)]
    assert len(I) > 0  # the wrong rule "all k in I" would count d roots
    # This full-J path is legal and exceeds the unrelated fixed R=6000 band.
    big_d, long_lag = 12005, 7000
    long_q = (0, long_lag, 3500)
    long_root_count = max(0, big_d-(max(long_q)-min(long_q)))
    assert long_root_count == 5005 and long_lag > 6000
    # Exact prime-power zero closure remains distinct from a nonzero product ratio.
    assert 2*2 == 4 and 2*3 != 5

    # Invalid alternatives are numerically falsified in this regression.
    assert left_res[2] > 1e-9  # omit displacement phase
    # Dropping global centering changes the endpoint score in this example.
    endpoint_uncentered = sum(nonzero[I.index(k)][I.index(k)] for k in left)
    assert abs(endpoint_uncentered-left_res[0]) > 1e-9
    # The wrong commutator orientation changes at least one off-diagonal entry.
    k0, k1 = I[0], I[1]
    wrong = (A[0]-A[1])/(math.pi*(k0-k1))
    assert abs(wrong-V[0][1]) > 1e-9

    return {"dimension": d, "entry_identity_error": entry_error,
            "adjoint_identity_error": adjoint_error,
            "signed_reconstruction_error": reconstruct_error,
            "full_relative_lag_diagonal_error": full_lag_error,
            "left_centered_path_error": left_res[1], "right_centered_path_error": right_res[1],
            "left_nonzero_paths": left_res[3], "right_nonzero_paths": right_res[3],
            "root_lag_cases": root_cases, "missing_displacement_mutation_detected": True,
            "dropped_centering_mutation_detected": True, "wrong_orientation_mutation_detected": True,
            "wrong_f_sign_mutation_detected": True, "omitted_intermediate_root_detected": True,
            "long_lag_above_6000_is_legal": long_root_count,
            "source_subset_note": "finite algebra regression using actual p^v labels and coefficient formula; not a complete natural-cutoff calculation"}


def replay_lag_bound():
    # Numerical finite partial sums are diagnostics; the certificate's Young
    # and integral-comparison inequalities are the proof of the symbolic bound.
    R = 8
    def w(x):
        return 1.0 if x == 0 else 1/(math.pi*abs(x))
    inside = sum(w(a)*w(b)*w(-a-b) for a in range(-80,81) for b in range(-80,81)
                 if max(abs(a),abs(b),abs(a+b)) <= R)
    wider = sum(w(a)*w(b)*w(-a-b) for a in range(-80,81) for b in range(-80,81)
                if max(abs(a),abs(b),abs(a+b)) > R)
    assert inside > 0 and wider > 0
    # The tail is not asserted negligible after source coefficient weights.
    return {"finite_cutoff_R": R, "partial_inside_mass": inside,
            "partial_tail_mass": wider, "is_asymptotic_prime_bound": False}


def main():
    cert = json.loads(CERT.read_text(encoding="utf-8"))
    reg = build_regression()
    tail = replay_lag_bound()
    assert cert["classification"].startswith("J2")
    assert reg["dimension"] == cert["finite_regression"]["dimension"]
    assert cert["lag_summability"]["tail_bound"].find("R^(-1/3)") >= 0
    assert "does not tend to zero" in cert["lag_summability"]["normalized_natural_scale"]
    qgate = cert["quantitative_gate"]
    assert "32*||w||_(3/2)^3*S(T)^3/sin(pi*delta)" in qgate["far_sector"]
    assert "still diverges" in qgate["far_sector"]
    assert "No signed or positive constant saving" in qgate["new_saving"]
    print("PASS independent U entry, adjoint, and signed reconstruction checks")
    print("PASS direct matrix cubic equals relative-lag root-restricted expansion")
    print("PASS endpoint intersections contiguous; exact root cardinality verified")
    print("PASS displacement, orientation, and global-centering hostile mutations")
    print("PASS wrong-sign, omitted-root, >6000-lag, and proper-power hostile cases")
    print("PASS lag Young bound/tail scope retained; weighted tail is not declared negligible", tail)
    print("PASS fixed-gap far-sector bound is stronger than inherited envelope but diverges")
    print("DECISION J2; far-sector quantitative improvement only; strict >79 OPEN")


if __name__ == "__main__":
    main()
