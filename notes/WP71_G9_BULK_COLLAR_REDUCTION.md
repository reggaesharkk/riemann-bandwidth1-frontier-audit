# WP71 — bulk/collar reduction for the moving welding interval

Date: 2026-10-04
Status: **DETERMINISTIC GEOMETRY REDUCTION; analytic bulk estimate and normalized collar charge remain**

The apparent 'short-window' difficulty in G9-C can be reduced further by using the actual Stage-A scales.

After the consumed cell truncation, b1 and b2 are polylogarithmic. The Stage-A locks have J on the ambient X-scale, while an m-block has scale comparable to X/b2 (equivalently, in the paper's rescaled notation the prime windows have length Y comparable to their ambient scale). Thus the natural moving j-strip width 2J/b2 is also of the same ambient m-scale up to logarithmic factors.

For fixed k, let [A_k,B_k] be the simultaneous static support and put

    Hm = J/b2,
    c(n) = b1*n/b2.

Ignoring integer rounding and the already isolated j=0 puncture, the moving interval is exactly

    [A_k,B_k] intersect [c(n)-Hm, c(n)+Hm].

Its length is therefore a trapezoidal piecewise-linear function of c(n): two monotone ramps and a plateau. The exact floor/ceiling version differs by O(1).

## Logarithmic collar

Let

    M_k = min(B_k-A_k+1, floor(2J/b2)+1)

be the maximal moving-window length in the cell, and choose

    delta = (log X)^(-D).

Call n **bulk** when

    |I_k(n)| >= delta*M_k,

and **collar** otherwise.

Because c(n+1)-c(n)=b1/b2, each ramp spends at most

    delta*M_k * b2/b1 + O(1)

integer n-values below the bulk threshold. There are two ramps, hence

    # collar_n(k)
      <= 2*delta*M_k*b2/b1 + O(1).

The complete nonempty n-support has size of order

    (B_k-A_k+1 + 2J/b2)*b2/b1,

so the collar is an O(delta) geometric fraction, up to endpoint O(1) terms.

This statement is purely deterministic and survives the exact floor/ceiling endpoints from WP71_G9_B_MOVING_INTERVAL.

## Consequence for the bulk

On the bulk, every moving interval has length at least delta*M_k. If an MRT/Dirichlet-series argument gives a maximal arbitrary-subinterval estimate at the ambient block scale

    sum_k Emax(rk;M_k)^2
      << K*M_k^2*(log X)^(-A'),

then

    M_k^2 <= delta^(-2) * |I_k(n)|^2
             = (log X)^(2D) * |I_k(n)|^2.

Thus any fixed logarithmic loss caused by maximalization/truncation is harmless: request the source estimate with

    A' > A + 2D + C,

where C covers the deterministic outer-weight logarithms.

This is exactly the setting where MRT Lemma 2.2 and Corollary 2.5 are useful: arbitrary endpoint truncation costs logarithms, not a power of X.

## Consequence for the collar

The collar no longer needs the full shifted-prime theorem. Its deterministic n-support is only an O(delta) fraction of the geometric support. A crude prime-weight envelope costs fixed powers of log X. Therefore choosing D larger than those fixed powers is sufficient **provided the exact R-unit cell-mass normalization is written out**.

This is the natural place to merge G7 and G9:

- G9-C handles bulk endpoint errors with MRT maximal/truncation machinery;
- G7 charges the logarithmic boundary collar;
- the j=0 puncture is already confined to the lower-dimensional same-prime outer family.

## What this does not yet prove

The statement 'O(delta) geometric fraction' is not by itself an R-unit estimate. The next write-out must multiply the collar count by:

- the exact outer Lambda(b1)Lambda(b2)/(b1*b2) weight;
- the largest overlap/kernel factor on the cell;
- the prime n and m envelopes;
- the T/(pi*l*X*ell1^4) normalization;

and show the full sum is O((log X)^(-eta)) for some eta>0.

If that calculation closes, the troublesome genuinely short moving intervals disappear into G7, and the bulk G9-C theorem only needs arbitrary interval truncation at essentially the ambient prime scale.
