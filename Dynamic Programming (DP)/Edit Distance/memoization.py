"""
Edit Distance using Memoization

Problem:
    Given two strings s1 and s2, find the minimum number of
    operations required to convert s1 into s2.

    Allowed operations:
        • Insert
        • Delete
        • Replace

Approach:
    Memoization (Top-Down Dynamic Programming)

    We use the same recursive recurrence as the recursive
    solution, but store the result of every subproblem.

    `memo[i][j]` represents:

        Minimum operations required to convert
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
    • i == 0 → insert all j remaining characters.
    • j == 0 → delete all i remaining characters.

Time Complexity:
    O(N × M)

    There are (N + 1) × (M + 1) possible states,
    and each state is solved only once.

Space Complexity:
    O(N × M)

    For the memoization table.

    Additionally, O(N + M) recursion-stack space is used.

where,
    N = length of s1
    M = length of s2
"""

def eD(s1, s2):
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
            memo[i][j] =  solve(i - 1, j - 1)
        else:
            insert = solve(i, j - 1) # Insert: match s1[i-1] with s2[j-1] by inserting s2[j-1]
            delete = solve(i - 1, j) # Delete: remove s1[i-1]
            replace = solve(i - 1, j - 1) # Replace: replace s1[i-1] with s2[j-1]

            memo[i][j] = 1 + min(insert, delete, replace)

        return memo[i][j]

    return solve(n, m)