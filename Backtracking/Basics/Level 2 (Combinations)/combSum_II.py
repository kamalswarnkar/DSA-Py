"""
Combination Sum II

Problem:
    Given an array of integers that may contain duplicates and a target
    integer, find all unique combinations whose sum equals the target.

    Each element can be used at most once.
    Duplicate combinations must not appear in the answer.

Backtracking Idea:
    We build combinations while keeping track of the current sum.

    Since each element can be used only once:
        • Move to the next index after choosing an element.
        • Never reuse the same array position.

    Since the array may contain duplicate values:
        • Different copies of the same value should not create duplicate
          combinations.


========================================================
LEVEL 1: INCLUDE / EXCLUDE
========================================================

For every element, make two choices:

    1. Include the current element.
    2. Exclude the current element.

Because every element can be used only once:

    Include → backtrack(idx + 1)
    Exclude → backtrack(idx + 1)

Both branches move to the next index.

Note:
    This method naturally considers every possible subset.
    Therefore, duplicate combinations may be generated when the input
    contains duplicate values.

Example:

    arr = [1, 1, 2]

    The two different `1`s can create the same combination:

        [1, 2]
        [1, 2]

    So Level 1 requires an additional duplicate-removal strategy if
    unique output is required.


========================================================
LEVEL 2: CHOICE + START INDEX + CONSTRAINT
========================================================

Sort the array first.

For every recursive call:

    1. Choose a candidate from start_idx onward.
    2. Explore using elements after that candidate.
    3. Undo the choice.

Duplicate Handling:
    After sorting, duplicate values become adjacent.

        if idx > start_idx and arr[idx] == arr[idx - 1]:
            continue

    This skips duplicate choices at the SAME recursion level.

Important:
    We skip duplicate choices only when:

        idx > start_idx

    because duplicate values are allowed in the same combination
    when they come from different positions.

Example:

    arr = [1, 1, 2]

    [1, 1] is valid because both `1`s are different elements.

    But starting two separate branches with the first `1` and second
    `1` would generate duplicate combinations, so the second `1` is
    skipped at that recursion level.

Because each element can be used only once:

    backtrack(idx + 1)

Time Complexity:
    Exponential in the worst case.

    The algorithm may explore a subset of the 2^N possible subsets,
    while copying every valid combination also costs O(K).

Space Complexity:
    O(N)

    Recursion depth can reach N, and the current combination can
    contain at most N elements, excluding the output.

where,
N = number of elements
K = size of a generated combination

Note:
• Each array element can be used at most once.
• Duplicate combinations must not appear.
• Sorting is required for the Level 2 duplicate-skipping technique.
• `idx + 1` ensures that the same array position is never reused.
"""


#==================================
# Level 1 Method of Include/Exclude
#==================================
def combSumI(arr, target):
    result = []
    curr = []
    total = 0

    def backtrack(idx):
        nonlocal total

        if total == target: # base case
            result.append(curr.copy())
            return

        if idx == len(arr) or total > target:
            return

        # Include
        curr.append(arr[idx]) # choose
        total += arr[idx]
        backtrack(idx + 1) # explore
        curr.pop() # undo
        total -= arr[idx]

        # Exclude
        backtrack(idx + 1)

    backtrack(0)

    return result


#====================================================
# Level 2 Method of Choice + Start Index + Constraint
#====================================================
def combSumII(arr, target):
    result = []
    curr = []
    total = 0

    arr.sort()

    def backtrack(start_idx):
        nonlocal total

        # Constraint
        if total == target: # base case
            result.append(curr.copy())
            return

        # pruning
        if total > target:
            return

        # Choice
        for idx in range(start_idx, len(arr)):
            if idx > start_idx and arr[idx] == arr[idx - 1]: # to avoid using duplicate elements already in the original array
                continue

            curr.append(arr[idx]) # choose
            total += arr[idx]
            backtrack(idx + 1) # explore
            curr.pop() # undo
            total -= arr[idx]

    backtrack(0) # Start Index

    return result