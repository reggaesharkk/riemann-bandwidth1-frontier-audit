# WP71 — welding modulus versus MRT arc modulus

Date: 2026-10-04
Status: **MANDATORY NOTATION FIREWALL**

Two unrelated quantities were both previously called q. They must never be identified.

## 1. Welding modulus

From the exact lock reindexing,

    g=gcd(b1,b2),
    r_w=b1/g,
    q_w=b2/g,

and the structured prime-pair shifts are

    m' = m-r_w*k,
    n' = n-q_w*k.

Thus q_w is an arithmetic multiplier in the physical shift h=q_w*k. It can be large.

G2 handles the family of such structured shifts by multiplicity aggregation: a fixed h can occur only through divisors, giving multiplicity bounded by a divisor function. The arbitrary log saving in the all-shift theorem absorbs that multiplicity. G2 does **not** require q_w<=(log X)^B.

## 2. MRT / circle-method arc modulus

In MRT Proposition 3.4 and Proposition 5.4, q is the denominator q_arc of a rational approximation

    alpha = a/q_arc + beta,

with

    q_arc <= Q=(log X)^B.

This q_arc has nothing to do with q_w=b2/g.

For a dilated prime sum

    S_m(alpha)=sum Lambda(m) e(b2*m*alpha),

the rational part b2*a/q_arc reduces to denominator

    q_m = q_arc / gcd(q_arc,b2).

Likewise

    q_n = q_arc / gcd(q_arc,b1).

Therefore q_m,q_n<=q_arc<=Q automatically, regardless of the size of b1,b2. Large outer prime-power legs do not by themselves violate the logarithmic-denominator hypothesis.

## 3. Why this matters

Any Stage-A/MRT substitution table must have separate columns for:

- q_w: welding/structured-shift multiplier;
- q_arc: circle-method rational-approximation denominator;
- q_m,q_n: reduced denominators after dilation by b2,b1.

Identifying q_w with q_arc would incorrectly force the outer coefficients to be polylogarithmic and would discard a leading part of the Stage-A prime-power measure.

## 4. Remaining analytic issue

The denominator reduction is easy. The nontrivial part is the **arc width after dilation**:

    gamma_m=b2*alpha,
    gamma_n=b1*alpha.

The beta-errors are multiplied by b2 and b1. Hence one must classify when both dilated frequencies are near major arcs and otherwise show that at least one side is genuinely minor in its own approximation quality.

This is the correct role of the public candidate's 'joint near-major classification' and 'dilation transfer' lemmas.
