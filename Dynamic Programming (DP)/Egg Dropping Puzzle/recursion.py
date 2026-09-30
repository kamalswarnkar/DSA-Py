"""
Egg Dropping Puzzle using Recursion

Problem:
    Given `f` floors and `e` eggs, determine the minimum number
    of trials required in the worst case to find the critical
    floor from which an egg will break.

Approach:
    Recursion

    Try dropping an egg from every possible floor `x`.

    For each floor:

        1. Egg breaks:
           We only need to check the floors below `x`.

               minTrial(x - 1, e - 1)

        2. Egg does not break:
           We only need to check the floors above `x`.

               minTrial(f - x, e)

    Since either case can happen, we consider the worst case:

        max(break_case, no_break_case)

    We try every possible floor and choose the floor that
    minimizes this worst-case number of trials.

    Therefore:

        minTrial(f, e) =
            1 + min(
                max(
                    minTrial(x - 1, e - 1),
                    minTrial(f - x, e)
                )
            )

Base Cases:
    • 0 floors → 0 trials
    • 1 floor  → 1 trial
    • 1 egg    → f trials

Time Complexity:
    O(2^F)

    The recursive solution generates a large number of
    overlapping subproblems.

Space Complexity:
    O(F)

    The maximum recursion depth can be O(F).

where,
    F = number of floors
    E = number of eggs
"""

def minTrial(f, e):

    if f == 0 or f == 1 or e == 1:
        return f

    res = float("inf")

    for x in range(1, f + 1):
        do_break = minTrial(x - 1, e - 1)
        donot_break = minTrial(f - x, e)

        worst_case = max(do_break, donot_break)

        res = min(res, worst_case)

    return res + 1