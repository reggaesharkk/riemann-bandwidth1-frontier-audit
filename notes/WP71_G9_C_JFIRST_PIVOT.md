# WP71 G9-C — j-first four-point pivot

Date: 2026-10-04
Status: **EXACT ALGEBRA CLOSED; analytic four-point deviation theorem becomes the target**

The Stage-A scale audit killed the n-first pointwise welding route: for fixed n the hard window I_k(n) contains only O(1) candidate m-values.

The correct move is to change the order of analysis, not to seek a short-interval prime-pair theorem.

## 1. Keep j and k outside

For fixed b1,b2 let

    A(j) = sum_m Lambda(m)Lambda(n),
    n=(b2*m+j)/b1,

with the original block/support conditions.

Write g=(b1,b2), r=b1/g, q=b2/g. Define

    N4(k,j)
      = sum_m Lambda(m)Lambda(m-rk)
              Lambda(n)Lambda(n-qk),

where n=(b2*m+j)/b1 and all four variables remain in their original windows.

Equality of the two lock values in A(j)^2 forces

    m' = m-rk,
    n' = n-qk.

Hence, **pointwise in j**,

    boxed:  A(j)^2 = sum_k N4(k,j).

The companion script `src/wp71_g9_c_jfirst_identity.py` checks this with exact integer arithmetic on unrelated weighted systems.

## 2. Why this avoids the O(1)-window obstruction

For fixed n, the m-window is O(1). But for fixed (k,j), the variable m runs across the full outer block subject to one affine relation

    b1*n-b2*m=j.

That is the long averaged object on which spectral/circle-method technology can act.

So the same finite four-prime tuples admit two orderings:

- n-first: produces the bad short welding window w_k(n);
- j-first: produces the long four-point correlation N4(k,j).

The algebra is identical; only the analytic ordering changes.

## 3. Center at the four-point model before Cauchy--Schwarz

Let

    M4(k,j) = S4(k,j) V(k,j)

be the correct four-point singular-series/Archimedean model in the same window convention, and put

    E4(k,j)=N4(k,j)-M4(k,j).

Then for any deterministic cell weight W(k,j),

    sum_{k,j} W(k,j) N4(k,j)
      = sum_{k,j} W(k,j) M4(k,j)
        + sum_{k,j} W(k,j) E4(k,j).

The first term is the signed main and is where the G9-B Euler-factor/triangular calibration belongs.

Only the centered four-point remainder E4 is allowed into Cauchy--Schwarz.

## 4. Sufficient analytic theorem

A sufficient consumed theorem is the truncated four-point variance bound

    sum_{k<=K} sum_{|j|<=J} |E4(k,j)|^2
       <<_{A,B} K*J*V^2*(log X)^(-A)

uniformly for the polylogarithmic modulus family and the actual smooth/block windows.

If |W| and the number of cell families cost only fixed powers of log X, then

    |sum W E4|
      <= (sum |W|^2)^(1/2) (sum |E4|^2)^(1/2)

costs only half of the requested logarithmic saving. Since A is arbitrary, choose it larger than all deterministic log losses.

This use of Cauchy--Schwarz is fundamentally different from the rejected whole-band pair-dispersion bound: the Poisson/diagonal main has already been placed inside M4. We are squaring the **centered four-point error**, not the raw pair fluctuation A-MT.

## 5. Relation to the public spectral Lemma-D candidate

The public candidate states essentially this four-point L2 theorem as its truncated Lemma D. Its finite product/Parseval algebra is plausible and partly exact, but our hostile audit found that its mixed/minor size bookkeeping and comb-tail write-out still require independent proof.

Therefore we may use the public proof as a roadmap, not as an established theorem.

## 6. New G9-C target

G9-C is now:

1. independently reconstruct the weighted/truncated four-point variance theorem in the exact Stage-A conventions;
2. prove its spectral major-major, mixed/minor, and singular-series comb leaves;
3. feed it to the exact j-first identity above;
4. use G9-B only for the signed main;
5. perform G9-D normalization of the deterministic weight L2 budget.

No pointwise asymptotic for w_k(n) is required.
