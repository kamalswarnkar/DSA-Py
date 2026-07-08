"""
Left View of a Binary Tree - The set of all nodes that are
visible when the tree is viewed from the left side.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def leftView(root):
    max_lvl = 0
    
    def traverse(node, lvl):
        nonlocal max_lvl

        if node is None:
            return
        
        if lvl == max_lvl:
            print(node.val, end=" ")
            max_lvl += 1
        
        traverse(node.left, lvl + 1)
        traverse(node.right, lvl + 1)
    
    traverse(root, 0)