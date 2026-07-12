"""
Mirror Binary Tree

This file covers two related problems:

1. Check whether two binary trees are mirror images.
2. Convert a binary tree into its mirror image.

Mirror Trees:
Two trees are mirrors if:
    • Their root values are equal.
    • Left subtree of one tree is the mirror of the
      right subtree of the other tree.

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

def isMirror(r1, r2):
    if not r1 and not r2:
        return True
        
    if (r1 and not r2) or (not r1 and r2):
        return False
    
    if r1.val != r2.val:
        return False
        
    return isMirror(r1.left, r2.right) and isMirror(r1.right, r2.left)

def mirror(root):
    if root is None:
        return
    
    root.left, root.right = root.right, root.left

    mirror(root.left)
    mirror(root.right)