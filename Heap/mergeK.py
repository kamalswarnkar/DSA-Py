"""
Merge K Sorted Arrays

Given K individually sorted arrays, merge them into
a single sorted array.

Idea:
1. Insert the first element of every array into a Min Heap.
2. Remove the smallest element and append it to the result.
3. Insert the next element from the same array into the heap.
4. Repeat until the heap becomes empty.

Time Complexity:
    O(N log K)

Space Complexity:
    O(K)

where,
N = total number of elements across all arrays
K = number of sorted arrays

Core Intuition:
The heap always contains at most one candidate from each
array. The smallest among these candidates is the next
element in the final sorted order.

Interview Notes:
• More efficient than repeatedly merging two arrays.
• Uses a Min Heap of size at most K.
• Similar approach is used to merge K sorted linked lists.
"""

import heapq

def mergeK(arr):
    res = []
    h = []

    for i in range(len(arr)):
        heapq.heappush(h, (arr[i][0], i, 0))

    while h:
        # arr_idx = Which array the element belongs to
        # ele_idx = Index within that array
        val, arr_idx, ele_idx = heapq.heappop(h)
        res.append(val)

        if ele_idx + 1 < len(arr[arr_idx]):
            heapq.heappush(h, (arr[arr_idx][ele_idx + 1], arr_idx, ele_idx + 1))

    return res