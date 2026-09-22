"""
Maximum Sum Increasing Subsequence (MSIS)

Problem:
    Given an array of integers, find the maximum possible sum
    of an increasing subsequence.

Approach:
    Dynamic Programming (Tabulation)

    `msis[i]` represents the maximum sum of an increasing
    subsequence that ends at index `i`.

    For every pair (j, i):

        If arr[j] < arr[i]:
            arr[i] can be added after the subsequence ending at j.

        Therefore:

            msis[i] = max(msis[i],
                           arr[i] + msis[j])

    The answer is the maximum value in the `msis` array.

Time Complexity:
    O(N²)

Space Complexity:
    O(N)

where,
    N = length of the array
"""

def maxSIS(arr):
    n = len(arr)
    msis = [x for x in arr]

    for i in range(1, n):
        for j in range(i):
            if arr[j] < arr[i]:
                msis[i] = max(msis[i], arr[i] + msis[j])

    return max(msis)