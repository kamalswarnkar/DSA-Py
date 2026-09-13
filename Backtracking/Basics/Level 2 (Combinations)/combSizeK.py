"""
Combinations of Size K

Problem:
    Given two integers n and k, generate all possible combinations
    of k distinct numbers chosen from:

        1, 2, 3, ..., n

    The order of elements inside a combination does not matter.

========================================================
LEVEL 1: INCLUDE / EXCLUDE
========================================================

Backtracking Idea:
    For every number, make two choices:

        1. Include the current number.
        2. Exclude the current number.

    This creates a binary decision tree similar to the
    "Generate Subsets" problem.

    We stop a branch once k elements have been selected.

Time Complexity:
    O(2^N + C(N, K) * K)

    The include/exclude tree can contain up to 2^N states.
    Additionally, every valid combination must be copied,
    which costs O(K).

Space Complexity:
    O(K)

    The current combination and recursion depth require O(K)
    auxiliary space, excluding the output.

========================================================
LEVEL 2: CHOICE + START INDEX + CONSTRAINT
========================================================

Backtracking Idea:
    Instead of explicitly making an include/exclude decision,
    directly choose the next element from the remaining candidates.

    `start` ensures:
        • We never reuse an element.
        • We never generate duplicate combinations.
        • Elements are always chosen in increasing order.

    For every recursive call:
        1. Choose a candidate.
        2. Explore with candidates after it.
        3. Undo the choice.

Time Complexity:
    O(C(N, K) * K)

    There are C(N, K) valid combinations, and copying each
    combination takes O(K).

Space Complexity:
    O(K)

    The current combination and recursion depth require O(K)
    auxiliary space, excluding the output.

========================================================

where,
N = number of available numbers
K = size of each combination
C(N, K) = number of possible combinations

Note:
• Each number can be selected at most once.
• [1, 2] and [2, 1] represent the same combination.
• Processing numbers from left to right automatically preserves
  the canonical order of every combination.
"""

#==================================
# Level 1 Method of Include/Exclude
#==================================
def combI(n, k):
    result = []
    curr = []

    def backtrack(idx):
        if len(curr) == k: # base case 1
            result.append(curr.copy())
            return

        if idx == n: # base case 2
            return

        # Include
        curr.append(idx + 1) # choose
        backtrack(idx + 1) # explore
        curr.pop() # undo

        # Exclude
        backtrack(idx + 1)

    backtrack(0)

    return result

#====================================================
# Level 2 Method of Choice + Start Index + Constraint
#====================================================
def combII(n, k):
    result = []
    curr = []

    def backtrack(start_idx):
        # Constraint
        if len(curr) == k: # base case 1
            result.append(curr.copy())
            return

        # Choice
        for choice in range(start_idx, n + 1):
            curr.append(choice) # choose
            backtrack(choice + 1) # explore
            curr.pop() # undo

    backtrack(1) # Start Index

    return result
