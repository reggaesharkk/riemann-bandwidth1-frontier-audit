A1294 LOCAL BENCHMARK PACKAGE
==============================

WHAT THIS DOES
--------------
1. Runs the same seam-aware A1294 exact branch-and-bound logic locally.
2. Measures a 250,000-node single-process benchmark.
3. Measures a 6-worker multiprocessing throughput probe.
4. Compares your laptop with our GitHub 1M reference run:
   1,000,000 nodes / 1406.36 s = about 711 nodes/s.
5. Writes:
   results\A1294_LOCAL_BENCHMARK_RESULT.json
   results\A1294_LOCAL_BENCHMARK_SUMMARY.txt

THIS IS A SPEED TEST, NOT A COMPLETE PROOF.

EASIEST WAY
-----------
Download BOTH:
- A1294_LOCAL_BENCHMARK_PACKAGE.zip
- RUN_A1294_FROM_DOWNLOADS.bat

Leave both in your normal Windows Downloads folder.
Double-click RUN_A1294_FROM_DOWNLOADS.bat.

The launcher will:
- find the newest A1294_LOCAL_BENCHMARK_PACKAGE*.zip in Downloads,
- extract it into Downloads\A1294_LOCAL_BENCHMARK,
- run the benchmark,
- leave the result JSON in that extracted folder.

Then send A1294_LOCAL_BENCHMARK_RESULT.json back to ChatGPT.

PYTHON
------
Requires Python 3. It tries:
1. py -3
2. python

The code uses only Python's standard library; no pip packages are required.

FROZEN INPUT HASHES
-------------------
macro-data-exact.json
961a0281a134382f9c2678cc49487839d2b9c2cbd9df382871f2c7b706552a5b

refinement-catalog-v1-exact.json
3f83563fb3d6f5a4e1aa0263384d0781494a672368233445a8c6e8e0e9817cb9

refinement-catalog-v3.json
7625c6dd291b88604fb7a201fef400eabd1309155e203e366aac8ca4357d992d
