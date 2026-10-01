"""
Count Total BSTs with N Keys using Tabulation

Problem:
    Given N distinct keys, count the total number of
    structurally different Binary Search Trees (BSTs)
    that can be formed using all N keys.

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[i]` represents:

        Number of structurally different BSTs
        that can be formed using `i` keys.

    For every possible root `j`:

        • `j` keys form the left subtree.
        • `i - j - 1` keys form the right subtree.

    Therefore:

        dp[i] =
            Σ dp[j] * dp[i - j - 1]

    The table is filled from smaller numbers of keys
    to larger numbers of keys.

Base Cases:
    • 0 keys → 1 BST
    • 1 key  → 1 BST

Time Complexity:
    O(N²)

    There are N DP states, and each state tries
    all possible root positions.

Space Complexity:
    O(N)

    The DP array stores the result for every
    number of keys.

where,
    N = number of keys
"""

def countWays(n):
    if n == 0 or n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0], dp[1] = 1, 1

    for i in range(2, n + 1):
        for j in range(i):
            dp[i] += dp[j] * dp[i - j - 1]

    return dp[n]