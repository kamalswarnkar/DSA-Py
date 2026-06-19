# height of tree (Binary Tree)

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def height(root):
    if root is None:
        return 0
    
    lh = height(root.left)
    rh = height(root.right)

    return max(lh, rh) + 1