"""
Egg Dropping Puzzle using Memoization

Problem:
    Given `floor` floors and `egg` eggs, determine the minimum
    number of trials required in the worst case to find the
    critical floor from which an egg will break.

Approach:
    Memoization (Top-Down Dynamic Programming)

    `memo[f][e]` represents:

        Minimum number of trials required for
        `f` floors and `e` eggs.

    For every possible floor `x`, we have two possibilities:

        1. Egg breaks:
               solve(x - 1, e - 1)

           We only need to check the floors below `x`,
           and one egg is lost.

        2. Egg does not break:
               solve(f - x, e)

           We only need to check the floors above `x`,
           and the number of eggs remains unchanged.

    Since either case can occur, we consider the worst case:

        max(break_case, no_break_case)

    We try every possible floor and choose the floor that
    minimizes this worst-case result.

    Therefore:

        solve(f, e) =
            1 + min(
                max(
                    solve(x - 1, e - 1),
                    solve(f - x, e)
                )
            )

Base Cases:
    • 0 floors → 0 trials
    • 1 floor  → 1 trial
    • 1 egg    → f trials

Time Complexity:
    O(F² × E)

    There are O(F × E) unique states.
    For every state, we try all F possible dropping floors.

Space Complexity:
    O(F × E)

    The memoization table stores F × E states.

    Additionally, O(F) recursion-stack space is used.

where,
    F = number of floors
    E = number of eggs
"""

def minTrials(floor, egg):
    if floor == 0 or floor == 1 or egg == 1:
        return floor

    memo = [[-1] * (egg + 1) for _ in range(floor + 1)]

    def solve(f, e):
        if f == 0 or f == 1 or e == 1:
            memo[f][e] = f
            return memo[f][e]

        if memo[f][e] != -1:
            return memo[f][e]

        res = float("inf")

        for x in range(1, f + 1):
            do_break = solve(x - 1, e - 1)
            donot_break = solve(f - x, e)

            worst_case = max(do_break, donot_break)

            res = min(res, worst_case)

        memo[f][e] = res + 1

        return memo[f][e]

    return solve(floor, egg)

        