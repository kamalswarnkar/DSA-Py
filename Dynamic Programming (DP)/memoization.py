"""
Fibonacci Using Memoization (Top-Down Dynamic Programming)

Problem:
    Calculate the nth Fibonacci number using Dynamic Programming.

    Fibonacci sequence:
        F(0) = 0
        F(1) = 1

        F(n) = F(n-1) + F(n-2)

Approach:
    Memoization (Top-Down)

Idea:
    The normal recursive Fibonacci solution repeatedly calculates
    the same subproblems.

    For example:

        fib(5)
        ├── fib(4)
        │   ├── fib(3)
        │   └── fib(2)
        └── fib(3)   ← already calculated

    Memoization solves this problem by storing the result of every
    subproblem after calculating it.

    When the same subproblem is needed again, its stored result
    is returned instead of calculating it again.

Steps:
    1. Create a memo array to store previously calculated results.
    2. Check whether fib(n) has already been calculated.
    3. If yes, return the stored result.
    4. If n is 0 or 1, return n.
    5. Otherwise, recursively calculate fib(n-1) and fib(n-2).
    6. Store the result in the memo array.
    7. Return the stored result.

Time Complexity:
    O(N)

    Each Fibonacci value from 0 to N is calculated only once.

Space Complexity:
    O(N)

    O(N) space is used for:
        • Memoization array
        • Recursion call stack

where,
N = nth Fibonacci number

Key Idea:
    Memoization = Recursion + Storage

    Solve the problem recursively, but store the result of each
    subproblem so that it is not solved again.
"""

memo = [None] * 100

def fib(n):
    if memo[n] != None:
        return memo[n]
    if n == 0 or n == 1:
        memo[n] = n
    else:
        memo[n] = fib(n - 1) + fib(n - 2)

    return memo[n]