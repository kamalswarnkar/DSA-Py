"""
Number of Unique Paths using Tabulation

Problem:
    Given an `a × b` matrix with the initial position at the
    top-left cell, find the number of unique paths to reach
    the bottom-right cell.

    Allowed moves:
        • Down  → matrix[i + 1][j]
        • Right → matrix[i][j + 1]

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[i][j]` represents:

        Number of unique paths from the top-left cell
        to cell (i, j).

    To reach cell (i, j), the previous cell must be either:

        • (i - 1, j) → move down
        • (i, j - 1) → move right

    Therefore:

        dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

Base Cases:
    • Every cell in the first row has exactly one path:
        move only right.

    • Every cell in the first column has exactly one path:
        move only down.

Time Complexity:
    O(A × B)

    Every cell of the matrix is computed once.

Space Complexity:
    O(A × B)

    The DP table requires A × B space.

where,
    A = number of rows
    B = number of columns
"""


def numberOfUniquePaths(a, b):
    dp = [[0] * (b + 1) for _ in range(a + 1)]

    for i in range(1, a + 1):
        dp[i][1] = 1

    for j in range(1, b + 1):
        dp[1][j] = 1

    for i in range(2, a + 1):
        for j in range(2, b + 1):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[a][b]