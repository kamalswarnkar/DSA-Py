"""
Longest Common Subsequence (LCS) using Tabulation

Problem:
    Given two strings s1 and s2, find the length of their
    Longest Common Subsequence.

    A subsequence:
        • Maintains the relative order of characters.
        • Does not require characters to be contiguous.

Approach:
    Dynamic Programming - Tabulation (Bottom-Up)

DP State:
    dp[i][j] = length of the LCS of:
               s1[0:i] and s2[0:j]

Transition:
    If the current characters match:
        dp[i][j] = 1 + dp[i - 1][j - 1]

    Otherwise:
        dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

Base Case:
    If either string is empty, the LCS length is 0.

Time Complexity:
    O(N * M)

Space Complexity:
    O(N * M)

where,
    N = length of s1
    M = length of s2

Key Idea:
    Instead of recursively solving the same subproblems repeatedly,
    we build the solution from smaller prefixes to larger prefixes.
"""

def lcs(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[None] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for j in range(m + 1):
            if i == 0 or j == 0:
                dp[i][j] = 0
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = 1 + dp[i - 1][j - 1]
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]