"""
Count Distinct Rows in a Binary Matrix

Problem:
    Count the number of distinct rows using a binary Trie.

Approach:
    Insert each row into the Trie.
    Mark the end of every complete row.
    Count a row only if its terminal node has not been
    marked previously.

Time Complexity:  O(R * C), where R is the number of rows
                  and C is the number of columns.
Space Complexity: O(R * C) in the worst case.
"""

class TrieNode:
    def __init__(self):
        self.child = [None] * 2 # Binary Matrix -> only '0' and '1'
        self.isEndOfRow = False

def insert(node, row):
    for bit in row:
        if not node.child[bit]:
            node.child[bit] = TrieNode()

        node = node.child[bit]

    if node.isEndOfRow:
        return False

    node.isEndOfRow = True

    return True

def countDist(mat):
    res = 0
    root = TrieNode()

    for i in range(len(mat)):
        if insert(root, mat[i]):
            res += 1

    return res