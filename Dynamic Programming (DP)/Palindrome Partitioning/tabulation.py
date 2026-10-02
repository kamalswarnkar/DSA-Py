"""
Palindrome Partitioning using Tabulation

Problem:
    Given a string `s`, find the minimum number of cuts required
    to partition the string such that every resulting substring
    is a palindrome.

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[i][j]` represents:

        Minimum number of cuts required to partition
        the substring s[i:j+1] into palindromic substrings.

    If s[i:j+1] is already a palindrome:

        dp[i][j] = 0

    Otherwise, try every possible partition point `k`:

        s[i ... k] | s[k + 1 ... j]

    One cut is required between the two parts:

        dp[i][j] =
            min(
                1 + dp[i][k] + dp[k + 1][j]
            )

    The table is filled using increasing substring length
    (`gap`) so that all smaller subproblems are already solved.

Base Cases:
    • gap = 0 → single character → 0 cuts.
    • A palindrome substring → 0 cuts.

Time Complexity:
    O(N³)

    There are O(N²) possible substring intervals.
    For each non-palindromic interval, we try O(N)
    partition points.

    Palindrome checking also takes O(N).

Space Complexity:
    O(N²)

    The DP table requires O(N²) space.

where,
    N = length of the string
"""

def isPalindrome(s, start, end):
    i, j = start, end

    while i < j:
        if s[i] != s[j]:
            return False

        i += 1
        j -= 1

    return True

def palPart(s):
    n = len(s)

    if n <= 1:
        return 0

    dp = [[0] * n for _ in range(n)]

    for gap in range(1, n):
        for i in range(n - gap):
            j = i + gap

            if isPalindrome(s, i, j):
                dp[i][j] = 0
            else:
                dp[i][j] = float('inf')

                for k in range(i, j):
                    left = dp[i][k]
                    right = dp[k + 1][j]

                    dp[i][j] = min(dp[i][j], 1 + left + right)

    return dp[0][n - 1]