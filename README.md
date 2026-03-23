# Sort Algorithm Benchmark

A simple experiment loop target. Optimize `sort.py` to maximize sorting throughput.

## Rules

- **Edit only `sort.py`** — `bench.py` is read-only
- Your `sort_array()` function must return a correctly sorted list
- The benchmark verifies correctness — incorrect results fail immediately
- Metric: `throughput` (elements sorted per second, higher is better)

## Run

```bash
python bench.py
```

## Baseline

Naive quicksort: ~925k elements/sec
