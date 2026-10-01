"""
Count Total BSTs with N Keys using Recursion

Problem:
    Given N distinct keys, count the total number of
    structurally different Binary Search Trees (BSTs)
    that can be formed using all N keys.

Approach:
    Recursion

    For every key `i`, consider it as the root.

        • `i` keys form the left subtree.
        • `N - i - 1` keys form the right subtree.

    Therefore, for root `i`:

        countBST(i) * countBST(N - i - 1)

    Summing this over every possible root gives:

        countBST(N) =
            Σ countBST(i) * countBST(N - i - 1)

    Base Cases:
        N = 0 → 1
        N = 1 → 1

    The recurrence generates the Catalan numbers.

Time Complexity:
    O(3^N)

    The recursive solution repeatedly solves the same
    overlapping subproblems.

Space Complexity:
    O(N)

    The maximum recursion depth is O(N).

where,
    N = number of keys
"""

def countBST(n):
    if n == 0 or n == 1:
        return 1

    """s, i = 0, 0

    while i < n:
        s += (countBST(i) * countBST(n - i - 1))
        i += 1

    return s""" # this method is fine but we can shorten this by going with more pythonic way like the one below

    return sum((countBST(i) * countBST(n - i - 1)) for i in range(n))
