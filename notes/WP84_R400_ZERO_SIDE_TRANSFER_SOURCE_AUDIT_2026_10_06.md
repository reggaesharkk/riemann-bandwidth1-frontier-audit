# WP84 — R=400 zero-side transfer source audit (2026-10-06)

Status: **CONDITIONAL LEDGER ARITHMETIC CHECKED; ACTUAL ZERO-SIDE MATRIX TRANSFER NOT ESTABLISHED BY THE AUDITED SOURCES**

Audit basis: PR #5, branch `research/frontier-7962-hostile-audit-v0.1`, head `38a97ecc332bfc96ca595a95ab1016c365b72fb4`.

## 1. What checks exactly

The R=400 notes give the conditional defect bound
`D <= 0.15589863406625 + o(1)`. Its arithmetic consequence is
`1-2D >= 0.6882027318675 - o(1)`, or
`68.82027318675% - o(1)`.

The integer implication used by the zero-side consumer is valid: if
`n_+ <= s1+s2+p` and `s1+2s2+2p <= N`, then
`s1 >= 2*n_+ - N`. The companion script
`src/wp84_simple_from_posindex_ledger.py` checks this integer implication
over a finite set of values. It does not prove either premise for the actual
compressed Weil matrix.

The R=400 quartic, pair, word-ledger, and endpoint calculations remain
conditional on their cited analytic inputs. The good-endpoint scale calculation
is consistent: with `U ~ epsilon_L T`, `N <= T^2`, and `d' ~ TL`,
the stated mean-square argument produces endpoint debt
`O(1/(epsilon_L L))=O(L^{-1/2})` for `epsilon_L=L^{-1/2}`.

## 2. Missing zero-side theorem statements

The zero-side consumer note
`notes/WP84_BOUNDED_RESOLVENT_CONSUMER.md` labels the following as coming
from a “source-closed block structure”:
`n_+(Ahat) <= s1+s2+p` and
`s1+2s2+2p <= N(I')`. The note supplies the algebra after these
inequalities, but the audited source set does not supply their derivation for
the actual matrix, interval, and zero multiplicities used by the R=400
assembly.

The related bounded-resolvent route also invokes a “tail-Weyl interface” to
compare a thresholded positive index of `Ghat` with that of `Ahat`. The
consumer notes state the interface but do not give the operator decomposition,
the error norm or rank bound, or the threshold sequence needed to verify it
for the same finite sections and normalization.

Before the R=400 coefficient can be called an unconditional simple-zero
bound, the record needs a source-level proof of:

1. the matrix-to-zero block inequality for the actual compressed zero-side
   matrix, including multiplicities and off-line reflection pairs;
2. the matching count inequality on the same interval, including boundary
   zeros and endpoint conventions;
3. the finite-section tail/truncation comparison, with its norm or rank error
   and threshold tending to zero in the normalization used by the positive
   index;
4. compatibility of these statements with the exact dimension (N(I'))
   and the prime-side matrix trace appearing in the R=400 assembly.

These are proof obligations, not finite-arithmetic checks. No unconditional
simple-zero theorem follows until they are proved or replaced by a complete
source-verified transfer.

## 3. Claim boundary

The repository supports the exact conditional statement
`if the R=400 prime-side bound and the zero-side transfer hold with the
recorded normalizations, then the displayed coefficient follows`.

It does not yet support the unconditional R=400 simple-zero proportion.
The >79% Christoffel route has its separate open large-`T` arithmetic
resolvent-state estimate; this audit does not alter that status.
