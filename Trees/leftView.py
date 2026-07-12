"""
Left View of a Binary Tree

The Left View consists of all nodes visible when the
tree is viewed from the left side.

Idea:
1. Perform a preorder DFS (Root → Left → Right).
2. Keep track of the deepest level visited so far.
3. The first node visited at every level belongs to the left view.

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

def leftView(root):
    max_lvl = 0
    
    def traverse(node, lvl):
        nonlocal max_lvl

        if node is None:
            return
        
        if lvl == max_lvl:
            print(node.val, end=" ")
            max_lvl += 1
        
        traverse(node.left, lvl + 1)
        traverse(node.right, lvl + 1)
        
        """
        For the Right View, simply visit the right subtree
        before the left subtree.
        """
    
    traverse(root, 0)