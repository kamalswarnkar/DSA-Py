"""
Count Total BSTs with N Keys using Memoization

Problem:
    Given N distinct keys, count the total number of
    structurally different Binary Search Trees (BSTs)
    that can be formed using all N keys.

Approach:
    Memoization (Top-Down Dynamic Programming)

    `memo[i]` represents:

        Number of structurally different BSTs
        that can be formed using `i` keys.

    For every possible root `j`:

        • `j` keys form the left subtree.
        • `i - j - 1` keys form the right subtree.

    Therefore:

        solve(i) =
            Σ solve(j) * solve(i - j - 1)

    The result of every subproblem is stored in `memo`
    so that overlapping subproblems are solved only once.

Base Cases:
    • 0 keys → 1 BST
    • 1 key  → 1 BST

Time Complexity:
    O(N²)

    There are O(N) unique states, and each state
    tries up to O(N) possible roots.

Space Complexity:
    O(N)

    O(N) space is required for the memoization array,
    along with O(N) recursion-stack space.

where,
    N = number of keys
"""


def countWays(n):
    if n == 0 or n == 1:
        return 1

    memo = [-1] * (n + 1)

    def solve(i):
        if i == 0 or i == 1:
            return 1

        if memo[i] != -1:
            return memo[i]

        res = 0

        for j in range(i):
            res += solve(j) * solve(i - j - 1)
        
        memo[i] = res

        return memo[i]

    return solve(n)