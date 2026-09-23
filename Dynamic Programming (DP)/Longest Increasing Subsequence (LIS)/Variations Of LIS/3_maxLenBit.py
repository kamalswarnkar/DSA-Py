"""
Maximum Length Bitonic Subsequence

Problem:
    Given an array, find the length of the longest bitonic subsequence.

    A bitonic subsequence first increases and then decreases.

Approach:
    1. Build an LIS array.
       `lis[i]` = length of the longest increasing subsequence
       ending at index i.

    2. Build an LDS array.
       `lds[i]` = length of the longest decreasing subsequence
       starting at index i.

    3. Consider every index as the peak of the bitonic subsequence.

       bitonic_length = lis[i] + lds[i] - 1

       We subtract 1 because arr[i] is counted in both LIS and LDS.

Time Complexity:
    O(N²)

Space Complexity:
    O(N)

where,
    N = length of the array
"""

def lis(arr):
    n = len(arr)
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp

def lds(arr):
    n = len(arr)
    dp = [1] * n
    
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return dp

def maxLenBit(arr):
    n = len(arr)

    if n == 0:
        return 0
    
    LIS = lis(arr)
    LDS = lds(arr)

    res = -1

    for i in range(n):
        res = max(res, LIS[i] + LDS[i] - 1)

    return res
