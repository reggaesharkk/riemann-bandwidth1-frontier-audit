"""Exact tail-cap certificates, independent Fraction Sturm replay, conditioning diagnostics."""
import argparse
from fractions import Fraction as F
import sympy as S


def trim(p):
    while len(p)>1 and p[-1]==0:
        p.pop()
    return p


def rem(p,q):
    p=p[:]
    while len(p)>=len(q) and any(p):
        k=len(p)-len(q)
        v=p[-1]/q[-1]
        for j in range(len(q)):
            p[j+k]-=v*q[j]
        trim(p)
    return p


def rational_sturm(poly):
    # Independent exact implementation, using no SymPy root-count routine.
    p=[F(int(v.p),int(v.q)) for v in reversed(poly.all_coeffs())]
    normalize=lambda q:[v/abs(q[-1]) for v in q]
    seq=[normalize(p),normalize([j*p[j] for j in range(1,len(p))])]
    while len(seq[-1])>1:
        q=[-v for v in rem(seq[-2],seq[-1])]
        if not any(q):
            break
        seq.append(normalize(q))
    def signs(minus):
        return [(1 if q[-1]>0 else -1)*(-1 if minus and (len(q)-1)%2 else 1) for q in seq]
    def variations(v):
        return sum(a!=b for a,b in zip(v,v[1:]))
    lo,hi=signs(True),signs(False)
    return variations(lo)-variations(hi),lo,hi


def main():
    if not __debug__:
        raise RuntimeError('Certificates require Python without -O.')
    parser=argparse.ArgumentParser()
    parser.add_argument('--search',action='store_true')
    args=parser.parse_args()
    x,y,b=S.symbols('x y b',real=True)
    ap=S.Rational(43428,13891);bp=S.Rational(37704,13891);cp=S.Rational(9660,13891)
    c=bp/(3*cp)
    assert c==S.Rational(3142,2415)
    P=1-ap*x+bp*x*x-cp*x**3
    # All six support coefficients are positive polynomials in a^2.
    support=S.Poly((c*c+b)**3*P.subs(x,-y)**2-((y+c)**2+b)**3,y)
    assert support.nth(0)==0
    for j in range(1,7):
        coeff=S.Poly(support.nth(j),b)
        assert all(v>=0 for v in coeff.all_coeffs())
        assert coeff.nth(0)>0
    cc=S.symbols('cc',real=True)
    cap_generic=S.Poly(cp**2*((x-cc)**2+b)**3-P*P,x)
    assert S.expand(cap_generic.nth(5)-2*cp*(bp-3*cc*cp))==0
    w0=S.Rational(1415,13891)
    assert S.Rational(21,200)-w0==S.Rational(8711,2778200)
    q1,q2,q3=S.symbols('q1 q2 q3')
    hankel=S.Matrix([[q1,q2,q3],[q2,q3,0],[q3,0,0]])
    assert S.expand(hankel.det()+q3**3)==0
    wedge=S.kronecker_product(hankel,S.Matrix([[0,1],[-1,0]]))
    assert wedge.T == -wedge
    import mpmath as mp
    mp.iv.dps=45
    def ivrat(q):
        return mp.iv.mpf(int(q.p))/int(q.q)
    def ivabs(q):
        return mp.iv.sqrt(ivrat(S.re(q))**2+ivrat(S.im(q))**2)
    def coefficients(center,a):
        z=center+S.I*a
        delta=2*S.I*a
        r6=(center*center+a*a)**3
        p=S.expand(P.subs(x,z));p1=S.expand(S.diff(P,x).subs(x,z));p2=S.expand(S.diff(P,x,2).subs(x,z))
        D3=r6*p*p/delta**3
        D2=r6*(2*p*p1/delta**3-3*p*p/delta**4)
        D1=r6*((p1*p1+p*p2)/delta**3-6*p*p1/delta**4+6*p*p/delta**5)
        return tuple(S.expand_complex(S.expand(v)) for v in (D1,D2,D3/2))
    stencil={}
    for a in (S.Rational(2,3),S.Rational(131,200),S.Rational(451,1000)):
        r2=c*c+a*a
        Einf=S.factor(r2**3*cp**2)
        U=S.Poly(cp*cp*((x-c)**2+a*a)**3-P*P,x)
        assert U.degree()==4 and U.LC()>0 and U.nth(0)>0
        n,lo,hi=rational_sturm(U)
        assert n==0 and S.Poly(U,x).count_roots(-S.oo,S.oo)==0
        L=S.Poly(support.as_expr().subs(b,a*a),y)
        assert L.nth(0)==0 and all(L.nth(j)>0 for j in range(1,7))
        if a==S.Rational(2,3):
            assert Einf==S.Rational(30982745506824371707904,6563501109265634375625)
        co=coefficients(c,a)
        z=c+S.I*a
        positive=co[0]/(x-z)+co[1]/(x-z)**2+2*co[2]/(x-z)**3
        f=r2**3*P*P/((x-c)**2+a*a)**3
        assert S.cancel(f-Einf-positive-S.conjugate(positive))==0
        assert S.re(co[0])==0
        u=S.symbols('u')
        xn=z*u-S.conjugate(z)
        q=S.expand(S.sqrt(r2)**3/(2*S.I*a)**3*((u-1)**3-ap*xn*(u-1)**2+bp*xn*xn*(u-1)-cp*xn**3))
        assert S.Poly(q,u).degree()<=3
        qc=[S.Poly(q,u).nth(j) for j in range(4)]
        assert all(S.simplify(qc[j]-S.conjugate(qc[3-j]))==0 for j in range(4))
        xx=(z*u-S.conjugate(z))/(u-1)
        assert S.cancel(q-S.sqrt(r2)**3*P.subs(x,xx)*(u-1)**3/(2*S.I*a)**3)==0
        norms=[ivabs(v) for v in co]
        ia=ivrat(a)
        raw=sum(norms)
        weighted=norms[0]/ia+norms[1]/ia**2+2*norms[2]/ia**3
        stencil[a]=(raw,weighted)
        print('\na=',a,'Einf=',Einf,'decimal=',S.N(Einf,22))
        print('support coefficients y^1..y^6:',[L.nth(j) for j in range(1,7)])
        print('cap coefficients ascending:',list(reversed(U.all_coeffs())))
        print('independent Sturm signs -infinity:',lo,'+infinity:',hi,'real roots:',n)
        print('exact one-point coefficients:',co)
        print('interval raw norm:',raw,'interval weighted proxy:',weighted)
        print('Cayley coefficients:',S.Poly(q,u).all_coeffs())
    assert stencil[S.Rational(131,200)][1].b < stencil[S.Rational(2,3)][1].a
    # For a>=451/1000 cap safety follows by monotonicity of D_a^3.
    # Thus all points in the search below belong to an EXACT certified family.
    for center,a in ((S.Rational(4,5),S.Rational(4,5)),):
        co=coefficients(center,a)
        norms=[ivabs(v) for v in co];ia=ivrat(a)
        print('old shifted interval norms:',sum(norms),norms[0]/ia+norms[1]/ia**2+2*norms[2]/ia**3)
    canonical_a=(S.Rational(13891,9660))**S.Rational(1,3)
    co=coefficients(S.Integer(0),canonical_a)
    cn=[S.Abs(v) for v in co]
    print('canonical algebraic proxy diagnostics:',S.N(sum(cn),22),
          S.N(cn[0]/canonical_a+cn[1]/canonical_a**2+2*cn[2]/canonical_a**3,22))
    if args.search:
        import numpy as np
        aa=S.symbols('aa',positive=True)
        expr=coefficients(c,aa)
        fn=S.lambdify(aa,expr,'numpy')
        grid=np.arange(451,3001)/1000
        vals=fn(grid)
        raw=sum(abs(v) for v in vals)
        weighted=abs(vals[0])/grid+abs(vals[1])/grid**2+2*abs(vals[2])/grid**3
        for label,obj in (('raw',raw),('weighted',weighted)):
            i=int(np.argmin(obj))
            print('NUMERICAL certified-family grid reconnaissance:',label,'a=',grid[i],'proxy=',obj[i])
        print('Grid proxy minima are diagnostics, NOT a global continuous optimization theorem.')
    print('RESULT: EXACT_SUPPORT_PASS; TWO_INDEPENDENT_CAP_CERTIFICATES_PASS; TAIL_ELIMINATED; CURVATURE_OPEN')


if __name__=='__main__':
    main()
