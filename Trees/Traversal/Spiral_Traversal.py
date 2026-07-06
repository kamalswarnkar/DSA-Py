"""
Spiral (Zig-Zag) Traversal

Print tree level-by-level, but reverse the traversal
direction after every level.

Level 1 : Left -> Right
Level 2 : Right -> Left
Level 3 : Left -> Right
...
"""

from collections import deque

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

"""
Method 1 (using Stack)
Perform normal BFS, but use a stack to reverse alternate levels

Time Complexity: O(N)
Space Complexity: O(W)

where,
N = number of nodes
W = maximum width of tree
"""

def printSpiral_I(root):
    if root is None:
        return
    
    q = deque()
    s = []
    rev = False

    q.append(root)

    while q:
        count = len(q)

        for _ in range(count):
            tmp = q.popleft()

            if rev:
                s.append(tmp.val)
            else:
                print(tmp.val, end=" ")
            
            if tmp.left:
                q.append(tmp.left)
            if tmp.right:
                q.append(tmp.right)
        
        if rev:
            while s:
                print(s.pop(), end=" ")
        
        rev = not rev

"""
Method 2 (using 2 Stack) - Generally considered the best implementation
Alternate between two stacks to naturally reverse each level

Time Complexity: O(N)
Space Complexity: O(W)

where,
N = number of nodes
W = maximum width of tree
"""

def printSpiral_II(root):
    if root is None:
        return
    
    s1 = []
    s2 = []

    s1.append(root)

    while s1 or s2:
        while s1:
            node = s1.pop()

            print(node.val, end=" ")

            if node.left:
                s2.append(node.left)
            if node.right:
                s2.append(node.right)
        
        while s2:
            node = s2.pop()

            print(node.val, end=" ")

            if node.right:
                s1.append(node.right)
            if node.left:
                s1.append(node.left)

"""
Method 3 (using height)
Print one level at a time while alternating the traversal direction

Time Complexity: O(N^2)
Space Complexity: O(H)

where,
N = number of nodes
H = maximum height of tree
"""

def height(root):
    if root is None:
        return 0
    
    lh = height(root.left)
    rh = height(root.right)

    return max(lh, rh) + 1

def printGivenLevel(root, lvl, ltr):
    if root is None:
        return
    
    if lvl == 1:
        print(root.val, end = " ")
    elif lvl > 1:
        if ltr:
            printGivenLevel(root.left, lvl - 1, ltr)
            printGivenLevel(root.right, lvl - 1, ltr)
        else:
            printGivenLevel(root.right, lvl - 1, ltr)
            printGivenLevel(root.left, lvl - 1, ltr)

def printSpiral_III(root):
    h = height(root)
    ltr = True # left to right traversal

    for i in range(1, h + 1):
        printGivenLevel(root, i, ltr)
        ltr = not ltr
