#!/usr/bin/env python3
from fractions import Fraction as F
from decimal import Decimal, getcontext

# Independent exact scalar replay of the public VeriLoop-E2 q=8 assembly.
# This script intentionally does not import or reproduce third-party verifier code.

q = 8
m = 531
eta = F(1, 1)
B = F(93, 23000)
H = F(672167187145431, 10**15)
R = F(
    1113172768314043426732876281699,
    265625000000000000000000000000,
)

PUBLISHED = F(
    722547711262091300265625000000000,
    1072825050442925667061714615173641,
)

R_AKITIN = F(6734775921119, 10**13)
R_DEVINE = F(673399, 10**6)
THRESHOLD_6735 = F(6735, 10000)

C = (m * H - eta * B * (m - q)) / (m - R)

assert m > R
assert C == PUBLISHED
assert C > THRESHOLD_6735
assert C > R_AKITIN
assert C > R_DEVINE

getcontext().prec = 90

def dec(x: F) -> Decimal:
    return Decimal(x.numerator) / Decimal(x.denominator)

print("q =", q)
print("m =", m)
print("H =", H)
print("B =", B)
print("R =", R)
print("C exact =", C)
print("C decimal =", dec(C))
print("percent =", dec(C) * 100)
print("C - 0.6735 =", dec(C - THRESHOLD_6735))
print("C - Rakitin =", dec(C - R_AKITIN))
print("C - Devine =", dec(C - R_DEVINE))

# Exact first-order leverage of the scalar assembly, holding other inputs fixed.
dC_dH = F(m, 1) / (F(m, 1) - R)
dC_dR = C / (F(m, 1) - R)
dC_dB = -F(m - q, 1) / (F(m, 1) - R)

print("dC/dH =", dec(dC_dH))
print("dC/dR =", dec(dC_dR))
print("dC/dB =", dec(dC_dB))
print("RESULT: EXACT_SCALAR_ASSEMBLY_PASS")
