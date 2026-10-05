# WP84 — taper universality and adaptive endpoint width

Date: 2026-10-05

Status: **BOUNDARY-QUARANTINE SCALE GENERALIZED FROM K log L TO EVERY w,W=o(L)**

The fixed-boundary quadrature argument does not require the physical ramp
width to be constant, and the endpoint quarantine does not require
W=K log L.

This gives two useful freedoms.

## 1. Taper universality for every w=o(L)

Let phi be any admissible taper satisfying

    0<=phi<=1,
    supp(phi) subset [-L/2,L/2],
    phi=1 on [-L/2+w,L/2-w],

with

    w=o(L).

Let chi be the sharp indicator of [-L/2,L/2].

The exact identity

    phi=chi-r

has r supported on two fixed boundary strips of total length 2w.

The global ramp-to-sharp factorization then gives

    P_phi
      = P_sharp + D_rank + D_small,

where the self-contained quadrature construction yields

    rank(D_rank)/d
      = O(w/L)
      = o(1),

and

    ||D_small||op
      <= T^(1/2+o(1))
          exp(-c T w)
      = o(1).

Therefore every bounded fixed-resolvent spectral statistic used by WP84 is
asymptotically **independent of the detailed taper profile** as long as
w/L->0.

The sharp operator is an admissible analysis surrogate even though the
original zero-side test function remains smooth.

## 2. Endpoint quarantine for every W=o(L)

For endpoint shifts

    y>=L-W,

the same common-strip proof gives

    rank(E_rank)/d
      = O(W/L),

    ||E_small||op
      <= T^(1/2+o(1)) exp(-c T W).

Hence any choice

    W->infinity,
    W/L->0

removes the prime range

    n>=X exp(-W)

at o(1) bounded-spectral cost.

The previous choice

    W=K log L

is only one convenient instance.

## 3. Stronger subpower deletion at zero asymptotic rank cost

At the endpoint lambda=1, X=exp(L) asymptotically matches the T scale.

Choose, for example,

    W=L^(1/2).

Then

    rank(E_rank)/d
      = O(L^(-1/2))
      = o(1),

but the retained prime range becomes

    n<=X exp(-sqrt(L)).

Equivalently,

    X_ret/T
      <= exp(-sqrt(log T)+o(1)).

This beats every fixed negative power of log T:

    for every A>0,
    exp(-sqrt(log T))
      = o((log T)^(-A)).

Thus **all fixed polylogarithmic losses can be absorbed before the retained
arithmetic analysis begins**, while the zero-count coefficient loses nothing
asymptotically.

More generally, taking

    W=L^alpha,
    0<alpha<1,

gives

    rank fraction O(L^(alpha-1))

and retained ratio

    exp(-L^alpha).

## 4. Slowly vanishing exponent gap

One may push farther.

Let

    eta(L)->0,
    eta(L)L->infinity,

and set

    W=eta(L)L.

Then

    rank fraction=O(eta(L))->0,

while

    X_ret
      = X exp(-eta(L)L).

At lambda=1 this is

    X_ret
      = T^(1-eta(L)+o(1)).

Examples:

    eta(L)=1/sqrt(L)
      -> X_ret/T=exp(-sqrt(L));

    eta(L)=1/log L
      -> X_ret=T^(1-1/log log T+o(1));

    eta(L)=1/log log L
      -> an even larger deleted endpoint layer,
         still with vanishing rank fraction.

The choice should be made only after inspecting the retained-range analytic
losses.

## 5. Strategic consequence

Any retained-range theorem whose only endpoint obstruction is a fixed
polylogarithmic loss may now assume, without asymptotic coefficient cost,

    X_ret/T
      <= exp(-sqrt(log T))

or any comparable subpower saving.

A theorem that genuinely requires a fixed power saving T^(-c) is not closed
by this device, because that would require W/L bounded below by c and hence a
non-vanishing rank fraction.

This cleanly separates:

- **polylog/subpower endpoint debt**, now removable;
- **fixed-power endpoint debt**, still substantive.

No unconditional >79 theorem is claimed.
