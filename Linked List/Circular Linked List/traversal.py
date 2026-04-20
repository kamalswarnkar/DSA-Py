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
tmp_10.next = tmp_1

def printList(head):
    start = head
    curr = head.next

    print(start.key, end="→")
    
    while curr != start:
        print(curr.key, end="→")
        curr = curr.next
    
    print(curr.key, end="→")

printList(tmp_1)