#!/usr/bin/env python3
"""
Exact rational polytope audit of the continuum-core leading constant.

Goal
----
Evaluate exactly the l -> infinity leading geometry of the public one-sided
fourth-moment continuum core.  After scaling u_i = l * beta_i and writing
nu in [1,2], beta_1,beta_2 in [nu-1,nu/2], each overlap term is

    vol(p,q,r) = max(1 - (max(0,p,q,r)-min(0,p,q,r)), 0).

The continuum constant is

    C_core = -2 * integral_{nu=1}^2 (nu-1)
                       integral integral qbar(nu,b1,b2) db1 db2 dnu,

where qbar is the sum of the 12 oriented overlap terms.

For one overlap term, introduce s with
    0 <= s <= 1 - span(0,p,q,r).
Then its contribution to the weighted integral is the exact first moment
    integral_P (nu-1) dnu db1 db2 ds
of a rational 4D polytope P.

This checker:
  * enumerates every vertex by exact Fraction Gaussian elimination;
  * verifies every vertex against every halfspace exactly;
  * uses Qhull only for boundary triangulation topology;
  * recomputes every 4-simplex volume and affine moment with Fraction;
  * cross-checks Qhull's floating volume against the exact rational volume.

The final arithmetic is exact over Q.  SciPy/Qhull is not trusted for any
numerical inequality or determinant, only for combinatorial triangulation.
"""

from __future__ import annotations

from fractions import Fraction as F
from itertools import combinations
from math import factorial
import numpy as np
from scipy.spatial import ConvexHull

# affine form c + n*nu + a*b1 + b*b2
ZERO = (F(0), F(0), F(0), F(0))
NU   = (F(0), F(1), F(0), F(0))
B1   = (F(0), F(0), F(1), F(0))
B2   = (F(0), F(0), F(0), F(1))

def add(x,y): return tuple(x[i]+y[i] for i in range(4))
def neg(x): return tuple(-v for v in x)
def sub(x,y): return add(x,neg(y))

NMB1 = sub(NU,B1)
NMB2 = sub(NU,B2)

def oriented_overlap_terms():
    out=[]
    for u1,u3 in ((B1,NMB1),(NMB1,B1)):
        for u2,u4 in ((B2,NMB2),(NMB2,B2)):
            out.append((neg(u1), sub(u3,u4), neg(u4)))
            out.append((sub(sub(u2,u3),u4), neg(add(u3,u4)), neg(u4)))
            out.append((add(sub(neg(u2),u3),u4), add(neg(u3),u4), u4))
    assert len(out)==12
    return out

TERMS=oriented_overlap_terms()

def constraints(args):
    # Variables z=(nu,b1,b2,s), all inequalities c.z <= rhs.
    cons=[
        ((F(-1),F(0),F(0),F(0)), F(-1)), # nu >= 1
        ((F( 1),F(0),F(0),F(0)), F( 2)), # nu <= 2
        ((F( 1),F(-1),F(0),F(0)),F( 1)), # b1 >= nu-1
        ((F(-1),F( 2),F(0),F(0)),F( 0)), # b1 <= nu/2
        ((F( 1),F(0),F(-1),F(0)),F( 1)), # b2 >= nu-1
        ((F(-1),F(0),F( 2),F(0)),F( 0)), # b2 <= nu/2
        ((F(0),F(0),F(0),F(-1)),F(0)),   # s >= 0
    ]
    L=(ZERO,)+tuple(args)
    # s <= 1 - (L_i-L_j) for every pair, equivalent to
    # s <= 1 - span(L_0,...,L_3).
    for li in L:
        for lj in L:
            d=sub(li,lj)
            cons.append(((d[1],d[2],d[3],F(1)),F(1)-d[0]))
    # stable de-duplication
    uniq=[]
    seen=set()
    for item in cons:
        if item not in seen:
            seen.add(item); uniq.append(item)
    return uniq

def solve4(rows,rhs):
    M=[list(r)+[b] for r,b in zip(rows,rhs)]
    n=4
    r=0
    piv=[]
    for c in range(n):
        p=next((i for i in range(r,n) if M[i][c]),None)
        if p is None: continue
        M[r],M[p]=M[p],M[r]
        pv=M[r][c]
        M[r]=[x/pv for x in M[r]]
        for i in range(n):
            if i!=r and M[i][c]:
                f=M[i][c]
                M[i]=[M[i][j]-f*M[r][j] for j in range(n+1)]
        piv.append(c)
        r+=1
        if r==n: break
    if r<n: return None
    z=[F(0)]*n
    for i,c in enumerate(piv):
        z[c]=M[i][-1]
    return tuple(z)

def dot(c,z):
    return sum((ci*zi for ci,zi in zip(c,z)),F(0))

def exact_vertices(args):
    cons=constraints(args)
    verts=set()
    for idx in combinations(range(len(cons)),4):
        rows=[cons[i][0] for i in idx]
        rhs=[cons[i][1] for i in idx]
        z=solve4(rows,rhs)
        if z is None:
            continue
        if all(dot(c,z)<=r for c,r in cons):
            verts.add(z)
    # Every returned vertex is rechecked exactly.
    for z in verts:
        assert all(dot(c,z)<=r for c,r in cons)
    return cons,tuple(sorted(verts))

def det_exact(mat):
    M=[list(r) for r in mat]
    det=F(1)
    n=len(M)
    for c in range(n):
        p=next((i for i in range(c,n) if M[i][c]),None)
        if p is None:
            return F(0)
        if p!=c:
            M[c],M[p]=M[p],M[c]
            det=-det
        pv=M[c][c]
        det*=pv
        for j in range(c,n):
            M[c][j]/=pv
        for i in range(c+1,n):
            if M[i][c]:
                f=M[i][c]
                for j in range(c,n):
                    M[i][j]-=f*M[c][j]
    return det

def affine_rank(verts):
    if len(verts)<=1:
        return 0
    arr=np.array([[float(x-y) for x,y in zip(v,verts[0])] for v in verts[1:]])
    return int(np.linalg.matrix_rank(arr,tol=1e-11))

def simplex_volume_moment(v5):
    base=v5[0]
    vecs=[[v5[i][k]-base[k] for k in range(4)] for i in range(1,5)]
    vol=abs(det_exact(vecs))/F(factorial(4))
    mean_nminus1=sum((v[0]-1 for v in v5),F(0))/5
    return vol,vol*mean_nminus1

def polytope_volume_moment(verts):
    if affine_rank(verts)<4:
        return F(0),F(0),0
    if len(verts)==5:
        V,M=simplex_volume_moment(verts)
        return V,M,1

    arr=np.array([[float(x) for x in v] for v in verts],dtype=float)
    hull=ConvexHull(arr)
    center=tuple(sum((v[k] for v in verts),F(0))/len(verts) for k in range(4))
    V=M=F(0)
    pieces=0
    for facet in hull.simplices:
        fv=[verts[int(i)] for i in facet]
        v,m=simplex_volume_moment((center,*fv))
        if v:
            V+=v; M+=m; pieces+=1

    # Independent floating topology/volume cross-check only.
    assert abs(float(V)-float(hull.volume)) < 1e-12
    return V,M,pieces

EXPECTED_MOMENTS=(
    F(1,480), F(0), F(1,17280),
    F(1,480), F(1,17280), F(0),
    F(1,480), F(1,8640), F(1,1152),
    F(1,480), F(1,1152), F(1,8640),
)

def main():
    totalV=F(0)
    totalM=F(0)
    rows=[]
    for i,args in enumerate(TERMS):
        cons,verts=exact_vertices(args)
        V,M,pieces=polytope_volume_moment(verts)
        assert M==EXPECTED_MOMENTS[i], (i,M,EXPECTED_MOMENTS[i])
        totalV+=V
        totalM+=M
        rows.append((i,len(cons),len(verts),pieces,V,M))
        print(f"term={i:02d} constraints={len(cons):2d} vertices={len(verts):2d} "
              f"simplices={pieces:2d} volume={V} weighted_moment={M}")

    assert totalV==F(1,16)
    assert totalM==F(1,96)

    Ccore=-2*totalM
    assert Ccore==-F(1,48)

    # One-sided assembly using the already public conservative tail charge.
    tail=F(111,10000)
    Rbar=Ccore+tail
    Delta=Rbar+F(1,30)
    lam2=(F(5,108)+Delta/F(3))/(F(1,3)+F(4,3)*Delta)
    simple=F(1)-2*lam2
    distinct=F(1)-lam2

    assert Rbar==-F(73,7500)
    assert simple==F(1082,1539)
    assert distinct==F(2621,3078)
    assert simple>F(7,10)

    print("total_overlap_4d_volume =",totalV)
    print("total_weighted_moment =",totalM)
    print("C_core_exact =",Ccore)
    print("Rbar_with_tail_0.0111 =",Rbar)
    print("simple_conditional_exact =",simple)
    print("simple_conditional_decimal =",float(simple))
    print("simple_conditional_percent =",float(simple)*100)
    print("distinct_conditional_exact =",distinct)
    print("RESULT: EXACT_CONTINUUM_CORE_MINUS_1_OVER_48_PASS")

if __name__=="__main__":
    main()
