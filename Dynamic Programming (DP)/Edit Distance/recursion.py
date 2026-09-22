"""
Edit Distance using Recursion

Problem:
    Given two strings s1 and s2, find the minimum number of
    operations required to convert s1 into s2.

    Allowed operations:
        • Insert
        • Delete
        • Replace

Approach:
    Recursion

    For every pair of characters:

        1. If the characters are equal:
           No operation is required.
           Move to the previous characters of both strings.

        2. If the characters are different, try all three
           possible operations:

               Insert  → eD(s1, s2, n, m - 1)
               Delete  → eD(s1, s2, n - 1, m)
               Replace → eD(s1, s2, n - 1, m - 1)

           Take the operation requiring the minimum cost.

Base Cases:
    • n == 0 → insert all remaining `m` characters.
    • m == 0 → delete all remaining `n` characters.

Time Complexity:
    O(3^(N + M))

    Each state can branch into three recursive calls.

Space Complexity:
    O(N + M)

    Due to the recursion stack.

where,
    N = length of s1
    M = length of s2
"""

def eD(s1, s2, n, m):
    if n == 0:
        return m

    if m == 0:
        return n

    if s1[n - 1] == s2[m - 1]:
        return eD(s1, s2, n - 1, m - 1)
    else:
        return 1 + min(eD(s1, s2, n, m - 1), eD(s1, s2, n - 1, m), eD(s1, s2, n - 1, m - 1))

    