"""
Recover a Binary Search Tree

Two nodes of a BST are mistakenly swapped.
Find the two nodes and swap their values to restore
the BST without changing its structure.

Idea:
An inorder traversal of a BST produces a sorted sequence.

Whenever the previous node is greater than the current node,
an inversion is found.

Cases:
1. Adjacent swapped nodes:
      One inversion

2. Non-adjacent swapped nodes:
      Two inversions

The first incorrect node is the previous node of the
first inversion.

The second incorrect node is the current node of the
last inversion.

Time Complexity : O(N)
Space Complexity: O(H)

where,
N = number of nodes
H = height of the tree
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def fixBST(root):
    prev, first, second = None, None, None

    def traversal(node):
        nonlocal prev, first, second

        if node is None:
            return
        
        traversal(node.left)

        if prev is not None and prev.val > node.val:
            if first is None:
                first = prev

            second = node
        
        prev = node

        traversal(node.right)
    
    traversal(root)

    first.val, second.val = second.val, first.val