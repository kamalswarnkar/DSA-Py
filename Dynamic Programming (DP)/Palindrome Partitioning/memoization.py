"""
Palindrome Partitioning using Memoization

Problem:
    Given a string `s`, partition it into substrings such that
    every substring is a palindrome.

    Find the minimum number of cuts required to obtain
    such a palindrome partition.

Approach:
    Memoization (Top-Down Dynamic Programming)

    `memo[i][j]` represents:

        Minimum number of cuts required to partition
        the substring s[i:j+1] into palindromic substrings.

    For every possible partition point `k`:

        s[i ... k] | s[k + 1 ... j]

    We make one cut between the two parts and recursively
    solve both resulting substrings.

    Therefore:

        solve(i, j) =
            min(
                1 + solve(i, k) + solve(k + 1, j)
            )

        for every i <= k < j.

    However, if s[i:j+1] is already a palindrome:

        solve(i, j) = 0

    because no cut is required.

Base Cases:
    • A substring that is already a palindrome requires 0 cuts.
    • A single character is always a palindrome.

Time Complexity:
    O(N³)

    There are O(N²) possible (i, j) states.
    For each state, we try O(N) partition points.

    Additionally, checking whether a substring is a palindrome
    takes O(N), but the overall straightforward memoized
    implementation remains O(N³) when considering the
    partitioning work and palindrome checks.

Space Complexity:
    O(N²)

    O(N²) space is required for the memoization table.

    Additionally, O(N) recursion-stack space is used.

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

    memo = [[-1] * n for _ in range(n)]

    def solve(i, j):
        if i + 1 == j:
            memo[i][j] = 0
            return memo[i][j]
        
        if memo[i][j] != -1:
            return memo[i][j]

        if isPalindrome(s, i, j):
            memo[i][j] = 0
            return memo[i][j]

        res = float('inf')

        for k in range(i, j):
            left = solve(i, k)
            right = solve(k + 1, j)

            res = min(res, 1 + left + right)

        memo[i][j] = res
        return memo[i][j]

    return solve(0, n - 1)