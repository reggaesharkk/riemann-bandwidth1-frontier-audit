# WP84 — unified small-channel formula for the D1/D2 primitives

Date: 2026-10-05

Status: **EXACT FINITE-DIMENSIONAL REDUCTION CLOSED; BOTH LINDEBERG PRIMITIVES ARE ONE-DIMENSIONAL SMALL-MATRIX FOURIER OBJECTS**

No percentage theorem is claimed here.

For one current sharp block B and one intermediate resolvent

    R(z)=(H-zI)^(-1),

the exact Lindeberg coefficients are

    D1=d/dz tau(BR),

    D2=(1/2)d/dz tau((BR)^2).

The previous LRSC/displacement work reduced the D2 primitive
`tr((BR)^2)` to a rank-four Fourier channel.

The D1 primitive `tr(BR)` admits an even smaller rank-two-by-rank-two
formula.

## 1. Cross displacement identity

Let

    D=diag(0,1,...,d-1).

For two matrices A and B define

    C_A=[D,A],
    C_B=[D,B].

For i!=j,

    A_ij=(C_A)_ij/(i-j),

    B_ji=-(C_B)_ji/(i-j).

Therefore

    boxed:
    tr(AB)
      = sum_i A_ii B_ii
        - sum_{i!=j}
            (C_A)_ij (C_B)_ji/(i-j)^2.

This is exact for arbitrary finite matrices.

## 2. Fourier representation of the cross term

With

    S2(t)=pi^2/3-pi t+t^2/2,

the Fourier coefficient identity for 1/r^2 gives

    boxed:
    sum_{i!=j}
      (C_A)_ij (C_B)_ji/(i-j)^2

      = (1/(2*pi))
          int_0^(2*pi)
            S2(t)
            tr(
              C_A e^(itD)
              C_B e^(-itD)
            ) dt.

The constant Fourier coefficient of S2 is zero, so no diagonal correction is
needed.

## 3. Low displacement ranks collapse the trace

Suppose

    C_A=G_A H_A^T,
    rank C_A<=r_A,

    C_B=G_B H_B^T,
    rank C_B<=r_B.

Then

    tr(
      C_A e^(itD)
      C_B e^(-itD)
    )

equals

    boxed:
    tr_{r_A}[
      (H_A^T e^(itD) G_B)
      (H_B^T e^(-itD) G_A)
    ].

Thus the d by d trace is reconstructed from an
r_A by r_B channel and its reverse.

## 4. Apply to the D1 primitive

For the current sharp block and intermediate resolvent,

    rank[D,B] <= 2,
    rank[D,R] <= 2.

Hence

    boxed:
    tr(BR)
      = sum_i B_ii R_ii
        - (1/(2*pi))
          int S2(t)
            tr_2[
              A_BR(t) A_RB(-t)
            ] dt,

where the two rectangular channel matrices are at most 2 by 2.

So the primitive whose z-derivative is D1 consists only of:

- one scalar diagonal pairing;
- one one-dimensional integral of 2 by 2 matrices.

## 5. Apply to the D2 primitive

Put

    X=BR.

The Leibniz displacement identity gives

    rank[D,X] <= 4.

Therefore

    boxed:
    tr(X^2)
      = sum_i X_ii^2
        - (1/(2*pi))
          int S2(t)
            tr_4[
              A_X(t)A_X(-t)
            ] dt.

This is the D2 Fourier-channel formula already isolated in the companion
note.

## 6. The z-derivatives do not enlarge the theorem state conceptually

D1 and D2 are z-derivatives of the two scalar primitives above.

At the four F9 poles the imaginary-part gap is about 1.463.

Choose any fixed Cauchy radius rho smaller than this gap.  Uniform control of
the two primitives on the corresponding four small circles controls their
z-derivatives by the ordinary Cauchy estimate.

Thus there is no need to introduce a new d-dimensional derivative state.

Equivalently, one may differentiate the small-channel factors directly; both
routes stay finite-channel.

## 7. Current theorem state after all algebraic compression

For the bounded four-pole F9 rung, the exact permutation-Lindeberg theorem
has now been reduced from generic d by d nonlinear matrices to:

1. diagonal pairings of explicit current blocks with resolvent diagonals;
2. 2 by 2 Fourier channels for the D1 primitive;
3. 4 by 4 Fourier channels for the D2 primitive;
4. one scalar t integral with the explicit bounded kernel S2;
5. four fixed nonreal spectral parameters.

Every remaining difficulty is arithmetic/limit control of those channels.

There is no longer an algebraic need for:

- a generic bivariate spectral transition measure;
- an O(d^2) state;
- raw finite-T fourth moments.

## 8. Why this matters for the record inequality

The first record target only needs

    limsup tau F9(H_T) < 0.1632499815,

with model/Jensen benchmark

    50/329 ~= 0.151975684.

So the small-channel arithmetic proof need not identify a complete limiting
law.  A one-sided aggregate estimate fitting inside the 0.0112742976
consumer budget is enough.

The next step is to express the generators of B and R explicitly in the
scalar prime Dirichlet-polynomial variables Q_S(tau), then test which channel
terms are killed by prime-base valuation and which require the long-shift E2
input.

See:

    notes/WP84_D2_FOUR_BY_FOUR_FOURIER_CHANNEL.md
    notes/WP84_FOUR_POLE_INEQUALITY_KILL_GATE.md
    notes/WP84_SHARP_LOEWNER_DIRICHLET_REPRESENTATION.md
