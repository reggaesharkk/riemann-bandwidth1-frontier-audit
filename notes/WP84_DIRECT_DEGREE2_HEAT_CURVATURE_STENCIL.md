# WP84 — explicit Gaussian heat-curvature stencil for the direct degree-two square

Date: 2026-10-06

Status: **EXACT FINITE-d DIFFERENTIATION OF THE CLOSED RESONANT COVARIANCE FUNCTIONAL; HEAT CURVATURE REDUCED TO A FINITE LIST OF ONE-POINT RESOLVENT STATISTICS**

No unconditional zero-density percentage is claimed here.

The current primary bounded consumer is the scaled direct degree-two Cayley
square.  At scale a>0 its defect energy is

    E_u(a)
      =
      1260097/1000000

      +2 Re[
          a A m_u(ia)
          +a^2 B partial_z m_u(ia)
        ],

with

    A
      =
      -661949/250000
      -(157257/125000)i,

    B
      =
      347011/250000
      -(18067/125000)i.

The co-moving Gaussian bridge gives

    E_u'(a)
      =
      2 Re[
          a A C_u(ia)
          +a^2 B partial_z C_u(ia)
        ],

where

    C_u(z)
      =
      partial_u m_u(z)
      =
      E tau(
        R_u V_res(R_u) R_u
      )
      +o(1)

after the already-closed fast covariance removal.

This note eliminates the abstract covariance symbol C_u.

## 1. Resonant primitive

For one state resolvent

    R=(H-zI)^(-1),

define

    r_k
      =
      diag(R^k),

    h_k
      =
      diag(JR^k),

    q_k
      =
      diag(JR^kJ).

Also define the K2-weighted bilinears

    T_ab(R)
      =
      d^(-1)
      sum_{i!=j}
        (R^a)_ij
        (R^b)_ij
        /(i-j)^2.

The exact resonant primitive is

    boxed:

    Xi(R)

      =
      1/(6d)
        <r_1,r_1>

      -1/(2 pi^2)
        T_11

      +1/(2d)
        [
          <h_1,h_1>
          -<r_1,q_1>
        ].

This is the a_phi=1 sharp normalization.  The harmless a_phi factors can be
restored multiplicatively before the final taper limit.

## 2. First z derivative

Because

    partial_z R^k
      =
      k R^(k+1),

we obtain exactly

    boxed:

    Xi_z

      =
      1/(3d)
        <r_1,r_2>

      -1/pi^2
        T_12

      +1/d
        <h_1,h_2>

      -1/(2d)
        [
          <r_2,q_1>
          +<r_1,q_2>
        ].

The heat-flow covariance scalar is therefore

    boxed:

    C_u(z)
      =
      1/2
      E Xi_z(R_u(z))
      +o(1).

The factor 1/2 is the exact derivative relation between

    tau(BRBR)

and

    tau(RBRBR).

## 3. Second z derivative

Differentiating again gives

    boxed:

    Xi_zz

      =
      1/(3d)
        [
          <r_2,r_2>
          +2<r_1,r_3>
        ]

      -1/pi^2
        [
          T_22
          +2T_13
        ]

      +1/d
        [
          <h_2,h_2>
          +2<h_1,h_3>
        ]

      -1/d
        [
          <r_3,q_1>
          +<r_2,q_2>
          +<r_1,q_3>
        ].

Hence

    boxed:

    partial_z C_u(z)
      =
      1/2
      E Xi_zz(R_u(z))
      +o(1).

No prime sum and no covariance matrix remains in the exposed curvature.

## 4. Direct-square heat curvature

Substitute Sections 2--3 into the direct degree-two energy derivative.

For every fixed scale a,

    boxed:

    E_u'(a)

      =
      Re E[
        a A Xi_z(R_u(ia))
        +a^2 B Xi_zz(R_u(ia))
      ]
      +o(1).

At the currently better-conditioned scale

    a=4/3,

this is one explicit complex linear combination of the finite scalar list

    <r1,r2>,
    <r2,r2>,
    <r1,r3>,

    <h1,h2>,
    <h2,h2>,
    <h1,h3>,

    <r2,q1>,
    <r1,q2>,
    <r3,q1>,
    <r2,q2>,
    <r1,q3>,

    T12,
    T22,
    T13,

all evaluated at the single point

    z=4i/3.

This is the exact Gaussian integration-by-parts stencil suggested by the
current one-point architecture.

## 5. Displacement-channel size

The off-diagonal terms remain small-channel objects.

For every k,

    [D,R^k]
      =
      sum_{j=0}^{k-1}
        R^j [D,R] R^(k-1-j).

Since

    rank[D,R]<=2,

we have

    boxed:
    rank[D,R^k]<=2k.

Thus:

    T12
      uses at most a 2 x 4 channel,

    T22
      uses at most a 4 x 4 channel,

    T13
      uses at most a 2 x 6 channel.

The largest generator width exposed by the complete heat-curvature stencil is
therefore six.

This does not undo the rank-four statement for the consumed energy Q^*Q.
It only records the size of one exact derivative representation of its
Gaussian curvature.

## 6. One-dimensional Fourier form — corrected kernel

For

    T_ab
      =
      d^(-1)
      sum_{i!=j}
        (R^a)_ij (R^b)_ij/(i-j)^2,

using both commutators contributes an additional factor (i-j)^2:

    [D,R^a]_ij [D,R^b]_ij
      =
      (i-j)^2
      (R^a)_ij (R^b)_ij.

Therefore the low-rank Fourier representation uses the **fourth-order**
kernel

    S4(t)
      =
      sum_{r!=0} e^(irt)/r^4

      =
      pi^4/45
      -pi^2 t^2/6
      +pi t^3/6
      -t^4/24

for 0<=t<=2pi.

The exact representation is

    boxed:

    T_ab
      =
      1/(2pi d)
      int_0^(2pi)
        S4(t)
        tr(
          [D,R^a] e^(itD)
          [D,R^b]^T e^(-itD)
        )
      dt.

The earlier S2 statement was a bookkeeping error: S2 would remove only the
two powers introduced by the commutators and would represent the unweighted
sum of (R^a)_ij(R^b)_ij instead of T_ab.

The channel dimensions from Section 5 are unchanged; only the scalar Fourier
kernel is corrected from S2 to S4.

So the direct heat-flow theorem still has no hidden high-dimensional
covariance object, but its exact low-rank Fourier kernel is S4.

## 7. Immediate theorem target

At a=4/3, the finite-d heat-flow identity is

    E_0(a)

      =
      E_infinity

      -
      int_0^infinity
        Re E[
          a A Xi_z
          +a^2 B Xi_zz
        ]
      du,

with

    E_infinity
      =
      1260097/1000000.

The conservative record crossing requires

    E_0(4/3)
      <
      0.163249981456072....

Equivalently the integrated explicit curvature stencil must exceed

    1.096847018543928....

The pinned model endpoint leaves energy margin

    0.0403571324724767....

The next analytic question is therefore no longer
"compute C_u" in the abstract.  It is:

> obtain a one-sided integral bound for the explicit Xi_z / Xi_zz scalar
> stencil at z=4i/3 with total loss below 0.04035713247.

## 8. Evidence boundary

Closed here:

- exact relation C_u=(1/2)E Xi_z;
- exact relation C_{u,z}=(1/2)E Xi_zz;
- exact scalar formulas for Xi_z and Xi_zz;
- exact small-channel size through width six;
- exact insertion into the direct degree-two heat-flow consumer.

Still open:

- the one-sided large-d integral estimate for this stencil;
- a uniform large-u boundary if the proof integrates all the way to infinity
  rather than truncating and estimating the tail.

No unconditional record theorem is claimed.

See:

    notes/WP84_DIRECT_DEGREE2_SCALAR_HEAT_FLOW.md
    notes/WP84_DIRECT_DEGREE2_SCALE_CONDITIONING.md
    notes/WP84_RESONANT_D2_EXPLICIT_FUNCTIONAL.md
    notes/WP84_GAUSSIAN_COVARIANCE_HADAMARD.md


## 9. Correction record

This note originally stated an S2 Fourier kernel for T_ab after replacing
both resolvent powers by their displacement commutators. That was incorrect
by two powers of displacement.

The corrected theorem-grade identity uses S4, as shown in Section 6.

The direct formulas for Xi_z and Xi_zz, the regression gate, and all scalar
coefficients are unchanged.
