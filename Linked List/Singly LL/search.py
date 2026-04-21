class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def search(head, val):
    curr = head
    pos = 1

    while(curr != None):
        if(curr.key == val):
            return pos
        curr = curr.next
        pos += 1

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)

print(search(head, 30))