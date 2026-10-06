# WP84 — full-sharp mean/variance retuning of the sine-square consumer

Date: 2026-10-06

Status: **EXACT GLOBAL SUPPORT-FREE RETUNING; FULL-SHARP MODEL LEDGER IMPROVED AND THE REMAINING THEOREM REDUCED TO ONE BOUNDED TRACE-VARIANCE GATE**

No unconditional zero-density percentage is claimed here.

The sine-square family is

    S_a(H)
      =
      2aH/(H^2+a^2),

    Q_{a,t}
      =
      I-tS_a(H),

    P_{a,t}
      =
      Q_{a,t}^2.

For every a,t>0,

    1-P_{a,t}(x)
      <=
      1_{x>0}

globally.

The full-sharp theorem does not need to optimize the same objective as the
fixed-band O(1/R) route.

The natural full-sharp objective is instead:

1. lower-bound the mean tau(S_a) from the source-closed first two moments;
2. maximize the admissible trace variance of S_a.

That retuning gives a cleaner rational point.

## 1. Preferred full-sharp parameters

Use

    boxed:

    a=23/20,
    t=113/100.

These differ from the current fixed-band-conditioned point

    a=63/50,
    t=17/16.

The two points serve different theorem interfaces.

## 2. Exact quadratic lower minorant

For

    a=23/20,

define

    s_a(x)
      =
      2ax/(x^2+a^2),

and

    boxed:

    L_2(x)
      =
      -3/625
      +(16189/10000)x
      -(819/1250)x^2.

Then

    boxed:

    s_a(x)-L_2(x)

      =
      N(x)
      /
      [
        4000000x^2+5290000
      ],

where

    N(x)
      =
      2620800x^4
      -6475600x^3
      +3485208x^2
      +636019x
      +25392.

The denominator is strictly positive.

Exact Sturm count:

    boxed:
    N has zero real roots.

Also

    N(0)=25392>0,

and the leading coefficient is positive.

Hence

    boxed:
    L_2(x)<=s_a(x)

for every real x.

## 3. Source-closed mean gate

Using

    tau(H)=1+o(1),

    tau(H^2)=4/3+o(1),

the minorant gives

    boxed:

    tau(S_a)

      >=
      1481/2000
      +o(1)

      =
      0.7405+o(1).

This uses no fourth moment and no local resolvent theorem.

## 4. Exact mean/variance decomposition

Write

    mu_S=tau(S_a),

    sigma_S^2
      =
      tau(S_a^2)-mu_S^2.

Then

    boxed:

    tau(P_{a,t})

      =
      (1-t mu_S)^2
      +t^2 sigma_S^2.

For

    t=113/100,

the mean lower bound gives

    boxed:

    (1-t mu_S)^2

      <=
      (
        1
        -(113/100)(1481/2000)
      )^2

      =
      1065826609/40000000000

      =
      0.026645665225.

Therefore a sufficient full-sharp theorem is

    boxed:

    Var_tau(S_a)
      <
      0.1069812171909....

This is the complete remaining scalar gate after the first two moments.

## 5. Exact pinned-model benchmark

At the pinned model,

    boxed:

    E_model[S_a]
      =
      325240778083160
      /
      405859957296217

      =
      0.8013620763424636...,

and

    boxed:

    E_model[S_a^2]

      =
      119473137226275432821220460800
      /
      164722304936487086853082511089

      =
      0.7253003002376721....

Therefore

    boxed:

    Var_model(S_a)

      =
      13691573498136102617344875200
      /
      164722304936487086853082511089

      =
      0.0831191228377677....

The variance cushion is

    boxed:

    0.1069812171909...
      -
    0.0831191228378...

      =
      0.0238620943531....

## 6. Exact model defect energy

The full sine-square defect energy at the retuned point is

    boxed:

    E_model(P)

      =
      473814077352141196977236513933
      /
      4118057623412177171327062777225

      =
      0.1150576608395159....

Thus the model positive-index lower bound is

    0.8849423391604841...,

and the corresponding model simple-zero ledger is

    boxed:

    76.98846783209682...%.

This is a model benchmark only.

The conservative raw defect-energy margin is

    boxed:

    0.163249981456072...
      -
    0.1150576608395159...

      =
      0.0481923206165561....

## 7. Comparison with the previous sine-square point

Previous fixed-band-conditioned point:

    a=63/50,
    t=17/16,

    model simple ledger
      =
      75.5063108085...%,

    model variance
      =
      0.08687459834...,

    variance-gate cushion
      ~=
      0.02065.

New full-sharp mean/variance point:

    a=23/20,
    t=113/100,

    model simple ledger
      =
      76.9884678321...%,

    model variance
      =
      0.08311912284...,

    variance-gate cushion
      =
      0.02386209435....

Thus the new point is preferred for the **full-sharp mean/variance route**.

## 8. Keep the fixed-band point separate

The direct differentiated-resolvent band constant at the new point is

    C_sine
      ~=5.90825,

so its margin-to-band-cost ratio is slightly worse than the
a=63/50,t=17/16 point.

Therefore the route split is:

### Full sharp direct route

Use

    boxed:
    a=23/20,
    t=113/100.

Primary theorem target:

    boxed:
    Var_tau(S_a)
      <
      0.1069812171909....

### Fixed-band fallback

Keep

    a=63/50,
    t=17/16,

because it has the better current O(1/R) conditioning constant.

Do not force one parameter choice to serve both theorem interfaces.

## 9. Evidence boundary

Closed:

- exact support-free sine-square family;
- exact global quadratic mean minorant;
- exact first-two-moment mean lower bound;
- exact mean/variance decomposition;
- exact pinned-model mean, second moment, variance, and defect energy.

Open:

- the full-sharp bounded variance theorem

      Var_tau(S_{23/20})
        <
      0.1069812171909....

No unconditional record theorem is claimed.

See:

    notes/WP84_SINE_MEAN_VARIANCE_GATE.md
    notes/WP84_SINE_TWO_VECTOR_WEDGE.md
    notes/WP84_SINE_SCALAR_K2_WEDGE.md
