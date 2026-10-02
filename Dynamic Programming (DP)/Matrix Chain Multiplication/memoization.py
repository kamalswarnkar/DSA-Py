"""
Matrix Chain Multiplication using Memoization

Problem:
    Given an array `arr` representing the dimensions of a chain
    of matrices, find the minimum number of scalar multiplications
    required to multiply all matrices.

    If:

        arr = [p0, p1, p2, ..., pN]

    then the matrices are:

        A1 = p0 × p1
        A2 = p1 × p2
        ...
        AN = p(N-1) × pN

Approach:
    Memoization (Top-Down Dynamic Programming)

    `memo[i][j]` represents:

        Minimum multiplication cost required to multiply
        the matrix chain from index `i` to `j - 1`.

    For every possible partition `k`:

        Left  = solve(i, k)
        Right = solve(k, j)

    The cost of multiplying the two resulting matrices is:

        arr[i] × arr[k] × arr[j]

    Therefore:

        solve(i, j) =
            min(
                solve(i, k)
                + solve(k, j)
                + arr[i] × arr[k] × arr[j]
            )

        for every i < k < j.

Base Case:
    If only one matrix remains:

        i + 1 == j → 0

    because no multiplication is required.

Time Complexity:
    O(N³)

    There are O(N²) possible subproblems,
    and each subproblem tries O(N) partition points.

Space Complexity:
    O(N²)

    O(N²) space is required for the memoization table.

    Additionally, O(N) recursion-stack space is used.

where,
    N = len(arr)
"""

def matChain(arr):
    n = len(arr)

    if n <= 2:
        return 0

    memo = [[-1] * n for _ in range(n)]

    def solve(i, j):
        if i + 1 == j:
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        res = float('inf')

        for k in range(i + 1, j):
            left = solve(i, k)
            right = solve(k, j)
            cost = arr[i] * arr[k] * arr[j]

            res = min(res, left + right + cost)

        memo[i][j] = res

        return memo[i][j]

    return solve(0, n - 1)