"""
Prefix Sum Using a Binary Indexed Tree (Fenwick Tree)

Problem:
    Construct a BIT and calculate the prefix sum from index 0
    through a specified index.

Approach:
    1. Build the BIT in O(N) time.
    2. Convert the 0-based query index to 1-based indexing.
    3. Add the relevant BIT entries while removing the lowest
       set bit at each step.

Time Complexity:  O(N) construction + O(log N) query.
Space Complexity: O(N).
"""

def BITree(arr):
    n = len(arr)
    bitree = [0] + list(arr)

    for i in range(1, n + 1):
        par = i + (i & (-i))

        if par <= n:
            bitree[par] += bitree[i]

    def getSum(idx):
        idx += 1
        res = 0

        while idx > 0:
            res += bitree[idx]
            idx -= (idx & (-idx))

        return res

    return getSum(4)