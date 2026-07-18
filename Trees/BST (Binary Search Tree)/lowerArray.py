"""
Count Smaller Elements on the Right

For every element in the array, count how many elements
to its right are smaller than it.

Idea:
Traverse the array from right to left while inserting
elements into an augmented BST.

Each node stores:
    leftSize = Number of nodes in its left subtree.

During insertion:
1. If the current value is smaller than or equal to the node,
   move left and increment leftSize.
2. Otherwise, all nodes in the left subtree and the current
   node are smaller than the current value, so add
   (leftSize + 1) to the answer and move right.

Time Complexity:
    Average : O(N log N)
    Worst   : O(N²)

Space Complexity:
    O(N)

where,
N = number of elements

Note:
The worst case occurs when the BST becomes skewed.
Using a self-balancing BST (AVL/Red-Black Tree) guarantees
O(N log N).
"""

class Node: # Augmented BST
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.leftSize = 0

def lowerArray(arr):
    n = len(arr)
    op = [-1] * n
    root = None

    def insert(node, x):
        nonlocal cnt

        if node is None:
            return Node(x)
        
        if x <= node.val:
            node.leftSize += 1
            node.left = insert(node.left, x)
        else:
            cnt += node.leftSize + 1
            node.right = insert(node.right, x)
        
        return node

    for i in range(n - 1, -1, -1):
        cnt = 0
        root = insert(root, arr[i])
        op[i] = cnt
    
    return op