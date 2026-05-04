def reverse(head):
    if head is None or head.next is None:
        return head

    prev = None
    curr = head

    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    
    return prev

def is_Palindrome(head):
    if head is None:
        return None
    
    if head.next is None:
        return True
    
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    if fast:
        slow = slow.next # skipping middle one in case of odd length of linked list
    
    second_half = reverse(slow)
    tmp = second_half
    curr = head

    while tmp:
        if curr.data != tmp.data:
            return False
        
        curr = curr.next
        tmp = tmp.next
    
    return True