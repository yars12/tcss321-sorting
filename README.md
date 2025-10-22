# tcss321-sorting

TCSS 321 — Extra Labor: **Programming Project**  
Author: **Yar Shkala**

This repo compares three Θ(n²) sorting algorithms:
- `bubble_sort` (with early-exit optimization)
- `selection_sort`
- `insertion_sort`

## Files
- `algorithms.py` — sorting implementations.
- `benchmark.py` — runs timings for n in {50..1000}, 5 trials each; saves `results.csv` and `sorting_times.png`.
- `requirements.txt` — Python dependencies.

## How to run
```bash
pip install -r requirements.txt
python benchmark.py
```