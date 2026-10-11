"""
Constructing a Segment Tree

Problem:
    Build a segment tree for range-sum queries on an array.

Approach:
    Recursively divide each segment into two halves.
    Store the array value at each leaf and the sum of the
    two child nodes at each internal node.

Time Complexity:  O(N), where N is the array length.
Space Complexity: O(N) for the tree and O(log N) recursion
                  stack for a balanced segment tree.
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

    buildTree(0, n - 1, 0)

    return tree