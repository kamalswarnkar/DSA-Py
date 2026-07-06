"""
Counting total no. of nodes in a complete binary tree

Time Complexity:
    Naive  : O(N)
    Optimal: O((log N)^2)

Space Complexity:
    O(log N)

where:
N = number of nodes
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def count_I(root): # naive solution
    if root is None:
        return 0
    
    return 1 + count_I(root.left) + count_I(root.right)

def count_II(root): # optimal solution
    lh, rh = 0, 0
    curr = root

    while curr:
        lh += 1
        curr = curr.left
    
    curr = root

    while curr:
        rh += 1
        curr = curr.right

    if lh == rh:
        return (1 << lh) - 1 # for perfect binary tree (i.e., same no of nodes in left and right subtree) - (2)^lh - 1
    
    return 1 + count_II(root.left) + count_II(root.right)