"""
Check Children Sum Property

A binary tree satisfies the Children Sum Property if every
non-leaf node has a value equal to the sum of its children's values.

Rules:
• NULL child contributes 0.
• Every leaf node automatically satisfies the property.

Idea:
1. For every non-leaf node, compute the sum of its children.
2. If the sum differs from the node's value, return False.
3. Recursively verify the left and right subtrees.

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

def isSumProperty(root):
    def dfs(node):
        if node is None:
            return True
        
        if not node.left and not node.right:
            return True
        
        v, l, r = node.val, 0, 0

        if node.left:
            l = node.left.val
        if node.right:
            r = node.right.val
        
        if v != (l + r):
            return False
        
        return dfs(node.left) and dfs(node.right)
    
    return dfs(root)