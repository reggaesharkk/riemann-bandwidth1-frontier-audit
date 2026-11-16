# WP84 — verification of the repeated-pole constant and symmetry conventions

Date: 2026-10-06

Status: **REPO-LEVEL VERIFICATION; CONSTANT 72 AND THE TRANSPOSE CONVENTION SURVIVE**

No unconditional zero-density percentage is claimed here.

This note records a direct verification of two load-bearing points:

1. the differentiated repeated-pole full-to-band constant;
2. the transpose/adjoint convention in the resonant covariance formulas.

## 1. Sharp state used by the theorem

The sharp retained prime matrix is

    H
      =
      M_beta + [M_alpha,J],

with

    J_ij = 1/[pi(j-i)],
    J_ii = 0,

and alpha,beta real.

Therefore H is real symmetric.

For the displacement truncation,

    H=H_R+Delta,

where H_R keeps 0<|i-j|<=R and

    Delta_ij
      =
      (alpha_i-alpha_j)/[pi(j-i)]

for |i-j|>R, with zero diagonal.

The normalized tail estimates are

    tau(Delta^2)
      <=
      8 q_alpha/(pi^2 R),

and

    ||[D,H_R]||_F^2/d
      <=
      8 R q_alpha/pi^2,

where

    q_alpha=||alpha||_2^2/d.

## 2. Differentiated resolvent identity

Write

    G=(H-zI)^(-1),
    S=(H_R-zI)^(-1),

with |Im z|>=eta.

The second resolvent identity is

    G-S
      =
      -S Delta S
      +S Delta S Delta G.

Differentiating gives exactly

    m_H'-m_R'

      =
      -2 tau(Delta S^3)

      +tau(S^2 Delta S Delta G)

      +tau(S Delta S^2 Delta G)

      +tau(S Delta S Delta G^2).

Thus there is one linear-tail term with coefficient 2 and three
quadratic-tail terms.

## 3. Linear term

For i!=j,

    Delta_ij
      =
      (alpha_i-alpha_j)/[pi(j-i)],

and

    (S^3)_ji
      =
      [D,S^3]_ji/(j-i).

Therefore

    |tau(Delta S^3)|

      <=
      1/(pi d)
      [
        sum_tail
          |alpha_i-alpha_j|^2/(i-j)^2
      ]^(1/2)

      [
        sum_tail
          |[D,S^3]_ji|^2/(i-j)^2
      ]^(1/2).

On the tail,

    1/|i-j|<=1/R.

Also

    [D,S]
      =
      -S[D,H_R]S,

so

    [D,S^3]
      =
      [D,S]S^2
      +S[D,S]S
      +S^2[D,S],

and hence

    ||[D,S^3]||_F
      <=
      3 eta^(-4)
      ||[D,H_R]||_F.

Combining the normalized Frobenius estimates gives

    boxed:

    |tau(Delta S^3)|
      <=
      24 q_alpha/
      (pi^2 eta^4 R).

The differentiated linear contribution is therefore

    boxed:

    48 q_alpha/
    (pi^2 eta^4 R).

## 4. Quadratic terms

For each of the three quadratic terms, cyclicity and
Hilbert--Schmidt Cauchy--Schwarz give

    |tau(S^2 Delta S Delta G)|
      <=
      eta^(-4) tau(Delta^2),

and similarly for the other two terms.

Hence the total quadratic contribution is bounded by

    3 eta^(-4) tau(Delta^2)

      <=
      24 q_alpha/
      (pi^2 eta^4 R).

## 5. Final constant

Adding the linear and quadratic contributions gives

    boxed:

    |m_H'-m_R'|

      <=
      72 q_alpha/
      (pi^2 eta^4 R).

With q_alpha=1/4+o(1),

    boxed:

    |m_H'-m_R'|

      <=
      18/
      (pi^2 eta^4 R)

      +o(R^-1).

The bookkeeping is

    72
      =
      2*24
      +3*8.

## 6. Transpose versus adjoint

Every subset sharp matrix is real symmetric:

    H^T=H.

The Gaussian bridge direction is also real symmetric because

    W
      =
      M_h+[M_a,J],

with a,h real and J real skew-symmetric, so

    [M_a,J]^T=[M_a,J].

Therefore along the bridge,

    H_u^T=H_u,

and for every nonreal z,

    R_u(z)^T=R_u(z).

The analytic D2 primitive is bilinear,

    tau((B R)^2),

rather than a Hilbert--Schmidt energy.

The transpose convention is therefore the correct one for the explicit
resonant covariance contraction.

## 7. One-half derivative identity

For a fixed direction B define

    Xi_B(z)
      =
      tau(BRBR).

Then

    d/dz Xi_B

      =
      tau(BR^2BR)
      +tau(BRBR^2).

By cyclicity both terms equal tau(R^2BRB). Hence

    boxed:

    (1/2) Xi_B'(z)
      =
      tau(RBRBR).

The factor 1/2 follows from trace cyclicity alone.

## 8. Verification status

Closed:

- differentiated second resolvent identity;
- O(R^-1) repeated-pole bound with constant 72;
- real-symmetric transpose convention;
- one-half derivative identity.

Open:

- the final one-sided large-T transport of the bounded positive energy.

See:

    notes/WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION.md
    notes/WP84_DIRECT_MPRIME_TAIL_O1_OVER_R.md
    notes/WP84_RESONANT_D2_EXPLICIT_FUNCTIONAL.md
    notes/WP84_GAUSSIAN_COVARIANCE_HADAMARD.md
