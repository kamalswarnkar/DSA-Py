"""
In DFS, we can traverse the trees in 3 ways: 
i. InOrder, ii. PreOrder, and iii. PostOrder

Inorder: Left -> Root -> Right
Preorder: Root -> Left -> Right
Postorder: Left -> Right -> Root
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def preorder(self, root):
        if root is not None:
            print(root.val, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)
    
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=" ")