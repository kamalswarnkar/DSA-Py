"""
Sum of Subsets

Problem:
    Given an array of positive integers and a target sum, find all
    subsets whose elements add up exactly to the target.

    Each array element can be used at most once.

Backtracking Idea:
    For every element, we have two choices:

        1. Include the current element.
        2. Exclude the current element.

    Since all elements are positive:
        • If current_sum == target → a valid subset is found.
        • If current_sum > target → we can stop exploring this path.

Time Complexity:
    O(2^N)

Space Complexity:
    O(N)

where,
N = number of elements

Note:
• Every element can be selected at most once.
• Positive numbers allow the `current_sum > target` pruning.
"""

def sumOfSubsets(arr, target):
    result = []
    curr = []
    total = 0

    def backtrack(idx):
        nonlocal total

        if total == target: # base case 1
            result.append(curr.copy())
            return

        if idx == len(arr) or total > target: # base case 2
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