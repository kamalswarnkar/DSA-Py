"""
0/1 Knapsack Problem using Memoization

Problem:
    Given `n` items, where each item has a value and a weight,
    select items such that:

        • The total weight does not exceed the capacity.
        • The total value is maximized.
        • Each item can be selected at most once.

Approach:
    Memoization (Top-Down Dynamic Programming)

    We use the same recursive decision process as the recursive
    solution, but store the result of every subproblem.

    `memo[cap][n]` represents:

        Maximum value obtainable using the first `n` items
        with a remaining capacity of `cap`.

    For every item, we have two choices:

        1. Exclude the current item.
        2. Include the current item, if its weight fits.

    If the item does not fit, it must be excluded.

Base Cases:
    • If there are no items left (`n == 0`), return 0.
    • If the remaining capacity is 0 (`cap == 0`), return 0.

Time Complexity:
    O(N × C)

    There are (N + 1) × (C + 1) possible states, and each
    state is solved only once.

Space Complexity:
    O(N × C)

    O(N × C) space is used for the memoization table.

    Additionally, O(N) recursion-stack space is required.

where,
    N = number of items
    C = maximum knapsack capacity

Note:
    Each item can be selected at most once, which is why the
    recursive call moves from `n` to `n - 1` after both
    including and excluding an item.
"""

def knapsack(val, wt, cap):
    n = len(val)
    memo = [[-1] * (n + 1) for _ in range(cap + 1)]

    def solve(cap, n):
        if n == 0 or cap == 0:
            return 0

        if memo[cap][n] != -1:
            return memo[cap][n]

        if wt[n - 1] > cap:
            memo[cap][n] = solve(cap, n - 1)
        else:
            memo[cap][n] = max(solve(cap, n - 1), val[n - 1] + solve(cap - wt[n - 1], n - 1))

        return memo[cap][n]

    return solve(cap, n)