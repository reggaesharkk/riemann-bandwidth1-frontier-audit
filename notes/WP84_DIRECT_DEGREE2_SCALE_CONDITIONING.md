# WP84 — scale conditioning of the direct degree-two Cayley square

Date: 2026-10-06

Status: **EXACT SUPPORT-FREE SCALE FAMILY; a=4/3 IMPROVES THE EXPLICIT FIXED-POLE CONDITIONING OF THE CURRENT BEST DEGREE-TWO RANK-FOUR CONSUMER**

No unconditional zero-density percentage is claimed here.

The direct degree-two support-free square at a=1 is

    q(u)
      =
      [623u^2 +(55-1058i)u -(557+58i)]/1000,

with

    U_1(H)
      =
      (H+iI)(H-iI)^(-1).

Its model defect energy is

    0.10803423463999824...,

with model simple-zero ledger

    78.3931530720...%.

The half-line certificate is scale invariant.

## 1. Scale family

For every a>0 define

    U_a(H)
      =
      (H+iaI)(H-iaI)^(-1),

and

    boxed:
    h_a(H)
      =
      I-q(U_a)^*q(U_a).

For a real scalar x,

    U_a(x)
      =
      U_1(x/a).

Therefore

    |q(U_a(x))|^2>=1
      for x<=0

follows directly from the already-certified a=1 inequality because x/a<=0.

For x>0 the defect square is nonnegative.

Hence for every a>0,

    boxed:
    h_a(x)<=1_{x>0}

globally.

No new Sturm calculation is required for each scale.

## 2. Scalar resolvent form at general a

Let

    m_a
      =
      m(ia),

    m_a'
      =
      m'(ia).

The exact Fourier coefficients of |q|^2 are scale independent, while

    U_a
      =
      I+2iaR(ia),

    U_a^2
      =
      I+4iaR(ia)-4a^2R(ia)^2.

Thus

    boxed:

    tau q(U_a)^*q(U_a)

      =
      1260097/1000000

      +2 Re[
          a A m(ia)
          +a^2 B m'(ia)
        ],

where

    A
      =
      -661949/250000
      -(157257/125000)i,

    B
      =
      347011/250000
      -(18067/125000)i.

The displacement rank remains

    rank[D,q(U_a)]<=4

for every a.

## 3. Explicit band-tail conditioning scales like a^-2

The one-point resolvent tail theorem gives

    |m_H(ia)-m_HR(ia)|
      <=
      6/(pi^2 a^3 R)
      +o(R^-1).

For the derivative, use a Cauchy circle of radius rho a.
Optimizing

    rho(1-rho)^3

gives

    rho=1/4.

Therefore the direct-square energy comparison obeys

    boxed:

    |
      E_a(H)-E_a(H_R)
    |

      <=
      C_dir/(a^2 R)
      +o(R^-1),

with

    C_dir
      =
      12/pi^2
      [
        |A|
        +(256/27)|B|
      ]

      ~=19.65226898.

Thus the natural proof-conditioning metric is

    boxed:
    Delta_a a^2,

where

    Delta_a
      =
      E_rec-E_model(a)

is the positive defect-energy margin.

## 4. Exact a=4/3 certificate

At

    boxed:
    a=4/3,

exact reduction against the pinned Christoffel model gives

    boxed:

    E_model(4/3)

      =
      2643915226535620881849576949
      /
      21513987578630813262384200000

      =
      0.12289284898359526....

Hence the model positive-index lower bound is

    boxed:
    0.8771071510164047...,

and the model simple-zero ledger is

    boxed:
    75.42143020328095...%.

The conservative energy margin is

    boxed:
    Delta_{4/3}
      =
      0.0403571324724767....

The conditioning metric is

    boxed:
    Delta_{4/3}(4/3)^2
      =
      0.0717460132844031....

For comparison, at a=1,

    Delta_1
      =
      0.0552157468160738...,

so

    Delta_1*1^2
      =
      0.0552157468160738....

Thus a=4/3 improves the explicit margin-versus-tail metric by about

    boxed:
    29.9%.

## 5. Continuous reconnaissance

Using the exact pinned four-node model only as a conditioning diagnostic, the
continuous metric

    a^2 [E_rec-E_model(a)]

peaks near

    a~=1.34424.

The simple rational choice

    a=4/3=1.333...

is essentially at that optimum while preserving exact arithmetic.

This reconnaissance is not part of the theorem proof.

## 6. Why the scaled direct square is now preferable for fixed-pole estimates

At a=4/3:

- only one upper-half-plane point is consumed;
- no second pole;
- no derivative order beyond one;
- positive energy remains exact;
- displacement rank remains at most four;
- the pole gap is larger by 4/3;
- the explicit long-displacement comparison constant drops by a factor 9/16;
- the model still remains far above the conservative comparison line.

So the current direct-square hierarchy should keep:

A. a=1:
       maximal raw model simple ledger 78.39315...%;

B. a=4/3:
       better explicit theorem conditioning,
       model simple ledger 75.42143...%.

Use a=4/3 for fixed-pole / band-tail estimates unless a later arithmetic
constant has a different scale dependence.

## 7. Evidence boundary

Closed here:

- scale invariance of the global half-line certificate;
- exact general-a resolvent representation;
- exact a^-2 tail scaling;
- exact a=4/3 pinned-model certificate;
- exact rank-four persistence.

Still open:

- the large-T bounded-energy transport itself.

No unconditional record theorem is claimed.

See:

    notes/WP84_DIRECT_DEGREE2_CAYLEY_SQUARE.md
    notes/WP84_DIRECT_DEGREE2_SCALAR_HEAT_FLOW.md
    notes/WP84_R2_RESOLVENT_TAIL_O1_OVER_R.md
