# WP84 — carrier-2T fast D2 channel is o(1)

Date: 2026-10-05

Status: **FAST / SUM-FREQUENCY D2 CURRENT-PRIME COVARIANCE CLOSED TO o(1) USING A VINOGRADOV--KOROBOV PRIME DIRICHLET-POLYNOMIAL BOUND**

No percentage theorem is claimed here.

The resonant/difference-frequency D2 channel was closed uniformly in

    notes/WP84_RESONANT_D2_UNIFORM_BV_CLOSURE.md.

This note treats the complementary same-sign channel.

After proper-power removal and D2 leave-one-out decoupling, the current block
is one ordinary prime p and is independent of the state resolvent R.

The same-sign covariance carries frequencies

    tau_i+tau_j,

which lie at height comparable with T.

A pointwise Vinogradov--Korobov bound for prime Dirichlet polynomials makes
that entire covariance uniformly o(1).

## 1. Fast covariance entries

For

    y_p=log p,

    c_p=-log p/(a L sqrt p),

the current scalar fields are

    alpha_p(tau)=c_p sin(tau y_p),

    beta_p(tau)=2c_p(1-y_p/L) cos(tau y_p).

Every sum-frequency covariance entry is a linear combination of terms

    H_w(i,j)
      =
      sum_{p<=N}
        (log p)^2/(L^2 p)
        w(log p/L)
        exp(
          +/- i (tau_i+tau_j) log p
        ),

where w is one of the fixed polynomials

    1,
    1-s,
    (1-s)^2,

up to harmless constants and the taper factor a^(-2).

On the active grid,

    2T <= tau_i+tau_j <= 4T+o(T).

So it suffices to bound these twisted prime-square sums uniformly for

    2T <= |t| <= 5T.

## 2. Public pointwise prime-polynomial input

Use Lemma 2.6 of

    "Existence of Smooth Numbers in Short Intervals",
    Quarterly Journal of Mathematics 77 (2026),

which follows from Perron's formula and the Vinogradov--Korobov zero-free
region.

With a global parameter X0 comparable with 5T, put

    sigma0
      =
      A_VK /
      [
        (log X0)^(2/3)
        (log log X0)^(1/3)
      ].

For

    P >=
      exp(
        (log X0)^(2/3)
        (log log X0)^(4/3)
      ),

the lemma gives uniformly for |t|<=X0

    boxed:
    |
      sum_{p~P}
        p^(-1-it)
    |

      <<
      P^(-sigma0)
      + (log X0)^3/(1+|t|).

The same bound holds with the sign of t reversed.

## 3. Split off a negligible small-prime range

Choose a fixed sufficiently large K and set

    log P0
      =
      K
      L^(2/3)
      (log L)^(4/3).

Because log P0=o(L),

    P0 = T^(o(1)).

The normalized square-prime mass below P0 is

    L^(-2)
    sum_{p<=P0}
      (log p)^2/p

      =
      O(
        (log P0/L)^2
      )

      =
      O(
        L^(-2/3)
        (log L)^(8/3)
      )

      = o(1).

Therefore all primes p<P0 may be discarded from D2 at o(1) normalized
square-mass cost.

This does not use oscillation.

## 4. High dyadic blocks have arbitrarily strong logarithmic saving

For P>=P0,

    P^(-sigma0)
      <=
      exp(
        -c K log L
      )
      =
      L^(-cK)

for a fixed c>0 coming from the zero-free-region constant.

Choose K once so large that

    cK>10.

Since |t| is comparable with T,

    (log X0)^3/(1+|t|)
      <<
      L^3/T.

Thus on every high dyadic prime block,

    boxed:
    |
      sum_{p~P}
        p^(-1-it)
    |

      <<
      L^(-10)+L^3/T.

## 5. Restore the log-square and slow polynomial weights

On p in [P,2P],

    (log p)^2
      =
      (log P)^2
      + O(log P),

and

    w(log p/L)
      =
      w(log P/L)
      + O(1/L),

because w is a fixed degree-two polynomial.

The main constant part uses Section 4.

The errors may be estimated absolutely:

    sum_{p~P}
      (log p)/p
      = O(1),

and

    sum_{p~P}
      (log p)^2/p
      = O(log P).

After the L^-2 normalization, summing over O(L) dyadic blocks costs only

    O(L^-1)

from the log-square variation and

    O(L^-1)

from the w variation.

The oscillatory main contributes at most

    O(L)
      [
        L^(-10)+L^3/T
      ]

because (log P)^2/L^2<=1.

Hence

    boxed:
    epsilon_T
      :=
      sup_{i,j}
      |H_w(i,j)|
      =
      o(1)

for each of the three fast covariance weights.

This is uniform over the full d by d Fourier section.

## 6. Entrywise covariance smallness is enough

The fast D2 primitive is quadratic in alpha,beta with the state R fixed.

Expand

    B
      =
      M_beta
      + M_alpha J
      - J M_alpha.

Every quadratic trace term has the form

    d^(-1)
    E tr(
      M_f A M_g B0
    ),

where

    f,g in {alpha,beta},

and A,B0 are products of R and at most one J adjacent to each current field.

For a covariance matrix

    C_fg(i,j)=E[f_i g_j],

the exact contraction is

    d^(-1)
    sum_{i,j}
      C_fg(i,j)
      A_ij
      (B0)_ji.

If

    max_{i,j}|C_fg(i,j)|<=epsilon_T,

then Cauchy--Schwarz gives

    |
      d^(-1)
      sum C_fg A_ij (B0)_ji
    |

      <=
      epsilon_T
      d^(-1)
      ||A||_F ||B0||_F

      <=
      epsilon_T
      ||A||op ||B0||op.

The discrete Hilbert matrix J is a finite compression of the classical
discrete Hilbert transform, so

    ||J||op <= C_J

with an absolute constant.

Also

    ||R||op <= eta^(-1)

at every fixed nonreal pole.

Therefore all nine alpha/beta expansion terms satisfy

    boxed:
    |D2_fast primitive|
      <= C_eta epsilon_T
      = o(1),

uniformly over the actual subset/Bernoulli state.

The z-derivative defining D2 adds one further resolvent factor and only
changes C_eta.

## 7. Consequence

Combining this note with the resonant BV closure gives:

    boxed:
    D2 current-prime arithmetic
      =
      explicit resonant state functional
      + o(1).

The carrier-2T channel is not a surviving theorem obstruction.

This is a stronger conclusion than the earlier
"V-fast remains open" notes.

## 8. What D2 still needs

The **current-prime arithmetic** of D2 is now closed.

The second-order path still contains the Bernoulli-state average of the
explicit resonant functional

    Xi_res(R_t).

That is a nonlinear state-evolution problem, but it no longer contains an
uncontrolled current-prime sum.

The main remaining theorem frontier is therefore:

1. D1 drift / mean-path control;
2. close the Bernoulli state evolution of the bounded four-pole functional
   using the now-explicit D2 resonant generator.

No current-prime E2 theorem and no fast-Hankel theorem remain in D2.

Sources:

- QJM 77 (2026), "Existence of Smooth Numbers in Short Intervals",
  Lemma 2.6.
- The lemma itself is a Vinogradov--Korobov zero-free-region consequence.

See:

    notes/WP84_RESONANT_D2_UNIFORM_BV_CLOSURE.md
    notes/WP84_D2_CURRENT_COVARIANCE_CLOSURE.md
    notes/WP84_SHAPLEY_BERNOULLI_FLOW.md
