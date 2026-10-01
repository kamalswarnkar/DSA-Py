"""
Maximum Sum without 2 Consecutive Elements using Tabulation

Problem:
    Given an array of integers, find the maximum possible sum
    such that no two selected elements are consecutive.

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[i]` represents:

        Maximum sum that can be obtained using the
        first `i` elements without selecting two
        consecutive elements.

    For every element, we have two choices:

        1. Exclude the current element:
               dp[i - 1]

        2. Include the current element:
               arr[i - 1] + dp[i - 2]

           If we include arr[i - 1], we must skip
           arr[i - 2].

    Therefore:

        dp[i] =
            max(
                dp[i - 1],
                arr[i - 1] + dp[i - 2]
            )

Base Cases:
    • dp[0] → 0
    • dp[1] → arr[0]
    • dp[2] → max(arr[0], arr[1])

Time Complexity:
    O(N)

    Each DP state is computed exactly once.

Space Complexity:
    O(N)

    The DP array stores the result for all N states.

where,
    N = number of elements in the array
"""

def maxSum(arr):
    n = len(arr)

    if n == 0:
        return 0

    if n == 1:
        return arr[0]

    if n == 2:
        return max(arr[0], arr[1])

    dp = [0] * (n + 1)
    dp[0], dp[1], dp[2] = 0, arr[0], max(arr[0], arr[1])

    for i in range(3, n + 1):
        exclude = dp[i - 1]
        include = arr[i - 1] + dp[i - 2]

        dp[i] = max(include, exclude)

    return dp[n]