"""
Generate All Binary Strings

Problem:
    Given an integer n, generate all binary strings of exactly length n.

    A binary string contains only 0 and 1.

Backtracking Pattern:
    At every position, we have two choices:

        1. Choose '0'
        2. Choose '1'

    We recursively make a choice for every position until the
    string reaches length n.

    Therefore, the total number of binary strings is:

        2^N

Time Complexity:
    O(N * 2^N)

    There are 2^N binary strings, and creating each string takes O(N).

Space Complexity:
    O(N)

    O(N) recursion depth and O(N) space for the current string,
    excluding the space required to store the final result.

where,
N = length of the binary string
"""

def binaryString(n):
    result = []
    curr = []

    def backtrack():
        if len(curr) == n: # base case
            result.append(''.join(curr))
            return

        for choice in ['0', '1']:
            curr.append(choice) # choose
            backtrack() # explore
            curr.pop() # undo

    backtrack()

    return result