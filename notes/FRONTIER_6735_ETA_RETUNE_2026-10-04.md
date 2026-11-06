# Exact eta retune above the public 67.350003708785593% freeze

Date: 2026-10-04

## Classification

**EXACT_SCALAR_IMPROVEMENT_CONDITIONAL_ON_IMPORTED_STRICT_LOCAL_CERTIFICATES**

This note records a strict scalar improvement of the public VeriLoop-E2 q=8
assembly.  It does not claim an independent replay of VeriLoop's
190,375,830-node local certificate layer or completion of its upstream analytic
normalization bridge.

## Imported certified local inputs

We use the public frozen q=8 strict certificate constants without modification:

- q = 8;
- m = 531, n = 523;
- H = 672167187145431 / 10^15;
- B = 93/23000;
- slope 1/2: epsilon = 526/78125;
- slope 19/20: epsilon = 9879/1250000;
- slope 1: epsilon = 20033/2500000.

The public release reports the three fail-closed local proofs as 23,644,472,
75,294,070, and 91,437,288 nodes respectively, for 190,375,830 nodes total,
plus a 327/327 difficult-well check.

Its published scalar freeze takes eta=1 and gives the exact fraction

[
C_{m pub}=
rac{722547711262091300265625000000000}
     {1072825050442925667061714615173641}
=
0.6735000370878558876607112201ldots
]

## Free scalar parameter

The public finite theory permits any multiplier eta >= 0:

[
p(E)=maxleft(0,max_s(nepsilon_s-sE)ight),
]

[
R(eta)=inf_{Ege0}left(h(E)+eta p(E)ight),
]

and

[
C(eta)=
rac{mH-eta B(m-q)}
     {m-R(eta)}.
]

Therefore eta=1 is a design choice, not a mathematical requirement.

## Retuned rational eta

We choose the exact rational

[
eta'=
rac{99988220836693}{10^{14}}
=
0.99988220836693.
]

This lies extremely close to the switch where the E=0 pressure endpoint and
the active interior pressure kink balance.

No local certificate is changed.  In particular, no new transcendental B&B
claim is introduced by this retune.

## Exact finite minimization

For q=8,

[
T=rac98,qquad d=16.
]

On E>T the profile is

[
h(E)=
rac{E}{17}
+rac{32}{17}sqrt{ET}
-rac{16}{17}T.
]

The checker evaluates a finite superset of every endpoint at which
(h(E)+eta'p(E)) can attain its infimum:

- E=0;
- E=T;
- the zero of every pressure line;
- every pairwise pressure-line intersection.

The winning candidate is exactly

[
oxed{E_*=rac{5753}{5000}=1.1506}.
]

Square roots are replaced by 120-decimal rational lower bounds generated with
integer square root.  Thus the resulting R value is a rigorous lower bound,
not a floating approximation.

The computed bound is

[
Rge
4.190409946620914418236475413456207423782442786978314632ldots
]

in the conservative direction required by the final denominator.

## New exact lower bound

Substituting this R lower bound gives

[
C>
0.6735000520898147515049271277577013701813356794080647676ldots
]

and therefore the clean fixed headline

[
oxed{C>0.6735000520898147}.
]

Equivalently,

[
oxed{67.35000520898147%}.
]

The exact rational checker proves a strictly positive margin above that fixed
headline.

It also proves

[
C_{m retuned,lower}-C_{m pub}
>
1.5001958863844215	imes10^{-8}
]

in proportion, about

[
1.500195886	imes10^{-6}
]

percentage points.

## Why this matters

The gain is deliberately small, but it has a useful property: it requires
**zero additional local B&B nodes**.  It exploits a free scalar degree of
freedom after the expensive q=8 certificate has already been established.

This demonstrates that the public eta=1 scalar assembly was not itself
fully optimized.

## Reproduction

Run:

`python src/frontier6735_eta_retune_exact.py`

Expected final line:

`RESULT: EXACT_ETA_RETUNE_PASS`

The checker uses only Python's standard library and exact integer/Fraction
arithmetic for every acceptance decision.

## Claim boundary

What this establishes:

- exact retuning of the published q=8 scalar assembly;
- strict arithmetic improvement over the public exact eta=1 fraction;
- fixed headline (0.6735000520898147) under the same certified local premises.

What it does **not** yet establish independently:

- a fresh replay of the three 190,375,830-node local interval certificates;
- a source-free reimplementation of their transcendental verifier;
- an end-to-end formal proof of the imported analytic D0/normalization layer;
- peer-reviewed or community-accepted record status.

The next high-value task is to independently replay/audit the q=8 certificate
and then tighten the active q=8 local epsilons before paying the dimensional
cost of q=9/q=10/q=12.
