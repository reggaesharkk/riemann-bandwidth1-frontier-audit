# WP80 — one-sided k=8 gate: exact route past 80%

Date: 2026-10-04
Status: EXACT CONSUMER-SIDE THEOREM; zeta moment transport remains open

## Why this is stronger than the previous k=8 gate

The previous exact gate assumed exact m7 and m8.  The analytic side is more
likely to deliver inequalities than identities.  We therefore recast the
consumer in one-sided form.

Assume a nonnegative measure on [0,infinity) with the exact moments

m0=1, m1=1, m2=4/3, m3=2, m4=13/4,
m5=101/18, m6=12809/1260,

and only

m7 >= L,
m8 <= U.

Put

L0 = 25866469/1352400 = 19.126345016267...

from the exact shifted-Hankel moment-cone floor.

## Feasibility floor

Positivity of the order-4 moment matrix forces

m8 >= F8(m7),

where

F8(x) =
(13335840000 x^2 - 504286322400 x + 4794396454037) / 748818000.

For x >= L0 this function is increasing because

F8'(x) = 2(25200x-476461)/1415 > 0.

Hence m7 >= L implies

U >= m8 >= F8(m7) >= F8(L).

## Sign-safe surrogate Christoffel polynomial

Build the degree-4 Christoffel minimizer using the surrogate moments
(m7,m8)=(L,U).  Its square P(x)=Q(x)^2 has coefficients y7,y8.

The highest polynomial coefficients have the exact sign structure

q4 = 945(1352400L-25866469)/D > 0,

q3 = 1470(3393360L-869400U-32718563)/D,

with D>0 in the feasible region.

Moreover

F8(L) - (3393360L-32718563)/869400
=
((25200L-476461)(1352400L-25866469))/1913646000
>= 0.

Since U >= F8(L), q3 <= 0. Therefore

y7 = 2 q3 q4 <= 0,
y8 = q4^2 > 0.

This is the key one-sided sign gate. It gives

E_actual[P]
<=
E_surrogate[P].

So exact m7 and m8 are unnecessary for consumption: a theorem-grade lower
bound for m7 and upper bound for m8 are enough.

## Strict improvement over 79.627%

The surrogate Christoffel value obeys the same exact factorization

lambda4(L,U) - 1415/13891
=
-27(1352400L-25866469)^2 / (55564 D(L,U)).

Therefore every valid finite U with

L > L0

gives a strict consumer improvement over

11061/13891 = 79.6270966813...%

provided the one-sided moment premises have been analytically transported.

## Exact 80% kill gate

The condition

1 - 2 lambda4(L,U) > 4/5

is equivalent to

U < T80(L),

where

T80(L) =
(18670176000 L^2 - 713649484800 L + 6822174057191) / 68531400.

Thus the theorem-grade target is now only

boxed:
    m7 >= L > L0
    and
    m8 <= U < T80(L).

This is strictly easier than pinning both moments exactly.

For orientation only, at L=19.136 the feasible/80 corridor is

F8(L) = 37.0956753273...
T80(L)= 37.1194109780...

so an upper bound for m8 landing inside that corridor is sufficient.

## Research consequence

The post-79 programme should target one-sided analytic transport:

1. use exact C7 and exact {5,2} to sharpen a rigorous LOWER bound for m7;
2. bound the m8 mixed classes from ABOVE;
3. compare that upper bound directly to T80(L);
4. use the exact square-polynomial certificate above.

This mirrors the successful LRSC K10/K11 proof architecture: a passing witness
and an exclusion/transport certificate are separate objects, with interval
bounds used only where exact algebra ends.

Companion checker:
src/wp80_k8_one_sided_gate.py

## Evidence boundary

This note proves only an exact moment-consumer implication.  It does not prove
that zeta supplies the required m7 lower bound or m8 upper bound.
