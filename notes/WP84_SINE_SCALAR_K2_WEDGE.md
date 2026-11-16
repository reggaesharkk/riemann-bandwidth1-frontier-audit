# WP84 — scalar Fourier form of the full-sharp two-vector wedge

Date: 2026-10-06

Status: **EXACT FINITE-d IDENTITY; THE FULL-SHARP RANK-FOUR OFF-DIAGONAL ENERGY REDUCES TO SIX SCALAR K2 BILINEARS**

No unconditional zero-density percentage is claimed here.

For the full sharp sine-square route let

    R=(H-iaI)^(-1),

    u=R1,
    v=R alpha,

and

    W_ij
      =
      u_i v_j-v_i u_j.

Then

    [D,Q]_ij
      =
      (2ta/pi) Re W_ij,

so

    E_off
      =
      4t^2a^2/(pi^2 d)
      sum_{i!=j}
        [Re W_ij]^2/(i-j)^2.

The rank-four matrix channel can be reduced further to scalar sequences.

## 1. Six scalar sequences

Define

    A_i=|u_i|^2,

    B_i=|v_i|^2,

    C_i=u_i conjugate(v_i),

and

    P_i=u_i^2,

    Q_i=v_i^2,

    S_i=u_i v_i.

Let K2 be the real symmetric matrix

    (K2)_ij
      =
      1/(i-j)^2,
      i!=j,

with zero diagonal.

## 2. Exact wedge-square identity

For every pair i,j,

    (Re W_ij)^2
      =
      1/2 |W_ij|^2
      +1/2 Re(W_ij^2).

Summing against K2 and using symmetry gives exactly

    boxed:

    sum_{i!=j}
      [Re W_ij]^2/(i-j)^2

      =
      A^T K2 B

      -Re(
        C^* K2 C
      )

      +Re[
        P^T K2 Q
        -S^T K2 S
      ].

Therefore

    boxed:

    E_off

      =
      4t^2a^2/(pi^2 d)
      {
        A^T K2 B
        -Re(C^*K2C)
        +Re(P^T K2 Q-S^T K2 S)
      }.

No 4 by 4 matrix integral is required.

## 3. Exact one-dimensional Fourier representation

Let

    S2(theta)
      =
      sum_{r!=0}
        e^(ir theta)/r^2

      =
      pi^2/3
      -pi theta
      +theta^2/2,

for 0<=theta<=2pi.

For a finite sequence x define

    xhat(theta)
      =
      sum_j
        x_j e^(ij theta).

Then every transpose bilinear satisfies

    x^T K2 y

      =
      1/(2pi)
      int_0^(2pi)
        S2(theta)
        xhat(-theta)
        yhat(theta)
      dtheta,

while

    x^* K2 x

      =
      1/(2pi)
      int_0^(2pi)
        S2(theta)
        |xhat(theta)|^2
      dtheta.

Hence the exact off-diagonal energy is one scalar theta integral involving
only the six Fourier transforms

    Ahat,
    Bhat,
    Chat,
    Phat,
    Qhat,
    Shat.

## 4. Why the scalar form is preferable

The 4 by 4 displacement formulation is useful for rank bookkeeping.

The scalar form is better for one-sided analysis because it exposes the
cancellations directly:

    -Re(C^*K2C),

and

    Re(P^TK2Q-S^TK2S).

These terms should not be replaced by absolute values unless necessary.

The exact positivity of E_off comes only after the complete combination is
formed.

## 5. Immediate theorem target

At

    a=63/50,
    t=17/16,

the coefficient is

    4t^2a^2/pi^2.

The full-sharp theorem remains

    boxed:

    E_diag+E_off
      <
      0.163249981456072...,

with

    E_diag
      =
      d^(-1)
      sum_i
        [1-2ta Re R_ii]^2,

and E_off given by the scalar identity above.

This route pays no band-truncation charge.

## 6. Relation to the leverage majorant

The canonical-frame gamma-kappa estimate follows by discarding the signed
cancellations in the scalar identity.

Therefore the hierarchy is:

1. exact scalar K2 identity — primary;
2. canonical gamma-kappa majorant — fail-closed sufficient gate;
3. separate absolute-value bounds — last resort.

## 7. Evidence boundary

Closed:

- exact scalar decomposition of the real wedge square;
- exact S2 Fourier representation;
- preservation of all sign cancellations.

Open:

- a theorem-grade one-sided estimate of the combined scalar Fourier
  functional for the actual sharp prime state.

No unconditional record theorem is claimed.

See:

    notes/WP84_SINE_TWO_VECTOR_WEDGE.md
    notes/WP84_SINE_WEDGE_CANONICAL_FRAME.md
