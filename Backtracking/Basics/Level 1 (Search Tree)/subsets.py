"""
Generate Subsets

Problem:
    Given an array of distinct integers, generate all possible subsets of the array.
    The empty subset [] must also be included.
    The order of the subsets does not matter.

    Goal: <Include/Exclude>
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