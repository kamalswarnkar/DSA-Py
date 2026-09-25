"""
Minimum Jumps to Reach the End using Tabulation

Problem:
    Given an array where arr[i] represents the maximum number of
    positions that can be jumped from index i, find the minimum
    number of jumps required to reach the last index.

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[i]` stores the minimum number of jumps required to reach
    index `i` from index 0.

Time Complexity:
    O(N²)

    For every index, we may check all previous indices.

Space Complexity:
    O(N)

    O(N) space is used for the DP array.

where,
    N = length of the array
"""

import sys

def minJumps(arr):
    n = len(arr)

    if n == 0 or n == 1:
        return 0

    dp = [sys.maxsize] * n
    dp[0] = 0

    for i in range(1, n):
        for j in range(i):
            if (i <= j + arr[j]) and (dp[j] != sys.maxsize):
                dp[i] = min(dp[i], dp[j] + 1)

    return dp[n - 1]