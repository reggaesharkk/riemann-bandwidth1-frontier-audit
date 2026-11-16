# WP84 — regroup the infinitesimal array by prime base

Date: 2026-10-05

Status: **PRIME-BASE GROUPING PRESERVES THE INFINITESIMAL LEDGER AND REMOVES ALL EXACT CURRENT-BASE RESONANCES FROM THE FIRST-ORDER STATE**

The prime-power Lindeberg decomposition is not unique.

A cleaner deterministic decomposition groups **all powers of one prime base**
before the permutation symmetrization.

This does not change the total matrix, but it improves the arithmetic
selection rules.

## 1. Prime-base blocks

Write the normalized Hermitian prime-power blocks as

    B_{p^a},

with the already established bound

    ||B_{p^a}||op
      <= 4 log(p)/(L p^(a/2)).

Define one Hermitian block per prime:

    boxed:
    G_p
      := sum_{a>=1, p^a<=X} B_{p^a}.

Then exactly

    sum_{p<=X} G_p
      = sum_{n<=X} B_n,

because Lambda(n) is supported on prime powers.

So the matrix and every final spectral statistic are unchanged.

## 2. Each grouped block is still infinitesimal

The geometric series gives

    ||G_p||op
      <= (4 log p/L)
          sum_{a>=1} p^(-a/2)

      <= (4 log p/L)/(sqrt(p)-1).

Therefore

    boxed:
    max_p ||G_p||op
      = O(1/L).

The square mass obeys

    sum_p ||G_p||op^2
      <= C/L^2
          sum_{p<=X} (log p)^2/p
      = O(1).

For the cubic mass,

    sum_p ||G_p||op^3
      <= C/L^3
          sum_p (log p)^3/p^(3/2)
      = O(L^-3).

The infinite prime series converges absolutely.

Hence the exact one-block resolvent remainder survives unchanged:

    boxed:
    sum_p ||G_p||op^3=o(1).

Permutation-Lindeberg may therefore be run over prime bases instead of
individual prime powers.

## 3. Exact valuation firewall for the current block

Fix a permutation of the prime-base blocks and suppose the current block is

    G_p.

The intermediate state contains only groups

    G_q,
    q != p.

Expand a finite translation word from the previous state and select one
summand from the current G_p.

That current summand carries a shift exponent

    +/- a log p,
    a>=1.

Every previous summand is a signed integer multiple of log q for primes

    q != p.

If the total displacement were zero, exponentiation would give

    p^(+/- a)
      * prod_{q != p} q^(e_q)
      = 1

with integer exponents e_q.

Unique factorization makes this impossible because the p-adic valuation is

    +/- a != 0.

Therefore:

    boxed:
    no exact closed translation word can contain the current
    prime-base group exactly once.

This is true at **every word length**.

## 4. Consequence for the first-order Lindeberg sector

For any polynomial R in the previously inserted grouped blocks,

    tau_infinite(
      R(previous groups) G_p
    )
      = 0

in the exact sharp translation trace, because every monomial has nonzero net
displacement.

Thus the first-order drift is algebraically absent in the ideal closed-word
translation law.

This is stronger than the prime-power decomposition, where a current p block
could resonate with previously inserted p^2,p^3 blocks.

Grouping by prime base removes that leakage completely.

## 5. Consequence for same-sign current-base insertions

The same selection rule sharpens the second-order branch.

Two selected summands from G_p have exponents a,b>=1.

For a same-sign pair the p-adic valuation is

    +(a+b)

or

    -(a+b),

and no previous group contains p.

Hence no exact closed word exists.

For an opposite-sign pair, exact p-adic cancellation is possible only when

    a=b.

Therefore the exact current-group second-order diagonal is automatically:

- same-sign: zero in the closed-word law;
- mixed-sign: only equal powers p^a against p^a survive exactly.

This cleanly isolates the pair covariance inside each prime-base group.

## 6. Why this does not yet prove the finite compressed drift is o(1)

The actual d-dimensional Fourier compression does not impose an exact delta
on total displacement.

A nonzero displacement is sampled by a Dirichlet/Gabor kernel of width
approximately 1/T.

Thus **near** multiplicative resonances can survive:

    |log(A/B)| <= O(1/T)

even when A/B != 1.

The grouped valuation firewall removes exact current-base resonances but does
not by itself rule out these near-resonant arithmetic tuples.

That residual near-resonance estimate is now the genuine drift theorem
obligation.

## 7. Strategic gain

The active arithmetic split becomes:

    exact diagonal / same-prime-power covariance
      -> contained inside one grouped block and source-closed;

    exact current-base first-order resonance
      -> impossible by unique factorization;

    finite-compression leakage
      -> near multiplicative resonances between distinct prime bases.

This is a materially cleaner interface for the bounded-resolvent theorem.

The new permutation should therefore use prime-base groups unless a later
calculation demonstrates a disadvantage.

No unconditional >79 theorem is claimed.
