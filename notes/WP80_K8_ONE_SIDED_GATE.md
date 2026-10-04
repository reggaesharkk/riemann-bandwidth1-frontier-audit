# WP80 — one-sided k=8 gate: exact route past 80%

Date: 2026-10-04
Status: **EXACT CONSUMER-SIDE THEOREM; zeta moment transport remains open**

Assume a nonnegative measure on ([0,infty)) with exact
(m_0,ldots,m_6) equal to the pinned values, and only one-sided information

[
m_7ge L,qquad m_8le U.
]

Put

[
L_0=rac{25866469}{1352400}=19.126345016267ldots .
]

## Feasibility and sign-safe consumption

Moment positivity forces

[
m_8ge F_8(m_7),
]

where

[
F_8(x)=
rac{13335840000x^2-504286322400x+4794396454037}{748818000}.
]

For (xge L_0), (F_8) is increasing. Thus (m_7ge L) implies

[
Uge m_8ge F_8(m_7)ge F_8(L).
]

Build the degree-4 Christoffel minimizer at the surrogate point ((L,U)).
Its square (P(x)=Q(x)^2) has top coefficients

[
y_7=2q_3q_4le0,qquad y_8=q_4^2>0
]

throughout the feasible one-sided region. Therefore

[
mathbb E_{m actual}P
le
mathbb E_{m surrogate}P.
]

So exact values of (m_7,m_8) are unnecessary: a lower bound for (m_7)
and an upper bound for (m_8) are sufficient.

## Strict improvement over 79.627%

The surrogate Christoffel value satisfies

[
lambda_4(L,U)-rac{1415}{13891}
=
-rac{27(1352400L-25866469)^2}{55564,D(L,U)}.
]

Hence every valid finite (U), with (L>L_0), strictly improves the
conditional k<=6 coefficient (11061/13891), once the moment inequalities
are transported analytically.

## Exact 80% gate

The sufficient-and-exact surrogate condition is

[
U<T_{80}(L),
]

where

[
T_{80}(L)=
rac{
18670176000L^2-713649484800L+6822174057191
}{68531400}.
]

The key new structural factorization is

[
oxed{
T_{80}(L)-F_8(L)
=
rac{(1352400L-25866469)^2}{7183106000}.
}
]

Thus the feasible 80% corridor is not an accidental decimal window. It opens
**quadratically and exactly** as soon as (L) moves above the flat Stieltjes
floor (L_0).

At (L=19.136),

[
F_8(L)=37.095675327302ldots,
]

[
T_{80}(L)=37.119410977975ldots,
]

and therefore

[
oxed{
T_{80}(L)-F_8(L)
=
0.0237356506725ldots .
}
]

A midpoint diagnostic gives a valid surrogate simple-zero coefficient
approximately (0.80359497536), but this is **not** a zeta theorem claim.

## Research consequence

The post-79 analytic target is now one-sided:

1. obtain a theorem-grade (m_7) lower bound (L>L_0);
2. obtain a theorem-grade (m_8) upper bound (U);
3. prove (U<T_{80}(L));
4. consume with the exact square-polynomial certificate.

The exact ({5,2}), (C_7), and m8 mixed-class work should therefore be
organized around lower-bounding (m_7) and upper-bounding (m_8), rather than
forcing exact evaluation when an inequality is enough.

Companion checker: `src/wp80_k8_one_sided_gate.py`.

## Evidence boundary

This note proves an exact moment-consumer implication only. It does not prove
that zeta supplies the required (m_7) lower bound or (m_8) upper bound.
