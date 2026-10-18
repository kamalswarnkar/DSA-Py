"""
Range GCD Queries Using a Segment Tree

Problem:
    Support range GCD queries and point updates on an array.

Approach:
    1. Build a segment tree storing the GCD of each segment.
    2. For a query, combine overlapping segment results using gcd.
    3. For an update, modify the leaf and recompute GCDs
       along the path back to the root.

Time Complexity:
    Build:  O(N)
    Query:  O(log N) typically, O(N) worst case
    Update: O(log N)

Space Complexity: O(N) for the tree.
"""

from math import gcd

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

        tree[si] = gcd(tree[2*si + 1], tree[2*si + 2])

    def getGCD(qs, qe, ss, se, si): # query_start, query_end, segment_start, segment_end, segment_index
        if se < qs or ss > qe: # no overlap
            return 0

        if qs <= ss and qe >= se: # complete overlap
            return tree[si]

        mid = (ss + se) // 2

        left_gcd = getGCD(qs,qe, ss, mid, 2*si + 1)
        right_gcd = getGCD(qs, qe, mid + 1, se, 2*si + 2)

        return gcd(left_gcd, right_gcd)

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

        tree[si] = gcd(tree[2*si + 1], tree[2*si + 2])

    buildTree(0, n - 1, 0)
    
    res = []

    for query in queries:
        if query[0] == 0:
            _, left, right = query
            res.append(getGCD(left, right, 0, n - 1, 0))
        else:
            _, index, value = query
            update(index, value, 0, n - 1, 0)

    return res