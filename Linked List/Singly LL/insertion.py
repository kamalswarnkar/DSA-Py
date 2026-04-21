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

new_val = 45

#insert at beginning
def insert_at_beginning(head, val):
    tmp = Node(val)
    tmp.next = head
    return tmp

#insert at end
def insert_at_end(head, val):
    tmp = Node(val)

    if head is None:
        return tmp

    curr = head
    while curr.next is not None:
        curr = curr.next

    curr.next = tmp
    return head

#insert at given pos
def insert(head, val, pos):
    tmp = Node(val)

    if pos == 1:
        tmp.next = head
        return tmp

    curr = head

    for _ in range(pos - 2):
        if curr is None:
            return head
        curr = curr.next

    tmp.next = curr.next
    curr.next = tmp

    return head


def traversal(head):
    curr = head
    while curr:
        print(curr.key, end=" -> ")
        curr = curr.next
    print("None")


tmp_1 = insert_at_beginning(tmp_1, new_val)
traversal(tmp_1)

tmp_1 = insert_at_end(tmp_1, new_val)
traversal(tmp_1)

tmp_1 = insert(tmp_1, new_val, 5)
traversal(tmp_1)

# insertion in sorted linked list
def insert_in_sorted(head, val):
    tmp = Node(val)
    if head is None:
        return tmp
    
    if head.key > val:
        tmp.next = head
        return tmp
    
    curr = head
    while curr.next != None and curr.next.key < val:
        curr = curr.next
    
    tmp.next = curr.next
    curr.next = tmp

    return head