"""
Minimum Jumps to Reach the End using Recursion

Problem:
    Given an array where arr[i] represents the maximum number of
    positions that can be jumped from index i, find the minimum
    number of jumps required to reach the last index.

Approach:
    Recursion

    Consider the last index as the destination. For every index
    before it, check whether that index can reach the destination.

    If it can:
        1. Recursively find the minimum jumps required to reach
           that index.
        2. Add one jump to move from that index to the destination.
        3. Keep the minimum among all possible choices.

Base Case:
    If the array contains only one element, we are already at the
    destination, so zero jumps are required.

Time Complexity:
    O(N^N)

    In the worst case, each recursive call can branch into many
    smaller subproblems, resulting in exponential growth of the
    recursion tree.

Space Complexity:
    O(N)

    O(N) maximum recursion-stack space.

where,
    N = length of the array

Note:
    `sys.maxsize` is used to represent an unreachable state.
"""

import sys

def minJumps(arr, n):
    if n == 1:
        return 0

    res = sys.maxsize

    for i in range(n - 1):
        if i + arr[i] >= n - 1:
            sub_res = minJumps(arr, i + 1)

            if sub_res != sys.maxsize:
                res = min(res, sub_res + 1)

    return res