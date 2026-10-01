"""
Maximum Sum without 2 Consecutive Elements using Memoization

Problem:
    Given an array of integers, find the maximum possible sum
    such that no two selected elements are consecutive.

Approach:
    Memoization (Top-Down Dynamic Programming)

    `memo[i]` represents:

        Maximum sum that can be obtained using the
        first `i` elements without selecting two
        consecutive elements.

    For every element, we have two choices:

        1. Exclude the current element:
               solve(i - 1)

        2. Include the current element:
               arr[i - 1] + solve(i - 2)

           If we include arr[i - 1], we must skip
           arr[i - 2].

    Therefore:

        solve(i) =
            max(
                solve(i - 1),
                arr[i - 1] + solve(i - 2)
            )

Base Cases:
    • i <= 0 → 0
    • i == 1 → arr[0]
    • i == 2 → max(arr[0], arr[1])

Time Complexity:
    O(N)

    There are O(N) unique states, and each state
    is computed only once.

Space Complexity:
    O(N)

    O(N) space is used for the memoization array,
    plus O(N) recursion-stack space.

where,
    N = number of elements in the array
"""

def maxSum(arr):
    n = len(arr)

    if n == 0:
        return 0

    memo = [-1] * (n + 1)

    def solve(i):
        if i <= 0:
            return 0

        if i == 1:
            return arr[0]

        if i == 2:
            return max(arr[0], arr[1])

        if memo[i] != -1:
            return memo[i]

        exclude = solve(i - 1)
        include = arr[i - 1] + solve(i - 2)

        memo[i] = max(include, exclude)

        return memo[i]

    return solve(n)