"""
Minimum Coins to Make a Given Value using Tabulation

Problem:
    Given an array of coin denominations and a target value,
    find the minimum number of coins required to make exactly
    that value.

    Each coin can be used any number of times.

    Return -1 if the target value cannot be formed.

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[value]` stores the minimum number of coins required
    to make the given `value`.

    Build the solution from value 0 up to the target value.

    For every value:
        1. Try every available coin.
        2. If the coin can be used, look at the solution for
           the remaining value.
        3. Add one coin and take the minimum.

Base Cases:
    • dp[0] = 0
    • dp[value] = -1 if the value cannot be formed.

Recurrence:
    dp[value] = 1 + min(
        dp[value - coin]
    )

    for every coin <= value.

Time Complexity:
    O(N × V)

    There are V states, and each state tries N coins.

Space Complexity:
    O(V)

    The DP array stores the result for every value from
    0 to V.

where,
    N = number of coin denominations
    V = target value
"""

def minCoins(coins, val):
    dp = [-1] * (val + 1)

    dp[0] = 0

    for value in range(1, val + 1):
        for coin in coins:
            if coin <= value:
                if dp[value - coin] != -1:
                    coins_needed = dp[value - coin] + 1
                    if dp[value] == -1 or coins_needed < dp[value]:
                        dp[value] = coins_needed

    return dp[val]