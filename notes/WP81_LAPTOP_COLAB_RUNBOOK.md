# WP81 laptop / Colab runbook

Date: 2026-10-04  
Goal: compute the exact target-blind `{5,2}` certificate without paid
GitHub Actions.

## First principle

There is **no random seed**.  The exact-polytope calculation is deterministic.
We lock source bytes, upstream commit, shard plan and environment instead.

## Laptop preparation

From the private Riemann repository root:

```bash
mkdir -p work/spec52

python src/wp81_spec52_shard_plan.py \
  --shard-size 10 \
  --out work/wp81_spec52_shards.json

python src/wp81_spec52_execution_lock.py \
  --repo . \
  --upstream ../zeta-0.7947-reproduction \
  --manifest work/wp81_spec52_shards.json \
  --out work/wp81_spec52_execution_lock.json
```

The upstream checkout must be exactly:

`d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`.

## Smoke test before long compute

Run one shard only:

```bash
python src/wp81_spec52_worker.py \
  --manifest work/wp81_spec52_shards.json \
  --lock work/wp81_spec52_execution_lock.json \
  --upstream ../zeta-0.7947-reproduction \
  --workdir work/spec52 \
  --shards 0
```

The producer first runs the exact convention gate against all public
`{4,2}` geometries.  If that gate fails, stop.

## Parallelization

There are 45 ten-term shards.

A safe division is, for example:

- laptop: `0-14`;
- Colab worker A: `15-29`;
- Colab worker B: `30-44`.

The exact division does not matter.  Coverage is checked later.

Do not let two workers run the same shard.

## Colab privacy

The Riemann repository remains private.

For Colab, prefer uploading only the small WP81 scripts and the locked
manifest/execution receipt rather than putting a long-lived GitHub personal
access token into a notebook.  The public upstream repository can be cloned
normally and checked out at the pinned commit.

The Colab worker must use the same manifest and run its own execution-lock
check on the uploaded bytes.

## Final collection

Put every raw `spec52_d*_*.txt` log into one directory and run:

```bash
python src/wp81_spec52_verify.py work/spec52/*.txt \
  --receipt work/wp81_spec52_verification_receipt.json
```

Then, independently:

```bash
python src/wp81_spec52_aggregate.py work/spec52/*.txt \
  --json-out work/wp81_spec52_exact_certificate.json
```

The verifier and aggregator must independently return the same exact
`U1,U2,U3,{5,2}` values.

## Promotion rule

A PASS here certifies only the model-side exact `{5,2}` fraction.

It does not become a zeta moment theorem until the analytic transport is
closed.  The first full result remains target-blind: no expected rational is
hard-coded in either verifier.
