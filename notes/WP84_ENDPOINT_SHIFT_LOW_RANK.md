# WP84 — endpoint-shift low-rank quarantine

Date: 2026-10-05

Status: **EXACT FINITE-SECTION RANK LEMMA; LARGE LONG-SHIFT COEFFICIENTS CAN BE DELETED WITHOUT NORM CONTROL**

The sharp carrier-free prime operator is a sum of non-cyclic translations.
Its longest translations have a special feature stronger than small
operator norm: they live entirely on a low-dimensional boundary subspace.

## 1. Exact finite-section lemma

Let S_r be the N by N non-cyclic shift by r:

    (S_r)_{i,j}=1_{j=i+r}.

Fix M<N.  For every

    r >= N-M,

the operator S_r maps the last M coordinates into the first M coordinates,
and S_r^* maps the first M coordinates into the last M coordinates.

Therefore for arbitrary coefficients a_r,

    E_M
      = sum_{r=N-M}^{N-1}
          a_r (S_r+S_r^*)

has support inside

    span{e_1,...,e_M,e_{N-M+1},...,e_N}.

Hence

    boxed:
    rank(E_M) <= 2M.

The bound is independent of the sizes and signs of the coefficients a_r.

Companion exact gate:

    src/wp84_endpoint_shift_low_rank.py

## 2. Continuum interpretation

For a sharp translation U_s on [0,1], every shift with

    s >= 1-epsilon

acts only between the two boundary strips

    [0,epsilon],
    [1-epsilon,1].

Thus the entire endpoint-shift family is confined to a boundary subspace of
relative dimension O(epsilon) after finite-section discretization.

## 3. Prime cutoff translation

In the sharp prime model

    s_n = log n / L,
    X = exp(L).

Choose

    epsilon = W/L.

Then

    s_n >= 1-W/L

is exactly

    n >= X exp(-W).

All prime blocks in that endpoint range, regardless of their total
coefficient mass, form an O(W/L)-rank-fraction perturbation in the sharp
finite-section model.

For

    W=K log L

with fixed K,

    rank fraction = O(log L/L)=o(1),

while the endpoint cutoff becomes

    n >= X/L^K.

## 4. Rank-robust consequence

For the bounded F61 consumer, or for any fixed nonreal Stieltjes probe, this
endpoint family may be removed at o(1) normalized spectral cost by the rank
inequality alone.

No estimate of its operator norm is needed.

This is important because the long-shift coefficients can be large in
aggregate even though their geometric support is small.

## 5. Interaction with logarithmic losses

Removing

    n in [X/L^K, X]

gains an arbitrary fixed power of L in endpoint-amplified coefficient scales
while paying only o(1) spectral rank.

Therefore any later bounded-resolvent estimate whose retained-prime error has
a fixed L^C loss may choose K after C and quarantine the endpoint layer first.

This is a theorem architecture, not yet the full arithmetic proof: the ramp
taper and finite Gabor compression must be shown to preserve the same
rank-negligible endpoint geometry up to o(1).

## 6. New subgate

Prove the endpoint-rank statement for the actual ramp-taper Gabor blocks:

    sum_{n>=X/L^K} B_n
      = E_rank + E_small,

with

    rank(E_rank)/d=o(1),
    ||E_small||_1/d=o(1)

for fixed K chosen after the logarithmic loss budget.

If this closes, the active F61 theorem can work only with the retained range

    n <= X/L^K,

while the dangerous endpoint layer is removed by rank rather than
cancellation.
