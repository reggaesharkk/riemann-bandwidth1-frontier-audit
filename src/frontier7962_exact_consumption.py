#!/usr/bin/env python3
"""
Independent exact consumption audit of the public 0.7962 certified-candidate
moment sequence.

Imported moment premises:
  m0 = 1
  m1 = 1
  m2 = 4/3
  m3 = 2
  m4 = 13/4
  m5 = 101/18
  m6 = 12809/1260

We solve the degree-3 Christoffel problem exactly over Q for a cubic
P(x)=1+a x+b x^2+c x^3 minimizing E[P(X)^2].  The resulting coefficients
have alternating signs, so for x<=0 every nonconstant term is nonnegative
and P(x)>=1.  Thus P(x)^2 >= 1 on the whole nonpositive half-line, exactly
what the inertia/counting certificate needs.

This is an exact scalar/certificate optimization only.  It does NOT prove the
imported moment asymptotics.
"""

from fractions import Fraction as F
from decimal import Decimal, getcontext

m = [
    F(1,1),
    F(1,1),
    F(4,3),
    F(2,1),
    F(13,4),
    F(101,18),
    F(12809,1260),
]

# Exact minimizer from the normal equations for coefficients [1,a,b,c].
a = -F(43428,13891)
b =  F(37704,13891)
c = -F(9660,13891)

def expectation_square(a,b,c):
    coeff=[F(1),a,b,c]
    s=F(0)
    for i,ci in enumerate(coeff):
        for j,cj in enumerate(coeff):
            s += ci*cj*m[i+j]
    return s

w0 = expectation_square(a,b,c)

assert w0 == F(1415,13891)
simple = F(1)-2*w0
distinct = F(1)-w0

assert simple == F(11061,13891)
assert distinct == F(12476,13891)

# Public rational-root certificate exact value.
w_public = F(
    829278553005924403328783,
    8140995278473611944088783,
)
simple_public = F(1)-2*w_public

assert simple > simple_public

# For x<=0:
#   a*x >= 0 because a<0,
#   b*x^2 >=0 because b>0,
#   c*x^3 >=0 because c<0 and x^3<=0.
# Therefore P(x)>=1 termwise.
assert a < 0 and b > 0 and c < 0

getcontext().prec=100
def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)

print("P(x) = 1 + a x + b x^2 + c x^3")
print("a =", a)
print("b =", b)
print("c =", c)
print("w0 exact =", w0)
print("w0 decimal =", dec(w0))
print("simple exact =", simple)
print("simple decimal =", dec(simple))
print("simple percent =", dec(simple)*100)
print("distinct exact =", distinct)
print("distinct decimal =", dec(distinct))
print("gain over public exact rational-root certificate =", dec(simple-simple_public))
print("RESULT: EXACT_7962_CONSUMPTION_OPTIMIZATION_PASS")
