"""
Lowest Common Ancestor (LCA) in a Binary Tree

The Lowest Common Ancestor of two nodes n1 and n2
is the deepest node that has both n1 and n2 as descendants.

Idea:
1. If it is same as n1 or n2, return it.
2. If one subtree contains n1, & other contains n2.
3. If one subtrees contains both n1 & n2.
4. If none of its subtrees containsany of n1 & n2.

Time Complexity: O(N)
Space Complexity: O(H)

where:
N = number of nodes
H = height of the tree
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def lca(root, n1, n2):
    if root is None or root.val == n1 or root.val == n2:
        return root
    
    lca_1 = lca(root.left, n1, n2)
    lca_2 = lca(root.right, n1, n2)

    if lca_1 and lca_2:
        return root
    
    return lca_1 if lca_1 else lca_2