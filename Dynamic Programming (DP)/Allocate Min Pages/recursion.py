"""
Allocate Minimum Number of Pages using Recursion

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
    Recursion / Divide and Conquer

    `minPages(arr, n, k)` represents:

        The minimum possible maximum number of pages assigned
        to any student when allocating the first `n` books
        among `k` students.

    We try every possible position `i` where the last student
    starts receiving books:

        First i books:
            minPages(arr, i, k - 1)

        Remaining books:
            sum(arr[i:n])

    Since the workload of the current allocation is determined
    by the student receiving the larger number of pages:

        max(
            minPages(arr, i, k - 1),
            sum(arr[i:n])
        )

    We choose the partition that minimizes this maximum.

Base Cases:
    • k == 1:
        One student gets all remaining books.

    • n == 1:
        Only one book remains, so it must be assigned to
        the only available student.

Time Complexity:
    O(N^K)

    At each recursive level, we try O(N) possible partitions
    across K levels.

    Note:
        The exact recurrence has overlapping subproblems, so
        this is an exponential recursive solution.

Space Complexity:
    O(K)

    The maximum recursion depth is K.

where,
    N = number of books
    K = number of students
"""

def minPages(arr, n, k):
    if k == 1:
        return sum(arr[0:n])

    if n == 1:
        return arr[0]

    res = float('inf')

    for i in range(1, n):
        left = minPages(arr, i, k - 1)
        right = sum(arr[i:n])
        curr = max(left, right)

        res = min(res, curr)

    return res