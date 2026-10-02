"""
Matrix Chain Multiplication using Recursion

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
    Recursion / Divide and Conquer

    `matChain(arr, i, j)` represents the minimum multiplication
    cost required to multiply the matrices from index `i`
    through `j - 1`.

    For every possible partition `k`:

        Left  = matChain(arr, i, k)
        Right = matChain(arr, k, j)

    After multiplying the two resulting matrices, the additional
    multiplication cost is:

        arr[i] × arr[k] × arr[j]

    Therefore:

        matChain(i, j) =
            min(
                matChain(i, k)
                + matChain(k, j)
                + arr[i] × arr[k] × arr[j]
            )

        for every i < k < j.

Base Case:
    If only one matrix remains, no multiplication is required:

        i + 1 == j → 0

Time Complexity:
    O(3^N)

    The recursive solution repeatedly solves overlapping
    subproblems and tries every possible partition.

Space Complexity:
    O(N)

    The maximum recursion depth is O(N).

where,
    N = number of matrices
"""

def matChain(arr, i, j):
    if i + 1 == j: # if only 1 matrix is remaining
        return 0

    res = float('inf')

    for k in range(i + 1, j): # checking every possible partition to get minimum no. of multiplication
        left = matChain(arr, i, k)
        right = matChain(arr, k, j)
        cost = arr[i] * arr[j] * arr[k]

        res = min(res, left + right + cost)

    return res
        