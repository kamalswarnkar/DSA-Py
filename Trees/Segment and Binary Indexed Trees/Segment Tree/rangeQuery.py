"""
Range Query on Segment Tree

Problem:
    Find the sum of array elements in a given query range [qs, qe].

Approach:
    1. Build a segment tree storing sums of array segments.
    2. Return 0 for non-overlapping segments.
    3. Return the stored sum for completely overlapping segments.
    4. Recursively query both children for partial overlap.

Time Complexity:
    Build: O(N)
    Query: O(log N) for a typical range query; O(N) worst case.

Space Complexity: O(N) for the tree and O(log N) recursion stack.
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

    def getSum(qs, qe, ss, se, si): # query_start, query_end, segment_start, segment_end, segment_index
        if se < qs or ss > qe: # no overlap
            return 0

        if qs <= ss and qe >= se: # complete overlap
            return tree[si]

        mid = (ss + se) // 2

        left_sum = getSum(qs,qe, ss, mid, 2*si + 1)
        right_sum = getSum(qs, qe, mid + 1, se, 2*si + 2)

        return left_sum + right_sum

    buildTree(0, n - 1, 0)
    
    return getSum(0, 2, 0, n - 1, 0)
