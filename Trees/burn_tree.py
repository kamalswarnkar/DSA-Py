"""
Minimum Time to Burn a Binary Tree

A fire starts from a given target node.

Every second, the fire spreads to:
    • Left child
    • Right child
    • Parent

Idea:
1. Store the parent of every node.
2. Locate the target node.
3. Perform DFS from the target while moving in
   all three directions (left, right, parent).
4. The farthest reachable node determines
   the minimum time to burn the entire tree.

Time Complexity : O(N)
Space Complexity: O(N)

where:
N = number of nodes
"""

target_node = None
NEG_INF = float('-inf')

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def getParent(root, parent, par):
    if root is None:
        return
    
    par[root] = parent

    getParent(root.left, root, par)
    getParent(root.right, root, par)

def getNode(root, leaf):
    global target_node

    if root is None:
        return
    
    if root.val == leaf:
        target_node = root
        return
    
    getNode(root.left, leaf)
    getNode(root.right, leaf)

def getMaxDist(target, dist, visited, par):
    if target is None:
        return dist - 1
    
    if target in visited:
        return NEG_INF
    
    visited.add(target)

    a1 = a2 = a3 = NEG_INF

    a1 = getMaxDist(target.left, dist + 1, visited, par)
    a2 = getMaxDist(target.right, dist + 1, visited, par)
    a3 = getMaxDist(par[target], dist + 1, visited, par)

    return max(a1, a2, a3)


def burnTree(root, leaf): # leaf is just the value of the target node, and not the node itself
    global target_node
    target_node = None # again initaied to None, so that on case of multiple calls of this function, the older val of target node does not persist

    par = {} # mapping of node to parent
    getParent(root, None, par) 

    getNode(root, leaf) # traversing to  target node / leaf and storing it (complete node, not just value) in global var - 'target_node'

    visited = set() # tracking all the nodes which are already visited once

    time = getMaxDist(target_node, 0, visited, par)

    return time