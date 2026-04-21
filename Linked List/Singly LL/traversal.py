class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def printList(head):
    curr = head

    while(curr != None):
        print(curr.key, end="->")
        curr = curr.next

head = Node(10)
head.next = Node(20)
head.next.next = Node(30)

printList(head)

# nth node from last of linked list

def print_nth_from_last(head, n): # two pointer method
    if head is None:
        return None
    
    first = head
    second = head

    for _ in range(n):
        if second is None:
            return None
        second = second.next
    
    while second != None:
        first = first.next
        second = second.next
    
    return first.data