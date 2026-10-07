"""Exact finite HS-square/lock audit. No prime asymptotic is certified."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import argparse
import json
import sympy as S


def check(ok, label):
    if not ok:
        raise ValueError(label)


def main(write=False):
    a = [F(-19101,185500), F(961,3710), F(31,50), F(-371,500)]
    c = [sum((a[r]*a[s] for r in range(4) for s in range(4) if r+s==b), F(0)) for b in range(7)]
    check(c[4]==0, 'c4 cancellation')
    band=F(128952763,92407500000)
    var=F(26060119,12734908593750)
    threshold=F(21,200)-band
    base=c[0]+c[2]/3
    ideal=base+c[5]/36+c[6]*F(157,630)
    relaxed=base+c[5]/36+c[6]*F(34,135)
    paid_ideal=threshold-ideal-var
    paid_relaxed=threshold-relaxed-var
    joint=threshold-base-var
    check(paid_relaxed==F(52897896569489,572357731837500000), 'frozen margin')
    check(joint==F(64788151489666079,572357731837500000), 'frozen signed target')
    check(paid_ideal-paid_relaxed==F(19663,13500000), 'distinct allowances')
    # A genuinely complex Hermitian example, including section boundaries.
    X=S.Matrix([[S.Rational(1,3),1+S.I,0],[1-S.I,-S.Rational(2,5),2],[0,2,S.Rational(3,7)]])
    d=3
    powers=[S.eye(d)]+[X**r for r in range(1,4)]
    Q=sum((S.Rational(v.numerator,v.denominator)*powers[r] for r,v in enumerate(a)), S.zeros(d))
    energy=S.expand(sum(Q[i,j]*S.conjugate(Q[i,j]) for i in range(d) for j in range(d))/d)
    check(S.simplify(energy-S.trace(Q**2)/d)==0, 'HS trace equality')
    pairs={}
    for r,s in product(range(4),repeat=2):
        pair=S.expand(sum(powers[r][i,j]*S.conjugate(powers[s][i,j]) for i in range(d) for j in range(d))/d)
        check(S.simplify(pair-S.trace(X**(r+s))/d)==0, 'all 16 polarized path blocks')
        # Explicit finite internal-vertex path sum; all vertices restricted to I.
        for i,j in product(range(d),repeat=2):
            if r==0:
                path=S.Integer(i==j)
            else:
                path=0
                for internal in product(range(d),repeat=r-1):
                    vertices=(i,)+internal+(j,)
                    path+=S.prod(X[vertices[t],vertices[t+1]] for t in range(r))
            check(S.expand(path-powers[r][i,j])==0, 'entrywise chains')
        pairs[f'{r},{s}']=str(pair)
    # Zero extension to a 4 by 4 analysis grid. No cyclic matrix multiplication.
    M=4
    omega=S.I
    spectra=[]
    for P in powers:
        spectra.append([[S.expand(sum(P[i,j]*omega**(-(u*i+v*j)) for i in range(d) for j in range(d)))
                         for v in range(M)] for u in range(M)])
    spectral=0
    for u,v in product(range(M),repeat=2):
        amp=S.expand(sum(S.Rational(x.numerator,x.denominator)*spectra[r][u][v] for r,x in enumerate(a)))
        spectral+=S.expand(amp*S.conjugate(amp))
    check(S.simplify(spectral/(d*M*M)-energy)==0, 'complete coefficient-weighted positive Parseval')
    for r,s in product(range(4),repeat=2):
        inner=sum(spectra[r][u][v]*S.conjugate(spectra[s][u][v]) for u,v in product(range(M),repeat=2))
        check(S.simplify(inner/(d*M*M)-S.sympify(pairs[f'{r},{s}']))==0, 'polarized Parseval')
    # Endpoint equality is weaker than a full relative-position lock.
    path1=(0,1,3); path2=(0,2,3)
    check(path1[0]==path2[0] and path1[-1]==path2[-1], 'shared endpoints')
    check(len(set(y-x for x,y in zip(path1,path2)))>1, 'no common shift witness')
    # Exact public product/polarization identity on Z/2, including complex data.
    G=range(2); b=3
    f=[[1+S.I,2],[3,1-S.I],[2,4]]
    g=[[2,3-S.I],[1+S.I,2],[5,1]]
    def N(fs,j):
        return S.expand(sum(fs[0][x]*S.prod(fs[k][(x+j[k-1])%2] for k in range(1,b)) for x in G))
    lhs=sum(N(f,j)*S.conjugate(N(g,j)) for j in product(G,repeat=b-1))
    rhs=sum(S.prod(sum(f[k][x]*S.conjugate(g[k][(x+t)%2]) for x in G) for k in range(b)) for t in G)
    check(S.expand(lhs-rhs)==0, 'complex public product polarization')
    hat=lambda fs,k,xi: sum(fs[k][x]*(-1)**(xi*x) for x in G)
    fourier=sum(hat(f,0,(-sum(xi))%2)*S.prod(hat(f,k,xi[k-1]) for k in range(1,b))*
                S.conjugate(hat(g,0,(-sum(xi))%2)*S.prod(hat(g,k,xi[k-1]) for k in range(1,b)))
                for xi in product(G,repeat=b-1))/2**(b-1)
    check(S.expand(lhs-fourier)==0, 'full multidimensional coupled-frequency Parseval')
    # Exact free-slot Fubini; identity padding is constrained, not this operation.
    free=[2,7]
    check(sum(N(f,j)*sum(free) for j in product(G,repeat=2))==sum(N(f,j)*free[z] for j in product(G,repeat=2) for z in G), 'free slot')
    check(X*S.eye(d)==X and X*S.ones(d)!=X, 'identity padding is not a free slot')
    # No arithmetic carrier cancellation: endpoints leave the nonunit ratio.
    check(F(2,3)!=1, 'diagonal two-prime carrier witness')
    # Covariance-only upper bounds cannot control the square: sixth grows M^4/3.
    t=S.symbols('t', positive=True)
    q=lambda x:sum(S.Rational(v.numerator,v.denominator)*x**r for r,v in enumerate(a))
    scalar=S.expand((1-1/(3*t**2))*q(0)**2+(q(t)**2+q(-t)**2)/(6*t**2))
    check(S.expand(scalar).coeff(t,4)==S.Rational(c[6].numerator,c[6].denominator)/3, 'no universal covariance upper certificate')
    data={
        'parent':'e85002990e9fb65dc2dd1cc1aea145c7f9910b06',
        'decision':'D', 'strict_gt79':False, 'prime_arithmetic_proved':False,
        'q':[str(v) for v in a], 'square_coefficients':[str(v) for v in c],
        'R_band':6000,'pole_height':'221/200',
        'square_threshold_strict':str(threshold), 'band':str(band),'variance_envelope':str(var),
        'ideal_square_reference':str(ideal),'relaxed_square_reference':str(relaxed),
        'ideal_paid_slack':str(paid_ideal),'relaxed_paid_slack':str(paid_relaxed),
        'ideal_direct_slack_before_variance':str(threshold-ideal),
        'relaxed_direct_slack_before_variance':str(threshold-relaxed),
        'ideal_relative_paid_precision':str(paid_ideal/ideal),
        'relaxed_relative_paid_precision':str(paid_relaxed/relaxed),
        'signed_cap':str(joint),'finite_example_energy':str(energy),
        'finite_pair_blocks':pairs,'public_polarized_example':str(S.expand(lhs)),
        'common_shift_counterexample':[path1,path2],
        'carrier_witness_ratio':'2/3','spectral_dimension':2,
        'spectral_grid':[M,M],'spectral_weight':'1/(d*M^2)',
        'tests':['all 16 path blocks','complex Hermitian HS identity','full weighted Parseval',
                 'all 16 polarized Parseval blocks','public complex product identity',
                 'complete public coupled-frequency transform','free-slot Fubini',
                 'endpoint/common-shift counterexample','identity-padding counterexample',
                 'covariance upper-bound obstruction']}
    if write:
        out=Path(__file__).resolve().parents[1]/'notes/WP84_ROBUST_CUBIC_HS_SQUARE_CERTIFICATE.json'
        out.write_text(json.dumps(data,indent=2)+'\n')
    for key in ['square_threshold_strict','ideal_paid_slack','relaxed_paid_slack','ideal_relative_paid_precision','relaxed_relative_paid_precision']:
        val=F(data[key]); print(key, '=', val, '=', format(float(val),'.15g'))
    print('PASS: exact finite path, HS, polarized product and full weighted spectral identities.')
    print('Decision D: endpoint equality does not imply the full common lock; log-product carrier survives.')
    print('OPEN: frozen signed theorem (12). No actual-prime upper bound or strict >79 certificate.')


if __name__=='__main__':
    parser=argparse.ArgumentParser(); parser.add_argument('--write',action='store_true')
    main(parser.parse_args().write)
