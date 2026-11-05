# D: and WSL read-only access recheck

Additive result for 2026-11-03. The prior access inventory is preserved unchanged.

- D: target: `D:\Reggae-shark-universe-\navier-stokes-bridge-audit`. The directory entry was visible in the normal sandbox, but Git reads returned permission denied. The targeted read-only escalation succeeded. Checkout commit: `33f91dc6b7826b792a8e49800afd87772512ec77`; branch: `main`; status clean: `True`.
- WSL: Ubuntu 2 was listed after read-only escalation. `/mnt/d/Reggae-shark-universe-/navier-stokes-bridge-audit` resolved and reported the same commit `33f91dc6b7826b792a8e49800afd87772512ec77` with clean status.
- Hash comparison: 81 tracked WP19 v0.28 note/script/result/workflow files were checked against all members of the nine already-inventoried WP19 archives and the packet's selected WP19/frozen source copies. 18 had an exact prior SHA-256 match; 63 file records (56 distinct SHA-256 values) had no exact match in that reviewed source set. The exact paths, byte lengths, hashes and matches are in the adjacent JSON. This is newly accessible provenance/evidence, not a new mathematical result.
- The previous inventory's `INACCESSIBLE` labels accurately describe that earlier execution context; this additive check records the access now obtained. No historical evidence or archive was changed.
