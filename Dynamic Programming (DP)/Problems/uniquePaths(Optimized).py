"""
Number of Unique Paths using Combinatorics

Problem:
    Given an `a × b` matrix with the initial position at the
    top-left cell, find the number of unique paths to reach
    the bottom-right cell.

    Allowed moves:
        • Down  → matrix[i + 1][j]
        • Right → matrix[i][j + 1]

Approach:
    Combinatorics

    To travel from the top-left cell to the bottom-right cell:

        • We must make (a - 1) downward moves.
        • We must make (b - 1) rightward moves.

    Therefore, every valid path consists of:

        (a - 1) + (b - 1) = a + b - 2

    total moves.

    We only need to choose which of these moves are downward
    (or equivalently, which are rightward).

    Therefore:

        Number of Paths =
            C(a + b - 2, a - 1)

    Python's `math.comb()` directly calculates this binomial
    coefficient.

Time Complexity:
    O(1)

    `math.comb()` is treated as a constant-time mathematical
    operation for the algorithmic analysis here.

Space Complexity:
    O(1)

    Only a constant amount of extra space is used.

where,
    A = number of rows
    B = number of columns
"""

import math

def numberOfUniquePaths(a, b):
    return math.comb(a + b - 2, a - 1)