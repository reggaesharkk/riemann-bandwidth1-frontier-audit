# WP84 — exact pole-strip certificate for F61

Date: 2026-10-05

Status: **ALL SIX CONSUMER POLES CERTIFIED OUTSIDE |Im z|<=1**

The bounded consumer

    F_61(x)=62 P(x)^2/(P(x)^2+61)

has six simple nonreal poles.  Numerical root locations suggested that every
pole lies more than unit distance from the real axis.  This can be certified
exactly.

## 1. Elimination

Put

    z=x+i y,
    s=y^2.

A pole satisfies

    Re P(x+i y)=0,
    (Im P(x+i y))^2=61.

For

    P(z)=1-a z+b z^2-c z^3,

with the exact rational coefficients of the Christoffel cubic,

    Re P
      = P(x)+s(-b+3cx),

and

    Im P
      = y[-a+2bx-3cx^2+c s].

Eliminating x gives an exact degree-9 polynomial R(s).

## 2. Exact Sturm gate

The companion script constructs R(s) in exact rational arithmetic and applies
an exact Sturm root count.

Result:

    number of real roots of R(s) in [0,1] = 0.

The denominator P(x)^2+61 has no real roots and is square-free.

Therefore every one of its six roots satisfies

    boxed:
    |Im z_j| > 1.

Numerically the closest pair has

    |Im z_j| ~= 1.076039256....

## 3. Resolvent consequence

At every consumed pole,

    ||(H-z_j I)^(-1)||op < 1

for every Hermitian H.

Hence the one-block cubic remainder at each pole obeys the particularly clean
bound

    |E_{>=3}(z_j)|
      <= sum_n ||B_n||^3
      = O(L^-3).

No contour factor and no small imaginary-part loss appears.

## 4. Why delta=61 is useful

The delta=61 consumer simultaneously has:

- a certified asymptotic simple-zero ledger floor
      0.7929311466... > 0.79;
- six simple poles;
- every pole outside the unit strip;
- a fixed bounded functional calculus.

This makes it a cleaner theorem target than the earlier high-order-pole beta
consumers.

Companion:

    src/wp84_bounded_christoffel_pole_gate.py
