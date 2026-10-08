# Fifth-block determinant-visible hidden-prime compression: source audit

Status: **not evaluated; source-selected matrix data are missing from the executable repository**. This note does not promote a rank or claim that all nine moments survive. The local audit is at R=6000 and preserves the frozen 73 -> 9 q-moment reduction.

## Decision

**F. GENUINE MULTIDIMENSIONAL HIDDEN-PRIME THEOREM REMAINS** is the closest listed status, with an important qualification: the available evidence does not establish that the true determinant is genuinely full-dimensional. It establishes that the repository does not provide enough executable source data to decide whether the determinant compresses. The exact determinant-visible subset K, its first nonzero section coefficient, correction ranks, and source-legal visible minors remain unknown. Accordingly, no new fifth rank is promoted and the existing bound remains 38–72.

The frozen reduction is

    73 candidate coordinates -> 9 master moments S_2,...,S_10 -> K_B unknown.

| Block | m | Candidate master moments | First possible deficit | First nonzero deficit | K_B | Correction rank | Visible rank lower bound |
|---|---:|---|---:|---|---|---|---:|
| B6 | 6 | S2–S8 (7) | 5 | unknown | unknown | unknown, <= 6 | 0 |
| B8a | 8 | S2–S8 (7) | 7 | unknown | unknown | unknown, <= 7 | 0 |
| B16 | 16 | S2–S10 (9) | 15 | unknown | unknown | unknown, <= 9 | 0 |
| B8b | 8 | S2–S8 (7) | 7 | unknown | unknown | unknown, <= 7 | 0 |

These are upper bounds on correction span only, from the count of candidate coefficient matrices. They are not computed ranks. Zero visible rank contribution means no source-legal nonzero minor is certified in the stored files; it does not assert that the actual visible subsystem has rank zero.

## What the source actually makes executable

`src/wp84_fifth_full_pool_amplitude.py` contains three different levels of information:

1. `source_amplitude_entry` returns a schema describing the amplitude. Its `section` and `carrier` are caller-supplied, and the returned object is not an evaluated matrix entry.
2. `iter_source_atoms` can enumerate terms only when the caller supplies the complete prime stream **and** a `source_mask(fid, slots, lags, T, section, alias)` callback. No such callback is defined in that module or by the new determinant certificate.
3. The block certificate gives layouts and jet/formal specializations, but does not identify a source-selected row tuple/order for the four unresolved blocks or instantiate their selected section endpoints and carrier/alias cells.

The order-five common vector is correctly kept as `v_B`; it is never replaced by an all-ones row here. However, `v_B`, the subleading rows, and their moment coefficient matrices are still sums over the unavailable source-selected cells. The formal coefficient file expresses these sums but does not evaluate them. The previous first-possible-deficit formula is therefore an unevaluated cofactor identity, not a polynomial with known coefficients.

The precise missing inputs are:

- executable source mask and alias/window predicates for every selected row;
- the source-selected row identities and their order, including the jet-to-row rule;
- executable selected-section endpoints `k_-(T), k_+(T)` (the asymptotic condition `d'/d -> 1` alone does not select them);
- actual carrier and alias-cell assignments with exact source-state values;
- evaluated complete visible-prime/path sums for V and each E_r entry;
- an equality certificate for the resulting logarithmic-prime and phase constants, sufficient to distinguish exact zero from nonzero.

The current amplitude iterator's external callback and the absence of a row selector are directly inspectable in `src/wp84_fifth_full_pool_amplitude.py`. Thus there is no legitimate exact calculation of K_B or of the first nonzero coefficient from the checked-in machine-readable inputs. Substituting the small-section rational-log specializations would answer a different question, so they are not used.

## Exact structural conclusion that does follow

For a size-m block, the source section expansion has a common order-five row direction. A determinant term with two such rows vanishes. The top section term and all terms with fewer than m−1 rows below top degree vanish, so deficit m−1 is the first **possible** deficit. In the stored notation its coefficient has the cofactor shape

    C_(m-1,B) = sum_(k=1)^m a_k det(r_1,...,r_(k-1),v_B,r_(k+1),...,r_m),
    a_k = (2 pi i lambda_k)^(h_k)/(h_k+1)!,

where `r_i` is the source-selected next section coefficient row. The repository does not instantiate those rows for these blocks. It therefore cannot determine whether C_(m−1,B) vanishes; if it does vanish, no later coefficient can be selected as first nonzero either.

The formal matrix decomposition

    M_B = V_B + sum_(r=2)^(hmax+2) S_r E_(B,r)

does not by itself give the ranks of `span{E_(B,r)}` or the determinant support: those ranks depend on the missing entries. The only certified exact moment counts remain 7, 7, 9, 7 by block, globally 9. No moment is removed from analytic debt without an exact wedge-cancellation identity.

## Smallest remaining analytic theorem

No smaller signed theorem can yet be stated honestly because the coefficient polynomial itself is not determined. The immediate prerequisite is a **source-matrix specification theorem/data certificate** that fixes the row selector, full source predicates, selected section rule, and exact entry sums. Once those data are present, the requested reducer can compute K_B and the first nonzero coefficient before any PNT step. PNT has not been applied: doing so to S2–S10 before the determinant-visible combination is known would violate the requested order of work.

## Reproducibility

Run:

```text
python src/wp84_determinant_visible_hidden_prime_compression.py
python src/wp84_determinant_visible_hidden_prime_replay.py
python -m unittest src/test_wp84_determinant_visible_hidden_prime_compression.py
```

The builder writes `notes/WP84_DETERMINANT_VISIBLE_HIDDEN_PRIME_COMPRESSION.json`. It fails closed: `K_B`, exact correction ranks, first nonzero deficits, and visible minors are null rather than inferred from formal templates. The independent replay pins the source files by SHA256 and rejects any certificate that silently reports an unproved K, rank promotion, coefficient, or visible minor. This makes the evidence boundary reproducible; it cannot manufacture the missing source inputs.
