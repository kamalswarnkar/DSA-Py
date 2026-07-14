"""
Binary Search Tree (BST)

A Binary Search Tree is a binary tree in which:
    • All values in the left subtree are smaller than the node.
    • All values in the right subtree are greater than or equal to the node.
    • Both left and right subtrees are also Binary Search Trees.

This implementation supports the following operations:
1. Create a BST
2. Recursive Insertion
3. Iterative Insertion
4. Recursive Search
5. Iterative Search
6. Deletion

Deletion Cases:
1. Node has no children (Leaf)
2. Node has one child
3. Node has two children
   → Replace the node with its inorder successor
     (smallest value in the right subtree).

Time Complexity (Average):
    Insertion : O(log N)
    Search    : O(log N)
    Deletion  : O(log N)

Time Complexity (Worst Case):
    Insertion : O(N)
    Search    : O(N)
    Deletion  : O(N)

Space Complexity:
    Recursive Operations : O(H)
    Iterative Operations : O(1)

where,
N = number of nodes
H = height of the BST

Note:
A BST becomes skewed for sorted input, causing the height
to become O(N). Self-balancing BSTs (AVL Tree, Red-Black Tree)
avoid this issue by maintaining a height of O(log N).
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert_rec(self, val): # recursive method
        def ins(node):
            if node is None:
                return Node(val)
            
            if val < node.val:
                node.left = ins(node.left)
            else:
                node.right = ins(node.right)
            
            return node

        self.root = ins(self.root)
    
    def insert_itr(self, val): # iterative method
        def ins(node): # its an iterative approach so no need for this helper function, its just to maintain the structure and symmetry with other functions
            if node is None:
                return Node(val)
            
            par = None
            curr = node
            while curr:
                par = curr

                if curr.val > val:
                    curr = curr.left
                else:
                    curr = curr.right   
                
            if par is None:
                return Node(val)
            elif par.val > val:
                par.left = Node(val)
            else:
                par.right = Node(val)

            return node

        self.root = ins(self.root)              

    def create(self):
        while True:
            ip = input()

            if ip == '#':
                break

            self.insert_rec(int(ip))
    
    def search_rec(self, key): # recursive method
        def search(node):
            if node is None:
                return False
            elif node.val == key:
                return True
            elif node.val > key:
                return search(node.left)
            else:
                return search(node.right)
        
        return search(self.root)
    
    def search_itr(self, key): # iterative method
        def search(node):
            while node is not None:
                if node.val == key:
                    return True
                elif node.val > key:
                    node = node.left
                else:
                    node = node.right
            
            return False
        
        return search(self.root)

    def delete(self, key):
        def getSucc(curr):
            while curr.left:
                curr = curr.left
            return curr.val
        
        def delNode(node, key):
            if node is None:
                return None
            
            if node.val > key:
                node.left = delNode(node.left, key)
            elif node.val < key:
                node.right = delNode(node.right, key)
            else: # if same 
                if node.left is None:
                    return node.right
                elif node.right is None:
                    return node.left
                else:
                    """
                    in case, it has both left and right node, then we will find its successor 
                    to be replaced as root node, which has to be greater than left subtree, 
                    which is why we'lll find it in right subtree
                    """
                    succ = getSucc(node.right) # Returns the inorder successor (smallest value in the right subtree). 
                    node.val = succ
                    """
                    we are not actually deleting the node, we are the replacing the valu of root 
                    node ith its successor's val, and after there is no need for that successor
                    node to be there, so we'll have to delete that successor node at last, as well
                    """
                    node.right = delNode(node.right, succ)
            return node
        
        self.root = delNode(self.root, key)
