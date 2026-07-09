"""
Constructing a Binary Tree

Here, we have given an array parent[] where each index represents a 
node and parent[i] gives the parent’s index, with -1 indicating the root.

Note: If two elements have the same parent, the one that appears first 
in the array will be the left child and the other is the right child.

Time Complexity: O(N)
Space Complexity: O(N)
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def createTree(parent): # 'parent' is the list of index's parent's index
    n = len(parent)

    if not n:
        return
    
    nodes = [Node(i) for i in range(n)]
    root = None

    for i in range(n):
        if parent[i] == -1:
            root = nodes[i]
        elif nodes[parent[i]].left is None:
            nodes[parent[i]].left = nodes[i]
        else:
            nodes[parent[i]].right = nodes[i]
    
    return root