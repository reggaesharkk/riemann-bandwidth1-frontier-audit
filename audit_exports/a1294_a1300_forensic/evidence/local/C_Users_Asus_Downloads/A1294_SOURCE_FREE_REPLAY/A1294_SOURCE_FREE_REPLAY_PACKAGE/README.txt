A1294 SOURCE-FREE EXACT REPLAY PACKAGE
======================================

Purpose
-------
Replay the final A1294 certificate outside the GitHub generating CI environment.

Trust boundary
--------------
The replay script uses only the Python standard library. It does not import:
- the A1294 search generator,
- the project Checker,
- the GitHub independent verifier,
- any project Python module.

It reconstructs the exact dyadic tree and recomputes every terminal inequality
from the frozen certificate streams and the three frozen catalog JSON files.

How to run on Windows
---------------------
1. Extract this ZIP.
2. Double-click RUN_A1294_SOURCE_FREE_REPLAY.bat.
3. Leave the terminal open until PASS/FAIL.
4. Upload:
   A1294_SOURCE_FREE_REPLAY_RESULT.json
   A1294_SOURCE_FREE_REPLAY_LOG.txt

Expected runtime
----------------
Approximately 2-5 hours on the previously benchmarked Windows ARM64 laptop.
Actual time depends on CPU scheduling and Fraction arithmetic.

Expected immutable certificate
------------------------------
Visited nodes: 13,454,121
Leaves: 6,727,061
Final GitHub artifact ZIP SHA-256:
11c1ab1820039284f60e492fe609f6a497175284acdd0c3c53d6ab62b8b1cd19

This package is for verification, not optimization.
