"""
Python Heap (`heapq` Module)

Python provides the `heapq` module to implement a Min Heap.

Unlike the custom Heap implementation, `heapq` works directly
on Python lists and automatically maintains the heap property.

Properties:
• Implements a Min Heap.
• Smallest element is always at index 0.
• Heap is stored as an array (list).

Common Operations:
1. heapify()
2. heappush()
3. heappop()
4. heappushpop()
5. heapreplace()
6. nlargest()
7. nsmallest()

Time Complexity:

heapify()      : O(N)
heappush()     : O(log N)
heappop()      : O(log N)
heappushpop()  : O(log N)
heapreplace()  : O(log N)
nlargest()     : O(N log K)
nsmallest()    : O(N log K)

where,
N = number of elements
K = number of required largest/smallest elements

Note:
`heapq` implements only a Min Heap.
To simulate a Max Heap, store negative values.
"""

import heapq

arr = [6, 7, 9, 4, 3, 5, 8, 10, 1]

heapq.heapify(arr) # convert list into Min Heap (in-place)

heapq.heappush(arr, 11) #  # Insert 11 while maintaining the heap property

heapq.heappop(arr) # Remove and return the smallest element

# Push 121 and immediately remove the smallest element
# More efficient than calling heappush() followed by heappop()
heapq.heappushpop(arr, 121)

heapq.heapreplace(arr, 99) # Remove the smallest element first, then insert 99.

heapq.nlargest(2, arr) # return 2 largest elements of the heap

heapq.nsmallest(2, arr) # return 2 smallest elements of the heap