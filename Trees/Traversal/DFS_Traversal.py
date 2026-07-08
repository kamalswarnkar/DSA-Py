"""
In DFS, we can traverse the trees in 3 ways: 
i. InOrder, ii. PreOrder, and iii. PostOrder

Inorder: Left -> Root -> Right
Preorder: Root -> Left -> Right
Postorder: Left -> Right -> Root

for all traversals:

Time Complexity: O(N)
Auxiliary Space:
    Recursive  -> O(H)
    Iterative  -> O(H)

where,
N = number of nodes
H = height of tree
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Tree:
    def preorder(self, root):
        if root is not None:
            print(root.val, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self, root):
        if root is not None:
            self.inorder(root.left)
            print(root.val, end=" ")
            self.inorder(root.right)
    
    def postorder(self, root):
        if root is not None:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.val, end=" ")
    
    def itrPreorder(self, root): # iterative preorder traversal
        if root is None:
            return
        
        st = [root]
        
        while len(st) > 0:
            curr = st.pop()
            print(curr.val, end=" ")
            # first right then left coz it will be reversed in stack
            if curr.right:
                st.append(curr.right)
            if curr.left:
                st.append(curr.left)
    
    def itrPreorder_II(self, root): # iterative preorder traversal (space optimized)
        if root is None:
            return
        
        st = []
        curr = root

        while st or curr != None:
            while curr != None:
                print(curr.val, end=" ")
                if curr.right:
                    st.append(curr.right)
                curr = curr.left
            
            if st:
                curr = st.pop()

    def itrInorder(self, root): # iterative inorder traversal
        if root is None:
            return
        
        st = []
        curr = root

        while st or curr:
            while curr:
                st.append(curr)
                curr = curr.left

            curr = st.pop()
            print(curr.val, end=" ")

            curr = curr.right
    