# WP84 — 80-digit hostile algebra audit of the exact-frontier rank-six consumer

Date: 2026-10-06

Status: **FINITE-D ALGEBRA REPLAY PASSED AT 80 DECIMAL DIGITS; NO CHANGE TO THE LARGE-T EVIDENCE BOUNDARY**

Target:

    notes/WP84_EXACT_FRONTIER_RANK6_CHRISTOFFEL_CAYLEY.md

Consumer:

    a_*^3=13891/9660,

    U_*=(H+i a_* I)(H-i a_* I)^(-1),

    Q_*=q_*(U_*).

This audit does not test the unresolved large-T arithmetic inequality.  It
hostile-checks the finite algebra that the future theorem must consume.

## 1. Deterministic sharp-Loewner state

The audit uses a deterministic 11x11 sharp Loewner state built directly from
six fixed Fourier sources.  No random seed is used.

All matrix arithmetic is performed with mpmath at 80 decimal digits.

## 2. Identities checked independently

The replay verifies:

1. Cayley unitarity

       U_*^* U_*=I;

2. symmetry inherited from real-symmetric H

       Q_*^T=Q_*;

3. skew symmetry of the displacement commutator

       [D,Q_*]^T=-[D,Q_*];

4. the cubic polynomial commutator identity

       [D,Q_*]
         =
         [D,U_*] B0
         +U_*[D,U_*]B1
         +U_*^2[D,U_*]q3;

5. the exact sharp two-column source factorization

       [D,U_*]
         =
         G2 H2^T;

6. the inherited six-column factorization

       [D,Q_*]
         =
         G6 H6^T;

7. the positive displacement-energy identity

       tau(Q_*^*Q_*)
         =
         d^(-1) sum_i |Q_ii|^2
         +
         d^(-1) sum_{i!=j}
           |[D,Q_*]_ij|^2/(i-j)^2.

## 3. 80-digit residuals

The deterministic replay returned:

    Cayley unitarity:
      1.06e-81

    Q symmetry:
      1.07e-82

    [D,Q] skew symmetry:
      4.51e-82

    polynomial commutator:
      8.38e-82

    rank-two source factor:
      8.36e-82

    six-column factor:
      8.29e-82

    positive-energy decomposition:
      3.22e-85.

These values are consistent with pure working-precision residuals.

## 4. What this rules out

This replay strongly rejects finite-algebra bugs in:

- the pole height a_*;
- the Cayley conversion;
- the cubic coefficient ordering;
- the rank-two sharp source sign;
- the 2x3 Krylov lift to six columns;
- the displacement-energy reconstruction.

In particular, the rank-six state is not an artifact of a floating SVD
threshold: the explicit six-column identity itself is verified.

## 5. What remains open

This audit does **not** prove

    limsup_T tau(Q_{*,T}^*Q_{*,T})
      <=
      1415/13891.

The remaining problem is genuinely arithmetic/asymptotic:

- control the six-column channel on the actual large-T sharp prime state;
- preserve the signed/differentiated Fourier channel through the Gaussian
  bridge;
- justify the large-u / large-d interchange in the one-point heat-flow
  representation;
- insert the already-established background, taper, and rank transfers.

The exact-frontier theorem target therefore remains one scalar inequality,
but it has now survived an independent high-precision finite-algebra replay.

## 6. Preferred next theorem interface

Use the exact one-point heat-flow identity

    E_0
      =
      1
      -
      int_0^infinity E_u' du,

with

    E_u'
      =
      Re E[
        A_* Xi_z
        +B_* Xi_zz
        +C_* Xi_zzz
      ]
      +o(1).

Do not split the Fourier part into independent absolute values.  Keep the
single differentiated T12 channel

    -(1/pi^2)
      Re E[
        A_* T12
        +B_* d_z T12
        +C_* d_z^2 T12
      ]

until the final one-sided estimate.

See:

    notes/WP84_EXACT_FRONTIER_RANK6_CHRISTOFFEL_CAYLEY.md
    notes/WP84_EXACT_FRONTIER_ONE_POINT_HEAT_FLOW.md
    src/wp84_exact_frontier_rank6_hp_audit.py
