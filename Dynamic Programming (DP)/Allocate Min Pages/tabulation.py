"""
Allocate Minimum Number of Pages using Tabulation

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
    Tabulation (Bottom-Up Dynamic Programming)

    `dp[i][j]` represents:

        Minimum possible maximum number of pages when allocating
        the first `i` books among `j` students.

    For every possible partition point `p`:

        First p books:
            dp[p][j - 1]

        Remaining books:
            pref[i] - pref[p]

    The maximum workload for this partition is:

        max(
            dp[p][j - 1],
            pref[i] - pref[p]
        )

    We try every valid partition and choose the one that
    minimizes this maximum.

    A prefix-sum array is used so that the number of pages
    in any range can be calculated in O(1).

Base Cases:
    • dp[i][1] = pref[i]
        One student receives all first i books.

    • dp[1][j] = arr[0]
        Only one book is being allocated.

Time Complexity:
    O(K × N²)

    There are O(N × K) DP states.
    For each state, we try O(N) partition points.

    Prefix sums make range-sum calculations O(1).

Space Complexity:
    O(N × K)

    O(N × K) for the DP table and O(N) for the
    prefix-sum array.

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

    pref = [0] * (n + 1)
    for idx in range(n):
        pref[idx + 1] = pref[idx] + arr[idx]

    dp = [[float('inf')] * (k + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        dp[i][1] = pref[i]

    for i in range(1, k + 1):
        dp[1][i] = arr[0]

    for j in range(2, k + 1):
        for i in range(2, n + 1):
            res = float('inf')

            for p in range(j - 1, i):
                left = dp[p][j - 1]
                right = pref[i] - pref[p]
                curr = max(left, right)

                res = min(res, curr)

                dp[i][j] = res

    return dp[n][k]