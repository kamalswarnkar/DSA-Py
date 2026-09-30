"""
Optimal Game Strategy using Recursion

Problem:
    Given an array of coins, two players play a game where each player
    can pick only the first or last coin from the remaining array.

    Both players play optimally.

    Find the maximum value that the first player can collect.

Approach:
    Recursion

    There are two ways for the current player to make a move:

        1. Pick the first coin.
        2. Pick the last coin.

    After making a choice, the opponent also plays optimally.
    Therefore, we consider the opponent's best possible response and
    choose the move that maximizes the current player's final score.

Method 1:
    Total-Sum Formulation

    `s` represents the total value of coins currently remaining.

    If we pick arr[i], the opponent can obtain the maximum value from
    the remaining range. Therefore, our final value is:

        s - opponent's maximum value

Method 2:
    Direct Recurrence

    If we pick the first coin `arr[i]`, the opponent can choose either:

        • arr[i + 1]
        • arr[j]

    Therefore, the remaining game value for us is the minimum of:

        solve(i + 2, j)
        solve(i + 1, j - 1)

    Similarly, if we pick the last coin `arr[j]`, the opponent can choose
    either:

        • arr[i]
        • arr[j - 1]

    Therefore:

        arr[j] + min(
            solve(i + 1, j - 1),
            solve(i, j - 2)
        )

Base Case:
    If only two coins remain, the current player simply picks the
    larger coin.

Time Complexity:
    O(2^N)

    Each recursive call can branch into two further subproblems.

Space Complexity:
    O(N)

    The maximum recursion depth is O(N).

where,
    N = number of coins

Note:
    Both methods produce the same result but use different
    formulations of the recurrence.
"""

def mVRec_I(arr, i, j, s):
    if i + 1 == j:
        return max(arr[i], arr[j])

    return max(s - mVRec_I(arr, i + 1, j, s - arr[i]),
               s - mVRec_I(arr, i, j - 1, s - arr[j]))

def mVRec_II(arr, i, j):
    if i + 1 == j:
        return max(arr[i], arr[j])

    return max(min(mVRec_II(arr, i + 2, j), mVRec_II(arr, i + 1, j - 1)) + arr[i],
               min(mVRec_II(arr, i + 1, j - 1), mVRec_II(arr, i, j - 2)) + arr[j])
