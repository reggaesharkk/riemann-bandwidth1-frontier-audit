# WP84 — full operator-valued generator fourth-order consistency gate

Date: 2026-10-05

Status: **MODEL/GENERATOR CONSISTENCY GATE; PAIR SECTOR SPLIT RESOLVED; CONNECTED TRANSPORT OPEN**

The infinitesimal-array estimate

    sum_j ||B_j||^3 = o(1)

removes cubic-and-higher **single-block Taylor remainders** from the fixed
nonreal resolvent expansion.  It does not justify scalarizing the evolving
resolvent or covariance map, and it does not imply a Gaussian/Wick limit.

## 1. Correct order-four decomposition

The pinned centered target is

    m4_centered = 1/4.

The exact translation-word geometry separates this into

    adjacent pair layer:
        2*t_adj = 2*(7/60) = 7/30,

    crossing pair layer:
        t_opp = 1/30,

    connected core:
        Phi4 = -1/60.

Hence

    boxed:
    1/4
      = 2*t_adj + t_opp + Phi4
      = 4/15 - 1/60.

The old shorthand

    1/4 - 7/30 = 1/60

is numerically correct but structurally incomplete: it hides a positive
crossing repair +1/30 followed by a negative connected repair -1/60.

## 2. Pair sector is a second-order operator-state gate

The exact noncommutative quadratic one-block update produces all six A^2 B^2
words with coefficient +1.

Under cyclic trace equivalence they split 4:2 into

    adjacent/nested,
    alternating/crossing.

Therefore the full pair layer has the exact multiplicity ratio 2:1 and the
model target

    2*t_adj + t_opp = 4/15.

A multiplication/covariance scalarization deletes the alternating class and
returns only 7/30.

Companion:

    src/wp84_lindeberg_m4_word_ledger.py
    notes/WP84_M4_LINDEBERG_WORD_ATTACK.md

## 3. Latest-block localization

For any fixed permutation and length-four word, let B be the latest inserted
label occurring in that word.

Then exactly:

- latest multiplicity 1 -> first-order Lindeberg sector A1;
- latest multiplicity 2 -> second-order Lindeberg sector A2;
- latest multiplicity >=3 -> cubic-remainder sector.

Consequences:

- every 2+2 pair word lies in A2;
- every four-distinct word lies in A1;
- 2+1+1 words split between A1 and A2 under permutation averaging.

Thus the nonzero connected sector is compatible with an o(1) single-block
cubic remainder: global multi-block memory survives through repeated
first/second-order history.

Companion:

    src/wp84_lindeberg_latest_block_m4.py
    notes/WP84_M4_LATEST_BLOCK_DECOMPOSITION.md

## 4. Two fail-closed subgates

### G4-P — crossing pair gate

The full operator-valued conditional variance/state evolution must reproduce

    t_opp = 1/30

and hence the complete pair layer 4/15.

### G4-C — connected-memory gate

After the complete pair layer is present, the non-pair conditional-state
sector must reproduce

    Phi4 = -1/60.

No unsupported assignment of Phi4 to one variance branch is permitted.

## 5. Important Proposition-R firewall

Extracting the theta^4 coefficient of the **finite-T arithmetic** resolvent is
equivalent to asking for a raw fourth-moment coefficient and must not be used
as the theorem proof itself.

This gate is a consistency test for any proposed limiting operator/generator.

The theorem-side bounded target is now the rationalized Christoffel consumer

    F_61(x)=62 P(x)^2/(P(x)^2+61),

whose six simple nonreal poles avoid finite-T raw moments entirely.

See:

    notes/WP84_BOUNDED_CHRISTOFFEL_CONSUMER.md

## 6. PASS / FAIL outcomes

PASS:
    the candidate limiting generator reproduces 4/15 in the pair sector and
    -1/60 in the connected sector.

FAIL:
    the candidate limiting generator returns 7/30, 4/15, or another
    incompatible final value.

ARITHMETIC-DEPENDENCE:
    identifying the connected bounded-resolvent sector requires a new
    arithmetic input.  That specific bounded input becomes the theorem
    frontier.

No finite-height raw m5/m6 calculation can substitute for the bounded
resolvent theorem.
