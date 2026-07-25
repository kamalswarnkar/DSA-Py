"""
Heap Sort

Heap Sort is a comparison-based, in-place sorting algorithm
that uses a Binary Heap.

Algorithm:
1. Build a Max Heap from the input array.
2. Swap the root (largest element) with the last element.
3. Reduce the heap size by one.
4. Restore the Max Heap property.
5. Repeat until the heap becomes empty.

Time Complexity:
    Best    : O(N log N)
    Average : O(N log N)
    Worst   : O(N log N)

Space Complexity:
    O(1)

where,
N = number of elements

Properties:
• In-place sorting algorithm.
• Not stable.
• Does not require additional memory.
• Used in hybrid sorting algorithms such as IntroSort.

Core Intuition:
A Max Heap always keeps the largest element at the root.
Repeatedly removing the root places elements into their
correct position from the end of the array.

Interview Notes:
• Heap Sort is not stable.
• Heap Sort is an in-place algorithm.
• Build Heap runs in O(N), not O(N log N).
• Unlike Merge Sort, Heap Sort requires only O(1) extra space.
"""

def maxHeapify(arr, n, i):
    largest = i

    lt = 2*i + 1
    rt = 2*i + 2

    if lt < n and arr[lt] > arr[largest]:
        largest = lt
    if rt < n and arr[rt] > arr[largest]:
        largest = rt

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        maxHeapify(arr, n, largest)


def buildHeap(arr):
    n = len(arr)
    start_idx = n // 2 - 1

    for i in range(start_idx, -1, -1):
        maxHeapify(arr, n, i)

def heapSort(arr):
    n = len(arr)

    buildHeap(arr)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        maxHeapify(arr, i, 0)