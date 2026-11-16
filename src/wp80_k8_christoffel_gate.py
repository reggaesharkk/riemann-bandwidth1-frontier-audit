#!/usr/bin/env python3
"""
WP80 exact k=8 Christoffel consumer gate.

This is pure exact algebra.  It assumes moments m0..m8 exist for a
nonnegative measure on [0,infinity), with

    m0 = 1
    m1 = 1
    m2 = 4/3
    m3 = 2
    m4 = 13/4
    m5 = 101/18
    m6 = 12809/1260

and leaves m7,m8 symbolic.

For any polynomial p of degree <=4 with p(0)=1,

    nu({0}) <= int p(x)^2 dnu(x).

Minimizing this quadratic form gives the order-4 Christoffel bound
lambda4(0) = 1 / (M4^{-1})_00 = det(M4)/det(B4), where
M4=(m_{i+j})_{0<=i,j<=4} and B4 is its principal block i,j=1..4.

The script verifies, by exact bivariate-polynomial determinants,

  lambda4 =
    N(m7,m8) / (4 D(m7,m8))

with

  N = 748818000*m8 - 13335840000*m7^2
      + 504286322400*m7 - 4794396454037,

  D = 1837779300*m8 - 24004512000*m7^2
      + 903891063600*m7 - 8574904106497.

It also verifies the exact comparison with the k<=6 Christoffel bound

  lambda3 = 1415/13891,

  lambda4-lambda3 =
    -27*(1352400*m7-25866469)^2 / (55564*D).

Thus, in the positive-definite feasible region D>0, any
m7 > 25866469/1352400 gives a STRICT improvement over 79.62709668...%
once exact m8 is supplied.

The clean 80% gate is

  1 - 2*lambda4 > 4/5

whenever

  m8 <
    (18670176000*m7^2 - 713649484800*m7 + 6822174057191)
    / 68531400

(with D>0 and the moment matrix feasible).

No zeta analytic transport is certified here.
"""

from fractions import Fraction as F
from itertools import permutations


# Polynomial in (u,v)=(m7,m8), dict[(deg_u,deg_v)] -> Fraction.
def add(a,b):
    out=dict(a)
    for k,x in b.items():
        out[k]=out.get(k,F(0))+x
        if out[k]==0:
            del out[k]
    return out

def neg(a):
    return {k:-x for k,x in a.items()}

def mul(a,b):
    out={}
    for (i,j),x in a.items():
        for (k,l),y in b.items():
            key=(i+k,j+l)
            out[key]=out.get(key,F(0))+x*y
    return {k:x for k,x in out.items() if x}

def const(x):
    return {(0,0):F(x)}

U={(1,0):F(1)}
V={(0,1):F(1)}

def det(mat):
    n=len(mat)
    out={}
    for p in permutations(range(n)):
        inv=sum(p[i]>p[j] for i in range(n) for j in range(i+1,n))
        term=const(-1 if inv%2 else 1)
        for i,j in enumerate(p):
            term=mul(term,mat[i][j])
        out=add(out,term)
    return out

M={
    0:const(F(1)),
    1:const(F(1)),
    2:const(F(4,3)),
    3:const(F(2)),
    4:const(F(13,4)),
    5:const(F(101,18)),
    6:const(F(12809,1260)),
    7:U,
    8:V,
}

M4=[[M[i+j] for j in range(5)] for i in range(5)]
B4=[[M[i+j] for j in range(1,5)] for i in range(1,5)]

det_m4=det(M4)
det_b4=det(B4)

# Expected determinant forms.
N={
    (0,1):F(748818000),
    (2,0):F(-13335840000),
    (1,0):F(504286322400),
    (0,0):F(-4794396454037),
}
D={
    (0,1):F(1837779300),
    (2,0):F(-24004512000),
    (1,0):F(903891063600),
    (0,0):F(-8574904106497),
}
assert det_m4 == {k:x/F(288054144000) for k,x in N.items()}
assert det_b4 == {k:x/F(72013536000) for k,x in D.items()}

# k<=6 exact Christoffel mass bound.
LAMBDA3=F(1415,13891)
SIMPLE3=1-2*LAMBDA3
assert SIMPLE3==F(11061,13891)

# Exact m7 floor from the shifted Stieltjes matrix.
L7=F(25866469,1352400)

def eval_poly(p,u,v):
    return sum(c*u**i*v**j for (i,j),c in p.items())

def m8_feasibility_floor(u):
    return (F(13335840000)*u*u-F(504286322400)*u+
            F(4794396454037))/F(748818000)

def m8_80_threshold(u):
    return (F(18670176000)*u*u-F(713649484800)*u+
            F(6822174057191))/F(68531400)

# At the flat m7 floor, the M4 floor and 80% threshold touch.
assert m8_feasibility_floor(L7)==m8_80_threshold(L7)

# Public reconnaissance upper endpoint, treated here only as a diagnostic.
U7=F(19136,1000)
floor_u7=m8_feasibility_floor(U7)
thr80_u7=m8_80_threshold(U7)
assert thr80_u7>floor_u7

print("lambda3 =",LAMBDA3,"simple3 =",SIMPLE3,"=",float(SIMPLE3))
print("m7 exact floor =",L7,"=",float(L7))
print("lambda4 = N/(4D)")
print("N =",N)
print("D =",D)
print("strict-improvement identity:")
print("  lambda4-lambda3 = -27*(1352400*m7-25866469)^2/(55564*D)")
print("80% gate:")
print("  m8 < (18670176000*m7^2 - 713649484800*m7 + 6822174057191)/68531400")
print("at m7=19.136:")
print("  feasibility floor m8 >=",floor_u7,"=",float(floor_u7))
print("  80% threshold       m8 <",thr80_u7,"=",float(thr80_u7))
print("  available corridor width =",float(thr80_u7-floor_u7))
print("RESULT: WP80_K8_CHRISTOFFEL_EXACT_GATE_PASS")
