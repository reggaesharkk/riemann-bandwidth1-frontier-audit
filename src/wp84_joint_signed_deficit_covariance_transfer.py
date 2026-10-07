#!/usr/bin/env python3
"""Exact joint telescope and covariance-dependent Price replay; no consumer PASS."""
import argparse
import functools
import itertools
import json
import math
from pathlib import Path
import sympy as s
import wp84_cross_repository_hermite_adjoint as old


def check(value, label):
    if s.simplify(s.expand(value)) != 0:
        raise ValueError(f'{label}: {value}')


def average(poly, variables, covariance):
    @functools.lru_cache(None)
    def moment(powers):
        if not any(powers):
            return s.Integer(1)
        if sum(powers) % 2:
            return s.Integer(0)
        i = next(j for j, p in enumerate(powers) if p)
        rest = list(powers)
        rest[i] -= 1
        ans = 0
        for j, multiplicity in enumerate(rest):
            if multiplicity:
                tail = rest[:]
                tail[j] -= 1
                ans += multiplicity * covariance[i, j] * moment(tuple(tail))
        return s.expand(ans)
    return s.expand(sum(c * moment(p) for p, c in
                        s.Poly(s.expand(poly), *variables).terms()))


def inner(A, B):
    return s.expand(s.trace(A.conjugate().T * B) / A.rows)


def joint_telescope():
    u, g = old.u, old.g
    polys = [1 + u*g[0]**2 + u**s.Rational(5, 2)*g[0]**5/3,
             s.sqrt(u)*g[1] + u*u*g[1]**4/7,
             2-u**s.Rational(3, 2)*g[0]**3+u*u*g[0]**2*g[1]**2]
    indices = old.basis(5)
    full = old.project(polys, indices)
    _, N, L, _, _, _ = old.chain(indices)
    old.matrix_zero(2*u*full.diff(u)-(N+L)*full, 'radial evolution')
    K = 3
    low = old.basis(K)
    rows = [indices.index(a) for a in low]
    x = full[rows, :]
    metric, _, _, A0, _, _ = old.chain(low)
    phi = old.propagator(low, old.U, u)
    Y = phi.T*metric*phi
    J = old.contract(x, Y-metric, x).subs(u, old.DELTA)
    flux = []
    for n in (K+1, K+2):
        upper = [j for j, a in enumerate(indices) if sum(a) == n]
        residual = L.extract(rows, upper)*full[upper, :]/(2*u)
        flux.append(2*old.integral(old.contract(x, Y, residual)))
    retained = old.contract(x, metric, x)
    direct = retained.subs(u, old.U)-retained.subs(u, old.DELTA)
    check(J+sum(flux)-direct, 'joint endpoint identity')
    old.expect_rejection(lambda: check(J+flux[0]-direct,
                         'missing second shell'), 'missing second shell')
    return {'K': K, 'J': str(J), 'fluxes': list(map(str, flux)),
            'retained_endpoint_difference': str(direct),
            'joint_amplification_remaining': False,
            'scope': 'exact polynomial normalization witness only'}


def covariance_price():
    theta, rho = s.symbols('theta rho', real=True)
    x = s.symbols('x0:2', real=True)
    C0 = s.diag(1, 0)  # Deliberately rank deficient.
    C1 = s.Matrix([[2, 1], [1, 2]])
    change = C1-C0
    C = C0+theta*change
    H = s.Matrix([[1+x[0], x[1]], [x[1], -1+2*x[0]]])
    Q = H**2+s.I*H**5/70  # Nonzero K+2 derivative; not the consumer.
    u = s.Rational(4)
    Qu = Q.subs({v: s.sqrt(u)*v for v in x}, simultaneous=True)
    tensors = {}
    for n in range(6):
        tensors[n] = {}
        for js in itertools.product(range(2), repeat=n):
            derivative = Q
            for j in js:
                derivative = derivative.diff(x[j])
            state = derivative.subs({v: s.sqrt(u)*v for v in x}, simultaneous=True)
            tensors[n][js] = state.applyfunc(lambda p: average(p, x, C))
    for n in range(4):
        for js, M in tensors[n].items():
            price = sum((change[i, j]*tensors[n+2][js+(i, j)]
                         for i in range(2) for j in range(2)), s.zeros(2))*u/2
            old.matrix_zero(M.diff(theta)-price, 'one-copy real Price factor')
    masses, prices, explicit = [], [], []
    for n in range(4):
        mass = Sterm = Rterm = 0
        for left, ML in tensors[n].items():
            for right, MR in tensors[n].items():
                weight = s.prod(C[i, j] for i, j in zip(left, right))
                mass += weight*inner(ML, MR)
                if n:
                    w = change[left[0], right[0]]*s.prod(
                        C[i, j] for i, j in zip(left[1:], right[1:]))
                    Rterm += n*w*inner(ML, MR)
                for i in range(2):
                    for j in range(2):
                        Sterm += weight*change[i, j]*s.re(
                            inner(ML, tensors[n+2][right+(i, j)]))
        mass = s.expand(u**n*mass/s.factorial(n))
        Rterm = s.expand(u**n*Rterm/s.factorial(n))
        Sterm = s.expand(u**(n+1)*Sterm/s.factorial(n))
        check(mass.diff(theta)-Rterm-Sterm, 'projection covariance derivative')
        masses.append(mass)
        prices.append(Rterm+Sterm)
        explicit.append(Rterm)
    old.expect_rejection(lambda: check(sum(masses).diff(theta)
                         -sum(prices)+sum(explicit), 'omitted explicit C factors'),
                         'omitted explicit C factors')
    # Independent two-copy Mehler/Wick calculation, without whitening C.
    y = s.symbols('y0:2', real=True)
    Qu2 = Qu.subs(dict(zip(x, y)), simultaneous=True)
    covariance = C.row_join(rho*C).col_join((rho*C).row_join(C))
    mehler = average(inner(Qu, Qu2), x+y, covariance)
    for n in range(4):
        check(s.Poly(mehler, rho).nth(n)-masses[n], 'Mehler coefficient and n!')
    # Rank-zero endpoint theta=0 causes no division or inverse covariance.
    check(s.integrate(sum(prices), (theta, 0, 1))
          -(sum(masses).subs(theta, 1)-sum(masses).subs(theta, 0)),
          'integrated covariance comparison')
    return {'max_one_factor_derivative_order': 'K+2',
            'max_total_derivative_order': '2K+2',
            'K_witness': 3, 'U_witness': '4', 'singular_endpoint': 'PASS',
            'real_Price_factor': '1/2',
            'explicit_projection_derivative_mutation': 'REJECTED',
            'mass_polynomials': list(map(str, masses)),
            'price_polynomial': str(s.expand(sum(prices))),
            'scope': 'exact algebra, not the missing projected BV bound'}


def hostile_and_symbol():
    r = s.symbols('r', integer=True, positive=True)
    t = s.symbols('t', real=True)
    check(s.integrate(t*(1-t)*s.sin(2*s.pi*r*t), (t, 0, 1)),
          'real h-a covariance')
    check(s.integrate(t*(1-t)*s.cos(2*s.pi*r*t), (t, 0, 1))
          +1/(2*s.pi**2*r**2), 'h symbol')
    check(s.integrate(t*s.cos(2*s.pi*r*t)/2, (t, 0, 1)), 'a white symbol')
    # Finite Toeplitz sections are not exactly circulant/DFT diagonal.
    nearest = -1/(2*s.pi**2)
    distant = -1/(8*s.pi**2)
    if nearest == distant:
        raise ValueError('False finite-section Fourier diagonalization')
    x = s.symbols('x', real=True)
    c, a = s.Rational(3142, 2415), s.Rational(131, 200)
    P = 1-s.Rational(43428,13891)*x+s.Rational(37704,13891)*x*x-s.Rational(9660,13891)*x**3
    p = (c*c+a*a)**3*P**2/((x-c)**2+a*a)**3
    negative = s.factor(s.diff(p, x, 2).subs(x, 0))
    positive_point = next(v for v in (s.Rational(j, 20) for j in range(1, 81))
                          if s.diff(p, x, 2).subs(x, v) > 0)
    if negative >= 0:
        raise ValueError('Hessian sign obstruction lost')
    # Analytic limiting bounded, growing-dimensional witness from the note.
    import mpmath as mp
    mp.iv.dps = 40
    iv = mp.iv
    limit = (iv.exp(-1)*(iv.cos(1)-1)
             -iv.exp(-iv.mpf(1)/16)*(iv.cos(iv.mpf(1)/4)-1))/2
    if not limit.b < 0:
        raise ValueError('Hostile nonzero joint limit not enclosed')
    return {'field_symbols': {'a': '1/(4 a_phi^2)', 'h': 's(1-s)/a_phi^2'},
            'finite_Toeplitz_is_circulant': False,
            'consumer_scalar_p_second_at_zero': str(negative),
            'positive_second_derivative_rational_point': str(positive_point),
            'bounded_wrong_scope_joint_limit_interval': str(limit),
            'scope': 'not an actual-prime/current-Q counterexample; tests missing Hessian uniformity'}


def projected_loewner_recon():
    """Actual finite-prime six-channel diagnostics, never sign certificates."""
    import numpy as np
    from wp84_integrated_cross_error_stein_chaos import prime_state
    rows = []
    for T in (128, 256):
        mean, directions, L, N = prime_state(T)
        d = len(mean)
        k = np.arange(d)
        lag = k[:, None]-k[None, :]
        J = np.zeros((d, d))
        off = lag != 0
        J[off] = -1/(np.pi*lag[off])
        A = np.zeros((d, d)); H = A.copy(); C = A.copy()
        for p in range(2, N+1):
            if any(p % q == 0 for q in range(2, math.isqrt(p)+1)):
                continue
            sp = np.log(p)/L
            cp2 = np.log(p)**2/(L*L*p)
            phase = 2*np.pi*lag*sp
            A += cp2*np.cos(phase)/2
            H += 2*cp2*(1-sp)**2*np.cos(phase)
            C -= cp2*(1-sp)*np.sin(phase)
        Hr = np.eye(d)/6
        Hr[off] = -1/(2*np.pi**2*lag[off]**2)
        da, dh, dc = np.eye(d)/4-A, Hr-H, -C
        def deltaV(X):
            return (dh*X+(dc*X)@J-dc*(X@J)+dc.T*(J@X)-J@(dc.T*X)
                    +(da*(J@X))@J-da*(J@X@J)-J@(da*X)@J+J@(da*(X@J)))
        z = 3142/2415+1j*131/200
        R = np.linalg.inv(mean-z*np.eye(d))
        Uc = np.eye(d)+2j*z.imag*R
        factors = [np.linalg.matrix_power(Uc, j)@R for j in range(3)]
        pairs = [(l, r) for l in range(3) for r in range(3-l)]
        gram = np.empty((6, 6), complex)
        for i, (l, r) in enumerate(pairs):
            for j, (m, n) in enumerate(pairs):
                gram[i, j] = np.trace(factors[r].conj().T
                    @deltaV(factors[l].conj().T@factors[m])@factors[n])/d
        eigen = np.linalg.eigvalsh((gram+gram.conj().T)/2)
        rows.append({'T': T, 'd': d, 'N': N,
                     'six_response_Gram_difference_eigenvalues': eigen.tolist()})
    return {'rows': rows, 'rigorous': False,
            'scope': 'finite full-sharp actual-prime mean, u=0; does not certify projected order at theta,u or the signed cross Hessian'}


def main():
    if not __debug__:
        raise RuntimeError('Run without -O')
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output', type=Path)
    ap.add_argument('--recon', action='store_true')
    args = ap.parse_args()
    c0 = s.Rational(28047, 34000000)
    out = {'schema': 'wp84-joint-signed-deficit-covariance-transfer-v1',
           'parent': 'ab70f368e66ccb04f15e65e59223ebf9eee0832b',
           'joint_telescope': joint_telescope(),
           'covariance_price': covariance_price(),
           'hostile_and_symbol': hostile_and_symbol(),
           'ledger': {'cushion': str(old.CUSHION), 'delta': '1/100000',
                      'K': 16, 'kappa_star': '1/2', 'initial_cost_upper': str(c0),
                      'initial_only_remaining': str(old.CUSHION-c0),
                      'covariance_transfer_error_certified': False,
                      'reference_signed_deficit': None,
                      'additional_Malliavin_residual_cost': '0 (exact telescope)',
                      'final_margin': None},
           'consumer_certified': False, 'certified_K_U': None,
           'decision': 'C: projected two-copy covariance-substitution extension remains open'}
    if args.recon:
        out['projected_loewner_diagnostic'] = projected_loewner_recon()
    result = json.dumps(out, indent=2, sort_keys=True)+'\n'
    if args.output:
        args.output.write_text(result, encoding='utf-8')
    print(result, end='')


if __name__ == '__main__':
    main()
