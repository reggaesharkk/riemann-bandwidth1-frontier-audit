# SharkLang v2.4.2 Security Follow-up

This release follows v2.4.1. It preserves the compiler output, carried-forward Lean certificate, example bytecode, and signed example package while tightening the Witness request parser and making certificate-byte handling explicit for library callers.

## Security changes

- The Witness accepts only the documented 4-byte length-prefixed JSON format. The unframed JSON fallback has been removed.
- Internal Witness processing failures return a generic denial reason. Rollback and socket cleanup suppress only their expected I/O errors.
- The sign and verify library methods document that certificate text is hashed as its exact UTF-8 encoding. Callers reading a Lean file should use read_bytes().decode("utf-8") to preserve CRLF.
- The v2.4.1 key permissions, TLS 1.3 floor, constant-time comparisons, exact Lean certificate reproduction, and raw-byte CLI signing protections remain in place.
- Eight security regression checks are included across v2.4.1 and v2.4.2; tests 69 and 70 cover framed-only Witness JSON parsing and generic internal-error responses.

## Contents

- sharklang.py — compiler, verifier, VM, Lean certificate backend, PKI, Witness, Egress client, and 70-test suite.
- shark_pki.py, shark_witness.py, shark_egress.py — standalone command-line entry points.
- Lifecycle4DCert.lean and examples/ — carried-forward v2.4 certificate, source, bytecode, and signed package.
- logs/ — Windows and Ubuntu test runs, Egress scenarios, signature verification, and bytecode/Lean reproducibility output.
- SHA256SUMS.txt — SHA-256 digests for release files other than the manifest itself.

No private keys or provider credentials are included.

## Verification

Windows ARM64 tests used Python 3.12.10 and OpenSSL 3.0.16. All three runs recorded 70 tests, with 69 passing and test 63 skipped because POSIX file modes are unavailable. Ubuntu WSL tests used Python 3.14.4 on aarch64 and OpenSSL 3.5.5; all 70 tests passed in each of the three modes, including the private-key permission test.

The Lean check log records Lean 4.35.0 with target x86_64-w64-windows-gnu. The Python release checks ran on Windows ARM64. These are separate toolchain targets, as shown in the logs.

The suites ran under -B, -O -B, and -OO -B. The local six-scenario Egress self-test passed on Windows and Ubuntu, including replay/equivocation rejection and offline fail-closed behavior. Recompiled bytecode SHA-256 is 49eb4fe401077bc9ff4fe2b0110e878bcd22ff1aa5db7653927035c0182e9c49. The regenerated Lean certificate SHA-256 is da5c7a42f92fbc0f9e57287cd89ca52ab0e1f6930fc96bfcfd2f0b7d78a4bf6a, matching the signed package; the package signature verifies with its embedded public key.

No provider API requests were sent. The Egress self-test used a temporary local Witness and temporary test keys.

## Runtime dependency

Python 3.10 or newer and the cryptography package are required.
