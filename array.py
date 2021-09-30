from typing import List


def get_maximum_subarray_sum(array: List[int]) -> int:
    """Kadane’s algorithm is an iterative dynamic programming algorithm in which
    we search for a maximum sum contiguous subarray within a one-dimensional numeric array.
    Recurrence relation: array[i] = array[i] + array[i - 1] if array[i - 1] > 0 else array[i]
    Time  Complexity: O(n)
    Space Complexity: O(1)
    """
    for i in range(1, len(array)):
        if array[i - 1] > 0:
            array[i] += array[i - 1]
    return max(array)
