"""
Vertical Width of a Binary Tree

The vertical width of a binary tree is the total number of unique
vertical lines (or columns) that pass through all the nodes of the
tree. If multiple nodes align vertically on the same column, they
are counted together as a single line.

Time Complexity : O(N)
Space Complexity: O(H)

where:
N = number of nodes
H = height of tree
"""

def lenUtil(root, mm, curr):
    if root is None:
        return
    
    if mm[0] > curr:
        mm[0] = curr
    if mm[1] < curr:
        mm[1] = curr
    
    lenUtil(root.left, mm, curr - 1)
    lenUtil(root.right, mm, curr + 1)

def verticalWidth(root):
    if root is None:
        return 0
    
    minMax= [0, 0]

    lenUtil(root, minMax, 0)

    return abs(minMax[0]) + minMax[1] + 1