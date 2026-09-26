"""
0/1 Knapsack Problem using Tabulation

Problem:
    Given `n` items, where each item has a value and a weight,
    select items such that:

        • The total weight does not exceed the capacity.
        • The total value is maximized.
        • Each item can be selected at most once.

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[capacity][items]` represents:

        Maximum value obtainable using the first `items` items
        with a knapsack capacity of `capacity`.

    For every item, we have two choices:

        1. Exclude the current item.
        2. Include the current item, if its weight fits.

    If the item does not fit, it must be excluded.

Base Cases:
    • 0 items → maximum value is 0.
    • 0 capacity → maximum value is 0.

Time Complexity:
    O(N × C)

    We fill (N + 1) × (C + 1) DP states, with O(1) work
    performed for each state.

Space Complexity:
    O(N × C)

    The 2D DP table requires O(N × C) space.

where,
    N = number of items
    C = maximum knapsack capacity

Note:
    Each item can be selected at most once, so when an item is
    included, we use the previous item state (`items - 1`).
"""

def knapsack(val, wt, cap):
    n = len(val)

    if n == 0 or cap == 0:
        return 0

    dp = [[0] * (n + 1) for _ in range(cap + 1)]

    for i in range(1, cap + 1):
        for j in range(1, n + 1):
            if wt[j - 1] > i:
                dp[i][j] = dp[i][j - 1]
            else:
                dp[i][j] = max(dp[i][j - 1], val[j - 1] + dp[i - wt[j - 1]][j - 1])

    return dp[cap][n]