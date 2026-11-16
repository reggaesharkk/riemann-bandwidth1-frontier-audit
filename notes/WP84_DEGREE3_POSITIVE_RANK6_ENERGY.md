# WP84 — exact positive rank-six energy for the degree-3 one-Cayley first strike

Date: 2026-10-05

Status: **EXACT FEJER-RIESZ / GRAM REDUCTION; THE REMAINING DEGREE-3 CAYLEY MAJORANT IS ONE POSITIVE ENERGY WITH DISPLACEMENT RANK AT MOST SIX**

No unconditional zero-density percentage is claimed here.

The conditioned first-strike note reduced the post-band arithmetic theorem to

    tau p_3(U_R),

where

    U_R=(H_R+iI)(H_R-iI)^(-1)

is unitary and

    p_3(e^{i theta})
      =
      1.6895
      +0.2101 cos(theta)
      -2.2720 sin(theta)
      -0.6312 cos(2theta)
      -0.3306 sin(2theta)
      -0.1525 cos(3theta)
      +0.0439 sin(3theta).

The exact global majorant proof already implies

    p_3(e^{i theta})>0

for every theta.

This note uses that positivity instead of treating the three Cayley moments
separately.

## 1. Exact complex Fourier coefficients

Write

    p_3(u)
      =
      a_0
      + sum_{k=1}^3
          [
            c_k u^k
            + conjugate(c_k) u^(-k)
          ],

for |u|=1.

The exact coefficients are

    a_0 = 3379/2000,

    c_1
      = 2101/20000
        + (284/250)i,

    c_2
      = -789/2500
        + (1653/10000)i,

    c_3
      = -61/800
        - (439/20000)i.

## 2. Independent exact rational Gram certificate

Let

    v(u)=(1,u,u^2,u^3)^T.

Define the exact Hermitian rational matrix

    G =

      [ 33/100,
        7/500 + 509i/1000,
        -229/1000 + 91i/1000,
        -61/800 - 439i/20000 ]

      [ conjugate,
        859/1000,
        41/500 + 239i/500,
        -433/5000 + 743i/10000 ]

      [ conjugate,
        conjugate,
        421/1000,
        181/20000 + 149i/1000 ]

      [ conjugate,
        conjugate,
        conjugate,
        159/2000 ].

The sums along its superdiagonals are exactly

    sum_i G_{ii}=a_0,

    sum_i G_{i,i+k}=c_k,
    k=1,2,3.

Hence exactly on the unit circle,

    boxed:
    p_3(u)=v(u)^* G v(u).

The leading principal minors are

    Delta_1 = 33/100,

    Delta_2 = 24193/1000000,

    Delta_3 = 127207/1000000000,

    Delta_4 = 36360049/400000000000000.

All are strictly positive.

By Sylvester's criterion,

    boxed:
    G>0.

So p_3 positivity has a second completely rational exact certificate,
independent of the earlier Sturm proof.

## 3. One degree-3 spectral factor

Because p_3 is a strictly positive trigonometric polynomial of degree three,
the Fejer--Riesz theorem gives a polynomial

    q(u)
      =
      q_0+q_1u+q_2u^2+q_3u^3

such that

    boxed:
    p_3(e^{i theta})
      =
      |q(e^{i theta})|^2.

One numerical choice, included only for reproducibility, is

    q_0
      ~= -0.111279833433495
          +0.032033997952331 i,

    q_1
      ~= -0.422627371593675
          -0.074630488297440 i,

    q_2
      ~= -0.056863359037240
          -1.009535291195556 i,

    q_3
      ~= 0.685209508743288.

The theorem uses the exact Fejer--Riesz factor, not these rounded decimals.

## 4. Positive matrix energy

Functional calculus gives

    boxed:
    p_3(U_R)
      =
      q(U_R)^* q(U_R).

Put

    Q_R=q(U_R).

Then the entire post-band theorem target is

    boxed:
    tau p_3(U_R)
      =
      tau(Q_R^*Q_R).

Thus the remaining arithmetic object is positive.

There is no cancellation between three separately estimated Cayley moments.

## 5. Exact displacement-energy decomposition

Let

    D=diag(0,1,...,d-1),

and

    C_Q=[D,Q_R].

For i!=j,

    (Q_R)_{ij}
      =
      (C_Q)_{ij}/(i-j).

Therefore exactly

    boxed:

    tau(Q_R^*Q_R)

      =
      (1/d)
      sum_i
        |(Q_R)_{ii}|^2

      +
      (1/d)
      sum_{i!=j}
        |(C_Q)_{ij}|^2/(i-j)^2.

Both pieces are nonnegative.

So the first-strike theorem is now one positive diagonal energy plus one
positive squared-Cauchy displacement energy.

## 6. Displacement rank is at most six

Let

    C=[D,U_R].

The sharp fixed-pole Loewner law gives

    rank C<=2.

For

    q(U)
      =
      q_0 I+q_1U+q_2U^2+q_3U^3,

the commutator is

    [D,q(U)]

      =
      C
        (q_1 I+q_2U+q_3U^2)

      + U C
        (q_2 I+q_3U)

      + U^2 C q_3.

Each displayed term has rank at most two.

Hence

    boxed:
    rank[D,Q_R]<=6.

This is sharper than summing the separate bounds for
[D,U], [D,U^2], [D,U^3].

If

    C=G_0 H_0^*

is any rank-two factorization, an explicit rank-six factorization is

    G_Q
      =
      [ G_0, U G_0, U^2 G_0 ],

and

    H_Q^*
      =
      [
        H_0^*
          (q_1 I+q_2U+q_3U^2);

        H_0^*
          (q_2 I+q_3U);

        q_3 H_0^*
      ].

Thus the Google-suggested "rank-six boundary" is now an exact algebraic
object rather than three separate rank bounds.

## 7. One-dimensional 6x6 channel

With

    S_2(t)
      =
      pi^2/3-pi t+t^2/2,

the off-diagonal energy has the exact Fourier representation

    boxed:

    sum_{i!=j}
      |(C_Q)_{ij}|^2/(i-j)^2

      =
      (1/(2pi))
      int_0^(2pi)
        S_2(t)
        tr(
          C_Q e^(itD)
          C_Q^* e^(-itD)
        )
      dt.

Using the rank-six factorization above, the d-dimensional trace reduces to
matrices of size at most

    boxed:
    6 x 6.

So after band truncation the remaining theorem state is:

    one positive diagonal energy
      +
    one one-dimensional rank-six Fourier energy.

## 8. Record inequality

For the conditioned degree-3 majorant,

    E_model p_3(U)
      =
      0.13697308812816694...,

while the conservative record ceiling before band charge is

    0.163249981456072....

At R=256 the two-pole full-to-band charge is approximately

    0.00862476586,

leaving the finite-band target

    boxed:

    limsup_T tau(Q_{T,R}^*Q_{T,R})
      <
      0.15462521560...

with model benchmark

    0.13697308813....

The remaining positive-energy margin is therefore about

    boxed:
    0.01765212747.

## 9. Why this is preferable to three separate moment estimates

Estimating

    tau(U), tau(U^2), tau(U^3)

individually permits large artificial cancellations in the error budget.

The Fejer--Riesz form instead asks directly for the one quantity that the
minorant consumes:

    tau(Q^*Q).

Its decomposition is positive and its displacement state has rank at most
six.

So the preferred next arithmetic task is:

> estimate the diagonal and rank-six K2 energies together, preserving their
> positivity, rather than proving three independent Cayley moment limits.

## 10. Evidence boundary

Closed here:

- exact rational positive Gram certificate;
- exact Fejer--Riesz existence of one degree-3 factor;
- exact positive-energy identity;
- exact rank-six displacement factorization;
- exact 6x6 Fourier-channel reduction.

Still open:

- the actual zeta-side finite-band arithmetic bound
      tau(Q^*Q)<0.15462521560...
  for one convenient fixed R such as 256.

No unconditional record theorem is claimed.

See:

    notes/WP84_CONDITIONED_DEGREE3_CAYLEY_MAJORANT.md
    notes/WP84_TWO_POLE_POSITIVE_DISPLACEMENT_ENERGY.md
    notes/WP84_R2_RESOLVENT_TAIL_O1_OVER_R.md
