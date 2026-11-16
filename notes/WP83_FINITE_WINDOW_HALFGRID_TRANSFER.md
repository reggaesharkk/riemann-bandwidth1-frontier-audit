# WP83 — finite-window persistence of the half-grid cancellation

Date: 2026-10-04
Status: **FINITE ACTIVE-WINDOW TRANSFER CLOSED FOR INTERIOR DEEP PAIRS**

The half-grid cancellation was first derived on the infinite critical-density Gabor grid.  Proposition R, however, concerns the finite compression with indices 0<=k<d.  This note shows that an interior deep pair inherits the same cancellation up to a vanishing error.

## 1. Full and finite evaluation vectors

Let

    tau_k = T + 2*pi*k/L,

and for a spectral point z=gamma+i*delta define

    u_full = ( phi_hat(z-tau_k) )_{k in Z},
    u_I    = ( phi_hat(z-tau_k) )_{0<=k<d}.

Assume the ordinate is D away from both Gabor endpoints:

    T+D <= gamma <= 2T-D.

C26's two-integration-by-parts bound is

    |phi_hat(x+i y)|
      <= exp(|y|L/2) * ||phi''||_1 / |x+i y|^2.

For every omitted grid point, |gamma-tau_k| is at least D+O(2*pi/L).  Since the grid spacing is h=2*pi/L,

    sum_{k outside I} |gamma-tau_k|^(-4)
      << (L/D^3).

Hence

    boxed:
    ||u_full-u_I||_2^2
      << ||phi''||_1^2 * exp(delta L) * L / D^3.

## 2. Comparison with the deep-pair main scale

For fixed delta>0 and fixed ramp width w, the exact full-grid norm is

    ||u_full||_2^2 = L Phi(2 i delta).

Because phi=1 on the plateau and the Laplace weight is largest at one endpoint,

    Phi(2 i delta)
      >>_{delta,w} exp(delta L).

Therefore

    boxed:
    ||u_full-u_I||_2^2 / ||u_full||_2^2
      <<_{delta,w} D^(-3).

Equivalently,

    ||u_full-u_I||_2 / ||u_full||_2
      <<_{delta,w} D^(-3/2).

## 3. Pair-matrix transfer

For

    H(u)=u u^T + conj(u) conj(u)^T,

the elementary rank-one inequality gives

    ||H(u)-H(v)||_F
      <= 4 ||u||_2 ||u-v||_2 + 2 ||u-v||_2^2.

Thus, for an interior fixed-depth pair,

    ||H_full-H_I||_F / ||H_full||_F
      <<_{delta,w} D^(-3/2).

Take the same buffer used by C26,

    D=T^(1/2).

Then the finite active-window pair matrix differs from its infinite-grid model by

    O_{delta,w}(T^(-3/4))

in relative Frobenius scale.

## 4. Consequence for the half-grid construction

Let two equal-depth off-line pairs have ordinate separation

    Delta=pi/L + o(1/L)

and both lie at least T^(1/2) from the Gabor endpoints.

The full-grid result gives

    ||H_1+H_2||_F / ||H_1||_F -> 0.

The finite-window transfer above adds only o(1). Therefore

    boxed:
    ||H_{1,I}+H_{2,I}||_F / ||H_{1,I}||_F -> 0.

So the anti-isolation mechanism is not an artifact of the infinite Poisson frame.  It persists in the actual finite compression for interior pairs.

## 5. Endpoint pairs

This argument deliberately excludes zeros within D of T or 2T.  That is not a serious escape for a global Proposition-R proof: a fixed zero ordinate can be placed in the interior of a neighboring dyadic compression.  Nevertheless any theorem using that maneuver must write the window-selection bookkeeping explicitly.

## 6. Evidence boundary

This result still does not assert that zeta possesses two same-depth off-line pairs at half-grid separation.  It proves only that the **Gabor compression cannot rule them out or suppress their cancellation** once such a configuration is present.

Therefore a valid Proposition-R globalization lemma must use information beyond the finite/infinite-window distinction.
