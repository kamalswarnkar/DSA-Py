"""
Check if One Binary Tree is a Subtree of Another

A tree S is a subtree of T if there exists a node in T
such that the subtree rooted at that node is identical to S.

Two trees are identical if:
    • Their structures are the same.
    • Corresponding node values are equal.

Idea:
1. Traverse every node of tree T.
2. At each node, check whether the subtree rooted there
   is identical to tree S.
3. If a match is found, return True.
4. Otherwise, continue searching in the left and right subtrees.

Time Complexity : O(N*M)
Space Complexity: O(H)

where,
N = number of nodes in tree T
M = number of nodes in tree S
H = height of tree T

*Note: By serializing both trees and then checking whether the serialized string of S 
       is a substring of T (using algorithms like KMP or Rabin–Karp), the complexity 
       can be improved to approximately:

        Time: O(N + M)
        Space: O(N + M)
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def isSame(a, b):
    if not a and not b:
        return True
    
    if (a and not b) or (not a and b):
        return False
    
    if a.val != b.val:
        return False
    
    return isSame(a.left, b.left) and isSame(a.right, b.right)

def isSubTree(root1, root2):
    if root2 is None:
        return True
    
    if root1 is None:
        return False
    
    if isSame(root1, root2):
        return True
    
    return isSubTree(root1.left, root2) or isSubTree(root1.right, root2)