# WP84 — exact quartic majorant reduces the fixed-band first strike to one-sided moments through order four

Date: 2026-10-05

Status: **EXACT GLOBAL MAJORANT + EXPLICIT ROBUST MOMENT BUDGET FOR THE FIXED-BAND MATCHED FILTER**

No unconditional zero-density percentage is claimed here.

The matched two-pole route gives

    tau f_match(H)
      >=
      tau f_match(H_R)
      - C_match/R
      + o(R^-1),

with

    C_match
      = 2.1728342265...,

and

    f_match(x)
      =
      1-g_match(x),

    g_match(x)
      =
      [(x-1)^2/(x^2+1)]
      [(x-9/4)^2/(x^2+81/16)].

The remaining fixed-band theorem can be reduced to a one-sided fourth-moment
problem.

## 1. Exact quartic polynomial

Define

    boxed:

    P4(x)
      =
      (593/2000) x^4
      -(212/125) x^3
      +(1761/500) x^2
      -(3133/1000) x
      +1011/1000.

Then

    boxed:

    P4(x)-g_match(x)
      =
      N4(x)
      /
      [
        2000
        (x^2+1)
        (16x^2+81)
      ],

where

    N4(x)
      =
      9488 x^8
      -54272 x^7
      +170225 x^6
      -429280 x^5
      +731653 x^4
      -674554 x^3
      +284698 x^2
      -39546 x
      +1782.

The denominator is strictly positive on R.

The exact Sturm count is

    boxed:
    N4 has 0 real roots.

Also

    N4(0)=1782>0

and its leading coefficient is positive.

Therefore

    boxed:
    P4(x)>g_match(x)

for every real x.

Hence

    boxed:
    1-P4(x)
      <
      f_match(x)
      <=
      1_{x>0}.

So after band truncation the bounded matched-filter theorem may be proved by
an upper bound on one quartic polynomial trace.

## 2. Exact model expectation

Using the pinned first four moments

    mu0=1,
    mu1=1,
    mu2=4/3,
    mu3=2,
    mu4=13/4,

we get exactly

    boxed:

    E_model P4
      =
      233/1600
      =
      0.145625.

Thus the induced model positive-index lower bound is

    boxed:
    1367/1600
      =
      0.854375,

and the corresponding model simple-zero ledger is

    boxed:
    0.70875
      =
      70.875%.

This is a model/consumer value only.

The quartic majorant deliberately gives up part of the matched-filter model
margin in exchange for a finite degree-four arithmetic theorem.

## 3. Record inequality after band truncation

Let

    E_rec
      =
      (1-C_rec)/2
      =
      0.163249981456072...

be the conservative positive-index defect ceiling.

A sufficient condition for the record crossing is

    boxed:

    tau P4(H_R)
      +
      C_match/R

      <
      E_rec.

For example:

    R=256:
      band charge
        ~=0.00848763370,

      remaining quartic budget
        ~=0.00913734776.

    R=400:
      band charge
        ~=0.00543208557,

      remaining quartic budget
        ~=0.01219289589.

    R=512:
      band charge
        ~=0.00424381685,

      remaining quartic budget
        ~=0.01338116461.

## 4. Exact robust moment budget

Write fixed-band moment bounds as

    mu1 >= 1-delta1,

    mu2 <= 4/3+delta2,

    mu3 >= 2-delta3,

    mu4 <= 13/4+delta4.

Because the P4 coefficients have signs

    x^4: positive,
    x^3: negative,
    x^2: positive,
    x:   negative,

we get

    tau P4(H_R)

      <=
      233/1600

      +(593/2000) delta4
      +(212/125) delta3
      +(1761/500) delta2
      +(3133/1000) delta1.

Therefore the exact sufficient record condition is

    boxed:

    (593/2000) delta4
    +(212/125) delta3
    +(1761/500) delta2
    +(3133/1000) delta1

      <
      E_rec
      -233/1600
      -C_match/R.

This is the new fail-closed arithmetic budget.

## 5. If the first three moments are at their target values

Set

    delta1=delta2=delta3=0.

Then the allowed fourth-moment ceiling is

    mu4
      <
      13/4
      +
      [
        E_rec
        -233/1600
        -C_match/R
      ]
      /(593/2000).

Numerically:

    R=192:
      mu4 < 3.27127533...

    R=256:
      boxed:
      mu4 < 3.28081736...

    R=320:
      mu4 < 3.28654258...

    R=400:
      boxed:
      mu4 < 3.29112275...

    R=512:
      mu4 < 3.29513040...

    R=768:
      mu4 < 3.29990142...

    R=1024:
      mu4 < 3.30228692....

For comparison, the sine-process target is

    13/4=3.25.

So even at R=256 the theorem does **not** need the exact fourth moment.
It only needs a one-sided upper bound roughly

    boxed:
    mu4(H_R)<3.2808

provided the lower moments are controlled sharply enough.

## 6. Why this is strategically important

The current one-Cayley rank-six and rational rank-four routes are bounded and
structurally elegant, but their final local-law target still contains all
resolvent degrees implicitly.

The quartic majorant gives a different fallback:

    full bounded matched filter
      -> O(1/R) band truncation
      -> exact global quartic majorant
      -> one-sided fixed-band moments through degree four.

This is precisely the degree at which the existing arithmetic programme is
already most developed:

- mu1 and mu2 are classical/source-closed;
- the mu3 reconstruction is already on the branch;
- degree four is the first balanced 2-vs-2 sector;
- the product-correlation bridge identifies it with weighted E2 /
  Lambda*Lambda correlations;
- the Phi4 support theorem localizes the connected correction entirely to
  the supercritical product side;
- Evans supplies the relevant average almost-prime correlation theorem in
  the long-shift range.

So the remaining hard theorem is no longer an all-degree local resolvent law
if this fixed-band fourth-moment bound can be proved.

## 7. Proposition-R firewall

Do not apply this quartic polynomial directly to the original full matrix.

That would reopen the raw-moment/outlier problem blocked by Proposition R.

The order is essential:

1. first compare the original bounded consumer f_match(H) with f_match(H_R)
   using the O(1/R) fixed-pole theorem;
2. only on the fixed-band matrix H_R use
       g_match(H_R)<=P4(H_R);
3. prove the required one-sided quartic bound for H_R.

This keeps the original theorem bounded and rank-robust.

## 8. New preferred arithmetic kill gate

Before attempting a global local-law theorem, test whether the existing
degree-four arithmetic machinery can establish, for a convenient fixed R,

    mu1(H_R) >= 1-o(1),

    mu2(H_R) <= 4/3+o(1),

    mu3(H_R) >= 2-o(1),

and for example at R=256

    boxed:
    mu4(H_R) < 3.28081736....

A larger fixed R relaxes the fourth-moment requirement further.

If this closes, the first record crossing follows without proving the full
rank-four/rank-six bounded-unitary local law.

See:

    notes/WP84_ONE_CAYLEY_RATIONAL_RANK4.md
    notes/WP84_BALANCED_PRODUCT_CORRELATION_BRIDGE.md
    notes/WP84_PHI4_SUPERCRITICAL_SUPPORT_THEOREM.md
    notes/WP70_1B_ROBUST_MOMENT_REGION.md
