"""
Subset Sum Problem using Memoization

Problem:
    Given an array of integers, count the number of subsets
    whose elements sum exactly to a given target sum `s`.

Approach:
    Memoization (Top-Down Dynamic Programming)

    `memo[i][j]` represents:

        Number of subsets that can be formed using the
        first `i` elements whose sum is exactly `j`.

    For every element, we have two choices:

        1. Exclude the current element:
               solve(i - 1, j)

        2. Include the current element:
               solve(i - 1, j - arr[i - 1])

    Therefore:

        solve(i, j) =
            solve(i - 1, j)
            + solve(i - 1, j - arr[i - 1])

Base Cases:
    • i == 0 and j == 0 → 1
      The empty subset forms sum 0.

    • i == 0 and j != 0 → 0
      No elements remain to form the target.

    • j < 0 → 0
      A negative target cannot be formed when array elements
      are non-negative.

Time Complexity:
    O(N × S)

    There are O(N × S) possible states, and each state
    is computed only once.

Space Complexity:
    O(N × S)

    O(N × S) space is used for the memoization table.

    Additionally, O(N) recursion-stack space is used.

where,
    N = number of elements in the array
    S = target sum
"""

def subsets(arr, s):
    n = len(arr)

    if n == 0:
        return 0

    memo = [[-1] * (s + 1) for _ in range(n + 1)]

    def solve(i, j):
        if j < 0:
            return 0
        
        if i == 0:
            if j == 0:
                return 1
            else:
                return 0

        if memo[i][j] != -1:
            return memo[i][j]

        exclude = solve(i - 1, j)
        include = solve(i - 1, j - arr[i - 1])

        memo[i][j] = include + exclude

        return memo[i][j]

    return solve(n, s)