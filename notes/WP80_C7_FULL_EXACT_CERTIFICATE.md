# WP80 — full exact C7 orbit certificate

Date: 2026-10-04  
Status: **LAUNCHED / FAIL-CLOSED**

The public higher-moment development identifies

\[
C_7=-\frac{17}{360}
\]

numerically but does not consume it because symbolic certification was not
completed.

Our symmetry audit proved, against the complete exact C5 and C6 archives, that
the cycle integrals are invariant under the combined dihedral / translation /
global-sign action used by \`wp80_c7_symmetry_reduce.py\`.

For \(b=7\):

- raw exact-polytope terms: **9,366**;
- validated canonical orbits: **397**;
- reduction: **23.592x**.

The full certificate therefore evaluates exactly one representative per orbit,
using the pinned upstream rational facet-recursion engine, and multiplies by
the exact orbit multiplicity.

Thirty-two round-robin jobs spread the 397 representatives.  Every job
checkpoints after every orbit.  The aggregate gate requires:

1. all 32 batches complete;
2. exactly 397 unique orbit representatives;
3. exact contribution identity
   \[
   c_{\mathcal O}=s_{\mathcal O}|\mathcal O|I_{\mathcal O};
   \]
4. exact total
   \[
   \sum_{\mathcal O}c_{\mathcal O}
   =
   -\frac{17}{360}.
   \]

Any timeout, missing orbit, duplicate orbit, inconsistent contribution, or
fraction mismatch fails the aggregate.

If this passes, the model-side \(C_7\) identification is promoted to an exact
computer-assisted certificate.  It still does not by itself prove a new zeta
zero proportion: the \(k=8\) arithmetic transport and moment ledger remain
separate analytic gates.
