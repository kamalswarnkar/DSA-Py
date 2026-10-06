"""
Problem: Count Ways with 3 Moves

Description:
    A child can climb either 1, 2, or 3 stairs at a time.
    Find the number of distinct ways to reach the nth stair.

Approach:
    To reach stair i, the child can come from:
        i - 1  -> by taking 1 step
        i - 2  -> by taking 2 steps
        i - 3  -> by taking 3 steps

    Therefore:
        ways(i) = ways(i - 1) + ways(i - 2) + ways(i - 3)

    Memoization stores the result of each subproblem so that
    already solved subproblems are not calculated again.

Base Cases:
    ways(0) = 1
    ways(1) = 1
    ways(2) = 2

Complexity:
    Time  : O(n)
        Each subproblem from 0 to n is calculated at most once.

    Space : O(n)
        O(n) for the memoization array and O(n) for the
        recursive call stack in the worst case.
"""

def countWays(n):
    memo = [-1] * (n + 1)

    def solve(i):
        if i == 0 or i == 1:
            memo[i] = 1
            return memo[i]

        if memo[i] == 2:
            memo[i] = 2
            return memo[i]
        
        if memo[i] != -1:
            return memo[i]

        memo[i] = solve(i - 1) + solve(i - 2) + solve(i - 3)

        return memo[i]

    return solve(n)