"""Бенчмарк сортировок, поиска и Two Sum."""

import csv
import os
import random
import timeit

from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort

FIELDNAMES = ["task", "n", "impl", "seconds"]


def _time(fn, *args):
    return timeit.timeit(lambda: fn(*args), number=1)


def save_csv(path, rows):
    """Пытается использовать write_csv из ЛР4, иначе пишет CSV сам."""
    try:
        from src.lab04.io_txt_csv import write_csv

        write_csv(path, rows)
        return
    except Exception:
        pass

    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        writer.writeheader()
        writer.writerows(rows)


def bench_sorts(n):
    data = [random.randint(-10**6, 10**6) for _ in range(n)]
    rows = []

    rows.append({
        "task": "sort",
        "n": n,
        "impl": "sorted",
        "seconds": _time(sorted, data),
    })

    for name, fn in (
        ("bubble_sort", bubble_sort),
        ("insertion_sort", insertion_sort),
        ("selection_sort", selection_sort),
    ):
        if n >= 100_000:
            seconds = ">60"
        else:
            seconds = _time(fn, data)

        rows.append({
            "task": "sort",
            "n": n,
            "impl": name,
            "seconds": seconds,
        })

    return rows


def bench_search():
    n = 100_000
    data = [random.randint(-10**6, 10**6) for _ in range(n)]
    queries = [random.randint(-10**6, 10**6) for _ in range(10_000)]

    rows = []

    rows.append({
        "task": "search",
        "n": n,
        "impl": "linear_search",
        "seconds": timeit.timeit(
            lambda: [linear_search(data, x) for x in queries],
            number=1,
        ),
    })

    rows.append({
        "task": "search",
        "n": n,
        "impl": "sorted_for_binary",
        "seconds": _time(sorted, data),
    })

    sorted_data = sorted(data)

    rows.append({
        "task": "search",
        "n": n,
        "impl": "binary_search",
        "seconds": timeit.timeit(
            lambda: [binary_search(sorted_data, x) for x in queries],
            number=1,
        ),
    })

    return rows


def bench_two_sum(n):
    data = [random.randint(-10**6, 10**6) for _ in range(n)]
    i, j = random.sample(range(n), 2)
    target = data[i] + data[j]

    return [
        {
            "task": "two_sum",
            "n": n,
            "impl": "two_sum_brute",
            "seconds": _time(two_sum_brute, data, target),
        },
        {
            "task": "two_sum",
            "n": n,
            "impl": "two_sum_fast",
            "seconds": _time(two_sum_fast, data, target),
        },
    ]


def _fmt_seconds(value):
    if isinstance(value, str):
        return value
    return f"{value:.6f}"


def print_table(rows):
    print(f"{'task':<10} {'n':>8} {'impl':<20} {'seconds':>12}")
    print("-" * 54)

    for row in rows:
        print(
            f"{row['task']:<10} "
            f"{row['n']:>8} "
            f"{row['impl']:<20} "
            f"{_fmt_seconds(row['seconds']):>12}"
        )


def main():
    random.seed(42)

    rows = []

    for n in (1_000, 10_000, 100_000):
        rows.extend(bench_sorts(n))

    rows.extend(bench_search())

    for n in (1_000, 10_000):
        rows.extend(bench_two_sum(n))

    print_table(rows)

    os.makedirs("data/lab07", exist_ok=True)
    save_csv("data/lab07/bench.csv", rows)

    print("\nCSV сохранён: data/lab07/bench.csv")


if __name__ == "__main__":
    main()