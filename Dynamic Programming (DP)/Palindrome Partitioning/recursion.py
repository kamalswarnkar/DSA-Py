"""
Palindrome Partitioning using Recursion

Problem:
    Given a string `s`, partition it into substrings such that
    every substring is a palindrome.

    Find the minimum number of cuts required to obtain
    such a palindrome partition.

Approach:
    Recursion / Divide and Conquer

    `palPart(s, i, j)` represents:

        Minimum number of cuts required to partition
        the substring s[i:j+1] into palindromic substrings.

    If s[i:j+1] is already a palindrome, no cut is required.

    Otherwise, try every possible partition point `k`:

        s[i ... k] | s[k+1 ... j]

    The total cuts are:

        1 + palPart(s, i, k) + palPart(s, k + 1, j)

    The `1` represents the cut between the two partitions.

Base Cases:
    • If s[i:j+1] is already a palindrome → 0 cuts.
    • A single character is always a palindrome.

Time Complexity:
    O(N × 2^N)

    There are exponentially many recursive partitions,
    and checking whether a substring is a palindrome takes O(N).

Space Complexity:
    O(N)

    The maximum recursion depth is O(N).

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

def palPart(s, i, j):
    if isPalindrome(s, i, j):
        return 0

    res = float('inf')

    for k in range(i, j):
        res = min(res, 1 + palPart(s, i, k) + palPart(s, k + 1, j))

    return res

def minCuts(s):
    n = len(s)

    if n <= 1:
        return 0

    return palPart(s, 0, n - 1)