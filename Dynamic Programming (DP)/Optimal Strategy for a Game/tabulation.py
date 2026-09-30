"""
Optimal Game Strategy using Tabulation

Problem:
    Given an array of coins, two players alternately pick either
    the first or last coin from the remaining array.

    Both players play optimally.

    Find the maximum value that the first player can collect.

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[i][j]` represents the maximum value the current player
    can collect from the subarray arr[i...j].

    At every state, the current player has two choices:

        1. Pick arr[i]
        2. Pick arr[j]

    After our choice, the opponent plays optimally and leaves us
    with the worse of the possible remaining outcomes.

    Therefore:

        Pick first:
            arr[i] + min(
                dp[i + 2][j],
                dp[i + 1][j - 1]
            )

        Pick last:
            arr[j] + min(
                dp[i + 1][j - 1],
                dp[i][j - 2]
            )

    We then choose the better of these two choices.

Base Cases:
    • gap = 0 → one coin remains.
    • gap = 1 → two coins remain.

    All larger gaps are calculated using previously computed
    smaller gaps.

Time Complexity:
    O(N²)

    There are O(N²) subarray states, and each state requires
    O(1) work.

Space Complexity:
    O(N²)

    The 2D DP table requires O(N²) space.

where,
    N = number of coins
"""


def maxVal(arr):
    n = len(arr)

    if n == 0:
        return 0

    if n == 1:
        return arr[0]
    
    dp = [[-1] * n for _ in range(n)]

    for i in range(n): # gap = 0
        dp[i][i] = arr[i]

    for i in range(n - 1): # gap = 1
        dp[i][i + 1] = max(arr[i], arr[i + 1])

    for gap in range(2, n): # gap >= 2
        for i in range(n - gap):
            j = i + gap

            pick_first = arr[i] + min(dp[i + 2][j], dp[i + 1][j - 1])
            pick_last = arr[j] + min(dp[i + 1][j - 1], dp[i][j - 2])

            dp[i][j] = max(pick_first, pick_last)

    return dp[0][n - 1]