"""
Optimal Game Strategy using Memoization

Problem:
    Given an array of coins, two players alternately pick either
    the first or last coin from the remaining array.

    Both players play optimally.

    Find the maximum value the first player can collect.

Approach:
    Memoization (Top-Down Dynamic Programming)

    memo[i][j] represents the maximum value the current player
    can collect from the subarray arr[i...j].

    At every state, the current player has two choices:

        1. Pick arr[i]
        2. Pick arr[j]

    After our choice, the opponent plays optimally.
    Therefore, the opponent will leave us with the worse of
    the two possible remaining outcomes.

    Hence:

        Pick first:
            arr[i] + min(
                solve(i + 2, j),
                solve(i + 1, j - 1)
            )

        Pick last:
            arr[j] + min(
                solve(i + 1, j - 1),
                solve(i, j - 2)
            )

    Finally, we choose the better of these two options.

Base Cases:
    • i > j → no coins remain → 0
    • i == j → one coin remains → arr[i]
    • i + 1 == j → two coins remain → max(arr[i], arr[j])

Time Complexity:
    O(N²)

    There are O(N²) possible (i, j) states and each state
    requires O(1) work.

Space Complexity:
    O(N²)

    O(N²) for the memoization table and O(N) recursion stack.

where,
    N = number of coins
"""


def maxVal(arr):
    n = len(arr)

    if n == 0:
        return 0

    if n == 1:
        return arr[0]

    memo = [[-1] * n for _ in range(n)]

    def solve(i, j):
        if i > j:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        if i == j:
            memo[i][j] = arr[i]
            return memo[i][j]

        if i + 1 == j:
            memo[i][j] = max(arr[i], arr[j])
        else:
            pick_first = arr[i] + min(solve(i + 2, j), solve(i + 1, j - 1))
            pick_last = arr[j] + min(solve(i + 1, j - 1), solve(i, j - 2))
            memo[i][j] = max(pick_first, pick_last)

        return memo[i][j]

    return solve(0, n - 1)
        