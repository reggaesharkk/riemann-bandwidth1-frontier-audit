# WP84 — exact Jensen ladder thresholds and conditional theorem (2026-10-06)

Status: **EXACT CONSUMER THEOREM AND THRESHOLD RECORD; ARITHMETIC TRANSFER STILL OPEN**

Let
```
w0 = 1415/13891,
g(x) = P(x)^2,
F_delta(x) = (delta+1)g(x)/(g(x)+delta),
h_delta(w) = (delta+1)w/(delta+w).
```
The exact Christoffel certificate gives (g(x)\ge1) for (x\le0) and
(int g\,d\nu\le w_0) for every measure satisfying the pinned model
moments.

## 1. Consumer bound

The function (h_\delta) is increasing and concave for (w\ge0).
Since (F_\delta=h_\delta\circ g), Jensen gives
[
\int F_\delta\,d\nu
\le h_\delta\left(\int g\,d\nu\right)
\le h_\delta(w_0).
]
Also (F_\delta(x)\ge1) for (x\le0), because (g(x)\ge1) and
(h_\delta(1)=1). Therefore
[
\nu(( -\infty,0])\le h_\delta(w_0),
\qquad
S_\delta:=1-2h_\delta(w_0)
=\frac{\delta(1-2w_0)-w_0}{\delta+w_0}.
]

This is an exact model-measure theorem. Its arithmetic consequence is
conditional on proving, for the actual zeta-side matrices and each fixed
(delta\ge61),
[
\limsup_{T\to\infty}\tau(F_\delta(H_T))\le h_\delta(w_0).
]
Under that hypothesis, the existing zero-counting transfer gives
[
\liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}\ge S_\delta.
]
If the hypothesis holds for every fixed (delta\ge61), taking the
supremum yields
[
\liminf_{T\to\infty}\frac{N_0^s(T)}{N(T)}
\ge \sup_{\delta\ge61}S_\delta
=1-2w_0=\frac{11061}{13891}
=79.6270966813\ldots\%.
]
The displayed arithmetic hypothesis is the unresolved state-flow transfer;
this note does not assert it.

## 2. Exact first-parameter record

For a target (q<1-2w_0), set (c=(1-q)/2). Solving
(S_\delta>q) gives the exact threshold
[
\delta>\frac{w_0(1-c)}{c-w_0}.
]
The exact rational gate in
`src/wp84_jensen_threshold_record.py` verifies:

| Strict target | Exact real threshold for `delta` | First integer `delta >= 61` | Exact achieved score |
|---|---:|---:|---:|
| 79.5% | (507985/3531\approx143.8643) | 144 | (1591369/2001719\approx79.5001196472\%) |
| 79.6% | (635335/941\approx675.1700) | 676 | (7475821/9391731\approx79.6000332633\%) |
| 79.62% | (12708115/4929\approx2578.817\) | 2579 | (3565613/4478288\approx79.6200021079\%) |

For the simplest member, (delta=61),
[
S_{61}=\frac{336653}{424383}=79.3276356499\ldots\%.
]
The full coefficient (11061/13891) is a supremum, approached as
(delta\to\infty); no finite (delta) attains it.

## 3. Evidence boundary

The rational calculations are exact. They improve the model/conditional
ladder over the older pointwise cap. They do not prove the six-pole
inequality for (H_T), and therefore do not establish an unconditional
simple-zero proportion.
