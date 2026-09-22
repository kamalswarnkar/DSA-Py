"""
Edit Distance using Tabulation
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