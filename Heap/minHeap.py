"""
Min Heap

A Min Heap is a Complete Binary Tree in which every parent
node is smaller than or equal to its children.

This implementation stores the heap as an array for efficient
operations and also provides a utility to convert the array
into a binary tree for visualization and traversal.

Array Representation:
    Parent      : (i - 1) // 2
    Left Child  : 2 * i + 1
    Right Child : 2 * i + 2

Supported Operations:
1. Insert
2. Extract Minimum
3. Build Heap
4. Decrease Key
5. Delete Key
6. Min Heapify
7. Convert Array → Tree

Time Complexity:

Insert            : O(log N)
Extract Min       : O(log N)
Build Heap        : O(N)
Decrease Key      : O(log N)
Delete            : O(log N)
Min Heapify       : O(log N)
Array → Tree      : O(N)

Space Complexity:
    Heap Storage  : O(N)
    Tree Build    : O(N)

where,
N = number of elements

Notes:
1.  MinHeapify assumes that only the current node violates the
    heap property while both its subtrees already satisfy it.

2.  Max Heap is the mirror implementation of a Min Heap.
    Simply reverse all comparison operators (< ↔ >) and
    replace minimum operations with maximum operations.

3.  Build Heap runs in O(N), not O(N log N), because most heapify
    operations occur on nodes near the leaves, where the subtree
    heights are very small.

4.  Interview Notes:
• Heap is NOT a Binary Search Tree.
• Only the root is guaranteed to be the minimum element.
• There is no ordering between sibling nodes or across subtrees.
• Build Heap (O(N)) is more efficient than inserting N elements one by one (O(N log N)).
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class MinHeap: # Array Representation
    def __init__(self):
        self.arr = []

    def parent(self, i): # return index of parent of child 'i'
        return (i - 1)//2

    def lChild(self, i): # return index of left child of parent 'i'
        return (2*i + 1)

    def rChild(self, i): # return index of right child of parent 'i'
        return (2*i + 2)

    def insert(self, x): # inserting new node in tree
        self.arr.append(x)

        idx = len(self.arr) - 1

        while idx > 0 and self.arr[self.parent(idx)] > self.arr[idx]: # if index exist and the child is smaller than parent
            p = self.parent(idx)
            self.arr[idx], self.arr[p] = self.arr[p], self.arr[idx] # swap with parent

            idx = p

    def minHeapify(self, i): 
        lt = self.lChild(i) # left child of node
        rt = self.rChild(i) # right child of node

        smallest = i # initiating it as parent
        n = len(self.arr)

        # updating smallest
        if lt < n and self.arr[lt] < self.arr[smallest]:
            smallest = lt
        if rt < n and self.arr[rt] < self.arr[smallest]:
            smallest = rt

        if smallest != i: # if parent doesn't remain smallest then swapping
            self.arr[i], self.arr[smallest] = self.arr[smallest], self.arr[i]
            self.minHeapify(smallest) # doing it unitl complete rectification

    def extractMin(self):
        n = len(self.arr)

        if n == 0:
            return float("-inf")

        if n == 1:
            return self.arr.pop()

        res = self.arr[0]

        self.arr[0] = self.arr[n - 1] # assigning instead of swapping
        self.arr.pop()

        self.minHeapify(0)

        return res

    def buildHeap(self):
        n = len(self.arr)
        start_idx = n // 2 - 1 # starting from last non-leaf node

        for i in range(start_idx, -1, -1): # Heapify every internal node in bottom-up order
            self.minHeapify(i)

    def decreaseKey(self, i, x):
        self.arr[i] = x

        while i != 0 and self.arr[self.parent(i)] > self.arr[i]:
            p = self.parent(i)
            self.arr[i], self.arr[p] = self.arr[p], self.arr[i]
            i = p

    def delete(self, i):
        n = len(self.arr)

        if i >= n:
            return

        self.decreaseKey(i, float("-inf"))
        self.extractMin()

"""
Converts the heap's array representation into
a pointer-based binary tree.

Useful for visualization and traversals.
Heap operations should still be performed
on the array representation.
"""

def buildTree(arr): # Tree representation
    if not arr:
        return None

    nodes = [Node(x) for x in arr]

    for i in range(len(arr)):
        l = 2*i + 1
        r = 2*i + 2

        if l < len(arr):
            nodes[i].left = nodes[l]

        if r < len(arr):
            nodes[i].right = nodes[r]

    return nodes[0]