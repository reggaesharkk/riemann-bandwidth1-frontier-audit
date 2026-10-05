# WP84 — endpoint ramp quarantine via a common prolate boundary subspace

Date: 2026-10-05

Status: **RAMP ENDPOINT LOW-RANK + SMALL-NORM QUARANTINE CLOSED, CONDITIONAL ONLY ON A STANDARD PUBLISHED DPSS EIGENVALUE-CONCENTRATION THEOREM**

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

Thus the ramp changes only the weight. Compact support preserves the exact
shift support.

## 2. Common boundary strips for endpoint shifts

Fix W>0 and suppose

    y >= L-W.

A nonzero term requires both x and x+y in [-L/2,L/2]. Therefore

    x in I_left
      := [-L/2,-L/2+W],

and

    x+y in I_right
      := [L/2-W,L/2].

Hence every endpoint block in the entire range y>=L-W factors through the
same pair of boundary strips.

After the common carrier gauge is removed, the total complex endpoint
operator has the exact factorization

    E_plus
      = T_left^* K_W T_right,

where

    T_I := M_I P_d

is the time-restriction map from the d-mode Fourier space to L2(I), and K_W
is the weighted-translation sum between the two boundary strips.

The real endpoint operator is E_plus+E_plus^*.

## 3. The concentration matrix is exactly a DPSS prolate matrix

For a strip I of length W,

    Q_I := T_I^* T_I
         = P_d M_I P_d.

After rescaling x=L t and translating I to start at zero,

    (Q_I)_{kl}
      = int_0^(W/L) exp(i2*pi(l-k)t) dt.

Up to a harmless diagonal phase from interval translation, this is exactly
the standard d by d prolate Toeplitz matrix with DPSS bandwidth

    W_DPS = W/(2L).

Therefore the published nonasymptotic DPSS eigenvalue-concentration bounds
apply directly.

A suitable source is:

    S. Karnik, J. Romberg, M. A. Davenport,
    "Improved bounds for the eigenvalues of prolate spheroidal wave functions
    and discrete prolate spheroidal sequences",
    Applied and Computational Harmonic Analysis 55 (2021), 97--128.

Their nonasymptotic Theorem 2 gives, for epsilon in (0,1/2),

    #{j: epsilon < lambda_j(Q_I) < 1-epsilon}
      <= (2/pi^2) log(100 d W_DPS + 25)
           log(5/[epsilon(1-epsilon)])
         + 7,

with

    W_DPS=W/(2L).

Thus in the present regime the transition width is

    O(log(d W_DPS) log(1/epsilon)).

## 4. Rank of the epsilon-concentrated boundary subspace

Let Pi_I be the spectral projection of Q_I onto eigenvalues >epsilon.

Since

    tr Q_I = d W/L,

the number of eigenvalues above 1-epsilon is at most

    d W/[L(1-epsilon)].

Adding the transition-width bound gives

    rank(Pi_I)
      <= d W/[L(1-epsilon)]
         + O(log d * log(1/epsilon)).

On the complementary subspace,

    ||T_I(I-Pi_I)||op
      <= sqrt(epsilon).

This is the exact approximation interface needed below.

## 5. Crude middle-operator norm is only polynomial in T

The already-closed prime-block norm gives

    ||B_n||op
      <= 4 Lambda(n)/(L sqrt(n)).

Using only Lambda(n)<=log n and X<=T^(1+o(1)),

    ||K_W||op
      <= sum_{n<=X} O(Lambda(n)/(L sqrt(n)))
      <= T^(1/2+o(1)).

No prime cancellation is used.

## 6. Choose polynomially tiny concentration error

Take

    epsilon=T^(-A)

with any fixed A>2.

Choose

    W=K log L

with fixed K.

Since d asymp T L,

    rank(Pi_I)/d
      <= O(W/L)
         + O(log d * log T / d)

      = O(log L/L)+o(1)
      = o(1).

Also

    ||T_I(I-Pi_I)||op
      <= T^(-A/2).

## 7. Low-rank plus small-norm decomposition

Insert Pi_left and Pi_right into

    E_plus=T_left^* K_W T_right.

Define the main piece by retaining the high-concentration subspaces on both
sides. Its rank is at most

    rank(Pi_left)+rank(Pi_right)
      = o(d).

Every complementary term contains at least one factor

    T_I(I-Pi_I),

so its operator norm is

    O(||K_W|| sqrt(epsilon))
      <= T^(1/2+o(1)-A/2)
      = o(1).

Therefore

    boxed:
    E_endpoint
      = E_rank + E_small,

with

    rank(E_rank)/d=o(1),
    ||E_small||op=o(1).

This conclusion is independent of the signs and sizes of the individual
endpoint coefficients beyond the crude polynomial norm bound above.

## 8. Prime cutoff consequence

The condition

    y>=L-K log L

is exactly

    n>=X/L^K.

Hence the **actual ramp-taper endpoint prime family**

    n in [X/L^K, X]

may be removed at o(1) bounded spectral cost:

- E_rank is invisible by rank stability;
- E_small is invisible by the fixed nonreal resolvent identity.

No endpoint prime cancellation is required.

## 9. Strategic gain

After this quarantine the active arithmetic range is

    n<=X/L^K.

K may be chosen after a fixed logarithmic loss budget.

Therefore any later retained-range bounded-resolvent estimate with an L^C
loss can choose K>C before beginning the arithmetic analysis.

This closes the endpoint geometry that previously contaminated the
large-shift regime.

No unconditional >79 theorem is claimed.


## 10. Precision-budget check

The possible failure mode is that the concentration threshold needed to beat
the crude middle-operator norm might make the DPSS transition rank too large.

Here it does not.

With

    d asymp T L/(2*pi),
    W=K log L,
    W_DPS=W/(2L),

we have

    d W_DPS
      asymp T log L.

Choose

    epsilon=T^(-A)

with fixed A>2.  Then

    log(d W_DPS)=O(L),
    log(1/epsilon)=O(L).

The explicit DPSS transition bound therefore gives only

    O(L^2)

transition directions.

Since

    d asymp T L,

their rank fraction is

    O(L/T)=o(1).

So the polynomially small concentration precision needed for
`||E_small||=o(1)` is fully compatible with an o(d) deleted subspace.
