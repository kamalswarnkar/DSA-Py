"""
Constructing a Binary Indexed Tree (Fenwick Tree)

Problem:
    Build a BIT for efficient prefix-sum queries and point updates.

Approach:
    1. Create a 1-indexed BIT from the input array.
    2. Propagate each node's accumulated sum to its parent.
    3. Find the parent using the lowest set bit: i + (i & -i).

Time Complexity:  O(N)
Space Complexity: O(N)
"""

def BITree(arr):
    n = len(arr)
    bitree = [0] + list(arr) # BIT uses 1-based indexing; index 0 is unused.

    for i in range(1, n + 1):
        # i & -i extracts the lowest set bit of i
        # Adding it to i gives the next BIT index that receives the current node's sum
        parent = i + (i & (-i))

        if parent <= n: # Propagate this node's sum to its parent.
            bitree[parent] += bitree[i]

    return bitree