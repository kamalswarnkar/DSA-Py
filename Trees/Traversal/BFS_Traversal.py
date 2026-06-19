"""
BFS Traversal , a.k.a. Level Order Traversal
where all nodes of same level are printed 
together from left to right
"""

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def level_order(self, root):
        if root is None:
            return
        
        q = deque()
        q.append(root)

        while len(q) > 0:
            node = q.popleft()
            print(node.val, end=" ")

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
        