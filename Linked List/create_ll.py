"""
For creating a liniked list
dynamically, by user only,
so that user can create its
ow linked list, however he wants!
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def create_linked_list():
    ip = int(input("No. of Nodes: "))
    head = start_node = Node(0)

    for _ in range(ip):
        val = int(input("Node Data: "))
        node = Node(val)
        start_node.next = node
        start_node = start_node.next

    return head.next

def printList(head):
    curr = head

    while(curr != None):
        print(curr.data, end="->")
        curr = curr.next
    print("None")

head = create_linked_list()
printList(head)
