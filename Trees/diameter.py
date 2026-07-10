"""
Diameter of a Binary Tree

Diameter = maximum number of nodes on any path
between two nodes.

Method I:
    Compute height for every node.

Method II:
    Compute height and diameter together in one DFS.

Time Complexity:
    Method I : O(N²)
    Method II: O(N)

Space Complexity:
    O(H)

where:
N = number of nodes
H = height of tree
"""

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

def diameter_I(root): # Naive Solution
    if root is None:
        return 0
    
    d1 = 1 + height(root.left) + height(root.right)
    d2 = diameter_I(root.left)
    d3 = diameter_I(root.right)

    return max(d1, d2, d3)

"""
This function is efficient and mainly returns the height,
but in the process it sets the 'res' which is the diameter
"""
res = 0
def diameter_II(root):
    if root is None:
        return 0
    
    lh = diameter_II(root.left)
    rh = diameter_II(root.right)

    global res
    res = max(res, 1 + lh + rh)
    """
    diameter - Longest path between any two nodes
    so it can either be taken as max no of nodes, or max no. of edges

    for nodes - (1 + lh + rh)
    for edges - (lh + rh)
    """

    return 1 + max(lh, rh)