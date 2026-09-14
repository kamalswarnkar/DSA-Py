"""
Permutations

Problem:
    Given an array of distinct integers, generate all possible
    permutations of the array.

    A permutation is an arrangement containing every element
    exactly once.

Backtracking Idea:
    At every position, choose one element that has not been used yet.

    There are two common ways to track which elements are available:

        Method 1:
            Use a `used[]` array.

        Method 2:
            Swap elements in-place so that the current position
            is fixed directly.

Number of Permutations:
    N!

Time Complexity:
    O(N * N!)

    There are N! permutations, and copying each permutation
    takes O(N).

Space Complexity:
    Method 1:
        O(N) auxiliary space for `used[]`, recursion, and `curr`.

    Method 2:
        O(N) auxiliary space for recursion.
        The input array is modified in-place and restored
        through backtracking.

where,
N = number of elements
"""

#========================
# Method 1 - used[]
#========================
def permute_I(arr):
    n = len(arr)
    result = []
    curr = []
    used = [False] * n

    def backtrack():
        if len(curr) == n: # base case
            result.append(curr.copy())
            return

        for idx in range(n):
            if used[idx]: # used
                continue

            curr.append(arr[idx]) # choose
            used[idx] = True

            backtrack() # explore

            curr.pop() # undo
            used[idx] = False

    backtrack()

    return result

#========================
# Method 2 - swapping
#========================
def permute_II(arr):
    n = len(arr)
    result = []

    def backtrack(pos): # base case
        if pos == n:
            result.append(arr.copy())
            return

        for candidate in range(pos, n):
            arr[candidate], arr[pos] = arr[pos], arr[candidate] # choose - swapping
            backtrack(pos + 1) # explore
            arr[candidate], arr[pos] = arr[pos], arr[candidate] # undo - re-swap

    backtrack(0)

    return result
