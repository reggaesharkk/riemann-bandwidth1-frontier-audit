# WP71 — exact joint-major denominator classification

Date: 2026-10-04
Status: **ARITHMETIC DENOMINATOR PART CLOSED; ARC-WIDTH SEPARATION REMAINS**

Let an additive-frequency rational center be reduced:

    alpha0 = a/q_arc,  gcd(a,q_arc)=1.

Under dilation by an integer b,

    b*alpha0 = b*a/q_arc

has reduced denominator

    q_b = q_arc/gcd(q_arc,b).

For the two Stage-A prime sums this gives

    q_m = q_arc/gcd(q_arc,b2),
    q_n = q_arc/gcd(q_arc,b1).

Assume both dilated frequencies are in a P-major denominator class:

    q_m <= P,  q_n <= P.

Then immediately

    q_arc <= P*b1,
    q_arc <= P*b2.

For the third bound put g=gcd(b1,b2). Prime by prime,

    gcd(q_arc,b1)*gcd(q_arc,b2)
      <= q_arc*g.

Hence

    q_arc
      <= q_m*q_n*g
      <= P^2*g.

Therefore

    boxed:
    q_arc <= min(P*b1, P*b2, P^2*g).

This is exactly the denominator shape quoted in the public candidate's joint-near-major classification.

The companion exact integer checker is `src/wp71_joint_major_denominator.py`.

## What is not closed by this lemma

This is only denominator arithmetic. For **near** major arcs one must also prove that two independently chosen rational centers cannot both lie within the dilated arc widths unless their underlying rational centers are compatible. That requires a separation inequality using the actual Stage-A/MRT arc widths.

Once that width inequality is written, the joint-major family is finite in the required sense; outside it at least one dilated prime sum is minor and can be sent to Vaughan/MRT.
