# WP84 — exact Gaussian quadrature bridge with mixed-sign-only covariance

Date: 2026-10-05

Status: **NEW EXACT INTERPOLATION — THE HARD SAME-SIGN VARIANCE CHANNEL CAN BE REMOVED BY BRIDGE DESIGN WITHOUT CHANGING EITHER ENDPOINT**

No percentage theorem is claimed here.

This note introduces a different theorem representation from the
permutation-Lindeberg path.

The key freedom is simple: to compare the deterministic endpoint matrices
S and S+P, we may insert **any** random bridge whose noise vanishes at both
endpoints.

Choosing the noise covariance intelligently removes the previously open
same-sign/twisted variance channel.

## 1. Complex positive ordinary-prime branch

For each ordinary prime p let A_p denote its normalized sharp positive branch,
including its scalar coefficient and carrier.

The deterministic Hermitian p block is

    C_p = A_p + A_p^*.

Define the Hermitian quadrature companion

    S_p = i(A_p-A_p^*).

Both have the same block norm scale and the same shift length.

## 2. Exact quadrature cancellation

For every matrix X,

    C_p X C_p

equals

    A_p X A_p
      + A_p X A_p^*
      + A_p^* X A_p
      + A_p^* X A_p^*.

Also

    S_p X S_p

equals

    -A_p X A_p
      + A_p X A_p^*
      + A_p^* X A_p
      - A_p^* X A_p^*.

Therefore

    boxed:
    (1/2)[
      C_p X C_p + S_p X S_p
    ]

      =
      A_p X A_p^*
      + A_p^* X A_p.

The same-sign +/+ and -/- channels cancel **algebraically**.

Only the mixed-sign covariance survives.

## 3. Artificial Gaussian noise

Let g_{p,c},g_{p,s} be independent standard real Gaussians and define

    W
      = (1/sqrt(2))
          sum_{p<=X, p prime}
            [g_{p,c} C_p + g_{p,s} S_p].

Its covariance map is exactly

    boxed:
    V_mix(X)
      := E[W X W]

      = sum_p [
          A_p X A_p^*
          + A_p^* X A_p
        ].

There are:

- no same-sign carrier terms;
- no p^(+/-2iT) variance sums;
- no proper-prime-power variance terms, because the bridge noise was chosen
  to use ordinary primes only.

This is a **choice of interpolation noise**, not an approximation to the
deterministic endpoint operator.

## 4. Exact Gaussian bridge

Let P_full be the entire deterministic retained sharp prime operator,
including all prime powers.

For 0<=t<=1 put

    v(t)=t(1-t),

and define

    H_t
      = S + t P_full + sqrt(v(t)) W.

At the endpoints,

    H_0=S,
    H_1=S+P_full

exactly, because v(0)=v(1)=0.

For nonreal z let

    R_t=(H_t-zI)^(-1),

and

    F(t)=E tau(R_t).

## 5. Exact derivative by Gaussian integration by parts

For 0<t<1,

    dR_t/dt
      = -R_t[
          P_full
          + v'(t)/(2 sqrt(v(t))) W
        ]R_t.

Therefore

    F'(t)
      = -E tau(R_t P_full R_t)
        - v'(t)/(2 sqrt(v))
          E tau(R_t W R_t).

For one Gaussian coefficient,

    partial_{g_j} R_t
      = -sqrt(v) R_t C_j R_t.

Gaussian integration by parts gives

    E[g_j tau(R_t C_j R_t)]
      = -2 sqrt(v)
          E tau(R_t C_j R_t C_j R_t).

Summing over every quadrature noise direction yields

    boxed:
    F'(t)
      =
      - E tau(R_t P_full R_t)

      + v'(t)
        E tau(
          R_t V_mix(R_t) R_t
        ).

For v=t(1-t),

    v'(t)=1-2t.

Hence the deterministic endpoint difference has the exact representation

    boxed:
    m_{S+P_full}(z)-m_S(z)

      =
      int_0^1
        [
          - E tau(R_t P_full R_t)

          + (1-2t)
            E tau(
              R_t V_mix(R_t) R_t
            )
        ] dt.

There is no Taylor expansion and no cubic remainder in this identity.

## 6. Why this is stronger than the old variance split

The old permutation-Lindeberg representation exposed the actual current-block
variance and therefore inherited four channels:

    mixed + mixed + same-sign + same-sign.

The present Gaussian bridge is not required to use that covariance.

Because the noise is artificial and vanishes at the endpoints, we are free to
choose the two Hermitian quadratures C_p,S_p.  Their covariance is exactly the
mixed channel.

Therefore the previously open twisted square-prime object

    V_fast

is **not an obligatory theorem object in this bridge representation**.

The difficulty is not magically solved; it has been moved into the
expectation of the drift and mixed covariance along H_t.  But the explicit
p^(+/-2iT) variance channel has disappeared.

## 7. The bridge stays inside the LRSC/Loewner class

Every realization of W is still a sharp Hermitian sum of the same partial
translations.

Its positive branch simply has complex Gaussian scalar coefficients.

Consequently every sample H_t has the same scalar Loewner representation

    H_t
      = diagonal(Q_t,Q_t')
        + [M_{Im Q_t},J],

for one complex scalar random Dirichlet polynomial Q_t.

Therefore, sample by sample,

    rank[D,H_t] <= 2,

    rank[D,R_t] <= 2,

and for any deterministic current direction B,

    rank[D,BR_t] <= 3.

The rank-three scalar D1/D2 formulas survive unchanged inside the Gaussian
expectation.

## 8. Prime-square measure becomes the only covariance arithmetic

The mixed covariance weights are

    (log p)^2/(a^2 L^2 p),

and their carriers cancel.

Thus the covariance side is matched directly to the source-closed
Chebyshev--Mertens square-prime measure.

No long-shift E2 theorem and no same-sign twisted prime sum is required merely
to define or simplify the Gaussian covariance.

The remaining hard object is the drift

    E tau(R_t P_full R_t),

where P_full retains the actual deterministic arithmetic information.

## 9. Strategic consequence for the F9 record gate

The first record theorem can now be attacked through either:

A. the exact Bernoulli/permutation bridge, which preserves current-base
   exclusion; or

B. this exact Gaussian quadrature bridge, which removes the same-sign
   variance channel and replaces subset combinatorics by a Gaussian scalar
   Dirichlet field.

Route B has the smaller variance algebra.

The next hostile audit should test whether the Gaussian randomization makes
the deterministic drift controllable at the four F9 poles within the
0.0112742976 consumer budget.

See:

    notes/WP84_BR_RANK3_SCALAR_D1.md
    notes/WP84_FOUR_POLE_INEQUALITY_KILL_GATE.md
    notes/WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION.md
