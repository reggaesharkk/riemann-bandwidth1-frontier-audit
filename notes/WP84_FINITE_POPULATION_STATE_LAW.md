# WP84 — exact finite-population state law for the permutation path

Date: 2026-10-05

Status: **PERMUTATION MEMORY WEIGHTS CLOSED EXACTLY; CONNECTED FOURTH-ORDER MEMORY LOCATED IN DISTINCT-LABEL SYMMETRIC WORD SUMS**

The permutation in the Lindeberg path is an analytical symmetrization of a
fixed deterministic block family.  At subset size k, the inserted set is a
uniform k-subset of the M blocks.

This gives an exact state law for every fixed noncommutative word.

## 1. Hypergeometric inclusion identity

Let

    X_S = sum_{j in S} B_j

for a uniform k-subset S of {1,...,M}.

Fix a block word

    w=(j_1,...,j_q)

and let r be the number of distinct labels appearing in w.

Then

    E_S [
      1_{j_1 in S} ... 1_{j_q in S}
    ]

depends only on those r distinct labels, so exactly

    boxed:
    alpha_r(M,k)
      = (k)_r/(M)_r,

where (n)_r is the falling factorial.

Consequently

    E tau(X_S^q)
      = sum_w
          alpha_{r(w)}(M,k)
          tau(B_{j_1}...B_{j_q}).

No independence approximation enters.

Companion exact checker:

    src/wp84_finite_population_word_weights.py

## 2. Exact one-step generator weight

The falling-factorial identity

    (k+1)_r-(k)_r
      = r (k)_{r-1}

gives

    boxed:
    alpha_r(M,k+1)-alpha_r(M,k)
      = r (k)_{r-1}/(M)_r.

Thus the one-step permutation generator automatically differentiates the
distinct-label sectors with the correct finite-population weight.

If k/M->t with fixed r,

    alpha_r(M,k)->t^r,

and the one-step coefficient is the discrete analogue of

    d(t^r)/dt = r t^(r-1).

This is the precise source of state memory in the permutation flow.

## 3. Order-four sectors

At q=4 the word multiplicity partitions are

    4          -> r=1,
    3+1        -> r=2,
    2+2        -> r=2,
    2+1+1      -> r=3,
    1+1+1+1    -> r=4.

Therefore the averaged fourth-order state has the exact form

    E tau(X_S^4)
      = alpha_1 W_4
        + alpha_2 (W_31+W_22)
        + alpha_3 W_211
        + alpha_4 W_1111,

where each W_lambda is the deterministic symmetric sum of traces of block
words with that multiplicity pattern.

The connected sector is therefore not forced to vanish when the
single-block cubic Taylor remainder vanishes.

The r=3 and r=4 symmetric word sums remain present with coefficients t^3 and
t^4 in the macroscopic subset flow.

## 4. Relation to the latest-block decomposition

The previously derived latest-block rule says:

- latest multiplicity one -> first-order insertion sector;
- latest multiplicity two -> second-order insertion sector;
- latest multiplicity at least three -> current-block cubic remainder.

The hypergeometric identity explains how these local insertion sectors
reassemble the global t^r state weights.

In particular:

- four-distinct words are generated through first-order history;
- 2+2 pair words are generated through second-order insertions;
- 2+1+1 words use both.

Therefore a nonzero connected fourth contribution can live entirely in the
exact evolving D1/D2 state even though the sum of current-block cubic
remainders is o(1).

## 5. What Phi4 provenance now reduces to

The model calibration requires

    Phi4=-1/60.

The combinatorial provenance question is no longer

    "which Taylor order creates Phi4?"

The answer is: the exact first/second insertion flow is sufficient to carry
all r=3 and r=4 state memory.

The remaining mathematical question is instead:

    do the retained arithmetic symmetric word sums
        W_211 and W_1111
    converge, together with the r=2 non-pair pieces, to the model
    partition-cyclic connected combination giving -1/60?

That is an arithmetic/translation-word limit, not a missing third/fourth
single-block Taylor term.

## 6. Bounded-theorem interpretation

This order-four identity is a calibration gate only.

For the actual F_delta theorem, the exact intermediate state enters through

    tau(f'(A_S) M1(S))

and the transition measure

    Gamma_S.

Those bounded objects contain the same finite-population memory without
requiring a finite-T raw fourth moment.

No unconditional >79 theorem is claimed.
