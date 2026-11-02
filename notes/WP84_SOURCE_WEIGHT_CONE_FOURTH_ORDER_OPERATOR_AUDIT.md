# WP84 fourth-order source-weight cone and operator audit

**Audit revision:** `codex/wp84-source-weight-cone-operator-audit-20261103`
**Base:** `861bdad5f6f6495c5b755546b4b2fa43367e2901`
**Decision:** `LEGAL_SOURCE_COUNTEREXAMPLE`, scoped to a pointwise source-admissible balanced fourth-order atom.
**Aggregate:** open. The legal atom does not determine the sign of the complete signed sum over the full prime-power pool.

The prior extracted package is an exact abstract warning, not evidence about the WP84 source. This audit reconstructs the fourth-order hard-band operator and its finite row cumulant directly from `notes/WP84_R400_FILTERED_SHARP_REPAIR.md` and `notes/WP84_R400_FILTERED_CONNECTED_KERNEL.md`. It does not use the fifth-order `source_mask` callback to infer anything about degree four.

## 1. Revisions and evidence replay

The local repository was at the requested base commit. Work was performed on the separate audit branch named above. No tracked historical file was edited, and no push, merge, publish, or history rewrite was performed.

The extracted package at `C:\Users\Asus\SHARK_AGENT_LAB\wp84_source_weight_mask_hostile_20261102` passed its own SHA-256 manifest verification (9/9 entries) and its seven existing unit tests. Its rational model is

\[
v=(1/6,-1/6,11/12,-11/12),\qquad B=-1/12,
\]

with all 26 artificial weights positive, (w_1=1), (w_2=\cdots=w_{26}=1/100), producing (B_w=1187/1200>0). This remains **abstract only**. It is independently reproduced in the new exact checker and explicitly not used as the legal-source result.

The prior source-matched audit replay was also recomputed without writing its
evidence file. Its generated JSON matched the base commit's Git blob byte for
byte: SHA-256 `b1ee1446feda8871506f422df6c3326593e55b833fab32a561f11a857b922cd1`.
The checked-out copy hashes to `8a2b91ec1b15d31a3333f3765e32382c4fc1e5545b5d54875cd2226bb3410c73`
because Windows checkout normalized the blob's LF newlines to CRLF; the
replay log records this normalization explicitly. The extracted package's
manifest sidecar SHA-256 is `e8389181a9cbfd40be3e247a36ab07bc03fd29203b09d2263eb95e4f9e57f4a7`.

The exact SHA-256 hashes for the base commit, extracted package inputs, source notes and scripts, audit outputs and tests are pinned in `evidence/WP84_SOURCE_WEIGHT_CONE_SHA256_MANIFEST.json`.

## 2. Fourth-order physical operator and the selected section

Let

\[
L=\log(T/(2\pi)),\quad h=2\pi/L,\quad d=\lfloor TL/(2\pi)\rfloor,
\quad N=\lfloor e^{L-\sqrt L}\rfloor,
\quad c_n=-\frac{\Lambda(n)}{a_\phi(T)L\sqrt n}.
\]

The pool is the full set of prime powers (n=p^e\le N), with
\(\Lambda(p^e)=\log p\), and both signs \(\epsilon\in\{-1,+1\}\). For
\(v=\epsilon\log n/L\), let (J_v=[\max(0,-v),\min(1,1-v)]) for
\(|v|<1), and (J_v=\varnothing) for \(|v|\ge1\). The actual fixed-band
entry is the Fourier projection of (1_{J_v}) to \(|r|\le R\), followed by
the translation and the source carrier. Here (R=400).

The selected section is one common contiguous interval
\(I=[k_-,k_+]) of cardinality (m). The endpoint-selection result in
`notes/WP84_FIXED_BAND_WEIGHTED_REPROJECTION.md` gives
\(m\ge d-2q\), (q=\lfloor d/\sqrt L\rfloor), and hence (m/d\to1).
Its endpoints are selected using the source endpoint score; they are not
chosen term by term. For the witness below the exact endpoints are immaterial:
the total log shift is zero, so every section carrier involving (k_-)
equals one, and the proof is uniform for every selected section once (m\ge10).

For a closed lag path (r=(r_1,r_2,r_3,r_4)), each
\(|r_j|\le400\), \(\sum_jr_j=0\), the row variables are the four actual
hard-band matrix entries along that path. The normalized single-compression
trace is (B_{4,T,R}=\sum_r E_I[X_1X_2X_3X_4]), where
\(E_I=m^{-1}\sum_{k\in I}\). The row-path closure is Fourier index
closure; it is distinct from the arithmetic/log closure
\(S=\sum_jv_j=0\). The source note counts 342,615,201 such lag paths at
\(R=400\). No path or orientation multiplicity is silently removed here.

For each atom (v=(v_0,v_1,v_2,v_3)), define prefix shifts
\(p_0=0, p_j=\sum_{a<j}v_a\) and the **actual filtered** external overlap

\[
\Omega_{4,R}(v)=\int_0^1\prod_{j=0}^3
       (F_R1_{J_{v_j}})(x+p_j)\,dx.
\]

Equivalently, with \(a_r(v)=\int_{J_v}e^{-2\pi irx}\,dx\), its exact finite
Fourier expansion is
\[
\Omega_{4,R}(v)=\sum_{\substack{|r_j|\le R\\\sum_jr_j=0}}
 \left(\prod_ja_{r_j}(v_j)\right)e^{2\pi i\sum_jr_jp_j}.
\]
This records the interval endpoints, frequency cutoff, and orientation
phases. The condition \(\sum r_j=0\) is matrix-index closure, distinct from
the arithmetic/log closure \(S=0\).

The finite row Dirichlet average is

\[
D_m(u)=\frac1m\sum_{k=0}^{m-1}e^{2\pi iku}.
\]

The exact connected identity from the finite physical operator is

\[
\mathrm{Connected}_{4,\mathrm{row}}(T,R,I)
=\sum_{n_0,\ldots,n_3\le N}\sum_{\epsilon\in\{-1,+1\}^4}
  \left(\prod_jc_{n_j}\right)e^{iTLS}e^{2\pi ik_-S}
  \Omega_{4,R}(v)\,\kappa_m(v),
\]

\[
\kappa_m(v)=\sum_{\pi\text{ anchored ordered partition of }\{0,1,2,3\}}
(-1)^{|\pi|-1}\prod_{B\in\pi}D_m\!\left(\sum_{j\in B}v_j\right).
\]

This is a finite algebraic identity. The row cumulant is not the public
sharp-overlap bracket and is not a Gaussian or model moment.

## 3. Exact 26-term source-weight ledger

The source construction has 1, 7, 12 and 6 **ordered** contributions with
respectively 1, 2, 3 and 4 blocks. Each ordered contribution has its original
coefficient \((-1)^{k-1}\): signs are +, −, +, − by block count. On grouping
block orders, the coefficients become: the four 1+3 splits at −1 each; the
three 2+2 splits at −1 each; the six 1+1+2 products at +2 each (two orders);
and the four-singleton product at −6 (six orders). These sum to the familiar
26-term fourth cumulant exactly.

The complete ordered list for the witness is in
`evidence/WP84_SOURCE_WEIGHT_CONE_26_TERM_LEDGER.json`. Each row records its
ordered blocks, original coefficient, exact block frequency sums, symbolic
row factor \(\prod_BD_m(v_B)\), and the exact factor when 5 divides (m).
That JSON also records the full 26-row ledger separately for each of the 24
unique source and conjugate orientation tuples.

There is a common **outer** tuple factor across all 26 terms:

\[
\left(\prod_jc_{n_j}\right)e^{iTLS}e^{2\pi ik_-S}\Omega_{4,R}(v).
\]

The prime-power cutoff indicator and four sign choices are also common across
the 26 terms. There is no fourth-order partition-dependent source callback or
independent admission mask in this identity. The 26 **inner** weights are not
equal: they are the stated products of blockwise (D_m)'s. Since (D_m) can
be complex away from closure and its centered real form can change sign,
there is no globally nonnegative 26-vector factorization. At (S=0), all
partition products have the same midpoint phase (1), and each term is real,
but the terms still need not be nonnegative.

## 4. Legal positive source atom and exact cone violation

Take any sufficiently large actual prime (p\ge5), set

\[
T=2\pi p^5,\quad L=5\log p,\quad
(n_0,n_1,n_2,n_3)=(p,p^2,p^3,p^2),\quad
(\epsilon_0,\epsilon_1,\epsilon_2,\epsilon_3)=(+,-,+,-).
\]

Then

\[
v=(1/5,-2/5,3/5,-2/5),\qquad S=0.
\]

The tuple is source-admissible with the original prime-power pool: for
\(p\ge5\), (2\log p>\sqrt{5\log p}), so
\(p^5e^{-\sqrt{5\log p}}>p^3), and therefore every (n_j\le N).
All four translations are short, (|v_j|<1), and all four cutoff intervals
\(J_{v_j}\) are nonempty. Since (a_\phi(T)\to1), it is positive for all
sufficiently large choices in this prime family. Its exact source coefficient
product has positive sign:

\[
\prod_jc_{n_j}=\frac{(\log p)^4}{a_\phi(T)^4L^4p^4}>0.
\]

The arithmetic carrier and selected-section endpoint phase are both exactly
one because (S=0).

For every nonempty proper block (B\), the sum (v_B) is a noninteger fifth
of an integer, so
\[
|D_m(v_B)|=\frac{|\sin(\pi m v_B)|}{m|\sin(\pi v_B)|}<\frac2m,
\]
using \(\sin(\pi/5)>1/2\). The one-block term is exactly (D_m(S)=1).
Every other partition has at least two proper blocks. Thus, with the exact
counts 7, 12 and 6,

\[
\kappa_m(v)\ge1-7(2/m)^2-12(2/m)^3-6(2/m)^4
\ge\frac{384}{625}>0\qquad(m\ge10).
\]

At (m=10), the exact rational-grid term vector is
\((1,0,\ldots,0)\). For the evaluated term vector (t=e_1), the cone of
artificial multipliers satisfying (u\cdot t\le0) is (u_1\le0); the
actual unreweighted vector (u=(1,\ldots,1)) is outside it. For arbitrary
selected (m\ge10), the 25-term absolute remainder bound above gives the
same strict positive sign without assuming a congruence for the selected
section size.

The row cumulant and common closed source factor are invariant under these
label permutations. The external filtered overlap is not: the certified
values split into two positive orientation classes, near 0.199750432 and
0.399748481. The earlier sharp fixed-scale 6/24/8 orientation replay also
replays exactly from the pinned prior audit; its multiplicity identity is
not substituted for this order-dependent R400 overlap. The interval certificate in
`evidence/WP84_SOURCE_WEIGHT_CONE_ORIENTATION_INTERVALS.json` covers the
source family and its conjugate: each has 24 labeled placements, six balanced
sign orthants, two positive-shift orders, and two negative-shift orders. The
two equal shifts collapse each family to 12 unique ordered tuples. Across
both families there are 48 labeled placements and 24 distinct source tuples.
Every R400 filtered external-overlap interval is strictly positive (the
smallest lower endpoint is about 0.19975043199909). Conjugation preserves
the positive source coefficient and real row cumulant on S=0. Thus all 24
distinct source tuples have positive atoms for sufficiently large p and every
selected m>=10; swapping equal prime powers does not add multiplicity in the
Cartesian pool sum.

This is a genuine source counterexample to a **pointwise nonpositive kernel**
claim on the balanced short-shift sector. It is not a counterexample to the
sign of the entire sum over the complete prime-power pool: this one atom has
vanishing asymptotic mass, and the other source atoms carry signed phases and
correlations. No prime was synthesized and no source mask was inferred from
the floating diagnostics.

## 5. Zero-margin and orientation stress tests

The exact rational finite-grid diagnostic

\[
v=(-3/4,-1/2,1/2,3/4),\quad m=4
\]

has exactly two nonzero ordered contributions, +1 and −1, and
\(\kappa_4(v)=0\). Multiplying the first contribution by (1+\delta) while
leaving the second at 1 gives exactly \(\delta\), with either sign for
arbitrarily small rational δ. It demonstrates the absence of a robustness
margin at a zero bracket. It is a diagnostic finite-grid zero, not the legal
positive atom used for the decision and not an assertion about the unknown
selected section's congruence class.

The checker also verifies all six balanced sign orthants and all 24 ordered
orientations of the positive atom. No continuum cell arrangement is claimed.
The actual R400 kernel includes trigonometric Dirichlet block factors and
filtered Fourier overlaps; the rational hyperplane arrangement for the
different public sharp overlap cannot be transferred to it. A finite
cell-constant vertex method is therefore not justified for the actual source
weights. The exact source-admissible pointwise counterexample settles the
pointwise sign question without such an arrangement.

## 6. Replay and tests

The additive rational checker is `src/wp84_source_weight_cone_audit.py`; its
full executable ledger is `evidence/WP84_SOURCE_WEIGHT_CONE_26_TERM_LEDGER.json`.
The independent regression suite is
`tests/test_wp84_source_weight_cone_audit.py`. It is run in normal Python,
`python -O` and `python -OO`; the result logs and hashes are in the evidence
manifest. The inherited source interval script was separately run in normal
Python as

```text
python -B src/wp84_r400_filtered_connected_kernel.py --certificate
```

It reproduced the exact rational cumulant, finite row identity diagnostic,
R400 positive overlap interval and both indefinite-kernel certificates. Its
own fail-closed design intentionally rejects `-O`; the new exact checker and
tests do not rely on Python `assert` statements and pass in all three modes.
The interval values for all 24 unique source and conjugate atom orientations were separately
replayed through its outward-rounded interval FFT.

## 7. Strongest justified result and open obligations

The source semantics for the fourth-order physical operator and finite row
cumulant are defined well enough to refute a pointwise nonpositive-sign
claim. The fifth-order `source_mask` callback gap is irrelevant to this
fourth-order conclusion. No fourth-order source definition is being declared
missing.

The complete source-weighted arithmetic total remains open. The narrow
source-independent conditional lemma needed for the R400 consumer is:

> For the exact finite source measure \(\mu_{T,I}\), exact kernel
> \(\Phi_{4,400,m}=\Omega_{4,400}\kappa_m\), and one admissible common
> selected section (I=I_T), if
> \[
> \limsup_{T\to\infty}\operatorname{Re}\int
>      \Phi_{4,400,m}(v)\,d\mu_{T,I}(v)\le\Delta_{400}
> \quad\text{with}\quad
> \Delta_{400}<\frac{3675673694911}{148250000000000},
> \]
> uniformly with the complete prime-power pool, all orientations,
> unbalanced terms, exact and near aliases, and selected endpoints included
> (unless any removed component is separately bounded), then the displayed
> R400 consumer margin survives, conditional on the other frozen gates.

The required signed aggregate estimate is not proved here. In particular,
the positive atom is not summed against the full source measure, and the
large total variation of that measure prevents replacing this estimate by a
pointwise supremum bound. The first/third-moment, normalization, resolvent,
zero-side, and fifth/sixth bounded-consumer obligations remain separate.
The strict greater-than-79% theorem and unconditional RH claims remain open.

## Reproduction commands

```powershell
python -B src/wp84_source_weight_cone_audit.py --write-evidence
python -B src/wp84_source_weight_cone_run_modes.py
python -B src/wp84_source_weight_cone_orientation_replay.py
python -B src/wp84_source_weight_cone_certificate_replay.py
```
