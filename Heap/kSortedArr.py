"""
Sort a K-Sorted Array

A K-Sorted (Nearly Sorted) array is one in which every
element is at most K positions away from its correct
position in the sorted order.

Idea:
1. Insert the first (K + 1) elements into a Min Heap.
2. Repeatedly remove the minimum element and place it
   into the output.
3. Insert the next array element into the heap.
4. After processing all elements, remove the remaining
   heap elements.

Time Complexity:
    O(N log K)

Space Complexity:
    O(K)

where,
N = number of elements
K = maximum distance of any element from its
correct sorted position.

Note:
Using a Min Heap of size (K + 1) guarantees that the
smallest remaining element is always available at the root.

Core Intuition:
Since every element can be displaced by at most K positions,
its correct position must lie within the next (K + 1) elements.
A Min Heap of size (K + 1) efficiently keeps track of the
smallest candidate.

Interview Notes:
• Much faster than Heap Sort when K << N.
• If K = N - 1, this algorithm becomes similar to Heap Sort
  with O(N log N) complexity.
"""

import heapq

def sortK(arr, k):
    n = len(arr)

    pq = arr[:k + 1] # Build a Min Heap using the first (K + 1) elements
    heapq.heapify(pq)

    idx = 0

    for i in range(k + 1, n): # Process the remaining elements
        arr[idx] = heapq.heappop(pq)
        idx += 1
        heapq.heappush(pq, arr[i])

    while pq: # Place the remaining heap elements into the array
        arr[idx] = heapq.heappop(pq)
        idx += 1