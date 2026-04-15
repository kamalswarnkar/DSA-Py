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

def printList(head):
    curr = head

    while(curr != None):
        print(curr.key, end="->")
        curr = curr.next

# def reverse_I(head): # using stack
#     stack = []
#     curr = head

#     while curr is not None:
#         stack.append(curr.key)
#         curr = curr.next
    
#     curr = head

#     while curr is not None:
#         curr.key = stack.pop()
#         curr = curr.next
    
#     return head

# def reverse_II(head):
#     prev = None
#     curr = head

#     while curr:
#         next = curr.next
#         curr.next = prev
#         prev = curr
#         curr = next
    
#     return prev

# def reverse_III(head): # using recursion
#     if head == None or head.next == None:
#         return head
    
#     rest_head = reverse_III(head.next)
#     rest_tail = head.next
#     rest_tail.next = head
#     head.next = None

#     return rest_head

def reverse_IV(curr, prev = None): # using tail recursion
    if curr == None:
        return prev
    
    next = curr.next
    curr.next = prev
    
    return reverse_IV(next, curr)

