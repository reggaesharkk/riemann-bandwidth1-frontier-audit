#!/bin/bash
set -eu
cd "$(dirname "$0")"
experiment="$PWD"
mkdir -p baseline/lib/Zeta23/ThmD/Sextuple
export LEAN_PATH="$experiment/baseline/lib:$LEAN_PATH"
for name in CompositionalLeaf CompositionalRight A1294CompactParent; do
  /usr/bin/time -v timeout 240 lean -M 6800 --root "$experiment/baseline" "baseline/Zeta23/ThmD/Sextuple/$name.lean" -o "baseline/lib/Zeta23/ThmD/Sextuple/$name.olean" > "baseline/$name.log" 2>&1
done
