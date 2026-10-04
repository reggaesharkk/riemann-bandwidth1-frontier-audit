# WP82 — truncation-consumption hostile audit

Date: 2026-10-04
Status: **BLOCKED BY AN UNDEFINED/COLLIDING CELL PARAMETER IN THE PUBLIC WRITE-OUT**

The public spectral route depends critically on the claim that all cells outside a polylogarithmic modulus range can be discharged absolutely before the Siegel--Walfisz/Vaughan analysis.

That claim is currently not independently consumable from the public source because the truncation variable is not defined consistently.

## 1. Global ell_1 is already fixed

Earlier in the paper the notation is fixed globally as

    ell_1 = log(T/(2*pi)) + 2*log(2) - 1,

the first-moment / zero-density normalization. It is a single global quantity, not a cell modulus.

The public scripts use `ell1` only in this global normalization sense; code search finds no independent cell-index variable with that name.

## 2. The truncation section reuses the same symbol differently

The truncation section says:

- the k-cycle cell mass at **cell parameter ell_1** is `<< Y^2 (log Y)^c ell_1`;
- the number of prime-power tuples with **cell parameter ell_1=ell** is `<<_epsilon ell^epsilon`;
- `F^(P)` is the restriction to `ell_1<=P`;
- the proof then sums `ell^{-k} * ell * ell^epsilon` over `ell>P`;
- the introduction says the `1/ell_1^k` weights discharge cells with `ell_1>(log X)^B`.

No separate definition of this cell parameter was found in the paper or reproduction scripts.

These statements cannot all use the globally defined

    ell_1 = log(T/(2*pi))+2log2-1,

because that quantity does not vary from cell to cell and cannot have a divisor-bounded multiplicity of prime-power tuples.

Therefore the truncation proof currently contains either:

1. a notation collision hiding a different arithmetic cell parameter `ell`; or
2. a genuine missing definition / missing factor in the argument.

Until that object is identified, the tail exponent

    P^(-(k-2)+epsilon)

cannot be audited from the public write-out.

## 3. Why this is a hard gate

The spectral Lemma-D theorem assumes `b1,b2 <= (log X)^B`. The paper justifies consuming only those logarithmic moduli by the truncation proposition.

If the truncation variable is undefined, the passage from the full moment ledger to the logarithmic-modulus spectral problem is not established.

This is independent of the later major/minor-arc estimates. Even a perfect spectral proof on logarithmic cells would not recover the full moment unless this tail bridge is repaired.

## 4. What would repair it

A valid repair must explicitly define one arithmetic cell-size variable, call it `ell_cell`, and show all of the following in one convention:

1. the actual cell weight contains `ell_cell^{-k}`;
2. the consumption-normalized mass at fixed `ell_cell=ell` is `<<Y^2(log Y)^c ell`; 
3. the number of relevant unordered prime-power tuples at fixed `ell` is `<<_epsilon ell^epsilon`; 
4. summing over `ell>P` gives the stated `P^{-(k-2)+epsilon}` tail;
5. `ell_cell<=P=(log X)^B` really implies the prime-sum denominators/moduli needed by the spectral argument are logarithmic.

Every map in items 1--5 must be explicit. A renamed symbol alone is not enough.

## 5. Current grade

- algebraic tail summation `sum_{ell>P} ell^{-k+1+epsilon}`: CORRECT IF the premises are true;
- identity of the cell variable and its weight: OPEN / UNDEFINED IN PUBLIC SOURCE;
- fixed-cell mass estimate: OPEN WRITE-OUT;
- multiplicity estimate: OPEN WRITE-OUT;
- implication to logarithmic spectral moduli: OPEN;
- truncation-consumption proposition as a whole: **NOT YET CONSUMABLE**.

## Strategic effect

This does not damage the exact local S4 work or the j-first identity. It tells us exactly where the spectral route must be repaired before it can replace the older bridge/glue import.

The next search should be for the archived meaning of this cell parameter in the upstream program history or, if unavailable, reconstruct the cell-size variable directly from the fourth-moment ledger rather than guessing.

## 6. Public-package provenance check

The ambiguity is not a recent post-release typo:

- the tagged v2.0 paper at commit `01ec104dfcbe64badc352ae3fc9bac938fe499c4` contains the same truncation text;
- the current main commit changes later exact-constant material but leaves this truncation paragraph structurally unchanged;
- recursive inspection of the public repository finds no dedicated truncation/consumer implementation or archived D1 script; the only references to the D1 tail and rounds 91--93 are statements in `paper.tex`;
- `REPRODUCTION.md` says the full forward research archive is preserved separately. It grades truncation as part of the certified-candidate analytic layer, but supplies no separate executable reconstruction of the claimed cell parameter.

So the present public package does not provide enough information to infer safely what the varying `ell_cell` was intended to be.

**Fail-closed rule:** do not repair the notation by guesswork. Either recover the archived definition from an authoritative source, or reconstruct a new truncation theorem directly from the actual cell ledger with fresh notation and proof.
