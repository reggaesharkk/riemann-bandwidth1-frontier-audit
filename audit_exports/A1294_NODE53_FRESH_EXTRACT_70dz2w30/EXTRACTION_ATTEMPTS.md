# Independent extraction attempt record

The first verifier version used Python `TemporaryDirectory` under the Codex sandbox's Windows temporary directory. The sandbox denied creation of a nested `reference_inputs` directory (`WinError 5: Access is denied`). This happened before archive extraction completed, so it is not a ZIP/CRC or mathematical failure. The full command output is preserved in `failed_sandbox_temp_extraction.log`.

The verifier was adjusted to extract into a fresh uniquely named sibling directory under the writable audit workspace. The final V2 packet is tested from that workspace location using Python's `zipfile`, and both evidence-manifest and exact-rational reconstruction replays run under normal, `-O`, and `-OO` modes. The successful final run output is recorded outside the packet as `audit_exports/A1294_NODE53_TERMINAL16_V2_INDEPENDENT_EXTRACTION.log`.
