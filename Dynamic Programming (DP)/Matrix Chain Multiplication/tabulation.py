"""
Matrix Chain Multiplication using Tabulation

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
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[i][j]` represents:

        Minimum multiplication cost required to multiply
        the matrix chain from index `i` to `j - 1`.

    For every interval [i, j], try every possible partition `k`.

        Left  = dp[i][k]
        Right = dp[k][j]

    Cost of multiplying the two resulting matrices:

        arr[i] × arr[k] × arr[j]

    Therefore:

        dp[i][j] =
            min(
                dp[i][k]
                + dp[k][j]
                + arr[i] × arr[k] × arr[j]
            )

    The table is filled by increasing interval length (`gap`)
    so that all smaller subproblems are already computed.

Base Cases:
    • gap = 0 → i == j → no multiplication required.
    • gap = 1 → one matrix → cost is 0.

Time Complexity:
    O(N³)

    There are O(N²) subproblems, and each subproblem
    checks O(N) possible partition points.

Space Complexity:
    O(N²)

    The DP table requires O(N²) space.

where,
    N = len(arr)
"""

def matChain(arr):
    n = len(arr)

    if n <= 2:
        return 0

    dp = [[0] * n for _ in range(n)]

    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            dp[i][j] = float('inf')
            for k in range(i + 1, j):
                left = dp[i][k]
                right = dp[k][j]
                cost = arr[i] * arr[k] * arr[j]

                dp[i][j] = min(dp[i][j], left + right + cost)
                

    return dp[0][n - 1]