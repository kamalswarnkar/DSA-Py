"""
Updating Elements in a Binary Indexed Tree (Fenwick Tree)

Problem:
    Update an array element to a new value and reflect the
    change in the Fenwick Tree.

Approach:
    1. Calculate the difference between the new and old values.
    2. Update the original array.
    3. Add the difference to every responsible BIT index.
    4. Advance using the lowest set bit.

Time Complexity:  O(N) construction + O(log N) per update.
Space Complexity: O(N).
"""

def BITree(arr):
    n = len(arr)
    bitree = [0] + list(arr)

    for i in range(1, n + 1):
        par = i + (i & (-i))

        if par <= n:
            bitree[par] += bitree[i]

    def update(idx, num):
        diff = num - arr[idx]
        arr[idx] = num
        idx += 1

        while idx < len(bitree):
            bitree[idx] += diff
            idx += (idx & (-idx))

    update(2, 8) # original array = [3, 7, 11, 8, 6]

    return bitree