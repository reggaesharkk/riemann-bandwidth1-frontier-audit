#!/usr/bin/env python3
"""
Exact asymptotic scaling of the continuum-law core once the universal
slope is 1 and the rational overlap moments are known.

Inputs already established by wp70_exact_continuum_core.py:
  A = ∫(nu-1) Qbar = 1/96
  B = ∫ Qbar = 1/16

For the public law gmass_law:
  gmass = -l^2(nu-1) - l*c_tilde
and normalization 2/(l*ell1^4), with ell1=l+2 log 2 -1.

Thus
  C_law(l) = -2*A*(l/ell1)^4 - 2*c_tilde*B*l^3/ell1^4
and therefore C_law -> -2A = -1/48.

The c_tilde term is lower order O(1/l): the unidentified constant c*
does not affect the leading asymptotic constant.

This script freezes the exact rational consequence and the exact remaining
tail/error budget for crossing 70%.
"""

from fractions import Fraction as F

A=F(1,96)
B=F(1,16)
C_LIMIT=-2*A
TARGET_R=-F(1,180)

assert C_LIMIT==-F(1,48)

# If R <= C_LIMIT + eps_total, 70% follows from R < -1/180.
EPS_TOTAL_MAX = TARGET_R - C_LIMIT
assert EPS_TOTAL_MAX==F(11,720)

TAIL_115=F(115,10000)
TAIL_111=F(111,10000)

ROOM_AFTER_115=EPS_TOTAL_MAX-TAIL_115
ROOM_AFTER_111=EPS_TOTAL_MAX-TAIL_111

assert ROOM_AFTER_115==F(17,4500)
assert ROOM_AFTER_111==F(47,11250)

# Exact consumer at the two public tail charges, assuming no additional limit error.
def simple_from_R(R):
    Delta=R+F(1,30)
    lam=(F(5,108)+Delta/F(3))/(F(1,3)+F(4,3)*Delta)
    return F(1)-2*lam

S115=simple_from_R(C_LIMIT+TAIL_115)
S111=simple_from_R(C_LIMIT+TAIL_111)

print("A_weighted =",A)
print("B_unweighted =",B)
print("C_core_limit =",C_LIMIT)
print("max_total_positive_error_for_70 =",EPS_TOTAL_MAX,float(EPS_TOTAL_MAX))
print("room_after_tail_0.0115 =",ROOM_AFTER_115,float(ROOM_AFTER_115))
print("room_after_tail_0.0111 =",ROOM_AFTER_111,float(ROOM_AFTER_111))
print("simple_if_tail_0.0115_and_no_other_error =",S115,float(S115))
print("simple_if_tail_0.0111_and_no_other_error =",S111,float(S111))
print("RESULT: EXACT_CORE_LIMIT_AND_70_ERROR_BUDGET_PASS")
