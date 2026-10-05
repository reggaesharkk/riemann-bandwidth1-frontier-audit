# WP84 — local additive-window form of the balanced E2 kernel

Date: 2026-10-06

Status: **THEOREM-INTERFACE REDUCTION — ON SHORT PRODUCT CELLS, THE MULTIPLICATIVE FINITE-COMPRESSION KERNEL BECOMES A LOCAL ADDITIVE FOURIER ENERGY ON THE EXACT 1/H SCALE USED BY THE E2 MINOR-ARC THEOREM**

No unconditional zero-density percentage is claimed here.

The fixed-band fourth-moment fallback leaves only the positive
finite-compression / near-resonant leakage above the complete pair layer.

The balanced two-positive/two-negative sector has already been collapsed to
a product coefficient c(m).  The remaining finite-compression kernel is

    K_T(m,n)
      =
      (1/d)
      sum_{k=0}^{d-1}
        exp(
          i tau_k log(m/n)
        ),

with

    tau_k
      =
      T + 2pi k/L.

This note identifies its local additive Fourier form.

## 1. Product-scale and shift-scale

Fix a product scale

    M < m,n <= 2M,

and write

    h=n-m.

The near-resonant window is

    |h|
      <=
      C H,

where

    boxed:
    H=M/T.

This is the same shift scale that appears in the E2 correlation problem.

## 2. Short multiplicative cells

Partition the dyadic product block into cells

    I=[M_0,M_0(1+delta)]

with delta=o(1), but large enough that the number of cells is harmless.

For m,n in one cell and |h|<=CH,

    log(m/n)
      =
      -log(1+h/m).

Taylor expansion gives

    log(m/n)
      =
      -h/M_0
      +
      O(
        delta |h|/M_0
        +h^2/M_0^2
      ).

Since |h|<=C M_0/T and tau_k<=2T+o(T),

    boxed:

    tau_k
    [
      log(m/n)
      +h/M_0
    ]

      =
      O_C(
        delta
        +1/T
      ).

Therefore uniformly in the near-resonant window,

    boxed:

    exp(
      i tau_k log(m/n)
    )

      =
      exp(
        -i tau_k h/M_0
      )

      +
      O_C(
        delta+1/T
      ).

This is the exact place where multiplicative near resonance becomes additive
short-shift Fourier analysis.

## 3. Additive frequency window

Define

    alpha_k
      =
      tau_k/(2pi M_0).

Then

    exp(
      -i tau_k h/M_0
    )

      =
      e(
        -h alpha_k
      ).

The grid spacing is

    alpha_{k+1}-alpha_k
      =
      1/(L M_0).

The total alpha-span is

    (tau_{d-1}-tau_0)/(2pi M_0).

For the consumed Fourier window, tau spans an interval of length comparable
to T, so the alpha-span is

    boxed:
    comparable to T/M_0
      =
      1/H.

Thus the finite-compression trace samples an additive Fourier-energy window
at exactly the local frequency scale 1/H.

## 4. Energy identity after linearization

Let c_I(m) be the product coefficient restricted to one short cell.

After the phase replacement from Section 2,

    sum_{m,n in I}
      c_I(m) conjugate(c_I(n))
      K_T(m,n)

becomes

    boxed:

    (1/d)
    sum_k
      |
        sum_{m in I}
          c_I(m)
          e(
            m alpha_k
          )
      |^2

plus the controlled phase-linearization error.

So the hard balanced trace sector is a local additive Fourier energy, not an
arbitrary sum over shifts.

## 5. Match to the E2 minor-arc theorem

For the factor-sliced semiprime coefficient, Evans' E2 circle-method
argument uses

    S(alpha)
      =
      sum_{X<n<=2X}
        varpi_2(n)e(n alpha).

Its Proposition 3.5 controls, uniformly for a minor-arc centre alpha,

    int_{
      minor
      cap
      [alpha-1/(2H),alpha+1/(2H)]
    }
      |S(theta)|^2 dtheta

by a power of log smaller than the full local mass, in the range

    log^(19+epsilon) X
      <=
      H
      <=
      X log^(-A) X.

The WP84 finite-compression window found above has the same width 1/H.

This is the correct source interface: apply the local frequency-window bound
before converting to an absolute sum over additive shifts.

## 6. Discrete samples versus local integral

The alpha grid spacing is

    1/(L M_0),

which is finer by a factor comparable to L than the natural 1/M_0
oscillation scale of a product-block exponential sum.

Therefore the discrete local average can be transferred to a slightly
enlarged local integral by the standard oversampling inequality for
trigonometric polynomials.

A theorem-grade implementation should prove the elementary form directly:

    boxed:

    (1/N_I)
    sum_{alpha_k in J}
      |S_I(alpha_k)|^2

      <=
      C
      H
      int_{J^+}
        |S_I(theta)|^2 dtheta,

where

    |J| comparable to 1/H,

    J^+

is enlarged by O(1/M_0), and C is absolute.

The enlargement is negligible because

    1/M_0
      =
      1/(T H)
      =
      o(1/H).

## 7. Weight transfer still required

The WP84 product coefficient is not literally varpi_2.

On a factor slice it has the form

    smooth(n)
    *
    log p_1
    *
    log p_2

for n=p_1p_2, together with the square-root normalization.

The remaining source transfer is finite and explicit:

1. partition one prime factor multiplicatively;
2. freeze log p_1 up to a 1+o(1) factor on each slice;
3. use partial summation for the smooth n^(-1/2) weight;
4. apply the local minor-arc estimate to the varpi_2 factor;
5. sum the factor slices.

This is narrower than an arbitrary weighted Hardy--Littlewood theorem.

## 8. Major arcs

The major-arc contribution must be kept with its sign.

At the closed-cycle limit the connected fourth-order kernel satisfies

    C4<=0

pointwise.

The desired theorem is therefore not an asymptotic for every individual
shift.  It is enough to show that:

- the major-arc main term converges to the already-certified closed-cycle
  connected contribution;
- all major-arc transfer errors are o(1);
- the minor-arc local energy is o(1).

Then the positive connected leakage is o(1), which is far below the current
R=400 allowance of approximately 0.02479.

## 9. Transition layer

Evans' long-shift range begins at a polylogarithmic H.

The unresolved transition layer has

    H<log^(19+epsilon) M.

Equivalently

    M/T
      =
      exp(
        o(log T)
      ),

so its normalized product exponent satisfies

    s=1+o(1).

The exact connected-kernel turn-on

    |C4|
      <=
      26(s-1)_+

then supplies a separate shrinking-layer mechanism.

A complete proof still needs a normalized mass bound for this layer, but the
kernel itself vanishes linearly at the wall.

## 10. Current fourth-moment theorem target

At R=400 the exact pair sector satisfies

    Pair_400
      <
      0.266329,

while the centered-fourth ceiling is

    W_400
      ~=
      0.2911227517.

Thus the available positive non-pair leakage is

    boxed:

    >0.0247937.

If the local-window transfer above yields o(1) on the fixed supercritical
cells and the shrinking transition layer is o(1), the centered-fourth gate
closes.

## 11. Evidence boundary

Closed here:

- exact product/shift scale H=M/T;
- uniform multiplicative-to-additive phase linearization on short product
  cells;
- exact identification of the additive frequency-window width 1/H;
- correct placement of the E2 local minor-arc theorem before any lossy
  shiftwise Cauchy--Schwarz step.

Still open:

- the weighted varpi_2 transfer with explicit constants/uniformity;
- the discrete-sample-to-local-integral lemma in the exact normalization;
- major-arc matching to the closed connected kernel;
- a normalized mass bound for the shrinking s=1+o(1) transition layer.

No unconditional record theorem is claimed.

See:

    notes/WP84_BALANCED_PRODUCT_CORRELATION_BRIDGE.md
    notes/WP84_FIXED_BAND_M4_EVIDENCE_BOUNDARY.md
    notes/WP84_R400_EXACT_PAIR_LAYER.md
    notes/WP84_PHI4_POINTWISE_NONPOSITIVITY.md
