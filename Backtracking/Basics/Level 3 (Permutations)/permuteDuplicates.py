"""
Permutations With Duplicates

Problem:
    Given an array of integers that may contain duplicates,
    generate all unique permutations.

    Duplicate permutations must not appear in the result.

Backtracking Idea:
    The normal permutation approach can generate the same permutation
    multiple times when duplicate values exist.

    Example:
        arr = [1, 1, 2]

    Choosing the first `1` or the second `1` produces the same
    choice at the current position.

    Therefore, at every recursion level, maintain a `seen` set
    to ensure that the same VALUE is not chosen more than once
    at that level.

    Important:
        `seen` is recreated at every recursion level.

        It does NOT mean:
            "This value has already been used in the whole permutation."

        It means:
            "I have already tried this value as a choice
             for the current position."

Method 1:
    Use `used[]` to track which array indices are already selected.

Method 2:
    Use swapping to fix one position at a time.

Time Complexity:
    O(N * N!)

    This is the general upper bound because there can be up to
    N! permutations. With duplicates, the actual number of
    unique permutations can be smaller.

Space Complexity:
    O(N)

    Excluding the output:
        • Method 1 uses O(N) for `used[]`, recursion, and `curr`.
        • Method 2 uses O(N) recursion depth.

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

        seen = set()

        for idx in range(n):
            if used[idx]: # used
                continue

            if arr[idx] in seen: # removing dupllicate choice at this level
                continue

            seen.add(arr[idx])

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

        seen = set()

        for candidate in range(pos, n):
            if arr[candidate] in seen: # removing dupllicate choice at this level
                continue

            seen.add(arr[candidate])

            arr[candidate], arr[pos] = arr[pos], arr[candidate] # choose - swapping
            backtrack(pos + 1) # explore
            arr[candidate], arr[pos] = arr[pos], arr[candidate] # undo - re-swap

    backtrack(0)

    return result
