#!/usr/bin/env python3
"""Independent Fraction-only verifier of ALL-n Mehler cutoff dual witnesses.

No scipy, floating arithmetic, covariance theorem, or consumer claim is imported.
"""
import argparse
from fractions import Fraction as F
import json
from pathlib import Path


def evaluate(coefficients, rhos, n):
    return coefficients[0]+sum(c*r**n for c, r in zip(coefficients[1:], rhos))


def tail_bound(coefficients, rhos, N, kind):
    if not rhos:
        return coefficients[0] if kind == 'lower' else -coefficients[0]
    # Discard only favorable exponential terms. This is an analytic bound
    # for every n>=N+1, since 0<rho<=rho_max<1.
    adverse = sum(max(F(0), c if kind == 'lower' else -c)
                  for c in coefficients[1:])
    constant = coefficients[0] if kind == 'lower' else -coefficients[0]
    return constant+adverse*max(rhos)**(N+1)


def verify(witness):
    kind = witness['kind']
    if kind not in ('lower', 'upper'):
        raise ValueError('Unknown dual orientation')
    K, N = witness['K'], witness['finite_end']
    if not isinstance(K, int) or not isinstance(N, int) or not 0 <= K <= N <= 20000:
        raise ValueError('Invalid finite coverage')
    rhos = [F(x) for x in witness['rhos']]
    coeff = [F(x) for x in witness['coefficients']]
    if len(coeff) != len(rhos)+1 or len(set(rhos)) != len(rhos):
        raise ValueError('Coefficient coverage or duplicate rho')
    if not all(0 < r < 1 for r in rhos):
        raise ValueError('rho outside (0,1)')
    powers = [F(1)]*len(rhos)
    min_slack = None
    worst_n = None
    for n in range(N+1):
        q = coeff[0]+sum(c*p for c, p in zip(coeff[1:], powers))
        target = F(int(n <= K))
        slack = target-q if kind == 'lower' else q-target
        if slack < 0:
            raise ValueError(f'{kind} dual fails at n={n}')
        if min_slack is None or slack < min_slack:
            min_slack, worst_n = slack, n
        powers = [p*r for p, r in zip(powers, rhos)]
    tail = tail_bound(coeff, rhos, N, kind)
    if tail > 0:
        raise ValueError('Uncertified infinite tail')
    # No finite list of point tests is accepted without the tail proof.
    return {'kind': kind, 'K': K, 'checked_integer_range': [0, N],
            'analytic_tail_start': N+1, 'worst_finite_n': worst_n,
            'all_n_valid': True,
            'tail_method': 'constant plus adverse coefficient sum times rho_max^(N+1)'}


def measured_bound(witness, E, measurements):
    verify(witness)
    coeff = [F(x) for x in witness['coefficients']]
    intervals = [tuple(map(F, E))]+[tuple(map(F, x)) for x in measurements]
    if len(intervals) != len(coeff) or any(lo > hi for lo, hi in intervals):
        raise ValueError('Invalid measurement enclosure coverage')
    lower = witness['kind'] == 'lower'
    return sum(c*(lo if (c >= 0) == lower else hi)
               for c, (lo, hi) in zip(coeff, intervals))


def reject(action):
    try:
        action()
    except ValueError:
        return True
    raise ValueError('Corrupted witness was accepted')


def one_rho(K, rho, kind):
    rho = F(rho)
    if kind == 'lower':
        r = rho**(K+1)
        coefficients = [-r/(1-r), 1/(1-r)]
    else:
        coefficients = [F(0), rho**(-K)]
    return {'kind': kind, 'K': K, 'finite_end': K,
            'rhos': [str(rho)], 'coefficients': list(map(str, coefficients))}


def hostile():
    for K in (0, 4, 6, 8, 12, 16, 24, 32):
        for rho in (F(1, 1000), F(1, 2), F(999, 1000)):
            lower, upper = one_rho(K, rho, 'lower'), one_rho(K, rho, 'upper')
            verify(lower); verify(upper)
            sequences = [{K: F(1)}, {K+1: F(1)}, {10000: F(1)},
                         {K: F(2, 7), K+1: F(5, 7)},
                         {0: F(1, 11), 10000: F(10, 11)}]
            for masses in sequences:
                E = sum(masses.values())
                A = sum(v*rho**n for n, v in masses.items())
                S = sum(v for n, v in masses.items() if n <= K)
                lo = measured_bound(lower, (E, E), [(A, A)])
                hi = measured_bound(upper, (E, E), [(A, A)])
                if not lo <= S <= hi:
                    raise ValueError('Abel sequence regression failed')
            t = F(3, 4)
            A = (1-t)/(1-t*rho)
            S = 1-t**(K+1)
            if not measured_bound(lower, (1, 1), [(A, A)]) <= S <= measured_bound(upper, (1, 1), [(A, A)]):
                raise ValueError('Infinite geometric tail regression failed')
    bad_rho = one_rho(6, F(1, 2), 'lower')
    bad_rho['rhos'] = ['3/4']
    bad_coefficient = one_rho(6, F(1, 2), 'upper')
    bad_coefficient['coefficients'][1] = '32'
    reject(lambda: verify(bad_rho))
    reject(lambda: verify(bad_coefficient))
    bad_tail = {'kind': 'lower', 'K': 6, 'finite_end': 6,
                'rhos': ['1/2'], 'coefficients': ['1/100', '0']}
    reject(lambda: verify(bad_tail))
    return {'boundary_atoms': True, 'high_n_10000': True,
            'geometric_infinite_tail': True, 'two_point_adversaries': True,
            'rho_near_0_and_1': True,
            'corrupt_rho_coefficient_and_unproved_tail': 'REJECTED'}


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('certificate', type=Path)
    args = ap.parse_args()
    data = json.loads(args.certificate.read_text(encoding='utf-8'))
    witnesses = data['witnesses']
    checks = [verify(w) for w in witnesses]
    print(json.dumps({'independent_exact_all_n_replay': checks,
                      'hostile': hostile(), 'consumer_certified': False}, indent=2))


if __name__ == '__main__':
    main()
