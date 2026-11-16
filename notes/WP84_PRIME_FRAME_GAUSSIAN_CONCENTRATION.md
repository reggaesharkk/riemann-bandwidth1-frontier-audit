# WP84 — prime-block frame bound and Gaussian resolvent-trace concentration

Date: 2026-10-05

Status: **NEW THEOREM-SIDE BOUND — ORDINARY-PRIME SHARP QUADRATURE BLOCKS HAVE HILBERT-SCHMIDT FRAME NORM O(L^-2); FIXED-POLE GAUSSIAN RESOLVENT TRACE CONCENTRATES AT O(L^-1)**

No percentage theorem is claimed here.

The artificial quadrature bridge introduces independent Gaussian coefficients
in the ordinary-prime cosine/sine directions.

A priori one could worry that its normalized resolvent trace has order-one
random fluctuations.

The adaptive endpoint deletion plus the exact two-word Dirichlet trace show
the opposite.

## 1. Ordinary-prime quadrature directions

For each retained ordinary prime p<=N define the two Hermitian sharp
directions

    C_p=A_p+A_p^*,

    S_p=i(A_p-A_p^*),

including the normalized coefficient

    kappa_p
      = log p/(a L sqrt p).

Use the normalized Hilbert-Schmidt inner product

    <X,Y>_tau
      = tau_d(X^*Y)
      = d^(-1) tr(X^*Y).

The one-block operator bound gives

    ||C_p||_op+||S_p||_op
      <= C log p/(L sqrt p),

and therefore

    ||C_p||_(2,tau)^2,
    ||S_p||_(2,tau)^2

      <= C (log p)^2/(L^2 p).

In particular the diagonal Gram entries are

    O(L^-2)

uniformly in p.

## 2. Off-diagonal Gram entries are two-word leakage

For p!=q every normalized Hilbert-Schmidt product between one p-quadrature
and one q-quadrature is a linear combination of sharp two-shift traces.

The possible net displacements are

    +/- log p +/- log q.

By the exact spread--Dirichlet trace identity:

- same-sign displacement log(pq) costs O(1/T);
- mixed displacement log(p/q) costs

      O(
        1/[T |log(p/q)|]
      ).

For distinct integers p,q,

    |log(p/q)|
      >= c |p-q|/max(p,q)

in the close range.

Hence every off-diagonal quadrature Gram entry obeys

    boxed:
    |G_pq|

      <=
      C (log p)(log q)/(L^2 sqrt(pq))
      [
        max(p,q)/(T|p-q|)
        + 1/T
      ].

No prime-pair theorem enters.

## 3. Uniform row sum

Fix p.

For p/2<q<2p, enlarge the prime sum to all integer gaps h=|p-q|.

Then

    sum_close |G_pq|

      <=
      C (log(2p))^2/(L^2 T)
        sum_{1<=h<=2p} 1/h

      <=
      C (log(2p))^3/(L^2 T)

      <= C L/T.

For q>=2p, use |log(q/p)|>=log 2 and the elementary estimate

    sum_{q<=N} log q/sqrt q
      <= C sqrt(N) log N.

This gives a tail

    <=
    C sqrt(N)/T

up to harmless logarithmic factors.

The q<=p/2 tail is smaller.

Under the adaptive endpoint deletion

    N/T -> 0,

and T=e^(L+o(L)), so all off-diagonal row sums are

    o(L^-2).

Therefore the full cosine/sine block Gram matrix satisfies

    boxed:
    ||Gram||_op
      <= C/L^2.

## 4. Bessel/frame inequality

Equivalently, for every d by d matrix A,

    boxed:
    sum_p [
      |tau(A^* C_p)|^2
      + |tau(A^* S_p)|^2
    ]

      <=
      C/L^2
      * tau(A^*A).

This is the matrix-block analogue of the large-sieve/Bessel bound for
well-separated logarithmic prime frequencies.

The decisive spacing ratio is

    (minimum log-frequency separation)^(-1) / d
      = O(N/T)
      = o(1).

## 5. Gaussian Poincare for the bridge resolvent trace

Use the quadrature noise directions

    E_{p,c}=C_p/sqrt2,
    E_{p,s}=S_p/sqrt2.

At bridge variance v=t(1-t), for

    m_t(z)=tau(R_t(z)),

    partial_{g_j} m_t
      = -sqrt(v) tau(E_j R_t^2).

Gaussian Poincare therefore gives

    Var m_t(z)
      <=
      v sum_j
        E|tau(E_j R_t^2)|^2.

Apply the frame inequality with

    A=(R_t^2)^*.

For Im z>=eta>0,

    tau(A^*A)
      <= eta^(-4).

Hence

    boxed:
    Var m_t(z)
      <=
      C v/(L^2 eta^4).

Uniformly on the four F9 poles,

    sd[m_t(z)]
      = O(L^-1).

Thus the normalized resolvent trace of the artificial Gaussian bridge is
asymptotically deterministic at every consumed fixed pole.

## 6. Derivatives and fixed circles

The same argument applies to

    tau(R_t^k)

for every fixed k, with a larger fixed power of eta^(-1).

Consequently Cauchy-circle derivatives used by bounded rational consumers
also concentrate.

This is a fixed-imaginary-part statement; no microscopic random-matrix local
law is needed.

## 7. What this closes and what remains

Closed:

- order-one stochastic fluctuations of the bridge trace are ruled out;
- standard MDE "self-averaging" is available here from prime-log spacing and
  the exact two-word trace, not from flatness.

Still open:

- identify/bound the deterministic expectation of the bridge resolvent;
- control the deterministic arithmetic drift P_full strongly enough for F9;
- close the small-generator expectation equation.

This is the first bespoke fixed-pole concentration input toward that
expectation equation.

See:

    notes/WP84_GAUSSIAN_QUADRATURE_BRIDGE.md
    notes/WP84_CONTINUOUS_SPREAD_DIRICHLET_TRACE.md
    notes/WP84_CIRCULAR_GAUSSIAN_Q_FIELD.md
