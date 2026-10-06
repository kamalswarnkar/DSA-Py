"""
Problem: Ways to Reach the Nth Stair

Description:
    A person can climb either 1 stair or 2 stairs at a time.
    Find the number of distinct ways to reach the nth stair.

    Order does not matter, which means different permutations
    of the same set of steps are considered the same.

Approach:
    Since the order of steps does not matter, we only need to
    determine how many 2-step moves can be used.

    If we use k two-step moves, the remaining stairs can be
    covered using one-step moves.

    The number of possible values of k is:

        k = 0, 1, 2, ..., floor(n / 2)

    Therefore, the total number of ways is:

        ways(n) = floor(n / 2) + 1

Example:
    n = 4

    Possible combinations:
        1 + 1 + 1 + 1
        1 + 1 + 2
        2 + 2

    Answer = 3

Complexity:
    Time  : O(1)
        The answer is calculated directly using a mathematical
        formula.

    Space : O(1)
        No additional data structures are required.
"""

def countWays(n):
    return (n // 2) + 1