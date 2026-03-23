"""
Sort implementation — this is the MUTABLE file.
Agents should edit this to maximize throughput (elements/sec).
"""


def sort_array(arr: list[int]) -> list[int]:
    """Sort an array of integers. Return a new sorted list."""
    # Naive quicksort — baseline ~925k elem/s
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return sort_array(left) + middle + sort_array(right)
