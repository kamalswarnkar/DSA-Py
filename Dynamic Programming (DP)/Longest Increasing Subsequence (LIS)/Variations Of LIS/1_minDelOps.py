"""
Minimum Deletions to Make Array Sorted

Problem:
    Given an array, find the minimum number of elements that must
    be deleted so that the remaining elements are in increasing order.

Approach:
    1. Find the Length of the Longest Increasing Subsequence (LIS).
    2. Keep those LIS elements.
    3. Delete all remaining elements.

Therefore:

    Minimum Deletions = N - LIS

For LIS, we use the optimized O(N log N) approach with binary search.

Time Complexity:
    O(N log N)

Space Complexity:
    O(N)

where,
    N = length of the array
"""

def ceilIdx(tail, x):
    l = 0
    r = len(tail) - 1

    while l < r:
        m = l + (r - l)//2

        if x <= tail[m]:
            r = m
        else:
            l = m + 1

    return r

def lis(arr):
    n = len(arr)
    tail = [arr[0]]

    for i in range(n):
        if arr[i] > tail[-1]:
            tail.append(arr[i])
        else:
            c = ceilIdx(tail, arr[i])
            tail[c] = arr[i]

    return len(tail)

def minDelOps(arr):
    n = len(arr)
    l = lis(arr)

    return n - l