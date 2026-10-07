"""Exact block-localization/covariance audit; no deterministic-prime CLT claim.

Run from any directory. Output is a proof-algebra certificate, not a measured
Gaussian consumer value. All acceptance checks use Fraction or SymPy.
"""
from fractions import Fraction as F
from pathlib import Path
import hashlib
import json
import math
import sympy as s
import wp84_mehler_weak_dual_certificate as dual
import wp84_actual_state_signed_dual_flux as flux
import mpmath as mp

ROOT = Path(__file__).resolve().parents[1]


def check(ok, label):
    if not ok:
        raise ValueError(label)


def zero(x, label):
    check(s.simplify(s.expand_complex(x)) == 0, label)


def boundary_checks():
    # Uniform translate of a partition, including its two short edge blocks.
    for m in range(1, 9):
        for i in range(13):
            for j in range(13):
                count = sum((i - t)//m != (j - t)//m for t in range(m))
                check(F(count, m) == min(F(1), F(abs(i-j), m)), 'cut probability')
    # pi^2 is factored out: exact arbitrary real scalar sequence, all offsets.
    d, m = 9, 4
    a = [F((i*i + 3*i) % 11 - 5, 7) for i in range(d)]
    cut = sum(
        sum((a[i]-a[j])**2/F((i-j)**2)
            for i in range(d) for j in range(d)
            if i != j and (i-t)//m != (j-t)//m)
        for t in range(m))/m/d
    kernel = sum(min(F(1), F(abs(r), m))/r**2
                 for r in range(-d+1, d) if r)
    mass = sum(x*x for x in a)/d
    check(cut <= 4*mass*kernel, 'weighted HS cut inequality')
    hm = sum(F(1, r) for r in range(1, m+1))
    check(kernel <= 2*(hm+1)/m, 'infinite kernel tail enclosure')
    # The harmonic term cannot be deleted from this particular proof.
    check(sum(F(1, r*32) for r in range(1, 33)) > F(1, 32),
          'reject unsupported constant/R replacement')
    return {'cut_probability': 'min(1,abs(i-j)/m)',
            'HS_squared_upper': '8*M*(H_m+1)/(pi^2*m)',
            'exact_test_mass': str(mass), 'exact_pi_squared_cut': str(cut),
            'all_boundary_tests_pass': True}


def covariance_checks():
    t = s.Symbol('t', real=True, nonzero=True)
    ints = [s.Integer(0)]
    for j in range(1, 4):
        ints.append(s.expand(1/(s.I*t)-j*ints[-1]/(s.I*t)))
    # Integral I_0 at nonzero integer lag is zero; endpoint phase is one.
    zero(ints[1] + s.I/t, 'I1')
    zero(ints[2] + s.I/t - 2/t**2, 'I2')
    zero(ints[3] + s.I/t - 3/t**2 - 6*s.I/t**3, 'I3')
    zero(s.re(ints[1])/2, 'alpha nonzero-lag covariance')
    zero(s.im(ints[1]-ints[2]), 'alpha beta covariance')
    zero(2*s.re(ints[1]-2*ints[2]+ints[3])+2/t**2,
         'beta nonzero-lag covariance')
    var = [F(1, j+1) for j in range(1, 4)]
    check(2*(var[0]-2*var[1]+var[2]) == F(1, 6), 'beta variance')
    # A positive spectral Gram makes every finite complex covariance PSD.
    x = s.Symbol('x', real=True)
    polys = [s.Integer(1), s.I*x]
    gram = s.Matrix([[s.integrate(x*p*s.conjugate(q), (x, 0, 1))
                      for q in polys] for p in polys])
    check(gram.det() == s.Rational(1, 72), 'one-site derivative Gram')
    # Pair covariance alone does not give conditional phase independence.
    signs = [(x, y, x*y) for x in (-1, 1) for y in (-1, 1)]
    check(all(sum(v[j] for v in signs) == 0 for j in range(3)), 'zero means')
    check(all(sum(v[i]*v[j] for v in signs) == 0
              for i in range(3) for j in range(i)), 'zero pair covariances')
    check(F(sum(v[0]*v[1]*v[2] for v in signs), 4) == 1,
          'conditional-dependence hostile example')
    return {'I1_nonzero_lag': str(ints[1]), 'I2_nonzero_lag': str(ints[2]),
            'I3_nonzero_lag': str(ints[3]), 't': '2*pi*r',
            'one_site_Q_D_gram': str(gram),
            'pseudocovariance_reference': 'zero',
            'deterministic_pair_covariance': 'proved in note, not a CLT',
            'conditional_independence_rejected': True}


def scalar_gaussian_certificate():
    # R=0: initial noisy baseline is 1+N(0,(1+delta)/6).
    # This diagnostic is not extrapolated to R>0 or to the full operator.
    x = s.Symbol('x')
    c, a = s.Rational(3142, 2415), s.Rational(131, 200)
    p = 1-s.Rational(43428, 13891)*x+s.Rational(37704, 13891)*x*x-s.Rational(9660, 13891)*x**3
    den = ((x-c)**2+a*a)**3
    num = (c*c+a*a)**3*p*p
    lower = s.Rational(29, 50)
    poly = s.Poly(num-lower*den, x)
    check(poly.count_roots(s.Rational(9, 10), s.Rational(11, 10)) == 0,
          'scalar interval has no boundary root')
    check(poly.eval(1) > 0, 'scalar consumer lower interval sign')
    v = F(100001, 600000)
    check(2*F(22, 7)*v < F(103, 100)**2, 'Gaussian density normalization')
    check(F(1, 100)/(2*v) < F(3, 100), 'Gaussian exponent enclosure')
    exact_initial_lower = F(29, 50)*F(1, 5)*F(97, 103)
    check(exact_initial_lower > F(21, 200), 'R0 initial energy obstruction')
    mp.iv.dps = 40
    def iv(q):
        q = F(q)
        return mp.iv.mpf(q.numerator)/q.denominator
    ci, ai, vi = iv(F(3142, 2415)), iv(F(131, 200)), iv(v)
    r6 = (ci*ci+ai*ai)**3
    total = mp.iv.mpf(0)
    bins = 4096
    for k in range(bins):
        lo = F(-4)+F(8*k, bins)
        hi = lo+F(8, bins)
        z = mp.iv.mpf([str(lo.numerator/lo.denominator),
                      str(hi.numerator/hi.denominator)])
        # Endpoints are dyadic; these decimal strings represent them exactly.
        y = 1+z
        pp = 1-iv(F(43428, 13891))*y+iv(F(37704, 13891))*y*y-iv(F(9660, 13891))*y**3
        ff = r6*pp**2/((y-ci)**2+ai*ai)**3
        density = mp.iv.exp(-z*z/(2*vi))/mp.iv.sqrt(2*mp.iv.pi*vi)
        total += ff*density*iv(F(8, bins))
    einf = F(7761139416076220170204368647089, 1680256283972002400160000000000)
    tail = iv(einf)*2*mp.iv.exp(-16/(2*vi))
    def exact_mpf(t):
        sign, mantissa, exponent, _ = t
        return (-1 if sign else 1)*F(mantissa)*(F(2)**exponent)
    lo = exact_mpf(total._mpi_[0])
    hi = exact_mpf((total+tail)._mpi_[1])
    scale = 10**9
    enclosure = [F((lo*scale).__floor__(), scale),
                 F((hi*scale).__ceil__(), scale)]
    check(enclosure[0] >= exact_initial_lower, 'quadrature stronger than rational diagnostic')
    return {'R': 0, 'initial_variance': str(v), 'quadrature_bins': bins,
            'quadrature_interval': list(map(str, enclosure)),
            'quadrature_scope': 'initial Gaussian energy only; not full signed F',
            'support_interval': ['9/10', '11/10'], 'consumer_lower_on_interval': '29/50',
            'consumer_lower_polynomial_ascending': [str(poly.nth(j)) for j in range(7)],
            'density_lower_on_centered_interval': '97/103',
            'independent_rational_initial_lower': str(exact_initial_lower),
            'R0_any_U_signed_upper': str(einf-exact_initial_lower),
            'R0_cannot_pay_gt79': True, 'extension_to_positive_R_claimed': False}


def main():
    check(__debug__, 'Python -O is not accepted')
    src = json.loads((ROOT/'notes/WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF_CERTIFICATE.json').read_text())
    witnesses = [w for w in src['witnesses'] if w['K'] == 32]
    replay = [dual.verify(w) for w in witnesses]
    lower = next(w for w in witnesses if w['kind'] == 'lower')
    lam = list(map(F, lower['coefficients']))
    amplification = sum(abs(x) for x in lam)
    einf = F(7761139416076220170204368647089, 1680256283972002400160000000000)
    epsilon, w0, initial = F(8711, 2778200), F(1415, 13891), F(53503, 66000000)
    threshold = einf-w0+initial-epsilon
    check(threshold == F(83446820694177651440799215197979,
                         18482819123692026401760000000000), 'exact threshold')
    rows, _ = flux.constants()
    constants = [F(43, 20)]+[F(row['C_r_rational_upper']) for row in rows[:4]]
    derivatives = [sum(math.comb(n, j)*constants[j]*constants[n-j]
                       for j in range(n+1))*(amplification+1)*6**n
                   for n in range(1, 5)]
    gaussian_interval = [einf*(sum(x for x in lam if x < 0)-1),
                         einf*sum(x for x in lam if x > 0)]
    m = 401
    harmonic = sum(F(1, r) for r in range(1, m+1))
    # pi>3: an outward rational enclosure for the squared tail factor.
    tail_factor = F(8, 9)*(harmonic+1)/m
    paths = ['notes/WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION.md',
             'notes/WP84_RESONANT_D2_UNIFORM_BV_CLOSURE.md',
             'notes/WP84_COMPILED_MEHLER_PRIME_LINDEBERG.md',
             'notes/WP84_SHIFTED_K2_GRAM_CANCELLATION.md',
             'notes/WP84_TAIL_CAPPED_EXACT_FRONTIER_CONSUMER.md',
             'notes/WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF_CERTIFICATE.json']
    out = {'schema': 'wp84-direct-prime-field-state-law-v1',
           'parent': 'aaa7410af42d40f56784b0a7535a64dd018f1aa2',
           'decision': 'D', 'localization_closed': True,
           'boundary': boundary_checks(), 'covariance': covariance_checks(),
           'witnesses': witnesses, 'independent_dual_replay': replay,
           'Lambda_U': str(amplification), 'Lambda_total': str(amplification+1),
           'consumer_derivative_bounds_0_to_4': list(map(str, constants)),
           'Phi_R_derivative_bounds_1_to_4': list(map(str, derivatives)),
           'Phi_R_sup_absolute_upper': str((amplification+1)*einf),
           'R400_tail_factor_squared_rational_upper': str(tail_factor),
           'epsilon': str(epsilon), 'E_inf': str(einf), 'w0': str(w0),
           'initial_payment_upper': str(initial), 'required_l_minus_e': str(threshold),
           'gaussian_uniform_interval': list(map(str, gaussian_interval)),
           'scalar_gaussian_diagnostic': scalar_gaussian_certificate(),
           'gaussian_interval_is_useful_consumer_evidence': False,
           'actual_gaussian_evaluation': None, 'prime_smooth_comparison_proved': False,
           'conditional_first_second_response': 'OPEN',
           'public_candidate_pin': 'JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8',
           'literature_primary_sources': ['https://arxiv.org/html/0902.1757',
               'https://arxiv.org/html/2212.01411v2', 'https://arxiv.org/pdf/1601.02515',
               'https://arxiv.org/html/1201.5295', 'https://arxiv.org/html/1203.5328'],
           'selected_actual_U': None, 'actual_margin': None, 'strict_gt79': False,
           'rng_used': False,
           'source_sha256': {p: hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    path = ROOT/'notes/WP84_DIRECT_PRIME_FIELD_STATE_LAW_CERTIFICATE.json'
    path.write_text(json.dumps(out, indent=2)+'\n', encoding='utf-8')
    print('PASS: exact boundary weights, squared-tail inequality, derivative covariance,')
    print('conditional-dependence hostile gate, all-n dual replay, and exact ledger.')
    print('Decision D: phase-dependent smooth comparison and useful Gaussian value OPEN.')


if __name__ == '__main__':
    main()
