# WP83 — successor retraction / Proposition-R barrier audit

Date: 2026-10-04
Status: **CRITICAL EXTERNAL FALSIFIER; unconditional higher-even-moment route downgraded pending an independent Proposition-R resolution**

## 1. New upstream fact

The same public research program later created `JoshuaHKU/zeta-density-one-reproduction`. On 2026-09-03 commit

    ac851520f1d135a56d2911ff512011feab2a32dd

retracted the central unconditional higher-moment claims.

`RETRACTION.md` states explicitly that unconditional convergence of the higher even trace moments, beginning with the `mu_4 -> 13/4` tier, and the density-one consequences are retracted.

The stated reason is a reviewer argument called **Proposition R**, which the program says it verified and strengthened: finite unconditional higher-even-moment bounds of the claimed strength would force power-law-strength zero-free regions, far beyond the declared analytic inputs. The program says the essential gap was located and the claims do not survive.

## 2. This is directly relevant to our project

Our exact model/consumer algebra is not invalidated by this retraction:

- exact connected/polytope constants;
- exact Christoffel certificates;
- exact m7 Stieltjes floor;
- exact one-sided m7/m8 consumer;
- exact S4 local coupling / CRT identities;
- exact {5,2} and C7 model computations.

Those are finite algebraic/model statements.

What is affected is the **unconditional analytic transport** from zeta to a finite fourth or higher trace moment.

Our Stage-A target

    R <= -1/48 + o(1)

would give a finite unconditional fourth-moment upper bound. Therefore it lies exactly in the class of statements that the successor retraction warns are constrained by Proposition R.

Likewise the 79.627% and >80% consumers become unconditional only if m4,m5,m6,m7,m8 are transported. The retraction is therefore not peripheral: it attacks the analytic premise of the whole higher-moment ladder.

## 3. Independent corroboration in the predecessor repository

The predecessor `zeta-0.7947-reproduction` currently has an open issue titled

    Proposition 5.3: the cell weight does not decay in the modulus

which independently identifies the same truncation problem we found:

- global ell_1 is a fixed normalization, not a cell variable;
- the shipped k=4 outer weight is Lambda(b1)Lambda(b2)/(b1 b2);
- a fixed polylog cutoff retains a vanishing fraction of the normalized Mertens mass;
- the archived D1 truncation layer is absent from the reproduction package;
- the unrestricted large-modulus Lemma D is stated by the paper itself to remain open.

A later comment on that issue points to the successor retraction and asks whether the 0.7962 theorem is thereby superseded.

## 4. Evidence-grade correction

Effective immediately, the private project must distinguish:

### Exact/model/consumer layer — ACTIVE

Exact rational computations remain valuable and may continue. They tell us what would follow from moment inputs and give target inequalities such as the exact >80 corridor.

### Unconditional higher-moment theorem layer — BLOCKED BY PROPOSITION R

No `mu_4`, `mu_6`, `m7/m8`, 71.164%, 79.627%, or 80% statement may be promoted unconditionally merely by repairing the local glue/truncation write-outs.

A valid route must first do one of the following:

1. independently disprove or evade Proposition R because our object/hypotheses differ;
2. prove the zero-free/zero-density input that Proposition R says a finite higher-even-moment bound requires;
3. replace the higher-even-moment transport with a genuinely different consumer that does not imply the forbidden zero-free strength.

## 5. What not to throw away

The j-first S4 work remains strategically useful for two reasons:

- it precisely identifies the analytic object whose claimed unconditional variance estimate must now be tested against Proposition R;
- if one later adds an explicit zero-free/zero-density hypothesis, the exact S4 and consumer machinery may become a rigorous conditional theorem.

But we should stop treating S4/Lemma-D closure as 'just bookkeeping'. The successor retraction says the missing analytic strength is qualitatively deep.

## 6. New theorem-side priority

The next theorem-side task is **Proposition-R reconstruction**:

- derive, from the compressed-Weil matrix definitions, exactly what finite fourth/even moment bound implies about off-line zeros;
- quantify the zero-free or zero-density consequence;
- compare that consequence with the precise strength of our Stage-A one-sided R bound;
- determine whether one-sided fourth-moment control already triggers the barrier or whether only two-sided convergence does.

Only after that audit do we decide whether Stage A is salvageable, conditional, or should be retired.

## 7. Compute-side policy

C7 and {5,2} may continue because they are exact finite/model certificates and do not consume the disputed analytic transport. Their claim label remains **conditional/model-side**.

PR #5 remains draft and must not merge.


## 8. One-sided Stage-A is inside the stated barrier

The successor retraction is stronger than a rejection of exact convergence: it states that **finite unconditional bounds on higher even moments** already force power-law zero-free information. Therefore the Stage-A goal, which is an unconditional finite upper bound on the normalized fourth moment, is not exempt merely because it is one-sided.

Conditional on the missing globalization/isolation lemma of Proposition R, the exponent calculation in `WP83_PROPOSITION_R_AGGREGATION_BARRIER.md` gives

    |beta-1/2| <= 1/(4*lambda)+o(1)

from any finite fourth-moment bound at bandwidth X=T^lambda. At lambda=1 this would confine all active-window zeros to the fixed strip [1/4,3/4]+o(1), far stronger than the declared analytic inputs.

Accordingly, Stage A remains useful as an audit/model decomposition but is **not an unconditional theorem route** until Proposition R is independently resolved.
