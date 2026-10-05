# WP84 — explicit resonant D2 state functional

Date: 2026-10-05

Status: **RESONANT SECOND-ORDER MAIN COLLAPSED TO FOUR SCALAR RESOLVENT STATISTICS; NO CURRENT-PRIME SUM REMAINS IN THE MAIN TERM**

No percentage theorem is claimed here.

The current-prime D2 primitive is

    tau((B R)^2),

with

    B=M_beta+[M_alpha,J],

and the current block is independent of the state after the D2
leave-one-out reduction.

The resonant current covariance is

    E[alpha alpha^T]
      = c_alpha I,

    c_alpha=1/(4 a^2),

    E[alpha beta^T]=0,

    E[beta beta^T]
      = c_beta I - gamma K2,

where

    c_beta=1/(6a^2),

    gamma=1/(2a^2 pi^2),

and K2 has entries 1/(i-j)^2 off the diagonal and zero diagonal.

This note performs the covariance contraction completely.

## 1. beta-beta contribution

Because R is symmetric under transpose,

    tr(M_beta R M_beta R)

      =
      sum_{i,j}
        beta_i beta_j R_ij^2.

Therefore

    boxed:
    E_res tr(M_beta R M_beta R)

      =
      (1/(6a^2))
        sum_i R_ii^2

      - (1/(2a^2 pi^2))
        sum_{i!=j}
          R_ij^2/(i-j)^2.

The second term is already one of the exact K2-weighted displacement
statistics.

## 2. alpha-alpha variance map

Put

    C_alpha=[M_alpha,J].

For white covariance

    E alpha_i alpha_j
      = c_alpha delta_ij,

a direct four-term expansion gives, for any matrix A,

    E[
      C_alpha A C_alpha
    ]

      =
      c_alpha [
        diag(diag(JA)) J
        - diag(diag(JAJ))
        - J diag(diag A) J
        + J diag(diag(AJ))
      ].

Set A=R and take the trace against R.

## 3. Symmetry identities

Since

    R^T=R,
    J^T=-J,

define

    r=diag R,

    h=diag(JR),

    q=diag(JRJ).

Then

    diag(RJ)=-h.

Also

    tr(
      [diag(h),J] R
    )
      =
      tr(
        diag(h)[J,R]
      ).

On the diagonal,

    [J,R]_ii
      =
      (JR)_ii-(RJ)_ii
      =
      2h_i.

Hence

    boxed:
    tr(
      [diag(h),J] R
    )
      =
      2 sum_i h_i^2.

Finally,

    sum_i r_i q_i
      =
      tr(
        diag(r) J R J
      )
      =
      tr(
        J diag(r) J R
      ).

Thus the two remaining terms are equal.

## 4. alpha-alpha contribution collapses

Combining the identities,

    boxed:
    E_res tr(
      [M_alpha,J] R
      [M_alpha,J] R
    )

      =
      (1/(2a^2))
      [
        sum_i h_i^2
        - sum_i r_i q_i
      ].

No two-index alpha covariance remains.

## 5. Cross terms vanish

The resonant covariance has

    E alpha beta^T
      =
      E beta alpha^T
      =0.

Therefore

    E_res tr(
      M_beta R [M_alpha,J] R
    )

and its reverse vanish.

## 6. Final resonant D2 primitive

Define

    Xi_res(R)

      =
      (1/d) E_res tr((B R)^2).

Then

    boxed:

    Xi_res(R)
      =
      1/(6a^2 d)
        sum_i r_i^2

      - 1/(2a^2 pi^2 d)
        sum_{i!=j}
          R_ij^2/(i-j)^2

      + 1/(2a^2 d)
        [
          sum_i h_i^2
          - sum_i r_i q_i
        ],

where

    r=diag R,
    h=diag(JR),
    q=diag(JRJ).

The actual resonant D2 Lindeberg coefficient is obtained by the already
closed z-derivative relation

    D2_res
      =
      (1/2) d/dz Xi_res(R(z)),

or directly by differentiating the four scalar statistics above.

## 7. LRSC/displacement reduction of the remaining off-diagonal statistic

The only explicit two-index term is

    sum_{i!=j}
      R_ij^2/(i-j)^2.

But

    [D,R]
      =
      pi^(-1)(v u^T-u v^T),

so

    R_ij
      =
      [v_i u_j-u_i v_j]/
      [pi(i-j)],
      i!=j.

Hence the displayed K2 statistic is itself a finite generator contraction
with total denominator 1/(i-j)^4.

It is even more summable than the generic D2 rank-three term.

Equivalently it has a one-dimensional Fourier representation with a fixed
2 by 2 generator channel.

Thus Xi_res is genuinely O(d)-state/small-channel.

## 8. What remains to make this theorem-grade

The algebraic resonant main is now finished.

Two analytic substitutions remain:

1. prove that the discrete ordinary-prime resonant covariance may be replaced
   by the continuum C_aa/C_bb kernels in the alpha/J contraction with o(1)
   error;

2. keep the already separate carrier-2T fast covariance under control.

The PNT prime-square measure upgrade already proves o(1) for every
K2-weighted bilinear.  The beta part is therefore in the closed class.

For the alpha part, the remaining job is only to show that its covariance
error contracts against

    tr([M_alpha,J]R[M_alpha,J]R)

through the bounded l2 Hilbert transform rather than an absolute harmonic
sum.

There are no unknown constants and no higher current-prime correlation
theorem left in the resonant D2 main.

See:

    notes/WP84_RESONANT_SCALAR_COVARIANCE.md
    notes/WP84_PNT_PRIME_SQUARE_MEASURE_UPGRADE.md
    notes/WP84_D2_CURRENT_COVARIANCE_CLOSURE.md
