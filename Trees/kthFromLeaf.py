"""
Count the number of Special Nodes.

A Special Node is a node having at least one leaf node
in its subtree such that the distance between them is exactly 'k'.

Note:
A node is counted only once, even if multiple leaf nodes
are at distance k from it.

Idea:
1. Perform a DFS while maintaining the current root-to-node path.
2. Whenever a leaf is reached, find its k-th ancestor using the path.
3. Count the ancestor only if it hasn't been counted before.

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

def kthFromLeaf(root, k):
    path = [] # Stores the current root-to-node path
    visited = set() # Prevent counting the same ancestor multiple times
    count = 0

    def dfs(node):
        nonlocal count
        if node is None:
            return
        
        path.append(node) # append when going down the tree

        if node.left is None and node.right is None: # to reach to the leaf node
            if len(path) > k: # to make that k doesn't lie outside path or out of tree depth
                ancestor = path[-(k + 1)]
                if ancestor not in visited: # to make sure each node is counted only once
                    visited.add(ancestor)
                    count += 1
        
        dfs(node.left)
        dfs(node.right)

        path.pop() # pop when going up the tree
    
    dfs(root)

    return count