"""
Serialization & Deserialization of a Binary Tree

Serialization:
    Convert a binary tree into a linear sequence
    while preserving its structure.

Deserialization:
    Reconstruct the original binary tree from
    the serialized sequence.

Idea:
1. Perform a preorder traversal.
2. Store every node value.
3. Store a special marker (EMPTY) for NULL nodes.
4. During deserialization, read values in preorder
   and recursively rebuild the tree.

Note: Preorder is used because the root must be created before
      its left and right subtrees during reconstruction.

Time Complexity : O(N)
Space Complexity: O(N)

where:
N = number of nodes
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

EMPTY = '#' # marker for representing a NULL node
index = 0 # curr position while deserializing

def serialize(root, arr):
    if root is None:
        arr.append(EMPTY)
        return
    
    arr.append(root.val)
    serialize(root.left, arr)
    serialize(root.right, arr)

def deserialize(arr):
    global index
    if index == len(arr):
        return None
    
    val = arr[index]
    index += 1

    if val == EMPTY:
        return None
    
    root = Node(val)
    root.left = deserialize(arr)
    root.right = deserialize(arr)

    return root

# everytime, before calling deserialize function, make sure to reset the global index to ZERO '0'