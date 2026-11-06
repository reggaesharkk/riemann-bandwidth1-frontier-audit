#!/usr/bin/env python3
"""
Explicit degree-2 polynomial witness for a >70% simple-critical-zero target.

This is intentionally simpler than recomputing the optimal Christoffel
polynomial after perturbing the moments.  Fix

    P(x) = 1 - 7x/4 + 2x^2/3.

At the sine-kernel moment target
(mu0,mu1,mu2,mu3,mu4)=(1,1,4/3,2,13/4),
E[P(X)^2]=5/36.

For a nonnegative spectral measure, mass at zero <= E[P^2], hence
positive-rank fraction >= 1-E[P^2].  The simple-zero transfer then gives

    simple fraction >= 1 - 2 E[P^2].

If mu3 >= 2-d3 and mu4 <= 13/4+d4, then because the mu3 coefficient is
negative and the mu4 coefficient positive,

    E[P^2] <= 5/36 + (7/3)d3 + (4/9)d4.

Therefore >70% follows from the exact linear budget

    210*d3 + 40*d4 < 1.
"""

from fractions import Fraction as F

a = -F(7,4)
b = F(2,3)

mu0 = F(1)
mu1 = F(1)
mu2 = F(4,3)
mu3 = F(2)
mu4 = F(13,4)

E0 = (
    mu0
    + 2*a*mu1
    + (a*a + 2*b)*mu2
    + 2*a*b*mu3
    + b*b*mu4
)

assert E0 == F(5,36)

def E_upper(d3: F, d4: F) -> F:
    return E0 + F(7,3)*d3 + F(4,9)*d4

def simple_lower(d3: F, d4: F) -> F:
    return F(1) - 2*E_upper(d3,d4)

# Clean theorem target:
# mu3 >= 1.996 = 499/250, mu4 <= 13/4.
d3 = F(1,250)
d4 = F(0)
B = simple_lower(d3,d4)

assert 210*d3 + 40*d4 < 1
assert B == F(1583,2250)
assert B > F(7,10)

print("P(x) = 1 - 7x/4 + 2x^2/3")
print("nominal_E_P2 =", E0)
print("linear_70_budget: 210*d3 + 40*d4 < 1")
print("example_mu3_lower =", F(499,250))
print("example_mu4_upper =", F(13,4))
print("example_simple_lower_exact =", B)
print("example_simple_lower_decimal =", float(B))
print("example_simple_percent =", float(B)*100)
print("RESULT: EXPLICIT_POLYNOMIAL_70_PERCENT_WITNESS_PASS")
