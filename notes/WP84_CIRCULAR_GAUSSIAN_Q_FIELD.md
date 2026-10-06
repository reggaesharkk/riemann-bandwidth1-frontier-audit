# WP84 — circular Gaussian scalar field behind the quadrature bridge

Date: 2026-10-05

Status: **EXACT FINITE-L STRUCTURE CLOSED; FIXED-LAG CONTINUUM COVARIANCE IDENTIFIED**

No percentage theorem is claimed here.

The two-quadrature Gaussian bridge has an especially simple interpretation at
the scalar Dirichlet-polynomial level.

## 1. Circular complex coefficient per prime

For an ordinary prime p write its positive scalar branch as

    q_p(tau)
      = - (log p)/(a L sqrt p)
          exp(i tau log p).

The Gaussian quadrature noise is

    (1/sqrt2)[
      g_{p,c}(A_p+A_p^*)
      + g_{p,s} i(A_p-A_p^*)
    ].

On the positive branch its random coefficient is

    gamma_p
      = (g_{p,c}+i g_{p,s})/sqrt2.

Thus the scalar positive-branch noise field is

    boxed:
    Z_L(tau)
      = sum_{p<=X}
          gamma_p q_p(tau).

The gamma_p are independent standard circular complex Gaussians:

    E gamma_p = 0,
    E |gamma_p|^2 = 1,
    E gamma_p^2 = 0.

The last identity is exactly the scalar reason the same-sign covariance
vanishes.

## 2. Exact covariance and zero pseudocovariance

For all tau,sigma,

    boxed:
    E[
      Z_L(tau)
      conjugate(Z_L(sigma))
    ]

      =
      1/(a^2 L^2)
      sum_{p<=X}
        (log p)^2/p
        exp(i(tau-sigma)log p).

Meanwhile

    boxed:
    E[
      Z_L(tau) Z_L(sigma)
    ]
      = 0.

So the artificial bridge noise is a circular Gaussian analytic field whose
entire law is fixed by one carrier-free prime-square covariance kernel.

## 3. Fourier-grid Toeplitz covariance

On

    tau_k=T+2*pi*k/L,

the carrier T disappears from the covariance:

    K_L(k-l)
      =
      1/(a^2 L^2)
      sum_p (log p)^2/p
        exp(
          i 2*pi(k-l) log p/L
        ).

Thus the covariance of the scalar noise samples is Toeplitz.

For every fixed integer r, the source-closed square-prime Mertens law plus
partial summation gives

    boxed:
    K_L(r)
      ->
      (1/a^2)
      int_0^1
        s exp(i2*pi*r*s) ds.

Hence

    K_infty(0)=1/(2a^2),

and for r!=0,

    boxed:
    K_infty(r)
      = 1/(2*pi*i*r*a^2).

The Hermitian relation

    K_infty(-r)
      = conjugate(K_infty(r))

is automatic.

Equivalently, the limiting Toeplitz covariance has physical-space symbol

    boxed:
    kappa(s)=s/a^2,
    0<=s<=1.

## 4. Derivative field is explicit too

Since

    q_p'(tau)
      = i log p q_p(tau),

the joint Gaussian law of

    Z_L,
    Z_L'/L

is determined by the same prime-square measure with extra powers of

    s=log p/L.

For fixed grid lag r,

    E[
      (Z_L'/L)(tau_k)
      conjugate(Z_L(tau_l))
    ]

converges to

    (i/a^2)
    int_0^1 s^2 e^(i2*pi*r*s) ds,

and all higher derivative covariances are analogous.

Therefore the random diagonal Loewner field

    2 Re Z_L - 2 Im Z_L'/L

also has an explicit limiting Gaussian covariance.

## 5. The bridge remains rank-two in displacement

For every realization of the circular field, the corresponding Hermitian
sharp noise matrix is

    diagonal(Z_L,Z_L')
      + [M_{Im Z_L},J].

So despite having a nontrivial Gaussian law across all d grid points,

    rank[D,W] <= 2

sample by sample.

Randomness does not enlarge the displacement state.

## 6. Why this is useful

The quadrature bridge has now separated the theorem into:

    deterministic arithmetic mean:
      t Q_full;

    artificial circular Gaussian fluctuation:
      sqrt(t(1-t)) Z_L;

    covariance:
      one Toeplitz kernel with symbol s/a^2;

    nonlinear matrix state:
      still rank-two Loewner/Cauchy-like.

This is a much more rigid random operator than a generic correlated Gaussian
matrix.

The next analytic question is whether its fixed-imaginary-part resolvent can
be controlled directly from the explicit covariance and displacement
generators, without invoking a black-box local law whose hypotheses do not
match this long-range Cauchy structure.

See:

    notes/WP84_GAUSSIAN_QUADRATURE_BRIDGE.md
    notes/WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION.md
