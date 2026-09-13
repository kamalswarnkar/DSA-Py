"""
Generate All Subsets

Problem:
    Given an array of distinct integers, generate all possible subsets
    of the array.

    The empty subset [] must also be included.

Backtracking Pattern:
    For every element, we have exactly two choices:

        1. Include the current element.
        2. Exclude the current element.

    This creates a binary decision tree with 2^N possible subsets.

Time Complexity:
    O(N * 2^N)

    There are 2^N subsets, and copying each subset can take O(N).

Space Complexity:
    O(N)

    O(N) recursion depth and O(N) space for the current subset,
    excluding the space required to store the final result.

where,
N = number of elements
"""


def subset(arr):
    result = []
    curr = []

    def backtrack(idx):
        if idx == len(arr): # base case
            result.append(curr.copy())
            return

        # include
        curr.append(arr[idx]) # choose
        backtrack(idx + 1) # explore
        curr.pop() # undo

        # exlude
        backtrack(idx + 1)

    backtrack(0)

    return result