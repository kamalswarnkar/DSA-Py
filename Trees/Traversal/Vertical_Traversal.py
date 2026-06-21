"""
Vertcal Traversal using BFS where Nodes having the same 
horizontal distance belong to the same vertical column.

         1(0)
       /   \
     2(-1)  3(1) 
   /   \
  4(-2) 5(0)

Traversal:
4 
2 
1 5 
3

Time Complexity: O(N + K log K)
Space Complexity: O(N)

where,
N = total no. of nodes, 
K = no. of unique vertical cols.
"""

import collections

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def vertical_traversal(root): 
    if root is None:
        return
    
    mp = {}
    q = collections.deque()
    q1 = collections.deque()

    q.append(root)
    q1.append(0)
    
    while len(q) > 0:
        curr = q.popleft()
        hd = q1.popleft()
        
        if mp.get(hd) is None:
            mp[hd] = []

        mp[hd].append(curr.val)
        
        if curr.left is not None:
            q.append(curr.left)
            q1.append(hd - 1)

        if curr.right is not None:
            q.append(curr.right)
            q1.append(hd + 1)
    
    sorted_mp = collections.OrderedDict(sorted(mp.items()))

    for i in sorted_mp.values():
        for j in i:
            print(j, end=" ")
        
        print()

def topView(root): # Keeps only the first node seen at that $hd$ (highest level).
    if root is None:
        return
    
    mp = {}
    q = collections.deque([(root, 0)]) # update - no need to maintain 2 seperate queues
    
    while q:
        curr, hd = q.popleft()
        
        if hd not in mp:
            mp[hd] = curr.val
        
        if curr.left is not None:
            q.append((curr.left, hd - 1))

        if curr.right is not None:
            q.append((curr.right, hd + 1))
    
    for i in sorted(mp):
        print(mp[i], end=" ")
    print()

def bottomView(root): # Keeps overwriting so only the last node seen remains (lowest level).
    if root is None:
        return
    
    mp = {}
    q = collections.deque([(root, 0)])
    
    while len(q) > 0:
        curr, hd = q.popleft()
        
        mp[hd] = curr.val
        
        if curr.left is not None:
            q.append((curr.left, hd - 1))

        if curr.right is not None:
            q.append((curr.right, hd + 1))
    
    for i in sorted(mp):
        print(mp[i], end=" ")
    print()