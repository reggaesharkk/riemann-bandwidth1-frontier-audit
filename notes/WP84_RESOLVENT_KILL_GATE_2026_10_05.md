# WP84 resolvent kill gate -- 2026-10-05

Status: **BOUNDED SIX-POLE >79 CONSUMER ACTIVE; FULL-LAW IDENTIFICATION NO LONGER NECESSARY FOR THE FIRST >79 TARGET**

No unconditional >79 theorem is claimed.

## 1. Exact structural facts already closed

- Every intermediate matrix in the Lindeberg path is Hermitian, so for
  nonreal z

      ||(H-zI)^(-1)|| <= 1/|Im z|

  deterministically.

- Prime-power blocks satisfy

      max_j ||B_j|| = O(1/L),
      sum_j ||B_j||^2 = O(1),
      sum_j ||B_j||^3 = O(L^-3)=o(1).

- The exact one-block resolvent identity reduces the bounded fixed-z problem
  to conditional first/second-order operators plus an o(1) cubic remainder.

- Non-cyclic translation-word traces obey the exact spread law

      tr(word)=max(0,N-(max partial_sum-min partial_sum))

  for closed words.

- o(d)-rank perturbations are invisible to the weak/Stieltjes limit:

      |m_A(z)-m_B(z)|
        <= pi rank(A-B)/(d Im z).

## 2. Closures already rejected

- scalar covariance/multiplication closure:
      centered m4=7/30 instead of 1/4;

- finite F/G unitary state:
      repeated evolution generates longer translation words;

- Radau beta values:
      surrogate evaluations, not moment-forced lower bounds;

- prolate sharp-window counting-statistic spectral identification:
      failed its low-order gates;

- raw finite higher-even moment route:
      exposed to the Proposition-R amplification barrier.

## 3. Exact polynomial half-line certificate

Let

    P(x)
      = 1
        - (43428/13891)x
        + (37704/13891)x^2
        - (9660/13891)x^3,

    g(x)=P(x)^2.

For the pinned model moments through degree six,

    integral g dnu = 1415/13891,

and the coefficient-sign identity gives

    g(x)>=1 for x<=0.

Therefore every representing probability measure on R satisfies

    nu((-infinity,0]) <= 1415/13891.

This is support-free.

## 4. Active bounded consumer

For delta=61 define

    F_61(x)
      = 62 g(x)/(g(x)+61).

Then

    F_61(x)>=1 for x<=0,

and

    0 <= F_61(x) <= (62/61) g(x).

Hence every pinned-moment model law satisfies

    integral F_61 dnu
      <= 87730/847351
      = 0.1035344267....

The exact counting ledger then gives the bounded-consumer coefficient

    boxed:
    671891/847351
      = 0.7929311466... > 0.79.

This sacrifices part of the 79.627% polynomial optimum in exchange for a
bounded theorem interface.

## 5. Six simple fixed poles

The denominator

    P(z)^2+61

has six simple nonreal roots.  Numerically

    min_j |Im z_j| ~= 1.0760.

With residues

    c_j
      = -61*62/[2 P(z_j)P'(z_j)],

we have

    F_61(x)
      = 62 + sum_j c_j/(x-z_j).

Thus the active theorem target is the single bounded statistic

    L_61(T)
      = 62 + sum_j c_j m_{H_T}(z_j).

A sufficient theorem is

    boxed:
    limsup_T L_61(T)
      <= 87730/847351.

After the vanishing-threshold correction and o(d)-rank deletion, this yields
the >79 asymptotic simple-zero bound.

No contour derivatives and no full limiting spectral law are required for
this first bounded target.

## 6. Order-four consistency gate

Any proposed operator-valued closure used to prove the six-pole inequality
must pass the exact order-four model check.

The pair sector is

    2*t_adj + t_opp
      = 2*(7/60)+1/30
      = 4/15.

The connected core is

    Phi4=-1/60.

Therefore

    centered m4
      = 4/15 - 1/60
      = 1/4.

The exact latest-block decomposition locates:

- every 2+2 pair word in the second-order sector A2;
- every four-distinct word in the first-order history A1;
- mixed 2+1+1 words across both.

Hence a static covariance-only law cannot close the theorem.

## 7. Proposition-R firewall

The order-four coefficient is a **model/generator consistency gate only**.
Do not prove the theorem by extracting finite-T raw theta^4 derivatives.

The theorem itself stays at the six fixed nonreal poles of F_61.

Bounded rational probes may recover moments only **after** a limiting law has
been identified; see

    notes/WP84_BOUNDED_RATIONAL_MOMENT_RECOVERY.md.

## 8. Current analytic debt

At each of the six poles z_j, use the exact permutation-Lindeberg identity

    m_H(z_j)-m_S(z_j)
      = -A1(z_j)+A2(z_j)+o(1).

The remaining task is to prove the **weighted six-pole inequality**

    limsup_T
      [62 + sum_j c_j(
          m_S(z_j)-A1(z_j)+A2(z_j)
      )]
      <= 87730/847351.

The active attack must preserve:

1. the alternating/crossing 2+2 word geometry;
2. the connected non-pair state memory;
3. the actual prime-block arithmetic interface.

That six-pole scalar inequality is the current kill gate.
