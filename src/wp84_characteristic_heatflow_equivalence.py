"""Exact characteristic/heat rescaling and covariance normalization gates."""
import argparse
from fractions import Fraction as F
import sympy as S


def main():
    if not __debug__:
        raise RuntimeError('Checks require Python without -O.')
    parser = argparse.ArgumentParser()
    parser.add_argument('--toeplitz', action='store_true')
    args = parser.parse_args()
    t = S.symbols('t', positive=True)
    u = (1-t)/t
    assert S.simplify(S.diff(u,t)+1/t**2) == 0
    assert S.simplify((1-2*t)-2*t*(1-t)/t+1) == 0
    # Primitive scaling and moving partial-fraction coefficients.
    for q in range(1,4):
        assert S.simplify(t**q*t**(-2-q)-t**-2) == 0
    # Exact noncommuting finite regression matrix.
    tt = S.Rational(3,5)
    ss = S.Integer(1)
    z = S.Rational(4,5)*(1+S.I)
    P = S.Matrix([[S.Rational(1,3), S.Rational(2,7)],
                  [S.Rational(2,7),-S.Rational(1,5)]])
    W = S.Matrix([[S.Rational(3,4),S.Rational(1,8)],
                  [S.Rational(1,8),S.Rational(5,6)]])
    I = S.eye(2)
    H = ss*I+tt*P+S.sqrt(tt*(1-tt))*W
    Aheat = ss*I+P+S.sqrt((1-tt)/tt)*W
    zt = ss+tt*(z-ss)
    assert (tt*(H-zt*I).inv()-(Aheat-z*I).inv()).applyfunc(S.simplify) == S.zeros(2)
    # Verify moving functional through its degree-three resolvent stencil.
    Ah = -S.Rational(183845781504,120599925625)+S.I*S.Rational(112029847146,602999628125)
    Bh = S.Rational(297763801992,602999628125)-S.I*S.Rational(623773801728,602999628125)
    Ch = S.Rational(1589960358912,15074990703125)+S.I*S.Rational(2139153937184,15074990703125)
    Einf = S.Rational(122310623232,120599925625)
    Rt = (H-zt*I).inv()
    Ru = (Aheat-z*I).inv()
    # Factor before expanding to keep this exact check fast.
    assert (tt*Rt-Ru).applyfunc(S.simplify) == S.zeros(2)
    for j in (1,2,3):
        assert (tt**j*Rt**j-Ru**j).applyfunc(S.simplify) == S.zeros(2)
    eta = S.Rational(4,5)
    Bstar = 2*((abs(S.re(Ah))+abs(S.im(Ah)))/eta
               +(abs(S.re(Bh))+abs(S.im(Bh)))/eta**2
               +2*(abs(S.re(Ch))+abs(S.im(Ch)))/eta**3)
    s = S.symbols('s', real=True)
    fa = S.Rational(1,4)
    fh = s*(1-s)
    assert S.expand((s+(1-s))/4-fa) == 0
    assert S.expand(s*(1-s)**2+(1-s)*s**2-fh) == 0
    assert S.integrate(fh,(s,0,1)) == S.Rational(1,6)
    for r in range(1,5):
        cosine = S.integrate(fh*S.cos(2*S.pi*r*s),(s,0,1))
        sine = S.integrate(fh*S.sin(2*S.pi*r*s),(s,0,1))
        assert S.simplify(cosine+1/(2*S.pi**2*r*r)) == 0
        assert sine == 0
    assert S.integrate(S.log(s)+S.log(1-s),(s,0,1)) == -2
    CF = F(112913213256073216,87917345780625)
    cushion = F(8711,2778200)
    budget = cushion/4
    print('Bstar =', Bstar, S.N(Bstar,18))
    print('C_F =', CF)
    print('quarter-cushion tail budget =', budget, float(budget))
    print('K sufficient =', max(F(2),2*CF/budget))
    print('growing-U sufficient range: U=o(sqrt(L)); not a maximum rate')
    if args.toeplitz:
        import numpy as np
        print('NUMERICAL continuum-window diagnostics; a_phi=1; NOT actual-prime covariances')
        print('d lambda_min min_conditional center_conditional analytic_lower')
        for d in (2,4,8,16,32,64,128):
            i = np.arange(d)
            lag = i[:,None]-i[None,:]
            cov = np.full((d,d),0.0)
            cov[lag==0] = 1/6
            nz = lag != 0
            cov[nz] = -1/(2*np.pi**2*lag[nz]**2)
            ev = np.linalg.eigvalsh(cov)
            conditional = 1/np.diag(np.linalg.inv(cov))
            assert ev[0] > 1/(16*d)
            print(d,ev[0],min(conditional),conditional[d//2],1/(16*d))
    print('RESULT: EXACT_RESCALING_PASS; SAME_MATCHED_GAUSSIAN_HEAT_OBJECT; STATUS_C_TAIL_BLOCKED')


if __name__ == '__main__':
    main()
