"""All-radius Gaussian obstruction and interval localization-budget audit.

No prime CLT, Monte Carlo or synthetic chaos value is used. Polynomial
minorants are exact. Interval calculations use outward rational endpoints.
"""
import json
import hashlib
import math
from fractions import Fraction as F
from pathlib import Path
import sympy as s
import mpmath as mp
import wp84_mehler_weak_dual_certificate as dual

ROOT = Path(__file__).resolve().parents[1]
T = F(100001, 100000)
DELTA = F(1, 100000)
EPSILON = F(8711, 2778200)
EINF = F(7761139416076220170204368647089, 1680256283972002400160000000000)
Q4 = [F(-3, 250), F(27, 50), F(-1, 50)]
Q6 = [F(1265, 10000), F(-8561, 10000), F(25977, 10000), F(-13633, 10000)]


def check(ok, label):
    if not ok:
        raise ValueError(label)


def rat(q):
    q = F(q)
    return s.Rational(q.numerator, q.denominator)


def iv(q):
    q = F(q)
    return mp.iv.mpf(q.numerator)/q.denominator


def endpoints(v):
    def exact(t):
        sign, mantissa, exponent, _ = t
        return (-1 if sign else 1)*F(mantissa)*F(2)**exponent
    return exact(v._mpi_[0]), exact(v._mpi_[1])


def outward(v, digits=40):
    lo, hi = endpoints(v)
    scale = 10**digits
    return [str(F(math.floor(lo*scale), scale)), str(F(math.ceil(hi*scale), scale))]


def pi_enclosure():
    def atan(q, n=60):
        v = sum((-1)**k*q**(2*k+1)/F(2*k+1) for k in range(n))
        nxt = (-1)**n*q**(2*n+1)/F(2*n+1)
        return min(v, v+nxt), max(v, v+nxt)
    a, b = atan(F(1, 5)), atan(F(1, 239))
    return 16*a[0]-4*b[1], 16*a[1]-4*b[0]


def minorant(coeff):
    x, y = s.symbols('x y')
    c, a = s.Rational(3142, 2415), s.Rational(131, 200)
    p = lambda x: 1-s.Rational(43428, 13891)*x+s.Rational(37704, 13891)*x*x-s.Rational(9660, 13891)*x**3
    dp, dm = ((1+x-c)**2+a*a)**3, ((1-x-c)**2+a*a)**3
    num = (c*c+a*a)**3*(p(1+x)**2*dm+p(1-x)**2*dp)
    den = 2*dp*dm
    b = sum(rat(v)*x**(2*j) for j, v in enumerate(coeff))
    poly = s.Poly(s.expand(num-b*den), x)
    check(all(poly.nth(j) == 0 for j in range(1, poly.degree()+1, 2)), 'even minorant numerator')
    yp = s.Poly(sum(poly.nth(2*j)*y**j for j in range(poly.degree()//2+1)), y)
    check(yp.count_roots(0, s.oo) == 0 and yp.eval(0) > 0, 'global nonnegative minorant')
    return {'coefficients_in_x_squared': list(map(str, coeff)),
            'positive_numerator_coefficients_in_x_squared': [str(yp.nth(j)) for j in range(yp.degree()+1)],
            'degree': yp.degree(), 'positive_half_line_roots': 0}


def wick_check():
    u = s.Symbol('u', real=True)
    result = []
    for m in (2, 3, 4):
        jmat = s.Matrix(m, m, lambda i, j: u/(j-i) if i != j else 0)
        def cov(i, j, k, l):
            if i == j and k == l:
                return s.Rational(1, 6) if i == k else -u*u/(2*(i-k)**2)
            if i == j or k == l:
                return s.Integer(0)
            return u*u*s.Rational(int(i == k)-int(i == l)-int(j == k)+int(j == l),
                                  4*(j-i)*(l-k))
        moment = sum(cov(i,j,j,k)*cov(k,l,l,i)+cov(i,j,k,l)*cov(j,k,l,i)
                     +cov(i,j,l,i)*cov(j,k,k,l)
                     for i in range(m) for j in range(m)
                     for k in range(m) for l in range(m))/m
        rowmass = [sum(jmat[i,j]**2 for j in range(m)) for i in range(m)]
        s2 = sum(s.Rational(m-r, r*r) for r in range(1,m))
        s4 = sum(s.Rational(m-r, r**4) for r in range(1,m))
        components = [s.Rational(1,12), 2*u*u*s2/(3*m), -u**4*s4/m,
                      (s.trace(jmat**4)+4*sum(x*x for x in rowmass)
                       +sum(jmat[i,j]**4 for i in range(m) for j in range(m)))/(8*m)]
        check(s.expand(moment-sum(components)) == 0, 'fourth Wick geometry')
        result.append({'m': m, 'fourth_moment': str(s.expand(moment)),
                       'diagonal_adjacent_alternating_alpha_components': list(map(str, components))})
    return result


def moments2():
    u = s.Symbol('u', positive=True)
    v0, v1, v2 = rat(T)*(s.Rational(1,12)-u/4), rat(T)*(s.Rational(1,12)+u/4), rat(T)*u/2
    er2 = v1+v2
    er4 = 3*v1*v1+2*v1*v2+3*v2*v2
    er6 = 15*v1**3+9*v1*v1*v2+9*v1*v2*v2+15*v2**3
    moments = [s.Integer(1), v0+er2, 3*v0*v0+6*v0*er2+er4,
               15*v0**3+45*v0*v0*er2+15*v0*er4+er6]
    bound = s.Poly(s.expand(sum(rat(q)*v for q,v in zip(Q6, moments))), u)
    coeff = [F(str(bound.nth(j))) for j in range(4)]
    ulo, uhi = F(1,10), F(103,1000)
    lo = sum(q*(ulo**j if q >= 0 else uhi**j) for j,q in enumerate(coeff))
    check(lo > F(109,1000), 'two-site uniform rational gap')
    return moments, coeff, lo


def harmonic(m):
    if m < 1000:
        return iv(sum(F(1,k) for k in range(1,m+1)))
    # H_m = log(m)+gamma+1/(2m)-theta/(12m^2), 0<theta<1.
    # NIST DLMF 5.11.2, positive-real first-omitted-term remainder.
    center = mp.iv.log(m)+mp.iv.euler+iv(F(1,2*m))
    return center+mp.iv.mpf([-1,0])*iv(F(1,12*m*m))


def localization_coefficient(lam, U):
    # Inherited eventual prime mass <=2, uniform a_phi>=1/2.
    return 43*(iv(lam)*mp.iv.sqrt(2+iv(U))+mp.iv.sqrt(2+iv(DELTA)))


def localization_squared(m, lam, U, pii):
    return localization_coefficient(lam,U)**2*8/(pii*pii)*(harmonic(m)+1)/m


def minimum_R(lam, U, allocation, pii):
    target = allocation*allocation
    def wins(m):
        lo, hi = endpoints(localization_squared(m,lam,U,pii))
        if hi < target:
            return True
        if lo >= target:
            return False
        raise ValueError('Interval precision cannot decide radius')
    lo, hi = 1, 2
    while not wins(hi):
        lo, hi = hi, hi*2
    while hi-lo > 1:
        mid = (lo+hi)//2
        if wins(mid):
            hi = mid
        else:
            lo = mid
    check(wins(hi) and not wins(hi-1), 'minimum integer radius bracket')
    return {'U': str(U), 'allocation': str(allocation), 'minimum_R': hi-1,
            'cost_at_R_interval': outward(mp.iv.sqrt(localization_squared(hi,lam,U,pii)), 50),
            'cost_at_previous_R_interval': outward(mp.iv.sqrt(localization_squared(hi-1,lam,U,pii)), 50)}


def main():
    check(__debug__, 'No -O')
    mp.mp.dps = mp.iv.dps = 100
    parent = json.loads((ROOT/'notes/WP84_DIRECT_PRIME_FIELD_STATE_LAW_CERTIFICATE.json').read_text())
    lower = next(w for w in parent['witnesses'] if w['kind']=='lower')
    lam = list(map(F,lower['coefficients']))
    Lambda = sum(abs(v) for v in lam)
    pilo, pihi = pi_enclosure()
    check(pihi < F(355,113), 'rational pi upper')
    check(pilo*pilo > F(1000,103) and pihi*pihi < 10, 'two-site pi interval')
    pii = mp.iv.pi
    moments, sextic, L2 = moments2()
    Lbig = -F(3,250)+F(27,50)*T*(F(1,6)+F(3,4)*F(113,355)**2)-T*T/F(100)
    check(Lbig > F(109,1000), 'all m>=3 rational gap')
    radii = [0,1,2,3,4,6,8,12,16,24,32]
    rows = []
    uiv = 1/(pii*pii)
    upper = EINF*(2-sum(v for v in lam if v < 0))
    for R in radii:
        m = R+1
        second = iv(T)*(iv(F(1,6))+sum(iv(F(m-r,m*r*r)) for r in range(1,m))*uiv)
        if R == 0:
            lb = iv(F(2813,25750))
        elif R == 1:
            lb = sum(iv(q)*uiv**j for j,q in enumerate(sextic))
        else:
            lb = -iv(F(3,250))+iv(F(27,50))*second-iv(T*T/F(100))
        rows.append({'R':R,'m':m,'second_moment_interval':outward(second),
                     'certified_GaussianValue_lower_interval':outward(lb),
                     'complete_signed_defect_upper_rational':str(upper),
                     'localization_cost_U_delta_interval':outward(mp.iv.sqrt(localization_squared(m,Lambda,DELTA,pii))),
                     'actual_gain_vs_R0':None})
    budget = [minimum_R(Lambda,U,EPSILON/F(div),pii)
              for U in (DELTA,F(1)) for div in (1,2,4,10)]
    initial = F(53503,66000000)
    gap = F(109,1000)+initial-F(21,200)
    check(gap == F(317503,66000000), 'full Gaussian-side negative margin')
    paths = ['notes/WP84_DIRECT_PRIME_FIELD_STATE_LAW.md',
             'notes/WP84_DIRECT_PRIME_FIELD_STATE_LAW_CERTIFICATE.json',
             'notes/WP84_TAIL_CAPPED_EXACT_FRONTIER_CONSUMER.md']
    out = {'schema':'wp84-positive-lag-Gaussian-viability-v1',
           'parent':'c3fbdd74a1a75ceb8d77ab1066b311bf28f481be',
           'decision':'A', 'GaussianValue_definition':'E_inf minus complete compiled signed observable',
           'fixed_delta':str(DELTA), 'uniform_all_R_all_U_lower':'109/1000',
           'quartic_minorant':minorant(Q4),'sextic_minorant':minorant(Q6),
           'two_site_moments_in_u':list(map(str,moments)),
           'two_site_lower_coefficients_in_u':list(map(str,sextic)),
           'two_site_simple_rational_lower':str(L2),
           'all_m_ge3_simple_rational_lower':str(Lbig),
           'pi_Machin_bounds':[str(pilo),str(pihi)],
           'wick_geometry_checks':wick_check(),
           'Gaussian_reference_bounds_by_R':rows,
           'witnesses':parent['witnesses'], 'dual_replay':[dual.verify(w) for w in parent['witnesses']],
           'Lambda_U':str(Lambda), 'Lambda_total':str(Lambda+1),
           'localization_prime_mass':'2', 'localization_uniform_a_phi_lower':'1/2',
           'localization_prefactor':'43', 'localization_h':'8*(H_(R+1)+1)/(pi^2*(R+1))',
           'minimum_radius_budget_table':budget,
           'minimum_U_scope':'best possible inherited bound over U>=delta; not a winning U',
           'epsilon':str(EPSILON),'initial_payment':str(initial),
           'negative_margin_at_least':str(gap),
           'zero_localization_cost_still_cannot_win':True,
           'arithmetic_attack_started':False,'Monte_Carlo_used':False,
           'actual_gain_decomposition_certified':False,'strict_gt79':False,
           'source_sha256':{p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in paths}}
    path=ROOT/'notes/WP84_POSITIVE_LAG_GAUSSIAN_VIABILITY_CERTIFICATE.json'
    path.write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print('PASS: global quartic/sextic minorants, Gaussian Wick geometry, all-R obstruction.')
    print('Decision A: complete Gaussian defect >=109/1000 for all R and U.')
    print('Gaussian-side margin <= -',gap,'even before localization cost.')
    for row in budget:
        print('U=',row['U'],'allocation=',row['allocation'],'minimum R=',row['minimum_R'])


if __name__=='__main__':
    main()
