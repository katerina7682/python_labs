def linear_search(nums, x):
    """Индекс первого вхождения x или -1.
    """
    for i, value in enumerate(nums):
        if value == x:
            return i
    return -1
def binary_search(sorted_nums, x):
    lo=0
    hi=len(sorted_nums)-1
    while lo<=hi:
        mid=(lo+hi)//2
        if x==sorted_nums[mid]:
            return mid
        elif x<sorted_nums[mid]:
            hi=mid-1
        else:
            lo=mid+1
    return -1
def two_sum_brute(nums, target):
    """Пара индексов (i, j), i < j, nums[i] + nums[j] == target, или None.

    """
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return (i, j)
    return None
def two_sum_fast(nums: list, target) -> tuple[int, int] | None:
    """Находит пару индексов (i, j) с i < j за один проход через словарь."""
    seen = {}
    for j, x in enumerate(nums):
        complement = target - x
        if complement in seen:
            return (seen[complement], j)
        if x not in seen:
            seen[x] = j
    return None
    
