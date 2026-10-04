# A1294 source-free replay — Windows launcher correction

Date: 2026-10-04

## V1 outcome

The first Windows source-free replay package did **not** reach certificate
parsing or arithmetic. It failed immediately while opening
`certificate/manifest.json`.

Observed exception:

`OSError: [Errno 22] Invalid argument`

The malformed path contained:

`A1294_SOURCE_FREE_REPLAY_PACKAGE" --progress 250000 \certificate\manifest.json`

## Cause

The batch runner passed

`--package-root "%~dp0"`

where `%~dp0` ends in a backslash. Under Windows command-line parsing, the
trailing backslash can escape the closing quote, causing subsequent command
arguments to be absorbed into the path string.

This was a launcher/quoting failure only. No certificate token, terminal
inequality, catalog model, hash, or proof margin was evaluated in the failed
V1 run.

## V2 correction

The V2 runner first changes directory to the extracted package folder and then
invokes

`replay_a1294_source_free.py --progress 250000`

without passing `--package-root`.

An optional preflight script was added to confirm that the manifest, canonical
streams, and three frozen catalog JSON files are readable before the
multi-hour replay starts.

V2 package ZIP SHA-256:

`3ecf4d268a74d94310d4d5d8863160e5d6f1fe8a6dd00afef9afe6a80a4ed1a5`

Evidence classification remains unchanged until the V2 source-free replay
finishes: GitHub generation PASS + GitHub independent verifier PASS; external
Windows source-free replay pending.
