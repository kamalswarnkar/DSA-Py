class Node:
    def __init__(self, key):
        self.key = key
        self.next = None


tmp_1 = Node(10)
tmp_2 = Node(20)
tmp_3 = Node(30)
tmp_4 = Node(40)
tmp_5 = Node(50)
tmp_6 = Node(60)
tmp_7 = Node(70)
tmp_8 = Node(80)
tmp_9 = Node(90)
tmp_10 = Node(100)

tmp_1.next = tmp_2
tmp_2.next = tmp_3
tmp_3.next = tmp_4
tmp_4.next = tmp_5
tmp_5.next = tmp_6
tmp_6.next = tmp_7
tmp_7.next = tmp_8
tmp_8.next = tmp_9
tmp_9.next = tmp_10

#traversal
def printList(head):
    curr = head

    while(curr != None):
        print(curr.key, end="->")
        curr = curr.next

# deleting head (1st node)
def delete_head(head):
    if head is None:
        return None
    
    return head.next

#printList(delete_head(tmp_1))

# deleting last node

def delete_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None
    
    curr = head

    while curr.next.next != None:
        curr = curr.next

    curr.next = None

    return head

printList(delete_tail(tmp_1))