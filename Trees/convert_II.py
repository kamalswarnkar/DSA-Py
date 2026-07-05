"""
Construct a Binary Tree from given Inorder & Preorder of sequence

Idea:
1. Preorder always gives the current root.
2. Inorder divides the tree into left and right subtrees.
3. Recursively build left and right subtrees.

Time Complexity : O(N)
Space Complexity: O(N)

where:
N = number of nodes

Note: Binary Tree can be constructed using only (PreOrder & Inorder) or (InOrder & PostOrder)
      but not using (PreOrder & PostOrder) unless it is Full Binary Tree
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

pre_idx = 0 # curr index in preorder traversal
mp = {} # maps the node value -> index in inorder traversal

def buildMap(ino):
    global mp

    for i in range(len(ino)):
        mp[ino[i]] = i

def buildTree(pre, ino, i_start, i_end):
    if i_start > i_end: # when no nodes in left sub-tree
        return None
    
    global pre_idx

    root = Node(pre[pre_idx])
    pre_idx += 1

    if i_start == i_end: # no further children
        return root
    
    i = mp[root.val]

    """
    instead of using global variables like pre_idx, and mp
    we can wrap them inside to avoid using global var and 
    make function reusable, like this:

    mp = {v: i for i, v in enumerate(ino)}
    pre_idx = [0] # mutable integer
    """

    root.left = buildTree(pre, ino, i_start,  i - 1)
    root.right = buildTree(pre, ino, i + 1, i_end)

    return root

# always call buildMap first, otherwise buildTree will raise Key_Error