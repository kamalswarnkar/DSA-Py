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

# deleting head from LL
def delete_head_I(head):
    if head == None or head.next == head:
        return None
    
    start = head
    curr = head.next

    while curr.next != start:
        curr = curr.next
    
    curr.next = start.next

    return curr.next

# efficient method O(1)

def delete_head_II(head):
    if head == None or head.next == head:
        return None
    
    head.key = head.next.key
    head.next = head.next.next

    return head

# deleting the Kth node in LL

def delete_node(head, k):
    if head == None or head.next == head:
        return None
        """
        if there is only 1 node, and suppose k is 23, 
        even then also it will delete the only present node, 
        coz it is a circular one, every time k increse it will 
        always point to same node"""

    elif k == 1:
        return delete_head_II(head)
    
    curr = head

    for _ in range(k - 2):
        curr = curr.next

    curr.next = curr.next.next

    return head