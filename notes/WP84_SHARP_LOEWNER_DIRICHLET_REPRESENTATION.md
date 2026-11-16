# WP84 — scalar Dirichlet-polynomial / Loewner representation of the sharp prime matrix

Date: 2026-10-05

Status: **EXACT MATRIX REPRESENTATION CLOSED; BOUNDED RESOLVENT LAW NOW REDUCED TO A DISCRETE CALDERON-COMMUTATOR MODEL**

This note sharpens the LRSC-inspired displacement-rank result.

The whole sharp retained prime matrix is determined by samples of **one scalar
prime Dirichlet polynomial and its first derivative**.

## 1. Scalar prime polynomial

Work on I=[0,L] with Fourier grid

    tau_k=T+2*pi*k/L,
    0<=k<d.

Let the sharp positive branch be

    A_+
      = sum_n c_n exp(i T y_n) U_{y_n}^+,

where

    y_n=log n

and c_n contains the fixed real prime coefficient and normalization.

Define the scalar analytic Dirichlet polynomial

    boxed:
    Q(tau)
      = sum_n c_n exp(i tau y_n).

Write

    a(tau)=Im Q(tau),
    b(tau)=Re Q(tau).

## 2. Exact off-diagonal formula

For k!=l the partial-shift matrix identity gives

    (U_y^+)_{kl}
      = [exp(i2*pi*k y/L)-exp(i2*pi*l y/L)]
          /[i 2*pi(l-k)].

After multiplication by exp(iTy) and summation over n,

    boxed:
    (A_+)_{kl}
      = [Q(tau_k)-Q(tau_l)]
          /[i 2*pi(l-k)].

The Hermitian prime matrix is

    P=A_+ + A_+^*.

Since A_+ is complex symmetric in this basis,

    boxed:
    P_{kl}
      = [a(tau_k)-a(tau_l)]
          /[pi(l-k)],
      k!=l.

Thus all off-diagonal entries are divided differences of one real scalar
sequence a_k=a(tau_k).

## 3. Exact diagonal formula

For one partial shift,

    (U_y^+)_{kk}
      = (1-y/L) exp(i2*pi*k y/L).

Therefore

    (A_+)_{kk}
      = sum_n c_n (1-y_n/L) exp(i tau_k y_n).

But

    Q'(tau)
      = i sum_n c_n y_n exp(i tau y_n),

so

    boxed:
    (A_+)_{kk}
      = Q(tau_k)+i Q'(tau_k)/L.

Hence

    boxed:
    P_{kk}
      = 2 b(tau_k)-2 a'(tau_k)/L.

The entire d by d matrix P is therefore determined by

    Q(tau_k),
    Q'(tau_k),

on the d-point grid.

No independent d^2 operator data remain.

## 4. Discrete Calderon commutator form

Define the skew discrete Hilbert kernel

    J_{kl}
      = 1/[pi(l-k)]  for k!=l,
      = 0             for k=l,

and let M_a=diag(a(tau_k)).

Then

    [M_a,J]_{kl}
      = [a(tau_k)-a(tau_l)]/[pi(l-k)]

off the diagonal and is zero on the diagonal.

Therefore

    boxed:
    P
      = M_{,2b-2a'/L}
        + [M_a,J].

This is an exact finite matrix identity.

The prime operator is a diagonal scalar sample plus a discrete
Calderon/Loewner commutator.

## 5. Recovery of the rank-two displacement law

Let D=diag(0,1,...,d-1).

Because

    (k-l) P_{kl}
      = -[a_k-a_l]/pi,

we get

    [D,P]
      = -(1/pi)
          [a 1^T-1 a^T],

hence

    rank[D,P]<=2.

So the previous displacement theorem is exactly the finite-rank signature of
the scalar Loewner representation.

## 6. Why this is a stronger state reduction

The old operator-valued formulation treated an intermediate sharp prime state
as a generic d by d Hermitian matrix.

The exact representation shows that each subset state is instead encoded by
one subset Dirichlet polynomial

    Q_S(tau)
      = sum_{n in S} c_n exp(i tau log n),

through

    P_S
      = M_{2 Re Q_S-2(Im Q_S)'/L}
        + [M_{Im Q_S},J].

Thus the permutation process evolves a scalar analytic function Q_S, not an
arbitrary matrix.

The resolvent is still nonlocal and noncommutative, but its matrix source is
now explicit and one-dimensional in the spectral variable.

## 7. Harmonic-analysis interpretation

In a continuum scaling, the kernel

    [a(x)-a(y)]/(x-y)

is the classical first Calderon commutator.

Therefore the retained-range WP84 problem can be reframed as a bounded
functional-calculus problem for

    diagonal prime field
      + Calderon commutator of its imaginary part.

This opens a different analytic toolbox from raw joint-prime moments:

- discrete Hilbert-transform bounds;
- commutator estimates;
- BMO/Lipschitz controls;
- resolvent identities for Loewner/Cauchy-like matrices.

No claim is made here that any off-the-shelf commutator theorem already gives
the required trace limit.

## 8. Immediate next gate

The next calculation should express

    tau(R B R)

and

    tau(R B R B R)

directly in terms of:

- diagonal values of R;
- the rank-two displacement generators of R;
- the scalar current-block exponential vector u_y.

If successful, the bivariate transition measure Gamma is replaced by a small
set of scalar grid sums.

That is the active LRSC-assisted attack.

No unconditional >79 theorem is claimed.
