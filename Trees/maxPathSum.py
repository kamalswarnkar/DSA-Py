"""
Maximum Path Sum in a Binary Tree

Find the maximum sum of values along any path in the tree.
The path may start and end at any node.

Note:
The tree may contain negative values.

Idea:
1. Recursively compute the maximum downward path sum from each node.
2. Ignore negative contributions from subtrees.
3. At every node, consider the path passing through it.
4. Keep updating the global maximum path sum.

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

def findMaxSum(root):
    res = float("-inf")

    def dfs(node):
        nonlocal res
        if node is None:
            return 0
        
        left = max(0, dfs(node.left)) # ignore negative contribution from left subtree
        right = max(0, dfs(node.right)) # ignore negative contribution from right subtree

        res = max(res, left + right + node.val)

        return node.val + max(left, right) # return the the best downward path
    
    dfs(root)

    return res
    