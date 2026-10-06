# WP83 — public pair-correlation literature versus EC-star

Date: 2026-10-04
Status: **NO PUBLIC RESULT LOCATED THAT DIRECTLY CLOSES EC-star FOR DEEP OFF-LINE CLUSTERS**

This note records the literature check for the large-component star in `WP83_ENERGY_COUNTING_SIEVE.md`.

## 1. Baluyot--Goldston--Suriajaya--Turnage-Butterbaugh

The 2024 Acta Arithmetica paper

    S. A. C. Baluyot, D. A. Goldston, A. I. Suriajaya,
    C. L. Turnage-Butterbaugh,
    'An unconditional Montgomery theorem for pair correlation of zeros
    of the Riemann zeta-function', Acta Arith. 214 (2024), 357--376,
    arXiv:2306.04799.

proves an unconditional form of Montgomery's pair-correlation formula.

However its simple-zero consequences still require either a narrow horizontal box condition or a strong zero-density hypothesis. The theorem does not directly provide the EC-star estimate needed here for the set

    beta-depth >= delta-D log L/L
    AND close ordinate separation
    AND power-saving cardinality strong enough for T X^(-4 delta).

Therefore the paper may be relevant technology, but it is not a black-box closure of EC-star.

## 2. Follow-up pair-correlation work

The 2025/2026 follow-up on proportions of simple and critical zeros similarly studies pair correlation under a narrow vertical-box hypothesis around the critical line. That geometry is opposite to the deep off-line set that Proposition R is trying to exclude.

Again, no direct EC-star implication has been established here.

## 3. Consequence

Importing 'unconditional Montgomery pair correlation' as if it counted the required deep close pairs would be a category error.

The theorem-side state remains:

- SC4 (components of <=4 pairs): analytic write-up closed modulo formalization/review;
- large components: starred;
- an external close-pair theorem could close the star only after an explicit extraction to the depth-band graph;
- absent that extraction, the self-contained route is PT-star / large-cluster scalar endpoint transfer.

## 4. Evidence rule

No literature result is consumed merely because it contains the words 'unconditional pair correlation'. The exact zero set, horizontal weights, ordinate scale, and power-saving exponent must match the EC-star ledger.
