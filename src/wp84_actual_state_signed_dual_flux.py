#!/usr/bin/env python3
"""Exact shell, Malliavin, Mehler and contracted-constant reconnaissance.

No actual-prime dual deficit is certified. No floating acceptance gates.
"""
import argparse
import itertools
import json
import math
from pathlib import Path
import sympy as s
import wp84_cross_repository_hermite_adjoint as old

u=old.u
g=old.g


def fall(n,r):
    return math.prod(range(n-r+1,n+1)) if n>=r else 0


def sqrt_upper(x):
    x=s.cancel(x)
    if not x.is_Rational or x<0:
        raise ValueError('Nonrational radical input')
    n,d=map(int,s.fraction(x)); scale=10**12
    k=math.isqrt(n*scale**2//d)
    if k*k*d<n*scale**2:k+=1
    out=s.Rational(k,scale)
    if out*out<x:raise ValueError('Inward radical bound')
    return out


def constants():
    a=s.Rational(131,200); c=s.Rational(3142,2415)
    z=c+s.I*a; delta=2*s.I*a; w=s.Symbol('w')
    p=[s.Integer(1),-s.Rational(43428,13891),s.Rational(37704,13891),-s.Rational(9660,13891)]
    r6=(c*c+a*a)**3
    q=s.Poly(s.expand(s.sqrt(r6)/delta**3*sum(p[j]*(z*w-s.conjugate(z))**j*(w-1)**(3-j) for j in range(4))),w)
    mags=[sqrt_upper(s.expand_complex(q.nth(j)*s.conjugate(q.nth(j)))) for j in range(1,4)]
    rows=[]
    def bound(r):
        return s.factorial(r)/a**r*sum(mags[j-1]*sum(math.comb(j,l)*math.comb(r-1,l-1)*2**l for l in range(1,min(j,r)+1)) for j in range(1,4))
    for r in range(1,9):
        Cr=bound(r)
        # Constant is an exact upper bound, not a fitted decimal proxy.
        energy=s.Rational(1,2)*s.Rational(5,2)**(r-1)*Cr**2
        candidates=[]
        for K in (16,64,256,1024):
            candidates.append({'K':K,'U1_tail_squared_upper':str(energy/fall(K+1,r))})
        rows.append({'r':r,'C_r_rational_upper':str(Cr),'U1_M_r_upper':str(energy),'U1_contracted_Z_r_upper':str(s.Rational(1,2)*s.Rational(5,2)**(r+1)*bound(r+2)**2),'tails':candidates})
        for k in range(1,4):
            old.zero(s.factorial(r)*math.comb(k+r-1,r)-s.rf(k,r),'ordered resolvent-power coefficient')
    # Pick the sharpest CERTIFIED squared-norm bound at each specified K,U=1.
    best=[]
    for K in (16,64,256,1024):
        vals=[s.Rational(row['U1_M_r_upper'])/fall(K+1,row['r']) for row in rows]
        r=min(range(1,9),key=lambda r:vals[r-1])
        best.append({'K':K,'U':1,'best_r_among_1_to_8_for_norm_tail':r,'squared_upper':str(vals[r-1])})
    old.zero(s.Rational(rows[0]['C_r_rational_upper'])-s.Rational(old.constants()['K1_rational_upper']),'C1 normalization')
    old.zero(s.Rational(rows[1]['C_r_rational_upper'])-s.Rational(old.constants()['K2_rational_upper']),'C2 normalization')
    return rows,best


def exact_malliavin_mehler():
    polys=[1+g[0]**2-g[1]**3+g[0]**4*g[1]**4/7,
           g[0]*g[1]+g[0]**6/9,2-g[1]**8/11]
    indices=old.basis(8); coefficients=old.project(polys,indices)
    masses={n:s.Integer(0) for n in range(9)}
    for j,alpha in enumerate(indices):
        norm=math.prod(math.factorial(t) for t in alpha)
        masses[sum(alpha)]+=norm*(coefficients[j,:]*old.HGRAM*coefficients[j,:].T)[0]
    for r in range(1,9):
        lhs=0
        for q in range(r+1):
            derivative=s.Matrix([s.diff(p,g[0],q,g[1],r-q) for p in polys])
            lhs+=math.comb(r,q)*old.gaussian_average((derivative.T*old.HGRAM*derivative)[0])
        old.zero(lhs-sum(fall(n,r)*mass for n,mass in masses.items()),'ordered Malliavin tensor normalization')
    rho=s.Symbol('rho'); generating=sum(rho**n*mass for n,mass in masses.items())
    gp=s.symbols('gp0:2',real=True)
    def average_four(poly):
        out=0
        for powers,coef in s.Poly(s.expand(poly),*(g+gp)).terms():
            moment=1
            for n in powers:
                if n%2:moment=0;break
                moment*=math.factorial(n)//(2**(n//2)*math.factorial(n//2))
            out+=coef*moment
        return s.simplify(out)
    for t in (s.Rational(0),s.Rational(3,5),s.Rational(1)):
        copy=[p.subs({g[j]:t*g[j]+s.sqrt(1-t*t)*gp[j] for j in range(2)},simultaneous=True) for p in polys]
        joint=average_four((s.Matrix(polys).T*old.HGRAM*s.Matrix(copy))[0])
        old.zero(joint-generating.subs(rho,t),'independent two-copy Mehler identity')
    return {'orders_verified':list(range(1,9)),'Mehler_correlations_verified':['0','3/5','1']}


def separated_shells():
    polys=[1+u*g[0]**2+u**s.Rational(5,2)*g[0]**5/3,
           u**s.Rational(1,2)*g[1]+u*u*g[1]**4/7,
           2-u**s.Rational(3,2)*g[0]**3+u*u*g[0]**2*g[1]**2]
    allidx=old.basis(5); full=old.project(polys,allidx)
    _,N,L,_,_,_=old.chain(allidx)
    old.matrix_zero(2*u*full.diff(u)-(N+L)*full,'odd and even radial chains')
    K=3; low=old.basis(K); rows=[allidx.index(a) for a in low]
    M,_,_,A0,_,S0=old.chain(low); x=full[rows,:]
    phi=old.propagator(low,old.U,u); Y=phi.T*M*phi
    fluxes=[]; rs=[]
    for n in (K+1,K+2):
        upper=[j for j,a in enumerate(allidx) if sum(a)==n]
        r=L.extract(rows,upper)*full[upper,:]/(2*u)
        rs.append(r)
        flux=2*old.integral(old.contract(x,Y,r))
        if flux==0:raise ValueError('Missing nonzero parity boundary witness')
        fluxes.append(str(flux))
    old.matrix_zero(x.diff(u)-A0*x/u-sum(rs,s.zeros(*x.shape)),'ONLY the two shell fluxes')
    dropped=old.expect_rejection(lambda: old.matrix_zero(x.diff(u)-A0*x/u-rs[0],
                                 'dropped K+2 boundary'),'missing parity boundary')
    old.replay(K,allidx,full,L,polys)
    # Exact indefinite initial dual on the normalized scalar levels0,2.
    t=s.Rational(2); b=s.Integer(1)/s.sqrt(2)
    P=s.Matrix([[1,b*(t-1)],[0,t]])
    X=P.T*P-s.eye(2)
    if X.det()!=-s.Rational(1,2):raise ValueError('Indefinite finite dual form lost')
    return {'K':K,'flux_Kplus1':fluxes[0],'flux_Kplus2':fluxes[1],
            'additional_boundary_terms':0,'normalized_level_0_2_X_determinant':'-1/2',
            'mutation_rejected':dropped}


def contracted_word_replay():
    a=s.Rational(131,200);z=s.Rational(3142,2415)+s.I*a
    H=s.Matrix([[0,1],[1,2]])
    R=(H-z*s.eye(2)).inv().applyfunc(lambda x:s.simplify(s.expand_complex(x)))
    B=[s.Matrix([[1,1],[1,0]]),s.Matrix([[0,1],[1,2]])]
    def clean(M):return M.applyfunc(lambda x:s.simplify(s.expand_complex(x)))
    def V(M):return clean(sum((b*M*b for b in B),s.zeros(2)))
    beta=s.Integer(9);kappa=s.trace(V(s.eye(2)))/2
    out=[]
    for r in range(1,4):
        direct=0;tensor=0
        for js in itertools.product(range(2),repeat=r):
            word=R
            for j in js:word=clean(word*B[j]*R)
            direct+=s.trace(clean(word.conjugate().T*word))/2
            derivative=s.zeros(2)
            for perm in itertools.permutations(range(r)):
                w=R
                for q in perm:w=clean(w*B[js[q]]*R)
                derivative+=(-1)**r*w
            derivative=clean(derivative)
            tensor+=s.trace(clean(derivative.conjugate().T*derivative))/2
        nested=clean(R.conjugate().T*R)
        for j in range(r):nested=clean(R.conjugate().T*V(nested)*R)
        old.zero(direct-s.trace(nested)/2,'covariance contraction before norms')
        bound=kappa*beta**(r-1)*a**(-2*(r+1))
        if s.simplify(direct-bound)>0 or s.simplify(tensor-s.factorial(r)**2*bound)>0:
            raise ValueError('Contracted noncommutative word bound failed')
        out.append({'r':r,'CP_nested_identity':'PASS','ordered_Frechet_tensor_bound':'PASS'})
    # Diagonal Loewner directions have zero displacement but growing covariance rank.
    directions=[s.diag(*(int(k==j) for k in range(7))) for j in range(7)]
    operator=s.Matrix.hstack(*(s.Matrix([x for x in d]) for d in directions))
    if operator.rank()!=7:raise ValueError('False six-dimensional covariance reduction')
    return {'orders':out,'rank_zero_displacement_covariance_output_rank':7,
            'scope':'exact finite structural regressions, not an actual-prime asymptotic bound'}


def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path);args=ap.parse_args()
    rows,best=constants()
    out={'schema':'wp84-actual-state-signed-dual-flux-v1','starting_commit':'68ced0e1d8e9efd9ff5423cb28044385be13aa21',
         'normalization':'standard real Gaussians; tau=tr/d; ordered Malliavin tensors',
         'constants_scope':'full-sharp a_phi=1, eventually kappa<=1/2 and beta<=5/2; other normalizations require explicit rescaling',
         'malliavin_mehler':exact_malliavin_mehler(),'shells':separated_shells(),
         'noncommutative_covariance_replay':contracted_word_replay(),
         'contracted_constants':rows,'certified_norm_tail_order_comparison':best,
         'cushion':str(old.CUSHION),'consumer_certified':False,'certified_flux_tuple':None,
         'initial_layer_only_example':{'delta':'1/100000','K':16,'cost_upper':'28047/34000000','remaining_budget':str(old.CUSHION-s.Rational(28047,34000000)),'scope':'No bulk flux or interior certificate'},
         'decision':'C: joint dual-projected covariance-contracted Malliavin deficit bound remains OPEN',
         'warning':'Norm-tail order comparisons do not bound the backward-dual flux or certify the initial dual form'}
    text=json.dumps(out,indent=2,sort_keys=True)+'\n'
    if args.output:args.output.write_text(text,encoding='utf-8')
    print(text,end='')


if __name__=='__main__':main()
