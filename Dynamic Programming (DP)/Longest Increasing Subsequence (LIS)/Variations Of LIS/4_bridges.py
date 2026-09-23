"""
Building Bridges

Problem:
    Given pairs representing the two endpoints of bridges, find the
    maximum number of bridges that can be built without crossing.

Approach:
    1. Sort the bridges by their first endpoint.
    2. If two bridges have the same first endpoint, sort them by
       their second endpoint.
    3. Extract the second endpoints.
    4. Find the Longest Increasing Subsequence (LIS) of the second
       endpoints.

Why LIS?
    After sorting by the first endpoint, two bridges do not cross
    when their second endpoints are also in increasing order.

    Therefore, the problem reduces to finding the longest increasing
    subsequence of the second endpoints.

Time Complexity:
    O(N log N)

    Sorting takes O(N log N).
    LIS using binary search takes O(N log N).

Space Complexity:
    O(N)

    For the extracted second endpoints and the LIS tail array.

where,
    N = number of bridges
"""

def ceilIdx(tail, x):
    l = 0
    r = len(tail) - 1

    while l < r:
        m = l + (r - l)//2
        if x <= tail[m]:
            r = m
        else:
            l = m + 1

    return r

def lis(arr):
    n = len(arr)
    tail = [arr[0]]

    for i in range(1, n):
        if arr[i] > tail[-1]:
            tail.append(arr[i])
        else:
            c = ceilIdx(tail, arr[i])
            tail[c] = arr[i]

    return len(tail)

def bridge(arr):
    n = len(arr)

    if n == 0:
        return 0
    
    arr.sort(key = lambda x : (x[0], x[1]))

    second_val = [pair[1] for pair in arr]

    return lis(second_val)
