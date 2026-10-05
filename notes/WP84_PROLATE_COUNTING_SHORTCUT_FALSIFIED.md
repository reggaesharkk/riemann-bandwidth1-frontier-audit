# WP84 — prolate/counting-statistic spectral shortcut is already falsified

Date: 2026-10-05

Status: **DO NOT PURSUE AS THE LIMIT-LAW IDENTIFICATION**

The public higher-moment reproduction record already tested the tempting idea
that the connected constants are cumulants of one sharp-window counting
statistic with a prolate-spectrum/Fredholm description.

That pre-registered gate failed before adoption:

    kappa_2 = 0.3442...  !=  1/3,
    kappa_3 != 0.

The target model requires

    centered m2 = 1/3,
    connected b=3 contribution = 0.

Therefore a single prolate counting-statistic law is not the WP84 limiting
spectral law.

## Correct surviving structure

The connected constants are instead represented by the partition-cyclic
chain family

    C_b(v)
      = sum_{P partition [b]} (-1)^(|P|-1)
          sum_{cyclic orders of P}
            overlap(merged-block walk).

The outer moment geometry contributes a second overlap factor.  Exact model
constants are therefore sums of products of two walk-overlap functionals, not
cumulants of one scalar counting statistic.

At b=4 this produces

    Phi4 = -1/60

through the exact 26-term partition-cyclic family.

## Consequence for WP84

A one-operator prolate/Fredholm determinant shortcut may not be inserted as the
limiting law without a new derivation that passes the already-failed b=2 and
b=3 gates.

The useful structure is the chain/partition-cyclic algebra itself.  Any
operator-valued resolvent model should be tested against that family, beginning
with the order-4 pair/connected decomposition.

This note prevents a known falsified spectral identification from being
reintroduced under new notation.
