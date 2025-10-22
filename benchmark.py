# benchmark.py
# Measure runtime of Bubble, Selection, and Insertion sort across input sizes.
# Saves results.csv and sorting_times.png.
#
# Usage:
#   python benchmark.py

import numpy as np
import time, statistics
import pandas as pd
import matplotlib.pyplot as plt
from algorithms import bubble_sort, selection_sort, insertion_sort

def time_func(func, arr):
    start = time.perf_counter()
    func(arr)
    end = time.perf_counter()
    return end - start

def run():
    np.random.seed(321)
    sizes = [50, 100, 150, 200, 250, 300, 400, 500, 600, 800, 1000]
    trials = 5
    algos = {
        "Bubble": bubble_sort,
        "Selection": selection_sort,
        "Insertion": insertion_sort,
    }
    rows = []
    for n in sizes:
        arrays = [np.random.randint(0, 10_000, size=n).tolist() for _ in range(trials)]
        for name, fn in algos.items():
            times = [time_func(fn, arr) for arr in arrays]
            med = statistics.median(times)
            rows.append({"n": n, "algorithm": name, "median_sec": med})
            print(f"{name:10s} n={n:4d} median={med:.6f}s")
    df = pd.DataFrame(rows)
    df.to_csv("results.csv", index=False)

    pivot = df.pivot(index="n", columns="algorithm", values="median_sec")
    ax = pivot.plot(marker="o", title="Runtime vs. n for Basic Sorting Algorithms")
    ax.set_xlabel("Input size (n)")
    ax.set_ylabel("Median runtime (seconds) over 5 trials")
    fig = ax.get_figure()
    fig.tight_layout()
    fig.savefig("sorting_times.png", dpi=150)

if __name__ == "__main__":
    run()