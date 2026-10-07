"""Exact finite algebra for compiled prime-block Mehler Lindeberg transport.
No prime-state average or consumer margin is certified by this verifier.
"""
from fractions import Fraction as F
from pathlib import Path
from itertools import permutations, combinations
import json, hashlib, math
import sympy as s
import wp84_mehler_weak_dual_certificate as dual
import wp84_actual_state_signed_dual_flux as caps
ROOT=Path(__file__).resolve().parents[1]

def zero(x,label):
    if s.simplify(s.expand_complex(x))!=0:raise ValueError(label)

def channel_tests():
    d=3;pi=s.Rational(22,7);D=s.diag(0,1,2)
    J=s.Matrix(d,d,lambda i,j:0 if i==j else 1/(pi*(j-i)))
    K=s.Matrix(d,d,lambda i,j:0 if i==j else s.Rational(1,(i-j)**2))
    X=s.Matrix([[1,s.I,2],[3,2,1],[1,4,-1]])
    Y=s.Matrix([[2,1,3],[s.I,-1,2],[4,1,1]])
    Bs=[]
    for kind in ('a','b'):
        for i in range(d):
            M=s.diag(*[int(k==i) for k in range(d)])
            Bs.append(M*J-J*M if kind=='a' else M)
    C=s.diag(*([s.Rational(1,4)]*d+[0]*d))
    C[d:,d:]=s.eye(d)/6-K/(2*pi*pi)
    direct=sum(C[i,j]*s.trace(Bs[i]*X*Bs[j]*Y)/d for i in range(2*d) for j in range(2*d))
    diag=lambda M:[M[i,i] for i in range(d)]
    dot=lambda a,b:sum(x*y for x,y in zip(a,b))
    aa=(dot(diag(J*X),diag(J*Y))+dot(diag(X*J),diag(Y*J))
        -dot(diag(J*X*J),diag(Y))-dot(diag(X),diag(J*Y*J)))/(4*d)
    bb=dot(diag(X),diag(Y))/(6*d)-sum(X[i,j]*Y[j,i]/(i-j)**2
                         for i in range(d) for j in range(d) if i!=j)/(2*pi*pi*d)
    zero(direct-aa-bb,'two-word resonant covariance')
    CX=D*X-X*D;CY=D*Y-Y*D
    cross=sum(CX[i,j]*CY[j,i]/(i-j)**2 for i in range(d) for j in range(d) if i!=j)
    zero(s.trace(X*Y)-dot(diag(X),diag(Y))+cross,'cross displacement reconstruction')
    gram=sum(s.conjugate(CX[i,j])*CY[i,j]/(i-j)**2
             for i in range(d) for j in range(d) if i!=j)
    off=sum(s.conjugate(X[i,j])*Y[i,j] for i in range(d) for j in range(d) if i!=j)
    zero(gram-off,'mixed K2 Gram cancellation')
    dual.reject(lambda:zero(direct-aa-2*bb,'corrupt covariance factor'))
    return {'arbitrary_nonsymmetric_two_word_covariance':'PASS',
            'cross_displacement':'PASS','mixed_K2_Gram':'PASS',
            'corrupt_covariance_factor':'REJECTED',
            'pi_for_finite_rational_regression':'22/7; analytic formula holds for actual pi'}

def mixed_response_test():
    e=s.symbols('e',real=True)
    A=s.Matrix([[1,s.I],[2,3]]);Ap=s.Matrix([[2,1],[s.I,-1]]);App=s.Matrix([[1,3],[2,s.I]])
    B=s.Matrix([[2,1],[s.I,1]]);Bp=s.Matrix([[3,2],[1,4]]);Bpp=s.Matrix([[s.I,1],[4,2]])
    inner=lambda X,Y:s.re(s.trace(X.conjugate().T*Y))/2
    value=inner(A+e*Ap+e*e*App/2,B+e*Bp+e*e*Bpp/2)
    d1=inner(Ap,B)+inner(A,Bp)
    d2=(inner(App,B)+2*inner(Ap,Bp)+inner(A,Bpp))/2
    zero(s.diff(value,e).subs(e,0)-d1,'noncommuting two-copy first derivative')
    zero(s.diff(value,e,2).subs(e,0)/2-d2,'noncommuting two-copy mixed Hessian')
    dual.reject(lambda:zero(s.diff(value,e,2).subs(e,0)/2-(d2-inner(Ap,Bp)),'dropped cross-copy derivative'))
    return {'first_derivative':'PASS','half_Hessian_with_cross_term':'PASS',
            'dropped_cross_term':'REJECTED','cross_term':str(inner(Ap,Bp))}


def flow_tests(w):
    coeff=list(map(F,w['coefficients']));rho=list(map(F,w['rhos']))
    q0=dual.evaluate(coeff,rho,0)
    a=s.Rational(131,200);c=s.Rational(3142,2415);z=c+s.I*a
    x=s.symbols('x',real=True)
    P=1-s.Rational(43428,13891)*x+s.Rational(37704,13891)*x*x-s.Rational(9660,13891)*x**3
    # Zero-noise realization checks the exact compiled coefficient signs.
    f=(c*c+a*a)**3*P**2/((x-c)**2+a*a)**3
    factor=s.Rational(q0.numerator,q0.denominator)-1
    fun=lambda h:s.cancel(factor*f.subs(x,h))
    df=s.diff(factor*f,x);ddf=s.diff(df,x)
    if df.subs(x,2)==0 or ddf.subs(x,2)==0:raise ValueError('Unexpected universal cancellation')
    blocks=[s.Rational(1,7),s.Rational(-1,11),s.Rational(1,13)];start=s.Rational(1)
    for order in permutations(blocks):
        state=start;tel=0
        for B in order:
            tel+=fun(state+B)-fun(state);state+=B
        zero(tel-fun(start+sum(blocks))+fun(start),'permutation telescope')
    t=s.Rational(2,5);drift=0;complement=0
    for i,B in enumerate(blocks):
        rest=[j for j in range(3) if j!=i]
        for size in range(3):
            for selected in combinations(rest,size):
                probability=t**size*(1-t)**(2-size)
                state=start+sum(blocks[j] for j in selected)
                drift+=probability*df.subs(x,state)*B
    for size in range(4):
        for selected in combinations(range(3),size):
            probability=t**size*(1-t)**(3-size)
            state=start+sum(blocks[j] for j in selected)
            remainder=sum(blocks[j] for j in range(3) if j not in selected)
            complement+=probability*df.subs(x,state)*remainder/(1-t)
    zero(drift-complement,'compiled complement collapse')
    # Formal one-block common-state conversion to quadratic order.
    eps=s.symbols('eps');f1,f2=s.symbols('f1 f2')
    common1=f1*eps+t*f2*eps**2
    common2=f2*eps**2/2
    zero(f1*eps+f2*eps**2/2-common1-(1-2*t)*common2,'Bernoulli skew factor')
    dual.reject(lambda:zero(f1*eps+f2*eps**2/2-common1-common2,'omitted skew factor'))
    return {'all_six_permutations':'PASS','exact_complement_collapse':'PASS',
            'common_state_1_minus_2t':'PASS','corrupt_skew_factor':'REJECTED',
            'q0_minus_1':str(F(q0)-1),'D1_zero_noise_at_2':str(s.cancel(df.subs(x,2))),
            'D2_zero_noise_at_2':str(s.cancel(ddf.subs(x,2)/2)),
            'scope':'exact fixed-realization algebra; no Gaussian or arithmetic measurement value'}

def main():
    cert=json.loads((ROOT/'notes/WP84_MEHLER_WEAK_DUAL_CHAOS_CUTOFF_CERTIFICATE.json').read_text())
    w,u=[x for x in cert['witnesses'] if x['K']==32]
    dual.verify(w);dual.verify(u)
    rows,_=caps.constants();C3=F(rows[2]['C_r_rational_upper'])
    Lambda=sum(abs(F(c)) for c in w['coefficients'])+1
    CF=Lambda*(F(43,20)*C3/3+10*74)
    delta=F(1,100000);c0=F(53503,66000000)
    E=F('7761139416076220170204368647089/1680256283972002400160000000000')
    w0=F(1415,13891);epsilon=F(8711,2778200)
    threshold=E-w0+c0-epsilon
    patterns=['BACKGROUND_SCALARIZATION','PERMUTATION_LINDEBERG_RESOLVENT','F61_FUNCTIONAL_LINDEBERG',
      'BERNOULLI_D1_COMPLEMENT_COLLAPSE','D1_D2_SMALL_CHANNEL_CLOSURE','BR_RANK3_SCALAR_D1',
      'D2_CURRENT_COVARIANCE_CLOSURE','RESONANT_D2_EXPLICIT_FUNCTIONAL','D2_FAST_CHANNEL_VK_CLOSURE',
      'BERNOULLI_COMMON_STATE_GENERATOR','GAUSSIAN_DRIFT_ELIMINATION','SHIFTED_K2_GRAM_CANCELLATION',
      'SHIFTED_THREE_CHANNEL_GRAM','RESONANT_D2_UNIFORM_BV_CLOSURE']
    source=[]
    for name in patterns:
        path=ROOT/'notes'/('WP84_'+name+'.md')
        source.append({'path':path.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    for path in sorted((ROOT/'src').glob('wp84_*.py')):
        if any(k in path.name for k in ('d1_','d2_','rank3','common_state','drift_elimination','shifted_resolvent_wedge','mehler')):
            source.append({'path':path.relative_to(ROOT).as_posix(),'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
    out={'parent':'3e332c1df5d00b588df38cd417f19cc216cb6400','witnesses':[w,u],
      'channel_tests':channel_tests(),'mixed_response_test':mixed_response_test(),'flow_tests':flow_tests(w),'C3_Q_upper':str(C3),
      'dual_absolute_mass':str(Lambda),'uniform_Taylor_cubic_constant':str(CF),
      'initial_payment_upper':str(c0),'exact_required_grouped_limit_lower_threshold':str(threshold),
      'synthetic_regression_margin':next(r['synthetic_margin_lower'] for r in cert['benchmark_rows'] if r['K']==32),
      'state_average_closed':False,'scalar_noisy_start_certified':False,'consumer_certified':False,
      'decision':'C: one augmented Bernoulli/Gaussian state-average resolvent response law remains',
      'source_coverage':source}
    (ROOT/'notes/WP84_COMPILED_MEHLER_PRIME_LINDEBERG_CERTIFICATE.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:out[k] for k in ('channel_tests','flow_tests','uniform_Taylor_cubic_constant','exact_required_grouped_limit_lower_threshold','decision')},indent=2))
if __name__=='__main__':main()
