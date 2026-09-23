"""
Rope Cutting using Memoization

Problem:
    Given a rope of length n and three possible cut lengths a, b, and c,
    maximize the number of pieces into which the rope can be divided.

    Return -1 if it is impossible to cut the rope completely.

Approach:
    Memoization (Top-Down Dynamic Programming)

    `memo[length]` stores the maximum number of pieces that can be
    obtained from a rope of the given `length`.

    For every rope length, try all three possible cuts:

        1. Cut length `a`
        2. Cut length `b`
        3. Cut length `c`

    Store the result so that the same rope length is never solved again.

Base Cases:
    • length == 0 → rope has been completely cut, return 0.
    • length < 0  → invalid cut, return -1.

Recurrence:
    f(length) = 1 + max(
        f(length - a),
        f(length - b),
        f(length - c)
    )

Time Complexity:
    O(N)

    There are N + 1 possible rope-length states.
    Each state performs at most 3 recursive calls.

Space Complexity:
    O(N)

    O(N) space for the memoization array and O(N) recursion
    stack in the worst case.

where,
    N = initial rope length
"""

def maxPieces(n, a, b, c):
    memo = [-1] * (n + 1)

    def solve(length):
        if length == 0:
            return 0

        if length < 0:
            return -1

        if memo[length] != -1:
            return memo[length]

        piece_a = solve(length - a)
        piece_b = solve(length - b)
        piece_c = solve(length - c)

        max_piece = max(piece_a, piece_b, piece_c)

        if max_piece == -1:
            memo[length]  = -1
        else:
            memo[length] = max_piece + 1

        return memo[length]

    return solve(n)