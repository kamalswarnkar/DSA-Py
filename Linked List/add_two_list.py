"""
You are given the head of two singly linked lists head1 and head2 
representing two non-negative integers. You have to return the head 
of the linked list representing the sum of these two numbers.

Note: There can be leading zeros in the input lists, but there should not be any leading zeros in the output list.
"""

# my initial failed approach
class Node:
    def __init__(self, key):
        self.key = key
        self.next = None

def addTwoLists(head1, head2):
    num1 = 0
    num2 = 0
    
    curr = head1
    while curr:
        num1 = num1 * 10 + curr.data
        curr = curr.next
    
    curr = head2
    while curr:
        num2 = num2 * 10 + curr.data
        curr = curr.next
    
    res = num1 + num2
    
    # Edge case
    if res == 0:
        return Node(0)
    
    rev = []
    while res > 0:
        rev.append(res % 10)
        res //= 10
    
    head = Node(rev[-1])
    curr = head
    
    for i in range(len(rev) - 2, -1, -1):
        curr.next = Node(rev[i])
        curr = curr.next
    
    return head

# efficient and optimal approachF
def reverse(head):
    prev = None
    curr = head
        
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
            
    return prev
    
def remove_leading_zeros(head):
    while head and head.data == 0 and head.next:
        head = head.next
        
    return head
    
def addTwoLists(head1, head2):
    head1 = reverse(head1)
    head2 = reverse(head2)
        
    carry = 0
    dummy = Node(0)
    curr = dummy
        
    while head1 or head2 or carry:
        sum_val = carry
            
        if head1:
            sum_val += head1.data
            head1 = head1.next
            
        if head2:
            sum_val += head2.data
            head2 = head2.next
                
        carry = sum_val // 10
        curr.next = Node(sum_val % 10)
        curr = curr.next
        
    res = reverse(dummy.next)
    return remove_leading_zeros(res)