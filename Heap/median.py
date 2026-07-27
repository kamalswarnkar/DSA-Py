"""
Median of a Data Stream

Given a stream of numbers, return the median after
each insertion.

Idea:
Maintain two heaps:
1. Max Heap (left half) stores the smaller elements.
2. Min Heap (right half) stores the larger elements.

Maintain the following invariants:
• The size difference between the heaps is at most 1.
• Every element in the Max Heap is less than or equal
  to every element in the Min Heap.

Time Complexity:
    Per Insertion : O(log N)
    Total         : O(N log N)

Space Complexity:
    O(N)

where,
N = number of elements in the stream

Core Intuition:
The Max Heap stores the lower half and the Min Heap
stores the upper half. The median is always available
at the roots of these heaps.

Interview Notes:
Python Version Note:
• Python versions before 3.14 provide only a Min Heap.
  A Max Heap is simulated by storing negative values.
• Python 3.14 and later provide native Max Heap support
  through `heapify_max()`, `heappush_max()`,
  `heappop_max()`, `heappushpop_max()`, and
  `heapreplace_max()`.
"""

import heapq

def streamMedian(arr):
    n = len(arr)
    small, large = [], [] # small -> Max-Heap (-ve values), large -> Min-Heap
    op = []

    for i in range(n):
        heapq.heappush(small, -arr[i])
        heapq.heappush(large, -heapq.heappop(small))

        if len(large) > len(small):
            heapq.heappush(small, -heapq.heappop(large))

        if len(large) < len(small):
            op.append(-small[0])
        else:
            op.append((large[0] - small[0])/2)

    return op
