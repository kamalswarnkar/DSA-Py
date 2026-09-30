"""
Egg Dropping Puzzle using Tabulation

Problem:
    Given `f` floors and `e` eggs, determine the minimum number
    of trials required in the worst case to find the critical
    floor from which an egg will break.

Approach:
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[i][j]` represents:

        Minimum number of trials required for
        `i` floors and `j` eggs.

    For every possible floor `x`, there are two outcomes:

        1. Egg breaks:
               dp[x - 1][j - 1]

           We need to check the floors below `x`,
           and one egg is lost.

        2. Egg does not break:
               dp[i - x][j]

           We need to check the floors above `x`,
           and the number of eggs remains unchanged.

    Since either outcome can occur, we consider the
    worst case:

        max(break_case, no_break_case)

    We try every possible dropping floor and choose the
    floor that minimizes the worst-case number of trials.

    Recurrence:

        dp[i][j] =
            1 + min(
                max(
                    dp[x - 1][j - 1],
                    dp[i - x][j]
                )
            )

    Base Cases:
        • 0 floors → 0 trials
        • 1 floor  → 1 trial
        • 1 egg    → i trials

Time Complexity:
    O(F² × E)

    There are O(F × E) DP states, and for each state
    we try all possible F dropping floors.

Space Complexity:
    O(F × E)

    The DP table contains (F + 1) × (E + 1) states.

where,
    F = number of floors
    E = number of eggs
"""

def minTrials(f, e): 
    if f == 0 or f == 1 or e == 1:
        return f

    dp = [[-1] * (e + 1) for _ in range(f + 1)]

    for i in range(1, e + 1):
        dp[0][i] = 0
        dp[1][i] = 1

    for i in range(2, f + 1):
        dp[i][1] = i

    for i in range(2, f + 1):
        for j in range(2, e + 1):
            dp[i][j] = float("inf")

            for x in range(1, i + 1):
                do_break = dp[x - 1][j - 1]
                donot_break = dp[i - x][j]

                worst_case = 1 + max(do_break, donot_break)

                dp[i][j] = min(dp[i][j], worst_case)

    return dp[f][e]