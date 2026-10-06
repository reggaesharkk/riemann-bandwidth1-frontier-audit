# WP84 — shrinking product-scale transition layer has vanishing normalized mass

Date: 2026-10-06

Status: **STANDARD-INPUT MASS BOUND CLOSED — THE PRODUCT CELLS BELOW THE E2 LONG-SHIFT RANGE HAVE o(1) NORMALIZED MASS**

No unconditional zero-density percentage is claimed here.

The local E2 theorem applies once

    H=M/T
      >=
      log^(19+eps) M.

The unresolved transition cells satisfy

    1
      <=
      M/T
      <
      log^(19+eps) M.

In logarithmic product coordinates this is a shrinking neighborhood of the
classical wall.

This note proves that its normalized prime-pair mass tends to zero.

## 1. Logarithmic prime measure

Let L be the logarithmic prime cutoff scale and define

    mu_L
      =
      (1/L)
      sum_{n<=e^L}
        Lambda(n)/n
        delta_{log n/L}.

The standard Mertens/PNT estimate gives the uniform discrepancy bound

    boxed:

    D_L
      =
      sup_{0<=u<=1}
      |
        mu_L([0,u])-u
      |

      =
      O(1/L).

Also

    mu_L([0,1])
      =
      1+O(1/L).

## 2. Product-scale strip

For two positive prime-power coordinates beta_1,beta_2 in [0,1], put

    s=beta_1+beta_2.

Let delta>0.

For each beta_1,

    1<s<=1+delta

means

    1-beta_1
      <
      beta_2
      <=
      1+delta-beta_1.

The interval has length at most delta.

By one-dimensional discrepancy,

    mu_L(
      (1-beta_1,1+delta-beta_1]
    )

      <=
      delta+2D_L,

uniformly in beta_1, after clipping to [0,1].

Integrating with respect to the first copy of mu_L gives

    boxed:

    (mu_L tensor mu_L)
    {
      1<s<=1+delta
    }

      <=
      (1+O(1/L))
      (
        delta+2D_L
      )

      =
      O(
        delta+1/L
      ).

No two-dimensional discrepancy theorem is required.

## 3. Width of the short-shift transition

Write

    M=e^(Ls).

The transition condition

    1
      <=
      M/T
      <
      log^(19+eps) M

implies

    0
      <=
      log(M/T)
      <
      (19+eps) log log M.

Since the classical wall M=T corresponds to s=1 in the current
normalization,

    boxed:

    0
      <=
      s-1
      <=
      C
      log L/L

throughout the transition layer.

Thus take

    delta_L
      =
      C log L/L.

Section 2 gives

    boxed:

    transition pair mass
      =
      O(log L/L)

      =
      o(1).

## 4. Four-variable balanced sector

The balanced two-positive/two-negative sector is a product of one positive
pair measure and one negative pair measure, followed by the finite-compression
near-resonance kernel.

The second pair has total normalized mass O(1).

Therefore if either product scale lies in the transition strip, the total
four-variable normalized mass is still

    boxed:
    O(log L/L).

## 5. Kernel amplitude is uniformly bounded

Every hard-window overlap factor lies in [0,1].

The normalized finite Dirichlet kernel satisfies

    |D_d(y)|<=1.

Carrier phases have unit modulus.

The connected order-four ledger contains only finitely many terms.

Therefore the absolute finite-compression kernel on the transition strip is
bounded by an absolute constant.

Combining with Section 4,

    boxed:

    transition contribution
      =
      O(log L/L)
      =
      o(1).

This conclusion does not require the closed-cycle sign C4<=0.

The linear turn-on bound for C4 is compatible with the result but is not
needed for the mass estimate.

## 6. Consequence

The short-shift cells below

    H=log^(19+eps) M

do not require a separate almost-prime correlation theorem at leading order.

Their entire normalized contribution vanishes from the order-four
finite-compression ledger.

Thus the balanced fourth-order arithmetic problem may be restricted to the
long-shift cells in the published E2 range, plus boundary terms already
covered by the standard prime-measure discrepancy.

## 7. Updated remaining debt

After this note and the oversampling transfer, the long-shift balanced sector
has only two substantive source transfers left:

1. the exact WP84 factor-sliced coefficient -> E2 coefficient transfer;
2. major-arc matching with the signed closed-cycle connected main term.

The discrete sampling step and the polylogarithmic transition layer are no
longer open.

No unconditional record theorem is claimed.

See:

    notes/WP71_PRIME_MEASURE_CONTINUUM_TRANSFER.md
    notes/WP84_E2_LOCAL_WINDOW_TRANSFER.md
    notes/WP84_E2_OVERSAMPLING_TRANSFER.md
    notes/WP84_PHI4_POINTWISE_NONPOSITIVITY.md
