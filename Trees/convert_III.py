"""
Convert a Singly Linked List into a Complete Binary Tree.

Idea:
1. The first linked list node becomes the root.
2. Use a queue to keep track of tree nodes whose children
   are yet to be assigned.
3. For each parent, assign the next linked list node as
   the left child and the following node as the right child.
4. Continue until all linked list nodes are processed.

Time Complexity: O(N)
Space Complexity: O(N)

where,
N = number of nodes
"""

from collections import deque as dq

class LinkedList:
    def __init__(self, val):
        self.val = val
        self.next = None

class Node: # for tree
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def convert(head):
    if head is None:
        return
    
    root = Node(head.val)
    q = dq()
    q.append(root)

    curr = head.next

    while curr:
        par = q.popleft()

        par.left = Node(curr.val)
        q.append(par.left)

        curr = curr.next
        if curr:
            par.right = Node(curr.val)
            q.append(par.right)
            curr = curr.next
    
    return root