# WP84 — smooth background scalarization in normalized trace norm

Date: 2026-10-04

Status: **LEADING SCALAR BACKGROUND DERIVED FROM SOURCE-CLOSED STIRLING / Pi / TAPER DECAY; MACHINE FORMALIZATION OPEN**

The permutation-Lindeberg process should start from the non-prime background

    S = H_mu + H_Pi

in hat units. This note shows that, for the bounded-resolvent statistic, S may be replaced by a scalar multiple of the identity at o(1) normalized trace-norm cost.

## 1. Gram operator notation

Let

    (Wc)(tau)=L^(-1/2) sum_{k<d} c_k phihat(tau-tau_k).

Then

    H_mu^tilde = W* M_mu W,
    H_Pi^tilde = W* M_Pi W,

and hat units divide by a_phi L.

The unweighted Gram is

    W*W = C(0).

For the sharp flat taper,

    C_sharp(0)=2*pi I.

For the actual width-w taper, the edge-support Hilbert--Schmidt argument from `WP84_VARIANCE_RAMP_TRANSFER.md` gives

    ||C(0)-2*pi I||_1/d
      <= ||C(0)-2*pi I||_F/sqrt(d)
      = O(sqrt(w/L)).

With headline w=1 this is o(1).

## 2. Choose the scalar density

Put

    mu_bar = ell1(T)/(2*pi).

The source-closed Stirling estimate says

    mu(tau)=(1/(2*pi)) log(|tau|/(2*pi)) + O(tau^(-2)).

On the main spectral strip

    tau in [T/2,3T],

we therefore have uniformly

    |mu(tau)-mu_bar| = O(1).

The constant part contributes

    (mu_bar/(a_phi L)) C(0)
      = (ell1/(a_phi L)) I + E_edge,

with

    ||E_edge||_1/d = O(sqrt(w/L)).

## 3. Main-strip mu residual is O(1/L) in operator norm

On the main strip the multiplication symbol

    q(tau)=mu(tau)-mu_bar

is uniformly O(1). Since ||W||^2=||C(0)||op<=2*pi,

    || W* M_q W ||op <= O(1).

After division by a_phi L,

    boxed:
    ||E_mu,main||op = O(1/L).

Thus its normalized trace norm is also O(1/L).

## 4. Mu tail is power-small

The public taper bounds give, on the real line,

    |phihat(r)| <= C_phi/(1+r^2)

with a T-uniform profile constant.

For tau outside [T/2,3T] and every grid center tau_k in [T,2T], the distance is at least a constant multiple of T at the nearest boundary and then grows linearly.

Using Cauchy--Schwarz in the coefficient vector,

    |Wc(tau)|^2
      <= ||c||^2/L * sum_k |phihat(tau-tau_k)|^2.

Since d is asymptotic to T L/(2*pi), integration of the r^-4 tail against the logarithmic growth of mu gives

    || W* M_{(mu-mu_bar) 1_tail} W ||op
      = O(log T / T^2)

up to a profile constant.

After division by a_phi L this is negligible.

Only the power of T matters here; exact optimization of the constant is unnecessary.

## 5. Pi background is smaller still

The formal source proves

    |Pi_X(tau)| <= 3 sqrt(X)/(1+|tau|).

On [T/2,3T],

    sup |Pi_X| = O(sqrt(X)/T).

Hence

    ||H_Pi^hat||op
      = O(sqrt(X)/(T L))

on the main strip.

The off-strip contribution uses the same r^-4 Gabor tail and is

    O(sqrt(X)/T^2)

before the harmless 1/L normalization.

For lambda<=1, X=T^(lambda+o(1)), both terms are o(1).

## 6. Background conclusion

Combining the pieces gives

    boxed:
    S_hat
      = s0(T) I + E_S,

with

    s0(T)=ell1(T)/(a_phi(T) L(T)),

and

    boxed:
    ||E_S||_1/d = O(sqrt(w/L)) + O(1/L) + o(1) = o(1).

For lambda=1 and the standard fixed-width taper,

    s0(T) -> 1.

## 7. Resolvent consequence

For z on the fixed circle Gamma_rho, the resolvent identity gives

    |tau_d((S_hat-zI)^(-1)) - (s0-z)^(-1)|
      <= (1-rho)^(-2) * ||E_S||_1/d
      = o(1).

So the Lindeberg flow starts from a scalar resolvent, not an unknown matrix-valued background.

## 8. What remains

This does not prove ALG-star through the prime-block evolution. It removes the **initial-condition** part of ALG-star.

The active closure problem is now:

    scalar initial resolvent
      + infinitesimal modulated-Toeplitz prime blocks
      + sharp mixed covariance K(x,u)=|x-u|
      -> prove permutation-averaged resolvents remain asymptotically in the multiplication algebra.

That is the remaining noncommutative step.