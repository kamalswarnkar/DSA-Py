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

# Basic
class Tree_1: # Normal BFS - Visits nodes level-by-level but prints them as a single sequence.
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

# Null Marker
class Tree_2: # NULL Marker BFS - Uses None as a level separator to print each level on a new line.
    def level_order(self, root):
        if root is None:
            return
        
        q = deque()
        q.append(root)
        q.append(None)

        while len(q) > 1:
            node = q.popleft()

            if node is None:
                print()
                q.append(None)
                continue

            print(node.val, end=" ")

            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)

# Most Preferred Method
class Tree_3: #Sized Based BFS - Processes one level at a time using the current queue size.
    def level_order(self, root):
        if root is None:
            return
        
        q = deque()
        q.append(root)

        while len(q) > 0:
            count = len(q)
            for i in range(count):
                node = q.popleft()

                print(node.val, end=" ")

                if node.left is not None:
                    q.append(node.left)
                if node.right is not None:
                    q.append(node.right)
            
            print()