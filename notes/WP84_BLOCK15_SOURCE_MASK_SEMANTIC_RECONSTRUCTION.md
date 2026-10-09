# WP84 block 15: source-mask semantic reconstruction

**Decision: E — SOURCE SEMANTICS INCOMPLETE.** This is a current-source
semantic audit for canonical functional block `{15,20,26,28,31,32}` at
`R=6000`. It does not search Git history, recover an old selector, or perform
determinant/wedge work. Strict `>79%` remains **OPEN**.

## Exact checked-in callback contract

The only executable callback contract is in
[`src/wp84_fifth_full_pool_amplitude.py`](../src/wp84_fifth_full_pool_amplitude.py).
`iter_source_atoms(fid, carrier, T, N, section, prime_stream, source_mask,
core_primes=None, R=6000)` has one required `source_mask` parameter. The
project source contains no `def source_mask`, and no project caller invokes
`iter_source_atoms`; the only executable call to the callback is its internal
call at the alias filter.

For each iterator input, the callback is called as
`source_mask(fid, slots, lag, T, section, m)` with six positional arguments:

| Argument | Meaning available at this call |
|---|---|
| `fid` | Canonical functional id. Its signs, equality partition, multiplicities and alias list are read from the pinned functional JSON. |
| `slots` | Five slot primes induced by the current injective assignment to equality blocks. |
| `lag` | One five-entry closed displacement path generated using the iterator's `R`. |
| `T` | Iterator height. |
| `section` | Caller-supplied inclusive endpoints `(k_-,k_+)`. |
| `m` | One alias from that descriptor's fixed alias list. |

The return has no annotation, explicit type check, or assertion. Its only use
is the list-comprehension filter
`[m for m in f['aliases'] if source_mask(...)]`. Thus the intended contract is
a Boolean predicate; technically Python truthiness controls whether that
alias is retained. The result is not interpreted as an index set, numerical
weight, or mask object. The callback is invoked once per candidate alias for
each current `(fid, slots, lag, T, section)` tuple. If the returned alias
list is empty, the path/assignment contributes nothing.

The callback does **not** receive the carrier, `N`, the prime stream, `R` as a
separate value, the root index or root interval, a precomputed Fourier
residual, `d`/`d'`, `a_phi`, a selected row/cell identity, or a normalization
object. The enclosing generator does have some of this context: it checks the
exact carrier before the callback; it generates the path with `paths(R)`; it
computes the root range after the callback; and it carries `n` from the
section endpoints. A closure could capture extra caller state, but no closure
or callback implementation is checked in, so no extra data are presumed.
Normalization has not been applied by the callback; the yielded expression
record later retains `a_phi(T)^-5`.

The six canonical descriptors are all degree five, have sign word `++++-`,
and alias list `[2]`. Their equality partitions are:

| id | equality partition | raw orbit members |
|---:|:---|---:|
| 15 | `0,0,1,2,0` | 20 |
| 20 | `0,1,0,2,0` | 20 |
| 26 | `0,1,1,2,1` | 10 |
| 28 | `0,1,2,0,0` | 10 |
| 31 | `0,1,2,3,0` | 20 |
| 32 | `0,1,2,3,1` | 20 |

The JSON records these as complete raw-correlation representatives/orbits;
it does not give per-atom membership bits.

## What actually governs iterator output

For each target descriptor, the generator's exact output rule is the
conjunction of its outer gates, a truthy callback result for a listed alias,
and positive root count. In source order:

1. It checks supplied prime-stream entries lie in `[2,N]` and that the stream
   is sorted and duplicate-free. It does not test primality or verify that
   every prime through `N` was supplied.
2. It enumerates assignments to equality blocks, enforces distinct primes
   across blocks, optionally applies the `core_primes` restriction to a hidden
   excess-pair block, and checks exact signed valuation carrier equality.
3. It generates `lag in [-R,R]^5` with zero sum.
4. It filters the descriptor's finite alias list by the callback's truth
   value.
5. Only after that callback does it compute the prefix range and skip paths
   with empty root interval. If positive, it constructs the root interval and
   expression record.

So the callback itself is an alias/window admission filter, not the whole
source row selector. The optional core restriction can produce a diagnostic
subsum; it is not the complete canceled-prime pool. `source_amplitude_entry`
returns a symbolic schema and does not evaluate the full source-selected
matrix entries.

## Mathematical predicate: known pieces and the gap

The checked-in `WP84_FIFTH_LEGAL_STENCIL_AND_PRIME_REALIZATION.md` calls an
atom admissible iff all original source factors are retained, and lists the
following requirements: theorem-admitted height and frozen descriptor;
ordinary-prime equality-block assignments; original slot-window
intersections and natural cutoff; reduced carrier, nearest alias and
`0 < |lambda-mL| <= H/T`; the section actually selected by the source and
its exact endpoints; closed paths at `R=6000`; valid root interval; full
assignment/path/root sum; and, for the frozen-cell argument, constant
admission data on a positive-length source branch. The note says this is an
iff with the full source summand.

That is a mathematical checklist, not an executable predicate. The precise
original slot-window functions/intersections are not supplied to this
callback or defined as executable source in the amplitude module. The
selected-section rule `T -> (k_-(T),k_+(T))`, row identities/order, and
jet-to-row map are also absent. `H` and the source cell/orientation state are
not callback arguments. Therefore the prose iff cannot be evaluated for a
candidate atom from the checked-in implementation. In addition, the
callback precedes the root-count calculation even though some prose source
mask summaries bundle root positivity into “the mask”; root positivity is an
outer iterator gate in executable order, not a callback result.

Classification:

| Class | Result |
|---|---|
| Necessary | The source checklist's cutoff/window, carrier/alias, path, source-section and root conditions are necessary for source atoms. Several are already enforced outside the callback. |
| Sufficient | The complete source checklist is stated sufficient **by definition/equality with the full source summand**, but is not executable because the original window family and selected-section/row rules are unspecified here. No executable sufficient callback predicate is present. |
| Equivalent | The iterator's own output is exactly equivalent to its outer gates AND callback truthiness AND post-callback positive-root test. No equivalence between callback truth and a fully defined original source mask is proved. |
| Diagnostic-only | `core_primes`, finite prime cores, rational/log-surrogate evaluations, small sections, and toy masks do not define source membership for this block. The hidden-prime `q` mask is only a specialized canceled-prime domain and cannot replace the five-slot callback. |

## Identifiability and rank consequences

The constraint builder records ten documented condition families, but zero
source-level equations fix the membership bit of a specified assignment/path/
alias row. The canonical data specify six columns and their raw orbits; they
do not specify a finite row universe or an expected-membership example. The
candidate atom family depends on the uninstantiated section rule and on
`T`, `N(T)`, actual primes, paths, and missing slot-window indicators.
Consequently neither candidate-row count nor number of admissible masks is
finite/computable from the repository's current source semantics. This is
not an assertion that there are `2^n` actual admissible source masks: the
unknown predicate has not been defined well enough to form that finite
constraint problem.

No source-admissible rank interval is obtained. The only unconditional formal
linear-algebra bound for a six-column map is `0 <= rank <= 6`; it is not a
mask-realizability result. The block rank, `K_B`, actual projected sixth
wedge, and a genuine nonzero source wedge seed remain unknown. Therefore the
conditional degree-24 exceptional-endpoint theorem from the preceding audit
is not activated. The global fifth analytic rank bounds remain `38–72`.

## Reproduction

From the repository root run:

```powershell
python src/wp84_source_mask_contract_extractor.py
python src/wp84_source_mask_constraint_builder.py
python src/wp84_source_mask_semantics_replay.py
```

The machine certificate is
[`WP84_BLOCK15_SOURCE_MASK_IDENTIFIABILITY_CERTIFICATE.json`](WP84_BLOCK15_SOURCE_MASK_IDENTIFIABILITY_CERTIFICATE.json).
It also contains a line-level index of every tracked current-tree occurrence
of `source_mask`, `iter_source_atoms`, or `source_amplitude_entry` found by
the audit scan (282 occurrences across 30 tracked files at generation time;
the untracked `notebooklm_packet/` directory is excluded). The executable AST
inventory separately records the one callback call and confirms there is no
project call site invoking the iterator.
The independent AST replay verifies callback arity and truth-filter use,
hash-pins the current source, and runs five hostile mutations. It confirms the
incomplete-semantics outcome rather than guessing a mask. No new theorem,
rank promotion, or change to prior research conclusions is made.
