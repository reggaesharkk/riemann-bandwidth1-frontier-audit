# WP83 — half-grid cancellation inside the actual Gabor evaluation family

Date: 2026-10-04
Status: **STRUCTURAL ANTI-ISOLATION MECHANISM IDENTIFIED; NUMERICAL C3-TAPER FALSIFIER PASSES; FULL ASYMPTOTIC WRITE-OUT PENDING**

The previous audit proved that critical Gabor spacing does not give a uniform principal-angle lower bound. A stronger phenomenon occurs: the Gabor evaluation family itself contains an asymptotic near-cancellation configuration for two deep off-line pairs.

## 1. Exact pair-matrix correlation formula

For a spectral point z define the full-grid evaluation vector u_z and pair matrix

    H_z = u_z u_z^T + conj(u_z) conj(u_z)^T.

The analytically continued Poisson-Gabor identity gives

    u_z^T u_w = L Phi(z-w),
    u_z^T conj(u_w) = L Phi(z-conj(w)).

Hence exactly

    <H_z,H_w>_F
      = 2 L^2 Re( Phi(z-w)^2 + Phi(z-conj(w))^2 ).

For two points of the same depth delta with real-ordinate separation Delta,

    z=gamma+i delta,
    w=gamma+Delta+i delta,

the normalized pair correlation is therefore

    R_L(Delta)
      = Re[ Phi(Delta)^2 + Phi(Delta-2i delta)^2 ]
        / [ Phi(0)^2 + Phi(2i delta)^2 ].

## 2. Half a Gabor spacing

The critical grid spacing is

    h=2*pi/L.

Take

    Delta=h/2=pi/L.

For fixed delta>0 and fixed ramp width w, the complex transform Phi(Delta-2i delta) is dominated by the same endpoint Laplace layer as Phi(-2i delta). Shifting the real frequency by Delta multiplies that endpoint contribution by

    exp(-i Delta L/2) = exp(-i pi/2) = -i

up to relative O(1/L) variation of the endpoint Laplace profile.

After squaring, the dominant term changes sign:

    Phi(Delta-2i delta)^2
      = - Phi(-2i delta)^2 * (1+o(1)).

The real-frequency term Phi(Delta)^2 is only polynomial in L, while the deep complex term has exponential scale exp(2 delta L). Therefore

    boxed:
    R_L(pi/L) -> -1.

Consequently

    ||H_gamma + H_{gamma+pi/L}||_F / ||H_gamma||_F -> 0

for equal-depth deep pairs in the full-grid model.

## 3. C3 taper falsifier

`src/wp83_halfgrid_pair_cancellation.py` evaluates the actual C26 taper family with the C3 monotone smoothstep

    rho(t)=35t^4-84t^5+70t^6-20t^7,

w=1 and delta=0.2.

Recorded values:

| L | pair Frobenius correlation | ||H0+H1||/||H0|| | ||u1+i u0||/||u0|| |
|---:|---:|---:|---:|
| 20  | -0.4881 | 1.0118 | 0.5795 |
| 40  | -0.8539 | 0.5406 | 0.3064 |
| 80  | -0.9616 | 0.2772 | 0.1554 |
| 120 | -0.9827 | 0.1858 | 0.1039 |
| 160 | -0.9902 | 0.1398 | 0.0781 |

The trend is exactly the half-grid cancellation predicted above.

## 4. Consequence for Proposition R

This is stronger than the abstract H and -H counterexample. It occurs inside the same critical-density Gabor evaluation geometry used by C26.

Therefore **Gabor spacing by itself cannot be the missing Proposition-R isolation lemma**. Two same-depth off-line pairs separated by about half a Gabor spacing can make their hyperbolic pair matrices nearly opposite.

No known general zero-spacing theorem forbids two distinct zeta zeros from having such an ordinate separation at scale 1/log T.

This does not disprove Proposition R for the actual zeta function. It proves that any valid Proposition-R globalization must use additional arithmetic or zero-configuration information strong enough to rule out or control these cancelling deep clusters.

## 5. Revised theorem-side target

The hard object is now explicit:

    **near-maximal-depth off-line clusters with phase separations near odd half-grid multiples.**

A successful Proposition-R reconstruction must show that such clusters either:

1. cannot occur for zeta;
2. cannot persist across the family of admissible windows/bandwidths needed by the moment theorem;
3. leave an uncancelled eigenvalue after summing the whole cluster;
4. or themselves force a comparably strong zero-free/zero-density conclusion by another argument.

Until one of these is proved, the successor retraction is an external warning, not a reconstructed theorem in our repository.
