"""
Maximum Sum without 2 Consecutive Elements using Recursion

Problem:
    Given an array of integers, find the maximum possible sum
    such that no two selected elements are consecutive.

Approach:
    Recursion

    For every element, we have two choices:

        1. Exclude the current element:
               maxSum(arr, n - 1)

        2. Include the current element:
               arr[n - 1] + maxSum(arr, n - 2)

           If we include arr[n - 1], we must skip arr[n - 2]
           because two consecutive elements cannot be selected.

    Therefore:

        maxSum(n) =
            max(
                maxSum(n - 1),
                arr[n - 1] + maxSum(n - 2)
            )

Base Cases:
    • n <= 0 → 0
    • n == 1 → arr[0]
    • n == 2 → max(arr[0], arr[1])

Time Complexity:
    O(2^N)

    The recursive solution repeatedly solves the same
    overlapping subproblems.

    More tightly, the recurrence is Fibonacci-like:
        O(φ^N), where φ ≈ 1.618.

Space Complexity:
    O(N)

    The maximum recursion depth is O(N).

where,
    N = number of elements in the array
"""

def maxSum(arr, n):
    if n <= 0:
        return 0
    
    if n == 1:
        return arr[0]

    if n == 2:
        return max(arr[0], arr[1])

    exclude = maxSum(arr, n - 1)
    include = arr[n - 1] + maxSum(arr, n - 2)

    return max(exclude, include)