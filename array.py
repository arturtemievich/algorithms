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


def compute_lps(pattern: str) -> List[int]:
    """Longest Proper Prefix which is Suffix (LPS) array
    """
    n = len(pattern)
    lps = [0] * n

    prefix = 0
    for i in range(1, n):
        while prefix and pattern[i] != pattern[prefix]:
            prefix = lps[prefix - 1]

        if pattern[prefix] == pattern[i]:
            prefix += 1
            lps[i] = prefix
    return lps


def KMP_search():
    """Knuth-Morris-Pratt (KMP) Pattern Search algorithm.
    Search a pattern or a sub-string.
    """
    pass


def main():
    pattern = "ACABACACD"
    print(f"pattern: {pattern}")
    print(compute_lps(pattern=pattern))


if __name__ == "__main__":
    main()
