# WP84 — unconditional theorem-chain review (2026-10-06)

Status: **CONDITIONAL CONSUMER ARITHMETIC VERIFIED; NO UNCONDITIONAL SIMPLE-ZERO THEOREM ESTABLISHED**

Audit basis: private PR #5, branch `research/frontier-7962-hostile-audit-v0.1`,
head `4e032b97819fed050a1b3ae9fcb86b2a88932bed`.

This review follows the two usable theorem routes from the consumer calculation
back to the actual zeta-side matrix. It separates exact algebra, asymptotic
prime-matrix estimates, and zero-count transfer.

## 1. Exact consumer deductions

For the Christoffel square (g=P^2), the fixed-(\delta) consumer is
[
F_\delta(x)=\frac{(\delta+1)g(x)}{g(x)+\delta}.
]
The branch certificate gives (g(x)\ge1) for (x\le0), (F_\delta\ge0)
on the real line, and the model moment value (w_0=1415/13891). Jensen then
gives the exact model cap (h_\delta(w_0)). These facts yield a conditional
simple-zero coefficient (1-2h_\delta(w_0)), provided the matching
arithmetic trace bound and the zero-count transfer hold.

At (\delta=144), the exact cap is (205175/2001719), the conditional
coefficient is (1591369/2001719=79.5001196472\ldots\%), and the actual
trace must be below (41/400) merely to clear 79.5%. The intervening
headroom is (479/800687600\approx5.98236\times10^{-7}). This is model
headroom, not a proved arithmetic error allowance.

The zero-count arithmetic (s_1\ge2n_+-N) is correct under the recorded
block inequalities (n_+\le s_1+s_2+p) and
(s_1+2s_2+2p\le N). The companion ledger script passes. This check does
not replace the source proof that the actual zero-side matrix has those block
and tail-Weyl properties.

## 2. Frozen 68.820273% route

The R=400 notes assemble a bounded two-pole consumer, a fixed-band quartic
majorant, the complete pair layer, and the connected-sector endpoint estimate.
The committed deterministic gates were rerun at the audited head:

- exact R=400 pair layer: (	exttt{WP84\_R400\_PAIR\_LAYER\_PASS});
- same-normalization replay: (	exttt{WP84\_R400\_SAME\_NORMALIZATION\_REPLAY\_PASS});
- first-record assembly: (	exttt{WP84\_R400\_FIRST\_RECORD\_ASSEMBLY\_PASS});
- simple-zero ledger: (	exttt{WP84\_SIMPLE\_FROM\_POSINDEX\_LEDGER\_PASS});
- exact connected-kernel vertex sign gate:
  (	exttt{WP84\_PHI4\_POINTWISE\_NONPOSITIVE\_PASS}).

An independent rational-polynomial replay also verified the matched quartic
identity and used an exact Fraction Sturm chain to confirm that its difference
from (g_{match}) has no real zero and is positive on the real line.

These checks support the recorded internal arithmetic
(\,\ge68.82027318675\ldots\%-o(1),) **if** the cited uniform
asymptotic lemmas and zero-side transfer are valid with their stated
normalizations. The scripts verify fixed algebra and rational calculations;
they do not establish those asymptotic lemmas.

## 3. Source and normalization boundary

The R=400 assembly itself names the remaining hostile-audit obligations:

1. the balanced-product endpoint feature second-mass normalization and the
   mean-square selection of the two endpoints;
2. uniform second-covariance normalization on the data-selected principal
   section;
3. the full-to-band resolvent tail estimate with the matched-consumer
   residues and (q_\alpha=1/4+o(1));
4. the zero-side block, threshold, and tail-Weyl transfer used to turn the
   prime-side spectral statistic into the simple-zero count.

The mean-square selection calculation is consistent with the stated scales:
(N\le T^2), candidate interval (U\asymp T L^{-1/2}), section dimension
(d'\asymp TL), and endpoint contribution (O(L^{-1/2})), provided the
finite-feature coefficient second-mass bound is uniform exactly as stated.
That uniform feature bound and its insertion in the complete connected ledger
remain source-level proof obligations, not consequences of the endpoint rate
calculation alone.

The external carrier-(2T) prime-sum estimate has a separate source-check
record in `WP84_FAST_CHANNEL_SOURCE_HOSTILE_AUDIT_2026_10_06.md). It closes
that covariance channel only; it does not evaluate the full Bernoulli
resolvent state.

## 4. Remaining theorem statements

For the 68.820273% route, theorem promotion requires completing the four
normalization/source checks in Section 3 and verifying that their hypotheses
match the actual zeta-side matrix and moving zero threshold.

For the first strict (>79.5\%) Christoffel rung, the direct open arithmetic
statement is
[
\limsup_{T\to\infty}\tau(F_{144}(H_T))
\le \frac{205175}{2001719}.
]
A weaker sufficient statement for merely (>79.5\%) is
[
\limsup_{T\to\infty}\tau(F_{144}(H_T))<\frac{41}{400}.
]
The current source notes do not prove either inequality. In particular,
Gaussian concentration of a bridge trace around its expectation does not
bound that expectation or the integrated arithmetic drift.

## 5. Conclusion

The exact model consumers and the finite rational ledgers are checked.
Neither the R=400 internal replay nor the (\delta=144) Jensen rung is an
unconditional theorem by itself. The short-term theorem path is the R=400
route, whose remaining work is a hostile source/normalization audit plus the
actual zero-side transfer. The higher Christoffel route still needs its
one-sided large-(T) resolvent-state estimate.

No unconditional zero-proportion claim is made.
