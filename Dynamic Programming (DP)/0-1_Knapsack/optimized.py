"""
0/1 Knapsack Problem using Optimized Tabulation

Problem:
    Given `n` items, where each item has a value and a weight,
    select items such that the total weight does not exceed
    the knapsack capacity while maximizing total value.

    Each item can be selected at most once.

Approach:
    Optimized Tabulation (1D Dynamic Programming)

    Instead of maintaining:

        dp[item][capacity]

    we use a single array:

        dp[capacity]

    where:

        dp[c] = maximum value achievable with capacity `c`
                using the items processed so far.

    For every item, we update capacities from right to left.

    The reverse traversal is essential because it ensures that
    the current item is used at most once.

    Recurrence:

        dp[c] = max(
            dp[c],
            value + dp[c - weight]
        )

    If we traversed from left to right, `dp[c - weight]`
    could already contain the current item, causing the same
    item to be selected multiple times. That would turn the
    solution into an Unbounded Knapsack solution.

Time Complexity:
    O(N × C)

    Each of the N items is processed for every relevant
    capacity up to C.

Space Complexity:
    O(C)

    Only one DP array of size C + 1 is used.

where,
    N = number of items
    C = knapsack capacity
"""

def knapsack(val, wt, cap):
    n = len(val)

    dp = [0] * (cap + 1)

    for i in range(n):
        weight = wt[i]
        value = val[i]

        for capacity in range(cap, weight - 1, -1):
            dp[capacity] = max(dp[capacity], value + dp[capacity - weight])

    return dp[cap]