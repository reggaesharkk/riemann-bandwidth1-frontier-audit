# WP84 — global ramp-to-sharp quarantine by fixed boundary channels

Date: 2026-10-05

Status: **ACTUAL RAMP PRIME OPERATOR = SHARP PRIME OPERATOR + o(d)-RANK + o(1)-NORM PERTURBATION**

This note uses the self-contained boundary-quadrature lemma to upgrade the
old variance-only ramp transfer.

The result applies to the **entire prime operator**, so it covers the
first-order drift and all bounded spectral consumers at once.

## 1. Exact gauged physical blocks

Let

    I=[-L/2,L/2],
    chi=1_I,

and let phi be the actual taper, with

    0<=phi<=chi,
    phi=1

away from the two boundary ramps of width w.

After the common carrier gauge, the positive-shift complex block is exactly

    A_y
      = M_phi U_y M_phi,

where

    (U_y f)(x)=f(x+y).

The sharp block is

    S_y
      = M_chi U_y M_chi.

The negative-shift branch is the adjoint.

Put

    r=chi-phi.

Then r is supported on the fixed boundary set

    B
      = [-L/2,-L/2+w]
        union
        [L/2-w,L/2],

with total length 2w, and 0<=r<=1.

The exact block difference is

    boxed:
    A_y-S_y
      = - M_r U_y M_chi
        - M_chi U_y M_r
        + M_r U_y M_r.

Every term contains the **same fixed boundary multiplier M_r**.

This is the key point.

## 2. Sum every prime block before estimating

In hat normalization the sharp carrier-free prime operator has the form

    P_sharp
      = - sum_{n<=X}
          c_n (S_{y_n}+S_{y_n}^*),

where

    y_n=log n,
    c_n=Lambda(n)/(a L sqrt(n)),

up to the already fixed sign convention.

Define the full translation sum

    K_+
      = sum_{n<=X} c_n U_{y_n},
    K_- = K_+^*.

Then the **complete** positive-branch ramp error is

    D_+
      = - M_r K_+ M_chi
        - M_chi K_+ M_r
        + M_r K_+ M_r,

and the real error is

    D=D_+ + D_+^*.

Thus we do not pay a separate boundary approximation for every prime.

## 3. The middle operator is only polynomially large

Using

    a>=1/2,
    Lambda(n)<=log n,

we have

    ||K_+||op
      <= sum_{n<=X}|c_n|

      <= (2/L)
          sum_{n<=X} log(n)/sqrt(n)

      <= C sqrt(X)

      <= T^(1/2+o(1))

for X<=T^(1+o(1)).

No prime cancellation is used.

## 4. Fixed boundary multiplier has o(d) effective rank

Let P_d be the d-mode Fourier projection and define

    A_B=M_r P_d.

Then

    A_B^*A_B
      = P_d M_{r^2} P_d
      <= P_d M_B P_d
      = Q_B.

The boundary set B is the union of two intervals of length w.

Apply the self-contained p-node boundary quadrature to each interval with

    Z_w=pi(d-1)w/L,

    p_w=ceil(e Z_w).

For one interval the concentration error is

    epsilon_w
      <= (T w/pi) 4^(-p_w).

For their union there is a positive rank-at-most 2p_w approximation with

    ||Q_B-R_B||op
      <= 2 epsilon_w.

Hence

    lambda_{2p_w+1}(Q_B)
      <= 2 epsilon_w.

By monotonicity under

    A_B^*A_B <= Q_B,

there is a projection Pi_B of rank at most 2p_w such that

    boxed:
    ||A_B(I-Pi_B)||op
      <= delta_B
      := sqrt(2 epsilon_w).

Moreover

    rank(Pi_B)/d
      <= 2e*pi*w/L + o(1).

For fixed w=1 this is O(1/L)=o(1).

## 5. Compress the complete ramp error

Work on the d-dimensional Fourier space and compress D by P_d.

Every term in D contains A_B or A_B^* on at least one side.

Insert

    I=Pi_B+(I-Pi_B)

at each boundary occurrence.

Collect all terms touching Pi_B into D_rank.

Because each such term factors through an at-most 2p_w dimensional boundary
space and there are only finitely many algebraic terms,

    rank(D_rank)
      <= C0 p_w

for an absolute constant C0.

Thus

    boxed:
    rank(D_rank)/d
      = O(w/L)
      = o(1).

Every remaining term contains at least one factor

    A_B(I-Pi_B)

or its adjoint, so

    ||D_small||op
      <= C1 ||K_+||op delta_B.

Using the crude polynomial K_+ bound and

    delta_B
      <= sqrt(2Tw/pi) 2^(-p_w),

with

    p_w asymp T w,

we obtain

    boxed:
    ||D_small||op=o(1).

Therefore

    boxed:
    P_actual
      = P_sharp + D_rank + D_small,

with

    rank(D_rank)/d=o(1),
    ||D_small||op=o(1).

## 6. Bounded spectral consequence

For Hermitian matrices, an o(d)-rank perturbation changes the normalized
empirical spectral distribution by o(1), independently of perturbation size.

A vanishing operator-norm perturbation changes every fixed nonreal resolvent
trace by o(1).

Therefore the actual ramp prime operator and the sharp carrier-free prime
operator have the same asymptotic value for every bounded fixed-resolvent
consumer used in WP84.

This includes the first-order drift problem.

The previous variance-only Hilbert--Schmidt transfer is now strictly weaker
than this global statement.

## 7. What this closes

The bounded-resolvent route no longer needs separate proofs for:

- actual ramp versus sharp-flat variance;
- actual ramp versus sharp-flat drift;
- ramp leakage in any higher bounded functional-calculus consumer.

All taper-edge effects are quarantined by one fixed boundary subspace.

## 8. What remains open

This does **not** prove that the sharp intermediate resolvent is a
multiplication operator.

The active theorem debt moves cleanly to the sharp carrier-free operator

    P_sharp
      = - sum_{n<=X}
          Lambda(n)/(a L sqrt(n))
          (U_{s_n}^+ + U_{s_n}^-).

The remaining task is its bounded spectral / resolvent law, including the
mixed-sign connected state memory required by the order-four calibration.

No unconditional >79 theorem is claimed.

## 9. Cross-research interpretation

The algebra

    phi=chi-r

and the fixed boundary factor M_r is the continuous analogue of a finite
dictionary changing by a low-rank boundary-orbit update.

The useful transfer from the LRSC work is therefore not a claim about the
Riemann operator's exact rank.  It is the proof pattern:

    isolate the boundary change
      -> factor it through evaluation/restriction channels
      -> certify the channel dimension
      -> keep the untouched bulk separate.

Here the finite channel count is supplied by the explicit Gauss quadrature
rather than by an odd-ring mask.
