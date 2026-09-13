"""
Combination Sum

Problem:
    Given an array of distinct positive integers and a target integer,
    find all unique combinations of numbers whose sum equals target.

    A number may be chosen unlimited times.
    The order of numbers in a combination does not matter.

Backtracking Idea:
    We build the combination while keeping track of the current sum.

    Since all numbers are positive:
        • current_sum == target → valid combination
        • current_sum > target  → stop exploring this branch

The important difference from normal combinations is that
the same number can be selected again.

========================================================
LEVEL 1: INCLUDE / EXCLUDE
========================================================

Decision for arr[idx]:

    INCLUDE → choose arr[idx] again
               ↓
               backtrack(idx)

    EXCLUDE → stop using arr[idx]
               ↓
               backtrack(idx + 1)

Notice:
    Include uses the SAME idx because the number can be reused.

========================================================
LEVEL 2: CHOICE + START INDEX + CONSTRAINT
========================================================

Instead of explicitly asking include/exclude, directly choose
the next candidate from start_idx onward.

    Choose arr[idx]
        ↓
    backtrack(idx)
        ↓
    same number remains available for reuse

Why `backtrack(idx)` instead of `backtrack(idx + 1)`?

    Because the current number can be selected unlimited times.

    If we used idx + 1, the current number could not be reused.

Time Complexity:
    Exponential in the worst case.

Space Complexity:
    O(T / min(arr))

    where T = target.
    This represents the maximum possible recursion depth when
    repeatedly choosing the smallest positive number.

Note:
• All numbers are positive.
• Each number can be reused unlimited times.
• Order does not matter, so we always move forward through
  the array.
• `current_sum > target` is a valid pruning condition because
  all numbers are positive.
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

        # Include
        curr.append(arr[idx]) # choose
        total += arr[idx]
        backtrack(idx) # explore # same no. can be reused
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
            curr.append(arr[idx]) # choose
            total += arr[idx]
            backtrack(idx) # explore # same no. can be reused
            curr.pop() # undo
            total -= arr[idx]

    backtrack(0) # Start Index

    return result