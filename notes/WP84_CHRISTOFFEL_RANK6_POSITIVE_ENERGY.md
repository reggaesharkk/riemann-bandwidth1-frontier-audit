# WP84 — Christoffel ladder is a positive rank-six full-sharp energy

Date: 2026-10-06

Status: **EXACT STRUCTURAL REDUCTION — EVERY FIXED BOUNDED CHRISTOFFEL CONSUMER IS ONE POSITIVE FULL-SHARP ENERGY WITH DISPLACEMENT RANK AT MOST SIX, UNIFORMLY IN THE LADDER PARAMETER**

No unconditional zero-density percentage is claimed here.

This note upgrades the bounded Christoffel ladder from a six-simple-pole
linear combination to a single positive finite-channel object.

Let

    P(x)
      =
      1
      -(43428/13891)x
      +(37704/13891)x^2
      -(9660/13891)x^3,

and, for fixed delta>0,

    F_delta(x)
      =
      (delta+1) P(x)^2
      /
      (P(x)^2+delta).

The earlier ladder theorem gives

    F_delta(x)>=1
    for x<=0,

and

    F_delta(x)
      <=
      (1+1/delta) P(x)^2.

Thus F_delta is the bounded negative-side defect whose theorem-side cap is

    (1+1/delta) w0,

with

    w0=1415/13891.

## 1. Exact spectral factor

For Hermitian H put

    A=P(H),

and define

    boxed:

    Q_delta
      =
      sqrt(delta+1)
      A
      (A+i sqrt(delta) I)^(-1).

Since A is Hermitian,

    Q_delta^*
      =
      sqrt(delta+1)
      (A-i sqrt(delta) I)^(-1)
      A.

All factors are functions of A and commute. Therefore

    boxed:

    Q_delta^* Q_delta
      =
      (delta+1)
      A^2
      (A^2+delta I)^(-1)
      =
      F_delta(H).

Hence

    boxed:

    tau F_delta(H)
      =
      tau(Q_delta^*Q_delta).

The entire bounded Christoffel theorem is one positive energy.

Equivalently, with

    R_delta
      =
      (P(H)+i sqrt(delta) I)^(-1),

one has

    boxed:

    Q_delta
      =
      sqrt(delta+1)
      [
        I
        -i sqrt(delta) R_delta
      ].

Thus Q_delta is bounded for every fixed delta and Proposition-R safe.

## 2. Displacement rank is at most six

Let

    D=diag(0,1,...,d-1),

and assume the full sharp Loewner identity

    C=[D,H],

    rank C<=2.

Write

    P(x)=p0+p1 x+p2 x^2+p3 x^3.

Then exactly

    [D,P(H)]

      =
      p1 C

      +p2(
          C H
          +H C
        )

      +p3(
          C H^2
          +H C H
          +H^2 C
        ).

Therefore

    boxed:

    rank[D,P(H)]
      <=6.

Resolvent commutation gives

    [D,R_delta]
      =
      -R_delta
      [D,P(H)]
      R_delta.

Using the affine form of Q_delta,

    boxed:

    [D,Q_delta]

      =
      i sqrt(delta(delta+1))
      R_delta
      [D,P(H)]
      R_delta.

Consequently

    boxed:

    rank[D,Q_delta]
      <=6

for every fixed delta>0.

The channel dimension is independent of delta.

This is the crucial structural improvement over treating F_delta as six
unrelated simple resolvents.

## 3. Explicit six-column source factorization

If

    C=G_2 H_2^*

is any rank-two factorization of [D,H], then [D,P(H)] has the explicit
six-column factorization

    [D,P(H)]
      =
      G_P H_P^*,

with

    G_P
      =
      [
        G_2,
        H G_2,
        H^2 G_2
      ],

and block rows

    H_P^*
      =
      [
        H_2^*
          (p1 I+p2 H+p3 H^2);

        H_2^*
          (p2 I+p3 H);

        p3 H_2^*
      ].

Therefore

    boxed:

    [D,Q_delta]
      =
      G_delta H_delta^*

with

    G_delta
      =
      i sqrt(delta(delta+1))
      R_delta G_P,

and

    H_delta^*
      =
      H_P^* R_delta.

This is an exact inherited boundary-channel factorization.

## 4. Positive diagonal plus rank-six K2 energy

For i!=j,

    (Q_delta)_{ij}
      =
      [D,Q_delta]_{ij}/(i-j).

Hence

    boxed:

    tau F_delta(H)

      =
      d^(-1)
      sum_i
        |(Q_delta)_{ii}|^2

      +
      d^(-1)
      sum_{i!=j}
        |[D,Q_delta]_{ij}|^2/(i-j)^2.

Both terms are nonnegative.

Using

    S2(theta)
      =
      pi^2/3-pi theta+theta^2/2,

the off-diagonal energy is exactly

    boxed:

    (1/(2pi d))
    int_0^(2pi)
      S2(theta)
      tr_6[
        A_delta(theta)
        A_delta(theta)^*
      ]
    dtheta,

where

    A_delta(theta)
      =
      H_delta^*
      e^(i theta D)
      G_delta.

Thus the full d-dimensional theorem has been compressed to

    one diagonal scalar energy
      +
    one one-dimensional channel of size at most 6.

No six-resolvent triangle inequality is required.

## 5. First bounded Christoffel theorem target

At delta=61, the exact universal moment cap is

    boxed:

    (62/61) w0
      =
      87730/847351
      =
      0.1035344267....

Therefore the bounded >79 theorem follows from

    boxed:

    limsup_T
      tau(
        Q_61^* Q_61
      )
      <=
      87730/847351.

This implies the simple-zero coefficient

    boxed:

    671891/847351
      =
      79.29311466...%.

The extremal four-node Christoffel model itself has

    E_model F_delta=w0

for every delta, because P(0)=1 and P vanishes at the three positive
quadrature nodes.

So at delta=61 the exact model-to-theorem-cap cushion is

    boxed:

    w0/61
      =
      1415/(13891*61)
      ~=0.00167008.

## 6. Full 79.62709668... ladder stays rank six

For every fixed delta>=61, the theorem target is

    boxed:

    limsup_T
      tau(
        Q_delta^*Q_delta
      )
      <=
      (1+1/delta) w0.

If this is proved for every fixed delta>=61, the already-closed ladder
argument gives

    liminf simple-zero proportion

      >=
      sup_delta
      [
        1-2(1+1/delta)w0
      ]

      =
      boxed:

      11061/13891
      =
      79.6270966813...%.

The key new fact is that the channel dimension never grows with delta:

    boxed:

    rank[D,Q_delta]<=6
    for the entire ladder.

Thus the full 79.627 frontier is not a six-pole-vs-accuracy tradeoff and not a
rank-20 repeated-pole problem.  It is a parameterized family of the same
rank-six positive-energy geometry.

## 7. Relation to the optimized cubic and r_m routes

The new exact cubic consumer from

    WP84_OPTIMIZED_RANK6_79_CONSUMER

has a larger direct fixed-target cushion than delta=61 and is still the best
single first >79 stress target.

But the Christoffel ladder has the stronger asymptotic architecture:

- optimized cubic:
      one fixed rank-six energy,
      model 79.51974015...%;

- bounded Christoffel delta=61:
      one fixed rank-six energy,
      theorem target 79.29311466...%;

- bounded Christoffel all fixed delta>=61:
      same rank-six channel family,
      headline limit 79.62709668...%.

So the direct cubic remains the first attack, while Q_delta is the route that
can recover the full model headline without increasing channel rank.

## 8. Cross-project mechanism

The useful LRSC transfer is exact:

    prove the boundary/displacement rank first,
    preserve the positive channel,
    and only then estimate the finite-dimensional state.

The useful Navier-Stokes audit transfer is also methodological:

    do not replace a signed/positive exact decomposition with a larger
    absolute envelope unless forced.

No theorem or numerical constant from another research program is imported as
a zeta premise.

## 9. Active kill gate

The preferred sequence is now:

1. finish the R=400 same-normalization replay for the 68.82 first theorem;
2. attack the optimized cubic rank-six energy <0.105 for a direct >79 theorem;
3. transfer the same six-channel estimates to Q_61;
4. parameterize the fixed-delta proof;
5. take the external supremum over fixed delta to recover 79.62709668...%.

The common hard object is no longer a generic resolvent law.  It is a
rank-six positive K2 channel with diagonal energy.

## Evidence boundary

Closed here:

- exact spectral factor F_delta=Q_delta^*Q_delta;
- exact rank[D,Q_delta]<=6;
- explicit six-column inherited factorization;
- exact positive diagonal/off-diagonal decomposition;
- exact one-dimensional rank-six Fourier channel;
- rank-six channel dimension uniform over every fixed delta;
- exact connection to the 79.62709668... bounded ladder.

Still open:

- theorem-grade large-T control of the diagonal plus rank-six channel for the
  actual full sharp zeta matrix.

See:

    notes/WP84_BOUNDED_CHRISTOFFEL_CONSUMER.md
    notes/WP84_BOUNDED_CHRISTOFFEL_LADDER.md
    notes/WP84_OPTIMIZED_RANK6_79_CONSUMER.md
    notes/WP84_LRSC_DISPLACEMENT_RANK_CLOSURE.md
    notes/WP84_SINE_SCALAR_K2_WEDGE.md
