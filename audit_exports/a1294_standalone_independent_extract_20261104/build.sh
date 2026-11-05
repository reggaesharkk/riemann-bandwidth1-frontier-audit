#!/bin/bash
set -eu
cd "$(dirname "$0")"
root="$PWD"
export LEAN_PATH="$root:$LEAN_PATH"
/usr/bin/time -v timeout 240 lean -M 6800 --root "$root" StandaloneCore.lean -o StandaloneCore.olean > core_build.log 2>&1
/usr/bin/time -v timeout 240 lean -M 6800 --root "$root" StandaloneTerminal22.lean -o StandaloneTerminal22.olean > leaf_build.log 2>&1
