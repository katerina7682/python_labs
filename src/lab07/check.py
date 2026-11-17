"""Проверка своих алгоритмов против эталона на случайных данных."""

import random

from src.lab07.search import (
    binary_search,
    linear_search,
    two_sum_brute,
    two_sum_fast,
)
from src.lab07.sorting import bubble_sort, insertion_sort, selection_sort


def check_sorting(fn, trials=100):
    """Сравнивает fn(nums) со sorted(nums) и проверяет, что nums не изменён."""
    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        original = list(nums)

        result = fn(nums)

        assert result == sorted(nums), (
            f"{fn.__name__} ошиблась на {nums}: "
            f"получено {result}, ожидалось {sorted(nums)}"
        )
        assert nums == original, f"{fn.__name__} изменила исходный список: {nums}"


def check_search(trials=100):
    """Проверяет linear_search и binary_search."""
    checks = 0

    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-100, 100) for _ in range(n)]
        x = random.randint(-110, 110)

        try:
            expected = nums.index(x)
        except ValueError:
            expected = -1

        got = linear_search(nums, x)
        assert got == expected, (
            f"linear_search({nums}, {x}) = {got}, ожидалось {expected}"
        )
        checks += 1

        sorted_nums = sorted(nums)
        candidates = [x, -101, 101, -100, 100]

        if sorted_nums:
            candidates.extend([sorted_nums[0], sorted_nums[-1], sorted_nums[len(sorted_nums) // 2]])

        for candidate in candidates:
            got = binary_search(sorted_nums, candidate)

            if candidate in sorted_nums:
                assert 0 <= got < len(sorted_nums), (
                    f"binary_search({sorted_nums}, {candidate}) = {got}: индекс вне диапазона"
                )
                assert sorted_nums[got] == candidate, (
                    f"binary_search({sorted_nums}, {candidate}) = {got}: "
                    f"там лежит {sorted_nums[got]}"
                )
            else:
                assert got == -1, (
                    f"binary_search({sorted_nums}, {candidate}) = {got}, ожидалось -1"
                )

            checks += 1

    return checks


def check_two_sum(trials=100):
    """Сравнивает two_sum_brute и two_sum_fast по смыслу ответа."""
    checks = 0

    for _ in range(trials):
        n = random.randint(0, 50)
        nums = [random.randint(-50, 50) for _ in range(n)]
        target = random.randint(-100, 100)

        brute = two_sum_brute(nums, target)
        fast = two_sum_fast(nums, target)

        assert (brute is None) == (fast is None), (
            f"two_sum разошлись на nums={nums}, target={target}: "
            f"brute={brute}, fast={fast}"
        )

        for name, result in (("two_sum_brute", brute), ("two_sum_fast", fast)):
            if result is not None:
                i, j = result
                assert 0 <= i < j < len(nums), (
                    f"{name}({nums}, {target}) вернула некорректные индексы {result}"
                )
                assert nums[i] + nums[j] == target, (
                    f"{name}({nums}, {target}) вернула {result}, "
                    f"но сумма {nums[i]} + {nums[j]} != {target}"
                )

        checks += 1

    return checks


if __name__ == "__main__":
    random.seed(42)

    total = 0

    for fn in (bubble_sort, insertion_sort, selection_sort):
        check_sorting(fn)
        total += 100

    total += check_search()
    total += check_two_sum()

    print(f"OK: {total} проверок")