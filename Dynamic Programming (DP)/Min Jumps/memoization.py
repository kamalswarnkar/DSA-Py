"""
Minimum Jumps to Reach the End using Memoization

Problem:
    Given an array where arr[i] represents the maximum number of
    positions that can be jumped from index i, find the minimum
    number of jumps required to reach the last index.

Approach:
    Memoization (Top-Down Dynamic Programming)

    `memo[n]` stores the minimum number of jumps required to reach
    index `n - 1` using the first `n` elements.

Time Complexity:
    O(N²)

    There are O(N) states, and each state may check O(N) previous
    positions.

Space Complexity:
    O(N)

    O(N) for the memoization array and O(N) recursion-stack space.

where,
    N = length of the array
"""

import sys

def minJumps(arr):
    n = len(arr)

    if n == 1:
        return 0

    memo = [-1] * (n + 1)

    def solve(size):
        if size == 1:
            return 0

        if memo != -1:
            return memo[size]

        res = sys.maxsize

        for i in range(size - 1):
            if i + arr[i] >= size - 1:
                sub_res = solve(i + 1)

                if sub_res != sys.maxsize:
                    res = min(res, sub_res + 1)

        memo[size] = res

        return memo[size]

    return solve(n)
