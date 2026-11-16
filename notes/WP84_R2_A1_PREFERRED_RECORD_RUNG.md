# WP84 — r2 at a=1 as the preferred first record theorem rung

Date: 2026-10-05

Status: **EXACT MODEL/CONSUMER CERTIFICATE; ONE UPPER-HALF-PLANE POINT z=i PLUS ONE z-DERIVATIVE**

No unconditional zero-density percentage is claimed here.

The scaled-r2 note used a=3/2 for extra pole distance. The later
Bernoulli-to-Gaussian and co-moving heat-flow reductions only require a fixed
positive distance from the real line. Therefore the simpler member a=1 is a
stronger first theorem target.

Define

    r_2(x)
      = 1 - [ (x-1)^2/(x^2+1) ]^2.

For x<=0, r_2(x)<=0. For x>0, 0<r_2(x)<=1. Hence

    1_{x>0} >= r_2(x)

for every real x. Also -3<=r_2(x)<=1, so the consumer is bounded and
Proposition-R safe.

Its exact partial fraction formula is

    r_2(x)
      = (2+i)/(x-i) - 1/(x-i)^2
        + (2-i)/(x+i) - 1/(x+i)^2.

Thus for Hermitian H,

    tau r_2(H)
      = 2 Re[ (2+i)m_H(i) - m_H'(i) ].

Only z=i and one z derivative are required.

The existing exact rational-minorant hierarchy evaluates the pinned model
value as

    q_1
      = 2575059657047327248
        /2914998924731524849
      = 0.8833827124943086....

The corresponding model simple-zero ledger is

    2 q_1 - 1
      = 2235120389363129647
        /2914998924731524849
      = 0.7667654249886171....

So the model rung is

    76.67654249886171...%.

This is a model/consumer value, not an unconditional theorem.

Against the public comparison

    C_pub=0.67350003708785588766...,

the positive-index threshold is

    q_pub=(1+C_pub)/2
         =0.8367500185439279....

Therefore the model consumer margin is

    q_1-q_pub
      =0.0466326939503807....

This is substantially larger than the a=3/2 margin
0.0165040971... and the F9 margin 0.0112742976....

Even against the repository's conditional eta-retuned scalar line

    C_retuned=0.6735000520898147,

the positive-index threshold is 0.83675002604490735 and the model margin
remains about 0.04663268645.

The pole distance |Im z|=1 is acceptable for every currently active
fixed-pole argument:

- ||R(i)||<=1;
- Bernoulli-to-Gaussian replacement requires only fixed eta_0>0;
- background/taper transfer works at fixed nonreal poles;
- m'(i)=tau(R(i)^2) may be used directly.

If a Cauchy circle is ever preferred, radius 1/2 stays a fixed distance
1/2 from the real axis.

Using the co-moving heat-flow note with a=1 gives

    tau r_2(H_1)
      = -2 Re int_0^infinity
          [ (2+i) C_u(i) - partial_z C_u(i) ] du

at finite d, with the large-u boundary issue separated explicitly there.

The preferred first theorem target is therefore

    liminf_T tau r_2(H_T)
      > 0.8367500185439279....

The model margin available for all analytic errors is about

    0.04663269395.

Recommended order:

1. attack r2,a=1 at z=i;
2. keep a=3/2 and F9 as robustness cross-checks;
3. after the first theorem crossing, move to r3 at z=i or the six-pole
   Christoffel family.

The existing exact hierarchy already gives r3 at a=1 a model simple ledger
above 79%, so the one-point repeated-pole route also has a natural second
rung.

See:

    src/wp84_rm_model_hierarchy.py
    notes/WP84_SCALED_R2_RECORD_RUNG.md
    notes/WP84_R2_COMOVING_GAUSSIAN_HEAT_FLOW.md
