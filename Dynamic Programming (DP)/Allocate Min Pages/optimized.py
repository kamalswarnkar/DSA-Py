"""
Allocate Minimum Number of Pages using Binary Search

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
    Binary Search on Answer

    Instead of directly finding the allocation, we binary-search
    the maximum number of pages that a student is allowed to receive.

    Search range:

        low  = max(arr)
        high = sum(arr)

    Why?

        low:
            At least one student must receive the book having
            the maximum number of pages.

        high:
            One student could receive all books.

    For every candidate `mid`, check whether it is possible to
    allocate all books among at most `k` students such that no
    student receives more than `mid` pages.

    If possible:
        Try a smaller maximum.
        high = mid - 1

    If not possible:
        We need a larger maximum.
        low = mid + 1

    The first feasible value is the answer.

Time Complexity:
    O(N × log(S))

    Each feasibility check takes O(N), and binary search performs
    O(log(S)) checks.

    S = sum(arr)

Space Complexity:
    O(1)

    Only a constant amount of extra space is used.

where,
    N = number of books
    K = number of students
    S = total number of pages
"""

def isPossible(arr, n, k, max_pages_allowed):
    stud_count = 1
    curr_pages = 0

    for pages in arr:
        if curr_pages + pages > max_pages_allowed:
            stud_count += 1
            curr_pages = pages

            if stud_count > k:
                return False
        else:
            curr_pages += pages

    return True

def minPages(arr, k):
    n = len(arr)

    if n < k:
        return -1

    low = max(arr)
    high = sum(arr)
    res = -1

    while low <= high:
        mid = low + (high - low)//2

        if isPossible(arr, n, k, mid):
            res = mid
            high = mid - 1
        else:
            low = mid + 1

    return res