import random
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None
        self.random = None
    
def clone(head):
    curr = head
    while curr:
        next = curr.next
        curr.next = Node(curr.key)
        curr.next.next = next
        curr = next
    
    curr = head
    while curr:
        curr.next.random = curr.random.next if curr.random else None
        curr = curr.next.next
    
    h = head.next
    clone = h
    curr = head
    while curr:
        curr.next = curr.next.next
        clone.next = None if clone.next == None else clone.next.next
        clone = clone.next
        curr = curr.next

    return h 