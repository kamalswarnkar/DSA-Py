"""
Shortest Common Supersequence

Problem:
    Given two strings s1 and s2, find the length of the shortest string
    that contains both s1 and s2 as subsequences.

Approach:
    Let solve(i, j) represent the length of the shortest common
    supersequence of s1[:i] and s2[:j].

    Cases:
        1. If either string is empty:
           The answer is the length of the other string.

        2. If the current characters are equal:
           We only need to include that character once.
               solve(i, j) = 1 + solve(i - 1, j - 1)

        3. If the current characters are different:
           We can include either s1[i - 1] or s2[j - 1].
           Choose the option producing the shorter supersequence.
               solve(i, j) = 1 + min(
                   solve(i - 1, j),
                   solve(i, j - 1)
               )

    Memoization stores the result of each (i, j) state to avoid
    recalculating overlapping subproblems.

Time Complexity:
    O(n × m)

Space Complexity:
    O(n × m) for the memoization table
    + O(n + m) recursion stack in the worst case.
"""

def scs(s1, s2):
    n = len(s1)
    m = len(s2)
    memo = [[-1] * (m + 1) for _ in range(n + 1)]

    def solve(i, j):
        if i == 0:
            return j

        if j == 0:
            return i
    
        if memo[i][j] != -1:
            return memo[i][j]

        if s1[i - 1] == s2[j - 1]:
            memo[i][j] = 1 + solve(i - 1, j - 1)
        else:
            memo[i][j] = 1 + min(solve(i - 1, j), solve(i, j - 1))

        return memo[i][j]

    return solve(n, m)