# WP71 — bulk/collar reduction for the moving welding interval

Date: 2026-10-04
Status: **FALSIFIED AS A STAGE-A THEOREM ROUTE — retained as forward audit record**

The earlier version of this note assumed that the Stage-A lock range J was on the ambient prime scale, so that the moving m-window had length comparable to the ambient block up to logarithms.

That assumption was imported from a different generic moment-window notation and is wrong for the actual Stage-A hard band.

## Falsifier

The live public Stage-A condition is

    |b1*n-b2*m|*T <= 40*min(b1*n,b2*m),

with m<=floor(T/(2*pi)). It implies

    |m-(b1/b2)n| <= 40/(2*pi),

so the full moving interval has total real length <40/pi<13 and therefore at most 13 integer m-values.

See `notes/WP71_G9_STAGEA_WINDOW_SCALE.md` and `src/wp71_g9_stageA_width_gate.py`.

## What survives from the old note

The exact endpoint formulas, monotonicity and source-switch bookkeeping remain true. A formal collar decomposition is still a correct geometric statement in an abstract large-J model.

What fails is its use to justify Stage-A asymptotics: there is no large bulk interval to which a long-interval twin-prime theorem can be applied.

## Replacement strategy

Do not approximate w_k(n) pointwise. Preserve the n/j/k averaging and attack the averaged four-prime object directly, most likely through an exact spectral/Parseval representation or an equivalent averaged covariance identity.

No result downstream may cite the superseded ambient/logarithmic-length claim.
