"""
Longest Increasing Subsequence (LIS) using Tabulation

Problem:
    Given an array of integers, find the length of the longest
    strictly increasing subsequence.

    A subsequence:
        • Maintains the original order of elements.
        • Does not need to contain contiguous elements.
        • Must have every next element greater than the previous one.

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[i]` represents:

        The length of the Longest Increasing Subsequence
        that ends at index `i`.

    For every element `arr[i]`, check all previous elements
    `arr[j]`.

    If:

        arr[i] > arr[j]

    then `arr[i]` can be appended to the increasing subsequence
    ending at `j`.

    Therefore:

        dp[i] = max(dp[i], dp[j] + 1)

    Finally, the LIS can end at any index, so the answer is:

        max(dp)

Base Case:
    Every individual element is itself an increasing subsequence
    of length 1.

    Therefore:

        dp[i] = 1

Time Complexity:
    O(N²)

    For every element, we check all previous elements.

Space Complexity:
    O(N)

    The `dp` array stores one value for every element.

where,
    N = number of elements in the array

Note:
• This implementation finds the length of the LIS, not the
  actual subsequence.
• The subsequence must be strictly increasing.
"""

def lis(arr):
    n = len(arr)

    if n == 0:
        return 0
    
    dp = [1] * n

    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                dp[i] = max(dp[i], dp[j] + 1)

    res = max(dp)

    return res