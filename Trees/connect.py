"""
Connect Nodes at the Same Level

For every node, set its 'nextRight' pointer to the
immediate node on its right in the same level.

If a node is the last node of its level,
its 'nextRight' pointer remains None.

Idea:
1. Perform a level-order traversal (BFS).
2. Store all nodes of the current level.
3. Connect each node to the next node in the level.
4. Clear the list and repeat for the next level.

Time Complexity : O(N)
Space Complexity: O(W)

where,
N = number of nodes
W = maximum width of the tree
"""
from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.nextRight = None

def connect(root):
    lvl = []

    def bfs(node):
        if node is None:
            return
        
        q = deque()
        q.append(node)

        while len(q) > 0:
            count = len(q)

            for _ in range(count):
                curr = q.popleft()

                lvl.append(curr)

                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            for i in range(len(lvl) - 1):
                lvl[i].nextRight = lvl[i + 1]
            
            lvl.clear()
        
    bfs(root)

    return root