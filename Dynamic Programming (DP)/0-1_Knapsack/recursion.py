"""
0/1 Knapsack Problem using Recursion

Problem:
    Given `n` items, where each item has a value and a weight,
    select items such that:

        • The total weight does not exceed the capacity.
        • The total value is maximized.
        • Each item can be selected at most once.

Approach:
    Recursion

    For every item, we have two choices:

        1. Exclude the current item.
        2. Include the current item, if its weight fits
           within the remaining capacity.

    We recursively explore both choices and take the one
    that gives the maximum value.

Base Cases:
    • If there are no items left (`n == 0`), return 0.
    • If the remaining capacity is 0 (`cap == 0`), return 0.

Decision:
    If the current item's weight exceeds the remaining capacity,
    it cannot be included.

    Otherwise:

        max(
            exclude current item,
            include current item
        )

Time Complexity:
    O(2^N)

    In the worst case, every item creates two recursive branches:
    include or exclude.

Space Complexity:
    O(N)

    The recursion depth can reach N.

where,
    N   = number of items
    cap = maximum knapsack capacity

Note:
    This is called "0/1" Knapsack because every item has exactly
    two possibilities: either take it (1) or leave it (0).
"""

def knapsack(val, wt, cap, n):
    if n == 0 or cap == 0:
        return 0

    if wt[n - 1] > cap:
        return knapsack(val, wt, cap, n - 1)
    else:
        return max(knapsack(val, wt, cap, n - 1), val[n - 1] + knapsack(val, wt, cap - wt[n - 1], n - 1))