#!/usr/bin/env python3
"""Exact sign witness for the F_61 trace-Hessian kernel.

Only Python's standard-library Fraction is used. The identity
K_f(x,x)=f''(x)/2 shows that opposite signs of f'' at two points rule out
global positivity of the kernel.
"""
from fractions import Fraction as F

A = F(43428, 13891)
B = F(37704, 13891)
C = F(9660, 13891)
DELTA = 61

def f_second(x):
    p = 1 - A*x + B*x*x - C*x**3
    pp = -A + 2*B*x - 3*C*x*x
    ppp = 2*B - 6*C*x
    g = p*p
    gp = 2*p*pp
    gpp = 2*(pp*pp + p*ppp)
    return F(62*DELTA) * (gpp*(g+DELTA) - 2*gp*gp) / (g+DELTA)**3

expected = {
    F(0): F(183349199136, 6394291229),
    F(1): -F(7327100576350070179618547976,
             40792215364263396525173233475),
}
for x, value in expected.items():
    actual = f_second(x)
    assert actual == value, (x, actual, value)
    print(f"x={x}: f''(x)={actual} ({float(actual):.15g})")

assert f_second(F(0)) > 0
assert f_second(F(1)) < 0
print("K_f(x,x)=f''(x)/2 changes sign: GLOBAL_POSITIVITY_FALSIFIED")
