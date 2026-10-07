#!/usr/bin/env python3
"""Low-order Price/Mehler algebra, all-n dual production and labeled recon.

SciPy proposes witnesses. An independent Fraction-only verifier accepts them.
Synthetic measurements never certify the actual prime/reference consumer.
"""
import argparse
from fractions import Fraction as F
import itertools
import json
import math
from pathlib import Path
import sympy as s
import wp84_joint_signed_deficit_covariance_transfer as prior
import wp84_cross_repository_hermite_adjoint as old
import wp84_mehler_weak_dual_certificate as cert

RHOS = [F(1, 4), F(1, 2), F(3, 4), F(7, 8), F(15, 16), F(31, 32),
        F(63, 64), F(127, 128)]
KS = (4, 6, 8, 12, 16, 24, 32)


def algebra():
    theta, rho = s.symbols('theta rho', real=True)
    x = s.symbols('x0:2', real=True)
    y = s.symbols('y0:2', real=True)
    C0, C1 = s.diag(1, 0), s.Matrix([[2, 1], [1, 2]])
    delta = C1-C0
    C = C0+theta*delta
    covariance = C.row_join(rho*C).col_join((rho*C).row_join(C))
    H = s.Matrix([[1+2*x[0], 2*x[1]], [2*x[1], -1+4*x[0]]])
    Q1 = H**2+s.I*H**3/5  # u=4 is inserted in H; noncommuting directions.
    Q2 = Q1.subs(dict(zip(x, y)), simultaneous=True)
    integrand = prior.inner(Q1, Q2)
    mean = prior.average(integrand, x+y, covariance)
    same = mixed = 0
    for i in range(2):
        for j in range(2):
            same += delta[i, j]*(s.diff(integrand, x[i], x[j])
                                  +s.diff(integrand, y[i], y[j]))/2
            mixed += rho*delta[i, j]*s.diff(integrand, x[i], y[j])
    price = prior.average(same+mixed, x+y, covariance)
    prior.check(s.diff(mean, theta)-price, 'joint-block Price identity')
    cert.reject(lambda: prior.check(s.diff(mean, theta)
                -prior.average(same, x+y, covariance), 'missing cross-covariance block'))
    # Independently project matrix-valued Q on standard real Hermites.
    cov_white = s.eye(2).row_join(rho*s.eye(2)).col_join(
        (rho*s.eye(2)).row_join(s.eye(2)))
    white = prior.average(integrand, x+y, cov_white)
    masses = []
    for n in range(4):
        mass = 0
        for alpha in itertools.product(range(n+1), repeat=2):
            if sum(alpha) != n:
                continue
            h = s.prod(s.hermite_prob(a, v) for a, v in zip(alpha, x))
            norm = math.prod(math.factorial(a) for a in alpha)
            coefficient = Q1.applyfunc(lambda p: prior.average(p*h, x, s.eye(2))/s.sqrt(norm))
            mass += prior.inner(coefficient, coefficient)
        prior.check(s.Poly(white, rho).nth(n)-mass, 'Mehler chaos mass')
        if mass < 0:
            raise ValueError('Negative Hermite mass')
        masses.append(str(mass))
    one_copy = prior.average(prior.inner(Q1, Q1), x, s.eye(2))
    prior.check(white.subs(rho, 1)-one_copy, 'rho=1 energy endpoint')
    # Singular endpoint: compare at theta=0 without any inverse covariance.
    for rr in (s.Rational(1, 1000), s.Rational(3, 5), s.Rational(999, 1000), s.Integer(1)):
        prior.check((s.diff(mean, theta)-price).subs({theta: 0, rho: rr}), 'singular comparison')
    return {'max_derivative_per_Q_factor': 2, 'max_total_derivative_order': 2,
            'K_dependence': False, 'real_Price_factor': '1/2',
            'noncommuting_matrix_and_singular_covariance': 'PASS',
            'missing_rho_cross_block': 'REJECTED',
            'Hermite_masses_standard_covariance': masses}


def bv_identity():
    d = 3
    z = s.symbols('s', real=True)
    phases = [s.exp(2*s.pi*s.I*k*z) for k in range(d)]
    U = s.Matrix(d, d, lambda i, j: (1-z)*phases[i] if i == j else
                 (phases[i]-phases[j])/(2*s.pi*s.I*(j-i)))
    point = s.Rational(1, 4)
    Up = U.subs(z, point)
    Um = Up.conjugate().T
    Dup = U.diff(z).subs(z, point)
    Dum = Dup.conjugate().T
    e = s.Matrix([v.subs(z, point) for v in phases])
    one, D = s.ones(d, 1), s.diag(0, 1, 2)
    M = s.Matrix([[1, 2, s.I], [0, 3, 1], [2, 0, -1]])
    N = s.Matrix([[2, 0, 1], [1, -1, 2], [s.I, 1, 3]])
    direct = s.trace(M*Dup*N*Um+M*Up*N*Dum)/d
    collapsed = (2*s.pi*s.I*s.trace(Um*M*Up*(D*N-N*D))
                 -s.trace(M*e*one.T*N*Um)
                 -s.trace(M*Up*N*one*e.conjugate().T))/d
    prior.check(direct-collapsed, 'two-word BV identity')
    minus_direct = s.trace(M*Dum*N*Up+M*Um*N*Dup)/d
    minus_by_swap = s.trace(N*Dup*M*Um+N*Up*M*Dum)/d
    prior.check(minus_direct-minus_by_swap, 'reverse branch by cyclic swap')
    return {'general_noncommuting_M_N': 'PASS', 'reverse_branch': 'PASS',
            'norm_bound': '2pi(B(M)D(N)+B(N)D(M))+4B(M)B(N)',
            'D_semnorm': 'trace_norm([D,X])/d'}


def bv_constants():
    from wp84_actual_state_signed_dual_flux import sqrt_upper
    a, c = s.Rational(131, 200), s.Rational(3142, 2415)
    z = c+s.I*a
    p = [s.Integer(1), -s.Rational(43428, 13891),
         s.Rational(37704, 13891), -s.Rational(9660, 13891)]
    b = [p[3], p[2]+3*z*p[3], p[1]+2*z*p[2]+3*z*z*p[3],
         sum(p[j]*z**j for j in range(4))]
    # Only b1,b2,b3 occur in first/second derivatives. b0 is unused here.
    r6 = (c*c+a*a)**3
    weights = [s.Integer(0)]+[sqrt_upper(s.expand_complex(r6*b[k]*s.conjugate(b[k])))
                              for k in range(1, 4)]
    qcap, K1cap = s.Rational(43, 20), s.Integer(10)
    amp = const = sigma = s.Integer(0)
    def add(weight, BM, BN, DM, DN):
        nonlocal amp, const, sigma
        amp += weight*2*BM*BN
        const += weight*4*BM*BN
        sigma += weight*s.Rational(44, 7)*(BM*DN+BN*DM)
    for k in range(1, 4):
        for pp in range(1, k+1):
            for qq in range(1, k+2-pp):
                rr = k+2-pp-qq
                if rr < 1:
                    continue
                BM, BN = qcap*a**(-pp-rr), a**(-qq)
                DM = K1cap*a**(-pp-rr)+qcap*(pp+rr)*a**(-pp-rr-1)
                DN = qq*a**(-qq-1)
                add(2*weights[k], BM, BN, DM, DN)
        for l in range(1, 4):
            for pp in range(1, k+1):
                qq = k+1-pp
                for rr in range(1, l+1):
                    tt = l+1-rr
                    BM, BN = a**(-tt-qq), a**(-pp-rr)
                    DM, DN = (tt+qq)*a**(-tt-qq-1), (pp+rr)*a**(-pp-rr-1)
                    add(weights[k]*weights[l], BM, BN, DM, DN)
    return {'alpha_amplitude': str(amp), 'beta_variation_constant': str(const),
            'gamma_variation_field_norm': str(sigma),
            'formula': '||h||inf<=u alpha; E Var(h)<=u(beta+gamma sigma_state); multiply by a_phi^-2',
            'scope': 'rational upper conditioning constants for covariance substitution, not consumer losses'}


def optimize_witness(K, t, kind, rhos=None):
    import numpy as np
    from scipy.optimize import linprog
    rhos = RHOS if rhos is None else rhos
    M = 256
    data = [F(1)]+[(1-t)/(1-t*r) for r in rhos]
    design = np.array([[1.]+[float(r)**n for r in rhos] for n in range(M+1)])
    target = np.array([float(n <= K) for n in range(M+1)])
    lower = kind == 'lower'
    result = linprog((-1 if lower else 1)*np.array(list(map(float, data))),
                     A_ub=design if lower else -design,
                     b_ub=target if lower else -target,
                     bounds=[(None, 0) if lower else (0, None)]
                            +[(-10**7, 10**7)]*len(rhos), method='highs')
    if not result.success:
        raise ValueError('Witness proposal failed: '+result.message)
    coeff = [F(float(c)).limit_denominator(10**9) for c in result.x]
    safety = F(1, 10**8)
    coeff[0] += -safety if lower else safety
    N = max(K, M)
    while cert.tail_bound(coeff, rhos, N, kind) > 0:
        N *= 2
        if N > 20000:
            raise ValueError('Tail coverage exceeded resource cap')
    # Independently repair EVERY finite rational constraint, not only LP rows.
    powers = [F(1)]*len(rhos)
    correction = F(0)
    for n in range(N+1):
        value = coeff[0]+sum(c*p for c, p in zip(coeff[1:], powers))
        residual = value-F(n <= K) if lower else F(n <= K)-value
        correction = max(correction, residual)
        powers = [p*r for p, r in zip(powers, rhos)]
    coeff[0] += -correction if lower else correction
    witness = {'kind': kind, 'K': K, 'finite_end': N,
               'rhos': list(map(str, rhos)), 'coefficients': list(map(str, coeff)),
               'producer': 'floating LP proposal followed by exact rational repair',
               'repair': str(correction), 'safety': str(safety)}
    cert.verify(witness)
    return witness


def build_certificate():
    witnesses, rows = [], []
    tU, td = F(3, 4), F(1, 100)
    Einf, w0 = F(str(old.EINF)), F(1415, 13891)
    delta = F(1, 100000)
    for K in KS:
        candidates = [optimize_witness(K, tU, 'lower', RHOS[:m]) for m in (6, 7, 8)]
        def terminal_bound(w):
            values = [(1-tU)/(1-tU*F(r)) for r in w['rhos']]
            return cert.measured_bound(w, (1, 1), [(v, v) for v in values])
        lower = max(candidates, key=terminal_bound)
        upper = optimize_witness(K, td, 'upper')
        AU = [(1-tU)/(1-tU*r) for r in RHOS]
        Ad = [(1-td)/(1-td*r) for r in RHOS]
        lo = terminal_bound(lower)
        hi = cert.measured_bound(upper, (1, 1), [(v, v) for v in Ad])
        # The cap S<=E is itself a fully certified weak dual.
        if hi > 1:
            upper = {'kind': 'upper', 'K': K, 'finite_end': K,
                     'rhos': [], 'coefficients': ['1'], 'producer': 'exact mass cap'}
            hi = cert.measured_bound(upper, (1, 1), [])
        trueU, trued = 1-tU**(K+1), 1-td**(K+1)
        if not lo <= trueU or not trued <= hi:
            raise ValueError('Certified dual violates exact geometric data')
        one_lower = max(cert.measured_bound(cert.one_rho(K, r, 'lower'), (1, 1),
                            [((1-tU)/(1-tU*r), (1-tU)/(1-tU*r))]) for r in RHOS)
        c0 = delta/2*(F(43, 20)*74+F(100, K+1))
        synthetic_lower_difference = Einf*lo-w0*hi
        synthetic_deficit = Einf-w0-synthetic_lower_difference
        synthetic_margin = F(str(old.CUSHION))-synthetic_deficit-c0
        witnesses.extend([lower, upper])
        rows.append({'K': K, 'lower_unit_terminal': str(lo),
                     'selected_lower_rho_count': len(lower['rhos']),
                     'upper_unit_initial': str(hi), 'exact_terminal_prefix': str(trueU),
                     'exact_initial_prefix': str(trued),
                     'best_one_rho_lower_among_chosen': str(one_lower),
                     'synthetic_deficit_upper': str(synthetic_deficit),
                     'initial_cost_upper': str(c0),
                     'synthetic_margin_lower': str(synthetic_margin),
                     'dual_measurement_amplification': str(sum(abs(F(c)) for c in lower['coefficients'])
                                                        +sum(abs(F(c)) for c in upper['coefficients']))})
    best = max(rows, key=lambda row: F(row['synthetic_margin_lower']))
    return {'schema': 'wp84-mehler-all-n-dual-v1', 'rhos': list(map(str, RHOS)),
            'witnesses': witnesses, 'benchmark_rows': rows,
            'best_synthetic_K': best['K'], 'delta_for_initial_budget': str(delta),
            'synthetic_measurement_model': {'terminal': 'E_inf*(1-3/4)*(3/4)^n',
                                          'initial': 'w0*(1-1/100)*(1/100)^n'},
            'scope': 'Exact all-n cutoff witnesses; geometric benchmark is NOT the actual/reference heat state',
            'actual_reference_measurements_certified': False,
            'consumer_certified': False, 'certified_actual_K_delta_U': None}


def reference_recon(certificate, samples=128):
    import numpy as np
    from wp84_integrated_cross_error_stein_chaos import prime_state
    mean, _, L, N = prime_state(128)
    d = len(mean)
    k = np.arange(d); lag = k[:, None]-k[None, :]
    J = np.zeros((d, d)); off = lag != 0
    J[off] = -1/(np.pi*lag[off])
    Hcov = np.eye(d)/6
    Hcov[off] = -1/(2*np.pi**2*lag[off]**2)
    chol = np.linalg.cholesky(Hcov)
    rng = np.random.default_rng(84079471)
    def noises():
        aa = rng.normal(size=(samples, d))/2
        hh = rng.normal(size=(samples, d))@chol.T
        W = (aa[:, :, None]-aa[:, None, :])*J
        W[:, k, k] = hh
        return W
    W, Wfresh = noises(), noises()
    c, a = 3142/2415, 131/200
    eta = (c*c+a*a)**1.5
    def values(matrix):
        lam, O = np.linalg.eigh(matrix)
        P = 1-43428/13891*lam+37704/13891*lam**2-9660/13891*lam**3
        return eta*P/(lam-c-1j*a)**3, O
    def endpoint(u):
        Q1, O1 = values(mean+np.sqrt(u)*W)
        E = float(np.mean(abs(Q1)**2))
        As = []
        for rho in RHOS:
            rr = float(rho)
            Q2, O2 = values(mean+np.sqrt(u)*(rr*W+np.sqrt(1-rr*rr)*Wfresh))
            overlap = np.swapaxes(O1, -1, -2)@O2
            A = np.einsum('si,sj,sij->s', Q1.conj(), Q2, overlap**2).real/d
            As.append(float(np.mean(A)))
        return E, As
    delta = 1/100000
    Ed, Ad = endpoint(delta)
    rows = []
    for U in (1, 2, 4, 8, 16):
        EU, AU = endpoint(U)
        cuts = []
        for K in KS:
            lower, upper = [w for w in certificate['witnesses'] if w['K'] == K]
            def diagnostic_value(w, E, A):
                lookup = dict(zip(map(str, RHOS), A))
                return float(F(w['coefficients'][0]))*E+sum(float(F(c))*lookup[r]
                        for c, r in zip(w['coefficients'][1:], w['rhos']))
            value = diagnostic_value(lower, EU, AU)-diagnostic_value(upper, Ed, Ad)
            cuts.append({'K': K, 'dual_difference_diagnostic': value,
                         'exceeds_exact_global_energy_cap': value > float(old.EINF),
                         'usable_as_a_bound': False})
        rows.append({'U': U, 'E_ref_diagnostic': EU,
                     'A_ref_diagnostic': AU, 'cutoff_duals': cuts})
    return {'T': 128, 'd': d, 'N': N, 'samples': samples, 'delta': delta,
            'E_delta_diagnostic': Ed, 'A_delta_diagnostic': Ad, 'rows': rows,
            'scope': 'Monte Carlo on SAME actual finite-prime mean with continuum field covariance; not interval-certified or a T-limit',
            'measurement_enclosures_certified': False}


def main():
    if not __debug__:
        raise RuntimeError('Run without -O')
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--certificate', type=Path, required=True)
    ap.add_argument('--output', type=Path, required=True)
    ap.add_argument('--recon', action='store_true')
    args = ap.parse_args()
    certificate = build_certificate()
    args.certificate.write_text(json.dumps(certificate, indent=2)+'\n', encoding='utf-8')
    replay = {'low_order_algebra': algebra(), 'BV_two_word_algebra': bv_identity(),
              'BV_rational_constants': bv_constants(),
              'hostile_duals': cert.hostile(),
              'all_n_witness_checks': [cert.verify(w) for w in certificate['witnesses']],
              'best_synthetic_K': certificate['best_synthetic_K'],
              'consumer_certified': False, 'final_actual_margin': None,
              'decision': 'B: low-order noise covariance transfer closed under frozen sharp-state bounds; reference measurement certificate remains'}
    if args.recon:
        replay['reference_diagnostic'] = reference_recon(certificate)
    args.output.write_text(json.dumps(replay, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'decision': replay['decision'], 'witness_count': len(certificate['witnesses']),
                      'best_synthetic_K': certificate['best_synthetic_K'],
                      'rows': certificate['benchmark_rows'], 'consumer_certified': False}, indent=2))


if __name__ == '__main__':
    main()
