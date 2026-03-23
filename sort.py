"""
Sort implementation — this is the MUTABLE file.
Agents should edit this to maximize throughput (elements/sec).
"""
import numpy as np


def sort_array(arr: list[int]) -> list[int]:
    """Sort an array of integers. Return a new sorted list."""
    return np.sort(np.array(arr, dtype=np.int64)).tolist()
