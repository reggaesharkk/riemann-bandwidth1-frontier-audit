# A1294 canonical finite-certificate format

**Status:** design frozen before a full certificate search. This is a finite
certificate for the affine five-gap inequality only; it is not by itself a
zeta zero-density theorem.

## Statement to certify

With

[
A=1294/100000,qquad B=1094977/5000000000,
]

certify on the full nonnegative gap domain reduced to the standard
([0,60]^5) search box that

[
A le E_6(g)+Bsum_{i=0}^4 g_i .
]

The one-dimensional lower models are exactly the three pinned catalogs whose
SHA-256 values are frozen in the v0.2 gate.

## Trust separation

The **search generator** may use floating point only to choose a promising
tangent anchor. It is not trusted.

The **certificate verifier** must:

- parse the frozen catalogs independently;
- reconstruct every dyadic box from the certificate stream;
- use only integer/Fraction arithmetic for accepted inequalities;
- check every leaf;
- check that the stream covers the root exactly once with no omissions or
  overlaps;
- reject trailing tokens, missing children, bad anchor codes, or hash
  mismatches.

The analytic zeta-density bridge and the proof that each one-dimensional
catalog piece lower-bounds the true kernel are separate obligations.

## Tree stream

The certificate is a UTF-8 preorder stream, optionally compressed for
transport. The uncompressed semantic form is:

- `S` — split the current box using the deterministic weighted widest-axis
  rule with weights `(5,8,9,8,5)`; midpoint is exact dyadic midpoint.
- `T` — tail leaf. The verifier checks
  `B * sum(lower_i) - A >= 0`.
- `Q c0 c1 c2 c3 c4` — quadratic/seam-aware leaf. Each `ci` is an integer
  in `[0,16384]`. It specifies the rational anchor
  `lo_i + ci/16384 * (hi_i-lo_i)`.

The verifier reconstructs the exact local convex lower form from the catalogs,
including the seam-aware segmented scalar fallback. It then evaluates the
supporting tangent at the encoded rational anchor and requires its lower bound
to be at least `A`.

No floating point appears in verification.

## Coverage verifier

Initialize a stack with the root ([0,60]^5). For each preorder token:

1. pop exactly one current box;
2. `S`: recompute the deterministic split axis, form left/right children,
   push right then left;
3. `T` or `Q`: verify the terminal inequality and create no children.

PASS requires:

- every token valid;
- no pop from an empty stack;
- stack empty exactly at EOF;
- every terminal inequality nonnegative;
- all three input hashes match.

This proves exhaustive dyadic coverage relative to the frozen catalog lower
models independently of the generator.

## Seam-aware scalar rule

For a partial-sum interval that straddles refinement boundaries, the verifier
may replace a weak parent stable model by the segmented catalog envelope:

1. split the scalar interval at every exact catalog boundary that lies inside;
2. on each segment, collect all certified pieces whose validity interval
   contains the whole segment;
3. take the maximum of their exact segment minima;
4. take the minimum of those maxima across segments.

Every selected piece is already a certified lower model on its interval, so
this construction remains a rigorous lower bound. It is used only when it is
stronger than the single parent model.

## Manifest

A frozen certificate bundle must record:

- repository commit SHA;
- A and B;
- root limit;
- split weights;
- anchor denominator;
- source/catalog hashes;
- stream SHA-256;
- token count;
- split count;
- tail leaf count;
- quadratic leaf count;
- maximum depth;
- smallest exact terminal margin;
- verifier source SHA-256;
- verifier result SHA-256.

## Claim gate

A full verifier PASS establishes only the finite catalog-relative inequality.
Before any new unconditional density bound is claimed we still require:

1. independent verification of catalog/kernel soundness;
2. the analytic sextuple-to-density bridge;
3. directed constant arithmetic;
4. a fresh literature/novelty audit;
5. preferably a Lean/kernel replay of the finite certificate layer.
