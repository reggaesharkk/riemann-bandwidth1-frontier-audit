# WP81 execution lock: no RNG seed required

The exact {5,2} computation has no stochastic initialization.  Asking for a
random seed would create a false sense of reproducibility: the producer is
deterministic.

The correct lock is source-and-environment identity.

Before any laptop or Colab shard is accepted, run:

```
python src/wp81_spec52_shard_plan.py --shard-size 10 --out work/wp81_spec52_shards.json

python src/wp81_spec52_execution_lock.py \
  --repo . \
  --upstream /path/to/zeta-0.7947-reproduction \
  --manifest work/wp81_spec52_shards.json \
  --out work/wp81_spec52_execution_lock.json
```

The execution lock:

- verifies the upstream checkout is exactly
  `d85bddfe9d8f12856fba735fc9cb3ca23b48b3a8`;
- verifies Git-blob identities of the exact producer, shard planner, verifier,
  and the two pinned upstream exact engines;
- records SHA-256 of the actual bytes executed;
- records the SHA-256 and canonical digest of the shard manifest;
- records Python/platform metadata;
- explicitly records `rng_used=false`.

This is stricter and more relevant than a seed because every accepted worker
must run the same deterministic arithmetic.

The first complete 450-row aggregate remains target-blind.  Its exact rational
value is discovered only after coverage closes.
