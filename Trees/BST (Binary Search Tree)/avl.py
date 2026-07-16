"""
AVL Tree (Self-Balancing Binary Search Tree)

An AVL Tree is a self-balancing Binary Search Tree (BST)
in which the height difference (Balance Factor) between the
left and right subtrees of every node is at most 1.

Balance Factor:
    Balance = Height(Left) - Height(Right)

Possible Balance Factors:
    -1, 0, 1  → Balanced
    < -1 or > 1 → Rotation required

Rotations:
1. Left Rotation  (RR Case)
2. Right Rotation (LL Case)
3. Left-Right Rotation (LR Case)
4. Right-Left Rotation (RL Case)

Note: 
Only the first unbalanced ancestor after insertion
needs to be rebalanced.

Time Complexity:
    Search    : O(log N)
    Insertion : O(log N)
    Deletion  : O(log N)

Space Complexity:
    O(H)

where,
N = number of nodes
H = height of the AVL Tree = O(log N)

Advantages:
• Guarantees O(log N) search, insertion and deletion.
• Prevents the BST from becoming skewed.
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTrees:
    def insert(self, root, key):
        if root is None:
            return Node(key)
        elif key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        
        root.height = 1 + max(self.getHeight(root.left), self.getHeight(root.right)) # Update the height of the current node after insertion.

        balance = self.getBalance(root) # Compute the balance factor to check whether rebalancing is needed.

        if balance < -1 and key > root.right.val: # Right-Right (RR) Case
            return self.leftRotate(root)
        
        if balance > 1 and key < root.left.val: # Left-Left (LL) Case
            return self.rightRotate(root)
        
        if balance > 1 and key > root.left.val: # Left-Right (LR) Case
            root.left = self.leftRotate(root.left)
            return self.rightRotate(root)
        
        if balance < -1 and key < root.right.val: # Right-Left (RL) Case
            root.right = self.rightRotate(root.right)
            return self.leftRotate(root)
        
        return root

    def leftRotate(self, z):
        y = z.right # pivot node
        T = y.left # subtree to be reassigned

        #perform rotation
        y.left = z
        z.right = T
        
        # Update heights after rotation
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y # Return the new root of this subtree

    def rightRotate(self, z):
        y = z.left # pivot node
        T = y.right # subtree to be reassigned

        #perform rotation
        y.right = z
        z.left = T
        
        # Update heights after rotation
        z.height = 1 + max(self.getHeight(z.left), self.getHeight(z.right))
        y.height = 1 + max(self.getHeight(y.left), self.getHeight(y.right))

        return y # Return the new root of this subtree

    def getHeight(self, root):
        if root is None:
            return 0
        
        return root.height

    def getBalance(self, root):
        if root is None:
            return 0
        
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        if root is None:
            return
        
        print(root.val, end=" ")
        self.preOrder(root.left)
        self.preOrder(root.right)