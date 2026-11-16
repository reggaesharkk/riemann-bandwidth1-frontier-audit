# WP84 — exact rank-six bounded consumer at 79.5197%

Date: 2026-10-06

Status: **EXACT SUPPORT-FREE BOUNDED >79.5 MODEL CONSUMER; ONE CAYLEY POINT; POSITIVE ENERGY; DISPLACEMENT RANK AT MOST SIX**

No unconditional zero-density percentage is claimed here.

The repeated-pole positive-energy reduction suggests optimizing directly in the
degree-three Cayley class instead of using the special power r_3.

Let

    U=(H+iI)(H-iI)^(-1)

and define the exact Gaussian-rational cubic

    boxed:

    q(u)
      =
      (1/1000)
      [
        419 u^3
        +(-15-1127 i)u^2
        +(-1127+7 i)u
        +(8+419 i)
      ].

Put

    p(x)=|q((x+i)/(x-i))|^2,

and

    h(x)=1-p(x).

The theorem statistic is

    tau h(H)
      =
      1-tau(q(U)^*q(U)).

## 1. Exact support certificate

A direct exact simplification gives

    p(x)-1
      =
      S(x)
      /
      [
        500000 (x^2+1)^3
      ],

where

    S(x)
      =
        1313 x^6
       -3353410 x^5
       +7506675 x^4
       -12370084 x^3
       +7613939 x^2
       -3398722 x
       +1313.

For x=-y<=0,

    boxed:

    S(-y)
      =
        1313 y^6
       +3353410 y^5
       +7506675 y^4
       +12370084 y^3
       +7613939 y^2
       +3398722 y
       +1313
      >
      0.

Therefore

    p(x)>=1
    for every x<=0.

For x>0, p(x)>=0 because it is a modulus square.  Hence globally

    boxed:

    h(x)
      <=
      1_{x>0}.

So every Hermitian H obeys

    boxed:

    n_+(H)/d
      >=
      tau h(H)
      =
      1-tau(q(U)^*q(U)).

No support assumption, raw moment, or spectral gap is used.

## 2. Exact model value

Against the frozen four-node Christoffel extremal model, exact rational
reduction modulo the Christoffel cubic gives

    boxed:

    E_model[p]
      =
      254819740781074726741910188950681
      /
      2488442457874785010845734628500000

      =
      0.10240129924430702....

Thus

    E_model[h]
      =
      0.89759870075569298...,

and the induced model simple-zero coefficient is

    boxed:

    1-2 E_model[p]

      =
      989401488156317778680957125299319
      /
      1244221228937392505422867314250000

      =
      0.795197401511386....

So this exact degree-three bounded consumer has model value

    boxed:

    79.5197401511...%.

This materially improves the special r_3 degree-three consumer

    79.0998651237...%

without increasing the displacement rank.

## 3. Positive rank-six energy

Let

    Q=q(U).

Then

    h(H)=I-Q^*Q,

so the only theorem-side defect is

    boxed:

    E_q(T)=tau(Q^*Q).

For the full sharp Loewner matrix,

    rank[D,U]<=2.

Since q has degree three,

    [D,Q]
      =
      q_1 [D,U]
      +q_2(
          [D,U]U
          +U[D,U]
        )
      +q_3(
          [D,U]U^2
          +U[D,U]U
          +U^2[D,U]
        ),

and therefore

    boxed:

    rank[D,Q]<=6.

Exactly as in the repeated-pole displacement note,

    boxed:

    tau(Q^*Q)
      =
      d^(-1) sum_i |Q_ii|^2
      +
      d^(-1) sum_{i!=j}
        |[D,Q]_ij|^2/(i-j)^2.

The off-diagonal term is a one-dimensional Fourier energy with a channel of
size at most 6.

## 4. Theorem threshold

A simple-zero proportion above 79 percent follows as soon as

    tau h(H)>0.895+o(1),

equivalently

    boxed:

    limsup_T tau(Q_T^*Q_T)
      <
      0.105.

The exact model energy is

    0.10240129924430702...,

so the available full-sharp theorem cushion is

    boxed:

    0.105
      -
    0.10240129924430702...

      =
      0.00259870075569298....

That is more than five times the cushion of the special r_3 consumer while
keeping the same rank-six displacement ceiling.

## 5. Why this is preferable to the current r_3 first >79 gate

Both consumers have:

- one Cayley point z=i;
- degree three;
- a positive energy defect;
- displacement rank at most six;
- Proposition-R safety.

But the present exact cubic has a substantially larger >79 error budget:

    special r_3:
      ~4.993e-4;

    optimized exact cubic:
      ~2.599e-3.

Thus this consumer should replace r_3 as the preferred first direct >79
full-sharp target.

The m=10 repeated-pole consumer still has a slightly larger >79 cushion
(~3.135e-3), but it carries a rank-at-most-20 channel.  The new cubic captures
most of that conditioning gain at rank six.

## 6. Cross-project method transfer

This construction uses two portfolio methods, not cross-domain assumptions:

1. LRSC: optimize the finite channel after proving the rank mechanism, rather
   than optimizing an unrelated scalar surrogate;

2. Physics / verification lineage: convert the support condition to an exact
   coefficient-positivity certificate whenever possible instead of relying on
   a floating minimization plot.

No LRSC, Navier-Stokes, or Physics theorem is imported as a zeta premise.

## 7. Active kill gate

The preferred direct >79 theorem target is now

    boxed:

    limsup_T
      tau[
        q(U_T)^* q(U_T)
      ]
      <
      0.105,

with q fixed exactly as above.

Attack this at the positive-energy level:

    diagonal energy
      +
    rank-six K2 Fourier energy,

preserving cancellations inside the rank-six source factorization before any
absolute-value estimate.

If this closes, the resulting theorem already exceeds 79 percent.  It does
not by itself recover the full 79.62709668... model frontier.

## Evidence boundary

Closed:

- exact global support-free minorant;
- exact coefficient-positive negative-half-line certificate;
- exact rational model evaluation;
- exact 79.5197401511... model coefficient;
- exact positive-energy form;
- exact rank-six displacement ceiling;
- explicit >79 theorem threshold and cushion.

Open:

- the large-T arithmetic bound
      limsup tau(q(U_T)^*q(U_T))<0.105
  for the actual sharp zeta matrix.

See:

    notes/WP84_RM_POSITIVE_DISPLACEMENT_ENERGY.md
    notes/WP84_FIXED_POLE_HIERARCHY.md
    notes/WP84_LRSC_DISPLACEMENT_RANK_CLOSURE.md
    notes/WP84_SINE_SCALAR_K2_WEDGE.md
