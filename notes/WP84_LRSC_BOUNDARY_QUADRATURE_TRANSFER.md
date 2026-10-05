# WP84 — self-contained endpoint quarantine by finite boundary quadrature

Date: 2026-10-05

Status: **ENDPOINT LOW-RANK + SMALL-NORM QUARANTINE CLOSED WITHOUT DPSS INPUT**

This note replaces the external prolate-eigenvalue theorem in the endpoint
quarantine with a direct finite-rank quadrature construction.

The mechanism was suggested by the rank-one boundary-update structure seen
in the LRSC odd-ring work, but the proof below is self-contained in the
present Fourier-compression setting.

## 1. Restriction matrix

Let

    e_k(x)=L^(-1/2) exp(i 2*pi*k*x/L),
    0<=k<d,

and let

    T_I : C^d -> L2(I)

be Fourier synthesis restricted to an interval I of physical length W.

Then

    Q_I := T_I^* T_I

has entries

    (Q_I)_{kl}
      = (1/L) int_I exp(i 2*pi*(l-k)x/L) dx.

Translation of I changes Q_I only by diagonal unitary conjugation, so take

    I=[-W/2,W/2].

Put

    xi_{kl}=2*pi*(l-k)/L,
    Z := pi*(d-1)W/L.

Because

    d <= LT/(2*pi),

we have

    Z <= TW/2.

## 2. Positive p-node Gauss quadrature gives a rank-p matrix

Let

    x_s in I,
    omega_s>0,
    s=1,...,p,

be the p-node Gauss-Legendre quadrature rule on I.

It is exact for polynomials of degree at most 2p-1 and

    sum_s omega_s = W.

Define the Fourier evaluation vector

    v(x)
      = (1, exp(i2*pi*x/L), ..., exp(i2*pi*(d-1)x/L))^T

and the positive semidefinite matrix

    R_p
      := (1/L) sum_{s=1}^p
           omega_s v(x_s)v(x_s)^*.

Then

    rank(R_p) <= p.

This is the finite continuous analogue of a channel dictionary assembled from
point-evaluation vectors.

## 3. Uniform entrywise quadrature error

Fix k,l and expand

    exp(i xi_{kl} x)

at x=0 through degree 2p-1.

For real x, Taylor's theorem gives the sharp remainder bound

    |R_{2p-1}(x)|
      <= |xi_{kl} x|^(2p)/(2p)!.

On I,

    |xi_{kl}x| <= Z.

Because the quadrature is exact on the Taylor polynomial and has positive
weights summing to W,

    |(Q_I-R_p)_{kl}|
      <= (2W/L) Z^(2p)/(2p)!.

Therefore

    boxed:
    ||Q_I-R_p||op
      <= (2dW/L) Z^(2p)/(2p)!.

Using

    d <= LT/(2*pi),

this becomes

    ||Q_I-R_p||op
      <= (TW/pi) Z^(2p)/(2p)!.

## 4. Explicit exponentially small tail

The elementary factorial inequality

    n! >= (n/e)^n

gives

    Z^(2p)/(2p)!
      <= (eZ/(2p))^(2p).

Choose

    boxed:
    p = ceil(e Z).

Then

    eZ/(2p) <= 1/2,

hence

    boxed:
    epsilon_p
      := ||Q_I-R_p||op
      <= (TW/pi) 4^(-p).

This is exponentially small in the time-bandwidth product TW.

No asymptotic spectral theorem enters.

## 5. Effective boundary rank

Since R_p is positive semidefinite and rank at most p, Weyl's inequality gives

    lambda_{p+1}(Q_I)
      <= epsilon_p.

Let Pi_I be the spectral projection of Q_I onto its top p eigendirections.

Because

    Q_I=T_I^*T_I,

the singular-value identity yields

    boxed:
    ||T_I(I-Pi_I)||op
      <= sqrt(epsilon_p).

The rank fraction is explicit:

    p/d
      <= e*pi*W/L + 1/d.

Thus whenever

    W/L -> 0,

we have

    rank(Pi_I)/d -> 0.

For the endpoint choice

    W=K log L

with fixed K,

    rank(Pi_I)/d
      = O(log L/L)
      = o(1).

## 6. Apply to the common endpoint strips

The ramp endpoint factorization already gives

    E_plus
      = T_left^* K_W T_right

for the two common boundary strips

    I_left=[-L/2,-L/2+W],
    I_right=[L/2-W,L/2].

Each strip has the same concentration spectrum as the centered interval.

Let Pi_left, Pi_right be the p-dimensional projections above and define

    E_main
      = Pi_left E_plus Pi_right.

Then

    rank(E_main) <= p.

Moreover

    ||E_plus-E_main||op
      <= 2 ||K_W||op sqrt(epsilon_p).

The real endpoint operator is

    E_endpoint=E_plus+E_plus^*.

Therefore it decomposes as

    boxed:
    E_endpoint
      = E_rank + E_small,

with

    rank(E_rank) <= 2p,

and

    ||E_small||op
      <= 4 ||K_W||op sqrt(epsilon_p).

## 7. The crude prime norm is more than enough

The already established block bound gives

    ||K_W||op
      <= T^(1/2+o(1))

without prime cancellation.

But

    sqrt(epsilon_p)
      <= sqrt(TW/pi) 2^(-p),

while

    p asymp TW.

Thus

    ||E_small||op
      <= T^(1+o(1)) sqrt(W) 2^(-cTW)
      = o(1)

by an overwhelming margin.

At the same time

    rank(E_rank)/d
      <= 2e*pi*W/L + o(1)
      = o(1).

Hence the entire ramp endpoint prime family

    n >= X/L^K

is quarantined at bounded-spectral o(1) cost with:

- no prime cancellation;
- no DPSS theorem;
- no numerical spectral-concentration hypothesis.

## 8. Exact boundary-rank interpretation

For the centered interval define

    Q(a)_{kl}
      = (1/L) int_{-a}^a
          exp(i2*pi(l-k)x/L) dx.

Then

    dQ/da
      = (1/L)
          [v(a)v(a)^* + v(-a)v(-a)^*],

so a moving symmetric boundary is rank at most two at the infinitesimal level.

On the reflection-even cosine sector and reflection-odd sine sector, each
piece is rank one.

This is the exact continuous boundary-update mechanism behind the quadrature
construction.

The continuum of boundary updates has full algebraic span in general; the
finite-rank theorem comes from polynomially accurate quadrature, not from
pretending that the full continuum has exact low rank.

## 9. Why this is stronger than the previous endpoint proof

The earlier DPSS route remains valid as independent corroboration, but it is
no longer required.

The present proof gives a constructive rank bound and a closed error estimate:

    rank <= 2 ceil(e*pi*(d-1)W/L),

    error <=
      4 ||K_W|| sqrt((TW/pi) 4^(-ceil(e*pi*(d-1)W/L))).

Every quantity is explicit.

No unconditional >79 theorem is claimed; this closes only the endpoint
geometry used by the bounded-resolvent route.
