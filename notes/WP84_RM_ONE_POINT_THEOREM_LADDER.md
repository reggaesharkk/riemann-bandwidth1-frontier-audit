# WP84 — one-point repeated-pole theorem ladder

Date: 2026-10-05

Status: **MODEL/CONSUMER HIERARCHY + THEOREM STRATEGY; ONE FIXED SPECTRAL POINT z=i CAN IN PRINCIPLE RECOVER THE FULL 79.627 MODEL FRONTIER**

No unconditional zero-density percentage is claimed here.

The preferred first strike r2 is one member of a much larger bounded
one-point family already present in the model reconnaissance.

For every fixed integer m>=1 define

    boxed:
    r_m(x)
      =
      1
      -
      [
        (x-1)^2/(x^2+1)
      ]^m.

## 1. Support-free bounded minorants

For x<=0,

    (x-1)^2/(x^2+1) >= 1,

so

    r_m(x)<=0.

For x>0,

    0 <= (x-1)^2/(x^2+1) < 1,

hence

    0<r_m(x)<=1.

Therefore for every fixed m,

    boxed:
    1_{x>0} >= r_m(x)

on the whole real line.

Also the ratio lies in [0,2], so

    1-2^m <= r_m(x) <= 1.

Thus every fixed member is bounded and Proposition-R safe.

## 2. Only one conjugate pole pair

The denominator is

    (x^2+1)^m
      =(x-i)^m(x+i)^m.

Therefore r_m has no poles except

    z=+i,
    z=-i,

each of order at most m.

For a Hermitian matrix H,

    tau r_m(H)

is consequently a fixed real linear combination of

    m_H(i),
    m_H'(i),
    ...,
    m_H^(m-1)(i)

and their conjugates.

So every fixed rung consumes only **one upper-half-plane point z=i** plus a
finite number of z derivatives.

## 3. The first two important rungs

The exact model hierarchy already gives:

    m=2:
      model simple ledger
        = 76.67654249886171...%;

    m=3:
      model simple ledger
        = 79.09986512365327...%.

Thus, after the first record crossing with r2, the same one-point architecture
already has a second rung above 79%.

The m=3 consumer needs only

    m(i),
    m'(i),
    m''(i).

## 4. Limit of the model ladder

Let

    w0=1415/13891

be the extremal zero atom in the pinned six-moment Christoffel model.

At every positive node of that extremal measure,

    0 <= (x-1)^2/(x^2+1) < 1,

whereas at x=0 the ratio is exactly 1.

Hence by bounded finite-node convergence,

    integral r_m dnu_model
      -> 1-w0
      = 12476/13891.

The corresponding simple-zero model ledger tends to

    boxed:
    2(1-w0)-1
      =
      11061/13891
      =
      79.62709668...%.

So the full six-moment headline can be approached by **fixed bounded
one-point consumers**.  Six distinct poles are not logically required on
the model side.

## 5. Correct order of limits

This does not require m=m(T).

The theorem schema would be:

1. fix m;
2. prove the bounded r_m comparison as T->infinity;
3. obtain one valid asymptotic coefficient S_m;
4. only after that take the supremum over the already-proved fixed-m
   statements.

This keeps every finite-T consumer bounded and preserves the Proposition-R
firewall.

## 6. One fixed Cauchy circle is enough

Choose any fixed

    0<rho<1,

for example rho=1/2.

The circle

    |z-i|=rho

stays a fixed positive distance from the real line.

If the Gaussian/Loewner state theorem yields a uniform o(1) comparison for
m_H(z) on this one circle, then Cauchy's formula gives, for every fixed k,

    m_H^(k)(i)
      =
      k!/(2 pi i)
      int_{|z-i|=rho}
        m_H(z)/(z-i)^(k+1) dz,

and therefore every fixed r_m consumer follows.

Thus a single fixed-circle theorem could support the entire repeated-pole
ladder.

## 7. Co-moving Gaussian heat flow for every fixed m

Each r_m is bounded and satisfies

    r_m(x)->0
    as |x|->infinity.

Therefore the co-moving Gaussian heat-flow identity from

    WP84_R2_COMOVING_GAUSSIAN_HEAT_FLOW.md

extends verbatim to every fixed m.

For

    Phi_m(u)
      =
      E tau r_m(H_1+sqrt(u)W),

one has the exact finite-d heat equation

    Phi_m'(u)
      =
      1/2
      E sum_j
        D^2[tau r_m(H_1+sqrt(u)W)]
          [E_j,E_j].

At fixed d,

    Phi_m(u)->0

as u->infinity by the same almost-sure invertibility argument.

The theorem-side issue is again a uniform large-u truncation and a one-sided
control of the mixed covariance heat curvature.

## 8. Strategic consequence

The current preferred ladder is:

    r2 at z=i
      -> first record crossing with large margin;

    r3 at z=i
      -> 79.0999% model rung;

    fixed r_m hierarchy
      -> approach 79.62709668% model frontier.

F9 and the six-pole Christoffel family remain independent cross-checks, but
the one-point ladder has strictly simpler spectral geography.

The central analytic problem is therefore even more focused:

> control the Gaussian mixed-covariance heat flow uniformly on one fixed
> circle around z=i.

If that theorem can be made sufficiently quantitative, it can feed every
fixed rung without redesigning the arithmetic transport.

See:

    src/wp84_rm_model_hierarchy.py
    notes/WP84_R2_A1_PREFERRED_RECORD_RUNG.md
    notes/WP84_R2_COMOVING_GAUSSIAN_HEAT_FLOW.md
