# WP84 — endpoint ramp quarantine via a common prolate boundary subspace

Date: 2026-10-05

Status: **EXACT COMMON-BOUNDARY FACTORIZATION DERIVED; LOW-RANK APPROXIMATION REDUCED TO A STANDARD PROLATE EIGENVALUE-CONCENTRATION INPUT**

This note upgrades the sharp endpoint-shift rank observation to the actual
compactly supported ramp taper.

## 1. Exact physical representation of the complex block

Let

    e_k(x)=L^(-1/2) exp(i k (2*pi/L) x)

on the physical interval, and let P_d project onto the d consecutive Fourier
modes.

From

    Cplus(y)=(2*pi/L) D_y T_y D_y,

with

    (T_y)_{kl}=int phi(x-y/2)phi(x+y/2)
                    exp(-i(k-l)2*pi*x/L) dx,

Fourier synthesis gives the exact weighted-shift form

    Cplus(y) psi(x)
      = 2*pi exp(i T y)
          phi(x) phi(x+y) psi(x+y).

The adjoint branch is the reverse shift.

Thus the actual ramp changes only the weight.  Compact support still enforces
the same geometric shift support as the sharp block.

## 2. Common boundary strips for endpoint shifts

Fix W>0 and suppose

    y >= L-W.

Then a nonzero term requires both x and x+y to lie in

    [-L/2,L/2].

Hence necessarily

    x in I_left
      := [-L/2,-L/2+W],

and

    x+y in I_right
      := [L/2-W,L/2].

Therefore **every** endpoint block in the whole range y>=L-W factors through
the same pair of boundary strips.

After the common carrier gauge is removed, the total complex endpoint operator
has the form

    E_plus
      = P_d M_{I_left} K_W M_{I_right} P_d

for one bounded operator K_W assembled from the weighted translations.

The real endpoint operator is E_plus+E_plus^*.

## 3. Crude middle-operator norm is only polynomial in T

Using only

    Lambda(n)<=log n,
    X<=T^(1+o(1)),

and the already-closed block norm,

    ||B_n|| <= 4 Lambda(n)/(L sqrt(n)),

the absolute endpoint sum obeys

    ||K_W||
      <= sum_{n<=X} O(Lambda(n)/(L sqrt(n)))
      <= O(sqrt(X))
      <= T^(1/2+o(1)).

No prime cancellation is used.

Thus the middle operator may be large, but only polynomially large in T.

## 4. Boundary concentration operator

Put

    Q_I = P_d M_I P_d

for either boundary strip I of length W.

The nonzero singular values of

    M_I P_d

are the square roots of the eigenvalues of Q_I.

The time-bandwidth product is

    d * W/L.

Classical prolate/DPSS eigenvalue concentration says that, for
epsilon in (0,1/2), the number of eigenvalues in the plunge region is only

    O(log d * log(1/epsilon)),

while the number near one is the Shannon count

    d W/L

up to the same logarithmic correction.

A suitable nonasymptotic source is:

    S. Karnik, J. Romberg, M. A. Davenport,
    "Improved bounds for the eigenvalues of prolate spheroidal wave functions
    and discrete prolate spheroidal sequences",
    Applied and Computational Harmonic Analysis 55 (2021), 97--128.

The paper proves logarithmic transition-width bounds for both DPSS and PSWF
eigenvalues.

## 5. Choose polynomially tiny concentration error

Take

    epsilon=T^(-A)

with fixed A>2.

Let Pi_I project onto the prolate singular directions with concentration
eigenvalue > epsilon.

Then the literature bound gives

    rank(Pi_I)
      <= d W/L
         + O(log d * log T).

For

    W=K log L,
    d asymp T L,

the rank fraction is

    rank(Pi_I)/d
      = O(log L/L) + O(log T/(T))
      = o(1).

On the orthogonal complement,

    ||M_I P_d (I-Pi_I)|| <= sqrt(epsilon)=T^(-A/2).

## 6. Low-rank plus small-norm endpoint decomposition

Insert Pi_left and Pi_right into

    E_plus=P_d M_left K_W M_right P_d.

The part touching either high-concentration projection has rank

    o(d).

The complementary part has operator norm at most

    ||K_W|| * epsilon^(1/2)
      <= T^(1/2+o(1)-A/2)
      = o(1)

for any fixed A>1.

Therefore the endpoint family admits

    boxed:
    E_endpoint
      = E_rank + E_small,

with

    rank(E_rank)/d=o(1),
    ||E_small||op=o(1).

This is exactly the decomposition required by the bounded-resolvent route.

## 7. Consequence for the prime cutoff

Taking

    W=K log L

corresponds to

    y>=L-K log L

or

    n>=X/L^K.

Hence the actual ramp-taper endpoint prime family above X/L^K can be
quarantined at o(1) bounded spectral cost, provided the prolate concentration
theorem is mapped to the present Fourier normalization exactly.

This mapping is the only remaining formalization step in the endpoint gate.

## 8. Strategic gain

After endpoint quarantine, the retained prime range is

    n<=X/L^K.

K may be chosen after a fixed logarithmic loss budget.

Thus any retained-range estimate suffering an L^C loss can first choose K>C
and work away from the geometric endpoint, while the discarded layer is
handled by rank plus small norm rather than arithmetic cancellation.

No unconditional >79 theorem is claimed.
