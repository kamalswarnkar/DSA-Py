"""
Coin Change — Counting Ways using Recursion

Problem:
    Given a set of coin denominations and a target sum, find the
    number of different ways to make the target sum.

    Each coin can be used any number of times.

Approach:
    Recursion using Include / Exclude choices.

    For each coin, we have two choices:

        1. Include the current coin:
           - Subtract its value from the target.
           - Keep the same coin available because it can be reused.

        2. Exclude the current coin:
           - Move to the previous coin.
           - The current coin can no longer be used.

Base Cases:
    • target == 0 → one valid way has been found.
    • target < 0 → target cannot be formed.
    • n == 0 → no coins are available.

Time Complexity:
    O(2^(N + S)) approximately

    The recursive solution explores a large number of repeated
    subproblems.

Space Complexity:
    O(N + S)

    Due to the recursion depth.

where,
    N = number of coin denominations
    S = target sum

Note:
    The order of coins does not create a new way.

    For example:
        [1, 2, 2] and [2, 1, 2]
    
    represent the same combination.
"""

def countWays(coins, n, s):
    if s == 0:
        return 1
    if s < 0 or n == 0:
        return 0

    return countWays(coins, n, s - coins[n - 1]) + countWays(coins, n - 1, s)
