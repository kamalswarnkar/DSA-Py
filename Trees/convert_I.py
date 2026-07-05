"""
Convert a Binary Tree into a Doubly Linked List (DLL).

The DLL is created in Inorder Traversal order:
    Left -> Root -> Right

left  pointer -> previous node in DLL
right pointer -> next node in DLL

Time Complexity: O(N)
Space Complexity: O(H)

where:
    N = number of nodes
    H = height of tree
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

prev = None

def convert(root):
    if root is None:
        return root
    
    head = convert(root.left)

    global prev

    if prev is None:
        head = root
    else:
        prev.right = root
        root.left = prev
    
    prev = root

    convert(root.right)

    return head