# WP84 — repeated-pole consumers are positive finite-rank displacement energies

Date: 2026-10-06

Status: **EXACT FULL-SHARP REDUCTION — EVERY FIXED r_m CONSUMER IS ONE POSITIVE ENERGY WITH DISPLACEMENT RANK AT MOST 2m**

No unconditional zero-density percentage is claimed here.

This note combines the fixed-pole hierarchy with the LRSC-style displacement-channel
mechanism.  It gives a direct full-sharp theorem interface for the bounded consumers

    r_m(x)
      =
      1
      -
      [ (x-1)^2/(x^2+1) ]^m.

The point is that the complete defect is a single positive matrix energy.  No
separate control of m(i),m'(i),..., and no raw high moment are needed.

## 1. Cayley identity

Let

    U
      =
      (H+iI)(H-iI)^(-1),

and

    S
      =
      (U-U^*)/(2i)
      =
      2H/(H^2+I).

For real x,

    1-S(x)
      =
      (x-1)^2/(x^2+1).

Also, because U is unitary,

    (I+iU)^*(I+iU)
      =
      2(I-S).

Define

    boxed:

    Q_m
      =
      2^(-m/2)
      (I+iU)^m.

Since U, U^*, and S are all functions of H, they commute.  Therefore exactly

    boxed:

    Q_m^* Q_m
      =
      (I-S)^m
      =
      [
        (H-I)^2
        (H^2+I)^(-1)
      ]^m.

Hence

    boxed:

    r_m(H)
      =
      I-Q_m^*Q_m,

and

    boxed:

    tau r_m(H)
      =
      1-tau(Q_m^*Q_m).

Thus the bounded r_m theorem is equivalent to one upper bound on a positive
energy.

## 2. Exact displacement rank

For the full sharp Loewner matrix, let

    D=diag(0,1,...,d-1),

and

    C=[D,U].

The sharp Loewner identity gives

    rank C<=2.

Put

    A=I+iU.

The power commutator identity gives

    [D,A^m]
      =
      i
      sum_{k=0}^{m-1}
        A^k C A^(m-1-k).

Therefore

    boxed:

    rank[D,Q_m]
      <=
      2m.

This is a fixed finite rank for every fixed consumer m.

In particular:

    m=3  -> rank <=6,
    m=10 -> rank <=20.

The m=3 route is therefore no larger, at the displacement level, than the
already-developed rank-six one-Cayley first-strike machinery.

## 3. Positive diagonal plus squared-Cauchy energy

Let

    C_m=[D,Q_m].

For i!=j,

    (Q_m)_ij
      =
      (C_m)_ij/(i-j).

Therefore exactly

    boxed:

    tau(Q_m^*Q_m)

      =
      d^(-1)
      sum_i |(Q_m)_ii|^2

      +
      d^(-1)
      sum_{i!=j}
        |(C_m)_ij|^2/(i-j)^2.

Both terms are nonnegative.

If

    C_m=G_m H_m^*

is any rank-r factorization with r<=2m, then the off-diagonal term is a
one-dimensional Fourier channel of size at most 2m:

    sum_{i!=j}
      |(C_m)_ij|^2/(i-j)^2

      =
      (1/(2pi))
      int_0^(2pi)
        S2(theta)
        tr_r[
          A_m(theta)
          A_m(theta)^*
        ]
      dtheta,

where

    S2(theta)
      =
      pi^2/3-pi theta+theta^2/2,

and

    A_m(theta)
      =
      H_m^* e^(i theta D) G_m.

Thus the d-dimensional full-sharp problem collapses to

    one diagonal scalar energy
      +
    one finite-dimensional Fourier channel.

## 4. Exact factorization inherited from the rank-two source

If C=G_2 H_2^*, then an explicit 2m-column factorization is obtained directly
from the commutator sum:

    G_m
      =
      2^(-m/2)
      [
        G_2,
        A G_2,
        ...,
        A^(m-1) G_2
      ],

with block rows

    H_m^*
      =
      i
      [
        H_2^* A^(m-1);
        H_2^* A^(m-2);
        ...;
        H_2^*
      ].

No generic rank decomposition is required.

## 5. First >79 theorem gate: m=3

The exact model reconstruction already gives

    E_model r_3
      =
      0.895499325618266....

Equivalently the model defect energy is

    boxed:

    E_model[Q_3^*Q_3]
      =
      0.104500674381734....

To prove an unconditional simple-zero proportion above 79 percent it is
enough to prove

    boxed:

    limsup_T
      tau(Q_{3,T}^*Q_{3,T})
      <
      0.105.

The available model cushion is therefore about

    boxed:

    4.99325618266e-4.

This is tight, but the state is only rank six and the consumer remains
bounded.

## 6. More robust >79 gate: m=10

The exact model hierarchy gives

    2 E_model[r_10]-1
      =
      0.796270912353962....

Hence

    E_model r_10
      =
      0.898135456176981...,

and the model defect energy is

    boxed:

    E_model[Q_10^*Q_10]
      =
      0.101864543823019....

For the same >79 target it suffices to prove

    boxed:

    limsup_T
      tau(Q_{10,T}^*Q_{10,T})
      <
      0.105.

So m=10 has theorem-side cushion

    boxed:

    0.003135456176981...,

more than six times the m=3 cushion, while the displacement state is still
only rank at most 20.

This gives a concrete conditioning tradeoff:

    m=3:
      6-channel state,
      ~4.99e-4 cushion;

    m=10:
      20-channel state,
      ~3.14e-3 cushion.

## 7. Why this is a useful cross-project transfer

The imported idea is structural only:

    global high-dimensional object
      -> exact low-displacement-rank source
      -> finite channel
      -> preserve the signed/positive energy until the last estimate.

No LRSC numerical constant or theorem is imported into the zeta argument.

The same proof-engineering rule was useful in the Navier–Stokes audit:
do not bound a large unsigned envelope when the exact signed or positive
decomposition is smaller.

Here the payoff is stronger: the entire repeated-pole defect is already one
positive energy.

## 8. Active theorem target

Do not expand Q_m into raw moments.

The preferred full-sharp attack is:

1. retain the exact rank-two sharp Loewner commutator;
2. build the explicit 2m-column source factorization above;
3. treat the diagonal and Fourier-channel energies together;
4. use the already-closed resonant current-prime covariance and Gaussian /
   Bernoulli invariance only at the finite channel level;
5. aim first at the inequality tau(Q_10^*Q_10)<0.105.

A proof of this single inequality yields an unconditional simple-zero
proportion above 79 percent.

Recovering the full 79.62709668... frontier still requires a sharper
fixed-m theorem family or the bounded Christoffel F_delta transport; this note
does not claim that final step.

## Evidence boundary

Closed here:

- exact r_m = I-Q_m^*Q_m identity;
- exact rank[D,Q_m]<=2m;
- explicit inherited 2m-column factorization;
- exact positive diagonal/off-diagonal energy decomposition;
- finite 2m-channel Fourier representation;
- explicit m=3 and m=10 theorem thresholds.

Still open:

- the large-T arithmetic estimate for the actual full sharp prime state.

See:

    notes/WP84_FIXED_POLE_HIERARCHY.md
    notes/WP84_R3_FIXED_POLE_CERTIFICATE.md
    notes/WP84_LRSC_DISPLACEMENT_RANK_CLOSURE.md
    notes/WP84_D1_D2_SMALL_CHANNEL_CLOSURE.md
    notes/WP84_RESONANT_D2_UNIFORM_BV_CLOSURE.md
