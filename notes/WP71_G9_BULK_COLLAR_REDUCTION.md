# WP71 — bulk/collar reduction for the moving welding interval

Date: 2026-10-04
Status: **DETERMINISTIC GEOMETRY REDUCTION; analytic bulk estimate and normalized collar charge remain**

The apparent short-window difficulty in G9-C can be reduced further by using the actual Stage-A scales.

After the consumed cell truncation, the relevant moduli are polylogarithmic. In the public Stage-A notation the prime window has ambient scale X, the lock range has J asymptotic to X, and the moving strip |b1*n-b2*m|<=J has m-width asymptotic to J/b2. Since b2<=(log X)^B, this width loses only logarithmic powers relative to the ambient prime scale.

For fixed k, let [A_k,B_k] be the simultaneous static support and put Hm=J/b2 and c(n)=b1*n/b2. Ignoring integer rounding and the already isolated j=0 puncture, the moving interval is exactly [A_k,B_k] intersect [c(n)-Hm,c(n)+Hm]. Its length is a trapezoidal piecewise-linear function of c(n): two monotone ramps and a plateau. The exact floor/ceiling version differs only by endpoint O(1) terms.

## 1. The n-endpoint collar

Let M_k=min(B_k-A_k+1, floor(2J/b2)+1) be the maximal moving-window length at fixed k, and choose delta=(log X)^(-D). Call n bulk when |I_k(n)|>=delta*M_k and collar otherwise.

Because c(n+1)-c(n)=b1/b2, each ramp spends at most delta*M_k*b2/b1+O(1) integer n-values below the bulk threshold. There are two ramps, hence

    #collar_n(k) <= 2*delta*M_k*b2/b1 + O(1).

The complete nonempty n-support has size comparable to (B_k-A_k+1+2J/b2)*b2/b1, so the n-collar is an O(delta) geometric fraction, up to endpoint O(1) terms.

The companion falsifier src/wp71_g9_bulk_collar_count.py checks a conservative exact floor/ceiling version of this estimate over a large grid of unrelated integer cells.

## 2. The k-endpoint collar is even cheaper

Let the unsheared outer m-window have integer length M. The exact simultaneous support of m and m-rk has triangular length W_k=(M-r|k|)_+ up to the harmless choice of inclusive endpoints.

Declare the k-edge collar by 0<W_k<delta*M. There are O(delta*M/r+1) such k near each edge, and every one has weight at most delta*M. Therefore its weighted triangular mass is

    sum_{k in edge collar} W_k
      << delta^2*M^2/r + delta*M.

The full triangular mass is asymptotic to M^2/r. Thus away from the negligible endpoint lattice term the k-edge costs O(delta^2), stronger than the O(delta) n-collar.

Consequently we may place the doubly-bulk analysis on cells satisfying both W_k>=delta*M and |I_k(n)|>=delta*M_k. All remaining short-support configurations belong to deterministic collars.

## 3. Consequence for the analytic bulk

On the bulk, every moving interval loses at most a fixed logarithmic factor from its ambient cell scale. If an MRT/Dirichlet-series argument gives a maximal arbitrary-subinterval estimate at ambient scale M_k,

    sum_k Emax(rk;M_k)^2 << K*M_k^2*(log X)^(-A'),

then M_k^2 <= delta^(-2)*|I_k(n)|^2 = (log X)^(2D)*|I_k(n)|^2.

Thus maximalization/truncation and the bulk lower-length threshold cost only fixed logarithmic powers. Since the MRT input permits an arbitrarily large requested logarithmic saving, choose A'>A+2D+C, where C absorbs deterministic outer-weight losses.

MRT Corollary 2.5 is especially useful here: its right-hand side is independent of the truncation endpoints, so the supremum over all moving intervals can be taken without a union bound.

## 4. Consequence for G7 and the collar

The collar need not consume the full shifted-prime theorem. Its geometric support is O(delta) in the n-ramps and O(delta^2) in triangular k-mass.

A crude prime-weight envelope costs only fixed powers of log X. Therefore choosing D larger than those powers will force the collar to zero **once the exact consumed R-unit mass bound is written out**.

This is the natural merger of G7 and G9:

- G9-C handles the doubly-bulk endpoint errors through MRT maximal/truncation machinery;
- G7 charges the logarithmic n- and k-collars;
- the j=0 puncture is already confined to the lower-dimensional same-prime outer family.

## 5. What remains to make this theorem-grade

The geometric O(delta) and O(delta^2) statements are not by themselves R-unit estimates. The next write-out must multiply them by:

- the exact outer Lambda(b1)Lambda(b2)/(b1*b2) weight;
- the largest overlap/kernel factor in the cell;
- the crude inner prime-weight envelope;
- the factor T/(pi*l*X*ell1^4);
- the polylogarithmic cell multiplicity;

and show the total collar contribution is O((log X)^(-eta)) for some eta>0.

If that calculation closes, genuinely short moving intervals disappear into G7 and the G9-C bulk theorem only needs arbitrary interval truncation at an ambient scale reduced by logarithmic factors.
