"""Exact grouped OU/heat identities and conservative reference-data certificate.
No sampled measurements or synthetic data certify the consumer.
"""
import json
import math
import hashlib
from fractions import Fraction as F
from pathlib import Path
import sympy as s
import wp84_mehler_weak_dual_certificate as dual
import wp84_joint_signed_deficit_covariance_transfer as wick
import wp84_actual_state_signed_dual_flux as bounds

ROOT = Path(__file__).resolve().parents[1]
EINF = F('7761139416076220170204368647089/1680256283972002400160000000000')
W0 = F(1415, 13891)
EPS = F(8711, 2778200)

def exact_algebra(w):
    # A matrix-valued polynomial with noncommuting direction matrices.
    x, z, h = s.symbols('x z h', real=True)
    t = s.symbols('t', positive=True)
    H=s.Matrix([[h+x, 2*x],[2*x,1-x]])
    Q=H**2+s.I*H**3/5
    def expectation(M,var,cov):
        return M.applyfunc(lambda p: wick.average(p, (var,), s.Matrix([[cov]])))
    def heat(M,v):
        return M.applyfunc(lambda p: sum(v**k*s.diff(p,x,2*k)/(2**k*math.factorial(k))
                                         for k in range(4)))
    rho=s.symbols('rho',positive=True)
    conditional=heat(Q,t*(1-rho)).subs(x,s.sqrt(t*rho)*z)
    common_norm=wick.average(wick.inner(conditional,conditional),(z,),s.eye(1))
    x1,x2=s.symbols('x1 x2',real=True)
    Q1=Q.subs(x,s.sqrt(t)*x1);Q2=Q.subs(x,s.sqrt(t)*x2)
    direct=wick.average(wick.inner(Q1,Q2),(x1,x2),s.Matrix([[1,rho],[rho,1]]))
    wick.check(common_norm-direct,'conditional common noise and heat normalization')
    coeff=[s.Rational(c) for c in w['coefficients']]
    rr=[s.Rational(r) for r in w['rhos']]
    E=direct.subs(rho,1)
    grouped=coeff[0]*E+sum(c*direct.subs(rho,r) for c,r in zip(coeff[1:],rr))
    spectrum=s.Poly(direct,rho)
    spectral=sum((coeff[0]+sum(c*r**n for c,r in zip(coeff[1:],rr)))*spectrum.nth(n)
                 for n in range(4))
    wick.check(grouped-spectral,'compiled OU quadratic observable')
    # Differentiate the grouped observable once, not its measurements separately.
    dQ1=Q1.diff(h);dQ2=Q2.diff(h)
    derivative=wick.average(wick.inner(dQ1,Q2)+wick.inner(Q1,dQ2),
                              (x1,x2),s.Matrix([[1,rho],[rho,1]]))
    grouped_derivative=coeff[0]*derivative.subs(rho,1)+sum(c*derivative.subs(rho,r) for c,r in zip(coeff[1:],rr))
    wick.check(s.diff(grouped,h)-grouped_derivative,'grouped baseline derivative')
    # The frozen dual is not annihilating the constant or first chaos.
    q0=dual.evaluate(list(map(F,w['coefficients'])),list(map(F,w['rhos'])),0)
    q1=dual.evaluate(list(map(F,w['coefficients'])),list(map(F,w['rhos'])),1)
    if not q0 or not q1 or s.diff(grouped,h)==0:
        raise ValueError('Baseline sensitivity unexpectedly vanished')
    dual.reject(lambda: wick.check(common_norm-direct*2,'wrong heat normalization'))
    return {'matrix_heat_identity':'PASS','OU_compilation':'PASS',
            'grouped_baseline_derivative':'PASS','wrong_normalization':'REJECTED',
            'q0':str(q0),'q1':str(q1),'baseline_derivative_nonzero':True}

def taylor_tests():
    masses={0:F(2,7),4:F(1,7),32:F(3,7),100:F(1,7)}
    for rho in (F(1,4),F(1,2),F(3,4),F(15,16),F(31,32),F(63,64),F(127,128)):
        actual=sum(v*rho**n for n,v in masses.items())
        for r in range(1,9):
            moments=[sum(v*math.prod(range(n-k+1,n+1)) for n,v in masses.items() if n>=k)
                     for k in range(r+1)]
            poly=sum((-1)**k*(1-rho)**k*moments[k]/math.factorial(k) for k in range(r))
            remainder=(-1)**r*(actual-poly)
            if not 0<=remainder<=(1-rho)**r*moments[r]/math.factorial(r):
                raise ValueError('Taylor remainder sign or normalization')
    return 'PASS through order 8 on exact boundary/high-chaos masses'

def baseline_obstructions():
    c,a=F(3142,2415),F(131,200)
    p=[F(1),-F(43428,13891),F(37704,13891),-F(9660,13891)]
    def energy(x):
        value=sum(p[j]*x**j for j in range(4))
        return (c*c+a*a)**3*value*value/((x-c)**2+a*a)**3
    # Binomial finite difference of order five annihilates degree <=4.
    measures=[{F(k):F(math.comb(5,k),16) for k in range(6) if k%2==parity}
              for parity in (0,1)]
    for j in range(5):
        if sum(w*x**j for x,w in measures[0].items())!=sum(w*x**j for x,w in measures[1].items()):
            raise ValueError('Equal lower moments failed')
    energies=[sum(w*energy(x) for x,w in mu.items()) for mu in measures]
    if energies[0]==energies[1]:
        raise ValueError('Consumer distinguished no lower-moment pair')
    D=s.diag(0,1,2,3);H1=s.zeros(4);H2=s.zeros(4)
    H1[0,1]=H1[1,0]=1;H2[2,3]=H2[3,2]=1
    ranks=[(D*H-H*D).rank() for H in (H1,H2,(H1+H2)/2)]
    if ranks!=[2,2,4]:raise ValueError('Averaging-rank obstruction failed')
    return {'equal_moments':'0 through 4','consumer_energies':list(map(str,energies)),
            'difference':str(energies[0]-energies[1]),'displacement_ranks':ranks,
            'scope':'Generic algebra tests, not actual prime-state counterexamples'}


def main():
    original=json.loads((ROOT/'notes/WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF_CERTIFICATE.json').read_text())
    witnesses=original['witnesses']
    checks=[dual.verify(w) for w in witnesses]
    lower,upper=[w for w in witnesses if w['K']==32]
    rows,_=bounds.constants()
    intervals=[]
    for U in (1,2,4,8,16,32):
        moment_caps=[F(row['U1_M_r_upper'])*U**row['r'] for row in rows]
        intervals.append({'U':U,'E_interval':['0',str(EINF)],
                          'A_intervals':{r:['0',str(EINF)] for r in original['rhos']},
                          'factorial_moment_caps':list(map(str,moment_caps)),
                          'scope':'uniform conservative intervals; not small uncertainty enclosures'})
    delta=F(1,100000);K=32
    c0=delta/2*(F(43,20)*74+F(100,K+1))
    # For the independently-boxed data set: U=zero, delta=constant E_inf.
    # Every valid upper dual has q(0)>=1. Lower zero / upper I attains -E_inf.
    robust=-EINF
    robust_margin=EPS-(EINF-W0-robust)-c0
    benchmark=next(r for r in original['benchmark_rows'] if r['K']==K)
    if F(benchmark['synthetic_margin_lower'])<=0:
        raise ValueError('Frozen synthetic regression failed')
    files=[]
    keys=('scalarization','permutation','lindeberg','rank-six','rank6','T12','S4','adjoint','endpoint compatibility','weak-dual','Hadamard')
    for path in sorted((ROOT/'notes').glob('*.md')):
        content=path.read_bytes();text=content.decode('utf-8-sig',errors='replace')
        hits=[k for k in keys if k.lower() in text.lower()]
        if hits:
            files.append({'path':path.relative_to(ROOT).as_posix(),
                          'sha256':hashlib.sha256(content).hexdigest(),'search_hits':hits})
    report={'schema':'wp84-reference-grouped-mehler-v1','parent_commit':'d702810f6b165f2d9a1e11392d6462df940b9b37',
            'frozen_witnesses':witnesses,'witnesses':witnesses,'all_n_checks':checks,
            'all_witness_benchmark_ledgers':original['benchmark_rows'],
            'exact_algebra':exact_algebra(lower),'Taylor_regression':taylor_tests(),'baseline_obstructions':baseline_obstructions(),
            'conditional_derivative_intervals':intervals,
            'cost_aware_box_optimum_difference':str(robust),
            'cost_aware_retained_rhos':[],
            'cost_aware_witness':{'lower':'0','upper':'I'},
            'initial_payment_upper':str(c0),'box_margin':str(robust_margin),
            'grouped_actual_margin':None,'certified_actual_K_delta_U':None,
            'synthetic_regression_margin':benchmark['synthetic_margin_lower'],
            'source_search_coverage':files,
            'decision':'D: available reference intervals and baseline bounds do not certify the grouped target',
            'consumer_certified':False}
    out=ROOT/'notes/WP84_REFERENCE_MEHLER_MEASUREMENT_CERTIFICATE.json'
    out.write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'algebra':report['exact_algebra'],'Taylor':report['Taylor_regression'],
                      'witness_count':len(checks),'source_search_count':len(files),
                      'box_margin':float(robust_margin),'decision':report['decision']},indent=2))

if __name__=='__main__':
    main()
