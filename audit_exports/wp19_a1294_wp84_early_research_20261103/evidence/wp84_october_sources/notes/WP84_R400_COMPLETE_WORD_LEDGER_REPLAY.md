# WP84 — R=400 complete same-normalization order-four replay

Date: 2026-10-06

Status: **INTERNAL THEOREM-SIDE WORD LEDGER CLOSED; THE R=400 FIRST-STRIKE INEQUALITY NOW HAS A COMPLETE SAME-NORMALIZATION PATH, SUBJECT TO INDEPENDENT AUDIT OF THE CITED ANALYTIC INPUTS**

This note performs the six-item replay requested by
`WP84_R400_FIRST_RECORD_ASSEMBLY.md`.

It does not alter any source theorem, normalization, or numerical constant.
It only checks that every degree-four word class lands in exactly one already
proved gate after the good-endpoint principal section is selected.

No claim of external peer review is made here.

## 1. Order of operations

The proof order is fixed:

    bounded full consumer
      -> fixed R=400 band comparison
      -> delete o(d) frequency rows and choose the good contiguous section I
      -> apply the quartic majorant only to the selected fixed-band section.

This preserves the Proposition-R firewall.

Write

    H_{400,I}=I+P_{400,I}+o(1)

in the already-established centered normalization, and define

    w_{400}(I)
      =
      tau_I(P_{400,I}^4).

The target is

    boxed:

    w_{400}(I)
      <=
      0.266329
      +o(1).

## 2. Exhaustive sign partition of degree-four words

After removal of the scalar background and proper-prime-power remainder, every
ordinary-prime length-four translation word belongs to exactly one of the
following sign populations:

    4-vs-0,
    3-vs-1,
    2-vs-2,
    1-vs-3,
    0-vs-4.

There is no sixth sign class.

The 1-vs-3 and 0-vs-4 cases are conjugates of the first two, so it is enough
to audit:

    same-sign 4-vs-0,
    unbalanced 3-vs-1,
    balanced 2-vs-2.

The proper-prime-power sector is kept separate and added at the end as o(1).

## 3. Same-sign 4-vs-0 sector

The exact order-four same-sign/V-sum analysis shows:

- an exact resonance involving a current ordinary prime forces previous
  factors with the same prime base and proper powers;
- the complete resonant order-four weight is absolutely summable and o(1);
- current proper-prime-power blocks are themselves o(1).

The carrier-2T fast covariance theorem closes the complementary same-sign
current-prime channel uniformly over the actual intermediate state.

Therefore the complete fixed-degree-four same-sign contribution is

    boxed:

    SameSign_4=o(1).

No ordinary distinct-prime exact resonance survives.

Reference:

    WP84_ORDER4_VSUM_PRIME_RESONANCE
    WP84_D2_FAST_CHANNEL_VK_CLOSURE.

## 4. Unbalanced 3-vs-1 and 1-vs-3 sectors

After the adaptive endpoint deletion, the retained individual prime-power
range satisfies

    N/T ->0.

The exact sign-balance spacing theorem gives, for every nonclosed word whose
smaller sign population has size one,

    normalized trace
      =
      o(1)

uniformly.

Thus every nonclosed 3-vs-1 and 1-vs-3 degree-four word is o(1).

An exact multiplicative closure with three ordinary primes on one side and
one ordinary prime on the other is impossible by unique factorization unless
a repeated prime base/proper prime power is present.  Those pieces belong to
the already-negligible proper-power sector.

Hence

    boxed:

    Unbalanced_4=o(1).

Reference:

    WP84_SIGN_BALANCE_NEAR_RESONANCE_GATE
    WP84_BALANCED_PRODUCT_SECOND_MASS.

## 5. Proper-prime-power sector

The normalized proper-prime-power squared mass is

    O(L^-2),

and the ordinary-prime balanced product vector has O(1) squared mass.

Cauchy--Schwarz therefore makes every degree-four term containing at least one
proper-prime-power coefficient lower order.

Thus

    boxed:

    ProperPower_4=o(1).

This includes the exceptional exact closures excluded in Sections 3 and 4.

Reference:

    WP84_BALANCED_PRODUCT_SECOND_MASS
    WP84_ORDER4_VSUM_PRIME_RESONANCE.

## 6. Balanced 2-vs-2 sector: exact pair part

The exact multiplicative pair closures give the complete pair-pair sector.

The orientation normalization has already been reconciled:

    C24=4 C6=C8,

so no factor two/four/eight ambiguity remains between the six sign positions,
the 24 labelled permutations, and the eight alternating labelled words.

For the selected good-endpoint principal section I, the fixed-R locality
lemma gives

    Pair_400(I)
      =
      Pair_400
      +o(1).

The independent exact certificate gives

    boxed:

    Pair_400
      <
      0.266329.

Therefore

    boxed:

    Pair_400(I)
      <
      0.266329
      +o(1).

References:

    WP84_BALANCED_ORIENTATION_NORMALIZATION
    WP84_R400_EXACT_PAIR_LAYER
    WP84_R400_PRINCIPAL_SECTION_PAIR_STABILITY.

## 7. Balanced 2-vs-2 sector: connected/nonpair part

After the exact pair contractions are removed, the remaining balanced
ordinary-prime degree-four sector is the connected ordered-partition kernel.

The exact geometry gives:

1. four of the six balanced sign interleavings vanish identically on support;
2. on a fixed product-scale slice, the complete six-word connected kernel is
   a negative Brownian covariance kernel;
3. for unequal scales, the exact residual E obeys

       -dist(s-t,Z)
         <=
       E
         <=
       0;

4. multiplying by the finite Fourier trace can rotate that negative residual
   into a positive contribution only through the detuning remainder;
5. the exact commutator identity moves that detuning factor onto a rank-two
   endpoint carrier;
6. the threshold-feature decomposition reduces the entire positive remainder
   to finitely many endpoint Dirichlet families;
7. good-endpoint trimming plus Montgomery--Vaughan/Sobolev sampling gives

       endpoint debt
         =
         O(L^-1/2)
         =
         o(1).

Consequently, on the selected section I,

    boxed:

    Connected_4(I)
      <=
      o(1)

in the one-sided sense required for the fourth-moment upper bound.

No quantitative use of the model value Phi4=-1/60 is made.

References:

    WP84_FIXED_SCALE_CONNECTED_KERNEL
    WP84_CROSS_SCALE_SHARP_DETUNING
    WP84_DETUNING_COMMUTATOR_ENDPOINT
    WP84_DETUNING_FEATURE_MAXIMAL_REDUCTION
    WP84_GOOD_ENDPOINT_TRIMMING.

## 8. No word class is left over

Combining Sections 2--7 gives the exhaustive degree-four ledger

    w_400(I)

      =
      Pair_400(I)

      + SameSign_4

      + Unbalanced_4

      + ProperPower_4

      + Connected_4(I).

Every term on the right has already been assigned:

    Pair_400(I)
      <0.266329+o(1),

    SameSign_4
      =o(1),

    Unbalanced_4
      =o(1),

    ProperPower_4
      =o(1),

    Connected_4(I)
      <=o(1).

Therefore

    boxed:

    w_400(I)
      <=
      0.266329
      +o(1).

This is the exact promotion statement required by the centered quartic gate.

## 9. Final quartic assembly

The centered quartic identity is

    tau P4(H_{400,I})

      =
      1/2000
      +(213/1000) v_{400}(I)
      +(593/2000) w_{400}(I)
      +o(1).

The fixed-band variance satisfies

    v_{400}(I)
      <=
      1/3
      +o(1).

Hence

    tau P4(H_{400,I})

      <=
      1/2000
      +213/3000
      +(593/2000)(0.266329)
      +o(1)

      =
      boxed:

      0.1504665485
      +o(1).

Pay the matched full-to-band charge

    C_match/400
      =
      2.1728342265/400
      =
      0.00543208556625.

The o(d) principal-section deletion was performed at the bounded-consumer
level and costs only o(1).

Thus the complete bounded-consumer defect satisfies

    boxed:

    defect
      <=
      0.15589863406625
      +o(1).

Against the conservative record ceiling

    E_rec
      =
      0.163249981456072...,

the explicit asymptotic margin is

    boxed:

    0.007351347389822....

The zero-side conversion gives

    boxed:

    simple-zero coefficient
      >=
      0.6882027318675
      -o(1)

      =
      68.82027318675...%
      -o(1).

## 10. Evidence status

This note closes the internal six-item bookkeeping replay requested by
`WP84_R400_FIRST_RECORD_ASSEMBLY.md`.

The branch can now distinguish two statements:

**Internal theorem-side closure:** the cited lemmas, taken as proved with their
stated normalizations, imply the 68.82027318675...% asymptotic coefficient.

**External theorem promotion:** before public unconditional presentation, the
load-bearing analytic inputs should receive one hostile source audit,
especially:

- the good-endpoint Montgomery--Vaughan sampling step;
- uniformity of the endpoint-feature second-mass normalization;
- the fixed-R covariance/source normalization used by Pair_400;
- the bounded full-to-band constant C_match;
- the zero-count/simple-zero conversion.

No new arithmetic lemma remains inside the degree-four word ledger itself.

See:

    notes/WP84_R400_FIRST_RECORD_ASSEMBLY.md
    notes/WP84_R400_PRINCIPAL_SECTION_PAIR_STABILITY.md
    notes/WP84_GOOD_ENDPOINT_TRIMMING.md
