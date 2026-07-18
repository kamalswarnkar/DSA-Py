"""
Kth Smallest Element in a BST

Each node stores the number of nodes in its left subtree (lcount).

Idea:
1. If k == lcount + 1, the current node is the kth smallest.
2. If k <= lcount, search the left subtree.
3. Otherwise, search the right subtree with
   k reduced by (lcount + 1).

Time Complexity : O(H)
Space Complexity: O(H)

where,
N = number of nodes
H = height of the BST

Note:
The lcount field must be maintained during every insertion
(and deletion, if supported).
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.lcount = 0 # Number of nodes in the left subtree

def insert(root, x):
    if root is None:
        return Node(x)
    
    if x < root.val:
        root.lcount += 1
        root.left = insert(root.left, x)
    else:
        root.right = insert(root.right, x)

    return root  

def kthSmallest(root, k):
    if root is None:
        return
    
    count = root.lcount + 1 # Number of nodes that come before (and including) current node

    if count == k:
        return root
    
    if count > k:
        return kthSmallest(root.left, k)
    
    return kthSmallest(root.right, k - count)