"""
Check if a Binary Tree is Foldable

A Binary Tree is foldable if its left and right
subtrees are structural mirror images of each other.

Only the structure is compared; node values are ignored.

An empty tree is always foldable.

Idea:
1. Compare the left and right subtrees recursively.
2. If both corresponding nodes are absent, the tree is foldable.
3. If only one node exists, the tree is not foldable.
4. Compare left child of one subtree with the right child
   of the other subtree and vice versa.

Time Complexity : O(N)
Space Complexity: O(H)

where,
N = number of nodes
H = height of tree
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isFoldable(root):
    if root is None:
        return True
    
    def isMirror(a, b):
        if not a and not b:
            return True
        
        if (a and not b) or (not a and b):
            return False
        
        # Only the mirror structure is compared; node values are ignored.
        
        return isMirror(a.left, b.right) and isMirror(a.right, b.left)
    
    return isMirror(root.left, root.right)