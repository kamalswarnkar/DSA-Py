"""
Range LCM Queries Using a Segment Tree

Problem:
    Process point updates and range LCM queries on an array.

Approach:
    1. Build a segment tree storing the LCM of each segment.
    2. Return 1 for non-overlapping segments (LCM identity).
    3. Combine overlapping results using lcm().
    4. For updates, modify the leaf and recompute ancestor LCMs.

Time Complexity:
    Build:  O(N)
    Query:  O(log N) typically, O(N) worst case
    Update: O(log N)

Space Complexity: O(N) for the tree.
"""

from math import lcm

def segmentTree(arr, queries):
    n = len(arr)

    if n == 0:
        return []

    tree = [0] * (4 * n)

    def buildTree(ss, se, si):
        if ss == se:
            tree[si] = arr[ss]
            return

        mid = (ss + se) // 2

        buildTree(ss, mid, 2*si + 1)
        buildTree(mid + 1, se, 2*si + 2)

        tree[si] = lcm(tree[2*si + 1], tree[2*si + 2])

    def getLCM(qs, qe, ss, se, si):
        if qs > se or qe < ss:
            return 1

        if qs <= ss and se <= qe:
            return tree[si]

        mid = (ss + se) // 2

        left_lcm = getLCM(qs, qe, ss, mid, 2*si + 1)
        right_lcm = getLCM(qs, qe, mid + 1, se, 2*si + 2)

        return lcm(left_lcm, right_lcm)

    def update(idx, val, ss, se, si):
        if ss == se:
            arr[idx] = val
            tree[si] = val
            return

        mid = (ss + se) // 2

        if idx <= mid:
            update(idx, val, ss, mid, 2*si + 1)
        else:
            update(idx, val, mid + 1, se, 2*si + 2)

        tree[si] = lcm(tree[2*si + 1], tree[2*si + 2])

    buildTree(0, n - 1, 0)

    res = []

    for query in queries:
        if query[0] == 1:
            _, index, value = query
            update(index, value, 0, n - 1, 0)
        else:
            _, left, right = query
            res.append(getLCM(left, right, 0, n - 1, 0))

    return res