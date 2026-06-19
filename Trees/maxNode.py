# finding the node in tree with maximum/highest value

import math

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getMax(root):
    if root is None:
        return -math.inf
    
    lm = getMax(root.left)
    rm = getMax(root.right)

    return max(root.val, lm, rm)