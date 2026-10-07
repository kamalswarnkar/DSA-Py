"""
Egg Dropping Puzzle using Optimized Binary Search

Problem:
    Given `floor` floors and `eggs` eggs, determine the minimum
    number of trials required to find the highest floor from
    which an egg can be dropped without breaking.

    Rules:
        • If an egg breaks, it cannot be used again.
        • If an egg does not break, it can be reused.
        • The goal is to guarantee finding the critical floor
          using the minimum number of trials.

Approach:
    Memoization + Binary Search

    `memo[f][e]` represents:

        Minimum number of trials required for `f` floors
        and `e` eggs.

    If we drop an egg from floor `mid`, there are two possible
    outcomes:

        1. Egg breaks:
               We only need to consider floors below `mid`.

               solve(mid - 1, e - 1)

        2. Egg does not break:
               We need to consider floors above `mid`.

               solve(f - mid, e)

    Since we need to guarantee the answer in the worst case:

        worst_case =
            1 + max(do_break, donot_break)

    We choose the floor that minimizes this worst-case value.

    Binary Search Optimization:
        As the dropping floor increases:

            do_break decreases
            donot_break increases

        Therefore, the maximum of the two follows a
        unimodal pattern, allowing binary search to locate
        the optimal partition instead of checking every floor.

Time Complexity:
    O(E × F × log F)

    There are O(E × F) DP states, and each state performs
    O(log F) binary-search iterations.

Space Complexity:
    O(E × F)

    The memoization table requires (F + 1) × (E + 1) space.

    Additionally, O(F) recursion-stack space may be used.

where,
    F = number of floors
    E = number of eggs
"""

def minTrials(floor, eggs):
    if floor == 0 or floor == 1 or eggs == 1:
        return floor

    memo = [[-1] * (eggs + 1) for _ in range(floor + 1)]

    def solve(f, e):
        if f <= 1 or e == 1:
            memo[f][e] = f
            return memo[f][e]

        if memo[f][e] != -1:
            return memo[f][e]

        low, high = 1, f
        res = float('inf')

        while low <= high:
            mid = (low + high) // 2

            do_break = solve(mid - 1, e - 1)
            donot_break = solve(f- mid, e)

            worst_case = 1 + max(do_break, donot_break)

            res = min(res, worst_case)

            if do_break < donot_break:
                low = mid + 1
            else:
                high = mid - 1

        memo[f][e] = res

        return memo[f][e]

    return solve(floor, eggs)