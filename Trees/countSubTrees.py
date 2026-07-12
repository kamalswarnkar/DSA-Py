"""
Count Subtrees with a Given Sum

Given a binary tree and an integer x, count the number
of subtrees whose sum of all node values equals x.

Idea:
1. Traverse the tree using postorder DFS.
2. Compute the sum of every subtree.
3. If the subtree sum equals x, increment the count.
4. Return the subtree sum to the parent.

Time Complexity : O(N)
Space Complexity: O(H)

where,
N = number of nodes
H = height of tree
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def countSubTrees(root, x):
    count = 0

    def dfs(node):
        nonlocal count
        if node is None:
            return 0
        
        left = dfs(node.left)
        right = dfs(node.right)

        subtree = node.val + left + right

        if subtree == x:
            count += 1
        
        return subtree
    
    dfs(root)

    return count