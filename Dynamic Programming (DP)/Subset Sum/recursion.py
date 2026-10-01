"""
Subset Sum Problem using Recursion

Problem:
    Given an array of integers, count the number of subsets
    whose elements sum exactly to a given target sum `s`.

Approach:
    Recursion using the Include / Exclude pattern.

    For every element, we have two choices:

        1. Exclude the current element:
               subsets(arr, n - 1, s)

        2. Include the current element:
               subsets(arr, n - 1, s - arr[n - 1])

    Therefore:

        count(n, s) =
            count(n - 1, s)
            + count(n - 1, s - arr[n - 1])

Base Case:
    When no elements remain:

        • s == 0 → A valid subset has been formed.
        • s != 0 → No valid subset exists.

Time Complexity:
    O(2^N)

    Each element creates two recursive branches:
    include and exclude.

Space Complexity:
    O(N)

    The maximum recursion depth is N.

where,
    N = number of elements in the array
    S = target sum
"""

def subsets(arr, n, s):
    if n == 0:
        if s == 0:
            return 1
        else:
            return 0

    exclude = subsets(arr, n - 1, s)
    include = subsets(arr, n - 1, s - arr[n - 1])

    return include + exclude