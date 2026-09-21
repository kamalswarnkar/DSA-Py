"""
Longest Common Subsequence (LCS) - Recursive Approach

Problem:
    Given two strings s1 and s2, find the length of their
    Longest Common Subsequence (LCS).

    A subsequence:
        • Maintains the original order of characters.
        • Does not require characters to be contiguous.

Example:
    s1 = "ABCBDAB"
    s2 = "BDCAB"

    LCS length = 4

Approach:
    Recursion

Idea:
    Compare the last characters of the two strings.

    1. If the last characters match:
           Include that character in the LCS and move both
           strings one position backward.

    2. If the last characters do not match:
           We have two choices:
               • Ignore the last character of s1.
               • Ignore the last character of s2.

           Take the maximum of these two possibilities.

    3. If either string becomes empty, the LCS length is 0.

Recursive Relation:

    If s1[n-1] == s2[m-1]:

        LCS(n, m) = 1 + LCS(n-1, m-1)

    Otherwise:

        LCS(n, m) = max(
            LCS(n-1, m),
            LCS(n, m-1)
        )

Time Complexity:
    O(2^(N+M))

    In the worst case, every mismatch creates two recursive
    branches.

Space Complexity:
    O(N + M)

    Due to the maximum recursion depth.

where,
N = length of s1
M = length of s2

Key Idea:
    Match → take both characters.

    Mismatch → try both possibilities and take the better one.

    This overlapping-subproblem structure is what makes LCS
    a good candidate for Dynamic Programming.
"""

def lcs(s1, s2, n, m):
    if n == 0 or m == 0: # if of them is empty -> no common subsequence
        return 0

    if s1[n - 1] == s2[m - 1]: # if last char is common, include that and move with remaining chars
        return 1 + lcs(s1, s2, n - 1, m - 1)
    else:
        # If the characters do not match, try both possibilities:
        # 1. Skip the current character of s1.
        # 2. Skip the current character of s2.
        # Take whichever produces the longer subsequence.
        return max(lcs(s1, s2, n - 1, m), lcs(s1, s2, n, m - 1))
    