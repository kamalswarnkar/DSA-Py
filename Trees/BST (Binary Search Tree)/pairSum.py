"""
Find a Pair with a Given Sum in a BST

Determine whether there exists a pair of nodes in the BST
whose sum equals the given target value.

Idea:
Perform an inorder traversal while storing previously
visited node values in a hash set.

For every node:
1. Compute the required complement.
2. If the complement already exists in the set,
   a valid pair is found.
3. Otherwise, store the current node value and continue.

Time Complexity : O(N)
Space Complexity: O(N)

where,
N = number of nodes
H = height of the tree

Note:
The BST property is not directly used here; the same
approach works for any binary tree.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isPairSum(root, X):
    s = set()
    
    def helper(node):
        nonlocal s
        if node is None:
            return False
        
        if helper(node.left):
            return True
        
        if X - node.val in s:
            print(f"The Desired Pair - {node.val} & {X - node.val}")
            return True
        else:
            s.add(node.val)
        
        return helper(node.right)
    
    return helper(root)