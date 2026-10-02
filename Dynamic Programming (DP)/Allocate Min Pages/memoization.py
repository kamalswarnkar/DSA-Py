"""
Allocate Minimum Number of Pages using Memoization

Problem:
    Given an array `arr` where arr[i] represents the number of
    pages in the i-th book, allocate all books to `k` students.

    Rules:
        • Each student must receive at least one book.
        • Each book must be assigned to exactly one student.
        • Books must be allocated in contiguous order.

    Goal:
        Minimize the maximum number of pages assigned to any
        single student.

Approach:
    Memoization (Top-Down Dynamic Programming)

    `solve(i, j)` represents:

        Minimum possible maximum pages when allocating the
        first `i` books among `j` students.

    We choose a partition point `t`:

        First t books:
            solve(t, j - 1)

        Remaining books:
            pref[i] - pref[t]

    The maximum workload for this partition is:

        max(
            solve(t, j - 1),
            pref[i] - pref[t]
        )

    We try every valid partition and choose the one that
    minimizes this maximum.

    A prefix-sum array is used so that the number of pages
    in any range can be calculated in O(1).

Base Cases:
    • j == 1:
        One student receives all first i books.

    • i == 1:
        Only one book is being allocated.

Time Complexity:
    O(K × N²)

    There are O(N × K) states.
    For each state, we try O(N) partition points.

    Prefix sums make every range-sum calculation O(1).

Space Complexity:
    O(N × K)

    O(N × K) for the memoization table,
    O(N) for the prefix-sum array,
    and O(K) recursion-stack space.

where,
    N = number of books
    K = number of students
"""

def minPages(arr, k):
    n = len(arr)

    if n < k:
        return -1

    if k == 1:
        return sum(arr)

    if n == 1:
        return arr[0]

    pref = [0] * (n + 1) # Prefix sum array for O(1) range sum lookups
    for i in range(n):
        pref[i + 1] = pref[i] + arr[i]

    memo = [[-1] * (k + 1) for _ in range(n + 1)]

    def solve(i, j):
        if j == 1:
            return pref[i]

        if i == 1:
            return arr[0]

        if memo[i][j] != -1:
            return memo[i][j]

        res = float('inf')

        for t in range(j - 1, i):
            left = solve(t, j - 1)
            right = pref[i] - pref[t]
            curr = max(left, right)

            res = min(res, curr)

        memo[i][j] = res

        return memo[i][j]

    return solve(n, k)