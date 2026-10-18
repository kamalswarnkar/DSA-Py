"""
Longest Correct Bracket Subsequence

Problem:
    For each range [l, r], find the length of the longest
    correct bracket subsequence in s[l:r + 1].

Approach:
    Each segment-tree node stores:
        1. Unmatched opening brackets.
        2. Unmatched closing brackets.

    During merging, match opening brackets from the left
    segment with closing brackets from the right segment.

Time Complexity:
    Build:  O(N)
    Query:  O(log N) typically, O(N) worst case

Space Complexity: O(N) for the tree.
"""

def segmentTree(s, queries):
    n = len(s)

    if n == 0:
        return []

    tree = [0] * (4 * n)

    def merge(left, right):
        matched = min(left[0], right[1])

        return (
            left[0] + right[0] - matched,
            left[1] + right[1] - matched
        )

    def buildTree(ss, se, si):
        if ss == se:
            if s[ss] == '(':
                tree[si] = (1, 0)
            else:
                tree[si] = (0, 1)
            return

        mid = (ss + se) // 2

        buildTree(ss, mid, 2*si + 1)
        buildTree(mid + 1, se, 2*si + 2)

        tree[si] = merge(tree[2*si + 1], tree[2*si + 2])

    def getLongestSeq(qs, qe, ss, se, si):
        if se < qs or qe < ss:
            return (0, 0)

        if qs <= ss and se <= qe:
            return tree[si]

        mid = (ss + se) // 2

        left = getLongestSeq(qs, qe, ss, mid, 2*si + 1)
        right = getLongestSeq(qs, qe, mid + 1, se, 2*si + 2)

        return merge(left, right)

    buildTree(0, n - 1, 0)

    res = []

    for query in queries:
        left, right = query

        unmatched_open, unmatched_close = getLongestSeq(left, right, 0, n - 1, 0)

        res.append(right - left + 1 - unmatched_open - unmatched_close)

    return res