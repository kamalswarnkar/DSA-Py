"""
Rope Cutting using Recursion

Problem:
    Given a rope of length n and three possible cut lengths a, b, and c,
    maximize the number of pieces into which the rope can be divided.

    Return -1 if it is impossible to cut the rope completely.

Approach:
    Recursion

Recursive Idea:
    For every remaining rope length, try all three possible cuts:

        1. Cut length `a`
        2. Cut length `b`
        3. Cut length `c`

    Choose the option that produces the maximum number of pieces.

Base Cases:
    • n == 0 → rope has been completely cut, return 0.
    • n < 0  → invalid cut, return -1.

Recurrence:
    f(n) = 1 + max(
        f(n - a),
        f(n - b),
        f(n - c)
    )

Time Complexity:
    O(3^N)

    Each recursive call can generate up to 3 further calls,
    producing an exponential recursion tree.

Space Complexity:
    O(N)

    The maximum recursion depth is O(N).

where,
    N = initial rope length
"""

def maxPieces(n, a, b, c):
    if n == 0:
        return 0

    if n < 0:
        return -1

    res = max(maxPieces(n - a, a, b, c),
              maxPieces(n - b, a, b, c),
              maxPieces(n - c, a, b, c))

    if res == -1:
        return res

    return res + 1
