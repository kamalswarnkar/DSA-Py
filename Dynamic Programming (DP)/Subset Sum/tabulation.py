"""
Subset Sum Problem using Tabulation

Problem:
    Given an array of integers, count the number of subsets
    whose elements sum exactly to a given target sum `s`.

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[i][j]` represents:

        Number of subsets that can be formed using the
        first `i` elements whose sum is exactly `j`.

    For every element, we have two choices:

        1. Exclude the current element:
               dp[i - 1][j]

        2. Include the current element:
               dp[i - 1][j - arr[i - 1]]

           This choice is possible only when:
               arr[i - 1] <= j

    Therefore:

        dp[i][j] =
            dp[i - 1][j]
            + dp[i - 1][j - arr[i - 1]]

        when arr[i - 1] <= j.

    Otherwise:

        dp[i][j] = dp[i - 1][j]

Base Cases:
    • dp[i][0] = 1
      The empty subset always produces sum 0.

    • dp[0][j] = 0 for j > 0
      No elements cannot produce a positive sum.

Time Complexity:
    O(N × S)

    Every cell of the DP table is computed once.

Space Complexity:
    O(N × S)

    The DP table contains (N + 1) × (S + 1) states.

where,
    N = number of elements in the array
    S = target sum
"""

def subsets(arr, s):
    n = len(arr)

    if n == 0:
        return 0

    dp = [[0] * (s + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, s + 1):
            exclude = dp[i - 1][j]
            include = 0

            if arr[i - 1] <= j:
                include = dp[i - 1][j - arr[i - 1]]

            dp[i][j] = include + exclude

    return dp[n][s]