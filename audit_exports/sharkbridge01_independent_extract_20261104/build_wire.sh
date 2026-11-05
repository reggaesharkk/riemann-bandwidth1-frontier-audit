#!/bin/bash
set -eu
cd "$(dirname "$0")"
experiment="$PWD"
export LEAN_PATH="$experiment/baseline/lib:$LEAN_PATH"
/usr/bin/time -v timeout 240 lean -M 6800 --root "$experiment" WireParent.lean -o WireParent.olean > wire_build.log 2>&1
