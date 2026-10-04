# WP84 — sharp-flat mixed variance channel

Date: 2026-10-04

Status: **EXACT IN THE SHARP FLAT CONTINUUM MODEL; ACTUAL RAMP / FINITE-SECTION TRANSFER OPEN**

This note identifies the leading operator-valued object hidden inside the mixed-sign variance branches from `WP84_VARIANCE_TOEPLITZ_RULES.md`.

## 1. Physical-space form of the sharp block

Take the flat taper on an interval of length L and rescale physical position to x in [0,1]. Put

    s=y/L in [0,1].

For the sharp flat overlap, the Toeplitz factor is multiplication by the overlap indicator. The diagonal modulation D_y is translation by s/2 in physical space, up to the global carrier exp(iTy/2).

Consequently the two complex prime blocks act as partial translations:

    Cplus(s) F(x)
      = 2*pi * exp(iTy) * 1_{0<=x<=1-s} * F(x+s),

    Cminus(s) F(x)
      = 2*pi * exp(-iTy) * 1_{s<=x<=1} * F(x-s).

The global carrier is written explicitly because it distinguishes sum- and difference-frequency branches.

## 2. Mixed branches preserve the multiplication algebra

Let A=M_a be multiplication by a bounded function a(x). Then the global carriers cancel and

    Cplus A Cminus
      = (2*pi)^2 M_{1_{x<=1-s} a(x+s)},

    Cminus A Cplus
      = (2*pi)^2 M_{1_{x>=s} a(x-s)}.

So the mixed-sign channel maps multiplication operators to multiplication operators exactly in the sharp model.

## 3. Prime-square measure

The variance coefficient is

    kappa_n = Lambda(n)^2/(pi^2*n*a_phi^2*L^2),

where a_phi is the taper mass normalization (Phi(0)=a_phi L).

The source-closed Chebyshev--Mertens law gives, for slow scalar weights,

    sum_{n<=e^L} Lambda(n)^2/n * g(log n/L)
      = L^2 * integral_0^1 s g(s) ds + O_g(L).

Combining this with the real-cosine factor 1/4 and (2*pi)^2 from each mixed branch, the pi factors cancel.

Therefore the sharp mixed variance channel on multiplication symbols is

    boxed:
    (K a)(x)
      = 1/a_phi^2 * [
          integral_0^(1-x) s a(x+s) ds
          + integral_0^x s a(x-s) ds
        ]

or, equivalently,

    boxed:
    (K a)(x)
      = 1/a_phi^2 * integral_0^1 |x-u| a(u) du.

This is not a scalar multiple of a or of its mean. It is an explicit nonlocal integral operator.

## 4. Connection with the old second-moment geometry

The kernel |x-u| is exactly the same geometric kernel that appears in the Montgomery--Taylor window functional / second-moment denominator.

So the resolvent variance has not produced an unrelated new object: after the correct physical-space reduction, it lands on the familiar overlap geometry.

This is a strong structural consistency check.

## 5. Same-sign branches become translations by 2s

For A=M_a,

    Cplus A Cplus

is a partial translation by +2s with carrier exp(2iTy), while

    Cminus A Cminus

is the -2s analogue.

Hence they do not preserve the multiplication algebra.

In an infinite sharp multiplication model their diagonal/trace contribution is expected to vanish away from s=0 because a nonzero partial translation has no diagonal kernel. But this is only a model statement: the actual finite Gabor section and ramp edges require a theorem-grade trace estimate.

Thus V-sum is now a concrete finite-section translation-trace problem rather than an opaque twisted prime sum.

## 6. Exact discrete analogue

`src/wp84_sharp_variance_channel.py` proves the finite non-cyclic identity

    sum_{r>=1} r (S_r^+ A S_r^- + S_r^- A S_r^+)
      = diag_i( sum_j |i-j| a_j )

for arbitrary diagonal A.

This is the exact lattice analogue of the |x-u| kernel and verifies the branch bookkeeping without floating arithmetic.

## 7. What this buys the resolvent route

If the permutation-averaged intermediate resolvents are asymptotically represented by multiplication symbols r_t(x,z), then the mixed variance term is explicit:

    K[r_t](x,z)
      = a_phi^(-2) integral_0^1 |x-u| r_t(u,z) du.

The Lindeberg/Dyson closure would then live entirely in a commutative multiplication algebra, with a known nonlocal covariance kernel.

The remaining jobs are therefore sharply separated:

1. **algebra closure:** prove averaged intermediate resolvents stay asymptotically in the multiplication/Toeplitz algebra;
2. **V-sum:** prove normalized traces of the ±2s partial-translation branches are o(1);
3. **ramp transfer:** replace the sharp flat overlap by the actual w=1 taper with o(1) normalized error;
4. **drift:** treat the first-order partial-translation channel.

No claim of a >79 theorem is made at this stage.