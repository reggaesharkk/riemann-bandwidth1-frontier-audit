# WP84 — variance ramp transfer by normalized Hilbert--Schmidt control

Date: 2026-10-04

Status: **HISTORICAL VARIANCE-ONLY TRANSFER; SUPERSEDED BY THE GLOBAL BOUNDARY-QUARANTINE RESULT THAT ALSO COVERS DRIFT**

The sharp channel in `WP84_SHARP_VARIANCE_CHANNEL.md` is useful only if the
real ramp taper can be replaced at o(1) cost.

This note originally closed that transfer only for the second-order
prime-square variance sum.  A later fixed-boundary factorization now proves a
stronger statement for the **entire prime operator**, including first-order
drift:

    notes/WP84_GLOBAL_RAMP_SHARP_BOUNDARY_QUARANTINE.md
    src/wp84_global_ramp_sharp_boundary_gate.py

The argument below is retained as an independent Hilbert--Schmidt check.

## 1. Edge support of the overlap error

For y in [0,L], define

    f_y(x)=phi(x-y/2) phi(x+y/2)

and let

    f_y^sharp = 1_{[-L/2+y/2, L/2-y/2]}.

The actual ramp taper has width w=1 in the headline family: phi=1 off the two ramps and vanishes outside [-L/2,L/2].

Hence f_y-f_y^sharp can be nonzero only when at least one shifted argument lies in a ramp. Uniformly in y, the union of those edge pieces has measure at most 4w.

Also

    |f_y-f_y^sharp| <= 1.

Therefore

    integral |f_y-f_y^sharp|^2 <= 4w.

## 2. Compressed multiplication bound

Let P_d be the projection onto the d Fourier/Gabor modes on one interval of length L. For any bounded e,

    ||P_d M_e P_d||_F^2
      <= sum_{l<d} ||M_e e_l||_2^2
      = d/L * integral |e(x)|^2 dx.

The complex block difference is

    Delta Cplus(y)
      = 2*pi * P_d M_{f_y-f_y^sharp} P_d

up to the unitary modulations D_y, which do not change Schatten norms.

Thus

    boxed:
    ||Delta Cplus(y)||_F/sqrt(d)
      <= 4*pi*sqrt(w/L).

The same bound holds for Cminus and therefore, with a harmless constant, for the real cosine block C.

This estimate is uniform in y.

## 3. Transfer inside one resolvent variance trace

Write C=C0+E, where C0 is the sharp block. For a resolvent R on the fixed circle Gamma_rho,

    ||R||op <= M_rho := (1-rho)^(-1).

Then

    R C R C R - R C0 R C0 R
      = R E R C R + R C0 R E R.

Using normalized Hilbert--Schmidt Cauchy--Schwarz and ||C||op,||C0||op<=2*pi,

    boxed:
    |tau_d(R C R C R)-tau_d(R C0 R C0 R)|
      <= C_rho * sqrt(w/L),

uniformly in y.

No assumption that R is Toeplitz or multiplication is used here.

## 4. Sum over prime powers

The variance coefficient is

    kappa_n=Lambda(n)^2/(pi^2*n*a_phi^2*L^2).

The source-closed Chebyshev--Mertens estimate gives

    sum_{n<=X} kappa_n = O(1)

because a_phi is bounded away from zero.

Therefore summing the uniform one-block transfer bound yields

    boxed:
    sum_n kappa_n [
      tau(R C_n R C_n R)
      - tau(R C_n^sharp R C_n^sharp R)
    ]
      = O_rho(sqrt(w/L))
      = o(1)

for fixed w=1.

So the **entire second-order variance Lindeberg term may be computed with the sharp-flat blocks** up to o(1), even before ALG-star is known.

## 5. Why the same proof does not close the drift

The first-order coefficients have absolute mass

    sum_{n<=X} Lambda(n)/sqrt(n),

which grows like sqrt(X), not O(L^2).

Thus multiplying a per-block O(L^-1/2) ramp error by the absolute first-order mass is useless.

The drift still needs phase/trace cancellation or a separate structural identity.

This distinction is important: ramp transfer is now closed for V-diff/V-sum, but not for A1.

## 6. Updated variance frontier

After this note, the variance gate no longer needs to carry the physical ramp:

    actual variance
      = sharp variance + o(1).

The remaining variance tasks are:

1. prove the sharp intermediate resolvent is asymptotically multiplication/Toeplitz in the consumed trace sense;
2. then use `WP84_SHARP_RESOLVENT_TRACE.md` to kill same-sign branches and evaluate the mixed |x-u| channel.

This is a genuine reduction of the analytic debt, not a model-only numerical observation.