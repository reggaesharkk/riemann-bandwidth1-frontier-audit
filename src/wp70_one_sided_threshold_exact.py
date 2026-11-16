#!/usr/bin/env python3
"""
Exact threshold for converting the public one-sided fourth-moment route into
a >70% simple-zero bound.

Imported algebra:
    m4 = 197/60 + R
and, when m1=1,m2=4/3,m3=2, the degree-2 certificate gives >70% iff
    m4 < 59/18.

Therefore the exact target is R < -1/180.

If the public continuum-core decomposition is
    R <= C_core_UB + 111/10000,
then >70% follows from
    C_core_UB < -1499/90000.

If C_core_UB = C_core + B_total and C_core=-0.0209 exactly as a
diagnostic center, the certification budget must satisfy
    B_total < 191/45000 = 0.00424444...
"""

from fractions import Fraction as F
from decimal import Decimal, getcontext

M4_BASE = F(197,60)
M4_70 = F(59,18)
R_70 = M4_70 - M4_BASE
TAIL = F(111,10000)
CORE_UB_70 = R_70 - TAIL

assert R_70 == -F(1,180)
assert CORE_UB_70 == -F(1499,90000)

CORE_DIAG_209 = -F(209,10000)
B_ALLOW_209 = CORE_UB_70 - CORE_DIAG_209
assert B_ALLOW_209 == F(191,45000)

CORE_DIAG_208 = -F(208,10000)
B_ALLOW_208 = CORE_UB_70 - CORE_DIAG_208

getcontext().prec=70
def dec(x):
    return Decimal(x.numerator)/Decimal(x.denominator)

print("m4_base_197/60 =", dec(M4_BASE))
print("m4_threshold_for_70_59/18 =", dec(M4_70))
print("required_R_strictly_below =", dec(R_70), "exact", R_70)
print("tail_charge =", dec(TAIL), "exact", TAIL)
print("required_CcoreUB_strictly_below =", dec(CORE_UB_70), "exact", CORE_UB_70)
print("if_Ccore=-0.0209_allowed_Btotal <", dec(B_ALLOW_209), "exact", B_ALLOW_209)
print("if_Ccore=-0.0208_allowed_Btotal <", dec(B_ALLOW_208), "exact", B_ALLOW_208)
print("public_preregistered_B_cap =", Decimal("0.0045"))
print("worst_case_cap_shortfall_at_-0.0209 =", Decimal("0.0045")-dec(B_ALLOW_209))
print("RESULT: EXACT_ONE_SIDED_70_THRESHOLD_PASS")
