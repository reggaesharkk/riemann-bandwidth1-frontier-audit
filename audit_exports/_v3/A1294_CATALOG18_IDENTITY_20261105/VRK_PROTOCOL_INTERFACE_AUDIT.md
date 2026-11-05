# VRK and Reggae Shark Protocol interface audit

## Components actually inspected

- `reference/vrk/canonical.py` implements deterministic canonical JSON (`sort_keys=True`, compact separators, UTF-8, `allow_nan=False`), SHA-256 file hashing, and object digests.
- `reference/vrk/evidence.py` derives an order-independent evidence root by canonical-digesting evidence binding descriptors, sorting leaf digests, then digesting the root object.
- `reference/protocol/kernel.py` contains the actual protocol implementation. Its module docstring identifies the kernel source as **1.3.2**. `reference/protocol/pyproject.toml` labels the distribution `1.3.3.dev0`. The version labels are not silently reconciled; this packet records the mismatch.
- In `kernel.py`, `verify_and_hash_evidence_list` (around lines 1919–1962) resolves files inside its repository root, reads and SHA-256 hashes the actual bytes, optionally checks anchors, then derives an evidence root.
- `verify_exported_ledger` (around lines 2167–2215 and following) requires a nonempty signed head and a positive `min_length`, rejects truncation/stale heads, and supports freshness pins.
- `verify_chain_list` (around lines 2248–2302 and following) requires a normalized expected public key, validates claim schema/trust root/sealed status/scope/evidence roles, and checks on-disk evidence hashes. The implementation verifies Ed25519 signatures later in the method. It returns rejection on absent/malformed/revoked expected keys rather than accepting unpinned keys.

## Use in this checkpoint

This packet uses the real VRK `digest_object`, `sha256_file`, and `evidence_root` functions to create and validate an **unsigned local claim/evidence contract**. It does not construct a protocol `intentseal-vrk-claim-v2` ledger entry, signed head, Ed25519 signature, or trusted public-key pin. No signing key or API credential was accessed. The protocol verifier was inspected, not invoked to certify this local record.

The record statuses keep `KERNEL_PROVED`, `EXTERNALLY_CHECKED`, and `INCOMPLETE` distinct. Its hashes bind file identities; they do not prove the mathematics, authenticate a source conversion inside Lean, or prevent rollback by themselves. A future protocol-signed export would need the protocol's actual schema and a public-key/freshness trust policy supplied independently.

## Lineage correction

`lineage_identification.json` distinguishes the final published frozen lineage SHA-256 `05ba923c90dfc481a70a3784b72d1cd71a0adeac2c34a22631169f545ae5d4c0` from the historical inventory SHA-256 `14f920b5fcb970f8a97eaf98aa80c83e8ff4125bb85e311705f86edad5dd56db`. Both source archives are retained unchanged.
