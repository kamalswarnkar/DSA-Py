"""
Construct a Binary Tree from given (Inorder & Preorder) or (Inorder & Postorder) of sequence

Idea(Inorder & Preorder):
1. Preorder always gives the current root.
2. Inorder divides the tree into left and right subtrees.
3. Recursively build left and right subtrees.

Idea(Inorder & Postorder):
1. Postorder always gives the current root (last element).
2. Inorder divides the tree into left and right subtrees.
3. Since postorder is traversed backwards, build the
   right subtree before the left subtree.

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
post_idx = -1 # curr index in postorder traversal
mp = {} # maps the node value -> index in inorder traversal

def buildMap(ino):
    global mp
    mp.clear()

    for i in range(len(ino)):
        mp[ino[i]] = i

def buildTreePre(pre, ino, i_start, i_end):
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

    root.left = buildTreePre(pre, ino, i_start,  i - 1)
    root.right = buildTreePre(pre, ino, i + 1, i_end)

    return root

def buildTreePost(post, ino, i_start, i_end):
    if i_start > i_end: # when no nodes in left sub-tree
        return None
    
    global post_idx

    root = Node(post[post_idx])
    post_idx -= 1

    if i_start == i_end: # no further children
        return root
    
    i = mp[root.val]

    """
    instead of using global variables like post_idx, and mp
    we can wrap them inside to avoid using global var and 
    make function reusable, like this:

    mp = {v: i for i, v in enumerate(ino)}
    post_idx = [len(post) - 1] # mutable integer
    """

    # right subtree first
    root.right = buildTreePost(post, ino, i + 1, i_end)
    root.left = buildTreePost(post, ino, i_start,  i - 1)

    return root

# always call buildMap first, otherwise buildTreePre, and buildTreePost will raise Key_Error
# also in case of multiple calls of any of buildTreePre or buildTreePost, make sure to reset the pre_idx, post_idx