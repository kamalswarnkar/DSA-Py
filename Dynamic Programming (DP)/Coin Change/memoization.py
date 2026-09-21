"""
Coin Change — Counting Ways using Memoization (Top-Down DP)

Problem:
    Given a set of coin denominations and a target sum, find the
    number of different ways to make the target sum.

    Each coin can be used any number of times.

Approach:
    Memoization (Top-Down Dynamic Programming)

    We use the same Include / Exclude choices as the recursive
    solution, but store the result of every subproblem so that
    it is not calculated again.

    For each state (i, target):

        1. Include the current coin:
           - Reduce the target by the coin value.
           - Keep `i` unchanged because the coin can be reused.

        2. Exclude the current coin:
           - Move to the previous coin.

Memoization:
    memo[i][target] stores the number of ways to form `target`
    using the first `i` coins.

Base Cases:
    • target == 0 → one valid way.
    • i == 0 → no coins are available.
    • target < 0 → target cannot be formed.

Time Complexity:
    O(N × S)

    There are N × S possible states, and each state is solved
    only once.

Space Complexity:
    O(N × S)

    For the memoization table.

    Additionally, O(N + S) recursion-stack space may be used.

where,
    N = number of coin denominations
    S = target sum

Note:
    The order of coins does not create a new way.
    A coin can be used unlimited times.
"""

def countWays(coins, n, s):
    memo = [[-1] * (n + 1) for _ in range(s + 1)]

    def solve(i, j):
        if j == 0:
            return 1
        
        if i == 0 or j < 0:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]
        else:
            memo[i][j] = solve(i, j - coins[i - 1]) + solve(i - 1, j)

        return memo[i][j]

    return solve(n, s)