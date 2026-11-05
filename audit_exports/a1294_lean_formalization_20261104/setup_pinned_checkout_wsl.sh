set -euo pipefail
target='/home/reggaeshark/a1294_lean_formalization_20261104/formal-math'
mkdir -p "$(dirname "$target")"
test ! -e "$target"
git init "$target"
git -C "$target" remote add origin https://github.com/anthropics/formal-math.git
git -C "$target" fetch --depth 1 --filter=blob:none origin fba91d214655aaa1fd0504bb893c8859c20c79f9
git -C "$target" sparse-checkout init --cone
git -C "$target" sparse-checkout set zeta23
git -C "$target" checkout --detach FETCH_HEAD
git -C "$target" rev-parse HEAD
