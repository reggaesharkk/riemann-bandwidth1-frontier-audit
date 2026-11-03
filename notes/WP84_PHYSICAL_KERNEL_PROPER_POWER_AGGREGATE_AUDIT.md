# WP84 — physical-kernel reconciliation and proper-power aggregate audit

**Audit base:** `0185e68f53b50e2085eb30aaecc623861ccc107b`

**Audit branch:** `codex/wp84-physical-kernel-proper-power-aggregate-20261103`

**Decision:** `PROPER_POWER_EXCEPTION_CONTROLLED`, scoped to the complete one-base resonance family of the reported positive atom.

**Pointwise physical sign:** positive.

**Full R400 aggregate and consumer:** open.

This is an additive local audit. The previous source, its audit branch, prior
commits, evidence, and the earlier `LEGAL_SOURCE_COUNTEREXAMPLE` decision are
preserved. That earlier decision concerned the pointwise kernel atom; this
note adds a separate classification of its full proper-power resonance
family. No push, merge, publication, unconditional theorem, or RH conclusion
is made.

## 1. What was replayed

The worktree started at the requested base commit. Its parent is the earlier
source-weight audit revision. The existing exact 26-term ledger and the
interval orientation certificate were replayed with their independent replay
entry points, and the actual R400 interval certificate was rerun. The new
checker in `src/wp84_physical_kernel_proper_power_reconciliation.py` rebuilds
the ordered set partitions and the two kernel evaluations using only Python's
standard library and `fractions.Fraction`; it does not import the previous
term compiler. A separate direct call to the public implementation agrees at
the test point.

Replayed results:

- 26 anchored ordered partitions, with counts `1, 7, 12, 6` and the original
  Möbius signs.
- 48 labeled source and conjugate placements across the six balanced sign
  orthants; equal shifts collapse these to 24 distinct rational vectors.
- Every one of the 24 R400 interval-FFT enclosures for
  `Omega_4,400(v)` is strictly above `799/4000 = 0.19975`. The two orientation
  classes lie near `0.199750432` and `0.399748481`; permutation invariance is
  asserted only for the row cumulant and source admission, not for the
  filtered overlap.
- The original source coefficient normalization is
  `c_n = -Lambda(n)/(a_phi(T) L sqrt(n))`, with `Lambda(p^e)=log p`, and the
  complete common tuple factor is retained. The row average is
  `m^-1 sum_{j=0}^{m-1}` and the row factor is
  `D_m(u)=m^-1 sum_j exp(2 pi i j u)`.
- For `T=2 pi p^5`, `L=5 log p`, and every prime `p>=5`,
  `p^5 exp(-sqrt(5 log p)) > p^3`; hence all four entries in
  `(p,p^2,p^3,p^2)` are admitted by
  `N=floor(exp(L-sqrt(L)))`. Since `a_phi(T)->1`, the coefficient sign is
  positive for every sufficiently large physical prime in this family.
- The selected section is common to all terms and satisfies
  `m >= d-2q`, `d=floor(TL/(2 pi))`, `q=floor(d/sqrt(L))`; thus `m>=10`
  eventually. Since the signed logarithmic sum is zero, both the arithmetic
  carrier and section-start phase equal one for every selected section.

The root intervals in slot order are exactly
`[0,4/5], [2/5,1], [0,2/5], [2/5,1]`. These are nonempty, all shifts are
short, and the external R400 filter and all 48 labeled placements are retained.
The interval certificate concerns this external overlap only; it is not a
coefficient-weighted aggregate estimate.

## 2. Exact reconciliation of the two 26-term kernels

At

```text
v = (1/5, -2/5, 3/5, -2/5),   S=0,
```

the original prefix walk is
`(0, 1/5, -1/5, 2/5, 0)`. Its spread is `3/5`, so
`O_A=(1-spread)_+=2/5`.

The public geometric bracket assigns to each ordered partition a nested-path
intersection length. The physical row cumulant uses products of row averages
`D_m(sum_B v_j)` over the blocks. The full exact 26-row comparison is in
`evidence/WP84_PHYSICAL_KERNEL_PROPER_POWER_LEDGER.json`. Grouping those exact
rows by number of blocks gives:

| Blocks | Count | Public signed overlap sum | Physical signed row-factor sum at `m=10` |
|---:|---:|---:|---:|
| 1 | 1 | `1` | `1` |
| 2 | 7 | `-21/5` | `0` |
| 3 | 12 | `24/5` | `0` |
| 4 | 6 | `-8/5` | `0` |
| **Total** | **26** | **0** | **1** |

Thus the independently reproduced public value is `B_4,nc=0`, while the
physical `kappa_10=1`. Every proper nonempty block sum is a noninteger fifth.
When `5|m`, its exact row average is zero, so the physical 26-vector is
`e_1`. For an arbitrary selected `m>=10`, the existing exact estimate gives

```text
kappa_m >= 1 - 7(2/m)^2 - 12(2/m)^3 - 6(2/m)^4 >= 384/625 > 0.
```

The divergence is inside the per-partition kernel factor: a nested-path
overlap was substituted for a product of empirical row moments. The
partition set, Möbius coefficients, prime tuple coefficient, carrier,
cutoff, source-selected section, and label ordering are the same. Pair
subtraction is not the source of this fixed-tuple discrepancy: the physical
identity separates `Pair4` from `Connected4,row` only after defining the
classical row cumulant. It does not turn that cumulant into the public nested
overlap bracket. Nor is this a cutoff or section-endpoint effect.

At sharp scale, the physical kernel at this vector is `O_A kappa_m`, which is
at least `(2/5)(384/625)` for all selected `m>=10`; the public sharp product
is zero. At R400, the certified external overlap is positive for all labeled
placements. Combining the worst certified lower bound with the uniform row
bound gives

```text
Phi_4,400,m > (799/4000)(384/625) = 9588/78125.
```

This is a legal pointwise positive physical kernel atom, not an arithmetic
lower bound for the full sum.

## 3. Proper-prime-power ledger for the atom

The tuple has exponent/sign ledger

```text
slot       0     1     2     3
n_j        p    p^2   p^3   p^2
epsilon    +     -     +     -
```

It has one ordinary-prime slot and three proper-prime-power slots. The
signed exponent sum `1-2+3-2=0`, so the product closure is exact; the four
coefficient signs multiply to plus, and

```text
product_j c_(n_j) = (log p)^4/(a_phi(T)^4 L^4 p^4).
```

Consequently this atom is not an all-ordinary-prime connected-bulk tuple.
Partition by the actual prime-power exponent pattern, so this tuple and its
permutations occur in the proper-power-containing bucket only; do not charge
them a second time to the ordinary-prime-only bulk.

The complete one-base family with this exponent/sign pattern, all its
permutations, and its conjugate orientations is negligible. At fixed `R`,
`|Omega_4,R| <= G_R^4`, `G_R=1+2 H_R/pi`, and the actual row cumulant has the
uniform bound `|kappa_m|<=13/3`. Summing the original coefficients over
`p^3<=N` is bounded by the convergent full series:

```text
48 * (13/3) G_R^4 /( |a_phi(T)|^4 L^4 )
       * sum_p (log p)^4/p^4 = O_R(L^-4).
```

This proves `PROPER_POWER_EXCEPTION_CONTROLLED` for the complete family that
produces the reported atom. It does not prove deletion of every other
proper-power-containing quartic word.

For the full proper-power coefficient pool, the exact squared mass is

```text
sum_(p,k>=2, p^k<=N) |c_(p^k)|^2
  <= 1/(|a_phi|^2 L^2) * sum_p (log p)^2/[p(p-1)]
  <= 64/(|a_phi|^2 L^2)
  <= 256/L^2, eventually.
```

The last bound uses `|a_phi|>=1/2`, `log x<=4 x^(1/4)`,
`p(p-1)>=p^2/2`, and `sum_(n>=2) n^(-3/2)<=2`. This verifies the stated
`O(L^-2)` proper-power square mass with an explicit, deliberately crude
constant. The absolute first mass is only `O(1)`, not `o(1)`. Square mass
alone does not control a quartic mixed aggregate: a Hölder/Schatten argument
also needs a uniform ordinary-prime fourth-moment bound, or a separate
signed multilinear estimate. The existing source proper-power removal
argument for a complete fifth/sixth signed gate is conditional on a bounded
gate and is not a fourth-order proof here.

There is a precise conditional fourth-order removal statement. Write the
fixed-band matrix on the same section as `X=Y+P`, with `Y` the ordinary-prime
part and `P` the complete proper-power part. The source linear-field estimates
in `notes/WP84_SIGNED_NEAR_PRODUCT_CELL_DECOMPOSITION.md` §4 and the
source-matched arithmetic reduction §2 give `||P||op=O_R(1)` and normalized
`tau(P^2)=O_R(L^-2)`. Hence
`tau(P^4)<=||P||op^2 tau(P^2)=O_R(L^-2)` and
`||P||_(4,tau)=O_R(L^-1/2)`. If the missing source bound
`||Y||_(4,tau)=O(1)` holds on this same section, Schatten-Hölder applied to
the four telescoping terms gives

```text
|tau(X^4)-tau(Y^4)|
  <= 4 ||P||_(4,tau) max(||X||_(4,tau),||Y||_(4,tau))^3
  = O_R(L^-1/2).
```

The bound would dispose of the full proper-power-containing contribution to
the raw fourth trace, not just the displayed one-base family. It remains
conditional because the required ordinary-prime fourth norm is not certified
by the square-mass estimate. The row-cumulant/pair identity still leaves the
separate signed ordinary-prime connected inequality below.

## 4. Ordinary-prime sector and the exact aggregate obstruction

For four ordinary primes, exact multiplicative closure
`p_0 p_2 = p_1 p_3` forces the two multisets to agree by unique
factorization; these are the pair contractions already removed into
`Pair4`. The reported positive atom therefore cannot be reclassified as an
ordinary-prime non-pair equality. This audit establishes no
source-admissible positive ordinary-prime non-pair aggregate after pair
subtraction.

Near-product and near-alias terms remain in the source sum. They are not
discarded by a synthetic mask, a prime pool truncation, or the pointwise
kernel sign. The existing R400 physical identity still requires the signed
arithmetic estimate

```text
Re integral Phi_4,400,m(v) dmu_(T,I)(v)
    <= Delta_400 + o(1).
```

For the requested `w_400(I)<=0.266329+o(1)`, the needed error is
`Delta_400<=0` (or a proved compatible nonpositive allowance). No such bound
is established by the atom calculation or by the proper-power square mass.
The earlier downstream ledger records a conditional positive allowance of
`3675673694911/148250000000000 = 0.024793751736330524...`; that is a budget
cap under its other hypotheses, not a verified value of `Delta_400` and not
enough to assert the sharper `0.266329+o(1)` statement.

The smallest missing theorem is therefore not a source definition. It is a
uniform signed near-product/near-alias estimate for the actual ordinary-prime
measure, after the exact pair layer, on the common selected section. One
sufficient conditional lemma is:

> **Conditional R400 aggregate lemma.** For the source coefficients
> `c_n=-Lambda(n)/(a_phi L sqrt(n))`, full cutoff
> `N=floor(exp(L-sqrt(L)))`, all orientations and alias sectors, and one
> common source-admissible section `I`, if
> `limsup_T Re integral Phi_4,400,m dmu_(T,I) <= 0`, then
> `w_400(I)<=0.266329+o(1)` under the already stated pair and reprojection
> hypotheses. A proof must retain near products, near aliases, and the full
> ordinary-prime coefficient measure; pointwise kernel nonpositivity is
> unavailable.

This audit does not verify the lemma's hypothesis. The consumer remains
open, the conditional `68.820273%` coefficient is not promoted, the `79.627%`
model benchmark is not promoted, and the strict greater-than-79% and
unconditional RH claims remain open. The fifth/sixth bounded-consumer
requirements are separate and are not used to infer the fourth-order result.

## 5. Hostile diagnostics and verification

The adversarial ledger preserves two distinct tests:

- At `(-3/4,-1/2,1/2,3/4)`, `m=4`, the exact unweighted physical bracket is
  zero with only term 1 equal to `+1` and term 8 equal to `-1`. Reweighting
  term 1 by `1+delta` changes the result to exactly `delta`; there is no
  positive robustness margin at that zero. This is explicitly diagnostic,
  not source-admissible evidence.
- The earlier abstract public-kernel example is reproduced exactly:
  shifts `(1/6,-1/6,11/12,-11/12)`, weights
  `(1,1/100,...,1/100)`, unweighted bracket `-1/12`, reweighted bracket
  `1187/1200`. It is abstract only and is not used to infer source legality.

The independent rational regression suite passes in normal Python,
`python -O`, and `python -OO` (five tests in each mode). The separate prior
interval certificate replay reports the R400 positive witness interval
`[0.3997484808471383145453305746858843441601,
0.3997484808471383145453305746858907527673]` for the original ordering, and
the orientation replay certifies all 48 labeled placements. The new
machine-readable term ledger is
`evidence/WP84_PHYSICAL_KERNEL_PROPER_POWER_LEDGER.json`; exact source and
artifact SHA-256 values are in
`evidence/WP84_PHYSICAL_KERNEL_SOURCE_HASHES.json` and
`evidence/WP84_PHYSICAL_KERNEL_SHA256_MANIFEST.json`.

Commands used for independent replay:

```powershell
python src/wp84_source_weight_cone_certificate_replay.py
python src/wp84_source_weight_cone_orientation_replay.py
python src/wp84_physical_kernel_proper_power_reconciliation.py --json evidence/WP84_PHYSICAL_KERNEL_PROPER_POWER_LEDGER.json
python -m unittest tests.test_wp84_physical_kernel_reconciliation
python -O -m unittest tests.test_wp84_physical_kernel_reconciliation
python -OO -m unittest tests.test_wp84_physical_kernel_reconciliation
```
