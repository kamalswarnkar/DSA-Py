"""
Fibonacci Using Tabulation (Bottom-Up Dynamic Programming)

Problem:
    Calculate the nth Fibonacci number using Dynamic Programming.

    Fibonacci sequence:
        F(0) = 0
        F(1) = 1

        F(n) = F(n-1) + F(n-2)

Approach:
    Tabulation (Bottom-Up)

Idea:
    Instead of solving the problem recursively, solve all smaller
    subproblems first and use their results to build the answer.

    The DP table stores:

        dp[i] = Fibonacci number at position i

Steps:
    1. Create a DP table of size n + 1.
    2. Initialize the base cases:
           dp[0] = 0
           dp[1] = 1
    3. Starting from i = 2, calculate each Fibonacci number using:
           dp[i] = dp[i-1] + dp[i-2]
    4. Return dp[n].

Time Complexity:
    O(N)

    Each Fibonacci value is calculated exactly once.

Space Complexity:
    O(N)

    The DP table stores N + 1 Fibonacci values.

where,
N = nth Fibonacci number

Key Idea:
    Tabulation = Bottom-Up = Iteration + DP Table

    Start with the smallest subproblems and gradually build the
    solution to the original problem.
"""

def fib(n):
    dp = [None] * (n + 1)

    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]