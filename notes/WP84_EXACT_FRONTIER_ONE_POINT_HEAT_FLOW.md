# WP84 — one-point Gaussian heat flow for the exact-frontier rank-six consumer

Date: 2026-10-06

Status: **EXACT FINITE-d HEAT-FLOW INTERFACE — THE SINGLE FIXED 79.627 MODEL-FRONTIER CONSUMER REDUCES TO ONE NONREAL POINT AND THREE z-DERIVATIVE CURVATURE LEVELS**

No unconditional percentage theorem is claimed here.

Use the exact-frontier consumer from

    notes/WP84_EXACT_FRONTIER_RANK6_CHRISTOFFEL_CAYLEY.md.

Let

    a_*^3=13891/9660,

    U_*=(H+i a_* I)(H-i a_* I)^(-1),

    Q_*=q_*(U_*),

with q_* the exact degree-three Cayley polynomial.  Its positive defect is

    E(H)=tau(Q_*^*Q_*).

The model value is exactly

    1415/13891,

and q_*(1)=-1.

This note exposes the corresponding co-moving Gaussian heat-flow state.

## 1. Fourier coefficients of the positive energy

On the unit circle write

    |q_*(u)|^2
      =
      c0
      +sum_{k=1}^3[
         c_k u^k
         +conjugate(c_k)u^(-k)
       ].

The coefficients are exact algebraic numbers in Q(a_*,i).

At z=i a_* put

    R=(H-zI)^(-1),

    m(z)=tau R.

Since

    U_*=I+2 i a_* R,

we have exactly

    U_*^2
      =
      I+4 i a_* R-4 a_*^2 R^2,

and

    U_*^3
      =
      I+6 i a_* R-12 a_*^2 R^2-8 i a_*^3 R^3.

Therefore

    boxed:

    E(H)
      =
      1
      +2 Re[
          A_* m(z)
          +B_* partial_z m(z)
          +C_* partial_z^2 m(z)
        ],

where

    boxed:

    A_*
      =
      2 i a_*(
        c1+2c2+3c3
      ),

    B_*
      =
      (2 i a_*)^2(
        c2+3c3
      ),

    C_*
      =
      ((2 i a_*)^3/2)c3.

The constant is exactly one because

    q_*(1)=-1.

Numerically,

    a_*
      ~=1.128718027835367645,

    A_*
      ~=-3.903105590062112
        -4.544073147064304 i,

    B_*
      ~= 5.072784937065180
        +3.014625667936815 i,

    C_*
      ~=-1.117262443957614
        -0.031712655752998 i.

These decimals are diagnostics only; the theorem uses the exact algebraic
definitions above.

## 2. Additive Gaussian heat flow

Use the already-established co-moving bridge

    H_u
      =
      H_1+sqrt(u) W,

and define

    m_u(z)
      =
      E tau(H_u-zI)^(-1),

    C_u(z)
      =
      partial_u m_u(z).

Then

    boxed:

    E_u
      :=
      E tau[
        q_*(U_{*,u})^*
        q_*(U_{*,u})
      ]

      =
      1
      +2 Re[
          A_* m_u(z)
          +B_* partial_z m_u(z)
          +C_* partial_z^2 m_u(z)
        ],

and hence

    boxed:

    E_u'
      =
      2 Re[
        A_* C_u(z)
        +B_* partial_z C_u(z)
        +C_* partial_z^2 C_u(z)
      ].

No moving deterministic mean remains.

## 3. Insert the closed resonant covariance primitive

The existing Gaussian covariance reduction gives

    C_u(z)
      =
      (1/2)
      E Xi_z(R_u(z))
      +o(1).

Therefore

    partial_z C_u(z)
      =
      (1/2)
      E Xi_zz(R_u(z))
      +o(1),

and

    partial_z^2 C_u(z)
      =
      (1/2)
      E Xi_zzz(R_u(z))
      +o(1).

Thus

    boxed:

    E_u'
      =
      Re E[
        A_* Xi_z
        +B_* Xi_zz
        +C_* Xi_zzz
      ]
      +o(1).

This is the exact one-point curvature stencil for the full-frontier consumer.

## 4. Third derivative of the resonant primitive

Use the standard scalar state variables

    r_k=diag(R^k),

    h_k=diag(JR^k),

    q_k=diag(JR^kJ),

and

    T_ab
      =
      d^(-1)
      sum_{i!=j}
        (R^a)_ij
        (R^b)_ij
        /(i-j)^2.

The already-closed formulas are

    Xi_z

      =
      <r1,r2>/(3d)

      -T12/pi^2

      +<h1,h2>/d

      -[
         <r2,q1>
         +<r1,q2>
       ]/(2d),

and

    Xi_zz

      =
      [
        <r2,r2>
        +2<r1,r3>
      ]/(3d)

      -[
        T22+2T13
      ]/pi^2

      +[
        <h2,h2>
        +2<h1,h3>
      ]/d

      -[
        <r3,q1>
        +<r2,q2>
        +<r1,q3>
      ]/d.

Differentiating once more gives exactly

    boxed:

    Xi_zzz

      =
      (2/d)
      [
        <r2,r3>
        +<r1,r4>
      ]

      -(6/pi^2)
      [
        T23+T14
      ]

      +(6/d)
      [
        <h2,h3>
        +<h1,h4>
      ]

      -(3/d)
      [
        <r4,q1>
        +<r3,q2>
        +<r2,q3>
        +<r1,q4>
      ].

No prime sum remains in this exposed curvature.

## 5. Keep the Fourier leakage as one differentiated channel

The Fourier terms satisfy

    partial_z T12
      =
      T22+2T13,

and

    partial_z^2 T12
      =
      6(
        T23+T14
      ).

Therefore the complete Fourier leakage in the exact-frontier heat curvature
is not three independent debts.  It is exactly

    boxed:

    -(1/pi^2)
    Re E[
      A_* T12
      +B_* partial_z T12
      +C_* partial_z^2 T12
    ].

This form should be preserved before any triangle inequality.

When represented through both displacement commutators, the scalar Fourier
kernel is the corrected S4 kernel already established in the direct
heat-curvature notes.

The base T12 channel is only 2x4.  Differentiating that small channel in z is
the preferred implementation.  Expanding the second derivative term only as
a fallback exposes widths through 2x8.

## 6. Infinite-noise boundary

For every fixed finite section, the existing Gaussian invertibility argument
gives

    U_{*,u}->I

almost surely as u->infinity.

Because

    q_*(1)=-1,

we obtain

    boxed:

    E_u->1

at fixed d.

Therefore

    boxed:

    E_0
      =
      1
      -
      int_0^infinity
        E_u' du

at finite d.

The large-d theorem must still justify the tail or truncate it before
interchanging limits.

## 7. Two exact integrated targets

### First direct >79 target

A simple-zero proportion above 79 percent follows from

    E_0<0.105.

Equivalently it is enough to prove

    boxed:

    int_0^infinity
      E_u' du
      >
      0.895.

The frozen model endpoint has

    E_model=w0=1415/13891,

so its corresponding integral is

    boxed:

    1-w0
      =
      12476/13891
      =
      0.8981354834065222....

The exact >79 curvature cushion is therefore

    boxed:

    12476/13891
      -0.895

      =
      8711/2778200
      =
      0.00313548340652221....

### Full 79.62709668... target

The exact model-frontier theorem would follow from

    E_0<=w0+o(1),

equivalently

    boxed:

    int_0^infinity
      E_u' du

      >=
      12476/13891
      -o(1).

This is the single one-point integrated-curvature inequality corresponding to
the full fixed rank-six consumer.

## 8. Strategic comparison with the conditioned 79.5489 consumer

The exact-frontier q_* has the best possible frozen-model value in the current
Christoffel certificate, but its raw scalar heat coefficients are larger:

    |A_*|+|B_*|+|C_*|
      ~=13.00888.

The conditioned rational cubic in

    WP84_CONDITIONED_RANK6_79_CONSUMER

has the smaller proxy

    ~=9.85229

and may therefore be easier for the first >79 proof.

The preferred attack is consequently two-track:

1. use the conditioned cubic to obtain the first >79 theorem if its curvature
   stencil closes first;

2. use q_* to pursue the exact 79.62709668... frontier through the same
   one-point finite-channel machinery.

## Evidence boundary

Closed:

- exact one-point m,m',m'' representation;
- exact Gaussian heat-flow derivative;
- exact Xi_zzz formula;
- exact differentiated-T12 Fourier-channel compression;
- exact finite-d boundary E_infinity=1;
- exact integrated thresholds for >79 and 79.627.

Open:

- the one-sided large-d integrated curvature estimate;
- a uniform large-u tail/truncation estimate;
- final insertion of the already-closed background/taper/rank transfers.

See:

    notes/WP84_EXACT_FRONTIER_RANK6_CHRISTOFFEL_CAYLEY.md
    notes/WP84_CONDITIONED_RANK6_79_CONSUMER.md
    notes/WP84_DIRECT_DEGREE2_HEAT_CURVATURE_STENCIL.md
    notes/WP84_GAUSSIAN_COVARIANCE_HADAMARD.md
