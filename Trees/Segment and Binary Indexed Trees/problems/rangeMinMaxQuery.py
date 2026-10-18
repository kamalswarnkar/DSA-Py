"""
Range Min-Max Queries Using a Segment Tree

Problem:
    Support range minimum/maximum queries and point updates.

Approach:
    Each node stores (minimum, maximum) for its segment.
    Combine child nodes using min() for minimums and max()
    for maximums. Use identity values for non-overlapping ranges.

Time Complexity:
    Build:  O(N)
    Query:  O(log N) typically, O(N) worst case
    Update: O(log N)

Space Complexity: O(N) for the tree.
"""

def segmentTree(arr, queries):
    n = len(arr)

    if n == 0:
        return []

    tree = [(0, 0)] * (4 * n)

    def buildTree(ss, se, si):
        if ss == se:
            tree[si] = (arr[ss], arr[ss])
            return

        mid = (ss + se) // 2

        buildTree(ss, mid, 2*si + 1)
        buildTree(mid + 1, se, 2*si + 2)

        left = tree[2*si + 1]
        right = tree[2*si + 2]

        tree[si] = (
            min(left[0], right[0]),
            max(left[1], right[1])
        )

    def getMinMax(qs, qe, ss, se, si):
        if qs > se or qe < ss:
            return (float('inf'), float('-inf'))

        if qs <= ss and se <= qe:
            return tree[si]

        mid = (ss + se) // 2

        left = getMinMax(qs, qe, ss, mid, 2*si + 1)
        right = getMinMax(qs, qe, mid + 1, se, 2*si + 2)

        return (min(left[0], right[0]), max(left[1], right[1]))

    def update(idx, val, ss, se, si):
        if ss == se:
            arr[idx] = val
            tree[si] = (val, val)
            return

        mid = (ss + se) // 2

        if idx <= mid:
            update(idx, val, ss, mid, 2*si + 1)
        else:
            update(idx, val, mid + 1, se, 2*si + 2)

        left = tree[2*si + 1]
        right = tree[2*si + 2]
        
        tree[si] = (
            min(left[0], right[0]),
            max(left[1], right[1])
        )

    buildTree(0, n - 1, 0)

    res = []

    for query in queries:
        if query[0] == 1:
            _, left, right = query
            minimum, maximum = getMinMax(left, right, 0, n - 1, 0)
            res.append([minimum, maximum])
        else:
            _, index, value = query
            update(index, value, 0, n - 1, 0)

    return res