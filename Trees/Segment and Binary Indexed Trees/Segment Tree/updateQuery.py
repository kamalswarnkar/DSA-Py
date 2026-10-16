"""
Update Query on Segment Tree

Problem:
    Update an array element at index i and reflect the change
    in all affected nodes of a range-sum segment tree.

Approach:
    Calculate the difference between the new and old values.
    Add this difference to every segment-tree node along the
    path containing index i.

Time Complexity:  O(log N) per update.
Space Complexity: O(N) for the tree; O(log N) recursion stack.
"""

def segmentTree(arr):
    n = len(arr)

    if n == 0:
        return []
    
    tree = [0] * (4 * n)

    def buildTree(ss, se, si):
        if ss == se:
            tree[si] = arr[ss]
            return arr[ss]

        mid = (ss + se) // 2

        left_sum = buildTree(ss, mid, 2*si + 1)
        right_sum = buildTree(mid + 1, se, 2*si + 2)

        tree[si] = left_sum + right_sum

        return tree[si]

    def update(ss, se, si, i, diff):
        if i < ss or i > se:
            return

        tree[si] += diff

        if se > ss:
            mid = (ss + se) // 2
            update(ss, mid, 2*si + 1, i, diff)
            update(mid + 1, se, 2*si + 2, i, diff)

    buildTree(0, n - 1, 0)
    update(0, n - 1, 0, 1, 5) # increase the value at index 1 by 5

    return tree