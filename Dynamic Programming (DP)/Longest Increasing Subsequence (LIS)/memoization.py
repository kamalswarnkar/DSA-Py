"""
Longest Increasing Subsequence (LIS) using Memoization

Problem:
    Given an array of integers, find the length of the longest
    strictly increasing subsequence.

Approach:
    Memoization (Top-Down Dynamic Programming)

    `memo[i]` stores:

        The length of the Longest Increasing Subsequence
        ending at index `i`.

    For every previous index `j`:

        if arr[j] < arr[i]:

            LIS ending at i
            =
            LIS ending at j + current element

    Therefore:

        memo[i] = max(memo[i], memo[j] + 1)

    Since the LIS can end at any index, the final answer is
    the maximum value in the memo array.

Time Complexity:
    O(N²)

    There are N states, and each state checks at most N
    previous elements.

Space Complexity:
    O(N)

    O(N) for the memoization array and O(N) recursion stack.

where,
    N = number of elements in the array
"""

def lis(arr):
    n = len(arr)

    if n == 0:
        return 0

    memo = [-1] * n

    def solve(curr_idx):
        if memo[curr_idx] != -1:
            return memo[curr_idx]

        best_len = 1

        for prev_idx in range(curr_idx):
            if arr[curr_idx] > arr[prev_idx]:
                best_len = max(best_len, solve(prev_idx) + 1)

        memo[curr_idx] = best_len

        return memo[curr_idx]

    res = 0
    for i in range(n):
        res = max(res, solve(i))

    return res