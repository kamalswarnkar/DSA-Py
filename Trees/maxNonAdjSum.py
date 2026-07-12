"""
Maximum Non-Adjacent Nodes Sum

Find the maximum sum of node values such that no two
adjacent nodes (parent-child) are selected together.

Idea:
1. For every node, compute two values:
    • Include: Maximum sum if the current node is selected.
    • Exclude: Maximum sum if the current node is not selected.
2. If the current node is included, its children cannot be included.
3. If the current node is excluded, each child may be either
   included or excluded, whichever gives a larger sum.

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

def getMaxSum(root):
    def dfs(node):
        if node is None:
            return (0, 0) # inc, exc
        
        left = dfs(node.left)
        right = dfs(node.right)

        inc = node.val + left[1] + right[1] # include
        exc = max(left[0], left[1]) + max(right[0], right[1]) # exclude

        return (inc, exc)
    
    inc, exc = dfs(root)

    return max(inc, exc)