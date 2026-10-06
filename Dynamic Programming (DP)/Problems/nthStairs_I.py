"""
Problem: Ways to Reach the Nth Stair

Description:
    A person can climb either 1 stair or 2 stairs at a time.
    Find the number of distinct ways to reach the nth stair.

Approach:
    To reach stair i, the person can:
        1. Take 1 step from stair i - 1.
        2. Take 2 steps from stair i - 2.

    Therefore:
        ways(i) = ways(i - 1) + ways(i - 2)

    Memoization stores the result of each subproblem so that
    the same subproblem is not solved repeatedly.

Base Cases:
    ways(0) = 1
    ways(1) = 1

Complexity:
    Time  : O(n)
        Each stair from 0 to n is calculated at most once.

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
        
        if memo[i] != -1:
            return memo[i]

        memo[i] = solve(i - 1) + solve(i - 2)

        return memo[i]

    return solve(n)