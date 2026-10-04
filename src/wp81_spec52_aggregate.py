#!/usr/bin/env python3
"""
Fail-closed exact aggregator for WP81 {5,2} term logs.

Consumes any number of text logs produced by wp81_spec52_exact.py.
Requires, for each d=1,2,3:
  * exactly term indices 0..149,
  * no duplicate term index,
  * exact Fraction parse for every value,
  * sign in {-1,+1}.

It then computes
    U_d = sum_i sign_i * value_i
and
    {5,2} = 7 * (U_1 + U_2 + U_3).

No expected target is hard-coded.  This is intentional: the first complete
exact aggregation is an identification result, not a target-confirmation run.
"""

import argparse
import json
import re
from fractions import Fraction as F

RX = re.compile(
    r"^spec52 d ([123]) term (\d+) sign (-?1) value ([^ ]+) wall "
)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("logs", nargs="+")
    ap.add_argument("--json-out")
    args = ap.parse_args()

    seen = {1: {}, 2: {}, 3: {}}

    for path in args.logs:
        with open(path, "r", encoding="utf-8") as fh:
            for raw in fh:
                m = RX.match(raw.strip())
                if not m:
                    continue
                d = int(m.group(1))
                i = int(m.group(2))
                sign = int(m.group(3))
                val = F(m.group(4))
                if not 0 <= i < 150:
                    raise SystemExit(f"out-of-range term d={d} i={i} in {path}")
                if i in seen[d]:
                    raise SystemExit(f"duplicate term d={d} i={i}")
                seen[d][i] = (sign, val, path)

    for d in (1, 2, 3):
        missing = sorted(set(range(150)) - set(seen[d]))
        extra = sorted(set(seen[d]) - set(range(150)))
        if missing or extra:
            raise SystemExit(
                f"d={d} incomplete: got={len(seen[d])} "
                f"missing={missing[:20]}{'...' if len(missing)>20 else ''} "
                f"extra={extra}"
            )

    U = {}
    for d in (1, 2, 3):
        U[d] = sum((F(sign) * val for sign, val, _ in seen[d].values()), F(0))

    total = F(7) * (U[1] + U[2] + U[3])

    payload = {
        "schema": "wp81-spec52-exact-certificate-v1",
        "status": "PASS",
        "terms_per_class": 150,
        "placement_multiplicities": {"1": 7, "2": 7, "3": 7},
        "U1": str(U[1]),
        "U2": str(U[2]),
        "U3": str(U[3]),
        "spec52": str(total),
        "spec52_decimal": float(total),
    }

    print(json.dumps(payload, indent=2, sort_keys=True))
    if args.json_out:
        with open(args.json_out, "w", encoding="utf-8") as fh:
            json.dump(payload, fh, indent=2, sort_keys=True)
            fh.write("\n")


if __name__ == "__main__":
    main()
