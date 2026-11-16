# WP84 — local additive-window form of the balanced E2 kernel

Date: 2026-10-06

Status: **THEOREM-INTERFACE REDUCTION — ON SHORT PRODUCT CELLS, THE MULTIPLICATIVE FINITE-COMPRESSION KERNEL BECOMES A LOCAL ADDITIVE FOURIER ENERGY OF WIDTH 1/H; THE ACTUAL WINDOW IS PRINCIPAL-MAJOR-ARC, NOT GENERIC MINOR-ARC**

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

## 5. Source-interface correction: the window is principal major arc

The location of the window matters, not only its width.

Since

    alpha_k=tau_k/(2pi M_0)

and the consumed height interval satisfies

    T<=tau_k<=2T+o(T),

we have

    1/(2pi H)
      <=
      alpha_k
      <=
      1/(pi H)+o(1/H).

In the E2 long-shift range the circle-method parameters satisfy

    Q<H.

The q=1 principal major arc contains

    |alpha|<=1/Q.

Hence

    boxed:

    the entire WP84 local window lies inside the q=1 principal major arc.

Therefore the principal source interface is the E2 **major-arc**
decomposition, not Proposition 3.5's generic minor-arc estimate.

The major-arc source writes the E2 exponential sum as

    principal model
      +
    centered remainder.

The WP84 task is to transfer this decomposition through the exact smooth
factor weights, identify the principal term with the closed-cycle connected
main, and prove the centered q=1 remainder is o(1) in the project
normalization.

The minor-arc estimate remains relevant only for auxiliary side windows or
partition errors that genuinely leave the principal arc.

## 6. Discrete samples versus local integral

The alpha grid spacing is

    1/(L M_0),

which is finer by a factor comparable to L than the natural 1/M_0
oscillation scale of a product-block exponential sum.

The discrete-to-local transfer is proved separately in

    notes/WP84_E2_OVERSAMPLING_TRANSFER.md.

It is independent of the major/minor-arc classification and remains valid.
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
- exact location of the local window inside the q=1 principal major arc.

Still open:

- the weighted varpi_2 transfer with explicit constants/uniformity;
- weighted q=1 principal-character transfer with explicit normalization;
- major-arc matching to the closed connected kernel;
- a normalized bound for the centered q=1 major-arc remainder.

No unconditional record theorem is claimed.

See:

    notes/WP84_BALANCED_PRODUCT_CORRELATION_BRIDGE.md
    notes/WP84_FIXED_BAND_M4_EVIDENCE_BOUNDARY.md
    notes/WP84_R400_EXACT_PAIR_LAYER.md
    notes/WP84_PHI4_POINTWISE_NONPOSITIVITY.md
