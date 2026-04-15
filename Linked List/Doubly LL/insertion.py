class Node:
    def __init__(self, key):
        self.key = key
        self.prev = None
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
tmp_2.prev = tmp_1
tmp_2.next = tmp_3
tmp_3.prev = tmp_2
tmp_3.next = tmp_4
tmp_4.prev = tmp_3
tmp_4.next = tmp_5
tmp_5.prev = tmp_4
tmp_5.next = tmp_6
tmp_6.prev = tmp_5
tmp_6.next = tmp_7
tmp_7.prev = tmp_6
tmp_7.next = tmp_8
tmp_8.prev = tmp_7
tmp_8.next = tmp_9
tmp_9.prev = tmp_8
tmp_9.next = tmp_10
tmp_10.prev = tmp_9

def printList(head):
    curr = head

    while curr is not None:
        print(curr.key, end=" ⇆ ")
        curr = curr.next

val = 45

# insert at beginning
def insert_at_beginning(head, val):
    tmp = Node(val)

    if head != None:
        head.prev = tmp
    
    tmp.next = head

    return tmp

printList(insert_at_beginning(tmp_1, val))