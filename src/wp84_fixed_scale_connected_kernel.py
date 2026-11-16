#!/usr/bin/env python3
"""Exact certificate for the fixed-product-scale balanced connected kernel.

For s in [1,2] and factor splits
    x,s-x,y,s-y in [0,1],
sum the six balanced sign interleavings of the nonclosed connected overlap
amplitude.  The exact identity is

    C_s(x,y)
      = -2(s-1) [min(r_x,r_y)-(s-1)],

where r_x=min(x,s-x), r_y=min(y,s-y).

The checker reduces by the exact symmetries x<->s-x, y<->s-y and x<->y to
    1<=s<=2,  s-1<=x<=y<=s/2,
then proves all overlap branch hyperplanes have fixed sign on that polytope,
and evaluates the symbolic branch expression exactly.
"""
import itertools
import math
from fractions import Fraction as F
import sympy as sp

S,X,Y=sp.symbols("s x y", real=True)

def set_partitions(items):
    if not items:
        yield []
        return
    first,rest=items[0],items[1:]
    for part in set_partitions(rest):
        for i in range(len(part)):
            yield part[:i]+[[first]+part[i]]+part[i+1:]
        yield [[first]]+part

TERMS=[]
for P in set_partitions(list(range(4))):
    m=len(P)
    sign=(-1)**(m-1)
    first=next(i for i,b in enumerate(P) if 0 in b)
    others=[i for i in range(m) if i!=first]
    for perm in itertools.permutations(others):
        order=[first]+list(perm)
        masks=[]
        cur=frozenset()
        for bi in order[:-1]:
            cur=cur|frozenset(P[bi])
            masks.append(tuple(sorted(cur)))
        TERMS.append((sign,tuple(masks)))
assert len(TERMS)==26

def six_interleavings():
    out=[]
    for pos in itertools.combinations(range(4),2):
        P=set(pos)
        ip=iter([0,1]); im=iter([2,3])
        q=[]
        for k in range(4):
            q.append(next(ip) if k in P else next(im))
        out.append(tuple(q))
    assert len(out)==6
    return out
SIX=six_interleavings()

BASE=[X,S-X,-Y,-(S-Y)]

def positions(v,masks=None):
    if masks is None:
        out=[sp.Integer(0)]
        cur=sp.Integer(0)
        for z in v:
            cur=sp.expand(cur+z)
            out.append(cur)
        return out
    out=[sp.Integer(0)]
    for mk in masks:
        out.append(sp.expand(sum(v[j] for j in mk)))
    out.append(sp.expand(sum(v)))
    return out

def primitive_linear(expr):
    p=sp.Poly(sp.expand(expr),S,X,Y)
    coeff=[
        sp.Rational(p.coeff_monomial(1)),
        sp.Rational(p.coeff_monomial(S)),
        sp.Rational(p.coeff_monomial(X)),
        sp.Rational(p.coeff_monomial(Y)),
    ]
    den=1
    for c in coeff:
        den=sp.ilcm(den,c.q)
    z=[int(c*den) for c in coeff]
    g=0
    for a in z:
        g=math.gcd(g,abs(a))
    if g:
        z=[a//g for a in z]
    for a in z:
        if a:
            if a<0:
                z=[-b for b in z]
            break
    return tuple(z)

# Reduced-domain boundary planes a0+a_s s+a_x x+a_y y = 0:
# s=1, s=2, x=s-1, 2x=s, y=x, 2y=s.
BOUND=[
    (-1,1,0,0),
    (-2,1,0,0),
    (1,-1,1,0),
    (0,-1,2,0),
    (0,0,-1,1),
    (0,-1,0,2),
]

def solve3(fs):
    A=sp.Matrix([[f[1],f[2],f[3]] for f in fs])
    b=sp.Matrix([-f[0] for f in fs])
    if A.det()==0:
        return None
    z=A.LUsolve(b)
    return tuple(sp.Rational(q) for q in z)

def inside(pt):
    s,x,y=pt
    return (
        1<=s<=2
        and s-1<=x
        and 2*x<=s
        and x<=y
        and 2*y<=s
    )

def vertices():
    out=set()
    for fs in itertools.combinations(BOUND,3):
        z=solve3(fs)
        if z is not None and inside(z):
            out.add(z)
    return sorted(out)

def eval_lin(h,pt):
    a0,aS,aX,aY=h
    s,x,y=pt
    return F(a0)+F(aS)*F(s)+F(aX)*F(x)+F(aY)*F(y)

def overlap_expr(pos,sample):
    sub={S:sample[0],X:sample[1],Y:sample[2]}
    vals=[sp.Rational(q.subs(sub)) for q in pos]
    hi=max(range(len(vals)),key=lambda i: vals[i])
    lo=min(range(len(vals)),key=lambda i: vals[i])
    spread=vals[hi]-vals[lo]
    if spread>=1:
        return sp.Integer(0)
    return sp.expand(1-(pos[hi]-pos[lo]))

def main():
    verts=vertices()
    assert verts

    # Every possible max/min/cutoff branch wall.
    H=set()
    for perm in SIX:
        v=[BASE[i] for i in perm]
        families=[positions(v)]
        families += [positions(v,mk) for _,mk in TERMS]
        for pos in families:
            for i in range(len(pos)):
                for j in range(i+1,len(pos)):
                    d=sp.expand(pos[i]-pos[j])
                    for c in (-1,0,1):
                        H.add(primitive_linear(d-c))

    H.discard((0,0,0,0))

    # Each branch wall has a fixed weak sign on the reduced polytope.
    # Linear extrema occur at vertices.
    for h in H:
        vals=[eval_lin(h,v) for v in verts]
        assert min(vals)>=0 or max(vals)<=0,(h,vals)

    # Generic exact interior point.
    sample=(sp.Rational(3,2),sp.Rational(3,5),sp.Rational(7,10))
    assert inside(sample)
    for h in H:
        assert eval_lin(h,sample)!=0

    total=sp.Integer(0)
    for perm in SIX:
        v=[BASE[i] for i in perm]
        OA=overlap_expr(positions(v),sample)
        B=sp.Integer(0)
        for sign,masks in TERMS:
            B += sign*overlap_expr(positions(v,masks),sample)
        total += sp.expand(OA*B)

    total=sp.factor(sp.expand(total))
    target=sp.factor(-2*(S-1)*(X-(S-1)))
    assert sp.expand(total-target)==0,(total,target)

    # Reduced-domain form equals the invariant min-kernel formula because
    # r_x=x, r_y=y and x<=y.
    print("reduced vertices =",len(verts))
    print("branch hyperplanes =",len(H))
    print("symbolic reduced kernel =",total)
    print("RESULT: WP84_FIXED_SCALE_CONNECTED_KERNEL_PASS")

if __name__=="__main__":
    main()
