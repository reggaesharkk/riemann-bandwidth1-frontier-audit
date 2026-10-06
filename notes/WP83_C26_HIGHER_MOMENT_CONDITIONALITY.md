# WP83 — C26 conditionality cross-check for the fourth-moment route

Date: 2026-10-04
Status: **SOURCE-LEVEL BARRIER CONFIRMED; no unconditional m4 transport may be treated as routine**

## 1. What the two-thirds framework actually says

The original C26 paper explicitly separates the unconditional bandwidth-one theorem from higher moments.

In its limits-of-the-method section it states that prime-side evaluation of `tr G^k` by the diagonal method is available in the Rudnick--Sarnak range

    k*lambda < 2.

For lambda in (1/2,1), this excludes k=4. C26 then introduces a **conditional** hypothesis `HL*(k0,lambda)` for higher traces.

For k=4 and lambda>1/2, C26 says the missing input encodes a Hardy--Littlewood-type asymptotic for additive correlations of the form

    sum_m (Lambda*Lambda)(m) (Lambda*Lambda)(m+h),

over the relevant h-range.

It then says `HL*(4,lambda)` up to lambda->1 would yield the 13/18 simple-zero rung.

Thus the predecessor framework itself did **not** regard the fourth moment near bandwidth one as a consequence of the classical toolkit used for the first two moments.

## 2. Zero-side warning already present in C26

C26 also records that for an off-line zero pair of depth

    delta = |beta-1/2|,

the self-pair term in the zero-side expansion of the squared Frobenius norm is of size

    X^(|2 beta-1|) = X^(2 delta).

But it immediately warns that no termwise bound is available unconditionally because the complex zero-side expansion has cancelling cross terms. This is why the valid two-moment proof reads the full second moment from the prime side and uses only inertia/rank on the zero side.

Therefore a naive 'one extreme zero gives a positive huge term' proof is invalid. Any Proposition-R reconstruction must solve an aggregation/isolation problem, not merely quote the self-pair term.

## 3. Comparison with the 0.7947 successor claim

The 0.7947 paper later claimed to make the fourth moment unconditional through a polylogarithmic cell truncation plus spectral major/minor analysis.

Our independent audit and public issue #1 both identify a failure in that truncation: the claimed decaying cell parameter is undefined/collides with the global `ell_1` normalization, while the actual outer prime-power Mertens mass is not discharged by a fixed polylog cutoff.

The same program's later successor then explicitly retracted its unconditional `mu_4 -> 13/4` tier and above.

These facts are mutually consistent with the C26 boundary: the hard fourth-moment input never became routine merely by changing bookkeeping.

## 4. Consequence for this private project

The following statements remain useful but **conditional/model-side** until a genuinely new analytic theorem is supplied:

- the exact C_core and Stage-A model constants;
- exact S4 local/CRT couplings;
- exact C7 and {5,2};
- the 79.627% k<=6 consumer;
- the one-sided >80 m7/m8 consumer.

The unconditional theorem track must now be judged against the C26 `k*lambda<2` barrier and the successor's Proposition-R retraction, not against the internal completeness of our bookkeeping.

## 5. Proposition-R reconstruction status

We have two source facts:

1. C26: an individual off-line self-pair has power-law growth `X^(2 delta)` in the zero-side second-moment expansion;
2. successor retraction: a verified reviewer argument shows finite unconditional higher-even-moment bounds of the claimed strength force power-law zero-free regions.

What is **not** public is the bridge proving item 2 from the compressed-Weil matrix in the presence of all other zeros. The retraction says that proof exists in the private forward archive, but the released repository does not contain it.

So our independent Proposition-R reconstruction remains OPEN at one precise interface:

    extreme off-line witness  ->  non-cancellable lower bound on the full higher-even trace.

Until that interface is proved or evaded, we use the retraction for claim grading but do not pretend to possess an independent proof of Proposition R.
