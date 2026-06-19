# printingall nodes at same distance - 'k' from root node

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def print_node_at_K(root, k):
    if root is None:
        return
    
    if k == 0:
        print(root.val, end=" ")
        return
    
    print_node_at_K(root.left, k - 1)
    print_node_at_K(root.right, k - 1)