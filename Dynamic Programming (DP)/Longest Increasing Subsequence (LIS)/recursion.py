"""
Longest Increasing Subsequence (LIS) using Recursion

Problem:
    Given an array of integers, find the length of the longest
    strictly increasing subsequence.

Approach:
    Recursion

    `lis(i)` represents:

        The length of the Longest Increasing Subsequence
        ending at index `i`.

    To find LIS ending at `i`, check every previous index `j`.

    If:

        arr[j] < arr[i]

    then arr[i] can be added after the subsequence ending at j.

    Therefore:

        lis(i) = max(lis(i), lis(j) + 1)

    Since the LIS can end at any index, the final answer is:

        max(lis(0), lis(1), ..., lis(n-1))

Base Case:
    The LIS ending at the first element has length 1.

Time Complexity:
    O(2^N) approximately

    Many overlapping subproblems are recomputed.

Space Complexity:
    O(N)

    Due to the recursion stack.

where,
    N = number of elements in the array
"""

def lis(arr):
    n = len(arr)

    if n == 0:
        return 0

    def solve(curr_idx):
        best_len = 1

        for prev_idx in range(curr_idx):
            if arr[curr_idx] > arr[prev_idx]:
                best_len = max(best_len, solve(prev_idx) + 1)

        return best_len

    res = 0
    for i in range(n):
        res = max(res, solve(i))

    return res