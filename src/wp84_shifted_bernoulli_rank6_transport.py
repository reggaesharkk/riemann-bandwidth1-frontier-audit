"""Exact fixed-pole transport audit; no numerical theorem promotion."""
import sympy as S


def main():
    if not __debug__:
        raise RuntimeError('Exact checks require Python without -O.')
    x = S.symbols('x', real=True)
    s = S.symbols('s', real=True)
    z = S.Rational(4, 5)*(1+S.I)
    P = 1-S.Rational(43428,13891)*x+S.Rational(37704,13891)*x**2-S.Rational(9660,13891)*x**3
    f = S.Rational(32,25)**3*P**2/((x-S.Rational(4,5))**2+S.Rational(16,25))**3
    A = -S.Rational(183845781504,120599925625)+S.I*S.Rational(112029847146,602999628125)
    B = S.Rational(297763801992,602999628125)-S.I*S.Rational(623773801728,602999628125)
    C = S.Rational(1589960358912,15074990703125)+S.I*S.Rational(2139153937184,15074990703125)
    Einf = S.Rational(122310623232,120599925625)
    positive = A/(x-z)+B/(x-z)**2+2*C/(x-z)**3
    pf = Einf+positive+S.conjugate(positive)
    assert S.cancel(f-pf) == 0
    # Independent scalar derivation of the deterministic one-point term.
    deterministic = -(A*((x-z)**-1+(z-s)*(x-z)**-2)
                      +B*(2*(x-z)**-2+2*(z-s)*(x-z)**-3)
                      +C*(6*(x-z)**-3+6*(z-s)*(x-z)**-4))
    assert S.cancel((x-s)*S.diff(f,x)-deterministic-S.conjugate(deterministic)) == 0
    assert S.expand(P.subs(x,z)) == (-273989+90672*S.I)/347275
    assert S.cancel(S.Rational(32,25)**3*P.subs(x,z)**2/(z-S.conjugate(z))**3-2*C) == 0
    for j in range(1,9):
        e = (x-z)**-j
        assert S.cancel((x-s)*S.diff(e,x)+j*e+j*(z-s)*(x-z)**(-j-1)) == 0
    # All-n induction: multiplying the nth leading coefficient by
    # -(n+3)(z-s) gives exactly the displayed (n+1)st coefficient.
    n = S.symbols('n', integer=True, nonnegative=True)
    lead = lambda k: 2*C*(-1)**k*S.factorial(k+2)/2*(z-s)**k
    assert S.simplify(lead(n+1)+(n+3)*(z-s)*lead(n)) == 0
    background = S.factor(f.subs(x,1))
    assert background == S.Rational(73041477632,948011895353)
    model = S.Rational(1415,13891)
    cushion = S.Rational(21,200)-model
    assert cushion == S.Rational(8711,2778200)
    allowance = S.Rational(21,200)-background
    print('background:', background, S.N(background,30))
    print('background allowance:', allowance, S.N(allowance,30))
    print('model cushion:', cushion, S.N(cushion,30))
    print('fixed-pole invariant state dimension: infinite')
    print('RESULT: EXACT_DRIFT_ELIMINATION_PASS; FINITE_STATE_CLOSURE_BLOCKED; STRICT_79_OPEN')


if __name__ == '__main__':
    main()
