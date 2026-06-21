"""
This program is to determine whether the tree is balanced or not.

A height balanced binary tree is a binary tree in which the height 
of the left subtree and right subtree of any node does not differ 
by more than 1 and both the left and right subtree are also height 
balanced.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isBalancedMain(root):
    if isBalanced(root) == -1:
        return False
    
    return True

def isBalanced(root):
    if root is None:
        return 0
    
    lh = isBalanced(root.left)
    
    if lh == -1:
        return -1
    
    rh = isBalanced(root.right)

    if rh == -1:
        return -1
    
    if abs(lh - rh) > 1:
        return -1
    
    return max(lh, rh) + 1