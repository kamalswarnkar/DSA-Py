"""pairwise swapping in linked list 
where every two element in a continuous 
pair will be swapped with each other"""

def pairwise_swap(head):
    if head == None or head.next == None:
        return head
    
    prev = head
    curr = head.next.next
    head = head.next
    head.next = prev

    while curr and curr.next:
        prev.next = curr.next
        prev = curr
        next = curr.next.next
        curr.next.next = curr
        curr = next
    
    prev.next = curr

    return head

    