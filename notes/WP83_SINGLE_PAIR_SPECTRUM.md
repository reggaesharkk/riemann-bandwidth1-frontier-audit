# WP83 — exact spectrum of one off-line Gabor pair

Date: 2026-10-04
Status: **FULL-GRID SINGLE-PAIR SPECTRUM CLOSED EXACTLY; FINITE-WINDOW GLOBALIZATION STILL OPEN**

This is the first positive piece of the Proposition-R reconstruction.

## 1. Setup

Let z be the complex spectral ordinate associated with an off-critical-line zero, with

    |Im z| = delta = |beta-1/2|.

On the full critical-density Gabor grid define

    u_z = (phi_hat(z-tau_k))_{k in Z}.

Since phi is real and even, u_conj(z)=conj(u_z).

C26 Lemma 2.2 extends analytically in the spectral variables and gives

    sum_k phi_hat(z-tau_k) phi_hat(w-tau_k)
      = L Phi(z-w).

## 2. Two exact scalar identities

Put

    N_delta := ||u_z||^2,
    C0      := sum_k u_z(k)^2.

Using w=conj(z) in the analytically continued Poisson identity,

    N_delta = L Phi(z-conj(z)) = L Phi(2 i Im z).

Using w=z,

    C0 = L Phi(0) = a L^2.

C0 is real.

Write

    u_z = a_vec + i b_vec

with real vectors a_vec,b_vec. Then

    C0 = ||a_vec||^2 - ||b_vec||^2 + 2 i <a_vec,b_vec>.

Therefore, exactly,

    <a_vec,b_vec> = 0,

    ||a_vec||^2 = (N_delta+C0)/2,
    ||b_vec||^2 = (N_delta-C0)/2.

Thus the real and imaginary parts of the off-line evaluation vector are automatically orthogonal on the full critical Gabor grid.

## 3. Exact pair eigenvalues

The pair contribution for multiplicity m is

    H_z = m( u_z u_z^T + conj(u_z) conj(u_z)^T )
        = 2m( a_vec a_vec^T - b_vec b_vec^T ).

Since a_vec and b_vec are orthogonal, its two nonzero eigenvalues are exactly

    boxed:
    lambda_plus  = m( N_delta + C0 ),
    lambda_minus = -m( N_delta - C0 ).

For delta>0, evenness and nonnegativity of phi^2 give

    Phi(2 i delta) = integral phi(u)^2 cosh(2 delta u) du > Phi(0),

so N_delta>C0 and the pair has genuine signature (1,1).

This gives an explicit quantitative version of the signature statement, not merely inertia.

## 4. Growth with depth

Because phi=1 on the plateau [-L/2+w,L/2-w], for fixed delta>0 the integral Phi(2 i delta) contains an endpoint contribution of size

    exp(delta*L - O(delta*w)).

Hence, in the endpoint regime w/L->0,

    N_delta = X^(delta-o(1)) * polylog(X),

and therefore

    |lambda_plus|, |lambda_minus| = X^(delta-o(1)).

Consequently the Frobenius self-pair scale is

    ||H_z||_F^2 = X^(2 delta-o(1)),

matching C26 Remark 5.10.

## 5. What this proves for Proposition R

A single isolated off-line pair at fixed depth delta really does carry a pair of polynomially large eigenvalues. The remaining issue is not the pair itself.

The only missing step is **globalization**: prove that after adding all other zero contributions and restricting from the full grid to the finite active Gabor window, at least one eigenvalue of comparable polynomial size survives.

This sharply localizes Proposition R:

    single-pair growth: CLOSED,
    single-pair signature: CLOSED,
    full-grid quantitative spectrum: CLOSED,
    finite-window multi-pair anti-cancellation: OPEN.

## 6. Endpoint handling

C26 itself warns that individual pair traces may be distorted near the ends of a fixed [T,2T] compression. A Proposition-R proof may therefore choose a dyadic window placing the target zero a fixed distance from both Gabor endpoints, or prove a uniform finite-window recovery estimate.

That endpoint step must be explicit; the full-grid formula alone is not enough.
