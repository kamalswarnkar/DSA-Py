"""
Ceil in a Binary Search Tree

The ceil of a key is the lowest value in the BST
that is greater than or equal to the given key.

This file contains:
1. Recursive solution
2. Iterative solution

(Floor in BST is the mirror problem of this problem)

Time Complexity : O(H)
Space Complexity:
    Recursive : O(H)
    Iterative : O(1)

where,
N = number of nodes
H = height of the BST

Note:
If no ceil exists (all node values are lesser than the key),
the function returns None (iterative) or ∞ (recursive), depending
on the chosen implementation.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def ceil_rec(root, key): # recursive method
    ans = float("inf")

    def helper(node):
        nonlocal ans

        if node is None:
            return
        
        if node.val == key:
            ans = node.val
            return
        elif node.val < key:
            helper(node.right)
        else:
            ans = node.val
            helper(node.left)
        
        return
    
    helper(root)

    return ans

def ceil_ite(root, key): # iterative method
    ans = None
    while root is not None:
        if root.val == key:
            return root.val
        elif root.val > key:
            ans = root.val
            root = root.left
        else:
            root = root.right
    
    return ans