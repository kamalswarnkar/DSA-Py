"""
Minimum Coins to Make a Given Value using Recursion

Problem:
    Given an array of coin denominations and a target value,
    find the minimum number of coins required to make exactly
    that value.

    Each coin can be used any number of times.

    Return -1 if the target value cannot be formed.

Approach:
    Recursion

Recursive Idea:
    For every coin that does not exceed the current value:

        1. Choose the coin.
        2. Recursively solve the remaining value.
        3. Take the minimum number of coins among all choices.

    Since a coin can be used unlimited times, the same coin
    can be considered again in the recursive call.

Base Cases:
    • val == 0 → 0 coins are required.
    • If no coin can form the value → return -1.

Recurrence:
    f(val) = 1 + min(
        f(val - coin)
    )

    for every coin <= val.

Time Complexity:
    O(N^V)

    At each state, up to N coins can be tried, and the recursion
    depth can be as large as V when the smallest coin is 1.

Space Complexity:
    O(V)

    The recursion stack can grow up to V levels.

where,
    N = number of coin denominations
    V = target value
"""

def minCoins(coins, val):
    if val == 0:
        return 0

    n = len(coins)
    res = -1

    for i in range(n):
        if coins[i] <= val:
            sub_res = minCoins(coins, val - coins[i])

            if sub_res == -1:
                continue

            if res == -1 or sub_res + 1 < res:
                res = sub_res + 1

    return res