"""
Create a Binary Search Tree (BST)

A Binary Search Tree satisfies:
    • Left subtree contains smaller values.
    • Right subtree contains greater values.

Idea:
1. Read values one by one.
2. Insert each value into its correct position.
3. Stop when '#' is entered.

Time Complexity:
    Average : O(N log N)
    Worst   : O(N²)

Space Complexity:
    O(H)

where,
N = number of nodes
H = height of the BST
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
    