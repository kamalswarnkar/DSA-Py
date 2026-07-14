"""
Floor in a Binary Search Tree

The floor of a key is the greatest value in the BST
that is less than or equal to the given key.

This file contains:
1. Recursive solution
2. Iterative solution

Time Complexity : O(H)
Space Complexity:
    Recursive : O(H)
    Iterative : O(1)

where,
N = number of nodes
H = height of the BST

Note:
If no floor exists (all node values are greater than the key),
the function returns None (iterative) or -∞ (recursive), depending
on the chosen implementation.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def floor_rec(root, key): # recursive method
    ans = float("-inf")

    def helper(node):
        nonlocal ans

        if node is None:
            return
        
        if node.val == key:
            ans = node.val
            return
        elif node.val < key:
            ans = node.val
            helper(node.right)
        else:
            helper(node.left)
        
        return
    
    helper(root)

    return ans

def floor_ite(root, key): # iterative method
    ans = None
    while root is not None:
        if root.val == key:
            return root.val
        elif root.val > key:
            root = root.left
        else:
            ans = root.val
            root = root.right
    
    return ans