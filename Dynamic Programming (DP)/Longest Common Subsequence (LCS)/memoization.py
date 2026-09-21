"""
Longest Common Subsequence (LCS) - Memoization Approach

Problem:
    Given two strings s1 and s2, find the length of their
    Longest Common Subsequence (LCS).

Approach:
    Memoization (Top-Down Dynamic Programming)

Idea:
    Start with the recursive LCS solution, but store the result
    of every subproblem so that it is calculated only once.

    State:
        memo[n][m] = LCS length for the first n characters of s1
                     and the first m characters of s2.

Steps:
    1. Check whether the current state has already been solved.
    2. If yes, return the stored result.
    3. If either string is empty, the LCS length is 0.
    4. If the current characters match, move diagonally.
    5. Otherwise, try both possibilities and take the maximum.
    6. Store the result before returning it.

Time Complexity:
    O(N × M)

    There are N × M possible states, and each state is
    calculated only once.

Space Complexity:
    O(N × M)

    The memoization table requires N × M space.
    The recursion stack requires O(N + M) additional space.

where,
N = length of s1
M = length of s2

Key Idea:
    Memoization converts the exponential recursive solution
    into polynomial time by avoiding repeated subproblems.
"""

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)
    memo = [[-1] * m for _ in range(n)]

    def solve(i, j):
        if memo[i][j] != -1:
            return memo[i][j]

        if i == 0 or j == 0:
            memo[i][j] = 0
        else:
            if s1[i - 1] == s2[j - 1]:
                memo[i][j] = 1 + lcs(s1, s2, i - 1, j - 1)
            else:
                memo[i][j] = max(lcs(s1, s2, i - 1, j), lcs(s1, s2, i, j - 1))

        return memo[i][j]

    return solve(n, m)