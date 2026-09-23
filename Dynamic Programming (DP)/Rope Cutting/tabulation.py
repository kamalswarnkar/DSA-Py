"""
Rope Cutting using Tabulation

Problem:
    Given a rope of length n and three possible cut lengths a, b, and c,
    maximize the number of pieces into which the rope can be divided.

    Return -1 if it is impossible to cut the rope completely.

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[i]` represents the maximum number of pieces that can be obtained
    by completely cutting a rope of length `i`.

    For every rope length `i`, try all three possible cuts:

        1. Cut length `a`
        2. Cut length `b`
        3. Cut length `c`

    If a cut is possible, use the previously calculated result for
    the remaining rope length.

Base Cases:
    • dp[0] = 0 → a rope of length 0 requires 0 pieces.
    • dp[i] = -1 → length `i` cannot be formed using the given cuts.

Recurrence:
    dp[i] = 1 + max(
        dp[i - a],
        dp[i - b],
        dp[i - c]
    )

    Only consider a state if the corresponding previous state
    is not -1.

Time Complexity:
    O(N)

    We calculate each of the N rope-length states once, and each
    state checks at most 3 possible cuts.

Space Complexity:
    O(N)

    The tabulation array stores the result for every rope length.

where,
    N = initial rope length
"""


def maxPieces(n, a, b, c):
    dp = [-1] * (n + 1)

    dp[0] = 0

    for i in range(1, n + 1):
        if i >= a:
            dp[i] = dp[i - a]
        if i >= b:
            dp[i] = max(dp[i], dp[i - b])
        if i >= c:
            dp[i] = max(dp[i], dp[i - c])
        if dp[i] != -1:
            dp[i] += 1

    return dp[n]