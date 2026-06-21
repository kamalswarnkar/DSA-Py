"""
Maximum Width of Binary Tree

Width of a level = number of nodes present at that level.

Maximum Width = maximum number of nodes among all levels.

Approach:
Use Level Order Traversal (BFS).
For each level:
    1. Count the nodes currently in the queue.
    2. Update the maximum width.
    3. Process all nodes of that level.

Time Complexity: O(N)
Space Complexity: O(W)

where:
    N = total number of nodes
    W = maximum width of the tree
"""

from collections import deque as dq

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def maxWidth(root):
    if root is None:
        return 0
    
    q = dq()
    q.append(root)
    res = 0

    while q:
        count = len(q)

        for i in range(count):
            curr = q.popleft()

            if curr.left is not None:
                q.append(curr.left)
            
            if curr.right is not None:
                q.append(curr.right)
        
        res = max(res, count)
    
    return res