"""
we'll find either the exact or just smaller number than the given number
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def floor(root, key):
    ans = float("-inf")

    def helper(node):
        nonlocal ans

        if node is None:
            return
        
        if node.val == key:
            ans = node.val
            return
        elif node.val < key:
            ans = node.val
            helper(node.right)
        else:
            helper(node.left)
        
        return
    
    helper(root)

    return ans
