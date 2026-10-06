# Pinned public model sources and archives

Read-only copies from [JoshuaHKU/zeta-0.7947-reproduction](https://github.com/JoshuaHKU/zeta-0.7947-reproduction/tree/d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8),
commit `d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`. Retrieved 2026-10-06.
These copies preserve upstream bytes; they are model evidence, not arithmetic
transport certificates. Attribution and authorship remain with upstream.

| Local file | Upstream path |
| --- | --- |
| exact_connected.py | gpu/exact_connected.py |
| exact_polytope.py | gpu/exact_polytope.py |
| exact_t222.py | certification/exact_t222.py |
| exact_42.txt | gpu/exact/exact_42.txt |
| exact_c5.txt | gpu/exact/exact_c5.txt |
| exact_c6.txt | gpu/exact/exact_c6.txt |

`src/wp84_c5_c6_transport_audit.py` validates the two engine Git blob hashes
against the existing WP81 pin, validates all three archive hashes against the
existing WP79 pin, checks the ordered-partition term construction at degrees
4–6, and independently re-sums every archived rational term. It does not
recompute the full polytope integrals or the four triple-pair integrals.
