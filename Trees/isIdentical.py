"""
Two trees are identical when they have the same data and 
the arrangement of the data is also same.

Time Complexity: O(N)
Space Complexity: O(H)

where,
N = no. of nodes in smaller tree
H = height of tree
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isIdentical(r1, r2):
    if not r1 and not r2:
        return True
    
    if not r1 or not r2:
        return False
    
    if r1.val != r2.val:
        return False
    
    return isIdentical(r1.left, r2.left) and isIdentical(r1.right, r2.right)
