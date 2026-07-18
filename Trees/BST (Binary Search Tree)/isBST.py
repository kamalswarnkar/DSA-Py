"""
Check if a Binary Tree is a Binary Search Tree (BST)

A Binary Search Tree satisfies:
    Left Subtree < Root < Right Subtree

This file contains three approaches:

1. Inorder Traversal + List
2. Inorder Traversal + Previous Pointer
3. Range (Min-Max) Validation

Time Complexity:
    All Methods : O(N)

Space Complexity:
    Method I   : O(N)
    Method II  : O(H)
    Method III : O(H)

where,
N = number of nodes
H = height of the tree

Note:
Method II and Method III are the preferred interview solutions
as they avoid storing the entire inorder traversal.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isBST_I(root): # Inorder + List Method
    if root is None:
        return True
    
    inorder = []

    def traverse(node):
        if node is not None:
            traverse(node.left)
            inorder.append(node.val)
            traverse(node.right)
    
    traverse(root)

    for i in range(1, len(inorder)):
        if inorder[i - 1] > inorder[i]:
            return False
    
    return True

def isBST_II(root): # Inorder + Previous Pointer Method
    prev = None

    def inorder(node):
        nonlocal prev

        if node is None:
            return True
        
        if not inorder(node.left):
            return False
        
        if prev is not None and prev >= node.val:
            return False
        
        prev = node.val

        return inorder(node.right)
    
    return inorder(root)

def isBST_III(root): # Range(Min-Max) Method
    def helper(node, low, high):
        if node is None:
            return True
        
        if not (low < node.val < high):
            return False
        
        return helper(node.left, low, node.val) and helper(node.right, node.val, high)
    
    return helper(root, float("-inf"), float("inf"))