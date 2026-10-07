"""Exact first-strike budget and polynomial phase-response reconnaissance.

No long-prime estimate or strict >79 theorem is certified. The synthetic
hybrid test verifies an identity and rejects dropping higher Taylor terms.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import product
from collections import Counter
import hashlib
import json
import math
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PARENT = 'adbaef99d4aa6fd16119135a349facc127a8ca54'


def check(ok, text):
    if not ok:
        raise ValueError(text)


def partitions(items):
    if not items:
        yield []
        return
    first, *rest = items
    for part in partitions(rest):
        yield [[first]] + part
        for j in range(len(part)):
            yield part[:j] + [[first] + part[j]] + part[j+1:]


def exact_budget():
    a = [F(-19101,185500), F(961,3710), F(31,50), F(-371,500)]
    c = [sum((a[j]*a[k-j] for j in range(4) if 0 <= k-j < 4), F(0))
         for k in range(7)]
    A, B = -c[5], c[6]
    check(c[4] == 0 and A == F(11501,12500) and B == F(137641,250000), 'cubic square')
    check(sum(a[j]*(-1)**j for j in range(4)) == 1, 'support endpoint')
    model5, model6, cap6 = F(1,36), F(157,630), F(34,135)
    pair6, connected42, connected6 = F(131,420), -F(23,420), -F(1,126)
    check(pair6+connected42+connected6 == model6, 'sixth model ledger')
    check(pair6+connected42+F(2,3)*connected6 == cap6, 'two thirds')
    base = c[0]+c[2]/3
    target = base-A*model5+B*model6
    robust = base-A*model5+B*cap6
    gaussian_sharp = base+B*pair6
    band = F(128952763,92407500000)
    variance = F(26060119,12734908593750)
    margin = F(21,200)-robust-band-variance
    check(margin == F(52897896569489,572357731837500000), 'independent joint margin')
    gains = {'fifth': A*model5, 'sixth_42': -B*connected42, 'sixth_6': -B*connected6}
    check(gaussian_sharp-target == sum(gains.values()), 'moment decomposition')
    check(target == F(35116876419,344102500000), 'target exact square')
    cap = -A*model5+B*cap6+margin
    check(cap == F(21,200)-band-variance-base, 'single signed inequality')
    f5_worst = 1-36*margin/A
    f5_best = 1-36*(margin+B/378)/A
    f6_full5 = F(2,3)-126*margin/B
    required = gaussian_sharp+band+variance-F(21,200)
    check(sum(gains.values())-required == margin+B/378, 'actual-model remaining room')
    return {'centered_cubic': list(map(str,a)), 'square_coefficients': list(map(str,c)),
            'R_band': 6000, 'pole_height': '221/200', 'fourth_coefficient': '0',
            'E_gaussian_sharp_pair_reference': str(gaussian_sharp),
            'E_target_sharp_model': str(target), 'E_relaxed_target': str(robust),
            'gain_by_order_and_sector': {k:str(v) for k,v in gains.items()},
            'total_sharp_gain': str(sum(gains.values())),
            'band_payment': str(band), 'variance_payment': str(variance),
            'joint_margin': str(margin), 'single_signed_cap_strict': str(cap),
            'required_robust_gain_strict': str(required),
            'required_robust_gain_before_payments_strict': str(gaussian_sharp-F(21,200)),
            'required_robust_gain_after_band_strict': str(gaussian_sharp+band-F(21,200)),
            'required_old_Gaussian_gain_before_payments_strict': '1/250',
            'required_old_Gaussian_gain_after_initial_strict': str(F(1,250)+F(53503,66000000)),
            'fifth_fraction_if_sixth_at_relaxed_ceiling_strict': str(f5_worst),
            'fifth_fraction_if_sixth_at_model_strict': str(f5_best),
            'sixth_connected_fraction_if_full_fifth_strict': str(f6_full5),
            'model_extra_room_over_relaxed_ceiling': str(B/378),
            'fifth_loss_axis': str(margin/A), 'sixth_excess_axis': str(margin/B),
            'completion_square_center': str(A/(2*B)),
            'completion_negative_fourth_coefficient': str(-A*A/(4*B)),
            'finite_R_Gaussian_value_numeric_certified': False}


def gaussian_moment(n):
    if n % 2:
        return sp.Integer(0)
    return sp.Integer(math.prod(range(1,n,2)))


def polynomial_hybrid():
    # Three dependent but pairwise independent signs. These are NOT primes.
    gs = sp.symbols('g0:3')
    t = sp.Symbol('t')
    matrices = [sp.Matrix([[1,sp.Rational(1,3)],[sp.Rational(1,3),0]]),
                sp.Matrix([[0,sp.Rational(1,2)],[sp.Rational(1,2),1]]),
                sp.Matrix([[sp.Rational(1,5),1],[1,sp.Rational(-1,5)]])]
    roots = [(x,y,x*y) for x,y in product((-1,1),repeat=2)]
    def gauss(expr):
        p = sp.Poly(sp.expand(expr), *gs)
        return sum(coef*math.prod(gaussian_moment(n) for n in powers)
                   for powers,coef in p.terms())
    rows = []
    for b in (5,6):
        empirical = sum(sp.trace(sum((x*e for x,e in zip(root,matrices)), sp.zeros(2))**b)/2
                        for root in roots)/4
        gaussian = gauss(sp.trace(sum((g*e for g,e in zip(gs,matrices)), sp.zeros(2))**b)/2)
        responses = [sp.Integer(0)]*7
        for p in range(3):
            for root in roots:
                hybrid = sum((gs[j]*matrices[j] for j in range(p)),sp.zeros(2))
                hybrid += sum((root[j]*matrices[j] for j in range(p+1,3)),sp.zeros(2))
                polynomial = sp.Poly(sp.expand(sp.trace((hybrid+t*matrices[p])**b)/2),t)
                for m in range(1,b+1):
                    coefficient = gauss(polynomial.nth(m))
                    responses[m] += coefficient*(root[p]**m-gaussian_moment(m))/4
        check(sp.expand(empirical-gaussian-sum(responses)) == 0, 'full polynomial Taylor telescope')
        check(sum(responses[3:]) != 0, 'hostile higher-order remainder gate')
        # Reversing the prime ordering changes individual response assignments.
        rows.append({'degree':b, 'empirical_trace':str(empirical), 'Gaussian_trace':str(gaussian),
                     'A1':str(responses[1]), 'A2':str(responses[2]),
                     'A3_to_A6':list(map(str,responses[3:])),
                     'complete_difference':str(empirical-gaussian),
                     'only_A1_A2_is_not_exact':True})
    return rows


def multiplication_ansatz():
    # Distinct from the full Gaussian Loewner field. Exact operator-valued
    # semicircle recurrence, not scalar 3*variance^3 or 15*variance^3.
    x,u = sp.symbols('x u',real=True)
    def K(f):
        return sp.integrate((x-u)*f,(u,0,x))+sp.integrate((u-x)*f,(u,x,1))
    m2 = K(sp.Integer(1))
    m4 = sp.expand(m2*m2+K(m2.subs(x,u)))
    m6 = sp.expand(m2*m4+K(m2.subs(x,u))*m2+K(m4.subs(x,u)))
    fourth,sixth = sp.integrate(m4,(x,0,1)),sp.integrate(m6,(x,0,1))
    check(fourth == sp.Rational(7,30) and sixth == sp.Rational(29,140), 'multiplication-only recurrence')
    c = list(map(F,exact_budget()['square_coefficients']))
    value = c[0]+c[2]/3+c[6]*F(29,140)
    return {'mu4':str(fourth),'mu6':str(sixth),'robust_square':str(value),
            'is_full_Gaussian_Loewner_reference':False}


def structural_gates():
    from wp84_c5_pointwise_supercritical_sign import compile_terms
    counts = {}
    for b in (5,6):
        shapes = Counter(tuple(sorted(map(len,p))) for p in partitions(list(range(b))))
        check(sum(shapes.values()) == {5:52,6:203}[b], 'Bell count')
        check(shapes[(b,)] == 1 and shapes[(2,b-2)] == {5:10,6:15}[b], 'connected partitions')
        if b == 6:
            check(shapes[(2,2,2)] == 15 and shapes[(3,3)] == 10, 'sixth sectors')
        counts[str(b)] = {str(k):v for k,v in sorted(shapes.items())}
    def kernel(v):
        value = F(0)
        for sign,masks in compile_terms(len(v)):
            positions = [F(0)]+[sum((v[j] for j in mask),F(0)) for mask in masks]
            value += sign*max(F(0),1-max(positions)+min(positions))
        return value
    v = [F(-7,10),F(4,5),F(-7,10),F(3,5),F(-2,5),F(2,5)]
    w = [F(-1,10),F(3,10),F(-1,5),F(-3,10),F(4,5),F(-1,2)]
    check(kernel(v) == F(2,5) and kernel(w) == -F(1,10), 'preserved mixed C6 sign')
    # A complete sampled kernel has negative real values even without carrier.
    real_D3 = sp.simplify((1+sp.cos(3*sp.pi/5)+sp.cos(6*sp.pi/5))/3)
    check(sp.simplify(real_D3-(2-sp.sqrt(5))/6) == 0, 'signed Dirichlet witness')
    check(sp.sqrt(5)>2, 'negative sampled kernel')
    # Near-zero window, exact continuum limit of actual grid average [T,2T].
    v0 = sp.Symbol('v', real=True)
    check(sp.integrate(sp.cos(sp.pi*v0/2),(v0,1,2)) == -2/sp.pi, 'central resonance signed witness')
    return {'partition_counts':counts, 'C6_positive_witness':'2/5', 'C6_negative_witness':'-1/10',
            'Re_D3_at_3_over_10':'(2-sqrt(5))/6 < 0',
            'central_window_Re_K_at_pi_over_2T_limit':'-2/pi',
            'discarding_arithmetic_complement_using_C5_geometry_is_valid':False}


def resolved_parseval():
    # Complete (b-1)-coordinate transform on Z/2. Independent direct locks
    # and spectral evaluation, all integers/Fractions, no FFT tolerance.
    out = []
    for b in (5,6):
        fs = [(j+1,2*j-1) for j in range(b)]
        locks = list(product(range(2),repeat=b-1))
        N = {js:sum(fs[0][x]*math.prod(fs[i][(x+js[i-1])%2]
                                     for i in range(1,b)) for x in range(2)) for js in locks}
        lhs = sum(v*v for v in N.values())
        hats = [(f[0]+f[1],f[0]-f[1]) for f in fs]
        rhs = F(sum(hats[0][sum(xis)%2]**2*math.prod(hats[i][xis[i-1]]**2
                                                   for i in range(1,b)) for xis in locks),2**(b-1))
        check(lhs == rhs, 'coupled resolved multidimensional Parseval')
        # Common-shift product identity p:prod, independently counted.
        autocorr = [[sum(f[x]*f[(x+t)%2] for x in range(2)) for t in range(2)] for f in fs]
        common = sum(math.prod(a[t] for a in autocorr) for t in range(2))
        check(lhs == common, 'product/autocorrelation identity')
        out.append({'degree':b, 'lock_variance':str(lhs), 'spectral_value':str(rhs),
                    'first_factor_frequency':'-sum(xi_2,...,xi_b) mod M',
                    'normalization':'M^(-(b-1))'})
    return out


def main():
    check(__debug__, 'Python -O is not accepted')
    paths = ['notes/'+n+'.md' for n in [
        'WP84_M4_FREE_ROBUST_CUBIC_R6000','WP84_C5_POINTWISE_SUPERCRITICAL_SIGN',
        'WP84_FOURIER_REPROJECTION_BRIDGE_AUDIT','WP84_FIXED_BAND_WEIGHTED_REPROJECTION',
        'WP84_TWO_SCALE_FILTERED_TO_SHARP_MOMENT_BRIDGE',
        'WP84_FIXED_R_ARITHMETIC_FILTERED_MOMENT_TRANSFER',
        'WP84_FIXED_BAND_CHRISTOFFEL_CENTERED_LEDGER','WP84_COVARIANCE_ONLY_MOMENT_FALSIFIER',
        'WP84_DIRECT_PRIME_FIELD_STATE_LAW','WP84_POSITIVE_LAG_GAUSSIAN_VIABILITY_AND_PHASE_RESPONSE']]
    out = {'schema':'wp84-non-Gaussian-first-strike-v1', 'parent':PARENT,
           'decision':'B', 'strict_gt79':False, 'arithmetic_theorem_proved':False,
           'budget':exact_budget(), 'hybrid_noncommutative_replay':polynomial_hybrid(),
           'multiplication_only_ansatz':multiplication_ansatz(), 'structural_gates':structural_gates(),
           'resolved_Parseval_replay':resolved_parseval(),
           'public_candidate_pin':'JoshuaHKU/zeta-0.7947-reproduction@d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8',
           'public_source_sha256': {
               'paper.tex':'a2be2895348a26c93ca97ebf0f202c69cf2e3b447415c5e7174fd954601666f2',
               'pipeline/face_b5_frame.py':'f69d1982d7c48bd7b7265fb728da10e0acb514745be590dd168564198c580dec',
               'pipeline/face_b6_frame.py':'c67be2fe225a9dc5a019e6ba72ae83485d6ab751cd9f47f2a386e6479cb97e29',
               'pipeline/face_local_closure.py':'5f4e08de1a8cc22597379d3dfe139712bcd9fb87fe7b2514538ce5e570bb446a',
               'pipeline/face_parseval.py':'82c4527470aceb59edf383e4e2c2031d115cd6fe3c1c1ca9eb13db3f09ed108a',
               'certification/writeouts_verification.py':'24e998b13969669ad5e8537d5436a3e5039bcabafc29ed4b854ba303ec35f5b2'},
           'historical_compression_audit_commit':'c3f38619c4d1b534c58b91e990b5a44fd220e599',
           'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths},
           'new_parameters_optimized':False, 'prime_cutoff_changed':False, 'Monte_Carlo_used':False}
    path = ROOT/'notes/WP84_NON_GAUSSIAN_C5_C6_FIRST_STRIKE_CERTIFICATE.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    for name,value in out['budget'].items():
        print(name, '=', value)
    print('PASS: exact cubic budget, full polynomial hybrid identity, cumulant counts and signed-kernel falsifiers.')
    print('Decision B: one signed long-prime inequality OPEN; no strict >79 theorem certified.')


if __name__ == '__main__':
    main()
