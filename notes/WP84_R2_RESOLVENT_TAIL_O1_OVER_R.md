# WP84 — sharpen r2 displacement truncation from R^{-1/2} to R^{-1}

Date: 2026-10-05

Status: **ONE-POINT RESOLVENT STRUCTURE IMPROVES THE LONG-DISPLACEMENT ERROR TO O(R^-1); THE EARLIER HOFFMAN--WIELANDT R^-1/2 BOUND IS NOT THE SHARP THEOREM INTERFACE**

No unconditional zero-density percentage is claimed here.

The first displacement-tail note used only

    ||H-H^(R)||_F

plus Hoffman--Wielandt, giving an r2 trace error O(R^-1/2).

For the preferred one-point consumer this throws away the key resolvent
structure.

At z=i, a second resolvent identity supplies one more displacement
denominator.  The long-range error is actually O(R^-1).

## 1. Setup

Let

    H
      = M_beta+[M_alpha,J],

and let H_R retain only off-diagonal displacements

    0<|i-j|<=R.

Write

    Delta
      = H-H_R,

    G(z)
      = (H-zI)^(-1),

    S(z)
      = (H_R-zI)^(-1).

For |Im z|>=eta>0,

    ||G||op,
    ||S||op
      <= eta^(-1).

The exact tail Hilbert--Schmidt estimate is

    boxed:

    tau(Delta^2)
      <=
      8 q_alpha/(pi^2 R),

where

    q_alpha
      =
      ||alpha||_2^2/d.

For the retained full prime field,

    q_alpha
      =
      1/4+o(1).

## 2. Second resolvent identity

The resolvent identity iterated once gives

    G-S
      =
      -S Delta S
      + S Delta S Delta G.

Hence

    tau(G-S)
      =
      -tau(Delta S^2)
      + tau(S Delta S Delta G).

The second term is immediately quadratic in the tail:

    boxed:

    |
      tau(S Delta S Delta G)
    |

      <=
      eta^(-3)
      tau(Delta^2)

      <=
      8 q_alpha/
      (pi^2 eta^3 R).

## 3. The linear term gains a second displacement denominator

Because Delta has zero diagonal,

    tau(Delta S^2)

      =
      d^(-1)
      sum_{|i-j|>R}
        Delta_ij
        (S^2)_ji.

For i!=j,

    Delta_ij
      =
      (alpha_i-alpha_j)/
      [pi(j-i)],

while

    (S^2)_ji
      =
      [D,S^2]_ji/(j-i).

Therefore

    |
      tau(Delta S^2)
    |

      <=
      1/(pi d)
      [
        sum_tail
          |alpha_i-alpha_j|^2/(i-j)^2
      ]^(1/2)

      [
        sum_tail
          |[D,S^2]_ji|^2/(i-j)^2
      ]^(1/2).

The first square root is

    pi ||Delta||_F.

For the second,

    1/|i-j| <= 1/R

on the tail, so it is at most

    R^(-1)
    ||[D,S^2]||_F.

## 4. Banded commutator has only sqrt(R) normalized Frobenius size

The truncated matrix satisfies

    [D,H_R]_ij
      =
      -(alpha_i-alpha_j)/pi

for 0<|i-j|<=R and zero otherwise.

For each displacement r,

    sum_i
      |alpha_{i+r}-alpha_i|^2

      <=
      4 ||alpha||_2^2.

Summing positive and negative r gives

    boxed:

    ||[D,H_R]||_F^2/d
      <=
      8 R q_alpha/pi^2.

Now

    [D,S]
      =
      -S[D,H_R]S,

and

    [D,S^2]
      =
      [D,S]S+S[D,S].

Thus

    ||[D,S^2]||_F
      <=
      2 eta^(-3)
      ||[D,H_R]||_F.

Combining Sections 1--4 gives

    boxed:

    |
      tau(Delta S^2)
    |

      <=
      16 q_alpha/
      (pi^2 eta^3 R).

## 5. Uniform resolvent comparison

Therefore

    boxed:

    |
      tau G(z)-tau S(z)
    |

      <=
      24 q_alpha/
      (pi^2 eta^3 R)

for every z with |Im z|>=eta.

With

    q_alpha=1/4+o(1),

this is

    boxed:

    |
      m_H(z)-m_{H_R}(z)
    |

      <=
      6/
      (pi^2 eta^3 R)
      + o(R^-1).

No alpha amplitude clip is needed for this estimate.

## 6. The repeated pole m'(i)

The r2 consumer also uses

    m'(i).

Take a fixed Cauchy circle

    |z-i|=rho,
    0<rho<1.

On that circle

    |Im z|>=1-rho.

Cauchy's derivative estimate yields

    boxed:

    |
      m_H'(i)-m_{H_R}'(i)
    |

      <=
      1/rho
      *
      6/
      [
        pi^2
        (1-rho)^3
        R
      ]

      +o(R^-1).

The elementary choice

    rho=1/4

keeps the full circle in

    Im z>=3/4

and gives a fixed explicit O(R^-1) constant.

## 7. Direct r2 consequence

Using

    tau r2(H)
      =
      2 Re[
        (2+i)m_H(i)
        -m_H'(i)
      ],

Sections 5--6 imply

    boxed:

    |
      tau r2(H)
      -
      tau r2(H_R)
    |

      =
      O(R^-1)

with a completely explicit constant.

This supersedes the earlier O(R^-1/2) Hoffman--Wielandt estimate for the
preferred first theorem rung.

The older bound remains valid and useful as an independent check.

## 8. Strategic consequence

For a target displacement error epsilon_band, the old reduction required

    R
      asymp epsilon_band^(-2).

The one-point resolvent reduction only requires

    R
      asymp epsilon_band^(-1)

up to a fixed explicit constant.

This materially shrinks the finite local window / compact-polynomial fallback
problem.

It also reinforces why the a=1 one-point consumer is preferable to a generic
bounded function: the fixed imaginary spectral gap supplies extra summability
that a black-box eigenvalue perturbation estimate cannot see.

See:

    notes/WP84_R2_DISPLACEMENT_TAIL_TRUNCATION.md
    notes/WP84_R2_A1_PREFERRED_RECORD_RUNG.md
    notes/WP84_R2_CAYLEY_DEFECT_GATE.md
