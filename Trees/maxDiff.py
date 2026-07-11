"""
Maximum Difference Between an Ancestor and a Descendant

Find the maximum value of:

    Ancestor.val - Descendant.val

where the ancestor must lie on the path from the root
to the descendant.

Idea:
1. Traverse the tree using postorder DFS.
2. Every subtree returns its minimum node value.
3. For each node, compute the difference between
   the current node and the minimum descendant.
4. Keep updating the maximum difference.

Time Complexity : O(N)
Space Complexity: O(H)

where:
N = number of nodes
H = height of tree
"""

class Node:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None

def maxDiff(root):
    max_diff = float('-inf')

    def dfs(node):
        nonlocal max_diff

        if node is None:
            return float('inf')
        
        left_min = dfs(node.left)
        right_min = dfs(node.right)

        descendent_min = min(left_min, right_min)

        if descendent_min != float('inf'):
            max_diff = max(max_diff, node.val - descendent_min)
        
        subtree_min = min(node.val, descendent_min)

        return subtree_min
    
    dfs(root)

    return max_diff