"""
Minimum Coins to Make a Given Value using Memoization

Problem:
    Given an array of coin denominations and a target value,
    find the minimum number of coins required to make exactly
    that value.

    Each coin can be used any number of times.

    Return -1 if the target value cannot be formed.

Approach:
    Memoization (Top-Down Dynamic Programming)

    `memo[value]` stores the minimum number of coins required
    to make the given `value`.

    For every coin <= value:
        1. Choose the coin.
        2. Recursively solve the remaining value.
        3. Take the minimum valid result.

Base Cases:
    • value == 0 → 0 coins are required.
    • No valid combination → -1.

Recurrence:
    f(value) = 1 + min(
        f(value - coin)
    )

    for every coin <= value.

Time Complexity:
    O(N × V)

    There are V possible states, and each state tries N coins.

Space Complexity:
    O(V)

    O(V) for the memoization array and O(V) recursion-stack
    space in the worst case.

where,
    N = number of coin denominations
    V = target value
"""

def minCoins(coins, val):
    if val == 0:
        return 0

    memo = [-1] * (val + 1)

    def solve(value):
        if value == 0:
            return 0

        if memo[value] != -1:
            return memo[value]

        res = -1

        for coin in coins:
            if coin <= value:
                sub_result = solve(value - coin)

                if sub_result == -1:
                    continue

                if res == -1 or sub_result + 1 < res:
                    res = sub_result + 1

        memo[value] = res

        return memo[value]

    return solve(val)