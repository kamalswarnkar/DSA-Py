"""
Coin Change — Counting Ways using Tabulation (Bottom-Up DP)

Problem:
    Given a set of coin denominations and a target sum, find the
    number of different ways to make the target sum.

    Each coin can be used any number of times.

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    We build a 2D DP table where:

        dp[i][j] = number of ways to form sum `j`
                   using the first `i` coins.

    For every coin, we have two choices:

        1. Exclude the current coin:
           dp[i][j] = dp[i - 1][j]

        2. Include the current coin:
           dp[i][j] = dp[i][j - coin]

           We stay in the same row because the current coin
           can be used unlimited times.

    Therefore:

        dp[i][j] = dp[i - 1][j] + dp[i][j - coin]

Base Case:
    dp[i][0] = 1

    There is exactly one way to make sum 0:
    choose no coins.

Time Complexity:
    O(N × S)

    Every cell of the DP table is calculated once.

Space Complexity:
    O(N × S)

    The 2D DP table contains (N + 1) × (S + 1) states.

where,
    N = number of coin denominations
    S = target sum

Note:
    • A coin can be used unlimited times.
    • The order of coins does not create a new way.
    • The input array is not modified.
"""

def countWays(coins, n, s):
    dp = [[0] * (s + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = 1

    for i in range(n + 1):
        for j in range(s):
            dp[i][j] = dp[i - 1][j]

            if j >= coins[i - 1]:
                dp[i][j] += dp[i][j - coins[i - 1]]

    return dp[n][s]