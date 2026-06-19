# size (no. of nodes in) of a tree

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def size(root):
    if root is None:
        return 0
    
    ls = size(root.left)
    rs = size(root.right)

    return ls + rs + 1