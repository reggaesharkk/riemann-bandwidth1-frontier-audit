# Changelog

## v2.4.2 — Witness framing and failure handling

- Require the Witness TCP/TLS endpoint to receive exactly the documented length-prefixed JSON format; remove the unframed fallback.
- Return a generic denial reason for internal ledger/signing failures so exception details are not sent to the peer.
- Narrow rollback and socket cleanup handlers to SQLite and OS errors. The remaining broad exception handlers close or deny the request, or convert it to a failed client result.
- Document that the sign and verify APIs hash exact UTF-8 certificate text; callers should read files as bytes and decode UTF-8 to preserve CRLF.
- Add tests 69 and 70 for framed JSON acceptance, unframed JSON rejection, and generic internal-error responses.
- Clarify the Lean compiler target recorded in the verification log.

The compiler and VM output, canonical bytecode, carried-forward Lean certificate, and signed example package remain unchanged.

## v2.4.1 — Security hardening

- Write generated private keys with owner-only POSIX permissions; tighten pre-existing files before writing new key material.
- Set TLS 1.3 as the minimum version for Witness and Egress connections, including the standalone Witness server.
- Use constant-time comparison for digest and trust-root strings in equivocation handling and Witness response verification.
- Add regression coverage for private-key permissions, the TLS version floor, runtime assert usage, and the digest comparison helper.
- Preserve the legacy Lean certificate header because its exact text is part of the certificate hash bound into the carried-forward signed package; add a regression test for byte-for-byte certificate reproduction and package hash binding.
- Write generated certificate output as explicit UTF-8 bytes so Windows text-mode newline conversion cannot change the signed certificate hash.
- Read sign --lean-file as raw UTF-8 bytes before hashing, preserving CRLF files as stored; add regression coverage for the signed hash binding.
