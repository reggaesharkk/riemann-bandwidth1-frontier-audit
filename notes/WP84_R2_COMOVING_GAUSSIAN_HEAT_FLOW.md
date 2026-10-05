# WP84 — co-moving scaled-r2 Gaussian heat-flow kill gate

Date: 2026-10-05

Status: **EXACT FINITE-d GAUSSIAN IDENTITY; DETERMINISTIC PRIME DRIFT AND BERNOULLI TRANSPORT REMOVED FROM THE SCALED-r2 CONSUMER**

No unconditional zero-density percentage is claimed here.

The scaled-r2 consumer

    r_{2,a}(x)
      = 1 - [ (x-a)^2/(x^2+a^2) ]^2

with a=3/2 is currently the cleanest first-record candidate.

The Bernoulli drift-elimination identity already removed the independent D1
arithmetic.  The Gaussian bridge allows one more exact simplification:
transport the **test function itself** along the background characteristic.

The result is a pure additive Gaussian heat flow around the deterministic
endpoint matrix.

No separate prime drift remains anywhere in the identity.

## 1. Gaussian bridge

After background scalarization write

    H_t
      = s0 I
        + t P
        + sqrt(t(1-t)) W,

where:

- P is the deterministic retained sharp prime operator;
- W is the circular/quadrature Gaussian sharp operator;
- E W = 0;
- its covariance is the already-closed mixed-sign variance map.

At t=1,

    H_1=s0 I+P

is the deterministic endpoint.

## 2. Co-moving test function

Let f be any fixed C^2 rational function with poles away from R.

For 0<t<=1 define

    boxed:
    f_t(x)
      =
      f(
        s0 + (x-s0)/t
      ).

Then

    boxed:
    t partial_t f_t(x)
      + (x-s0) partial_x f_t(x)
      = 0.

Thus f_t is transported exactly along the characteristic of the
drift-eliminated Bernoulli/Gaussian equation.

## 3. Exact cancellation of the deterministic drift

For the Gaussian bridge and a fixed test g, Gaussian integration by parts
gives the exact functional identity

    t d/dt E tau g(H_t)

      =
      E tau[
        (H_t-s0 I) g'(H_t)
      ]

      - (t/2)
        E sum_j
          D^2[tau g(H_t)]
            [E_j,E_j],

where W=sum_j g_j E_j is any real Gaussian Hermitian decomposition.

Now put g=f_t and include the explicit t derivative of the test function.

The transport equation from Section 2 cancels the first term exactly.

Hence

    boxed:

    d/dt
      E tau f_t(H_t)

      =
      - 1/2
        E sum_j
          D^2[tau f_t(H_t)]
            [E_j,E_j].

This is exact at finite d for the scalar background model.

The actual background differs from s0 I by normalized trace-norm o(1), so
the active bounded consumer inherits the same equation with the already
closed o(1) background error.

## 4. Equivalent additive-noise formulation

Define

    u=(1-t)/t.

Then

    s0 + (H_t-s0 I)/t
      =
      s0 I + P + sqrt(u) W
      =
      H_1 + sqrt(u) W.

Therefore

    boxed:

    E tau f_t(H_t)

      =
      Phi_f(u)

      :=
      E tau f(
        H_1 + sqrt(u) W
      ).

So the co-moving bridge is simply the Gaussian heat flow of the endpoint
matrix.

There is no mean path left.

For every fixed finite section,

    boxed:
    d/du Phi_f(u)

      =
      1/2
      E sum_j
        D^2[
          tau f(
            H_1+sqrt(u)W
          )
        ][E_j,E_j].

The two forms are identical because

    du/dt = -1/t^2

and the Hessian of f_t scales by t^(-2).

## 5. Apply to the scaled-r2 consumer

Take

    a=3/2,

    f(x)=r_{2,a}(x).

The exact partial fraction identity is

    f(x)
      =
      a(2+i)/(x-ia)
      - a^2/(x-ia)^2

      + a(2-i)/(x+ia)
      - a^2/(x+ia)^2.

Define the Gaussian-regularized Stieltjes transform

    m_u(z)
      =
      E tau(
        H_1 + sqrt(u)W - zI
      )^(-1),

and the mixed-covariance scalar

    C_u(z)
      =
      partial_u m_u(z)

      =
      E tau(
        R_u V_mix(R_u) R_u
      ).

Then

    boxed:

    Phi_r2(u)
      =
      2 Re[
        a(2+i)m_u(ia)
        - a^2 partial_z m_u(ia)
      ],

and

    boxed:

    Phi_r2'(u)
      =
      2 Re[
        a(2+i) C_u(ia)
        - a^2 partial_z C_u(ia)
      ].

Thus the entire first-record theorem can be expressed at a **single
upper-half-plane point**

    z=3i/2

plus one z derivative.

## 6. Infinite-noise boundary

The function r_{2,a} is bounded and

    r_{2,a}(x) -> 0
    as |x|->infinity.

For each fixed finite section, the Gaussian quadrature matrix W is almost
surely invertible once one retained small-shift cosine direction is
invertible; for large L the p=2 cosine direction is a nonzero perturbation
of the identity, so the determinant polynomial is not identically zero.

Therefore, for fixed d,

    boxed:
    Phi_r2(u) -> 0
    as u->infinity

by dominated convergence.

The theorem-grade large-d use must keep the order of limits explicit; this
finite-d boundary statement alone is not yet a uniform-in-d anti-concentration
theorem.

## 7. One-point heat-flow kill gate

At finite d,

    Phi_r2(0)
      =
      - int_0^infinity
          Phi_r2'(u) du.

Hence

    boxed:

    tau r_{2,3/2}(H_1)

      =
      -2 Re
        int_0^infinity
          [
            a(2+i) C_u(ia)
            - a^2 partial_z C_u(ia)
          ] du,

    a=3/2,

subject only to the finite-d boundary just stated.

The audited record is beaten if the large-d limit of the left side exceeds

    q_rec
      = (1+0.673500037)/2
      = 0.8367500185.

The model benchmark is

    q_model
      = 0.8532541156027985...,

leaving margin

    0.0165040971027985....

So the new theorem target is:

> prove the one-point integrated mixed-covariance curvature is negative
> enough to give Phi_r2(0)>0.8367500185, with total analytic error below
> 0.0165040971.

## 8. Why this is smaller than the previous state problem

The previous frontier involved

    t in [0,1]
      x Bernoulli/Gaussian state
      x deterministic mean tP
      x a second-order covariance functional.

The co-moving representation removes both:

- the explicit deterministic drift;
- the moving mean tP.

The endpoint matrix H_1 appears only as the fixed center of an additive
Gaussian heat flow.

For the scaled-r2 rung the exposed analytic object is now only

    C_u(3i/2),
    partial_z C_u(3i/2),

integrated over u>=0.

No four-pole system is needed.

## 9. Evidence boundary

Closed here:

- exact finite-d co-moving transport identity;
- exact equivalence to additive Gaussian heat flow;
- exact one-point/double-pole representation;
- exact finite-d infinite-noise boundary.

Still open:

1. a uniform-in-d large-u boundary / anti-concentration estimate, or an
   alternate truncation argument avoiding exchange of limits;

2. a one-sided estimate for the integrated covariance curvature at z=3i/2
   strong enough to fit the 0.0165040971 record margin;

3. insertion of the already-closed background/taper/rank errors.

This is now the preferred first-strike formulation for the scaled-r2 rung.

See:

    notes/WP84_SCALED_R2_RECORD_RUNG.md
    notes/WP84_BERNOULLI_DRIFT_ELIMINATION.md
    notes/WP84_BERNOULLI_GAUSSIAN_INVARIANCE.md
    notes/WP84_GAUSSIAN_COVARIANCE_HADAMARD.md


## 10. Correction to the finite-d invertibility argument

The phrase in Section 6 saying that the p=2 cosine direction is an
operator-norm perturbation of the identity is not needed and should not be
used.  The Fourier band dimension grows with T, so small normalized shift
does not by itself imply operator-norm closeness to I.

The correct finite-d argument is as follows.

For one retained sharp shift s in (0,1), the positive branch matrix can be
written

    A_s = G_s D_s,

where D_s is diagonal unitary and G_s is the Gram matrix of the first d
Fourier exponentials restricted to an interval of length 1-s.

The restricted exponentials remain linearly independent on every interval
of positive length, hence

    G_s > 0

and A_s is invertible.

Its two Hermitian quadratures are

    C_s=A_s+A_s^*,
    S_s=i(A_s-A_s^*).

For real theta,

    cos(theta) C_s + sin(theta) S_s
      =
      exp(i theta) A_s
      + exp(-i theta) A_s^*.

The determinant of this matrix is a nonzero trigonometric polynomial in
theta, because its highest and lowest Fourier coefficients contain
det(A_s) and det(A_s^*), both nonzero.

Therefore some real quadrature combination is invertible.  Hence the
determinant polynomial of the full Gaussian quadrature matrix W is not
identically zero in its Gaussian coordinates.  Since the zero set of a
nonzero real polynomial has Lebesgue measure zero,

    boxed:
    W is invertible almost surely

for every fixed finite section.

This supplies the correct justification for the fixed-d boundary

    Phi_r2(u) -> 0
    as u->infinity.

The uniform-in-d boundary issue remains open exactly as stated in Section 9.
