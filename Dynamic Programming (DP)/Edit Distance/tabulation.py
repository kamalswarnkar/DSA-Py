"""
Edit Distance using Tabulation

Problem:
    Given two strings s1 and s2, find the minimum number of
    operations required to convert s1 into s2.

    Allowed operations:
        • Insert
        • Delete
        • Replace

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[i][j]` represents:

        Minimum number of operations required to convert
        s1[0:i] into s2[0:j]

    For every pair of characters:

        1. If they are equal:
           No operation is required.

        2. If they are different:
           Try:
               • Insert
               • Delete
               • Replace

           and choose the operation with minimum cost.

Base Cases:
    • dp[i][0] = i
      Convert a string of length i into an empty string
      by deleting all i characters.

    • dp[0][j] = j
      Convert an empty string into a string of length j
      by inserting all j characters.

Time Complexity:
    O(N × M)

    Every cell of the DP table is calculated exactly once.

Space Complexity:
    O(N × M)

    The DP table contains (N + 1) × (M + 1) states.

where,
    N = length of s1
    M = length of s2
"""

def eD(s1, s2):
    n = len(s1)
    m = len(s2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        dp[i][0] = i

    for j in range(m + 1):
        dp[0][j] = j

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                insert = dp[i][j - 1] # Insert: match s1[i-1] with s2[j-1] by inserting s2[j-1]
                delete = dp[i - 1][j] # Delete: remove s1[i-1]
                replace = dp[i - 1][j - 1] # Replace: replace s1[i-1] with s2[j-1]

                dp[i][j] = 1 + min(insert, delete, replace)

    return dp[n][m]